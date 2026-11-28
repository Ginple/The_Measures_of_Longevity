"""English glossary (B1 working list) against KERNEL, the ledger and the chapter map. Bookkeeping only."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOSSARY = ROOT / 'books/manuscript/en/GLOSSARY_EN.md'
KERNEL = (ROOT / 'knowledge_base/KERNEL.md').read_text(encoding='utf-8')
LEDGER = (ROOT / 'knowledge_base/CLAIM_LEDGER.md').read_text(encoding='utf-8')


def rows():
    out = []
    for line in GLOSSARY.read_text(encoding='utf-8').splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if line.startswith('|') and len(cells) == 6 and cells[0] not in ('Term',) and not set(cells[0]) <= set('-: '):
            out.append(dict(zip(['term', 'zh', 'meaning', 'owner', 'not', 'anchor'], cells)))
    return out


class GlossaryTest(unittest.TestCase):
    def setUp(self):
        self.rows = rows()

    def test_has_entries_and_unique_terms(self):
        terms = [r['term'] for r in self.rows]
        self.assertGreaterEqual(len(terms), 25)
        self.assertEqual(len(terms), len(set(terms)))

    def test_kernel_anchored_chinese_terms_exist_in_kernel(self):
        for r in self.rows:
            if 'KERNEL' not in r['anchor'] or r['zh'] in ('—', ''):
                continue
            m = re.search(r'KERNEL form: ([^)]+)\)', r['anchor'])
            with self.subTest(term=r['term']):
                self.assertIn(m.group(1) if m else r['zh'], KERNEL)

    def test_cited_ledger_ids_exist(self):
        have = set(re.findall(r'^\| (X\d+) \|', LEDGER, re.M))
        for r in self.rows:
            for a, b in re.findall(r'X(\d+)(?:–X(\d+))?', r['anchor']):
                ids = range(int(a), int(b or a) + 1)
                for i in ids:
                    with self.subTest(term=r['term'], id=i):
                        self.assertIn(f'X{i}', have)

    def test_owner_chapters_are_real(self):
        for r in self.rows:
            for n in re.findall(r'\d+', r['owner']):
                self.assertTrue(1 <= int(n) <= 33, (r['term'], n))

    def test_four_measures_match_kernel_and_chapter_titles(self):
        titles = {c['n']: c['title_en'] for c in json.loads((ROOT / 'books/manuscript/outline_v1.json').read_text(encoding='utf-8'))['chapters']}
        by_term = {r['term']: r for r in self.rows}
        for term, zh, ch in [('level', '水平', 6), ('rate', '速率', 7), ('recovery', '恢复', 8), ('reserve', '余量', 9)]:
            with self.subTest(term=term):
                self.assertEqual(by_term[term]['zh'], zh)
                self.assertEqual(by_term[term]['owner'], str(ch))
                self.assertIn(term.capitalize(), titles[ch])
        self.assertIn('**reserve**', KERNEL)

    def test_english_drafts_avoid_deprecated_reserve_term(self):
        for p in (ROOT / 'books/manuscript/en').glob('CH*_draft_en.md'):
            with self.subTest(file=p.name):
                self.assertNotRegex(p.read_text(encoding='utf-8').lower(), r'\bmargins?\b')


if __name__ == '__main__':
    unittest.main()

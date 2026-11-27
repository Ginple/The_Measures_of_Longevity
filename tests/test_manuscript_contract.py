"""Mechanical safeguards for selected draft files, not scientific review."""
from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (
    ROOT / 'books/manuscript/CH01_长寿的五个问题_示范稿.md',
    ROOT / 'books/manuscript/CH15_测量合同_示范稿.md',
    ROOT / 'books/manuscript/CH19_谁替谁维护_示范稿.md',
    ROOT / 'books/manuscript/CH20_平均不等于及时_示范稿.md',
    ROOT / 'books/manuscript/CH21_有余量却用不上_示范稿.md',
)


class ManuscriptDraftContractTest(unittest.TestCase):
    def test_footnote_references_match_unique_definitions(self):
        for path in CHAPTERS:
            with self.subTest(path=path.name):
                text = path.read_text(encoding='utf-8')
                definitions = re.findall(r'^\[\^([^\]]+)\]:', text, re.MULTILINE)
                body = re.sub(r'^\[\^[^\]]+\]:.*$', '', text, flags=re.MULTILINE)
                references = re.findall(r'\[\^([^\]]+)\]', body)
                self.assertTrue(references)
                self.assertEqual(set(references), set(definitions))
                self.assertTrue(all(count == 1 for count in Counter(definitions).values()))

    def test_draft_status_and_contract_present(self):
        for path in CHAPTERS:
            with self.subTest(path=path.name):
                text = path.read_text(encoding='utf-8')
                self.assertIn('示范稿', text)
                self.assertIn('独立外审未开展', text)
                self.assertIn('编辑用证据契约', text)
                self.assertIn('变更影响', text)
                self.assertIn('未决', text)

    def test_readme_links_to_all_selected_drafts(self):
        readme = (ROOT / 'books/manuscript/README.md').read_text(encoding='utf-8')
        for path in CHAPTERS:
            with self.subTest(path=path.name):
                self.assertIn(f']({path.name})', readme)


if __name__ == '__main__':
    unittest.main()

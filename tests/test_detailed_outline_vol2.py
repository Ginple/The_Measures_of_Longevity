"""Volume II detailed outline: the audit agent's Volume I outline checks (A15-A18, A20) applied to chapters 10-22.

Bookkeeping only. It does not judge whether the outline is a good plan.
"""
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import restructure_audit_agent as agent  # noqa: E402

VOL2 = ROOT / 'books/manuscript/en/DETAILED_OUTLINE_VOL2.md'
SPEC = ROOT / 'books/manuscript/en/DETAILED_OUTLINE_SPEC.md'
LEDGER = ROOT / 'knowledge_base/CLAIM_LEDGER.md'


class Vol2OutlineTest(unittest.TestCase):
    def setUp(self):
        self.text = VOL2.read_text(encoding='utf-8')
        self.secs = agent.outline_sections(self.text)
        spec = SPEC.read_text(encoding='utf-8')
        self.own_rows = [r for r in agent.table_rows(spec) if len(r) == 3 and r[0] != 'Concept, invariant or case']

    def test_covers_chapters_10_to_22(self):
        self.assertEqual(sorted(k for k in self.secs if isinstance(k, int)), list(range(10, 23)))

    def test_every_chapter_has_required_fields(self):
        for k in range(10, 23):
            fields = self.secs[k]
            with self.subTest(chapter=k):
                for f in agent.REQUIRED_FIELDS:
                    self.assertTrue(any(x.startswith(f) for x in fields), f)
                self.assertTrue(any(x.startswith(('Gaps', 'Source state')) for x in fields))
                self.assertTrue(fields.get('Strongest counterexample', '').strip())

    def test_cited_ledger_ids_exist(self):
        have = set(re.findall(r'^\| (X\d+) \|', LEDGER.read_text(encoding='utf-8'), re.M))
        cited = set(re.findall(r'\bX\d{2,3}\b', self.text))
        self.assertTrue(cited)
        self.assertEqual(sorted(cited - have), [])

    def test_owned_invariants_match_spec_owners(self):
        owned = {}
        for k in range(10, 23):
            for inv in re.findall(r'\bI(\d{1,2})\b', self.secs[k].get('Owns', '')):
                row = next((r for r in self.own_rows if re.search(rf'\bI{inv}\b', r[0])), None)
                with self.subTest(chapter=k, invariant=inv):
                    self.assertIsNotNone(row)
                    self.assertIn(str(k), re.findall(r'\d+', row[1]))
                owned[f'I{inv}'] = k
        # Every Volume II invariant in the spec is owned by its chapter in this outline.
        self.assertEqual(owned, {'I3': 13, 'I10': 14, 'I2': 15, 'I6': 15, 'I7': 16, 'I4': 17, 'I5': 21})

    def test_every_spec_concept_owned_in_vol2_is_listed_in_its_chapter(self):
        for concept, owner, _ in self.own_rows:
            nums = [int(n) for n in re.findall(r'\d+', owner)]
            if len(nums) == 1 and 10 <= nums[0] <= 22:
                self.assertTrue(self.secs[nums[0]].get('Owns', '').strip(), concept)

    def test_no_banned_novelty_words_and_leads_are_flagged(self):
        for w in agent.BANNED:
            self.assertNotIn(w, self.text)
        self.assertIn('not yet ledger entries', self.text)
        self.assertIn('(conditional, DEC-012)', self.text)


if __name__ == '__main__':
    unittest.main()

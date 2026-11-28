"""docs/TOOL_STATUS.tsv must list every tools/*.py honestly (CGEE R5.5 section 2.3)."""
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'planned', 'implemented', 'tested', 'verified'}


class ToolStatusTest(unittest.TestCase):
    def setUp(self):
        with open(ROOT / 'docs/TOOL_STATUS.tsv', encoding='utf-8', newline='') as f:
            self.rows = list(csv.DictReader(f, delimiter='\t'))

    def test_every_tool_is_registered_once(self):
        listed = [r['path'] for r in self.rows]
        actual = sorted(f'tools/{p.name}' for p in (ROOT / 'tools').glob('*.py'))
        self.assertEqual(sorted(listed), actual)

    def test_status_vocabulary_and_evidence(self):
        for r in self.rows:
            self.assertIn(r['status'], STATUSES, r['path'])
            if r['status'] in ('tested', 'verified'):
                tests = [t.strip() for t in r['last_receipt'].replace(';', ' ').split() if t.startswith('tests/')]
                self.assertTrue(tests, f"{r['path']} claims {r['status']} without a test file")
                for t in tests:
                    self.assertTrue((ROOT / t).is_file(), t)

    def test_only_tested_tools_may_block(self):
        # A tool below 'tested' must not be presented as blocking anything.
        for r in self.rows:
            if r['status'] in ('planned', 'implemented'):
                self.assertTrue(r['blocks_ci'].startswith('no'), r['path'])

    def test_nothing_is_verified_yet(self):
        # 'verified' needs validation by someone other than the authoring agent; none exists (D05 open).
        self.assertEqual([r['path'] for r in self.rows if r['status'] == 'verified'], [])


if __name__ == '__main__':
    unittest.main()

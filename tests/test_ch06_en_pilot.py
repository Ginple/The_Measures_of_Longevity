"""DEC-016 English ch6 pilot (written English-first): bookkeeping checks, not scientific validation."""
from pathlib import Path
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import inspect_project  # noqa: E402

PILOT = ROOT / 'knowledge_base/pilots/ch06_level_en'
spec = importlib.util.spec_from_file_location('ch06_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch06EnglishPilotTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))

    def copy_artifacts(self, tmp):
        for art in self.data['artifacts']:
            dst = Path(tmp) / art['path']
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / art['path'], dst)

    def test_committed_record_is_clean_and_matches_builder(self):
        r = inspect_project(self.data, ROOT)
        self.assertTrue(r['schema_valid'])
        self.assertEqual(r['issues'], [])
        self.assertEqual(r['artifact_drift'], [])
        self.assertEqual(r['formal_release_record_check'], 'blocked')
        self.assertEqual(self.data['reviews'], [])
        self.assertEqual(self.data, builder.build(), 'project.json differs from builder: rebind deliberately')

    def test_chapter_edit_makes_claims_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            with (Path(tmp) / builder.EN_PATH).open('a', encoding='utf-8') as f:
                f.write('\nAn unreviewed new sentence.\n')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-CH6-EN', r['artifact_drift'])
        self.assertTrue({c['id'] for c in self.data['claims']} <= set(r['stale_nodes']))

    def test_excerpt_edit_makes_dependent_claim_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            path = next(a['path'] for a in self.data['artifacts'] if a['id'] == 'A-COMP')
            p = Path(tmp) / path
            p.write_text(p.read_text(encoding='utf-8').replace('up to 53%', 'up to 35%'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-COMP', r['artifact_drift'])
        self.assertIn('CH6-EN-C004', r['stale_nodes'])

    def test_numbers_in_english_text_match_quoted_sources(self):
        claims = {c['id']: c['text'] for c in self.data['claims']}
        ev = {e['id']: e['text'] for e in self.data['evidence']}
        for cid, token, eid, source_token in [
            ('CH6-EN-C001', 'up to 9 years', 'E-HC-9Y', 'up to 9 years'),
            ('CH6-EN-C001', 'within 1.5 years', 'E-HC-PC', 'within 1.5 years'),
            ('CH6-EN-C001', 'between 0.9 and 2.4 years', 'E-BOR-RETEST', '0.9 and 2.4 years'),
            ('CH6-EN-C001', 'between 0.3 and 0.8 years', 'E-BOR-PC', '0.3–0.8 years'),
            ('CH6-EN-C001', '350 blood DNA samples', 'E-SUG-350', '350 blood DNA samples'),
            ('CH6-EN-C003', '38 sex-specific clocks across 15 organ systems', 'E-SEX-38', '38 sex-specific biological aging clocks across 15 organ systems'),
            ('CH6-EN-C004', '4,058 samples', 'E-COMP-4058', '4,058 samples'),
            ('CH6-EN-C004', 'up to 53 percent', 'E-COMP-53', 'up to 53%'),
            ('CH6-EN-C004', 'up to 21 percent', 'E-COMP-21', 'up to 21%'),
            ('CH6-EN-C004', '18,859 people', 'E-COMP-18859', '18,859 individuals'),
            ('CH6-EN-C005', '2,916 plasma proteins in 44,498 people', 'E-ORG-N', '(2,916 proteins) from 44,498'),
            ('CH6-EN-C005', 'hazard ratio of 8.3', 'E-ORG-HR', 'HR = 8.3'),
            ('CH6-EN-C006', '743,019 people', 'E-TEL-N', '743,019 individuals'),
            ('CH6-EN-C006', 'from minus 0.22 to minus 0.15', 'E-TEL-R', '-0.22 to -0.15'),
            ('CH6-EN-C007', '91.7 against 89.8', 'E-SR-LE', '89.75'),
            ('CH6-EN-C008', 'between 44 and 53 percent', 'E-COMP-RANGE', '44–53%'),
            ('CH6-EN-C008', '26 percent', 'E-COMP-RANGE', '26% was explained'),
            ('CH6-EN-C008', 'from 1 percent for one clock to 6 percent', 'E-COMP-MORT', 'from 1% for Horvath to 6% for PhenoAge'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, claims[cid])
                self.assertIn(source_token, ev[eid])

    def test_conflict_of_interest_is_disclosed_in_text(self):
        self.assertIn('Elysium Health', {c['id']: c['text'] for c in self.data['claims']}['CH6-EN-C002'])


if __name__ == '__main__':
    unittest.main()

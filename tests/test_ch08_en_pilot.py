"""DEC-016 English ch8 pilot (written English-first): bookkeeping checks, not scientific validation."""
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

PILOT = ROOT / 'knowledge_base/pilots/ch08_recovery_en'
spec = importlib.util.spec_from_file_location('ch08_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch08EnglishPilotTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))
        self.claims = {c['id']: c['text'] for c in self.data['claims']}
        self.ev = {e['id']: e['text'] for e in self.data['evidence']}

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
        self.assertIn('A-CH8-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_memo_edit_makes_formal_claim_stale_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / 'knowledge_base/experiments/SR_SNAPSHOT_IDENTIFIABILITY_2026-11-27.md'
            p.write_text(p.read_text(encoding='utf-8').replace('0.137/年', '0.173/年'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-SR', r['artifact_drift'])
        self.assertIn('CH8-EN-C008', r['stale_nodes'])
        self.assertNotIn('CH8-EN-C003', r['stale_nodes'])

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH8-EN-C002', 'only two studies', 'E-MAN-TWO', 'Only two studies'),
            ('CH8-EN-C003', '4,475 participants', 'E-HRR-N', '4475 participants'),
            ('CH8-EN-C003', 'mean follow-up of 4.3 years, 138 died', 'E-HRR-FU', '4.3 years served as the primary end point (n=138)'),
            ('CH8-EN-C003', 'by 6 percent', 'E-HRR-6', 'by 6%'),
            ('CH8-EN-C003', '69 people in the slowest quarter died, against 14', 'E-HRR-Q', 'Sixty-nine participants in the slowest HRR quartile died during the observation period compared with 14'),
            ('CH8-EN-C003', '2.3 times', 'E-HRR-Q', '2.3×'),
            ('CH8-EN-C004', '1,120 adults over 50', 'E-OGTT-N', '1,120 adults older than 50'),
            ('CH8-EN-C004', '36 percent', 'E-OGTT-36', '36%'),
            ('CH8-EN-C005', '1993 and 1998', 'E-HOSP-POP', '1993-1998'),
            ('CH8-EN-C005', '41.3 percent had died, 28.6 percent', 'E-HOSP-NEW', '41.3% died, 28.6%'),
            ('CH8-EN-C005', '30.1 percent', 'E-HOSP-NEW', '30.1%'),
            ('CH8-EN-C005', '17.8 percent had died and 67 percent', 'E-HOSP-BASE', '17.8% died'),
            ('CH8-EN-C006', 'between 120 and 150 years', 'E-PYR-EXTRAP', '120 - 150 years'),
            ('CH8-EN-C007', '1,961 adults', 'E-STEP-DESIGN', '1961 adults'),
            ('CH8-EN-C007', 'for 68 weeks', 'E-STEP-DESIGN', '68 weeks'),
            ('CH8-EN-C007', '327 participants', 'E-STEP-327', '327 participants'),
            ('CH8-EN-C007', '17.3 percent', 'E-STEP-LOSS', '17.3%'),
            ('CH8-EN-C007', '11.6 percentage points by week 120', 'E-STEP-REGAIN', '11.6 (SD: 7.7)'),
            ('CH8-EN-C007', 'net loss of 5.6 percent', 'E-STEP-REGAIN', 'net losses of 5.6%'),
            ('CH8-EN-C008', '0.137 against 0.114 per year', 'E-SR-LAMBDA', '0.137/年，产生组 0.114/年'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_extrapolation_never_called_a_limit_in_the_book_voice(self):
        text = (ROOT / builder.EN_PATH).read_text(encoding='utf-8')
        self.assertIn('never "a lifespan limit"', text)
        self.assertNotRegex(text.lower(), r'(150-year limit|lifespan limit of 1[25]0)')

    def test_declared_conflicts_are_disclosed_in_text(self):
        self.assertIn('employees of the company that funded the study', self.claims['CH8-EN-C006'])
        self.assertIn("employees of the drug's manufacturer", self.claims['CH8-EN-C007'])


if __name__ == '__main__':
    unittest.main()

"""DEC-016 English ch7 pilot (written English-first): bookkeeping checks, not scientific validation."""
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

PILOT = ROOT / 'knowledge_base/pilots/ch07_rate_en'
spec = importlib.util.spec_from_file_location('ch07_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch07EnglishPilotTest(unittest.TestCase):
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
        self.assertIn('A-CH7-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_code_snapshot_edit_makes_software_claim_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            path = next(a['path'] for a in self.data['artifacts'] if a['id'] == 'A-PACECODE')
            p = Path(tmp) / path
            p.write_text(p.read_text(encoding='utf-8').replace('<- 0.7', '<- 0.6'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-PACECODE', r['artifact_drift'])
        self.assertIn('CH7-EN-C010', r['stale_nodes'])
        self.assertNotIn('CH7-EN-C001', r['stale_nodes'])

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH7-EN-C001', '954 members', 'E-DUN-954', '954 young humans'),
            ('CH7-EN-C002', 'about 23 base pairs per year', 'E-TEL-BP', '-23 bp/year in cross-sectional'),
            ('CH7-EN-C002', 'about 38 base pairs per year', 'E-TEL-BP', '-38 bp/year in longitudinal'),
            ('CH7-EN-C002', 'until around age 50', 'E-TEL-NONLIN', 'until around age 50'),
            ('CH7-EN-C003', '375 women and 435 men aged 21 to 87', 'E-VO2-N', '375 women and 435 men ages 21 to 87'),
            ('CH7-EN-C003', 'median of 7.9 years', 'E-VO2-N', 'median follow-up period of 7.9 years'),
            ('CH7-EN-C003', 'from 3 to 6 percent per ten years', 'E-VO2-RATE', 'from 3% to 6% per 10 years'),
            ('CH7-EN-C003', 'more than 20 percent per ten years', 'E-VO2-RATE', '>20% per 10 years'),
            ('CH7-EN-C004', '108 Californians aged 25 to 75', 'E-SHEN-N', '108 participants, aged between 25 years and 75 years'),
            ('CH7-EN-C004', 'median of 1.7 years and at most 6.8 years', 'E-SHEN-FU', 'median period of 1.7 years, with a maximum follow-up duration of 6.8 years'),
            ('CH7-EN-C004', 'roughly 44 and 60 years', 'E-SHEN-44', 'approximately 44 years and 60 years'),
            ('CH7-EN-C005', '3.8 million', 'E-PARK-N', '3.8 million'),
            ('CH7-EN-C005', '1,828 people aged 19 to 97', 'E-PARK-N', '1,828 individuals aged 19-97'),
            ('CH7-EN-C006', '19 indicators', 'E-PACE-19', '19 indicators'),
            ('CH7-EN-C006', 'four visits spanning two decades', 'E-PACE-19', 'four time points spanning two decades'),
            ('CH7-EN-C007', '220 adults without obesity', 'E-CAL-220', '220 adults without obesity'),
            ('CH7-EN-C007', '25 percent reduction', 'E-CAL-220', '25% CR'),
            ('CH7-EN-C008', '51 public and private', 'E-TA-51', '51 public and private'),
            ('CH7-EN-C008', '16 prominent epigenetic clocks and 94 other', 'E-TA-51', '16 prominent epigenetic clocks for each study, along with 94 other'),
            ('CH7-EN-C009', 'Across 18 methylation-based', 'E-REL-18', 'across 18 DNA methylation-based'),
            ('CH7-EN-C010', 'by default, 80 percent', 'E-CODE-PARAM', '(default: 0.8)'),
            ('CH7-EN-C010', 'from 80 to 70 percent', 'E-CODE-V2', '0.7'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_declared_conflicts_are_disclosed_in_text(self):
        self.assertIn('inventors', self.claims['CH7-EN-C006'])
        self.assertIn('inventors of DunedinPACE', self.claims['CH7-EN-C007'])
        self.assertIn('employees of TruDiagnostic', self.claims['CH7-EN-C008'])
        self.assertIn('co-inventors', self.ev['E-TA-COI'])

    def test_no_surrogate_claim_for_any_clock(self):
        text = (ROOT / builder.EN_PATH).read_text(encoding='utf-8')
        self.assertIn('The second has not been shown for any methylation clock.', text)
        self.assertNotRegex(text.lower(), r'\b(validated surrogate endpoint for aging|proven to slow aging)\b')


if __name__ == '__main__':
    unittest.main()

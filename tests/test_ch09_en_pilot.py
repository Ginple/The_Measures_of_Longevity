"""DEC-016 English ch9 pilot (written English-first): bookkeeping checks, not scientific validation."""
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

PILOT = ROOT / 'knowledge_base/pilots/ch09_reserve_en'
spec = importlib.util.spec_from_file_location('ch09_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch09EnglishPilotTest(unittest.TestCase):
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
        self.assertIn('A-CH9-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_saved_synthetic_output_matches_script(self):
        spec = importlib.util.spec_from_file_location('margin_ttt', ROOT / 'knowledge_base/experiments/margin_time_to_threshold.py')
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        saved = json.loads((PILOT / 'evidence/RESERVE_SYNTHETIC_output.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, json.loads(json.dumps(m.run(), ensure_ascii=False)))

    def test_output_edit_makes_formal_claims_stale_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'RESERVE_SYNTHETIC_output.json'
            p.write_text(p.read_text(encoding='utf-8').replace('14.7', '17.4'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-RES-OUT', r['artifact_drift'])
        self.assertTrue({'CH9-EN-C007', 'CH9-EN-C008', 'CH9-EN-C009'} <= set(r['stale_nodes']))
        self.assertNotIn('CH9-EN-C004', r['stale_nodes'])

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH9-EN-C002', '15 healthy young adults with a median age of 26', 'E-REN-N', '15 healthy normotensive subjects of young age'),
            ('CH9-EN-C002', '10 healthy older adults with a median age of 70', 'E-REN-N', 'median age, 70 yr'),
            ('CH9-EN-C002', '102 against 122', 'E-REN-REST', '(102 and 339 mL/min per 1.73 m2) than in the young subjects (122'),
            ('CH9-EN-C002', 'reached 118 in the older group and 146', 'E-REN-LOAD', 'was 118 mL/min per 1.73 m2 (range, 98 to 137) in the elderly and 146'),
            ('CH9-EN-C004', '298 people aged 55 to 86, 152 men and 146 women', 'E-PAT-N', '298 subjects (152 men and 146 women), aged 55-86'),
            ('CH9-EN-C004', 'at most 37 percent', 'E-PAT-37', 'at most 37%'),
            ('CH9-EN-C004', '0.31 units per year in men and 0.25', 'E-PAT-SLOPE', '(0.31 mL x kg(-1) x min(-1) x yr(-1)) and women (0.25)'),
            ('CH9-EN-C004', 'approximately 18 mL/kg/min in men and 15', 'E-PAT-THRESH', 'approximately 18 mL x kg(-1) x min(-1) in men and 15'),
            ('CH9-EN-C005', 'around 80 to 85 years', 'E-SHE-THRESH', 'reached at 80-85 years'),
            ('CH9-EN-C005', 'by 10 or more years', 'E-SHE-10', 'by 10 or more years'),
            ('CH9-EN-C006', 'same 810 people', 'E-FLEG-N', '375 women and 435 men'),
            ('CH9-EN-C006', 'from 3 to 6 percent per ten years', 'E-FLEG-ACC', 'from 3% to 6% per 10 years'),
            ('CH9-EN-C006', 'more than 20 percent per ten years', 'E-FLEG-ACC', '>20% per 10 years'),
            ('CH9-EN-C007', 'he has 22.6 years', 'E-RO-25', '"years_linear_cross_sectional": 22.6'),
            ('CH9-EN-C007', 'at most 14.7 years', 'E-RO-25', '"years_proportional_longitudinal_upper": 14.7'),
            ('CH9-EN-C007', 'are 6.5 and 4.7 years', 'E-RO-20', '"years_proportional_longitudinal_upper": 4.7'),
            ('CH9-EN-C008', 'adds 32.3 years', 'E-RO-PLUS10', '"years_linear": 32.3'),
            ('CH9-EN-C008', 'at most 15.1 years', 'E-RO-PLUS10', '"years_proportional_upper": 15.1'),
            ('CH9-EN-C009', 'the same 4.3 years', 'E-RO-25', '"gain_level_plus10pct": 4.3'),
            ('CH9-EN-C009', '1.6 years for the man starting at 25', 'E-RO-25', '"gain_rate_minus10pct": 1.6'),
            ('CH9-EN-C009', 'about half a year', 'E-RO-20', '"gain_rate_minus10pct": 0.5'),
            ('CH9-EN-C009', 'about 38 years away', 'E-RO-CROSS', '38.4'),
            ('CH9-EN-C010', '302,467 people', 'E-TRAJ-N', '302 467 home care recipients'),
            ('CH9-EN-C010', 'median age of 81', 'E-TRAJ-N', 'median age of 81 years'),
            ('CH9-EN-C010', 'five distinct trajectories', 'E-TRAJ-5', 'Five distinct IC trajectories'),
            ('CH9-EN-C010', '48.4 percent against 38.1 percent', 'E-TRAJ-LTC', '48.4% vs 38.1%'),
            ('CH9-EN-C011', '74.43 against 74.42 years', 'E-SR2-ROW', '**74.43 / 74.42**'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_secondhand_and_synthetic_labels_present(self):
        self.assertIn('this description is secondhand', self.claims['CH9-EN-C001'])
        for cid in ('CH9-EN-C007', 'CH9-EN-C009'):
            self.assertRegex(self.claims[cid], r'synthetic')
        self.assertIn('should be read as the effect of training', self.claims['CH9-EN-C008'])
        text = (ROOT / builder.EN_PATH).read_text(encoding='utf-8')
        self.assertNotRegex(text.lower(), r'training (adds|extends|buys) \d')


if __name__ == '__main__':
    unittest.main()

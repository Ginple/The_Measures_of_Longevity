"""DEC-016 English ch1 pilot: bookkeeping checks, not scientific validation."""
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

PILOT = ROOT / 'knowledge_base/pilots/ch01_measure_en'
spec = importlib.util.spec_from_file_location('ch01_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
lt_spec = importlib.util.spec_from_file_location('ch01_life_table', PILOT / 'synthetic_life_table.py')
life_table = importlib.util.module_from_spec(lt_spec)
lt_spec.loader.exec_module(life_table)


class Ch01EnglishPilotTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))
        self.claims = {c['id']: c['text'] for c in self.data['claims']}
        self.ev = {e['id']: e['text'] for e in self.data['evidence']}
        self.text = (ROOT / builder.EN_PATH).read_text(encoding='utf-8')

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
        self.assertIn('A-CH1-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_saved_synthetic_output_matches_script(self):
        saved = json.loads((PILOT / 'evidence/LIFE_TABLE_SYNTHETIC_output.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, life_table.build())
        pops = saved['populations']
        self.assertEqual({p['life_expectancy'] for p in pops.values()}, {'18'})
        self.assertEqual({p['health_adjusted_life_expectancy'] for p in pops.values()}, {'15'})
        self.assertEqual(pops['A']['people_whose_loss_equals_gap'], 0)
        self.assertEqual(pops['B']['people_whose_loss_equals_gap'], 100)

    def test_output_edit_makes_formal_claim_stale_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'LIFE_TABLE_SYNTHETIC_output.json'
            p.write_text(p.read_text(encoding='utf-8').replace('"11": 20', '"12": 20'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-LT-OUT', r['artifact_drift'])
        self.assertIn('CH1-EN-C002', r['stale_nodes'])
        self.assertNotIn('CH1-EN-C005', r['stale_nodes'])

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH1-EN-C001', 'its 183 member states', 'E-GAP-183', 'The 183 WHO member states'),
            ('CH1-EN-C001', 'to 9.6 years', 'E-GAP-96', 'extending to 9.6 years'),
            ('CH1-EN-C001', '2.4 years wider', 'E-GAP-SEX', '2.4 (0.5) years wider than men'),
            ('CH1-EN-C001', 'at 12.4 years', 'E-GAP-US', 'amounting to 12.4 years'),
            ('CH1-EN-C002', 'either 1 or 3.5', 'E-LT-A', '"7/2": 80'),
            ('CH1-EN-C002', '80 people have 1 lost year and 20 have 11', 'E-LT-C', '"11": 20'),
            ('CH1-EN-C003', 'a target of 25 percent calorie restriction', 'E-CAL-220', 'randomized to 25% CR'),
            ('CH1-EN-C003', 'at 24 months', 'E-CAL-BMD', 'BMD at 24 months'),
            ('CH1-EN-C004', 'describes 220 randomized adults', 'E-CAL-220', 'n = 220 adults'),
            ('CH1-EN-C004', 'the bone report 218', 'E-CAL-218', 'Two-hundred eighteen'),
            ('CH1-EN-C005', '300 low-income adults aged 65 or older', 'E-CAP-DESIGN', '300 low-income community-dwelling adults'),
            ('CH1-EN-C005', 'up to ten home visits over five months', 'E-CAP-INT', 'up to 10 home visits over 5 months'),
            ('CH1-EN-C005', 'relative risk 0.70, 95 percent confidence interval 0.54 to 0.93', 'E-CAP-ADL', 'RR], 0.70; 95% CI, 0.54-0.93'),
            ('CH1-EN-C005', '(0.83, 0.65 to 1.06)', 'E-CAP-IADL', 'RR, 0.83; 95% CI, 0.65-1.06'),
            ('CH1-EN-C006', 'from 0 to 2 and the total ran from 0 to 16', 'E-CAP-RANGE', 'from 0 to 16 points'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_owned_concepts_and_guards(self):
        # Chapter 1 owns the three senses of "measure" and the book's five questions (VOL1, KERNEL section 2).
        for sense in ('**measurement**', '**the measure of what can be changed**', '**the measure of a life**'):
            self.assertIn(sense, self.text)
        for q in ('What is the extra time?', 'Who, and what, is being maintained?', 'What is seen, and what is missed?',
                  'Is a change already a benefit?', 'Who decides what is worth it?'):
            self.assertEqual(self.text.count(f'**{q}**'), 1, q)
        self.assertIn('deserves to be granted in full', self.text)  # strongest counterexample (VOL1)
        self.assertIn('synthetic calculation, built by this project with no real data', self.claims['CH1-EN-C002'])
        self.assertIn('not three confirmations', self.claims['CH1-EN-C004'])
        self.assertIn('not a 30 percent lower risk of any event', self.claims['CH1-EN-C006'])
        lowered = self.text.lower()
        for banned in ('slows aging', 'reverses aging', 'adds years to your life', 'proven to extend'):
            self.assertNotIn(banned, lowered)


if __name__ == '__main__':
    unittest.main()

"""DEC-016 English ch2 pilot: bookkeeping checks, not scientific validation."""
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

PILOT = ROOT / 'knowledge_base/pilots/ch02_clocks_en'
spec = importlib.util.spec_from_file_location('ch02_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
pc_spec = importlib.util.spec_from_file_location('ch02_period_cohort', PILOT / 'period_cohort.py')
period_cohort = importlib.util.module_from_spec(pc_spec)
pc_spec.loader.exec_module(period_cohort)


class Ch02EnglishPilotTest(unittest.TestCase):
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
        self.assertIn('A-CH2-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_saved_synthetic_output_matches_script(self):
        saved = json.loads((PILOT / 'evidence/PERIOD_COHORT_SYNTHETIC_output.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, json.loads(json.dumps(period_cohort.build())))
        # Cohort life expectancy exceeds period life expectancy when death rates fall over calendar time.
        self.assertGreater(saved['cohort_born_year0']['life_expectancy'], saved['period_year0']['life_expectancy'])
        tails = saved['tail_given_alive_at_105']
        for k in ('reach_110', 'reach_115', 'reach_122'):
            self.assertGreater(tails['hazard_flat_after_105'][k], tails['hazard_keeps_rising'][k])

    def test_output_edit_makes_formal_claims_stale_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'PERIOD_COHORT_SYNTHETIC_output.json'
            p.write_text(p.read_text(encoding='utf-8').replace('80.8', '81.8'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-PC-OUT', r['artifact_drift'])
        self.assertTrue({'CH2-EN-C001', 'CH2-EN-C007'} <= set(r['stale_nodes']))
        self.assertNotIn('CH2-EN-C006', r['stale_nodes'])

    def test_ledger_growth_does_not_stale_chapter(self):
        paths = {a['path'] for a in self.data['artifacts']}
        self.assertNotIn('knowledge_base/CLAIM_LEDGER.md', paths)

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH2-EN-C001', 'is 73.4 years', 'E-PC-PERIOD', '"life_expectancy": 73.4'),
            ('CH2-EN-C001', 'is 80.8 years, 7.4 years longer', 'E-PC-DIFF', '7.4'),
            ('CH2-EN-C001', 'a quarter have died by 66.4', 'E-PC-PERIOD', '"age_by_which_25pct_died": 66.4'),
            ('CH2-EN-C001', 'still alive at 82.9', 'E-PC-PERIOD', '"age_by_which_75pct_died": 82.9'),
            ('CH2-EN-C002', 'aged 18 to 65', 'E-W-SURVEY', 'participants aged 18-65 years'),
            ('CH2-EN-C002', 'from 0.033 to 0.215', 'E-W-REVISED', 'GBD 2010 0·033'),
            ('CH2-EN-C002', 'from 0.047 to 0.296', 'E-W-REVISED', 'GBD 2013 0·296'),
            ('CH2-EN-C003', '960 genetically diverse female mice', 'E-M-DESIGN', '960 genetically diverse female mice'),
            ('CH2-EN-C003', '40 percent calorie restriction', 'E-M-40', '40% caloric restriction'),
            ('CH2-EN-C004', 'for 183 member states', 'E-G-183', 'The 183 WHO member states'),
            ('CH2-EN-C004', 'globally to 9.6 years', 'E-G-96', 'extending to 9.6 years'),
            ('CH2-EN-C005', 'member states of 9.2 years', 'E-LED-X21', '183 会员国差值均值 9.2 年'),
            ('CH2-EN-C005', 'between 2000 and 2019 by 20', 'E-LED-X61', '(Estimate2019−Estimate2000)/20'),
            ('CH2-EN-C006', 'after age 100', 'E-L-DONG', 'tend to decline after age 100'),
            ('CH2-EN-C006', 'a total of 3,836 documented cases', 'E-L-BARBI-N', 'a total of 3836 documented cases'),
            ('CH2-EN-C006', 'essentially constant beyond age 105', 'E-L-BARBI-FLAT', 'essentially constant beyond age 105'),
            ('CH2-EN-C007', 'is 0.66', 'E-PC-Q105', '0.66'),
            ('CH2-EN-C007', 'about 1.6 in a hundred million', 'E-PC-TAIL', '"reach_115": 1.6e-08'),
            ('CH2-EN-C007', 'about 2.2 in a hundred thousand', 'E-PC-TAIL', '"reach_115": 2.2e-05'),
            ('CH2-EN-C007', 'some 1,400 times larger', 'E-PC-RATIO', '"reach_115": 1400.0'),
            ('CH2-EN-C007', 'about 710 billion', 'E-PC-RATIO', '"reach_122": 710000000000.0'),
            ('CH2-EN-C008', 'baseline of 1759 years to 156', 'E-L-EF-156', 'non-aging baseline of 1759 years to 156 years'),
            ('CH2-EN-C008', 'median lifespans of 146 to 194 years', 'E-L-EF-146', 'median lifespans of 146-194 years'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_owned_distinctions_and_guards(self):
        # Chapter 2 owns: three statistics kept apart; the gap; "limit" as a question about which statistic (VOL1).
        self.assertIn('Neither number is an appointment.', self.claims['CH2-EN-C001'])
        self.assertIn('built by this project with no real data', self.claims['CH2-EN-C001'])
        self.assertIn('not an age that no individual can exceed', self.claims['CH2-EN-C008'])
        self.assertIn('Here is the strongest case for healthy life expectancy as the single target', self.text)
        self.assertIn('Chapter 30 owns that argument', self.text)
        self.assertIn('which statistic the word "limit" is attached to', self.text)
        lowered = self.text.lower()
        for banned in ('the human limit is 122', 'there is no limit to human lifespan', 'you will live to',
                       'your life expectancy is'):
            self.assertNotIn(banned, lowered)
        # V7 tail figures for the mutation model are unchecked and must not appear in the body.
        body = self.text.split('**What this chapter does not settle:**')[0]
        for unchecked in ('557', '210', '134', '170'):
            self.assertNotIn(unchecked, body)


if __name__ == '__main__':
    unittest.main()

"""DEC-016 English ch3 pilot: bookkeeping checks, not scientific validation."""
from fractions import Fraction
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

PILOT = ROOT / 'knowledge_base/pilots/ch03_four_links_en'
spec = importlib.util.spec_from_file_location('ch03_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
cm_spec = importlib.util.spec_from_file_location('ch03_confounded_marker', PILOT / 'confounded_marker.py')
confounded_marker = importlib.util.module_from_spec(cm_spec)
cm_spec.loader.exec_module(confounded_marker)


class Ch03EnglishPilotTest(unittest.TestCase):
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
        self.assertIn('A-CH3-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_saved_synthetic_output_matches_script_and_hand_arithmetic(self):
        saved = json.loads((PILOT / 'evidence/CONFOUNDED_MARKER_SYNTHETIC_output.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, json.loads(json.dumps(confounded_marker.build())))
        # Independent hand arithmetic: 300 with Z, 700 without.
        high = 300 * Fraction(8, 10) + 700 * Fraction(2, 10)
        ev_high = 240 * Fraction(4, 10) + 140 * Fraction(1, 10)
        ev_low = 60 * Fraction(4, 10) + 560 * Fraction(1, 10)
        self.assertEqual((high, ev_high, ev_low), (380, 110, 80))
        # The marker predicts (risk ratio above 1) but setting it low changes nothing.
        self.assertGreater(float(saved['risk_ratio_high_vs_low']), 2)
        self.assertEqual(saved['events_without_treatment'], saved['events_with_marker_set_low'])

    def test_trial_excerpt_edit_stales_trial_claims_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'TRIALS_abstracts.txt'
            p.write_text(p.read_text(encoding='utf-8').replace('257 patients', '258 patients'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-TRIALS', r['artifact_drift'])
        self.assertTrue({'CH3-EN-C005', 'CH3-EN-C006', 'CH3-EN-C007', 'CH3-EN-C008', 'CH3-EN-C009'} <= set(r['stale_nodes']))
        for cid in ('CH3-EN-C001', 'CH3-EN-C002', 'CH3-EN-C004', 'CH3-EN-C010'):
            self.assertNotIn(cid, r['stale_nodes'])

    def test_ledger_growth_does_not_stale_chapter(self):
        paths = {a['path'] for a in self.data['artifacts']}
        self.assertNotIn('knowledge_base/CLAIM_LEDGER.md', paths)

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH3-EN-C004', 'Among the 380 people with a high marker, 110', 'E-CM-OUT', '"events_marker_high": 110'),
            ('CH3-EN-C004', 'a risk of 0.289', 'E-CM-OUT', '"risk_marker_high": "0.289"'),
            ('CH3-EN-C004', 'among the 620 with a low marker, 80', 'E-CM-OUT', '"events_marker_low": 80'),
            ('CH3-EN-C004', 'a risk ratio of 2.24', 'E-CM-OUT', '"risk_ratio_high_vs_low": "2.24"'),
            ('CH3-EN-C004', 'stays at 190', 'E-CM-OUT', '"events_with_marker_set_low": 190'),
            ('CH3-EN-C005', 'an odds ratio of 0.62', 'E-V-OBS', 'OR 0·62'),
            ('CH3-EN-C005', 'odds ratio 0.93, 95 percent interval 0.68 to 1.26', 'E-V-GEN', 'OR 0·93, 95% CI 0·68-1·26'),
            ('CH3-EN-C006', 'tested in 15,067 patients', 'E-T-N', '15,067 patients'),
            ('CH3-EN-C006', 'HDL cholesterol by 72.1 percent', 'E-T-LIPIDS', '72.1%'),
            ('CH3-EN-C006', 'LDL cholesterol by 24.9 percent', 'E-T-LIPIDS', '24.9%'),
            ('CH3-EN-C006', 'by 5.4 mm Hg', 'E-T-LIPIDS', '5.4 mm Hg'),
            ('CH3-EN-C006', 'hazard ratio 1.25', 'E-T-HR', 'hazard ratio, 1.25'),
            ('CH3-EN-C006', 'hazard ratio 1.58, 95 percent confidence interval 1.14 to 2.19', 'E-T-HR', '1.58; 95% CI, 1.14 to 2.19'),
            ('CH3-EN-C007', 'Of 1498 patients', 'E-C-N', 'Of 1498 patients'),
            ('CH3-EN-C007', 'a mean of 10 months, 43', 'E-C-DEATHS', 'mean follow-up of 10 months'),
            ('CH3-EN-C007', 'against 16 on placebo', 'E-C-DEATHS', '43 receiving drug vs. 16 receiving placebo'),
            ('CH3-EN-C008', 'assigned 10,251 patients', 'E-A-N', '10,251 patients'),
            ('CH3-EN-C008', 'below 6.0 percent', 'E-A-N', 'below 6.0%'),
            ('CH3-EN-C008', '7.0 to 7.9 percent', 'E-A-N', 'from 7.0 to 7.9%'),
            ('CH3-EN-C008', 'were 6.4 and 7.5 percent', 'E-A-ACHIEVED', '6.4% and 7.5%'),
            ('CH3-EN-C008', 'But 257 people died', 'E-A-DEATHS', '257 patients'),
            ('CH3-EN-C008', 'against 203', 'E-A-DEATHS', 'compared with 203'),
            ('CH3-EN-C008', 'hazard ratio 1.22, 95 percent interval 1.01 to 1.46', 'E-A-DEATHS', 'hazard ratio, 1.22; 95% CI, 1.01 to 1.46'),
            ('CH3-EN-C008', 'Over 3.5 years', 'E-A-CONC', 'for 3.5 years'),
            ('CH3-EN-C009', 'an odds ratio of 1.54', 'E-V-LDL', 'OR 1·54'),
            ('CH3-EN-C009', 'genetic one (2.13)', 'E-V-LDL', 'OR 2·13'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_owned_distinctions_and_guards(self):
        # Chapter 3 owns I1: explanation, prediction, control and benefit are separate steps (VOL1).
        self.assertIn('The book\'s first principle, which it calls I1, is that these are separate steps.', self.text)
        self.assertIn('built by this project with no real data', self.claims['CH3-EN-C004'])
        self.assertIn('a good enough mechanistic theory would collapse the four steps', self.text)
        self.assertIn('Chapter 18 treats these cases', self.text)
        self.assertIn('not as discoveries or new paradigms', self.text)
        self.assertIn('not as a first (ledger X85)', self.text)
        self.assertIn('ledger X28', self.text)
        lowered = self.text.lower()
        for banned in ('the correct theory of aging is', 'new paradigm:', 'we are the first', 'for the first time',
                       'you should take', 'you should stop'):
            self.assertNotIn(banned, lowered)
        # Full-text-only claims from the V6 corpus must not appear (not in the abstracts read).
        body = self.text.split('**What this chapter does not settle:**')[0]
        for unread in ('cannot yet be quantified', 'age-specific optimum'):
            self.assertNotIn(unread, body)


if __name__ == '__main__':
    unittest.main()

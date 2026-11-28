"""Every number or capitalised word in a bound English claim is either in its evidence or has been reviewed."""
from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('claim_token_scan', ROOT / 'tools/claim_token_scan.py')
cts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cts)
CODES = {'Y', 'X', 'S', 'A', 'H', 'M', 'W', 'E', 'P', 'D', 'C'}


class ClaimTokenScanTest(unittest.TestCase):
    def test_no_unreviewed_tokens(self):
        found = cts.scan()
        self.assertEqual(cts.unreviewed(found), {})
        self.assertEqual(cts.stale_reviews(found), {})

    def test_reason_codes_known(self):
        for cid, toks in cts.REVIEWED.items():
            for t, code in toks.items():
                self.assertIn(code, CODES, (cid, t))

    def test_removed_unsupported_words_stay_out(self):
        # The 2026-11-28 corrections: these words had no stored source.
        def body(p):  # skip the header blockquote, which records the corrections themselves
            lines = (ROOT / 'books/manuscript/en' / p).read_text(encoding='utf-8').split('\n')
            return '\n'.join(l for l in lines if not l.startswith('>'))
        text = {p: body(p) for p in
                ['CH06_level_draft_en.md', 'CH07_rate_draft_en.md', 'CH09_reserve_draft_en.md']}
        self.assertNotIn('4,058 people', text['CH06_level_draft_en.md'])
        self.assertNotIn('in New Zealand', text['CH07_rate_draft_en.md'])
        for w in ['A Canadian group', 'Canadian exercise physiologist', 'The Canadian study', 'Bernard Strehler', 'small German study', 'overnight amino']:
            self.assertNotIn(w, text['CH09_reserve_draft_en.md'], w)

    def test_scan_catches_a_planted_word(self):
        found = {'CH9-EN-C004': ['German', 'They']}
        self.assertEqual(cts.unreviewed(found), {'CH9-EN-C004': ['German']})


if __name__ == '__main__':
    unittest.main()

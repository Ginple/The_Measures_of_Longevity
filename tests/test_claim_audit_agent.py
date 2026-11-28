"""Contract tests for tools/claim_audit_agent.py (V1 claim audit agent, DEC-020)."""
import json
import shutil
import unittest

import claim_audit_agent as agent


class ClaimAuditAgentTest(unittest.TestCase):
    def test_current_tree_passes_every_check(self):
        scratch = agent.stage(agent.ROOT)
        try:
            res = agent.run_checks(scratch)
        finally:
            shutil.rmtree(scratch, ignore_errors=True)
        self.assertEqual([(r['id'], r['pilot'], r['detail']) for r in res if r['result'] != 'PASS'], [])
        self.assertEqual({r['pilot'] for r in res}, set(agent.PILOTS))
        self.assertGreaterEqual(len(res), 7 * len(agent.PILOTS) - 1)

    def test_every_mutation_is_detected(self):
        report = agent.self_test()
        self.assertGreaterEqual(len(report), 9)
        self.assertEqual({k: v for k, v in report.items() if v != 'DETECTED'}, {})

    def test_missing_input_fails_closed(self):
        scratch = agent.stage(agent.ROOT)
        try:
            (scratch / 'knowledge_base/pilots/ch10_routes_en/evidence/IMMUNE_SUPPORT_abstract.txt').unlink()
            with self.assertRaises(FileNotFoundError):
                agent.stage(scratch)
        finally:
            shutil.rmtree(scratch, ignore_errors=True)

    def test_every_english_pilot_is_covered(self):
        pilots = sorted(p.name for p in (agent.ROOT / 'knowledge_base/pilots').iterdir() if p.name.endswith('_en'))
        self.assertEqual(sorted(agent.PILOTS), pilots)

    def test_receipt_states_its_limits(self):
        receipt = json.loads(agent.OUT.read_text(encoding='utf-8'))
        self.assertIn('scientific verification', receipt['not'])
        self.assertIn('same assistant', receipt['independence'])
        self.assertEqual(receipt['failed'], [])

    def test_waived_review_debts_are_closed_but_release_stays_blocked(self):
        # DEC-020 closes the independent-review debts; it adds no review records, so release stays blocked.
        for p in agent.PILOTS:
            d = json.loads((agent.ROOT / f'knowledge_base/pilots/{p}/project.json').read_text(encoding='utf-8'))
            with self.subTest(pilot=p):
                rev = [x for x in d['debts'] if x['id'].endswith('INDEPENDENT-REVIEW')]
                self.assertEqual(len(rev), 1)
                self.assertEqual((rev[0]['status'], rev[0]['blocks_formal_release']), ('closed', False))
                self.assertIn('DEC-020', rev[0]['closure_evidence'])
                self.assertEqual(d['reviews'], [])
                self.assertTrue(any(x['blocks_formal_release'] and x['status'] != 'closed' for x in d['debts']))


if __name__ == '__main__':
    unittest.main()

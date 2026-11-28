"""Contract tests for tools/restructure_audit_agent.py (V1 audit agent for DEC-018).

Git-history checks (G01, G02) are skipped here because CI checkouts are shallow; run the tool locally for them.
"""
import shutil
import unittest

import restructure_audit_agent as agent


class RestructureAuditAgentTest(unittest.TestCase):
    def test_current_tree_has_no_failures_or_open_differences(self):
        scratch = agent.stage(agent.ROOT)
        try:
            res = agent.run_checks(scratch, git=False)
        finally:
            shutil.rmtree(scratch, ignore_errors=True)
        bad = [(r['id'], r['detail']) for r in res if r['result'] != 'PASS']
        self.assertEqual(bad, [])
        self.assertGreaterEqual(len(res), 24)

    def test_every_mutation_is_detected(self):
        report = agent.self_test()
        self.assertTrue(report)
        self.assertEqual({k: v for k, v in report.items() if v != 'DETECTED'}, {})

    def test_missing_input_fails_closed(self):
        scratch = agent.stage(agent.ROOT)
        try:
            (scratch / agent.INPUTS[0]).unlink()
            with self.assertRaises(FileNotFoundError):
                agent.stage(scratch)
        finally:
            shutil.rmtree(scratch, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()

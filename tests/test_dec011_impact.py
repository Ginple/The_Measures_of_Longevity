"""Invalidation-record checks for DEC-011/012 (software properties, not scientific truth)."""
from pathlib import Path
import hashlib
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dec011_impact', ROOT / 'tools/dec011_impact.py')
di = importlib.util.module_from_spec(spec)
spec.loader.exec_module(di)

# Bytes at base commit e0a598d. These files must not be edited by the restructure.
FROZEN_SHA256 = {
    'papers/P1_identity_selection/PROTOCOL.md': '456add6768ae641bb4247c3615a5160111cad0ea68a253aaf5afbbaed8603e1c',
    'papers/P2_weighting_observability/PROTOCOL.md': 'd8a920a42cde8d79d2b61324977c3b49c56456a6138bcc1d9e429236d672e292',
    'papers/P3_research_assurance/PROTOCOL.md': 'bd27bace7925f28892782c4c7f626a803d63fd7f1ab11e26d14145d73d8ccfcd',
    'review/ARCHITECTURE_AUDIT_PACKET_L2_2026-11-27.md': '96f49d0b1963406c96707e8ca0a7598dfe3a90c703ca82c4010be57cd8c5a569',
}


class Dec011Impact(unittest.TestCase):
    def test_record_in_sync_with_computation(self):
        stored = json.loads(di.OUT.read_text(encoding='utf-8'))
        self.assertEqual(stored, json.loads(json.dumps(di.build(), ensure_ascii=False)))

    def test_new_dependent_without_decision_fails(self):
        di.EDGES.append(('knowledge_base/MASTER.md', 'some/new/dependent.md'))
        try:
            with self.assertRaises(ValueError):
                di.build()
        finally:
            di.EDGES.pop()

    def test_transitive_global_propagation(self):
        queue = {x['node'] for x in di.build()['stale_queue']}
        # README depends on MASTER, which depends on the architecture change: two hops.
        self.assertIn('README.md', queue)
        self.assertIn('external:Linear THE-227/228/229/230/231', queue)

    def test_frozen_files_untouched_and_not_in_queue(self):
        queue = {x['node'] for x in di.build()['stale_queue']}
        for path, digest in FROZEN_SHA256.items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest, path)
            self.assertNotIn(path, queue)


if __name__ == '__main__':
    unittest.main()

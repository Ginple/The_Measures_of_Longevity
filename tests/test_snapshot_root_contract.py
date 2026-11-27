"""Root validation must actually invoke both snapshot verifier modes."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('root_validator', ROOT/'scripts/run_validation.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SnapshotRootContractTest(unittest.TestCase):
    def test_success_and_corruption_fail_both_modes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = Path('knowledge_base/source_snapshots')
            shutil.copytree(ROOT/rel, root/rel, ignore=shutil.ignore_patterns('__pycache__'))
            good = validator.snapshot_check(root)
            self.assertTrue(all(x['passed'] for x in good.values()))
            path = root/rel/'dunedinpace_4b569983/PACEProjector.R'
            raw = path.read_bytes()
            path.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])
            bad = validator.snapshot_check(root)
            self.assertFalse(any(x['passed'] for x in bad.values()))
            self.assertTrue(all('mismatch' in x['stderr'] for x in bad.values()))


if __name__ == '__main__':
    unittest.main()

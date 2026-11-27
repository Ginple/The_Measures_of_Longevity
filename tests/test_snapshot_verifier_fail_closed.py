"""Negative tests for the local snapshot verifier; mutations stay in temp dirs."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = Path('knowledge_base/source_snapshots')
SCRIPT = SNAPSHOTS / 'verify_snapshots.py'
MANIFEST = SNAPSHOTS / 'dunedinpace_4b569983/manifest.json'
SOURCE = SNAPSHOTS / 'dunedinpace_4b569983/PACEProjector.R'


class SnapshotVerifierFailClosedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / SNAPSHOTS, self.root / SNAPSHOTS,
                        ignore=shutil.ignore_patterns('__pycache__'))

    def run_verifier(self, optimized=False):
        args = [sys.executable] + (['-O'] if optimized else []) + [str(self.root / SCRIPT)]
        return subprocess.run(args, cwd=self.root, text=True, capture_output=True, timeout=20)

    def edit_manifest(self, change):
        path = self.root / MANIFEST
        data = json.loads(path.read_text(encoding='utf-8'))
        change(data)
        path.write_text(json.dumps(data), encoding='utf-8')

    def test_unmodified_passes_in_both_modes(self):
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                result = self.run_verifier(optimized)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.count('SHA256, git blob SHA1 OK'), 2)

    def test_same_length_corruption_fails_in_both_modes(self):
        path = self.root / SOURCE
        raw = path.read_bytes()
        path.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                result = self.run_verifier(optimized)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn(' OK', result.stdout)
                self.assertIn('mismatch', result.stderr)

    def test_empty_missing_or_duplicate_records_fail(self):
        original = json.loads((self.root / MANIFEST).read_text(encoding='utf-8'))
        for records in ([], original['records'][:1], original['records'] + original['records'][:1]):
            with self.subTest(record_count=len(records)):
                self.edit_manifest(lambda data: data.update(records=records))
                for optimized in (False, True):
                    result = self.run_verifier(optimized)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertNotIn(' OK', result.stdout)

    def test_missing_file_fails(self):
        (self.root / SOURCE).unlink()
        self.assertNotEqual(self.run_verifier().returncode, 0)
        self.assertNotEqual(self.run_verifier(True).returncode, 0)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Check this saved snapshot against its local manifest, not source authenticity.

The manifest is a local reference, not a trusted signature or proof that these
files were used by a study. No baselines or snapshots are rewritten.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = Path(__file__).parent / 'dunedinpace_4b569983' / 'manifest.json'
EXPECTED_PATHS = frozenset({
    'knowledge_base/source_snapshots/dunedinpace_4b569983/PACEProjector.R',
    'knowledge_base/source_snapshots/dunedinpace_4b569983/LICENSE',
})


def verify(root, manifest_path):
    """Fail closed on missing/duplicate entries or mismatched bytes in this snapshot."""
    root = Path(root).resolve()
    manifest = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    records = manifest.get('records')
    if not isinstance(records, list) or not records:
        raise ValueError('manifest records must be a nonempty list')
    paths = [record.get('local_path') if isinstance(record, dict) else None for record in records]
    if any(not isinstance(path, str) for path in paths) or len(set(paths)) != len(paths):
        raise ValueError('manifest paths must be unique strings')
    if set(paths) != EXPECTED_PATHS:
        raise ValueError('manifest must enumerate the two expected snapshot files')
    checked = []
    for record, name in zip(records, paths):
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f'snapshot path is missing or outside root: {name}')
        data = path.read_bytes()
        expected_bytes = record.get('bytes')
        expected_sha256 = record.get('sha256')
        expected_blob = record.get('git_blob_sha1')
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if (type(expected_bytes) is not int or len(data) != expected_bytes
                or hashlib.sha256(data).hexdigest() != expected_sha256
                or blob != expected_blob):
            raise ValueError(f'snapshot length or hash mismatch: {name}')
        checked.append(name)
    return checked


def main():
    try:
        checked = verify(ROOT, MANIFEST_PATH)
    except (OSError, ValueError, TypeError) as exc:
        raise SystemExit(f'snapshot verification failed: {exc}') from exc
    for name in checked:
        print(f'{name}: bytes, SHA256, git blob SHA1 OK')


if __name__ == '__main__':
    main()

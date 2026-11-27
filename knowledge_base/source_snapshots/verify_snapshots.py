#!/usr/bin/env python3
"""Verify saved snapshot bytes against the manifest, not scientific validity."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
manifest_path = Path(__file__).parent / 'dunedinpace_4b569983' / 'manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
for record in manifest['records']:
    data = (root / record['local_path']).read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert len(data) == record['bytes'], record['local_path']
    assert hashlib.sha256(data).hexdigest() == record['sha256'], record['local_path']
    assert blob == record['git_blob_sha1'], record['local_path']
    print(record['local_path'] + ': bytes, SHA256, git blob SHA1 OK')

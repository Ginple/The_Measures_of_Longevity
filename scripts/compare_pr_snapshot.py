#!/usr/bin/env python3
"""Read-only byte comparison with an explicitly pinned git snapshot.

Only paths changed between BASE and SNAPSHOT are compared; additional local
changes are not inventoried. This is neither a merge nor a semantic review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True, stdout=subprocess.PIPE).stdout


def parse_tree(data):
    tree = {}
    for entry in data.split(b'\0'):
        if not entry:
            continue
        meta, path = entry.split(b'\t', 1)
        mode, kind, oid = meta.decode('ascii').split(' ')
        tree[path.decode('utf-8')] = (mode, kind, oid)
    return tree


def casefold_collisions(paths):
    groups = {}
    for path in paths:
        groups.setdefault(path.casefold(), []).append(path)
    return sorted(sorted(group) for group in groups.values() if len(group) > 1)


def compare(root, base, snapshot):
    root = Path(root).resolve()
    # Resolve to immutable commits before any subsequent reads.
    base_oid = git(root, 'rev-parse', '--verify', base + '^{commit}').decode().strip()
    head_oid = git(root, 'rev-parse', '--verify', snapshot + '^{commit}').decode().strip()
    tree = parse_tree(git(root, 'ls-tree', '-r', '-z', '--full-tree', head_oid))
    changed = [p.decode('utf-8') for p in git(root, 'diff', '--no-renames', '--name-only', '-z', base_oid, head_oid).split(b'\0') if p]
    collisions = casefold_collisions(tree)
    rows = []
    for name in sorted(changed):
        remote = tree.get(name)
        path = root / name
        # Refuse a symlink at any component; do not read outside the checkout.
        components = [root.joinpath(*Path(name).parts[:i]) for i in range(1, len(Path(name).parts) + 1)]
        if any(component.is_symlink() for component in components):
            local_state, local_hash = 'symlink_not_read', None
        elif path.is_file():
            local_state, local_hash = 'file', hashlib.sha256(path.read_bytes()).hexdigest()
        elif path.exists():
            local_state, local_hash = 'not_regular_file', None
        else:
            local_state, local_hash = 'absent', None
        remote_hash = None
        if remote and remote[0] in ('100644', '100755') and remote[1] == 'blob':
            remote_hash = hashlib.sha256(git(root, 'cat-file', 'blob', remote[2])).hexdigest()
        if not remote:
            status = 'deleted_upstream'
        elif remote_hash is None:
            status = 'upstream_not_regular_file'
        elif local_state != 'file':
            status = 'local_' + local_state
        elif local_hash == remote_hash:
            status = 'identical'
        else:
            status = 'different'
        rows.append({'path': name, 'status': status, 'snapshot_sha256': remote_hash,
                     'worktree_sha256': local_hash})
    counts = {key: sum(row['status'] == key for row in rows) for key in sorted({r['status'] for r in rows})}
    return {'base_commit': base_oid, 'snapshot_commit': head_oid, 'changed_paths': len(rows),
            'counts': counts, 'casefold_collisions_in_snapshot': sorted(collisions), 'paths': rows,
            'scope': 'Bytes on upstream-changed paths only; not semantic equivalence, review or a merge.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True)
    parser.add_argument('--snapshot', required=True)
    args = parser.parse_args()
    print(json.dumps(compare(ROOT, args.base, args.snapshot), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

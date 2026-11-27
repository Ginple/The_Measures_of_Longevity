"""Check repository Markdown links; keep documented legacy exceptions visible.

The exception list is a fixed list of (file, link) pairs, not a directory or
wildcard exemption. A newly broken link anywhere still fails validation. This
simple checker examines inline Markdown links and file existence, not fragments
or external URLs; it is not a comprehensive Markdown parser.
"""
from pathlib import Path
import json
import re

EXCLUDED_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist', 'node_modules', '.pytest_cache'}
LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')


def broken_links(root):
    root = Path(root)
    broken = []
    for file in sorted(root.rglob('*.md')):
        if any(part in EXCLUDED_DIRS for part in file.relative_to(root).parts):
            continue
        for link in LINK_RE.findall(file.read_text(encoding='utf-8')):
            if not link.startswith(('http:', 'https:', 'mailto:', '#')) and not (file.parent / link.split('#')[0]).exists():
                broken.append({'file': file.relative_to(root).as_posix(), 'link': link})
    return broken


def classify_links(root):
    root = Path(root)
    baseline = json.loads((root / 'governance/legacy_broken_links.json').read_text(encoding='utf-8'))
    allowed = {(row['file'], row['link']) for row in baseline['known_broken_links']}
    current = broken_links(root)
    return {'new': [x for x in current if (x['file'], x['link']) not in allowed],
            'known_legacy': [x for x in current if (x['file'], x['link']) in allowed],
            'scope': 'Inline relative Markdown links only; external URLs and fragments not validated.'}

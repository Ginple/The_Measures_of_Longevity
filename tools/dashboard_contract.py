"""Repository output contract: no HTML deliverables, no case-colliding paths.

History: PR #1 briefly required two dashboard paths differing only by case
(STATE_DASHBOARD.HTML / .html). That pair cannot be checked out reliably on
case-insensitive file systems. On 2026-11-27 the lowercase copy was removed
(DEC-008) and, at the author's explicit request, the remaining dashboard was
deleted too. The contract therefore returns to main's original rule: the
repository ships Markdown/JSON/Python only and contains no HTML files. It also
rejects repository paths that collide when compared case-insensitively.
Structural checks only; this is not content certification.
"""
from collections import defaultdict
from pathlib import Path

DASHBOARDS = ()  # no HTML deliverable is authorized
EXCLUDED_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist', 'node_modules', '.pytest_cache'}


def _paths(root):
    root = Path(root)
    for path in root.rglob('*'):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        yield path, rel


def case_collisions(root):
    """Return groups of repository paths that are equal ignoring letter case."""
    groups = defaultdict(list)
    for _, rel in _paths(root):
        groups[rel.as_posix().casefold()].append(rel.as_posix())
    return sorted(sorted(v) for v in groups.values() if len(v) > 1)


def check_dashboard(root):
    errors = ['case-insensitive path collision: ' + ' | '.join(g) for g in case_collisions(root)]
    for path, rel in _paths(root):
        if path.is_file() and path.suffix.lower() in ('.html', '.htm'):
            errors.append('unauthorized HTML: ' + rel.as_posix())
    return errors

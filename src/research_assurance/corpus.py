"""A small Markdown paragraph adapter, not a general document parser or semantic extractor."""
import re
from itertools import combinations


def extract_units(text, ontology):
    """All nonempty Markdown blocks retained, including references. No silent exclusions.

    Lists/tables are block-level here (unlike historical v1 row splitting). Use a
    domain adapter for row/sentence/chapter modes and record its version explicitly.
    English aliases use word boundaries; Chinese matching is literal substring.
    """
    lines = text.splitlines(keepends=True)
    units, start, block = [], None, []
    def emit(end):
        if not block:
            return
        body = ''.join(block)
        first = body.lstrip()
        kind = 'heading' if first.startswith('#') else 'table' if first.startswith('|') else 'list' if re.match(r'(?:[-*+] |\d+[.)] )', first) else 'prose'
        hits = []
        for concept in ontology:
            found = []
            for alias in concept['aliases']:
                pattern = r'(?<!\w)' + re.escape(alias) + r'(?!\w)' if alias.isascii() else re.escape(alias)
                if re.search(pattern, body, flags=re.I):
                    found.append(alias)
            if found:
                hits.append({'id': concept['id'], 'matched_aliases': sorted(found)})
        units.append({'id': f'U{len(units)+1:04d}', 'lines_1based_halfopen': [start, end],
                      'kind': kind, 'text': body, 'concept_ids': sorted(h['id'] for h in hits), 'hits': hits})
    for index, line in enumerate(lines, 1):
        if not line.strip():
            emit(index)
            block, start = [], None
        else:
            if start is None:
                start = index
            block.append(line)
    emit(len(lines)+1)
    return units


def apophatic_scan(units, ontology, expected_pairs=()):
    seen = set().union(*(set(u['concept_ids']) for u in units)) if units else set()
    edges = {tuple(sorted(p)) for u in units if u['kind'] == 'prose' for p in combinations(set(u['concept_ids']), 2)}
    return {'zero_detected_entries': sorted(c['id'] for c in ontology if c['id'] not in seen),
            'expected_pairs_without_prose_cooccurrence': [list(p) for p in expected_pairs if tuple(sorted(p)) not in edges],
            'warning': 'A declared lexical lens can miss synonyms, negation scope and distributed arguments. Not proof of semantic absence.'}

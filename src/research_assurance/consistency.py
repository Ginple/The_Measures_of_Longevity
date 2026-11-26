"""Finite relational CSP feasibility. Historical h0 name is NOT sheaf cohomology."""
import json
import math


def finite_global_compatibility(sections, max_states=10000):
    if not sections or type(max_states) is not int or max_states < 1:
        return {'status': 'unknown', 'reason': 'empty_model_or_invalid_budget', 'external_truth': 'unknown'}
    ids = set()
    try:
        for s in sections:
            if not isinstance(s['id'], str) or not s['id'] or s['id'] in ids:
                raise ValueError
            ids.add(s['id'])
            if not isinstance(s['vars'], list) or not s['vars'] or any(not isinstance(v, str) or not v for v in s['vars']) or len(set(s['vars'])) != len(s['vars']):
                raise ValueError
            if not isinstance(s['allowed'], list):
                raise ValueError
            for row in s['allowed']:
                if not isinstance(row, list) or len(row) != len(s['vars']):
                    raise ValueError
                for v in row:
                    if type(v) not in (int, float, bool, str, type(None)) or isinstance(v, float) and not math.isfinite(v):
                        raise ValueError
    except (KeyError, TypeError, ValueError):
        return {'status': 'unknown', 'reason': 'invalid_model', 'external_truth': 'unknown'}
    count = 0
    ordered = sorted(sections, key=lambda s: (len(s['allowed']), s['id']))
    # Preserve JSON types: Python otherwise equates True and 1.
    key = lambda v: json.dumps(v, ensure_ascii=False, sort_keys=True, allow_nan=False)
    def visit(i, assignment):
        nonlocal count
        if i == len(ordered):
            return assignment
        s = ordered[i]
        for row in s['allowed']:
            count += 1
            if count > max_states:
                raise TimeoutError
            proposal = dict(zip(s['vars'], row))
            if all(k not in assignment or key(assignment[k]) == key(v) for k, v in proposal.items()):
                found = visit(i + 1, {**assignment, **proposal})
                if found is not None:
                    return found
        return None
    try:
        witness = visit(0, {})
        return {'status': 'sat' if witness is not None else 'unsat', 'witness': witness,
                'states': count, 'scope': 'encoded_relations_only', 'external_truth': 'unknown'}
    except (TimeoutError, RecursionError):
        return {'status': 'unknown', 'reason': 'search_budget_or_recursion_limit', 'states': count, 'external_truth': 'unknown'}


def h0_global_section_exists(sections, max_states=10000):
    """Legacy alias; no cohomology groups, topology, or external truth are computed."""
    return finite_global_compatibility(sections, max_states)

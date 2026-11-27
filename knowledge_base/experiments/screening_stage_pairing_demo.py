"""Finite synthetic counterfactual stage categories, not NHS-Galleri data.

Categories are mutually exclusive outcomes over an illustrative window; O means
anything other than III or IV, not necessarily absence of cancer. Both potential
outcomes per synthetic person are specified solely to demonstrate identification.
"""
from collections import Counter
import json

STATES = frozenset(('III', 'IV', 'O'))


def summarize(pairs):
    pairs = tuple(pairs)
    if not pairs:
        raise ValueError('at least one synthetic pair is required')
    for pair in pairs:
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            raise ValueError('each pair must contain control and intervention states')
        if any(not isinstance(state, str) or state not in STATES for state in pair):
            raise ValueError('states must be III, IV, or O')
    before = Counter(a for a, _ in pairs)
    after = Counter(b for _, b in pairs)
    return {
        'n': len(pairs),
        'control': {state: before[state] for state in ('III', 'IV', 'O')},
        'intervention': {state: after[state] for state in ('III', 'IV', 'O')},
        'control_IV_to_intervention_III': sum(a == 'IV' and b == 'III' for a, b in pairs),
    }


def main():
    control = ['IV', 'IV', 'III', 'O']
    worlds = {
        'one_cross_stage': ['III', 'IV', 'III', 'O'],
        'none_cross_stage': ['O', 'IV', 'III', 'III'],
        'two_cross_stage': ['III', 'III', 'IV', 'O'],
    }
    for name, treated in worlds.items():
        print(json.dumps({'world': name, 'synthetic': True,
                          **summarize(zip(control, treated))}))


if __name__ == '__main__':
    main()

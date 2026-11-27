#!/usr/bin/env python3
"""Two exact, synthetic selectivity identifiability examples, not source data."""
from fractions import Fraction as F
import json


def table(s_positive, s_negative, other_positive, other_negative):
    vals = tuple(map(F, (s_positive, s_negative, other_positive, other_negative)))
    if any(v < 0 for v in vals):
        raise ValueError('counts must be nonnegative')
    sp, sn, op, on = vals
    if sp + sn == 0 or sp + op == 0:
        raise ValueError('conditional denominators must be positive')
    return {'n': sum(vals), 'marker_count': sp + op,
            'marker_given_label': sp / (sp + sn),
            'label_given_marker': sp / (sp + op)}


def world(c, p, m=None, indirect=True):
    """C and P randomized, observed mediator M=P; off-support do(M) allowed.

    Indirect world: M mediates P-by-C. Direct world: P interacts with C.
    Marker, M, Y are identical across randomized arms in both worlds.
    Units are arbitrary synthetic scores, not real clinical measures.
    """
    if c not in (0, 1) or p not in (0, 1) or (m is not None and m not in (0, 1)):
        raise ValueError('binary variables required')
    m = p if m is None else m
    label = 50 - 30*c
    y = 50 + 10*c + 20*c*(m if indirect else p)
    return {'label': label, 'maintenance': m, 'outcome': y}


def main():
    a, b = table(30, 20, 20, 30), table(6, 4, 44, 46)
    pairs = []
    for c in (0, 1):
        for p in (0, 1):
            pairs.append({'C': c, 'P': p, 'world_A': world(c, p), 'world_B': world(c, p, indirect=False)})
    print(json.dumps({'tables': [{k: str(v) for k, v in t.items()} for t in (a, b)],
                      'randomized_arms': pairs,
                      'do_M_1_minus_0_at_C1_P0': {'A': world(1, 0, 1)['outcome']-world(1, 0, 0)['outcome'],
                                                   'B': world(1, 0, 1, False)['outcome']-world(1, 0, 0, False)['outcome']}}, indent=2))


if __name__ == '__main__':
    main()

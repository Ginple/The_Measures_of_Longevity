#!/usr/bin/env python3
"""Sharp deterministic bounds for one synthetic labelled cargo balance.

No biological data, kinetics or measurement uncertainty are modelled.
"""
from fractions import Fraction as F
import json


def bounds(start, uptake, end, other_min=0, other_max=None):
    """R_end = R_start + uptake - degradation - other_exit.

    All amounts are exact, nonnegative and over the same interval/units.
    `other_exit` is constrained to [other_min, other_max] or [other_min, T]
    when other_max is omitted. Return sharp [D_min, D_max].
    """
    start, uptake, end, other_min = map(F, (start, uptake, end, other_min))
    if min(start, uptake, end, other_min) < 0:
        raise ValueError('amounts must be nonnegative')
    total = start + uptake - end
    if total < 0:
        raise ValueError('negative total exit is infeasible under this model')
    other_max = total if other_max is None else F(other_max)
    if other_max < other_min or other_min > total:
        raise ValueError('infeasible other-exit constraints')
    return max(F(0), total-other_max), total-other_min


def witness(start, uptake, end, degradation):
    """Return the only other exit matching a candidate D; reject infeasibility."""
    lo, hi = bounds(start, uptake, end)
    degradation = F(degradation)
    if not lo <= degradation <= hi:
        raise ValueError('degradation outside feasible range')
    return F(start) + F(uptake) - F(end) - degradation


def main():
    lo, hi = bounds(0, 6, 2)
    no_other = bounds(0, 6, 2, 0, 0)
    print(json.dumps({'synthetic_only': True, 'total_receiver_exit': '4',
                      'degradation_bounds': [str(lo), str(hi)],
                      'witnesses_degradation_to_other_exit':
                          {str(d): str(witness(0, 6, 2, d)) for d in (0, 1, 4)},
                      'under_no_other_exit': [str(x) for x in no_other]}, indent=2))


if __name__ == '__main__':
    main()

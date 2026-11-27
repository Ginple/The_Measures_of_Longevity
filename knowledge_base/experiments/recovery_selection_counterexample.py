#!/usr/bin/env python3
"""Synthetic recovery eligibility and principal-stratum selection example.

Finite population, binary outcome defined only under the history in which the
unit is eligible. The two randomized history arms reveal marginals, not joint
potential outcomes. This is not a biological simulation or data analysis.
"""
from fractions import Fraction
import json


def world(name):
    if name not in ('A', 'B'):
        raise ValueError('world must be A or B')
    units = []
    for i in range(100):
        # 25 always eligible, 25 eligible only under H=0, 25 only under H=1,
        # and 25 never eligible.
        r0 = i < 50
        r1 = i < 25 or 50 <= i < 75
        if name == 'A':
            y0 = int(25 <= i < 45) if r0 else None
            y1 = int(i < 25 or 50 <= i < 55) if r1 else None
        else:
            y0 = int(i < 20) if r0 else None
            y1 = int(i < 5 or 50 <= i < 75) if r1 else None
        units.append({'r0': r0, 'r1': r1, 'y0': y0, 'y1': y1})
    return units


def summary(units):
    n = len(units)
    if not n:
        raise ValueError('empty population')
    arms = {}
    for h in (0, 1):
        eligible = [u[f'y{h}'] for u in units if u[f'r{h}']]
        arms[str(h)] = {'eligible': len(eligible), 'positive': sum(eligible),
                        'positive_fraction_among_eligible': str(Fraction(sum(eligible), len(eligible))) if eligible else None}
    common = [u for u in units if u['r0'] and u['r1']]
    effect = Fraction(sum(u['y1']-u['y0'] for u in common), len(common)) if common else None
    return {'population': n, 'history_arms': arms, 'always_eligible': len(common),
            'effect_in_always_eligible': str(effect) if effect is not None else None}


def main():
    print(json.dumps({w: summary(world(w)) for w in ('A', 'B')}, indent=2))


if __name__ == '__main__':
    main()

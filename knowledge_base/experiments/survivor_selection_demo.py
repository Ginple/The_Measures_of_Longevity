#!/usr/bin/env python3
"""Synthetic counterexample: identical randomized-arm marginals, different survivor effects.

Potential outcomes are known only because these are invented populations. The
example is not an analysis of any trial and does not prescribe a death score.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Type:
    count: int
    y0: int | None  # None means death; post-death function is undefined.
    y1: int | None


WORLD_A = (Type(50, 80, 70), Type(10, 20, None), Type(40, None, 100))
WORLD_B = (Type(50, 80, 70), Type(10, 20, 100), Type(30, None, 100), Type(10, None, None))


def summarize(population):
    total = sum(t.count for t in population)
    if total <= 0 or any(t.count <= 0 for t in population):
        raise ValueError('population counts must be positive')
    n0 = sum(t.count for t in population if t.y0 is not None)
    n1 = sum(t.count for t in population if t.y1 is not None)
    always = sum(t.count for t in population if t.y0 is not None and t.y1 is not None)
    if not n0 or not n1 or not always:
        raise ValueError('conditional means require survivors in both arms and the always-survivor stratum')
    avg0 = Fraction(sum(t.count * t.y0 for t in population if t.y0 is not None), n0)
    avg1 = Fraction(sum(t.count * t.y1 for t in population if t.y1 is not None), n1)
    survivor_effect = Fraction(sum(t.count * (t.y1 - t.y0) for t in population if t.y0 is not None and t.y1 is not None), always)
    marginal0 = sorted((v, sum(t.count for t in population if t.y0 == v)) for v in {t.y0 for t in population if t.y0 is not None})
    marginal1 = sorted((v, sum(t.count for t in population if t.y1 == v)) for v in {t.y1 for t in population if t.y1 is not None})
    return {'total': total, 'surv0': n0, 'surv1': n1, 'marginal0': marginal0,
            'marginal1': marginal1, 'mean0': avg0, 'mean1': avg1,
            'naive_difference': avg1 - avg0, 'always_survivors': always,
            'always_survivor_effect': survivor_effect}


def main():
    print('Synthetic potential outcomes; no clinical or trial data.')
    for name, pop in [('A', WORLD_A), ('B', WORLD_B)]:
        s = summarize(pop)
        print(f"{name}: control survivors {s['surv0']}/{s['total']}, treatment survivors {s['surv1']}/{s['total']}; "
              f"survivor means {float(s['mean0']):.3f} -> {float(s['mean1']):.3f}, "
              f"observed difference {float(s['naive_difference']):+.3f}; "
              f"always-survivor count {s['always_survivors']}, "
              f"counterfactual effect {float(s['always_survivor_effect']):+.3f}")
    a, b = summarize(WORLD_A), summarize(WORLD_B)
    assert (a['surv0'], a['surv1'], a['marginal0'], a['marginal1']) == (b['surv0'], b['surv1'], b['marginal0'], b['marginal1'])
    assert a['always_survivor_effect'] < 0 < b['always_survivor_effect']
    print('Same arm-wise observable distributions do not identify cross-world survivor membership or its effect.')


if __name__ == '__main__':
    main()

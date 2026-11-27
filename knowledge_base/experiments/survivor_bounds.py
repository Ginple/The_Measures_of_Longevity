#!/usr/bin/env python3
"""Exact finite-population bounds for always-survivor mean contrast.

Invented population marginals, not estimates from a real study. Outcomes are
undefined after death. The supports and frequencies are assumed exactly known.
"""
from fractions import Fraction


def _validated(n, histogram):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError('population size must be a positive integer')
    result = []
    for value, count in histogram.items():
        if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
            raise ValueError('values must be integer or Fraction')
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError('histogram counts must be positive integers')
        result.append((Fraction(value), count))
    count = sum(c for _, c in result)
    if count > n:
        raise ValueError('survivor count exceeds population')
    return sorted(result), count


def _trimmed_mean(histogram, keep, reverse=False):
    count, total = 0, Fraction(0)
    for value, amount in sorted(histogram, reverse=reverse):
        take = min(keep - count, amount)
        total += value * take
        count += take
        if count == keep:
            return total / keep
    raise ValueError('not enough survivors')


def always_survivor_bounds(n, control, treated, monotone=False):
    """Return sharp bounds over all *integer* couplings of given marginals.

    If monotone, assume S1>=S0 for each unit (no treatment-caused death).
    None signals that no always-survivor is possible, not an effect of zero.
    When q=0 is feasible but q>0 is also feasible, bounds condition on q>0;
    they do not imply the principal-stratum effect exists in every coupling.
    """
    h0, n0 = _validated(n, control)
    h1, n1 = _validated(n, treated)
    if monotone and n1 < n0:
        raise ValueError('survival marginals contradict monotonicity')
    q_min = n0 if monotone else max(0, n0+n1-n)
    q_max = min(n0,n1)
    if q_max == 0:
        return {'overlap': (0, 0), 'bounds': None}
    q = max(1, q_min)
    lower = _trimmed_mean(h1,q) - _trimmed_mean(h0,q,reverse=True)
    upper = _trimmed_mean(h1,q,reverse=True) - _trimmed_mean(h0,q)
    return {'overlap': (q_min,q_max), 'bounds': (lower,upper), 'extreme_overlap': q}


def main():
    for label, assumption in [('unrestricted',False), ('no treatment-caused death',True)]:
        r = always_survivor_bounds(100,{80:50,20:10},{70:50,100:40},assumption)
        print(f'{label}: overlap {r["overlap"]}; effect bounds {tuple(map(str,r["bounds"]))}; extrema at overlap {r["extreme_overlap"]}')
    print('Invented exact finite-population marginals only. No sampling-uncertainty interval.')


if __name__ == '__main__':
    main()

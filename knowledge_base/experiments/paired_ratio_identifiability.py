"""Exact finite toy example: marginal values do not identify paired ratios.

Exhausts possible pairings of known marginals. In the real X43 problem even
full marginal values are not available, only summaries. No model data here.
"""
from fractions import Fraction
from itertools import permutations
from statistics import median
import json


def enumerate_pairings(numerators, denominators):
    if len(numerators) != len(denominators) or not numerators:
        raise ValueError('equal nonempty sequences required')
    if len(numerators) > 8:
        raise ValueError('factorial enumeration limited to 8 toy runs')
    if any(type(x) is not int or x < 0 for x in numerators):
        raise ValueError('numerators must be nonnegative integers')
    if any(type(x) is not int or x <= 0 for x in denominators):
        raise ValueError('denominators must be positive integers')
    results = []
    for arrangement in sorted(set(permutations(denominators))):
        if any(n > d for n, d in zip(numerators, arrangement)):
            continue
        ratios = [Fraction(n, d) for n, d in zip(numerators, arrangement)]
        results.append({'denominators': arrangement, 'median': median(ratios),
                        'min': min(ratios), 'max': max(ratios)})
    if not results:
        raise ValueError('no feasible pairing with numerator <= denominator')
    return results


def example():
    numerators, denominators = [1, 2, 4, 8], [10, 20, 40, 80]
    pairings = enumerate_pairings(numerators, denominators)
    low = min(pairings, key=lambda p: p['median'])
    high = max(pairings, key=lambda p: p['median'])
    def render(p):
        return {'denominators_in_numerator_order': p['denominators'],
                'median_ratio': float(p['median']),
                'ratio_range': [float(p['min']), float(p['max'])]}
    return {'classification': 'FOUR SYNTHETIC RUNS; NOT MCED RESULTS',
            'numerators': numerators, 'denominator_marginals': denominators,
            'feasible_pairings': len(pairings),
            'ratio_of_marginal_medians': float(median(map(Fraction, numerators)) / median(map(Fraction, denominators))),
            'lowest_paired_median': render(low), 'highest_paired_median': render(high)}


if __name__ == '__main__':
    print(json.dumps(example(), indent=2))

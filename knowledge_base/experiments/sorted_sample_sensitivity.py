#!/usr/bin/env python3
"""Exact sensitivity algebra for a fictional selected-sample proportion.

Not estimates of any actual capture rate, tissue prevalence, or clinical effect.
"""
from fractions import Fraction as F
import json


def sample_from_population(population_fraction, relative_inclusion):
    """Selected fraction with U+ versus U- inclusion ratio, within S+."""
    t, r = F(population_fraction), F(relative_inclusion)
    if not 0 <= t <= 1 or r <= 0:
        raise ValueError('population fraction must be in [0,1], inclusion ratio positive')
    return r*t / (r*t + 1-t)


def population_from_sample(sample_fraction, relative_inclusion):
    """Inverse for a specified, known ratio; unknown ratio is not identified."""
    q, r = F(sample_fraction), F(relative_inclusion)
    if not 0 <= q <= 1 or r <= 0:
        raise ValueError('sample fraction must be in [0,1], inclusion ratio positive')
    return q / (q + r*(1-q))


def population_bounds(sample_fraction, relative_inclusion_min, relative_inclusion_max):
    low, high = F(relative_inclusion_min), F(relative_inclusion_max)
    if low <= 0 or high < low:
        raise ValueError('positive ordered inclusion ratio bounds required')
    return (population_from_sample(sample_fraction, high),
            population_from_sample(sample_fraction, low))


def main():
    q = F(3, 5)
    scenarios = {str(r): str(population_from_sample(q, r))
                 for r in (F(1, 10), F(1), F(10))}
    print(json.dumps({'sample_fraction_fictional': str(q),
                      'population_fraction_by_assumed_inclusion_ratio': scenarios,
                      'illustrative_bounds_if_ratio_between_half_and_two':
                          [str(x) for x in population_bounds(q, F(1, 2), 2)]}, indent=2))


if __name__ == '__main__':
    main()

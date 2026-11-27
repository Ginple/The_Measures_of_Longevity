#!/usr/bin/env python3
"""Synthetic algebra counterexamples, NOT clinical/biological data or a clock.

Run: python knowledge_base/experiments/mixture_identifiability_demo.py
Uses only the Python standard library. All quantities are fabricated.
"""
from math import isclose


def mix(p, m):
    assert len(p) == len(m) and isclose(sum(p), 1.0)
    assert all(0 <= x <= 1 for x in p + m)
    return sum(x * y for x, y in zip(p, m))


def components(p0, m0, p1, m1):
    dp = [b - a for a, b in zip(p0, p1)]
    dm = [b - a for a, b in zip(m0, m1)]
    return (sum(p * d for p, d in zip(p0, dm)),
            sum(d * m for d, m in zip(dp, m0)),
            sum(p * m for p, m in zip(dp, dm)))


p0, m0 = [0.75, 0.25], [0.2, 0.8]
p1_a, m1_a = [0.25, 0.75], [0.2, 0.8]  # composition only
p1_b, m1_b = [0.75, 0.25], [0.6, 0.8]  # within-type only
before = mix(p0, m0)
for name, p1, m1 in [('A composition only', p1_a, m1_a), ('B within-type only', p1_b, m1_b)]:
    after = mix(p1, m1)
    within, composition, interaction = components(p0, m0, p1, m1)
    assert isclose(after, 0.65, abs_tol=1e-12)
    assert isclose(after-before, within+composition+interaction, abs_tol=1e-12)
    print(f'{name}: before={before:.2f}, after={after:.2f}, Δ={after-before:.2f}; '
          f'within={within:.2f}, composition={composition:.2f}, interaction={interaction:.2f}')

# A fixed target has a missing value at one feature. Cohort-mean imputation is a
# stated rule in the pinned source, not a reproduction of its full algorithm.
# Input batches differ only in *other samples*: target's observed data are fixed.
# The illustrative final score is simply the imputed feature value.
for label, peers in [('cohort 1', [0.2, 0.4]), ('cohort 2', [0.6, 0.8])]:
    imputed = sum(peers)/len(peers)
    print(f'{label}: unchanged missing target value imputed to {imputed:.2f}')
assert isclose(sum([0.6, 0.8])/2 - sum([0.2, 0.4])/2, 0.4, abs_tol=1e-12)
print('Synthetic only: these equalities do not estimate any actual clock or intervention.')

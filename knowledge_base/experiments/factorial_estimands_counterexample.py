"""Synthetic 2×2 factorial risk means, not any trial or biomarker data.

Reports effects on an additive risk-difference scale with equal weights over
factor B. A risk difference of zero is not an assertion of no interaction on
other scales. Assumes fully observed counterfactual cell means.
"""
from math import isfinite
import json


def contrasts(p00, p10, p01, p11):
    cells = (p00, p10, p01, p11)
    if any(not isfinite(x) or not 0 <= x <= 1 for x in cells):
        raise ValueError('cell risks must be finite and within [0, 1]')
    a_b0 = p10 - p00
    a_b1 = p11 - p01
    b_a0 = p01 - p00
    b_a1 = p11 - p10
    return {'a_effect_if_b0': a_b0, 'a_effect_if_b1': a_b1,
            'equal_weight_marginal_a': (a_b0 + a_b1) / 2,
            'b_effect_if_a0': b_a0, 'b_effect_if_a1': b_a1,
            'combined_vs_neither': p11 - p00,
            'additive_interaction': p11 - p10 - p01 + p00}


def examples():
    return {'classification': 'SYNTHETIC; EQUAL-WEIGHT RISKS; NO OBSERVED DATA',
            'additive': contrasts(.4, .2, .2, 0),
            'heterogeneous': contrasts(.4, .2, .2, .3)}


if __name__ == '__main__':
    print(json.dumps(examples(), indent=2))

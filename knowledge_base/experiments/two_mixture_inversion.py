#!/usr/bin/env python3
"""Synthetic two-mixture inversion and deterministic error amplification.

Inputs are exact rational numbers, and all assumptions are documented in
P2_TWO_MIXTURE_INVERSION_2026-11-27.md. Not biological or patient data.
"""
from fractions import Fraction as F
import json


def reconstruct(ya, yb, pa, pb):
    """Invert two exact mixtures, reject singular or physically infeasible data."""
    ya, yb, pa, pb = map(F, (ya, yb, pa, pb))
    if not all(0 <= q <= 1 for q in (ya, yb, pa, pb)):
        raise ValueError('observations and weights must lie in [0,1]')
    d = pa - pb
    if d == 0:
        raise ValueError('singular design; separate constrained analysis is required')
    x1 = ((1-pb)*ya - (1-pa)*yb) / d
    x2 = (pa*yb - pb*ya) / d
    if not (0 <= x1 <= 1 and 0 <= x2 <= 1):
        raise ValueError('no solution in [0,1]^2 under exact assumptions')
    return x1, x2


def error_amplification(pa, pb, eps_a, eps_b):
    """Worst-case absolute algebraic errors from independent bounded y errors.

    These are sharp for unconstrained measurement errors but may be
    conservative if physical feasibility constraints bind. Weight error and
    model misspecification are excluded; this is not a confidence interval.
    """
    pa, pb, ea, eb = map(F, (pa, pb, eps_a, eps_b))
    if not (0 <= pa <= 1 and 0 <= pb <= 1 and ea >= 0 and eb >= 0):
        raise ValueError('weights must be in [0,1] and errors nonnegative')
    d = abs(pa-pb)
    if not d:
        raise ValueError('singular design')
    return ((1-pb)*ea + (1-pa)*eb)/d, (pb*ea + pa*eb)/d


def demo():
    p, q, eps = F(1, 2), F(51, 100), F(1, 1000)
    y = F(1, 2)
    true = reconstruct(y, y, p, q)
    altered = reconstruct(y+eps, y-eps, p, q)
    bound = error_amplification(p, q, eps, eps)
    return {'classification': 'synthetic only', 'weights': [str(p), str(q)],
            'true_y': [str(y), str(y)], 'perturbed_y': [str(y+eps), str(y-eps)],
            'true_x': list(map(str, true)), 'perturbed_x': list(map(str, altered)),
            'absolute_error_bounds': list(map(str, bound))}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2))

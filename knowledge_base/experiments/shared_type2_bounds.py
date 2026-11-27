"""Synthetic joint bounds when type 2 is constrained to be equal at both times.

Exact, normalized, linear two-type mixtures only. Not patient data, a clock,
a statistical confidence interval, or evidence that the shared assumption holds.
"""
from fractions import Fraction as F


def shared_type2_change_bounds(y0, y1, p0, p1, x2_low, x2_high):
    """Return (change bounds, shared x2 feasible interval), all exact Fractions.

    x1_t and shared x2 belong to [0, 1]; y_t = p_t*x1_t+(1-p_t)*x2.
    p0 and p1 must be known and strictly positive. The shared x2 must also be
    in the supplied closed interval. Infeasibility is an error, not projection.
    """
    y0, y1, p0, p1, a, b = map(F, (y0, y1, p0, p1, x2_low, x2_high))
    if not (0 <= y0 <= 1 and 0 <= y1 <= 1 and 0 < p0 <= 1
            and 0 < p1 <= 1 and 0 <= a <= b <= 1):
        raise ValueError('expected normalized values, ordered interval, and positive weights')
    lo, hi = a, b
    for y, p in ((y0, p0), (y1, p1)):
        if p < 1:
            lo = max(lo, (y-p)/(1-p))
            hi = min(hi, y/(1-p))
    if lo > hi:
        raise ValueError('no common type 2 value is feasible')
    def change(x2):
        return (y1-(1-p1)*x2)/p1 - (y0-(1-p0)*x2)/p0
    endpoints = (change(lo), change(hi))
    return (min(endpoints), max(endpoints)), (lo, hi)

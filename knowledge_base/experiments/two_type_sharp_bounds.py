"""Sharp conditional bounds for a synthetic linear two-type mixture.

All examples are synthetic, not data or an epigenetic clock. Inputs must be
exact and normalized: 0 <= x1,x2,y <= 1; 0 <= p_low <= p_high <= 1.
No statistical confidence interval, noise model or linkage is implied.
"""
from fractions import Fraction as F
import json


def type1_bounds(y, p_low, p_high):
    """Range of x1 satisfying y=p*x1+(1-p)*x2, x2 in [0,1].

    The range is sharp when p may vary over the given closed interval. When
    p=0 is permitted, x1 is completely unobserved. Otherwise both extrema
    can be attained at p_low. Values are exact Fractions.
    """
    y, lo, hi = F(y), F(p_low), F(p_high)
    if not (0 <= y <= 1 and 0 <= lo <= hi <= 1):
        raise ValueError('y and weight interval must be within [0,1] and ordered')
    if lo == 0:
        return F(0), F(1)
    return max(F(0), (y - 1 + lo) / lo), min(F(1), y / lo)


def change_bounds(y0, y1, p0_bounds, p1_bounds):
    """Sharp when two times have no additional joint/cross-time constraints."""
    low0, high0 = type1_bounds(y0, *p0_bounds)
    low1, high1 = type1_bounds(y1, *p1_bounds)
    return low1 - high0, high1 - low0


def example():
    half = F(1, 2)
    before, after = F(3, 5), F(2, 5)
    delta = change_bounds(before, after, (half, half), (half, half))
    return {'classification': 'SYNTHETIC, exact linear mixture, not trial data',
            'p': '1/2 at both times', 'y_before': str(before), 'y_after': str(after),
            'type1_before_bounds': [str(x) for x in type1_bounds(before, half, half)],
            'type1_after_bounds': [str(x) for x in type1_bounds(after, half, half)],
            'type1_change_bounds': [str(x) for x in delta],
            'increase_witness_x1_x2_before': ['1/5', '1'],
            'increase_witness_x1_x2_after': ['4/5', '0'],
            'decrease_witness_x1_x2_before': ['1', '1/5'],
            'decrease_witness_x1_x2_after': ['0', '4/5']}


if __name__ == '__main__':
    print(json.dumps(example(), indent=2))

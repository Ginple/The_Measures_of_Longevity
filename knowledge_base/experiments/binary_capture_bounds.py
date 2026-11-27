#!/usr/bin/env python3
"""Sharp identification bounds for a synthetic two-category capture model.

Deterministic population fractions, known category labels, positive category
capture weights. No sampling uncertainty and no real-world data are implied.
Inputs use decimal strings; output floats are for display, not inference.
"""
from decimal import Decimal, InvalidOperation, localcontext
import json


def _decimal(value):
    if isinstance(value, bool):
        raise ValueError('boolean is not a numeric model parameter')
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError('invalid model parameter') from None
    if not result.is_finite():
        raise ValueError('parameters must be finite')
    return result


def prevalence(y, ratio):
    """Recover p for observed category-1 fraction y and relative capture ratio e1/e0."""
    y, ratio = _decimal(y), _decimal(ratio)
    if not 0 <= y <= 1 or ratio <= 0:
        raise ValueError('y must be in [0,1]; relative capture ratio must be positive')
    return y / (y + ratio * (1 - y))


def change_bounds(y0, y1, lower, upper, shared=False):
    """Sharp p1-p0 bounds if ratios are separate or are equal across times.

    Uncertainty in y or calibration is not modeled. 'shared' is the strong
    cross-time restriction r0=r1, not a statistical or causal guarantee.
    """
    y0, y1, lower, upper = map(_decimal, (y0, y1, lower, upper))
    if not 0 <= y0 <= 1 or not 0 <= y1 <= 1 or not 0 < lower <= upper:
        raise ValueError('invalid observed fractions or positive ratio interval')
    if not isinstance(shared, bool):
        raise ValueError('shared must be boolean')
    with localcontext() as ctx:
        ctx.prec = 50
        if not shared:
            lo = prevalence(y1, upper) - prevalence(y0, lower)
            hi = prevalence(y1, lower) - prevalence(y0, upper)
        else:
            def delta(r): return prevalence(y1, r) - prevalence(y0, r)
            candidates = [lower, upper]
            if 0 < y0 < 1 and 0 < y1 < 1 and y0 != y1:
                k0 = (1-y0)/y0
                k1 = (1-y1)/y1
                critical = Decimal(1) / (k0*k1).sqrt()
                if lower <= critical <= upper:
                    candidates.append(critical)
            vals = [delta(r) for r in candidates]
            lo, hi = min(vals), max(vals)
        return lo, hi


if __name__ == '__main__':
    for shared in (False, True):
        lo, hi = change_bounds('0.4','0.6','0.5','2',shared=shared)
        print(json.dumps({'model':'shared_ratio' if shared else 'independent_ratios',
                          'lower':str(lo),'upper':str(hi)}, ensure_ascii=False))
    print('Illustrative deterministic model only; no confidence interval or causal effect.')

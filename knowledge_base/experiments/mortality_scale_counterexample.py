"""Conditional illustrative scale check; NOT an audit of real input data."""
import json
import math


def compare_hazard_and_probability_scaling(q, hazard_ratio):
    if not (math.isfinite(q) and 0 <= q < 1 and math.isfinite(hazard_ratio) and hazard_ratio >= 0):
        raise ValueError('q must be in [0,1), hazard ratio finite and nonnegative')
    # Second expression requires constant proportional hazards across one year.
    return {'direct_multiple': q * hazard_ratio,
            'proportional_hazard_probability': 1 - (1 - q) ** hazard_ratio}


if __name__ == '__main__':
    print(json.dumps({'classification': 'SYNTHETIC conditional example; not source model data',
                      'q': .2, 'hazard_ratio': 1.79,
                      'result': compare_hazard_and_probability_scaling(.2, 1.79)}, indent=2))

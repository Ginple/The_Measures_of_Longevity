"""Synthetic missingness bounds and arithmetic on rounded published summaries.

Neither calculation reproduces trial models or uses patient-level data.
The arm bounds describe observed finite-arm proportions, not an identified ATE.
"""
from fractions import Fraction
import json


def observed_arm_bounds(successes, measured, assigned):
    """Sharp finite-group bounds for a binary outcome, missing unrestricted."""
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (successes, measured, assigned)):
        raise ValueError('integer counts required')
    if assigned <= 0 or not 0 <= successes <= measured <= assigned:
        raise ValueError('require 0 <= successes <= measured <= assigned, assigned > 0')
    return Fraction(successes, assigned), Fraction(successes + assigned - measured, assigned)


def contrast_bounds(treatment, control):
    tlo, thi = observed_arm_bounds(*treatment)
    clo, chi = observed_arm_bounds(*control)
    return tlo - chi, thi - clo


def recovery_bounds(loss_abs_interval, final_change_interval):
    """Bounds for 1 + final_change / loss_abs for positive loss and final >= 0."""
    lo, hi = loss_abs_interval
    flo, fhi = final_change_interval
    if lo <= 0 or hi < lo or flo < 0 or fhi < flo:
        raise ValueError('invalid intervals')
    return 1 + flo / hi, 1 + fhi / lo


def result():
    loss = (Fraction(265, 100), Fraction(275, 100))
    final = (Fraction(5, 100), Fraction(15, 100))
    low, high = recovery_bounds(loss, final)
    diff = contrast_bounds((30, 50, 100), (20, 50, 100))
    return {
        'scope': 'illustration only: no participant data; missing binary outcomes unconstrained',
        'synthetic_treatment_bounds': [float(v) for v in observed_arm_bounds(30, 50, 100)],
        'synthetic_control_bounds': [float(v) for v in observed_arm_bounds(20, 50, 100)],
        'synthetic_finite_arm_difference_bounds': [float(v) for v in diff],
        'published_rounded_ffm_derived_percent_bounds': [float(low * 100), float(high * 100)],
        'published_rounded_weight_regain_percent': float(Fraction(49, 90) * 100),
        'rounding_note': 'nearest 0.1 kg, intervals as conservative closed limits; LS means, not mean of individual ratios',
    }


if __name__ == '__main__':
    print(json.dumps(result(), indent=2))

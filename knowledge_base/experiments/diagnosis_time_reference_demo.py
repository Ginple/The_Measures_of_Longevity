"""Synthetic regression parametrization; not a DO-HEALTH data analysis.

A case indicator C and case-only time T=C*d give y=a+b*C+g*T.
Here d is defined only for cases, and T is set to zero for controls.
"""
from fractions import Fraction


def exact(value):
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    raise ValueError('use integers or exact Fractions')


def predict(intercept, case_effect, slope, case, case_time):
    if type(case) is not int or case not in (0, 1):
        raise ValueError('case must be 0 or 1')
    intercept, case_effect, slope, case_time = map(
        exact, (intercept, case_effect, slope, case_time))
    if not case and case_time != 0:
        raise ValueError('noncase has case-only time zero')
    return intercept + case_effect * case + slope * case_time


def shift_reference(case_effect, slope, reference):
    """For T_new=T-reference*C, return coefficient on C in new coordinates."""
    return exact(case_effect) + exact(slope) * exact(reference)


def main():
    # Hypothetical units; no correspondence to measured clock outcomes.
    a, b, g = Fraction(0), Fraction(0), Fraction(1)
    reference = Fraction(2)
    new_b = shift_reference(b, g, reference)
    print('Synthetic only: original case coefficient:', b)
    print('After shifting case-only time by 2:', new_b)
    for case, t in ((0, 0), (1, 1), (1, 2), (1, 3)):
        original = predict(a, b, g, case, t)
        shifted = predict(a, new_b, g, case, t - reference * case)
        print('case, original time, original prediction, shifted prediction:',
              case, t, original, shifted)


if __name__ == '__main__':
    main()

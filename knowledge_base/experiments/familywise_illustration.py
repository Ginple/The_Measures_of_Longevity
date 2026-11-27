"""Synthetic null-test example; not a test of any article's statistics."""
from fractions import Fraction
import json


def familywise_independent(n, alpha):
    """Exact probability of at least one false rejection for independent null tests."""
    if type(n) is not int or n < 0 or not isinstance(alpha, Fraction) or not 0 <= alpha <= 1:
        raise ValueError('n must be a nonnegative int and alpha a Fraction in [0, 1]')
    return 1 - (1 - alpha) ** n


def main():
    a = Fraction(1, 20)
    probability = familywise_independent(20, a)
    print(json.dumps({'classification': 'synthetic; independent null tests; not trial data',
                      'tests': 20, 'per_test_alpha': str(a),
                      'any_false_positive_exact': str(probability),
                      'any_false_positive_approx': float(probability),
                      'perfectly_correlated_tests_comparison': str(a),
                      'note': 'assumes each null test has exactly this type I error; not FDR'}, indent=2))


if __name__ == '__main__':
    main()

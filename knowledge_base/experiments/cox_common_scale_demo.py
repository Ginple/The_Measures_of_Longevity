"""Synthetic Cox partial-likelihood factors under a common risk-weight scale.

This is not a Cox model fitter, patient data analysis, or CANTOS reanalysis.
"""
from fractions import Fraction


def positive_fraction(value):
    if type(value) is not int and not isinstance(value, Fraction):
        raise ValueError('weights and scale must be exact integers or Fractions')
    value = Fraction(value)
    if value <= 0:
        raise ValueError('weights and scale must be positive')
    return value


def event_probability(weights, event_index):
    weights = tuple(positive_fraction(w) for w in weights)
    if not weights or type(event_index) is not int or not 0 <= event_index < len(weights):
        raise ValueError('nonempty risk set and valid integer event index required')
    return weights[event_index] / sum(weights)


def main():
    # Hypothetical X values and a treatment multiplier: exp(log(2)*z).
    # For coefficient ln(2) on log2(X), exp(ln(2)*log2(X))=X.
    weights = [2, 8, 16]  # X=[2,4,8], z=[0,1,1]
    rescaled = [Fraction(w, 10) for w in weights]
    for i in range(len(weights)):
        print(f'synthetic event {i}: {event_probability(weights, i)} = '
              f'{event_probability(rescaled, i)}')


if __name__ == '__main__':
    main()

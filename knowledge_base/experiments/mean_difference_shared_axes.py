"""Synthetic finite-population algebra for shared mean/difference axes.

No WHO observations, inference, regressions of actual data, or clinical claims.
"""
from fractions import Fraction as F
import json


def _number(value):
    if type(value) is int or isinstance(value, F):
        return F(value)
    raise ValueError('values must be integers or exact Fractions')


def sample_covariance(first, second):
    if len(first) != len(second) or len(first) < 2:
        raise ValueError('equal-length sequences of at least two values required')
    a, b = tuple(map(_number, first)), tuple(map(_number, second))
    mean_a, mean_b = sum(a) / len(a), sum(b) / len(b)
    return sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b)) / (len(a) - 1)


def describe(life, healthy):
    if len(life) != len(healthy) or len(life) < 2:
        raise ValueError('equal-length sequences of at least two values required')
    life, healthy = tuple(map(_number, life)), tuple(map(_number, healthy))
    if any(h < 0 or l < h for l, h in zip(life, healthy)):
        raise ValueError('require 0 <= healthy <= life for each synthetic row')
    midpoint = tuple((l + h) / 2 for l, h in zip(life, healthy))
    gap = tuple(l - h for l, h in zip(life, healthy))
    return {'midpoint': midpoint, 'gap': gap,
            'cov_midpoint_gap': sample_covariance(midpoint, gap),
            'half_difference_of_variances': (sample_covariance(life, life) -
                                              sample_covariance(healthy, healthy)) / 2}


def main():
    examples = {'positive': ([70, 80, 90], [60, 65, 70]),
                'negative': ([70, 75, 80], [50, 65, 80]),
                'zero': ([68, 68, 72, 72], [58, 62, 58, 62])}
    for name, (life, healthy) in examples.items():
        result = describe(life, healthy)
        print(json.dumps({'world': name, 'classification': 'synthetic, not WHO data',
                          'life': life, 'healthy': healthy,
                          'covariance': str(result['cov_midpoint_gap']),
                          'variance_identity': str(result['half_difference_of_variances'])}))


if __name__ == '__main__':
    main()

"""Two synthetic worlds: a randomized treatment does not randomize its mediator.

All probabilities are exact and structural interventions are fictional. No
trial data, error estimates, or claims of scientific proof are produced.
"""
from fractions import Fraction as F
from collections import defaultdict
import json


def mediator(z, u):
    return z ^ u


def outcome(world, z, m, u):
    if world == 'mediated':
        return m
    if world == 'direct':
        return z ^ u
    raise ValueError('unknown world')


def summarize(world):
    # Z is an independent fair assignment; U has P(U=1)=1/4.
    observed = defaultdict(F)
    base = total_end = direct_end = F(0)
    for z in (0, 1):
        for u, p_u in ((0, F(3, 4)), (1, F(1, 4))):
            m = mediator(z, u)
            observed[(z, m, outcome(world, z, m, u))] += F(1, 2) * p_u
    for u, p_u in ((0, F(3, 4)), (1, F(1, 4))):
        m0, m1 = mediator(0, u), mediator(1, u)
        base += p_u * outcome(world, 0, m0, u)
        direct_end += p_u * outcome(world, 1, m0, u)
        total_end += p_u * outcome(world, 1, m1, u)
    return {'observed': dict(sorted(observed.items())),
            'total_effect': total_end - base,
            'natural_direct_effect_at_M0': direct_end - base,
            'natural_indirect_effect_at_Z1': total_end - direct_end}


def main():
    for world in ('mediated', 'direct'):
        result = summarize(world)
        print(json.dumps({'world': world, 'observed': [
            {'Z': z, 'M': m, 'Y': y, 'probability': str(prob)}
            for (z, m, y), prob in result['observed'].items()],
            'total_effect': str(result['total_effect']),
            'natural_direct_effect_at_M0': str(result['natural_direct_effect_at_M0']),
            'natural_indirect_effect_at_Z1': str(result['natural_indirect_effect_at_Z1'])}))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Fabricated counterexample: random Z does not randomize a post-Z trajectory.

Adapted from PR #1 at 52362b6, with attribution; synthetic, not patient data.
Two structural worlds share the full distribution of (Z, X, Y), but differ
under interventions setting X. X is a toy binary trajectory, not CALERIE data.
"""
from fractions import Fraction as F
from collections import Counter
import json


def y(world, z, u, x):
    if world == 'A':
        return x
    if world == 'B':
        return int(bool(z or u))
    raise ValueError('unknown world')


def observed(world):
    """Z and latent U are independent fair bits; X=Z OR U."""
    counts = Counter()
    for z in (0, 1):
        for u in (0, 1):
            x = int(bool(z or u))
            counts[(z, x, y(world, z, u, x))] += 1
    return {k: F(v, 4) for k, v in sorted(counts.items())}


def do_x_mean(world, x):
    if x not in (0, 1):
        raise ValueError('X must be 0 or 1')
    return F(sum(y(world, z, u, x) for z in (0, 1) for u in (0, 1)), 4)


def main():
    result = {'classification': 'SYNTHETIC only; no trial or human data',
              'observed_joint_z_x_y': {str(k): str(v) for k, v in observed('A').items()},
              'identical_observed_joint': observed('A') == observed('B'),
              'mean_do_x0': {w: str(do_x_mean(w, 0)) for w in ('A', 'B')},
              'mean_do_x1': {w: str(do_x_mean(w, 1)) for w in ('A', 'B')},
              'effect_do_x1_minus_do_x0': {w: str(do_x_mean(w, 1)-do_x_mean(w, 0))
                                         for w in ('A', 'B')}}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

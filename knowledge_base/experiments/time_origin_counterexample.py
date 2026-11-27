#!/usr/bin/env python3
"""Artificial event trajectories: moving observation origin can alter counts.

Not HARP data, not a hazard-ratio estimator, and not a bias estimate. Events
before the observation window are ignored; participants remain observed even
if they experienced an earlier event. Integer day intervals are [start, end).
"""
from fractions import Fraction
import json


def first_observed_risk(trajectories, start, duration):
    if not trajectories or type(start) is not int or type(duration) is not int or start < 0 or duration < 1:
        raise ValueError('nonempty trajectories and nonnegative integer start; positive integer duration required')
    affected = 0
    for events in trajectories:
        if any(type(day) is not int or day < 0 for day in events):
            raise ValueError('event days must be nonnegative integers')
        if any(start <= day < start + duration for day in events):
            affected += 1
    return Fraction(affected, len(trajectories))


def example():
    # The same four trajectories in both arms under both potential treatments:
    # any true effect on the fixed randomization-origin risk is exactly zero.
    people = ((1,), (1,), (3,), ())
    fixed0 = first_observed_risk(people, 0, 4)
    fixed1 = first_observed_risk(people, 0, 4)
    control_window = first_observed_risk(people, 0, 4)
    delayed_window = first_observed_risk(people, 2, 4)
    return {'fixed_control':fixed0,'fixed_treatment':fixed1,
            'observed_control':control_window,'observed_delayed':delayed_window}


if __name__ == '__main__':
    results=example()
    print(json.dumps({key:str(value) for key,value in results.items()},indent=2))
    print('Synthetic finite populations only: different windows and risk proportions, not an HR or real trial.')

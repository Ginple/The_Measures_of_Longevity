#!/usr/bin/env python3
"""Demonstrate why SD across clocks is not person-level uncertainty.

Synthetic data, no experimental observations or actual trial estimates.
"""
from math import sqrt
from statistics import mean, stdev


def example():
    person_effects = [0., 2.]  # hypothetical treatment-group participants
    clock_offsets = [-1., 0., 1.] * 12  # 36 perfectly dependent repeated readouts
    clock_group_means = [mean(effect + offset for effect in person_effects)
                         for offset in clock_offsets]
    return {
        'group_mean_across_clocks': mean(clock_group_means),
        'se_across_clock_means': stdev(clock_group_means) / sqrt(len(clock_group_means)),
        'se_across_persons_for_mean': stdev(person_effects) / sqrt(len(person_effects)),
        'people': len(person_effects), 'clocks': len(clock_offsets),
    }


if __name__ == '__main__':
    for k, v in example().items(): print(f'{k}: {v}')
    print('Contrived repeated outcomes, not a valid CI or real trial reanalysis.')

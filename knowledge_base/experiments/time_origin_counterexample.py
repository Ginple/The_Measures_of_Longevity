"""Synthetic timeline illustrating unequal calendar windows, not a HARP reanalysis.

Everyone is alive, under surveillance for 395 days, and has at most one fall.
Both groups have identical potential event days: there is no causal effect.
Groups are measured over equally long 365-day windows with distinct origins.
"""
import json


def observed_risk(first_days, start, length=365):
    if not first_days or start < 0 or length <= 0:
        raise ValueError('need nonempty cohort, nonnegative start and positive length')
    # Windows are (start, start + length] in days. A prior event is not a
    # post-origin event; no statement is made about original study risk sets.
    count = sum(day is not None and start < day <= start + length for day in first_days)
    return count / len(first_days)


def examples():
    early_peak = [10]*20 + [100]*30 + [380]*5 + [None]*45
    late_peak = [10]*5 + [100]*30 + [380]*20 + [None]*45
    return {'classification': 'SYNTHETIC; NOT TRIAL DATA OR A HAZARD-RATIO REANALYSIS',
            'early_peak': {'baseline_origin': observed_risk(early_peak, 0),
                           'delayed_origin': observed_risk(early_peak, 30)},
            'late_peak': {'baseline_origin': observed_risk(late_peak, 0),
                          'delayed_origin': observed_risk(late_peak, 30)}}


if __name__ == '__main__':
    print(json.dumps(examples(), indent=2))

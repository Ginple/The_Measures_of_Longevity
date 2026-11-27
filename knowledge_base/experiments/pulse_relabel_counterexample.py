#!/usr/bin/env python3
"""Identical measured labeled counts, different original-cohort retention.

Deterministic synthetic stock accounting with fractional cell equivalents;
not measurements, fitted kinetics, or a lineage tracing simulator.
"""
from fractions import Fraction as F
import json


def evolve(initial, exit_fraction, relabel_amounts):
    total, labeled, initial_cohort = map(F, (initial, initial, initial))
    k = F(exit_fraction)
    if total <= 0 or not 0 <= k <= 1:
        raise ValueError('initial stock must be positive and exit fraction in [0,1]')
    states = [{'total': total, 'labeled': labeled, 'initial_cohort': initial_cohort}]
    for amount in relabel_amounts:
        amount = F(amount)
        # Every interval, k of each subgroup exits; equal new unlabeled inputs
        # restore the total. New arrivals are available for labeling.
        retained = labeled * (1-k)
        entrants = total*k
        unlabeled_available = total-retained
        if amount < 0 or amount > unlabeled_available:
            raise ValueError('relabel exceeds available unlabeled stock')
        labeled = retained + amount
        initial_cohort *= (1-k)
        states.append({'total': total, 'labeled': labeled, 'initial_cohort': initial_cohort,
                       'exit_total': entrants, 'new_entries': entrants, 'relabel': amount})
    return states


def main():
    cases = {'closed_pulse': evolve(100, F(1,4), [0, 0]),
             'continued_labeling': evolve(100, F(1,2), [25, F(75,4)])}
    print(json.dumps({name: [{k: str(v) for k, v in row.items()} for row in rows]
                      for name, rows in cases.items()}, indent=2))


if __name__ == '__main__':
    main()

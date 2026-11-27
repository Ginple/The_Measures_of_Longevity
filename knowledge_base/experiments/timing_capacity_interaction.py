#!/usr/bin/env python3
"""Synthetic discrete queue; exact arithmetic, not fitted or clinical."""
from fractions import Fraction as F
import json


def simulate(arrivals, capacity, initial=0):
    """Arrivals appear at interval start; serve at most capacity each interval."""
    arrivals = tuple(map(F, arrivals))
    capacity, q = F(capacity), F(initial)
    if not arrivals or capacity < 0 or q < 0 or any(x < 0 for x in arrivals):
        raise ValueError('nonempty, nonnegative arrivals and capacity/backlog required')
    states = []
    for arrival in arrivals:
        available = q + arrival
        served = min(available, capacity)
        q = available - served
        states.append((served, q))
    return states


def score(arrivals, capacity):
    return sum((q for _, q in simulate(arrivals, capacity)), F(0))


def main():
    inputs = {'even': [1, 1], 'pulse': [F(3, 2), F(1, 2)]}
    capacities = {'preserved': F(3, 2), 'reduced': F(3, 4)}
    values = {(a, c): score(v, cap) for a, v in inputs.items() for c, cap in capacities.items()}
    interaction = (values['pulse', 'reduced'] - values['even', 'reduced']
                   - values['pulse', 'preserved'] + values['even', 'preserved'])
    print(json.dumps({'scores': {f'{a}_{c}': str(v) for (a, c), v in values.items()},
                      'difference_in_differences': str(interaction),
                      'scope': 'Synthetic exact model, not clinical data'}, indent=2))


if __name__ == '__main__':
    main()

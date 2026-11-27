#!/usr/bin/env python3
"""Exact finite-horizon queue illustrating time-varying service (synthetic)."""
from fractions import Fraction as F
import json


def simulate(arrivals, capacities, initial=0):
    arrivals, capacities = tuple(map(F, arrivals)), tuple(map(F, capacities))
    q = F(initial)
    if not arrivals or len(arrivals) != len(capacities) or q < 0:
        raise ValueError('equal nonempty schedules and nonnegative initial stock required')
    if any(x < 0 for x in arrivals + capacities):
        raise ValueError('negative arrivals or capacity')
    result = []
    for arrival, capacity in zip(arrivals, capacities):
        served = min(q + arrival, capacity)
        q += arrival - served
        result.append((served, q))
    return result


def main():
    scenarios = {'even': ([1, 1], [F(1, 2), F(3, 2)]),
                 'pulse': ([F(3, 2), F(1, 2)], [F(3, 2), F(1, 2)])}
    result = {}
    for key, (a, c) in scenarios.items():
        x = simulate(a, c)
        result[key] = {'arrivals': [str(v) for v in a],
                       'capacity': [str(v) for v in c],
                       'served': [str(s) for s, q in x],
                       'end_backlog': [str(q) for s, q in x],
                       'sum_end_backlog': str(sum((q for s, q in x), F(0)))}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

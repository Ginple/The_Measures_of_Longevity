#!/usr/bin/env python3
"""Synthetic source queue with simultaneous edge + receiver constraints.

Input arrives before service each period; no intermediate buffer. Exact amounts.
"""
from fractions import Fraction as F
import json


def simulate(arrivals, edges, receivers):
    a, e, r = (tuple(map(F, v)) for v in (arrivals, edges, receivers))
    if not a or len(a) != len(e) or len(a) != len(r):
        raise ValueError('schedules must be nonempty and equally long')
    if any(x < 0 for x in a + e + r):
        raise ValueError('amounts and capacities must be nonnegative')
    q = F(0)
    result = []
    for incoming, edge, receiver in zip(a, e, r):
        q += incoming
        processed = min(q, edge, receiver)
        q -= processed
        result.append((processed, q))
    return result


def aggregate_upper_bound(arrivals, edges, receivers):
    a, e, r = (tuple(map(F, v)) for v in (arrivals, edges, receivers))
    if not a or len(a) != len(e) or len(a) != len(r) or any(x < 0 for x in a + e + r):
        raise ValueError('invalid nonempty nonnegative schedules')
    return min(sum(a), sum(e), sum(r))


def main():
    arrivals, edges = [1, 0], [1, 0]
    schedules = {'aligned': [1, 0], 'misaligned': [0, 1]}
    result = {}
    for name, capacities in schedules.items():
        states = simulate(arrivals, edges, capacities)
        result[name] = {'static_upper_bound': str(aggregate_upper_bound(arrivals, edges, capacities)),
                        'processed': str(sum((p for p, q in states), F(0))),
                        'backlog_end': str(states[-1][1])}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

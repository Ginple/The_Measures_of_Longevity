#!/usr/bin/env python3
"""Sharp set-theoretic complete-case bounds under a fixed common cohort.

This does not estimate outcomes, missingness mechanisms, or effective model n.
"""
import json


def complete_case_bounds(n, missing_counts):
    """Return sharp bounds and explicit missing-index witnesses on range(n)."""
    counts = tuple(missing_counts)
    if type(n) is not int or n < 0:
        raise ValueError('n must be a nonnegative integer')
    if any(type(m) is not int or m < 0 or m > n for m in counts):
        raise ValueError('missing counts must be integers between 0 and n')

    # Largest possible union: fill consecutive slots, wrapping only if needed.
    maximum_union = []
    cursor = 0
    for m in counts:
        maximum_union.append(set((cursor + i) % n for i in range(m)))
        cursor += m
    # Smallest possible union: nest all missing sets inside the largest set.
    minimum_union = [set(range(m)) for m in counts]
    lower = max(0, n - sum(counts))
    upper = n - max(counts, default=0)
    return lower, upper, maximum_union, minimum_union


def main():
    n = 190
    m = (57, 33, 6)
    low, high, lo_witness, hi_witness = complete_case_bounds(n, m)
    result = {
        'interpretation': 'conditional set arithmetic, NOT actual complete cases or patient data',
        'assumed_shared_cohort': n,
        'reported_missing_by_time': list(m),
        'possible_complete_all_three': [low, high],
        'witness_missing_sizes': [list(map(len, w)) for w in (lo_witness, hi_witness)],
        'witness_complete_counts': [n - len(set().union(*w)) for w in (lo_witness, hi_witness)],
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

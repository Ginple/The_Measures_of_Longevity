#!/usr/bin/env python3
"""Artificial example: repeated clock labels do not create independent people."""
from math import sqrt
from statistics import mean, stdev


def summarize(repeats):
    if type(repeats) is not int or repeats < 1:
        raise ValueError('repeats must be a positive integer')
    people = (0.0, 2.0)
    offsets = (-1.0, 0.0, 1.0) * repeats
    clock_means = [mean(x + offset for x in people) for offset in offsets]
    return {
        'people': len(people), 'clock_labels': len(offsets),
        'grand_mean': mean(clock_means),
        'se_clock_means': stdev(clock_means) / sqrt(len(clock_means)),
        'se_person_mean': stdev(people) / sqrt(len(people)),
    }


if __name__ == '__main__':
    for n in (1, 12, 120):
        print(n, summarize(n))
    print('Synthetic repeated outcomes; neither SE is a treatment contrast CI.')

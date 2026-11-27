"""Synthetic only: distinguish repeated-event rates, risks, and ratio summaries.

These examples are not trial data and do not reconstruct any published model.
"""
from statistics import median
import json


def fall_summary(counts):
    """Equal one-year observation for each hypothetical person; no censoring."""
    if not counts:
        raise ValueError('need at least one person')
    if any(isinstance(n, bool) or not isinstance(n, int) or n < 0 for n in counts):
        raise ValueError('counts must be nonnegative integers')
    return {'persons': len(counts), 'person_years': len(counts),
            'people_falling': sum(n > 0 for n in counts),
            'fall_risk': sum(n > 0 for n in counts) / len(counts),
            'events': sum(counts), 'fall_rate_per_person_year': sum(counts) / len(counts)}


def ratio_summaries(pairs):
    """Compare marginal-extrema/median-denominator to paired run ratios."""
    if not pairs:
        raise ValueError('need at least one pair')
    for n, d in pairs:
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (n, d)) or d <= 0 or not 0 <= n <= d:
            raise ValueError('integer counts with 0 <= numerator <= positive denominator required')
    numerators = [n for n, _ in pairs]
    denominators = [d for _, d in pairs]
    ratios = [n/d for n, d in pairs]
    med_denom = median(denominators)
    return {'ratio_of_marginal_medians': median(numerators)/med_denom,
            'marginal_extrema_over_median_denominator': [min(numerators)/med_denom, max(numerators)/med_denom],
            'median_paired_ratio': median(ratios),
            'range_paired_ratios': [min(ratios), max(ratios)]}


def examples():
    # Both arms have 50 fallers in 100 people; recurrent fall counts differ.
    control = [3]*25 + [1]*25 + [0]*50
    intervention = [2]*10 + [1]*40 + [0]*50
    pairs = [(1, 10)] + [(2, 100)]*8 + [(9, 10)]
    return {'classification': 'SYNTHETIC ONLY / NOT A CLINICAL OR MODEL ESTIMATE',
            'control': fall_summary(control), 'intervention': fall_summary(intervention),
            'summary_counterexample': ratio_summaries(pairs)}


if __name__ == '__main__':
    print(json.dumps(examples(), indent=2))

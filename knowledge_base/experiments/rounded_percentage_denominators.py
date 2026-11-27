"""Candidate denominators under an explicit nearest-rounding convention.

Percentages are decimal strings, kept exact; ties at a rounding boundary are
allowed on both sides. This is arithmetic, not inference about actual cohorts.
"""
from fractions import Fraction
import json


def candidate_denominators(observations, min_n, max_n, decimal_places=1):
    """Return integer denominators consistent with every (count, percent) pair.

    The search range is finite and inclusive; 0.05 percentage-point boundaries
    for 1 decimal place are conservatively included to avoid assuming tie rules.
    """
    if (type(min_n) is not int or type(max_n) is not int or min_n < 1
            or max_n < min_n or type(decimal_places) is not int
            or not 0 <= decimal_places <= 6):
        raise ValueError('invalid denominator range or precision')
    pairs = []
    step = Fraction(1, 10 ** decimal_places)
    for count, pct_text in observations:
        if type(count) is not int or count < 0 or not isinstance(pct_text, str):
            raise ValueError('counts must be nonnegative integers; percentages decimal strings')
        try:
            pct = Fraction(pct_text)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError('invalid percentage') from exc
        if not 0 <= pct <= 100 or pct / step != int(pct / step):
            raise ValueError('percentage must be in range and at the stated precision')
        pairs.append((count, pct))
    return [n for n in range(min_n, max_n + 1)
            if all(count <= n and abs(Fraction(100 * count, n) - pct) <= step / 2
                   for count, pct in pairs)]


def main():
    # Extracted aggregate rows from the versioned CALERIE S3; not participant data.
    rows = [(3, '1.6'), (2, '1.0'), (1, '0.5'), (4, '2.1'),
            (5, '2.6'), (8, '4.2'), (42, '22.0'),
            (33, '17.3'), (57, '29.8'), (6, '3.1')]
    print(json.dumps({'source': 'CALERIE 2026 S3, reported aggregate rows',
                      'conditional_rule': 'one common integer denominator; nearest 0.1 percentage point; ties included',
                      'range': [57, 1000],
                      'candidates_all_rows': candidate_denominators(rows, 57, 1000),
                      'candidates_57_row': candidate_denominators([(57, '29.8')], 57, 1000),
                      'not_established': 'actual denominator, cohort membership, or complete-case count'}, indent=2))


if __name__ == '__main__':
    main()

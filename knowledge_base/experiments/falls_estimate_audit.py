"""Transparent arithmetic audit; no meta-analysis or patient-level reconstruction.

Cochrane table values are published rounded illustrative numbers. The denominator
comparison is conditional on published HARP and review appendix numbers being
for the same groups/endpoint. No assumptions about the unseen forest plot.
"""
from math import isfinite
import json


def absolute_projection(control_per_thousand, rr, rr_ci):
    if not isfinite(control_per_thousand) or not 0 <= control_per_thousand <= 1000:
        raise ValueError('control risk must be between 0 and 1000')
    lo, hi = rr_ci
    if not all(isfinite(x) and x >= 0 for x in (rr, lo, hi)) or not lo <= rr <= hi:
        raise ValueError('nonnegative ordered relative risks required')
    return {'expected_per_thousand': control_per_thousand * rr,
            'conditional_ci_per_thousand': [control_per_thousand * lo, control_per_thousand * hi],
            'fewer_per_thousand': control_per_thousand * (1 - rr)}


def risk_ratio(intervention_events, intervention_total, control_events, control_total):
    for events, total in ((intervention_events, intervention_total), (control_events, control_total)):
        if isinstance(events, bool) or isinstance(total, bool) or not isinstance(events, int) or not isinstance(total, int) or total <= 0 or not 0 <= events <= total:
            raise ValueError('invalid integer counts')
    if control_events == 0:
        raise ValueError('control risk must be positive')
    return (intervention_events / intervention_total) / (control_events / control_total)


def report():
    projection = absolute_projection(550, .74, (.65, .85))
    return {'scope': 'reported rounded aggregate values; arithmetic only; not a meta-analysis',
            'high_risk_projection': projection,
            'published_high_risk_corresponding': 461,
            'rounding_upper_bound_for_projection': 550.5 * .745,
            'harp_rr_paper_denominators': risk_ratio(67, 135, 74, 140),
            'harp_rr_review_appendix_denominators': risk_ratio(67, 140, 74, 135)}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, ensure_ascii=False))

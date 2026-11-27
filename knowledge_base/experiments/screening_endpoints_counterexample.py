"""Synthetic screening counterexamples; no real people, no trial replication.

Two binary screening assignments are compared at a fixed horizon in separate
hypothetical worlds. Counts are per 1,000 randomized people; all cases are
assumed staged and followed to the same horizon. These are *not* estimates of
NHS-Galleri or of any real intervention.
"""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Arm:
    total: int
    early: int
    late: int
    deaths: int
    overdiagnoses: int = 0

    def __post_init__(self):
        if any(not isinstance(v, int) or isinstance(v, bool) for v in (self.total, self.early, self.late, self.deaths, self.overdiagnoses)):
            raise ValueError('counts must be integers')
        if self.total <= 0 or min(self.early, self.late, self.deaths, self.overdiagnoses) < 0:
            raise ValueError('counts must be nonnegative and total positive')
        if self.early + self.late > self.total or self.overdiagnoses > self.early + self.late:
            raise ValueError('invalid diagnoses or overdiagnoses')
        if self.deaths > self.early + self.late - self.overdiagnoses:
            raise ValueError('modeled cancer deaths cannot exceed non-overdiagnosed cases')

    def metrics(self):
        diagnosed = self.early + self.late
        return {'population': self.total, 'early': self.early, 'late': self.late,
                'diagnosed': diagnosed, 'overdiagnoses': self.overdiagnoses,
                'late_fraction_among_diagnosed': self.late / diagnosed if diagnosed else None,
                'late_risk_all_randomized': self.late / self.total,
                'cancer_death_risk_all_randomized': self.deaths / self.total}


def median_ratio_demo():
    """Medians are not generally closed under division; three artificial runs."""
    from statistics import median
    runs = [(1, 1), (2, 100), (100, 1)]  # true positives, false positives
    median_tp = median(tp for tp, _ in runs)
    median_fp = median(fp for _, fp in runs)
    return {'runs': runs,
            'ratio_of_medians': median_tp / (median_tp + median_fp),
            'median_of_runwise_ratios': median(tp / (tp + fp) for tp, fp in runs)}


def examples():
    control = Arm(1000, early=20, late=80, deaths=50)
    worlds = {
        'extra_early_overdiagnoses_same_late_and_mortality': Arm(1000, early=120, late=80, deaths=50, overdiagnoses=100),
        'same_stage_shift_no_mortality_benefit': Arm(1000, early=70, late=30, deaths=50),
        'same_stage_shift_with_mortality_benefit': Arm(1000, early=70, late=30, deaths=30),
    }
    return {'classification': 'SYNTHETIC COUNTEREXAMPLE / NOT A CLINICAL ESTIMATE',
            'control': control.metrics(), 'intervention_worlds': {k: v.metrics() for k, v in worlds.items()},
            'median_ratio_demo': median_ratio_demo(),
            'interpretation': 'A lower late-stage proportion need not lower late-stage incidence; even equal stage distributions do not identify mortality effects.'}


if __name__ == '__main__':
    print(json.dumps(examples(), ensure_ascii=False, indent=2))

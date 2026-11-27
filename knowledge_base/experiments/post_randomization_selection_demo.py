"""Synthetic randomized-selection example; no trial or patient data.

Balanced assignment within four equal latent strata. The outcome is identical
under both assignments, while detection can depend on assignment and stratum.
"""
import json
from fractions import Fraction


def demo():
    # name, binary outcome, detectable under control, detectable under treatment
    strata = [('high_treatment_only', 1, 0, 1),
              ('low_control_only', 0, 1, 0),
              ('high_both', 1, 1, 1),
              ('low_both', 0, 1, 1)]
    n_per_arm_stratum = 25
    arms = {}
    for treatment in (0, 1):
        total = sum(n_per_arm_stratum for _ in strata)
        positive = sum(y*n_per_arm_stratum for _, y, _, _ in strata)
        eligible = [s for s in strata if s[2+treatment]]
        selected_n = len(eligible)*n_per_arm_stratum
        selected_positive = sum(s[1]*n_per_arm_stratum for s in eligible)
        arms['treatment' if treatment else 'control'] = {
            'all_n': total, 'all_positive': positive,
            'all_risk': str(Fraction(positive, total)),
            'selected_n': selected_n, 'selected_positive': selected_positive,
            'selected_risk': str(Fraction(selected_positive, selected_n)),
        }
    arms['selected_difference_treatment_minus_control'] = str(
        Fraction(arms['treatment']['selected_positive'], arms['treatment']['selected_n']) -
        Fraction(arms['control']['selected_positive'], arms['control']['selected_n']))
    return {'classification': 'synthetic; not observed patient data', 'arms': arms}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2))

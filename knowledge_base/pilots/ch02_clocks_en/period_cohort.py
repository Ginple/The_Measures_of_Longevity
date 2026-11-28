"""Period versus cohort life expectancy in one synthetic population.

SYNTHETIC. No real data. Purpose (English chapter 2, section 1): show that a period life expectancy
summarises one calendar year's death rates and is not a forecast for anyone born that year, and that an
average age at death says little about when any one person dies.

Model: a Gompertz hazard mu(age, year) = A * exp(B * age) * exp(-R * year), with A = 5e-5, B = 0.095
per year of age and R = 0.01 (all death rates fall by 1 percent per calendar year, for ever).
- Period life expectancy in year 0: every age is exposed to the year-0 rates.
- Cohort life expectancy for people born in year 0: at age x they meet the rates of year x.
Survival is integrated numerically with step H (midpoint rule) up to age 130. Results are rounded.

Tail comparison (chapter 2, section 4), using year-0 rates only: among people alive at 105, the chance of
reaching 110, 115 and 122 if the hazard keeps rising exponentially, versus if it stops rising at 105 and stays
at its age-105 value (a plateau). The two tails share everything up to 105; only the assumption differs.
"""
import json
import math
from pathlib import Path

A, B, R = 5e-5, 0.095, 0.01
H = 0.01
MAX_AGE = 130
OUT = Path(__file__).resolve().parent / 'evidence/PERIOD_COHORT_SYNTHETIC_output.json'


def survival_curve(cohort):
    """Return list of (age, survival) on the grid; cohort=True lets rates fall with the person's age."""
    s, out = 1.0, [(0.0, 1.0)]
    n = int(MAX_AGE / H)
    for i in range(n):
        x = (i + 0.5) * H
        mu = A * math.exp(B * x) * (math.exp(-R * x) if cohort else 1.0)
        s *= math.exp(-mu * H)
        out.append(((i + 1) * H, s))
    return out


def summary(curve):
    le = sum((curve[i][1] + curve[i + 1][1]) / 2 * H for i in range(len(curve) - 1))

    def age_at(p):  # age by which a share p of the population has died
        return next(a for a, s in curve if s <= 1 - p)
    died_before_le = 1 - next(s for a, s in curve if a >= le)
    return dict(life_expectancy=round(le, 1), share_dying_before_life_expectancy=round(died_before_le, 2),
                age_by_which_25pct_died=round(age_at(0.25), 1), age_by_which_75pct_died=round(age_at(0.75), 1))


def tail_from_105(plateau):
    mu105 = A * math.exp(B * 105)
    out = {}
    for target in (110, 115, 122):
        if plateau:
            p = math.exp(-mu105 * (target - 105))
        else:  # closed form of the integral of A*exp(B*x) from 105 to target
            p = math.exp(-A / B * (math.exp(B * target) - math.exp(B * 105)))
        out[f'reach_{target}'] = float(f'{p:.2g}')
    return out


def build():
    period, cohort = summary(survival_curve(False)), summary(survival_curve(True))
    return dict(nature='SYNTHETIC illustration; no real data', script='knowledge_base/pilots/ch02_clocks_en/period_cohort.py',
                parameters=dict(A=A, B=B, R=R, step=H, max_age=MAX_AGE),
                period_year0=period, cohort_born_year0=cohort,
                cohort_minus_period_years=round(cohort['life_expectancy'] - period['life_expectancy'], 1),
                annual_hazard_at_105=round(A * math.exp(B * 105), 2),
                annual_death_probability_at_105=round(1 - math.exp(-A * math.exp(B * 105)), 2),
                tail_given_alive_at_105=dict(hazard_keeps_rising=tail_from_105(False), hazard_flat_after_105=tail_from_105(True)),
                flat_over_rising_ratio={f'reach_{t}': float(f'{tail_from_105(True)[f"reach_{t}"] / tail_from_105(False)[f"reach_{t}"]:.2g}')
                                        for t in (110, 115, 122)})


if __name__ == '__main__':
    data = build()
    OUT.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))

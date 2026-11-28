"""Three synthetic populations with the same life expectancy, health-adjusted life expectancy and gap.

SYNTHETIC. No WHO or other real data. Exact arithmetic with fractions.
Purpose (English chapter 1, section 2): show that a population average gap between life expectancy and
health-adjusted life expectancy is not a forecast of any one person's years in poor health, and that the
same summary can come from very different lives.

Each population has 100 people. Each person is a list of (years lived in an interval, health-loss weight
in that interval), where weight 0 is full health and 1 is the worst health state. A person's equivalent
lost years are sum(years * weight). Life expectancy is the mean of years lived; health-adjusted life
expectancy is life expectancy minus the mean equivalent lost years.
- A: 20 people die at 10 and 80 die at 20; everyone alive carries weight 0.10 in years 0-10 and 0.25 in 10-20.
- B: all 100 die at 18; weight 0.10 in years 0-10 and 0.25 in years 10-18.
- C: as A for deaths, but in years 10-20 20 of the 80 survivors carry weight 1 and 60 carry weight 0
  (the interval's average weight is still 20/80 = 0.25).
"""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'evidence/LIFE_TABLE_SYNTHETIC_output.json'


def population(name):
    a, q = F(1, 10), F(1, 4)
    if name == 'A':
        return [[(10, a)]] * 20 + [[(10, a), (10, q)]] * 80
    if name == 'B':
        return [[(10, a), (8, q)]] * 100
    if name == 'C':
        return [[(10, a)]] * 20 + [[(10, a), (10, F(1))]] * 20 + [[(10, a), (10, F(0))]] * 60
    raise ValueError(name)


def summary(people):
    n = len(people)
    lived = [sum(F(y) for y, _ in p) for p in people]
    lost = [sum(F(y) * w for y, w in p) for p in people]
    le = sum(lived) / n
    gap = sum(lost) / n
    def dist(xs):
        return {str(k): v for k, v in sorted(Counter(xs).items())}
    return {
        'n': n,
        'life_expectancy': str(le),
        'health_adjusted_life_expectancy': str(le - gap),
        'gap_equivalent_lost_years': str(gap),
        'ages_at_death': dist(lived),
        'equivalent_lost_years_per_person': dist(lost),
        'people_dying_at_life_expectancy': sum(1 for x in lived if x == le),
        'people_whose_loss_equals_gap': sum(1 for x in lost if x == gap),
    }


def build():
    return {
        'nature': 'SYNTHETIC illustration; no real data; exact fractions',
        'script': 'knowledge_base/pilots/ch01_measure_en/synthetic_life_table.py',
        'populations': {k: summary(population(k)) for k in 'ABC'},
    }


if __name__ == '__main__':
    OUT.write_text(json.dumps(build(), indent=2) + '\n', encoding='utf-8')
    print(OUT.read_text(encoding='utf-8'))

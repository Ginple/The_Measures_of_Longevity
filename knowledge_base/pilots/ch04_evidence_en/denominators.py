"""SYNTHETIC illustrations for chapter 4 (English). No real data; exact fractions.

Part A, reversal. Two treatments, new and old, given to 800 patients each.
- Mild patients: new 200 treated, 180 recover; old 600 treated, 520 recover.
- Severe patients: new 600 treated, 300 recover; old 200 treated, 80 recover.
The new treatment does better within each group but worse overall, because it was
given mostly to severe patients.

Part B, many readouts. If an intervention has no effect and each of 16 independent
readouts is tested at the 5 percent level, the chance that at least one is "significant"
is 1 - 0.95^16. Real clocks are correlated, so this is an upper-end illustration.

Part C, rounded percentages. Three counts reported with percentages rounded to one decimal
place: 7 (3.7%), 12 (6.3%), 19 (9.9%). Search every denominator from 100 to 400.
"""
from fractions import Fraction
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent / 'evidence/DENOMINATORS_SYNTHETIC_output.json'


def pct(x):
    return f'{float(100 * x):.1f}'


def build():
    groups = {'mild': {'new': (200, 180), 'old': (600, 520)},
              'severe': {'new': (600, 300), 'old': (200, 80)}}
    a = {}
    for g, arms in groups.items():
        a[g] = {arm: dict(treated=n, recovered=r, percent=pct(Fraction(r, n))) for arm, (n, r) in arms.items()}
    overall = {}
    for arm in ('new', 'old'):
        n = sum(groups[g][arm][0] for g in groups)
        r = sum(groups[g][arm][1] for g in groups)
        overall[arm] = dict(treated=n, recovered=r, percent=pct(Fraction(r, n)))
    a['overall'] = overall
    a['new_better_in_each_group'] = all(
        Fraction(*groups[g]['new'][::-1]) > Fraction(*groups[g]['old'][::-1]) for g in groups)
    a['new_better_overall'] = Fraction(overall['new']['recovered'], overall['new']['treated']) > Fraction(
        overall['old']['recovered'], overall['old']['treated'])

    p_any = 1 - Fraction(95, 100) ** 16
    b = dict(readouts=16, level='0.05', chance_at_least_one_false_positive=f'{float(p_any):.2f}')

    obs = [(7, Fraction(37, 10)), (12, Fraction(63, 10)), (19, Fraction(99, 10))]
    half = Fraction(1, 20)
    fits = [n for n in range(100, 401) if all(abs(Fraction(100 * c, n) - p) <= half for c, p in obs)]
    c = dict(observations=[[7, '3.7'], [12, '6.3'], [19, '9.9']], search='100-400', denominators_consistent=fits)
    return dict(nature='SYNTHETIC illustration; no real data; exact fractions',
                script='knowledge_base/pilots/ch04_evidence_en/denominators.py',
                reversal=a, many_readouts=b, rounded_percentages=c)


if __name__ == '__main__':
    data = build()
    OUT.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))

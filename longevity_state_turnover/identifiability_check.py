"""SYNTHETIC analytic counterexamples; no biological fit. Python standard library only."""
from pathlib import Path
import csv, json, math
P = Path(__file__).resolve().parent
cases = [
    ('baseline',10,.08,.02),
    ('less_entry',5,.08,.02),
    ('more_maturation',10,.18,.02),
    ('more_loss',10,.08,.12),
    ('same_stock_slow',1,.008,.002),
    ('same_stock_fast',100,.8,.2),
    ('same_label_different_fate',10,.02,.08),
]
rows=[]
for name,j,m,d in cases:
    k=m+d; n=j/k; t=10.; l0=100.; remaining=l0*math.exp(-k*t)
    rows.append(dict(case=name,entry=j,maturation_hazard=m,loss_hazard=d,
        steady_stock=n,mature_output=m*n,loss_output=d*n,mean_residence=1/k,
        cohort_remaining_t10=remaining,
        cohort_mature_cumulative_t10=l0*m/k*(1-math.exp(-k*t)),
        cohort_loss_cumulative_t10=l0*d/k*(1-math.exp(-k*t))))
checks=[]
def check(name, test):
    assert test, name
    checks.append(name)
by={r['case']:r for r in rows}
check('three mechanisms give stock 50', all(math.isclose(by[x]['steady_stock'],50) for x in ['less_entry','more_maturation','more_loss']))
check('same stock 100 at 100 fold turnover difference', math.isclose(by['same_stock_slow']['steady_stock'],100) and math.isclose(by['same_stock_fast']['steady_stock'],100) and math.isclose(by['same_stock_fast']['entry']/by['same_stock_slow']['entry'],100))
check('opposite maturation output despite same reduced stock', by['more_maturation']['mature_output']>by['baseline']['mature_output']>by['more_loss']['mature_output'])
check('label survival cannot resolve fate partition', math.isclose(by['baseline']['cohort_remaining_t10'],by['same_label_different_fate']['cohort_remaining_t10']) and not math.isclose(by['baseline']['cohort_mature_cumulative_t10'],by['same_label_different_fate']['cohort_mature_cumulative_t10']))
check('stock mass balance',all(math.isclose(r['entry'],r['mature_output']+r['loss_output']) for r in rows))
check('cohort mass balance',all(math.isclose(r['cohort_remaining_t10']+r['cohort_mature_cumulative_t10']+r['cohort_loss_cumulative_t10'],100) for r in rows))
check('positive hazards',all(r['maturation_hazard']>0 and r['loss_hazard']>0 for r in rows))
with (P/'SYNTHETIC_CASES.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(P/'RESULTS.json').write_text(json.dumps({'classification':'SYNTHETIC / NOT FITTED / arbitrary units','checks':checks,'rows':rows},indent=2)+'\n')
print(json.dumps({'passed':len(checks),'classification':'synthetic analytic counterexamples'},indent=2))

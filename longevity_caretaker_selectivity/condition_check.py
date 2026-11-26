"""Exact arithmetic illustration only; NOT fitted biology, a safety model or new theorem.
Standard library only. No downloaded source data are analyzed.
"""
from pathlib import Path
from fractions import Fraction as F
import json,csv
P=Path(__file__).resolve().parent

def case(a,b):
    J,V,K=F(3,5),F(1),F(1)
    J1=(1-a)*J;V1=(1-b)*V
    bounded=J1<V1
    return {'fraction_input_removed':float(a),'fraction_capacity_removed':float(b),
            'input_before':float(J),'capacity_before':float(V),
            'input_after':float(J1),'capacity_after':float(V1),
            'load_ratio_after':float(J1/V1),
            'bounded_saturating_equilibrium':bounded,
            'equilibrium_retained_cargo':float(K*J1/(V1-J1)) if bounded else None,
            'exact_boundary_capacity_loss':float(1-(J/V)*(1-a))}

def main():
    examples=[case(F(1,2),b) for b in [F(1,10),F(1,2),F(7,10),F(4,5)]]
    checks=[]
    def ck(n,v):
        assert v,n
        checks.append({'name':n,'passed':True})
    ck('source-only reduction lowers ratio',case(F(1,2),F(0))['load_ratio_after']<.6)
    ck('capacity-only reduction raises ratio',case(F(0),F(1,2))['load_ratio_after']>.6)
    ck('equal fractions leave ratio unchanged',case(F(1,2),F(1,2))['load_ratio_after']==.6)
    ck('50 percent lower source can coexist with overload',examples[-1]['input_after']==.3 and examples[-1]['load_ratio_after']==1.5)
    ck('equality gives no finite saturating equilibrium',examples[2]['load_ratio_after']==1 and not examples[2]['bounded_saturating_equilibrium'])
    ck('capacity-preserving example finite cargo equals one half',examples[0]['equilibrium_retained_cargo']==.5)
    count=0
    for ai in range(11):
        for bi in range(10):
            a,b=F(ai,10),F(bi,10);rho=F(3,5)*(1-a)/(1-b)
            assert (rho>F(3,5))==(b>a)
            assert (rho<1)==(b<1-F(3,5)*(1-a))
            count+=1
    ck('ratio sign identity on exact grid',count==110)
    ck('capacity boundary identity on exact grid',count==110)
    out={'all_parameters_synthetic_dimensionless':True,'biological_fit':False,
         'equations':['rho_post=rho_pre*(1-a)/(1-b)','rho_post>rho_pre iff b>a for rho_pre>0 and b<1','finite constant-input saturating steady state requires b<1-rho_pre*(1-a)'],
         'examples':examples,'checks':checks,
         'limits':['a is fraction of input flux removed, NOT fraction of marker-positive cells removed.','b is fraction of effective processing capacity lost, NOT fraction of macrophages killed.','No killed-cell transient cargo, compensation, spatial bottleneck, immune toxicity, clinical dosing, or lifespan.','Algebraic capacity condition is NOT a biological safety condition.']}
    (P/'SYNTHETIC_CONDITIONS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    with (P/'SYNTHETIC_EXAMPLES.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(examples[0]));w.writeheader();w.writerows(examples)
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

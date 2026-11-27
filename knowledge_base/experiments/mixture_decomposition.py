#!/usr/bin/env python3
"""Exact accounting under fixed, observed classes; not a causal attribution."""
from fractions import Fraction as F


def decompose(p0, p1, x0, x1):
    arrays = [tuple(F(x) for x in a) for a in (p0,p1,x0,x1)]
    p0,p1,x0,x1=arrays
    if not p0 or len({len(a) for a in arrays}) != 1:
        raise ValueError('vectors must have equal positive length')
    if sum(p0)!=1 or sum(p1)!=1 or any(p<0 for p in p0+p1):
        raise ValueError('weights must be nonnegative and sum to one')
    dp=[b-a for a,b in zip(p0,p1)]; dx=[b-a for a,b in zip(x0,x1)]
    dot=lambda a,b: sum((i*j for i,j in zip(a,b)), F(0))
    within0=dot(p0,dx); mix0=dot(x0,dp); inter=dot(dp,dx)
    within1=dot(p1,dx); mix1=dot(x1,dp)
    symmetric_within=within0+inter/2; symmetric_mix=mix0+inter/2
    delta=dot(p1,x1)-dot(p0,x0)
    assert delta==within0+mix0+inter==within1+mix1-inter==symmetric_within+symmetric_mix
    return {'m0':dot(p0,x0),'m1':dot(p1,x1),'delta':delta,
            'baseline':(within0,mix0,inter), 'end':(within1,mix1,-inter),
            'symmetric':(symmetric_within,symmetric_mix)}


def main():
    r=decompose([F(4,5),F(1,5)],[F(1,5),F(4,5)],[F(1,10),F(9,10)],[F(9,10),F(2,5)])
    print('Synthetic fixed categories, not biological data:', {k:tuple(map(str,v)) if isinstance(v,tuple) else str(v) for k,v in r.items()})
    print('Accounting conventions allocate interaction differently; none identifies a causal mechanism.')

if __name__=='__main__':main()

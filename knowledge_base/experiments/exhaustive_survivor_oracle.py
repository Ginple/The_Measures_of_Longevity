#!/usr/bin/env python3
"""Independent enumeration of joint potential-outcome assignments for small N.

All finite populations are synthetic. Reads survivor_bounds, writes no data by
itself, and checks exact rational extrema under declared finite-grid assumptions.
"""
import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import importlib.util
import json

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('survivor_bounds',P/'survivor_bounds.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def histograms(n):
    # Counts for 0, 1, 2 (remainder died).
    return [{k:v for k,v in enumerate((a,b,c)) if v} for a in range(n+1)
            for b in range(n+1-a) for c in range(n+1-a-b)]


@lru_cache(None)
def allocations(n, counts):
    a=[None]*(n-sum(counts))+[i for i,c in enumerate(counts) for _ in range(c)]
    # Deduplicate permutations; iteration order is immaterial to extrema.
    return tuple(set(permutations(a)))


def brute(n,h0,h1,monotone):
    a=([None]*(n-sum(h0.values())) + [v for v,c in sorted(h0.items()) for _ in range(c)])
    counts=tuple(h1.get(i,0) for i in range(3))
    low=high=None
    for b in allocations(n,counts):
        if monotone and any(x is not None and y is None for x,y in zip(a,b)):continue
        ds=[y-x for x,y in zip(a,b) if x is not None and y is not None]
        if not ds:continue
        v=Fraction(sum(ds),len(ds))
        low=v if low is None or v<low else low
        high=v if high is None or v>high else high
    return None if low is None else (low,high)


def check_n(n):
    hs=histograms(n); checked=0
    for a in hs:
        for b in hs:
            for mono in (False,True):
                if mono and sum(b.values())<sum(a.values()):continue
                actual=m.always_survivor_bounds(n,a,b,mono)['bounds']
                expected=brute(n,a,b,mono)
                if actual!=expected:raise AssertionError((n,a,b,mono,actual,expected))
                checked+=1
    return {'n':n,'histograms':len(hs),'comparisons':checked,'outcome_values':[0,1,2]}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--max-n',type=int,default=6)
    args=parser.parse_args()
    if not 1<=args.max_n<=8: parser.error('max-n must be from 1 to 8')
    results=[]
    for n in range(1,args.max_n+1):
        result=check_n(n);results.append(result)
        print(json.dumps(result),flush=True)
    print(json.dumps({'status':'pass','total_comparisons':sum(r['comparisons'] for r in results),
                      'scope':'synthetic finite integer populations with ternary survivor outcomes; not real data or independent mathematical review'}),flush=True)

if __name__=='__main__':main()

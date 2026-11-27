"""Exhaustive small-population oracle checks, not empirical validation."""
import importlib.util
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import unittest

p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/survivor_bounds.py'
spec=importlib.util.spec_from_file_location('survivor_bounds',p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def hist(a,b):
    return {k:v for k,v in ((0,a),(1,b)) if v}

def brute(n, h0, h1, monotone=False):
    a=[None]*(n-sum(h0.values())) + [v for v,c in h0.items() for _ in range(c)]
    b=[None]*(n-sum(h1.values())) + [v for v,c in h1.items() for _ in range(c)]
    # Fix the first vector: relabeling units cannot change feasible effects.
    effects=[]
    for candidate in set(permutations(b)):
        if monotone and any(x is not None and y is None for x,y in zip(a,candidate)):
            continue
        diffs=[y-x for x,y in zip(a,candidate) if x is not None and y is not None]
        if diffs: effects.append(Fraction(sum(diffs),len(diffs)))
    return (min(effects),max(effects)) if effects else None

class BoundsTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(m.always_survivor_bounds(100,{80:50,20:10},{70:50,100:40})['bounds'],(-10,26))
        self.assertEqual(m.always_survivor_bounds(100,{80:50,20:10},{70:50,100:40},True)['bounds'],(5,20))
    def test_all_binary_histograms_up_to_four(self):
        for n in range(1,5):
            hs=[hist(a,b) for a in range(n+1) for b in range(n+1-a)]
            for h0 in hs:
                for h1 in hs:
                    for monotone in (False,True):
                        if monotone and sum(h1.values())<sum(h0.values()): continue
                        got=m.always_survivor_bounds(n,h0,h1,monotone)['bounds']
                        self.assertEqual(got,brute(n,h0,h1,monotone),(n,h0,h1,monotone))
    def test_zero_possible_or_empty(self):
        r=m.always_survivor_bounds(3,{0:1},{1:1})
        self.assertEqual(r['overlap'],(0,1));self.assertEqual(r['bounds'],(1,1))
        self.assertIsNone(m.always_survivor_bounds(3,{}, {1:1})['bounds'])
    def test_invalid(self):
        for args in [(0,{},{}),(1,{0:2},{}),(1,{0:0},{}),(1,{1.0:1},{}),(2,{0:2},{1:1},True)]:
            with self.assertRaises(ValueError):m.always_survivor_bounds(*args)

if __name__ == '__main__':unittest.main()

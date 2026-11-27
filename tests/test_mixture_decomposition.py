from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import unittest
p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/mixture_decomposition.py'
spec=importlib.util.spec_from_file_location('mixture_decomposition',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class DecompositionTests(unittest.TestCase):
    def test_example(self):
        r=m.decompose([F(4,5),F(1,5)],[F(1,5),F(4,5)],[F(1,10),F(9,10)],[F(9,10),F(2,5)])
        self.assertEqual(r['delta'],F(6,25));self.assertEqual(r['baseline'],(F(27,50),F(12,25),F(-39,50)))
        self.assertEqual(r['end'],(F(-6,25),F(-3,10),F(39,50)))
        self.assertEqual(r['symmetric'],(F(3,20),F(9,100)))
    def test_small_grid(self):
        for a,b in product(range(3),repeat=2):
            for x in product(range(2),repeat=4):
                r=m.decompose([F(a,2),1-F(a,2)],[F(b,2),1-F(b,2)],x[:2],x[2:])
                self.assertEqual(r['delta'],sum(r['symmetric']))
    def test_invalid(self):
        for args in [([],[],[],[]),([1],[1],[1],[]),([2,-1],[1,0],[1,2],[1,2]),([0],[1],[1],[1])]:
            with self.assertRaises(ValueError):m.decompose(*args)

if __name__=='__main__':unittest.main()

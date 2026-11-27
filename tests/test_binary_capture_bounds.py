import importlib.util
from decimal import Decimal, localcontext
from pathlib import Path
import unittest

p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/binary_capture_bounds.py'
s=importlib.util.spec_from_file_location('binary_capture_bounds',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class BinaryCaptureTests(unittest.TestCase):
 def test_independent_and_shared_example(self):
  with localcontext() as ctx:
   ctx.prec=50
   lo,hi=m.change_bounds('.4','.6','.5','2')
   self.assertAlmostEqual(float(lo),-1/7);self.assertEqual(hi,Decimal('.5'))
   lo,hi=m.change_bounds('.4','.6','.5','2',shared=True)
   self.assertAlmostEqual(float(lo),5/28);self.assertAlmostEqual(float(hi),.2)
 def test_constant_shared_and_boundary_outcomes(self):
  self.assertEqual(m.change_bounds('.4','.4','.5','2',shared=True),(0,0))
  self.assertEqual(m.change_bounds(0,1,'.5','2',shared=True),(1,1))
  self.assertEqual(m.change_bounds(1,0,'.5','2',shared=True),(-1,-1))
  self.assertEqual(m.change_bounds('.4','.6',1,1,shared=True),(Decimal('.2'),Decimal('.2')))
 def test_grid_inside_bounds_and_independent_endpoints_attained(self):
  for y0 in ('0','.2','.4','.7','1'):
   for y1 in ('0','.2','.4','.7','1'):
    il,iu=m.change_bounds(y0,y1,'.5','2');sl,su=m.change_bounds(y0,y1,'.5','2',True)
    self.assertAlmostEqual(float(il),float(m.prevalence(y1,2)-m.prevalence(y0,'.5')))
    self.assertAlmostEqual(float(iu),float(m.prevalence(y1,'.5')-m.prevalence(y0,2)))
    for step in range(151):
     r=Decimal('.5')+Decimal(step)/100
     d=m.prevalence(y1,r)-m.prevalence(y0,r)
     self.assertLessEqual(float(sl)-1e-25,float(d));self.assertLessEqual(float(d),float(su)+1e-25)
 def test_invalid_inputs(self):
  for args in [(-1,.4,.5,2),(.4,1.1,.5,2),(.4,.6,0,2),(.4,.6,2,1),(.4,.6,float('nan'),2),(True,.6,.5,2),(.4,.6,.5,2,1)]:
   with self.subTest(args=args),self.assertRaises(ValueError):m.change_bounds(*args)

if __name__=='__main__': unittest.main()

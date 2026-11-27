from pathlib import Path
import importlib.util
import unittest
from fractions import Fraction

p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/time_origin_counterexample.py'
s=importlib.util.spec_from_file_location('time_origin_example',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class TimeOriginTests(unittest.TestCase):
 def test_equal_fixed_outcomes_different_windows(self):
  r=m.example()
  self.assertEqual((r['fixed_control'],r['fixed_treatment']),(Fraction(3,4),Fraction(3,4)))
  self.assertEqual((r['observed_control'],r['observed_delayed']),(Fraction(3,4),Fraction(1,4)))
 def test_interval_boundaries_and_event_count(self):
  self.assertEqual(m.first_observed_risk(((0,2,4),(4,),()),2,2),Fraction(1,3))
  self.assertEqual(m.first_observed_risk(((0,1,2),()),0,4),Fraction(1,2))
 def test_rejects_invalid(self):
  for args in (([],0,4),([()],-1,4),([()],0,0),([(-1,)],0,4),([(True,)],0,4)):
   with self.subTest(args=args),self.assertRaises(ValueError):m.first_observed_risk(*args)

if __name__=='__main__':unittest.main()

import importlib.util
from pathlib import Path
import unittest

p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/clock_unit_counterexample.py'
s=importlib.util.spec_from_file_location('clock_unit_example',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class ClockUnitTests(unittest.TestCase):
 def test_two_distinct_standard_errors(self):
  result=m.example()
  self.assertEqual((result['people'],result['clocks']),(2,36))
  self.assertAlmostEqual(result['group_mean_across_clocks'],1)
  self.assertAlmostEqual(result['se_across_persons_for_mean'],1)
  self.assertAlmostEqual(result['se_across_clock_means'],(24/35)**.5/6)
  self.assertLess(result['se_across_clock_means'],result['se_across_persons_for_mean'])

if __name__=='__main__':unittest.main()

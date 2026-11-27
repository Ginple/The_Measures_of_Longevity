from pathlib import Path
import importlib.util
import unittest
P=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('exhaustive_oracle',P/'knowledge_base/experiments/exhaustive_survivor_oracle.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class OracleTests(unittest.TestCase):
 def test_ternary_small(self):
  for n in range(1,4):
   result=m.check_n(n)
   self.assertEqual(result['histograms'],(n+1)*(n+2)*(n+3)//6)
   self.assertGreater(result['comparisons'],0)
 def test_absent_survivor_undefined(self):
  self.assertIsNone(m.brute(3,{}, {1:2},False))

if __name__=='__main__':unittest.main()

import sys,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P/'tools'))
from numeric_contracts import check_percentage,execution_contract

class ProjectTests(unittest.TestCase):
 def test_rounded_third_is_legitimate(self):
  self.assertEqual(check_percentage('33.3',3,'crude_unweighted_binary')['status'],'compatible_with_printed_rounding')
 def test_wrong_crude_count(self):
  self.assertEqual(check_percentage('10.0',3,'crude_unweighted_binary')['status'],'incompatible_with_crude_count')
 def test_weighted_estimate_not_rejected_as_crude(self):
  r=check_percentage('10.0',3,'weighted');self.assertFalse(r['applied_integer_rule']);self.assertTrue(r['not_a_pass'])
 def test_survival_not_integer_frequency(self):
  self.assertEqual(check_percentage('72.5',11,'survival')['status'],'requires_estimand_specific_check')
 def test_adjusted_not_integer_frequency(self):
  self.assertFalse(check_percentage('12.5',11,'model_adjusted')['applied_integer_rule'])
 def test_zero_and_hundred(self):
  self.assertEqual(check_percentage('0',1,'crude_unweighted_binary')['example_compatible_numerators'],[0]);self.assertEqual(check_percentage('100',1,'crude_unweighted_binary')['example_compatible_numerators'],[1])
 def test_half_up_boundary(self):
  self.assertEqual(check_percentage('13',8,'crude_unweighted_binary')['example_compatible_numerators'],[1])
 def test_invalid_denominator(self):
  for n in [0,-1,True,3.5]:
   with self.assertRaises(ValueError):check_percentage('10',n,'crude_unweighted_binary')
 def test_empty_contract_fails(self):
  self.assertEqual(execution_contract([])['status'],'fail')
 def test_skipped_contract_fails(self):
  self.assertEqual(execution_contract([{'blocking':True,'status':'skipped'}])['status'],'fail')
 def test_advisory_not_counted(self):
  self.assertEqual(execution_contract([{'blocking':False,'status':'ran_pass'}])['executed_blocking_checks'],0)
 def test_explicit_run_count(self):
  r=execution_contract([{'blocking':True,'status':'ran_pass'}]);self.assertTrue(r['status'].startswith('pass_encoded'))
 def test_failed_check_fails(self):
  self.assertEqual(execution_contract([{'blocking':True,'status':'ran_fail'}])['status'],'fail')
 def test_partial_skip_not_green(self):
  self.assertEqual(execution_contract([{'blocking':True,'status':'ran_pass'},{'blocking':True,'status':'skipped'}])['status'],'fail')
 def test_invalid_minimum(self):
  with self.assertRaises(ValueError):execution_contract([],0)
 def test_no_html(self):
  self.assertFalse(any(f.suffix.lower()=='.html' for f in P.rglob('*') if f.is_file()))

if __name__=='__main__':unittest.main()

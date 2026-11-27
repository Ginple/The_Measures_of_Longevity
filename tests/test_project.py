import sys,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P/'tools'))
from numeric_contracts import check_percentage,execution_contract
from dashboard_contract import check_dashboard, DASHBOARDS
from markdown_links import classify_links
import json, shutil, tempfile

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
 def test_no_html_contract(self):
  self.assertEqual(check_dashboard(P), [])
  self.assertEqual(DASHBOARDS, ())
 def test_contract_rejects_html_and_case_collisions(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)
   self.assertEqual(check_dashboard(root), [])
   (root/'STATE_DASHBOARD.HTML').write_text('<!doctype html>')
   self.assertIn('unauthorized HTML: STATE_DASHBOARD.HTML',check_dashboard(root))
   (root/'STATE_DASHBOARD.HTML').unlink()
   (root/'docs').mkdir(); (root/'docs/Note.md').write_text('a'); (root/'docs/note.md').write_text('b')
   if len(list((root/'docs').iterdir()))==2:  # skip on case-insensitive hosts
    self.assertIn('case-insensitive path collision: docs/Note.md | docs/note.md',check_dashboard(root))
   shutil.rmtree(root/'docs')
   self.assertEqual(check_dashboard(root), [])
 def test_new_broken_links_are_not_hidden_by_legacy_exceptions(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/'governance').mkdir()
   (root/'governance/legacy_broken_links.json').write_text(json.dumps({'known_broken_links':[{'file':'history.md','link':'old.md'}]}))
   (root/'history.md').write_text('[old](old.md)\n[new](new.md)\n')
   result=classify_links(root)
   self.assertEqual(result['known_legacy'],[{'file':'history.md','link':'old.md'}])
   self.assertEqual(result['new'],[{'file':'history.md','link':'new.md'}])
 def test_state_turnover_model_terminology_and_examples(self):
  kernel=(P/'knowledge_base/KERNEL.md').read_text()
  row=next(line for line in kernel.splitlines() if line.startswith('| I6 |'))
  self.assertIn('m 是成熟退出风险率',row)
  self.assertIn('d 是其他丢失风险率',row)
  self.assertIn('模型不含迁移',row)
  self.assertNotIn('迁移+死亡',row)
  model=(P/'longevity_state_turnover/状态还在_不等于细胞没换.md').read_text()
  self.assertIn('成熟退出风险率为m，其他丢失风险率为d',model)
  self.assertIn('最小模型暂不含增殖、逆转、迁移',model)
  data=json.loads((P/'longevity_state_turnover/RESULTS.json').read_text())
  cases={r['case']:r for r in data['rows']}
  for r in cases.values():
   self.assertAlmostEqual(r['steady_stock'],r['entry']/(r['maturation_hazard']+r['loss_hazard']))
   self.assertAlmostEqual(r['mature_output'],r['maturation_hazard']*r['steady_stock'])
  self.assertAlmostEqual(cases['baseline']['maturation_hazard'],.08)
  self.assertAlmostEqual(cases['baseline']['mature_output'],8)
  self.assertAlmostEqual(cases['more_maturation']['mature_output'],9)
  self.assertAlmostEqual(cases['more_loss']['mature_output'],4)
  self.assertAlmostEqual(cases['baseline']['cohort_remaining_t10'],cases['same_label_different_fate']['cohort_remaining_t10'])
  self.assertNotAlmostEqual(cases['baseline']['cohort_mature_cumulative_t10'],cases['same_label_different_fate']['cohort_mature_cumulative_t10'])

if __name__=='__main__':unittest.main()

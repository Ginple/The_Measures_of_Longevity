import sys,unittest
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from pathlib import Path
P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P/'tools'))
from numeric_contracts import check_percentage,execution_contract
sys.path.insert(0,str(P/'scripts'))
from run_validation import project_files

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
 def test_only_authorized_dashboard_html(self):
  html={str(f.relative_to(P)) for f in project_files(P,{'.html','.htm'})}
  self.assertLessEqual(html, {'STATE_DASHBOARD.HTML'})

 def test_dashboard_relative_links(self):
  class Links(HTMLParser):
   def __init__(self): super().__init__(); self.links=[]; self.ids=[]
   def handle_starttag(self,tag,attrs):
    attrs=dict(attrs)
    if 'id' in attrs:self.ids.append(attrs['id'])
    if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])
  if not (P/'STATE_DASHBOARD.HTML').exists():return  # historical snapshot is optional
  parser=Links();parser.feed((P/'STATE_DASHBOARD.HTML').read_text(encoding='utf-8'))
  self.assertEqual(len(parser.ids),len(set(parser.ids)))
  for link in parser.links:
   url=urlsplit(link)
   if url.scheme or url.netloc:continue
   if url.path:self.assertTrue((P/unquote(url.path)).exists(),link)
   elif url.fragment:self.assertIn(url.fragment,parser.ids)

 def test_dashboard_sections_and_offline_rendering(self):
  class Structure(HTMLParser):
   def __init__(self): super().__init__(); self.ids=[]; self.assets=[]
   def handle_starttag(self,tag,attrs):
    attrs=dict(attrs)
    if 'id' in attrs:self.ids.append(attrs['id'])
    if tag in ('script','link','iframe','img','video','audio') and ('src' in attrs or 'href' in attrs):self.assets.append(tag)
  if not (P/'STATE_DASHBOARD.HTML').exists():return  # do not require creation
  doc=(P/'STATE_DASHBOARD.HTML').read_text(encoding='utf-8'); parser=Structure();parser.feed(doc)
  for section in ('overview','thesis','evidence','models','book','papers','frontier','experiment','audit','issues','handoff','sources','ledger','excerpts'):
   self.assertIn(section,parser.ids)
  self.assertFalse(parser.assets)
  self.assertNotIn('@import',doc.lower())
  self.assertIn('非寿命试验',doc)
  self.assertIn('D05',doc)
  # Historical content only: never require the frozen snapshot to follow the live ledger.
  self.assertIn('item-X01',parser.ids)
  self.assertIn('更年轻的样本，还是更年轻的细胞？',doc)
  self.assertIn('扶手不是细胞，但它改变了人的可能性',doc)
  self.assertIn('recovery-update',parser.ids)
  self.assertIn('两种处理下均会存活者的人数',doc)
  self.assertIn('修好这一次，还剩多少下一次？',doc)
  self.assertIn('research-update',parser.ids)
  self.assertIn('死亡后的功能、可识别界限与假设价格',doc)
  self.assertIn('141/152',doc)
  self.assertIn('chapter-one',parser.ids)
  self.assertIn('两本账，不是一张最终成绩单',doc)
  self.assertIn('measurement-update',parser.ids)
  self.assertIn('chapter-eleven',parser.ids)
  self.assertIn('一个平均数的分母',doc)
  self.assertIn('85,732',doc)

if __name__=='__main__':unittest.main()

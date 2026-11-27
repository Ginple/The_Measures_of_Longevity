"""Tests the fixture mechanics, not general detector efficacy."""
from pathlib import Path
import copy, hashlib, importlib.util, json, shutil, tempfile, unittest
P=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('fixture_comparison',P/'knowledge_base/experiments/assurance_fixture_comparison.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

def hashes():
 return {str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in (P/'examples/toy').rglob('*') if f.is_file()}

class ComparisonTests(unittest.TestCase):
 def test_fixture_reproducible_and_readonly(self):
  before=hashes();a=m.run();b=m.run();self.assertEqual(a,b);self.assertEqual(before,hashes())
  for mode, rows in a['cases'].items():
   self.assertEqual(len(rows),7);self.assertEqual(a['scores'][mode]['overall']['total'],7)
 def test_scenarios_expose_contract_differences(self):
  r=m.run()['cases']; lookup=lambda mode,case:next(x['decision'] for x in r[mode] if x['id']==case)
  self.assertEqual(lookup('A','claim_context_changed'),'valid')
  self.assertEqual(lookup('C','claim_context_changed'),'valid')
  self.assertEqual(lookup('D','claim_context_changed'),'stale')
  self.assertEqual(lookup('E','required_dimension_unknown'),'stale')
  self.assertEqual(lookup('C','irrelevant_append'),'valid')
  self.assertEqual(lookup('E','irrelevant_append'),'stale')
 def test_empty_or_unknown_is_not_silent_success(self):
  with self.assertRaises(ValueError):m.apply_case(P,{},'nonexistent')
 def test_changed_fixture_fails_closed(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'toy';shutil.copytree(P/'examples/toy',root)
   project=copy.deepcopy(json.loads((root/'project.json').read_text()))
   source=m.confined(root,m._artifact(project,'A-source')['path'])
   source.write_text('baseline no longer matches\n')
   for case in ('source_number_changed','source_rewritten_and_rebound'):
    with self.assertRaisesRegex(ValueError,'expected baseline text'):
     m.apply_case(root,project,case)

if __name__=='__main__':unittest.main()

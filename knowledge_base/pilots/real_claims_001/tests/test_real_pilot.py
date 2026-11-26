from pathlib import Path
import copy,json,shutil,sys,tempfile,unittest,hashlib
P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P/'scripts'))
from pilot_core import inspect,load,quantitative_checks,check_source_trace,sha256
from research_assurance.core import inspect_project,claim_record_hash

class RealRecordTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'pilot';shutil.copytree(P,self.root,ignore=shutil.ignore_patterns('__pycache__'));self.data=load(self.root)
 def tearDown(self):self.tmp.cleanup()
 def save(self): (self.root/'project.json').write_text(json.dumps(self.data,ensure_ascii=False,indent=2)+'\n')
 def test_baseline_literal_records_not_truth(self):
  r=inspect(self.root);self.assertEqual(r['engine']['issues'],[]);self.assertEqual(r['registered_paragraph_claims'],2);self.assertEqual(r['human_reviewed_claim_count'],0);self.assertEqual(r['scientific_truth'],'not_computed');self.assertEqual(r['formal_academic_release'],'blocked')
 def test_review_missing_for_both(self):
  r=inspect(self.root);self.assertEqual(r['engine']['independent_review_missing_for'],['LON-C000001','LON-C000002'])
 def test_portable_does_not_claim_whole_source_validation(self):
  self.assertEqual(inspect(self.root)['source_trace']['whole_source_status'],'not_checked_cache_not_supplied')
 def test_source_excerpt_drift_propagates_only_declared_consumers(self):
  with (self.root/'evidence/MTDNA_excerpts.txt').open('a') as f:f.write('New correction outside selected quotes.\n')
  r=inspect(self.root);self.assertIn('LON-C000002',r['stale_graph_nodes']);self.assertNotIn('LON-C000001',r['stale_graph_nodes']);self.assertEqual(r['affected_draft_ids'],['DRAFT-BOOK-VISIBILITY','PAPER-P1-INTERFACE','PAPER-P2-INTERFACE','PAPER-P3-INTERFACE'])
 def test_book_offspan_drift_not_ignored(self):
  with (self.root/'corpus/v6.md').open('a') as f:f.write('A new statement outside selected paragraph.\n')
  r=inspect(self.root);self.assertIn('LON-C000001',r['stale_graph_nodes']);self.assertEqual(r['affected_draft_ids'],['DRAFT-BOOK-FUNCTION','PAPER-P3-INTERFACE'])
 def test_context_change_invalidates_record(self):
  self.data['claims'][0]['context']['population']='all humans';self.save();r=inspect(self.root);self.assertIn('assessment_record_binding_mismatch',[x['reason'] for x in r['engine']['issues']])
 def test_same_source_different_quote_invalidates_record(self):
  self.data['evidence'][0]['text']='An invented quote.\n';self.save();r=inspect(self.root);self.assertIn('exact_span_mismatch',[x['reason'] for x in r['engine']['issues']])
 def test_causal_upgrade_not_licensed(self):
  c=self.data['claims'][1];c['kind']='causal';c['assessment']['record_sha256']=claim_record_hash(c,{e['id']:e for e in self.data['evidence']});self.save();r=inspect(self.root);self.assertTrue(any(x['reason']=='required_dimension_not_supported' and x['dimension']=='causal_identification' for x in r['engine']['issues']))
 def test_mapping_content_drift(self):
  with (self.root/'drafts/V6_FUNCTION_MODULE.md').open('a') as f:f.write('An unreviewed addition.\n')
  r=inspect(self.root);self.assertIn('DRAFT-BOOK-FUNCTION',r['affected_draft_ids']);self.assertNotIn('DRAFT-BOOK-VISIBILITY',r['affected_draft_ids'])
 def test_mapping_unknown_claim(self):
  f=self.root/'provenance/PUBLICATION_MAP.json';m=json.loads(f.read_text());m['targets'][0]['claim_ids']=['NO-SUCH-CLAIM'];f.write_text(json.dumps(m));self.assertIn('unknown_claim_reference',[x['reason'] for x in inspect(self.root)['mapping_issues']])
 def test_no_fabricated_external_review(self):self.assertEqual(self.data['reviews'],[])
 def test_claim_span_positions(self):
  self.assertEqual([c['lines_1based_halfopen'] for c in self.data['claims']],[[384,385],[79,80]])
 def test_no_html_export(self):self.assertFalse(any(f.suffix.lower()=='.html' for f in P.rglob('*') if f.is_file()))

class ArithmeticTests(unittest.TestCase):
 def test_raw_proportions_not_hazard_ratio(self):
  r=quantitative_checks()['LIFE'];self.assertTrue(r['crude_risk_ratio_is_not_cox_hazard_ratio']);self.assertAlmostEqual(float(r['control_minus_activity_crude_percentage_points']),5.422,places=3)
 def test_no_fixed_horizon_nnt(self):self.assertIsNone(quantitative_checks()['LIFE']['computed_nnt'])
 def test_three_worlds_same_endpoint(self):
  r=quantitative_checks()['constructed_not_empirical'];self.assertTrue(r['same_observed_endpoint']);self.assertEqual({x['B'] for x in r['worlds']},{'3/2000'})
 def test_world_parameters_really_differ(self):
  r=quantitative_checks()['constructed_not_empirical'];self.assertEqual(len({(x['f'],x['h'],x['r']) for x in r['worlds']}),3)

class SourceTraceFixtureTests(unittest.TestCase):
 """Small synthetic HTML fixtures, not copied full third-party articles."""
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();r=Path(self.tmp.name);self.root=r/'root';self.cache=r/'cache'
  for p in [self.root/'provenance',self.root/'evidence',self.cache]:p.mkdir(parents=True,exist_ok=True)
  raw=b'<article><p>Fixture quote.</p><p>Outside selection.</p></article>';text='Fixture quote.\nOutside selection.';quote='Fixture quote.'
  (self.cache/'X.html').write_bytes(raw);(self.cache/'X.txt').write_text(text);(self.root/'evidence/X.txt').write_text(quote+'\n')
  receipt={'sources':[{'id':'X','raw_html_sha256':sha256(raw),'normalized_text_sha256':sha256(text.encode())}],'selected_quotes':[{'evidence_id':'E-X','source_id':'X','snapshot_character_span_0based_halfopen':[0,len(quote)],'quote_sha256_utf8_without_appended_newline':sha256(quote.encode()),'bundle_path':'evidence/X.txt','bundle_lines_1based_halfopen':[1,2]}]}
  (self.root/'provenance/SOURCE_RECEIPTS.json').write_text(json.dumps(receipt))
 def tearDown(self):self.tmp.cleanup()
 def test_whole_snapshot_and_trace_success(self):self.assertEqual(check_source_trace(self.root,self.cache)['issues'],[])
 def test_outside_quote_original_changes(self):
  (self.cache/'X.html').write_bytes(b'<article><p>Fixture quote.</p><p>Correction outside selection.</p></article>');(self.cache/'X.txt').write_text('Fixture quote.\nCorrection outside selection.')
  r=check_source_trace(self.root,self.cache);self.assertEqual(r['changed_source_artifact_ids'],['A-X']);self.assertIn('whole_source_snapshot_hash_drift',[x['reason'] for x in r['issues']])
 def test_tampered_excerpt_trace(self):
  (self.root/'evidence/X.txt').write_text('Made up.\n');self.assertIn('excerpt_trace_mismatch',[x['reason'] for x in check_source_trace(self.root,self.cache)['issues']])
 def test_missing_cache_not_green(self):
  (self.cache/'X.html').unlink();self.assertEqual(check_source_trace(self.root,self.cache)['whole_source_status'],'drift_or_unavailable')

if __name__=='__main__':unittest.main()

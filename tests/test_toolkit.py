import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from research_assurance.core import inspect_project, validate, document_diff, impact, freeze, confined, read_span, sha256, claim_record_hash, reviewed_claim_hash
from research_assurance.consistency import finite_global_compatibility
from research_assurance.corpus import extract_units, apophatic_scan
from research_assurance.topology import analyze, sensitivity, adjusted_rand
from research_assurance.measurement import nominal_relabelling_audit, nominal_distances, founder_bounds, weighted_fraction
from research_assurance.tasks import generate_research_questions, generate_knowledge_graph

P = Path(__file__).resolve().parents[1]


class RecordsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)/'toy'
        shutil.copytree(P/'examples/toy', self.root)
        self.project = json.loads((self.root/'project.json').read_text())
    def tearDown(self):
        self.temp.cleanup()
    def check(self):
        return inspect_project(self.project, self.root)
    def reasons(self):
        return [x['reason'] for x in self.check()['issues']]
    def test_01_valid_is_not_truth(self):
        r = self.check()
        self.assertEqual(r['issues'], [])
        self.assertEqual(r['scientific_truth'], 'not_computed')
        self.assertEqual(r['formal_release_record_check'], 'blocked')
    def test_02_source_change_invalidates_claim(self):
        with (self.root/'evidence/synthetic_source.txt').open('a') as f: f.write('New correction.\n')
        self.assertIn('C1', self.check()['stale_nodes'])
        self.assertIn('artifact_hash_drift', self.reasons())
    def test_03_unreviewed_source_refresh_not_green(self):
        path = self.root/'evidence/synthetic_source.txt'
        path.write_text(path.read_text()+'new correction\n')
        self.project['artifacts'][0]['sha256'] = sha256(path.read_bytes())
        self.assertIn('assessment_hash_binding_mismatch', self.reasons())
    def test_04_outside_span_change_visible(self):
        path = self.root/'corpus/draft.md'
        path.write_text(path.read_text()+'Universal efficacy established.\n')
        self.assertIn('A-book', self.check()['artifact_drift'])
    def test_05_quote_edit_fails(self):
        self.project['evidence'][0]['text'] = 'Invented quotation\n'
        self.assertIn('exact_span_mismatch', self.reasons())
    def test_06_wrong_span_fails(self):
        self.project['claims'][0]['lines_1based_halfopen'] = [1,2]
        self.assertIn('exact_span_mismatch', self.reasons())
    def test_07_unknown_evidence_fails(self):
        self.project['claims'][0]['evidence_ids'] = ['ghost']
        self.assertIn('unknown_evidence', self.reasons())
    def test_08_duplicate_ids_fail(self):
        self.project['claims'].append(copy.deepcopy(self.project['claims'][0]))
        self.assertFalse(self.check()['schema_valid'])
    def test_09_absolute_path_rejected(self):
        self.project['artifacts'][0]['path'] = '/etc/passwd'
        self.assertIn('artifact_unavailable_or_unsafe', self.reasons())
    def test_10_traversal_rejected(self):
        with self.assertRaises(ValueError): confined(self.root, '../other')
    def test_11_symlink_escape_rejected(self):
        (self.root/'escape').symlink_to(self.root.parent)
        with self.assertRaises(ValueError): confined(self.root, 'escape/other')
    def test_12_no_evidence_no_resolved_state(self):
        self.project['claims'][0]['evidence_ids'] = []
        self.assertIn('resolved_state_without_evidence', self.reasons())
    def test_13_causal_upgrade_not_source_match(self):
        self.project['claims'][0]['kind'] = 'causal'
        self.assertIn('required_dimension_not_supported', self.reasons())
    def test_14_metadata_not_full_evidence(self):
        self.project['artifacts'][0]['access_depth'] = 'metadata'
        self.assertIn('metadata_not_evidence_for_full_claim', self.reasons())
    def test_15_no_fake_self_independence(self):
        self.project['reviews'] = [{'id':'R1','reviewer':'toy-author','independence_declared':True,'receipt':'fixture','claim_ids':['C1'],'bound_hashes':self.project['claims'][0]['assessment']['bound_hashes'],'response_complete':True,'claim_record_hashes':{'C1':reviewed_claim_hash(self.project['claims'][0],{e['id']:e for e in self.project['evidence']})}}]
        self.assertEqual(self.check()['independent_review_missing_for'], ['C1'])
    def test_16_review_needs_receipt_and_binding(self):
        self.project['reviews'] = [{'id':'R1','reviewer':'fixture-other','independence_declared':True,'receipt':'','claim_ids':['C1'],'bound_hashes':{},'response_complete':True,'claim_record_hashes':{'C1':reviewed_claim_hash(self.project['claims'][0],{e['id']:e for e in self.project['evidence']})}}]
        self.assertEqual(self.check()['independent_review_missing_for'], ['C1'])
    def test_17_full_prerequisites_not_certification(self):
        self.project['coverage']['human_inventory_complete'] = True
        self.project['debts'] = []
        self.project['reviews'] = [{'id':'R-fixture','reviewer':'fixture-other','independence_declared':True,'receipt':'fixture-not-real-review','claim_ids':['C1'],'bound_hashes':self.project['claims'][0]['assessment']['bound_hashes'],'response_complete':True,'claim_record_hashes':{'C1':reviewed_claim_hash(self.project['claims'][0],{e['id']:e for e in self.project['evidence']})}}]
        r = self.check()
        self.assertEqual(r['formal_release_record_check'], 'recorded_prerequisites_present_not_certification')
        self.assertEqual(r['scientific_truth'], 'not_computed')
    def test_18_source_family_not_independent_count(self):
        self.assertEqual(self.check()['source_families'], ['toy-family-1'])
    def test_19_coverage_count_contract(self):
        self.project['coverage']['registered_claims'] = 100
        self.assertIn('registered_claim_count_mismatch', self.reasons())
    def test_20_schema_no_silent_typo(self):
        self.project['claims'][0]['criticality'] = 'high'
        self.assertFalse(self.check()['schema_valid'])
    def test_21_freeze_cannot_overwrite(self):
        freeze(self.root, ['corpus/draft.md'], 'snapshot.json', 'new explicit byte snapshot')
        with self.assertRaises(FileExistsError): freeze(self.root, ['corpus/draft.md'], 'snapshot.json', 'overwrite forbidden')
    def test_22_missing_artifact(self):
        (self.root/'evidence/synthetic_source.txt').unlink()
        self.assertIn('artifact_unavailable_or_unsafe', self.reasons())
    def test_23_invalid_root_schema(self):
        self.assertTrue(validate([]))
    def test_24_cross_group_id_collision(self):
        self.project['claims'][0]['id'] = 'A-source'
        self.assertTrue(validate(self.project))
    def test_53_exact_quote_still_not_entailment(self):
        # A genuine but unrelated source line can satisfy byte/locator checks.
        # This deliberate blindspot MUST NOT produce scientific certification.
        lines = (self.root/'evidence/synthetic_source.txt').read_text().splitlines(keepends=True)
        self.project['evidence'][0].update(lines_1based_halfopen=[4,5],text=lines[3])
        self.assertIn('assessment_record_binding_mismatch', self.reasons())
        # Explicitly refreshing a human assertion can still be semantically wrong.
        # Record hashes cannot make an unfaithful assessor honest.
        self.project['claims'][0]['assessment']['record_sha256'] = claim_record_hash(self.project['claims'][0],{e['id']:e for e in self.project['evidence']})
        r = self.check()
        self.assertEqual(r['issues'], [])
        self.assertEqual(r['scientific_truth'], 'not_computed')
    def test_54_old_review_does_not_follow_new_source_hash(self):
        self.project['reviews'] = [{'id':'R-old','reviewer':'fixture-other','independence_declared':True,'receipt':'fixture-only','claim_ids':['C1'],'bound_hashes':dict(self.project['claims'][0]['assessment']['bound_hashes']),'response_complete':True,'claim_record_hashes':{'C1':reviewed_claim_hash(self.project['claims'][0],{e['id']:e for e in self.project['evidence']})}}]
        path = self.root/'evidence/synthetic_source.txt'
        path.write_text(path.read_text()+'New material.\n')
        h = sha256(path.read_bytes())
        self.project['artifacts'][0]['sha256'] = h
        # Even manually refreshing the claim does not refresh the external review.
        self.project['claims'][0]['assessment']['bound_hashes']['A-source'] = h
        self.assertEqual(self.check()['independent_review_missing_for'], ['C1'])


    def test_55_context_change_invalidates_judgement(self):
        self.project['claims'][0]['context']['population'] = 'all humans'
        self.assertIn('assessment_record_binding_mismatch', self.reasons())
        self.assertIn('C1', self.check()['stale_nodes'])

    def test_56_supported_report_requires_source_and_extraction(self):
        for dimension in ('source_support', 'extraction'):
            for state in ('refuted', 'mixed', 'unknown', 'not_applicable'):
                self.project['claims'][0]['assessment']['dimensions'][dimension] = state
                self.assertIn('required_dimension_not_supported', self.reasons())
                self.assertIn('C1', self.check()['stale_nodes'])
            self.project['claims'][0]['assessment']['dimensions'][dimension] = 'supported'


class ReasoningTests(unittest.TestCase):
    def test_25_unchanged_not_certified(self):
        self.assertEqual(document_diff('x\n','x\n')['state'], 'unchanged_not_truth_certified')
    def test_26_newline_change_detected(self):
        self.assertTrue(document_diff('x\n','x\r\n')['hunks'])
    def test_27_transitive_impact_with_cycles(self):
        self.assertEqual(impact([('a','e'),('e','c'),('c','e'),('c','s')],['a']), ['a','c','e','s'])
    def test_28_sat_not_external_truth(self):
        r = finite_global_compatibility([{'id':'a','vars':['x'],'allowed':[[1]]}])
        self.assertEqual(r['status'], 'sat'); self.assertEqual(r['external_truth'], 'unknown')
    def test_29_pairwise_not_global(self):
        # x=y, y=z, x!=z: each pair feasible, all three infeasible.
        s = [{'id':'a','vars':['x','y'],'allowed':[[0,0],[1,1]]},{'id':'b','vars':['y','z'],'allowed':[[0,0],[1,1]]},{'id':'c','vars':['x','z'],'allowed':[[0,1],[1,0]]}]
        import itertools
        self.assertTrue(all(finite_global_compatibility(list(p))['status']=='sat' for p in itertools.combinations(s,2)))
        self.assertEqual(finite_global_compatibility(s)['status'], 'unsat')
    def test_30_empty_unknown(self):
        self.assertEqual(finite_global_compatibility([])['status'], 'unknown')
    def test_31_budget_unknown(self):
        s = [{'id':'a','vars':['x'],'allowed':[[0],[1]]},{'id':'b','vars':['x'],'allowed':[[2],[3]]}]
        self.assertEqual(finite_global_compatibility(s,1)['status'], 'unknown')
    def test_32_json_boolean_not_integer(self):
        s = [{'id':'a','vars':['x'],'allowed':[[True]]},{'id':'b','vars':['x'],'allowed':[[1]]}]
        self.assertEqual(finite_global_compatibility(s)['status'], 'unsat')
    def test_33_relabelling_counterexample(self):
        r = nominal_relabelling_audit([[7]*3,[10]*3,[11]*3])
        self.assertFalse(r['numeric_invariant_all']); self.assertTrue(r['onehot_invariant_all']); self.assertEqual(len(r['runs']),6)
    def test_34_missingness_not_a_nominal_state(self):
        with self.assertRaises(ValueError): nominal_distances([[1,None],[2,2]])
    def test_35_founder_bounds(self):
        states = ['target_observed']*3+['non_target_observed']*2+['death_confirmed']+['lost_unknown']*4
        self.assertEqual(founder_bounds([{'founder_id':str(i),'state':s} for i,s in enumerate(states)])['target_fraction_bounds'],[.3,.7])
    def test_36_no_descendant_pseudoreplication(self):
        with self.assertRaises(ValueError): founder_bounds([{'founder_id':'a','state':'target_observed'}]*2)
    def test_37_weighting_changes_aggregate(self):
        self.assertAlmostEqual(weighted_fraction([.1,.9],[9,1]),.18)
        self.assertEqual(weighted_fraction([.1,.9],[1,1]),.5)
    def test_38_invalid_weight_rejected(self):
        with self.assertRaises(ValueError): weighted_fraction([.1,.9],[1,0])
    def test_39_span_halfopen(self):
        self.assertEqual(read_span(b'a\nb\nc\n',2,3), 'b\n')
    def test_40_span_bounds(self):
        with self.assertRaises(ValueError): read_span(b'a',1,3)


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.onto = [{'id':'a','aliases':['A']},{'id':'b','aliases':['B']},{'id':'c','aliases':['C']},{'id':'z','aliases':['ZZZ']}]
        self.units = extract_units('A B\n\nB C\n\nA\n',self.onto)
    def test_41_exact_unit_locators(self):
        self.assertEqual(self.units[1]['lines_1based_halfopen'], [3,4])
    def test_42_no_english_substring_leak(self):
        self.assertEqual(extract_units('ABBA',self.onto)[0]['concept_ids'], [])
    def test_43_missing_is_not_discovered(self):
        r=analyze(self.units,self.onto)
        self.assertEqual(r['zero_detected_vocabulary_entries'],['z'])
        self.assertNotIn('z',[n['id'] for n in r['nodes']])
    def test_44_threshold_causes_isolates(self):
        r=analyze(self.units,self.onto,min_support=2)
        self.assertEqual(r['isolates'],['a','b','c'])
    def test_45_actual_edges(self):
        r=analyze(self.units,self.onto)
        self.assertEqual(len(r['edges']),2)
        self.assertTrue(all(e['unit_ids'] for e in r['edges']))
    def test_46_cluster_pair_counts(self):
        r=analyze(self.units,self.onto,min_support=2)
        self.assertEqual(sum(x['possible_edges'] for x in r['cluster_pairs']),3)
        self.assertEqual(sum(x['actual_edges'] for x in r['cluster_pairs']),0)
    def test_47_states_not_psychology(self):
        r=sensitivity(self.units,self.onto)
        self.assertEqual(len(r['runs']),18)
        self.assertIn('not construct validity',r['warning'])
    def test_48_ari_invariant_to_label_names(self):
        self.assertEqual(adjusted_rand([['a','b'],['c']],[['c'],['b','a']]),1.)
        self.assertIsNone(adjusted_rand([['a']],[['b']]))
    def test_49_apophatic_is_not_semantic_absence(self):
        self.assertIn('not proof',apophatic_scan(self.units,self.onto)['warning'].lower())
    def test_50_not_causal_kg(self):
        self.assertFalse(generate_knowledge_graph(self.units,self.onto)['causal_knowledge_graph'])
    def test_51_contract_not_invented(self):
        with self.assertRaises(ValueError): generate_research_questions([{'id':'x','question':'why'}])
    def test_52_empty_graph_no_fabricated_focus(self):
        self.assertEqual(analyze([],self.onto)['local_heuristic_state'],'not_applicable_empty_graph')


if __name__ == '__main__':
    unittest.main()

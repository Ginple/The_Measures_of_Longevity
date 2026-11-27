from pathlib import Path
import importlib.util
import unittest
p=Path(__file__).resolve().parents[1]/'knowledge_base/experiments/assurance_benchmark_metrics.py'
spec=importlib.util.spec_from_file_location('assurance_metrics',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class MetricsTests(unittest.TestCase):
 def test_counts_and_abstentions(self):
  pairs=[('stale','stale'),('valid','stale'),('stale','valid'),('valid','valid'),('stale','abstain'),('valid','abstain')]
  rows=[{'id':str(i),'family': 'a' if i<3 else 'b','oracle':o,'decision':d} for i,(o,d) in enumerate(pairs)]
  r=m.score(rows)
  self.assertEqual([r['overall'][k] for k in ('TP','FP','FN','TN','abstain_stale','abstain_valid')],[1]*6)
  self.assertEqual(r['overall']['precision_among_flags'],.5)
  self.assertEqual(r['overall']['recall_among_decided_stale'],.5)
  self.assertAlmostEqual(r['overall']['recall_all_stale_treating_abstain_as_not_detected'],1/3)
  self.assertEqual(r['overall']['abstention_rate'],1/3)
  self.assertEqual(sum(f['total'] for f in r['by_family'].values()),6)
 def test_zero_denominator_none(self):
  r=m.score([])['overall']
  self.assertIsNone(r['precision_among_flags']);self.assertIsNone(r['abstention_rate'])
 def test_invalid(self):
  good={'id':'x','family':'a','oracle':'valid','decision':'valid'}
  for rows in ([good,good],[dict(good,oracle='unknown')],[dict(good,decision='unknown')],[dict(good,extra=1)],[dict(good,id='')]):
   with self.assertRaises(ValueError):m.score(rows)

if __name__=='__main__':unittest.main()

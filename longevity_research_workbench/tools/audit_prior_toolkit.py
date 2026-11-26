"""Adversarial fixture against frozen 0.1.0; no changes to original toolkit or real reviews."""
from pathlib import Path
import copy,importlib.util,json,shutil,tempfile,sys
P=Path(__file__).resolve().parents[1]

def main():
 old=Path(sys.argv[1]) if len(sys.argv)>1 else P.parent/'research_assurance_toolkit'
 spec=importlib.util.spec_from_file_location('old_core',old/'src/research_assurance/core.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 data=json.loads((old/'examples/toy/project.json').read_text())
 data['coverage']['human_inventory_complete']=True;data['debts']=[]
 c=data['claims'][0]
 c['assessment']['dimensions']['source_support']='refuted'
 data['reviews']=[{'id':'R-adversarial-fixture','reviewer':'fixture-only-not-a-real-reviewer','independence_declared':True,'receipt':'synthetic-test-record-not-actual-review','claim_ids':['C1'],'bound_hashes':dict(c['assessment']['bound_hashes']),'claim_record_hashes':{'C1':m.reviewed_claim_hash(c,{e['id']:e for e in data['evidence']})},'response_complete':True}]
 with tempfile.TemporaryDirectory() as td:
  root=Path(td)/'fixture';shutil.copytree(old/'examples/toy',root)
  result=m.inspect_project(data,root)
 out={'upstream_version':'0.1.0','constructed_fixture':True,'test':'supported reported claim but required source_support dimension is refuted',
      'actual_issues':result['issues'],'actual_release_record_status':result['formal_release_record_check'],
      'gap_reproduced':not result['issues'] and result['formal_release_record_check']=='recorded_prerequisites_present_not_certification',
      'scientific_truth':result['scientific_truth'],
      'meaning':'Internal contract inconsistency was not screened; no real external review asserted or fabricated.'}
 (P/'artifacts/PRIOR_TOOLKIT_ADVERSARIAL.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert out['gap_reproduced']
if __name__=='__main__':main()

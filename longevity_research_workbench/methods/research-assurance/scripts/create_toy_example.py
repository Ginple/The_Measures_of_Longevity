from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1]/'examples/toy'
source='CONSTRUCTED SOURCE / 构造来源，不是真实论文\nIn a synthetic classroom cohort, 3 of 10 baseline founders reached the toy target.\nFour founders had unknown terminal status; lost tracking was not labelled death.\nNo treatment effect or functional recovery was estimated.\n'
book='# Synthetic research note / 构造研究短文\n\nThe constructed source reports 3 target observations among 10 baseline founders.\n\nTracking uncertainty limits interpretation of target observations.\n\nFunction and net benefit require additional evidence.\n'
(P/'evidence/synthetic_source.txt').write_text(source)
(P/'corpus/draft.md').write_text(book)
h=lambda t:hashlib.sha256(t.encode()).hexdigest()
dims={k:'unknown' for k in ['source_support','extraction','measurement','statistical_inference','causal_identification','transportability','net_benefit','independent_review']};dims['source_support']='supported';dims['extraction']='supported'
p={'schema_version':'0.1','project_id':'toy-constructed-not-empirical','authors':['toy-author'],
'coverage':{'scope':'One curated reported claim; no exhaustive semantic claim extraction.','human_inventory_complete':False,'candidate_units':4,'registered_claims':1,'note':'Candidate units are not facts; toy actors are fixtures, not real reviewers.'},
'artifacts':[{'id':'A-source','path':'evidence/synthetic_source.txt','sha256':h(source),'role':'source','family':'toy-family-1','access_depth':'fulltext','url':'','version':'constructed-v1'},{'id':'A-book','path':'corpus/draft.md','sha256':h(book),'role':'manuscript','family':'toy-manuscript','access_depth':'fulltext','url':'','version':'constructed-v1'}],
'evidence':[{'id':'E1','artifact_id':'A-source','lines_1based_halfopen':[2,3],'text':source.splitlines(keepends=True)[1]}],
'claims':[{'id':'C1','artifact_id':'A-book','lines_1based_halfopen':[3,4],'text':book.splitlines(keepends=True)[2],'kind':'reported','role':'asserted','critical':True,'context':{'population':'synthetic classroom founders','time':'toy terminal observation','estimand':'reported target fraction, not causal effect','unit':'baseline founder','design':'constructed descriptive example','domain':'toy only'},'evidence_ids':['E1'],'assessment':{'state':'supported','reviewer':'fixture-curator-not-real-independent-review','rationale':'Literal comparison in a constructed example only.','bound_hashes':{'A-source':h(source),'A-book':h(book)},'dimensions':dims}}],
'reviews':[], 'debts':[{'id':'D-toy-review','status':'blocked','blocks_formal_release':True,'question':'Independent review absent','next_action':'Do not invent reviewer receipts','closure_evidence':'Real review of real research, not this fixture'}]}
from research_assurance.core import claim_record_hash
p['claims'][0]['assessment']['record_sha256']=claim_record_hash(p['claims'][0],{e['id']:e for e in p['evidence']})
(P/'project.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
onto=[{'id':i,'label_zh':z,'label_en':e,'aliases':a,'type':'analytic_concept'} for i,z,e,a in [('founder','基线原始单元','baseline founder',['founder','founders','原始单元']),('target','目标终点','target endpoint',['target','目标']),('tracking','追踪','tracking',['Tracking','追踪']),('uncertainty','不确定性','uncertainty',['uncertainty','不确定性']),('function','功能','function',['Function','功能']),('benefit','净益','net benefit',['net benefit','净益']),('ethics','伦理','ethics',['ethics','伦理'])]]
(P/'ontology.json').write_text(json.dumps(onto,ensure_ascii=False,indent=2)+'\n')
print('toy fixture created; never execute this to refresh a real project baseline')

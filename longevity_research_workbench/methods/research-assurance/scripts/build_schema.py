"""Maintainer-only schema authoring; NOT a data/trust baseline refresh command."""
from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
S={'type':'string','minLength':1}; BOOL={'type':'boolean'}; HASH={'type':'string','pattern':'^[a-f0-9]{64}$'}
def enum(*v):return {'enum':list(v)}
def arr(x):return {'type':'array','items':x}
def obj(p,required=None):return {'type':'object','properties':p,'required':list(p) if required is None else required,'additionalProperties':False}
def ref(n):return {'$ref':'#/$defs/'+n}
span={'type':'array','prefixItems':[{'type':'integer','minimum':1},{'type':'integer','minimum':2}],'minItems':2,'maxItems':2}
state=enum('supported','refuted','mixed','unknown','not_applicable')
hashes={'type':'object','additionalProperties':HASH}
defs={
'artifact':obj(dict(id=S,path=S,sha256=HASH,role=enum('source','manuscript','dataset','code'),family=S,access_depth=enum('metadata','abstract','excerpt','fulltext','data','code'),url={'type':'string'},version=S)),
'evidence':obj(dict(id=S,artifact_id=S,lines_1based_halfopen=span,text=S)),
'assessment':obj(dict(state=enum('supported','refuted','mixed','unknown'),reviewer={'type':'string'},rationale={'type':'string'},bound_hashes=hashes,record_sha256={'type':'string','pattern':'^([a-f0-9]{64})?$'},dimensions=obj({k:state for k in ['source_support','extraction','measurement','statistical_inference','causal_identification','transportability','net_benefit','independent_review']}))),
'claim':obj(dict(id=S,artifact_id=S,lines_1based_halfopen=span,text=S,kind=enum('formal','reported','descriptive','statistical','causal','transport','decision','normative','proposal'),role=enum('asserted','hypothesis','rejected_misreading','proposal'),critical=BOOL,context=obj({k:S for k in ['population','time','estimand','unit','design','domain']}),evidence_ids=arr(S),assessment=ref('assessment'))),
'review':obj(dict(id=S,reviewer=S,independence_declared=BOOL,receipt={'type':'string'},claim_ids=arr(S),bound_hashes=hashes,claim_record_hashes=hashes,response_complete=BOOL)),
'debt':obj(dict(id=S,status=enum('open','partial','blocked','closed'),blocks_formal_release=BOOL,question=S,next_action=S,closure_evidence=S))}
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'https://example.invalid/research-assurance/project-0.1.schema.json','title':'Local research assurance records, not scientific certification',**obj(dict(schema_version={'const':'0.1'},project_id=S,authors=arr(S),coverage=obj(dict(scope=S,human_inventory_complete=BOOL,candidate_units={'type':'integer','minimum':0},registered_claims={'type':'integer','minimum':0},note=S)),**{k:arr(ref(v)) for k,v in [('artifacts','artifact'),('evidence','evidence'),('claims','claim'),('reviews','review'),('debts','debt')]})),'$defs':defs}
for path in [P/'schemas/project.schema.json',P/'src/research_assurance/project.schema.json']:path.write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
print('two identical local schema copies written')

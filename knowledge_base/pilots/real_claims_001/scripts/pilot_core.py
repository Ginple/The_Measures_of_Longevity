"""Read-only pilot diagnostics. No refresh of evidence, judgments or receipt hashes."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import hashlib,json,re,sys
P=Path(__file__).resolve().parents[1]
W=P.parents[2]
sys.path.insert(0,str(W/'methods/research-assurance/src'))
from research_assurance.core import inspect_project,impact,confined,sha256

def load(root=P):return json.loads((Path(root)/'project.json').read_text())

def quantitative_checks(root=P):
 project=load(root)
 if inspect_project(project,root).get('issues'):raise ValueError('Do not recompute from stale or invalid records.')
 evidence={e['id']:e for e in project['evidence']}
 quote=evidence['E-LIFE-RESULT']['text'];pairs=re.findall(r'n=(\d+)/(\d+)',quote)
 if len(pairs)!=2:raise ValueError('Unexpected source formatting; review, do not guess numbers.')
 (pa_n,pa_d),(he_n,he_d)=[tuple(map(int,pair)) for pair in pairs]
 hr=re.search(r'HR=([0-9.]+)',quote).group(1)
 alt=evidence['E-LIFE-ALTERNATIVE']['text'];alt_counts=[int(x) for x in re.findall(r'\b(\d+) \(',alt)]
 if len(alt_counts)!=2:raise ValueError('Unexpected alternative-adjudication quote formatting.')
 with localcontext() as ctx:
  ctx.prec=35
  pa=Decimal(pa_n)/pa_d;he=Decimal(he_n)/he_d
  crude_rr=pa/he;rd=he-pa
 result={'LIFE':{'numeric_input_evidence_ids':['E-LIFE-RESULT','E-LIFE-ALTERNATIVE'],'numeric_input_quote_sha256':{eid:sha256(evidence[eid]['text'].encode()) for eid in ['E-LIFE-RESULT','E-LIFE-ALTERNATIVE']},'physical_activity':{'events':pa_n,'randomized':pa_d,'crude_percent':str(pa*100)},'health_education':{'events':he_n,'randomized':he_d,'crude_percent':str(he*100)},'control_minus_activity_crude_percentage_points':str(rd*100),'crude_risk_ratio':str(crude_rr),'published_cox_hazard_ratio':hr,'crude_risk_ratio_is_not_cox_hazard_ratio':crude_rr!=Decimal(hr),'alternative_adjudications':{'physical_activity':alt_counts[0],'health_education':alt_counts[1],'total':sum(alt_counts),'total_primary_events':pa_n+he_n,'fraction':str(sum(alt_counts))+'/'+str(pa_n+he_n)},'computed_nnt':None,'nnt_not_computed_reason':'No fixed-horizon survival risk estimated here; crude event proportions under variable follow-up are not a universally valid 2.6-year NNT.'}}
 f=Fraction(1,200);h=Fraction(3,5)
 def bulk(f,h,r):return f*r*h/(f*r+1-f)
 b0=bulk(f,h,Fraction(1));end=b0/2
 r=end*(1-f)/(f*(h-end))
 worlds=[('within_carrier_change',f,h/2,Fraction(1)),('carrier_fraction_change',f/2,h,Fraction(1)),('relative_copy_capture_change',f,h,r)]
 result['constructed_not_empirical']={'equation':'B=f*r*h/(f*r+1-f)','f':'true fraction of carrier cells','h':'mutant fraction within carrier cells','r':'relative effective molecular contribution per carrier cell vs noncarrier (copy number times capture in this simplified model)','baseline':{'f':str(f),'h':str(h),'r':'1','B':str(b0)},'worlds':[{'name':n,'f':str(ff),'h':str(hh),'r':str(rr),'B':str(bulk(ff,hh,rr))} for n,ff,hh,rr in worlds],'same_observed_endpoint':all(bulk(ff,hh,rr)==end for _,ff,hh,rr in worlds),'interpretation':'Non-unique inverse mapping in this explicitly simplified linear molecular-mixture model. Not an estimate for the Nature cohort, not a nonlinear clock model, not evidence of real rejuvenation.'}
 return result

def check_source_trace(root=P,cache=None):
 root=Path(root);receipt=json.loads((root/'provenance/SOURCE_RECEIPTS.json').read_text())
 issues=[];changed_sources=[]
 if cache is None:return {'mode':'portable_excerpt_only','whole_source_status':'not_checked_cache_not_supplied','issues':[],'changed_source_artifact_ids':[],'scientific_truth':'not_computed'}
 from bs4 import BeautifulSoup
 cache=Path(cache)
 for source in receipt['sources']:
  sid=source['id'];rawpath=cache/(sid+'.html');txtpath=cache/(sid+'.txt')
  try:
   raw=rawpath.read_bytes();txt=txtpath.read_bytes()
  except OSError:
   issues.append({'source_id':sid,'reason':'cached_source_unavailable'});changed_sources.append('A-'+sid);continue
  if sha256(raw)!=source['raw_html_sha256'] or sha256(txt)!=source['normalized_text_sha256']:
   issues.append({'source_id':sid,'reason':'whole_source_snapshot_hash_drift'});changed_sources.append('A-'+sid)
  soup=BeautifulSoup(raw,'html.parser');main=soup.find('article') or soup.find('main') or soup
  for node in main.select('script,style,nav'):node.decompose()
  expected=main.get_text('\n',strip=True).encode()
  if txt!=expected:issues.append({'source_id':sid,'reason':'normalization_not_reproducible'});changed_sources.append('A-'+sid)
  try:text=txt.decode('utf8')
  except UnicodeError:
   issues.append({'source_id':sid,'reason':'source_not_utf8'});changed_sources.append('A-'+sid);continue
  for sel in receipt['selected_quotes']:
   if sel['source_id']!=sid:continue
   start,end=sel['snapshot_character_span_0based_halfopen'];quote=text[start:end]
   bundle=confined(root,sel['bundle_path']).read_bytes().decode()
   a,b=sel['bundle_lines_1based_halfopen'];chosen=''.join(bundle.splitlines(keepends=True)[a-1:b-1])
   if sha256(quote.encode())!=sel['quote_sha256_utf8_without_appended_newline'] or quote+'\n'!=chosen:
    issues.append({'source_id':sid,'evidence_id':sel['evidence_id'],'reason':'excerpt_trace_mismatch'});changed_sources.append('A-'+sid)
 return {'mode':'local_whole_source_and_excerpt_trace','whole_source_status':'verified_cached_snapshot_and_normalization' if not issues else 'drift_or_unavailable','issues':issues,'changed_source_artifact_ids':sorted(set(changed_sources)),'scientific_truth':'not_computed'}

def check_mappings(root=P):
 root=Path(root);mapping=json.loads((root/'provenance/PUBLICATION_MAP.json').read_text());ids={c['id'] for c in load(root)['claims']};issues=[];edges=[]
 for item in mapping['targets']:
  try:
   file=confined(root,item['path']);raw=file.read_bytes()
   if sha256(raw)!=item['sha256']:issues.append({'id':item['id'],'reason':'mapped_draft_hash_drift'})
  except (ValueError,OSError):issues.append({'id':item['id'],'reason':'mapped_draft_unavailable_or_unsafe'});continue
  for cid in item['claim_ids']:
   if cid not in ids:issues.append({'id':item['id'],'reason':'unknown_claim_reference'})
   if cid not in raw.decode():issues.append({'id':item['id'],'reason':'claim_reference_not_in_target'})
   edges.append((cid,item['id']))
 return {'issues':issues,'edges':edges,'scope':'Declared reference graph only; no automatic semantic dependency extraction or sufficient-evidence certification'}

def inspect(root=P,cache=None):
 root=Path(root);project=load(root);engine=inspect_project(project,root);trace=check_source_trace(root,cache);maps=check_mappings(root)
 edges=[(e['artifact_id'],e['id']) for e in project['evidence']]+[(eid,c['id']) for c in project['claims'] for eid in c['evidence_ids']]+maps['edges']
 seeds=engine.get('stale_nodes',[])+trace['changed_source_artifact_ids']+[x['id'] for x in maps['issues']]
 stale=impact(edges,seeds)
 return {'registered_paragraph_claims':len(project['claims']),'evidence_excerpts':len(project['evidence']),'independent_study_families_not_replications':len({a['family'] for a in project['artifacts'] if a['role']=='source'}),'engine':engine,'source_trace':trace,'mapping_issues':maps['issues'],'stale_graph_nodes':stale,'affected_draft_ids':sorted(x['id'] for x in json.loads((root/'provenance/PUBLICATION_MAP.json').read_text())['targets'] if x['id'] in stale),'formal_academic_release':'blocked','external_review':'not_performed','human_reviewed_claim_count':0,'scientific_truth':'not_computed'}

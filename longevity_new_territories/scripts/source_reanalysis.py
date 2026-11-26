"""New papers, descriptive source-table recalculation. No causal or longevity p-values."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import openpyxl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parents[1]
def js(n,o):(P/'results'/n).write_text(json.dumps(o,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def numeric(v):return isinstance(v,(int,float)) and not isinstance(v,bool)
def main():
 w=openpyxl.load_workbook(P/'data/N01_supporting_values.xlsx',data_only=True,read_only=True);raw=[];summary=[]
 spec=[('Figure 2F',3,4,'Plasma ALT','3 months WD'),('Figure 2H',3,4,'Liver triglycerides','6 months WD'),('Figure 4D',3,4,'Plasma triglycerides','6 months WD'),('Figure 5K',3,4,'TG secretion rate','2 weeks WD; P407 assay'),('Figure 5L',3,4,'Plasma ApoB','2 weeks WD; 3h after P407')]
 def save_groups(study,panel,groups,endpoint,context):
  means={}
  for g,entries in groups.items():
   vals=np.array([v for cell,v in entries]);assert len(vals)>1 and np.isfinite(vals).all();means[g]=vals.mean()
   for cell,v in entries:raw.append({'study':study,'panel':panel,'group':g,'cell':cell,'value':float(v),'endpoint':endpoint,'context':context,'pairing':'not_assumed'})
   summary.append({'study':study,'panel':panel,'endpoint':endpoint,'context':context,'group':g,'n':len(vals),'mean':float(vals.mean()),'median':float(np.median(vals)),'sd':float(vals.std(ddof=1))})
  return means
 ratios=[]
 for sh,c1,c2,ep,ctx in spec:
  s=w[sh];groups={g:[(s.cell(r,c).coordinate,float(s.cell(r,c).value)) for r in range(1,s.max_row+1) if numeric(s.cell(r,c).value)] for g,c in [('WT',c1),('KO',c2)]}
  means=save_groups('TBX3',sh,groups,ep,ctx);ratios.append({'study':'TBX3','panel':sh,'endpoint':ep,'KO_over_WT_mean':means['KO']/means['WT'],'relative_change':means['KO']/means['WT']-1,'context':ctx})
 # Preselected Figure4A glucose tolerance, 10 observed trajectories per group.
 s=w['Figure 4A'];tt=np.array([s.cell(r,3).value for r in range(4,9)],float);assert np.array_equal(tt,[0,30,60,90,120]);auc={};trace=[]
 for g,cs in [('WT',range(4,14)),('KO',range(15,25))]:
  a=np.array([[s.cell(r,c).value for c in cs] for r in range(4,9)],float);assert a.shape==(5,10) and np.isfinite(a).all()
  av=np.trapezoid(a,x=tt,axis=0);auc[g]=av
  for i,c in enumerate(cs):
   for r,t in enumerate(tt):trace.append({'group':g,'column':c,'time_min':t,'value':a[r,i],'cell':s.cell(4+r,c).coordinate})
 pd.DataFrame(trace).to_csv(P/'results/TBX3_GTT_TRAJECTORIES.csv',index=False)
 pd.DataFrame({'WT_AUC':auc['WT'],'KO_AUC':auc['KO'],'row_order_is_not_pairing':True}).to_csv(P/'results/TBX3_GTT_AUC.csv',index=False)
 ratios.append({'study':'TBX3','panel':'Figure 4A','endpoint':'Glucose tolerance AUC 0-120min','KO_over_WT_mean':float(auc['KO'].mean()/auc['WT'].mean()),'relative_change':float(auc['KO'].mean()/auc['WT'].mean()-1),'context':'6 months WD; 10 columns/group; native glucose units x minutes'})
 # Independent relation check: 0/90/180min equally spaced => OLS slope/hour equals endpoint change/3h.
 s=w['Figure 5J'];ratechecks=[]
 for g,cs,col in [('WT',range(4,11),3),('KO',range(13,21),4)]:
  derived=np.array([(s.cell(9,c).value-s.cell(7,c).value)/3 for c in cs]);reported=np.array([w['Figure 5K'].cell(r,col).value for r in range(5,5+len(derived))],float)
  # Row-order comparison is conditional; observed discrepancies are retained, not repaired.
  ratechecks.append({'group':g,'n':len(derived),'max_abs_difference_from_reported_rate':float(np.max(np.abs(derived-reported))),'rounding_only_tolerance_used_in_failed_check':.06,'all_within_rounding_only_tolerance':bool(np.max(np.abs(derived-reported))<.06),'derived_endpoint_rate_mean':float(derived.mean()),'reported_rate_mean':float(reported.mean()),'interpretation':'Approximate agreement, not strict rounding-only identity; no source values altered'})
 # Primary niche depletion comparison uses ABT panels; do not use GCV CD45.1/2 label discrepancy for primary numbers.
 q=openpyxl.load_workbook(P/'data/N02_Fig5.xlsx',data_only=True,read_only=True)
 for sh,ep in [('Fig 5l','Senescent MSC frequency'),('Fig 5m','Donor BM contribution'),('Fig 5n','Donor HSC contribution')]:
  s=q[sh];groups={};names=['Control vehicle','Control ABT263','Mutant vehicle','Mutant ABT263']
  for g,c in zip(names,range(2,6)):groups[g]=[(s.cell(r,c).coordinate,float(s.cell(r,c).value)) for r in range(3,s.max_row+1) if numeric(s.cell(r,c).value)]
  assert [len(groups[g]) for g in names]==[10,9,8,10]
  means=save_groups('DNMT3A_stroma',sh,groups,ep,'Recipient mice; no cross-panel pairing assumed')
  dc=means[names[1]]-means[names[0]];dm=means[names[3]]-means[names[2]]
  ratios.append({'study':'DNMT3A_stroma','panel':sh,'endpoint':ep,'control_change_pp':dc,'mutant_change_pp':dm,'difference_in_changes_pp':dm-dc,'mutant_treated_over_vehicle':means[names[3]]/means[names[2]],'context':'Descriptive interaction contrast, not a randomized interaction test or stromal-only drug specificity proof'})
 # Healthy liver labeled-cell attrition: each timepoint is a separate destructive cohort.
 q=openpyxl.load_workbook(P/'data/N03_source.xlsx',data_only=True,read_only=True);s=q['Figure 1C'];cr=[]
 for j,time in enumerate(['10 days','1 month','2 months','3 months','6.5 months']):
  groups={}
  for g,c in [('Reporter',2+2*j),('BetaCatenin',3+2*j)]:
   groups[g]=[(s.cell(r,c).coordinate,float(s.cell(r,c).value)) for r in range(2,7) if numeric(s.cell(r,c).value)]
  means=save_groups('CTNNB1','Figure 1C',groups,'Labeled hepatocytes per area',time+' young healthy; cross-sectional');cr.append({'time':time,'mutant_over_reporter_mean':means['BetaCatenin']/means['Reporter']})
 pd.DataFrame(raw).to_csv(P/'results/SOURCE_VALUES_LONG.csv',index=False)
 pd.DataFrame(summary).to_csv(P/'results/SOURCE_GROUP_SUMMARIES.csv',index=False)
 pd.DataFrame(cr).to_csv(P/'results/CTNNB1_HEALTHY_COUNTS.csv',index=False)
 js('SOURCE_CONTRASTS.json',{'contrasts':ratios,'TG_rate_relation_check':ratechecks,'GTT_mean_AUC':{g:float(v.mean()) for g,v in auc.items()},'units_policy':'Original workbook native units retained; TBX3 absolute axis-unit scale not independently verified, ratios unitless. No pooled damage score.','cautions':['TBX3 whole-liver KO not sparse-clone dose response','No same-mouse linkage across panels','Figure4A embedded summary N=45 not used as animal n; actual table 10 trajectories/group','Figure5K caption self-reference not used as sample mapping evidence','N02 GCV figure5f/g caption CD45.1 vs source CD45.2 discrepancy; primary recalculation restricted to ABT panels','N03 Figure7D has formatted dimension 1048573 rows; not iterated or analyzed','No independent statistical review or disease-risk/lifespan inference']})
 fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained');d=[r for r in ratios if r['study']=='TBX3'];ax.barh([r['endpoint'] + (' (3h after P407)' if r['panel']=='Figure 5L' else ' (P407 assay)' if r['panel']=='Figure 5K' else '') for r in d],[100*r['relative_change'] for r in d],color=['#2a9d8f' if r['relative_change']<0 else '#d97706' for r in d]);ax.axvline(0,color='black',lw=.7);ax.set(xlabel='KO vs WT mean change (%) | separate cohorts / assays',title='TBX3: liver-local improvement does not imply systemic improvement');fig.savefig(P/'figures/01_TBX3_separate_endpoints.png',dpi=170);plt.close(fig)
 print(json.dumps({'contrasts':ratios,'healthy_counts':cr},indent=2))
if __name__=='__main__':main()

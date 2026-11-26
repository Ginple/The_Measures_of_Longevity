"""Small source summaries + a SYNTHETIC single-cargo max-flow countermodel.
No causal estimates, disease predictions, fitted biological capacities, or new p-values.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
import pandas as pd
from scipy.optimize import linprog
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
P=Path(__file__).resolve().parent

def network(j=(.8,.2),mu=(.4,.8),bridge=0.,remove_local=False):
    edges={('s','S1'):j[0],('s','S2'):j[1],('S2','M1'):2.,
           ('S2','M2'):2.,('M1','t'):mu[0],('M2','t'):mu[1]}
    if not remove_local:edges[('S1','M1')]=2.
    if bridge>0:edges[('S1','M2')]=bridge
    return edges

def solve(edges):
    arcs=list(edges); internal=['S1','S2','M1','M2']
    A=np.array([[float(v==n)-float(u==n) for u,v in arcs] for n in internal])
    c=np.array([-float(u=='s') for u,v in arcs])
    sol=linprog(c,A_eq=A,b_eq=np.zeros(len(internal)),bounds=[(0,edges[e]) for e in arcs],method='highs')
    assert sol.success
    cuts=[]
    for flags in product([False,True],repeat=len(internal)):
        left={'s'}|{n for n,b in zip(internal,flags) if b}
        crossing=[e for e in arcs if e[0] in left and e[1] not in left]
        cuts.append((sum(edges[e] for e in crossing),sorted(left),crossing))
    best=min(cuts,key=lambda q:q[0]);F=float(-sol.fun)
    assert abs(F-best[0])<1e-8
    return {'max_feasible_flow':F,'min_cut_capacity':float(best[0]),'one_min_cut_source_side':best[1],
            'cut_arcs':[list(e) for e in best[2]],
            'total_input':sum(v for (a,b),v in edges.items() if a=='s'),
            'total_processing_capacity':sum(v for (a,b),v in edges.items() if b=='t'),
            'arcs':[{'from':a,'to':b,'capacity':float(edges[(a,b)]),'one_optimal_flow':float(x)} for (a,b),x in zip(arcs,sol.x)]}

def main():
    summaries=[];long=[]
    maps=[('Figure6F','elife-75354-fig6-data4-v1.csv',{'WT':'WT','B1 -/-':'Itgb1 KO','X2 B1 -/-':'Itgb1 KO 2x cells','X2 WT':'WT 2x cells'},'24h normalized total-bead MFI, % baseline; not bead-count fraction','biological replicate summary; n=3 via Figure5 cross-reference'),
          ('Figure6supp2','elife-75354-fig6-figsupp2-data1-v1.csv',{'WT':'WT','Tln1 -/-':'Tln1 KO','B2 -/-':'Itgb2 KO','B1 -/-':'Itgb1 KO'},'BMDMs with internalized beads, % total','technical replicate; one representative experiment, N=3')]
    for panel,f,mapping,endpoint,level in maps:
        d=pd.read_csv(P/'data'/f).dropna(how='all')
        assert d.shape==(3,4) and set(d.columns)==set(mapping)
        for col in d:
            vals=d[col].to_numpy(float);assert np.isfinite(vals).all()
            summaries.append({'panel':panel,'group':mapping[col],'n_entries':len(vals),'mean':float(vals.mean()),'sd_entries':float(vals.std(ddof=1)),'endpoint':endpoint,'replication_level':level})
            for row,v in enumerate(vals,2):long.append({'panel':panel,'source_column':col,'source_row':row,'group':mapping[col],'value':v,'replication_level':level})
    pd.DataFrame(summaries).to_csv(P/'SOURCE_SUMMARIES.csv',index=False)
    pd.DataFrame(long).to_csv(P/'SOURCE_VALUES_LONG.csv',index=False)
    sm={(r['panel'],r['group']):r['mean'] for r in summaries}
    contrasts={'Fig6F_KO_minus_WT_normalized_MFI_pp':sm['Figure6F','Itgb1 KO']-sm['Figure6F','WT'],
               'Fig6F_KO2x_minus_KO_normalized_MFI_pp':sm['Figure6F','Itgb1 KO 2x cells']-sm['Figure6F','Itgb1 KO'],
               'Fig6F_KO2x_minus_WT_normalized_MFI_pp':sm['Figure6F','Itgb1 KO 2x cells']-sm['Figure6F','WT'],
               'suspension_KO_minus_WT_percentage_points_descriptive_only':sm['Figure6supp2','Itgb1 KO']-sm['Figure6supp2','WT'],
               'caution':'No cross-panel pairing, new p-values, equivalence claims, or terminal degradation inference.'}
    cases={'baseline':network(),'remote_capacity_doubled':network(mu=(.4,1.6)),
           'local_capacity_doubled':network(mu=(.8,.8)),
           'access_bridge_added':network(bridge=.4),'input_location_swapped':network(j=(.2,.8)),
           'fully_connected':network(bridge=2.),'S1_isolated':network(remove_local=True)}
    outputs={n:solve(e) for n,e in cases.items()};checks=[]
    def ck(n,v):
        assert bool(v),n
        checks.append({'name':n,'passed':True})
    ck('pooled capacity exceeds load yet flow shortfall',outputs['baseline']['total_processing_capacity']>1 and abs(outputs['baseline']['max_feasible_flow']-.6)<1e-8)
    ck('remote capacity increase does not help',abs(outputs['remote_capacity_doubled']['max_feasible_flow']-.6)<1e-8)
    for n in ['local_capacity_doubled','access_bridge_added','input_location_swapped','fully_connected']:
        ck(n+' restores ideal feasibility',abs(outputs[n]['max_feasible_flow']-1)<1e-8)
    ck('isolated S1 cannot be served remotely',abs(outputs['S1_isolated']['max_feasible_flow']-.2)<1e-8)
    for n,r in outputs.items():
        ck(n+' LP equals independently enumerated cut',abs(r['max_feasible_flow']-r['min_cut_capacity'])<1e-8)
        ck(n+' bounds and conservation',all(-1e-9<=e['one_optimal_flow']<=e['capacity']+1e-9 for e in r['arcs']) and all(abs(sum(e['one_optimal_flow'] for e in r['arcs'] if e['to']==v)-sum(e['one_optimal_flow'] for e in r['arcs'] if e['from']==v))<1e-8 for v in ['S1','S2','M1','M2']))
    grid=[]
    for b in np.linspace(0,.8,41):
        r=solve(network(bridge=float(b)));grid.append({'bridge_capacity':float(b),'max_feasible_flow':r['max_feasible_flow']})
    ck('bridge response matches analytic piecewise formula',all(abs(r['max_feasible_flow']-(.6+min(r['bridge_capacity'],.4)))<1e-8 for r in grid))
    ck('bridge response monotone',np.all(np.diff([r['max_feasible_flow'] for r in grid])>=-1e-8))
    pd.DataFrame(grid).to_csv(P/'SYNTHETIC_BRIDGE_SWEEP.csv',index=False)
    pd.DataFrame([{'scenario':n,**e} for n,r in outputs.items() for e in r['arcs']]).to_csv(P/'SYNTHETIC_NETWORK_ARCS.csv',index=False)
    record={'all_network_parameters_synthetic_dimensionless':True,'not_fitted_to_source':True,'source_descriptive_contrasts':contrasts,'networks':outputs,'checks':checks,
            'caveats':['Max flow is an optimistic static feasible throughput, not measured clearance or queue stability.','Finite edge capacities are assumed, not derived from contact counts.','One divisible cargo; no signaling, toxicity, delay, routing failure, or adaptive recruitment.','At equality with biological maximum, finite saturating steady state is not guaranteed.']}
    (P/'RESULTS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    # Draw the constructed physical access topology, not a literature/semantic graph.
    fig,axes=plt.subplots(1,2,figsize=(11.5,4.3),layout='constrained')
    ax=axes[0];pos={'S1':(0,1),'S2':(0,0),'M1':(1.3,1),'M2':(1.3,0)}
    for a,b in [('S1','M1'),('S2','M1'),('S2','M2')]:
        ax.add_patch(FancyArrowPatch(pos[a],pos[b],arrowstyle='-|>',mutation_scale=15,shrinkA=32,shrinkB=32,lw=1.8,color='#475569'))
    ax.add_patch(FancyArrowPatch(pos['S1'],pos['M2'],arrowstyle='-|>',mutation_scale=15,shrinkA=32,shrinkB=32,lw=2,color='#059669',linestyle='--',connectionstyle='arc3,rad=-.18'))
    for n,(x,y) in pos.items():
        ax.scatter(x,y,s=1900,c='#dbeafe' if n.startswith('S') else '#ffedd5',edgecolors='#334155',zorder=3)
        ax.text(x,y,n,ha='center',va='center',zorder=4)
    for n,text in [('S1','input 0.8'),('S2','input 0.2'),('M1','capacity 0.4'),('M2','capacity 0.8')]:
        x,y=pos[n];ax.text(x,y+.2,text,ha='center',fontsize=9)
    ax.text(.65,-.35,'Dashed: added access, capacity 0.4',ha='center',color='#047857',fontsize=9)
    ax.set(xlim=(-.4,1.8),ylim=(-.5,1.45),title='Constructed access graph');ax.axis('off')
    names=['baseline','remote_capacity_doubled','local_capacity_doubled','access_bridge_added','input_location_swapped']
    labels=['Baseline','Remote capacity x2','Local capacity x2','Add access bridge','Swap input location']
    axes[1].barh(labels,[outputs[n]['max_feasible_flow'] for n in names],color=['#64748b','#64748b','#059669','#059669','#059669'])
    axes[1].axvline(1,color='black',ls='--',lw=.8);axes[1].set(xlim=(0,1.12),xlabel='Ideal feasible throughput (input = 1)',title='Where capacity is matters');axes[1].invert_yaxis()
    fig.suptitle('SYNTHETIC: pooled capacity is not accessible capacity; no biological fit')
    fig.savefig(P/'spatial_counterexample.png',dpi=145);plt.close(fig)
    print(json.dumps({'source_summaries':summaries,'source_contrasts':contrasts,'network_flow':{k:v['max_feasible_flow'] for k,v in outputs.items()},'passed_checks':len(checks)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

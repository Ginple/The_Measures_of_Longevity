"""Synthetic equal-load timing counterexample. No biological fit or dose advice."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent

def cycle(r, segments, V, K, linear, dense=False):
    rows=[]; elapsed=0.; y=np.array([r,0.,0.])
    for duration,J in segments:
        def fun(t,y):
            v=V*y[0]/K if linear else V*y[0]/(K+y[0])
            return [J-v,v,y[0]]
        sol=solve_ivp(fun,[0,duration],y,rtol=1e-11,atol=1e-12,
                      t_eval=np.linspace(0,duration,401) if dense else None)
        assert sol.success
        if dense:
            for t,R,Q,A in zip(sol.t,sol.y[0],sol.y[1],sol.y[2]):
                rows.append({'time':elapsed+float(t),'backlog':float(R),'input_rate':J,
                             'processed':float(Q),'backlog_integral':float(A)})
        y=sol.y[:,-1];elapsed+=duration
    return y,rows

def main():
    V=K=1.;J=.6;T=8.;duty=.125
    cases=[('saturating_constant',False,[(T,J)]),
           ('saturating_pulse',False,[(T*duty,J/duty),(T*(1-duty),0.)]),
           ('linear_constant',True,[(T,J)]),
           ('linear_pulse',True,[(T*duty,J/duty),(T*(1-duty),0.)])]
    summaries=[];traces=[];checks=[]
    def ck(name,value):
        assert bool(value),name
        checks.append({'name':name,'passed':True})
    for name,linear,segments in cases:
        r=0.
        for n in range(10000):
            out,_=cycle(r,segments,V,K,linear)
            if abs(out[0]-r)<1e-11:break
            r=float(out[0])
        else:raise RuntimeError('periodic convergence failed')
        out,rows=cycle(r,segments,V,K,linear,True)
        amount=sum(d*j for d,j in segments)
        ck(name+' periodic closure',abs(out[0]-r)<1e-9)
        ck(name+' throughput equals input',abs(out[1]-amount)<1e-8)
        ck(name+' mass balance',abs(out[0]+out[1]-r-amount)<1e-8)
        ck(name+' nonnegative',min(z['backlog'] for z in rows)>=0)
        summaries.append({'scenario':name,'mean_input':amount/T,'input_per_cycle':amount,
                          'processed_per_cycle':float(out[1]),'mean_backlog':float(out[2]/T),
                          'peak_backlog_sampled':max(z['backlog'] for z in rows),
                          'min_backlog_sampled':min(z['backlog'] for z in rows),
                          'periodic_start_end_error':float(out[0]-r),'burn_in_cycles':n+1})
        for row in rows: row['scenario']=name
        traces.extend(rows)
    s={z['scenario']:z for z in summaries}
    equilibrium=K*J/(V-J)
    ck('saturating constant matches analytic equilibrium',abs(s['saturating_constant']['mean_backlog']-equilibrium)<1e-8)
    ck('Jensen inequality strict in pulse example',s['saturating_pulse']['mean_backlog']>equilibrium)
    ck('linear control same mean backlog',abs(s['linear_pulse']['mean_backlog']-s['linear_constant']['mean_backlog'])<1e-8)
    ck('linear control can still have higher peaks',s['linear_pulse']['peak_backlog_sampled']>s['linear_constant']['peak_backlog_sampled'])
    # Stop input: finite transient backlog does not imply irreversible damage/hysteresis.
    washout,_=cycle(s['saturating_pulse']['peak_backlog_sampled'],[(200.,0.)],V,K,False)
    ck('no-input washout returns close to zero',abs(washout[0])<1e-8)
    record={'all_parameters_synthetic_dimensionless':True,'biological_fit':False,
            'parameters':{'V':V,'K':K,'mean_J':J,'period':T,'pulse_duty':duty},
            'summaries':summaries,'checks':checks,
            'interpretation':'Same periodic total throughput, different retained backlog; not lifespan, injury, or a recommended dosing schedule.'}
    (P/'RESULTS.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    df=pd.DataFrame(traces);df.to_csv(P/'SYNTHETIC_PULSE_TRACES.csv',index=False)
    fig,axes=plt.subplots(1,2,figsize=(11,3.6),layout='constrained')
    for name,sub in df.groupby('scenario',sort=False):
        axes[1 if name.startswith('linear') else 0].plot(sub.time,sub.backlog,label=name)
    for ax,title in zip(axes,['Saturating processing','Linear processing control']):
        ax.set(xlabel='Arbitrary time, one periodic cycle',ylabel='Synthetic retained cargo',title=title);ax.legend(fontsize=8)
    fig.suptitle('SYNTHETIC: equal total input, not equal backlog; no biological fit')
    fig.savefig(P/'pulse_counterexample.png',dpi=140);plt.close(fig)
    print(json.dumps(record,indent=2))
if __name__=='__main__':main()

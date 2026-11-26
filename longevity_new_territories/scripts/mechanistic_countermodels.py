"""Deliberately synthetic, dimensionless models. Not fitted to biology or clinical doses."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.special import expit,logit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parents[1]
def js(n,o):(P/'results'/n).write_text(json.dumps(o,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

def cargo(g,k,e,u,V,K,initial,T=120,n=601):
 def fun(t,y):
  L,Pc,R,Q=y;d=V*R/(K+R)
  return [g-(k+e)*L,e*L-u*Pc,u*Pc-d,k*L+d]
 tt=np.linspace(0,T,n);s=solve_ivp(fun,[0,T],initial,t_eval=tt,rtol=1e-9,atol=1e-11)
 assert s.success
 a=s.y;balance=a.sum(axis=0)-(sum(initial)+g*tt)
 return pd.DataFrame({'t':tt,'source_cargo':a[0],'transit_cargo':a[1],'recipient_cargo':a[2],'terminally_processed_cumulative':a[3],'retained_total':a[:3].sum(axis=0),'balance_error':balance})

def schedule(order,b=.6,T=2.,a=1.,z0=.9,x0=.1):
 # rW=1-.8*z, rM=.8-.2*z gives difference -.2+.6*z; b varied as model sensitivity.
 y=np.array([logit(x0),z0]);parts=[]
 for i,action in enumerate(order):
  def fun(t,y):
   ell,z=y
   return [(-.2+b*z) if action=='R' else 0.,-a*z if action=='N' else 0.]
  ss=solve_ivp(fun,[0,T],y,t_eval=np.linspace(0,T,101),rtol=1e-10,atol=1e-12);assert ss.success;y=ss.y[:,-1]
  parts.extend({'t':float(t+i*T),'mutant_fraction':float(expit(ell)),'niche_state':float(z),'action':action,'schedule':''.join(order)} for t,ell,z in zip(ss.t,ss.y[0],ss.y[1]))
 return {'schedule':''.join(order),'x_final':float(expit(y[0])),'z_final':float(y[1]),'logit_final':float(y[0])},pd.DataFrame(parts)

def main():
 g,k,u,K=1.,.4,1.,1.;ew,em,V=.1,1.2,.55;jw=g*ew/(k+ew);jm=g*em/(k+em);xc=(V-jw)/(jm-jw)
 initial=[g/(k+ew),jw/u,K*jw/(V-jw),0.]
 rows=[];trajectories=[]
 for name,e,cap in [('baseline',ew,V),('export_only',em,V),('export_plus_capacity',em,2.)]:
  d=cargo(g,k,e,u,cap,K,initial);d['scenario']=name;trajectories.append(d)
  J=g*e/(k+e);row={'scenario':name,'g':g,'k':k,'e':e,'Vmax':cap,'J_steady_export':J,'bounded_steady_state':J<cap,'terminal_source_cargo':float(d.source_cargo.iloc[-1]),'terminal_recipient_cargo':float(d.recipient_cargo.iloc[-1]),'terminal_retained_total':float(d.retained_total.iloc[-1]),'max_abs_balance_error':float(d.balance_error.abs().max())}
  if J<cap:row.update({'analytic_source_star':g/(k+e),'analytic_transit_star':J/u,'analytic_recipient_star':K*J/(cap-J)})
  rows.append(row)
 tr=pd.concat(trajectories,ignore_index=True);tr.to_csv(P/'results/SYNTHETIC_CARGO_TRAJECTORIES.csv',index=False)
 # Below-capacity example: increasing export can raise total retained cargo even at equilibrium.
 def equilibrium(e,cap):
  J=g*e/(k+e);return g/(k+e)+J/u+K*J/(cap-J)
 below={'Vmax':.95,'baseline_total':equilibrium(ew,.95),'increased_export_total':equilibrium(em,.95),'source_baseline':g/(k+ew),'source_after':g/(k+em),'note':'Both equilibria bounded; total cargo is not itself a health score.'}
 # Check exact balance, zero export and high capacity limits.
 tests=[]
 def ck(n,b):assert bool(b),n;tests.append({'name':n,'passed':True})
 ck('all cargo conserved including terminal processing',all(r['max_abs_balance_error']<1e-7 for r in rows))
 zero=cargo(g,k,0,u,V,K,[1,0,0,0]);ck('zero export leaves downstream empty',np.allclose(zero.transit_cargo,0) and np.allclose(zero.recipient_cargo,0))
 ck('export improves source yet increases retained cargo in low-capacity scenario',rows[1]['terminal_source_cargo']<rows[0]['terminal_source_cargo'] and rows[1]['terminal_retained_total']>rows[0]['terminal_retained_total'])
 ck('larger capacity reduces recipient load',rows[2]['terminal_recipient_cargo']<rows[1]['terminal_recipient_cargo'])
 ck('below-capacity counterexample',below['increased_export_total']>below['baseline_total'] and below['source_after']<below['source_baseline'])
 ck('clone threshold identity',np.isclose((1-xc)*jw+xc*jm,V))
 res=[];sched=[]
 for b in [.6,0.,-.6]:
  rr=[]
  for order in ['NR','RN']:
   r,d=schedule(order,b=b);r['b']=b;res.append(r);rr.append(r)
   if b==.6:sched.append(d)
  delta=rr[0]['logit_final']-rr[1]['logit_final'];analytic=b*2*.9*(np.exp(-2)-1)
  ck('same endpoint niche b='+str(b),np.isclose(rr[0]['z_final'],rr[1]['z_final'],atol=1e-9))
  ck('analytic schedule contrast b='+str(b),np.isclose(delta,analytic,atol=1e-9))
  if b==0:ck('commuting negative control',np.isclose(rr[0]['x_final'],rr[1]['x_final'],atol=1e-10))
 ck('order ranking reverses when ecological coefficient reverses',(res[0]['x_final']-res[1]['x_final'])*(res[4]['x_final']-res[5]['x_final'])<0)
 pd.concat(sched,ignore_index=True).to_csv(P/'results/SYNTHETIC_SCHEDULE_TRAJECTORIES.csv',index=False)
 pd.DataFrame(res).to_csv(P/'results/SYNTHETIC_SCHEDULE_ENDPOINTS.csv',index=False)
 grid=[]
 for x in np.linspace(0,1,101):
  J=(1-x)*jw+x*jm
  for cap in np.linspace(.1,1.,91):grid.append({'clone_fraction':float(x),'Vmax':float(cap),'arrival_flux':float(J),'finite_equilibrium':bool(J<cap),'recipient_equilibrium':float(K*J/(cap-J)) if J<cap else None})
 pd.DataFrame(grid).to_csv(P/'results/SYNTHETIC_CLONE_CAPACITY_GRID.csv',index=False)
 out={'all_parameters_synthetic_dimensionless':True,'not_fitted_to_TBX3_or_mitochondria':True,'equations':['dL=g-(k+e)L','dP=eL-uP','dR=uP-Vmax*R/(K+R)','dQ=kL+Vmax*R/(K+R)'],'cargo_model':rows,'below_capacity_example':below,'clone_threshold':{'JWT':jw,'Jmut':jm,'Vmax':V,'xcrit':xc,'assumption':'Fixed clone fractions, same generation rate, fixed recipient capacity; no feedback or cargo identity change.'},'order_model':res,'tests':tests,'interpretation':'Countermodels yield conditional boundaries and discriminating experiments, not empirical discoveries or treatment advice.'}
 js('COUNTERMODELS.json',out)
 fig,axes=plt.subplots(1,3,figsize=(13,4),layout='constrained');colors={'baseline':'#64748b','export_only':'#d97706','export_plus_capacity':'#2a9d8f'}
 for name,d in tr.groupby('scenario',sort=False):
  for ax,key in zip(axes,['source_cargo','recipient_cargo','retained_total']):ax.plot(d.t,d[key],label=name,color=colors[name])
 for ax,title in zip(axes,['Source looks better','Recipient can overload','Retained cargo, NOT health']):ax.set(title=title,xlabel='Arbitrary time',ylabel='Synthetic cargo units')
 axes[0].legend(fontsize=7);fig.suptitle('SYNTHETIC, not fitted data: export is not terminal processing');fig.savefig(P/'figures/02_synthetic_export_capacity.png',dpi=170);plt.close(fig)
 fig,axes=plt.subplots(1,2,figsize=(10.5,4.2),layout='constrained')
 for d in sched:
  for ax,key in zip(axes,['mutant_fraction','niche_state']):ax.plot(d.t,d[key],label=d.schedule.iloc[0])
 for ax,title in zip(axes,['Same exposures, different clone fractions','Same final niche state']):ax.set(title=title,xlabel='Arbitrary time');ax.legend()
 fig.suptitle('SYNTHETIC ecological order effect | no drug identity or dosing claim');fig.savefig(P/'figures/03_synthetic_order_effect.png',dpi=170);plt.close(fig)
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()

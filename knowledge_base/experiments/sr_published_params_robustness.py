"""H-SR1 robustness: does the level-matched survival crossing survive published human SR parameters?

Synthetic re-run of the SR_SNAPSHOT_IDENTIFIABILITY comparison (lower damage
production vs. raise removal, matched so 70-year survivors carry the same mean
damage) using the human parameter set printed in Yang ... Alon, Nat Commun 2025
(s41467-025-57807-5, Methods; parameters attributed there to Karin et al. 2019;
attribution corrected 2026-11-27, ledger X128 -- values unchanged): eta = 1.4e-3 /(day*year), beta = 0.15 /day,
kappa = 0.5, eps = 0.16 /day, Xc = 17 (converted to years below). No Makeham
term, no heterogeneity: this is a model stress test, not a population estimate.
"""
import json
import sr_snapshot_identifiability as m

KARIN_2025_HUMAN = {'eta': 1.4e-3 * 365, 'beta': 0.15 * 365, 'kappa': 0.5, 'eps': 0.16 * 365, 'xc': 17.0}


def level_matched(base, d=0.2, t0=60.0, age=70.0, dt=0.05, dx=0.1, iters=16):
    kw = dict(dt=dt, dx=dx)
    untreated = m.summarize(m.survival_curve(base, **kw))
    prod = m.summarize(m.survival_curve(base, start=(t0, {**base, 'eta': base['eta'] * (1 - d)}), **kw))
    target = prod['mean_X_alive_at_70']
    lo, hi = 0.0, 0.6
    for _ in range(iters):
        mid = (lo + hi) / 2
        c = m.survival_curve(base, start=(t0, {**base, 'beta': base['beta'] / (1 - mid)}), t_end=age + 1e-9, **kw)
        lo, hi = (mid, hi) if c[-1][2] > target else (lo, mid)
    db = (lo + hi) / 2
    rem = m.summarize(m.survival_curve(base, start=(t0, {**base, 'beta': base['beta'] / (1 - db)}), **kw))
    return {'untreated': untreated, 'lower_production': prod, 'raise_removal_matched': rem, 'd_b': round(db, 4)}


def crossing(result):
    p, r = result['lower_production'], result['raise_removal_matched']
    return r['S70'] > p['S70'] and r['S90'] < p['S90']


def main():
    out = {'status': 'synthetic stress test of H-SR1 with published human SR parameters; not fitted, not clinical',
           'parameters_per_year': KARIN_2025_HUMAN, 'runs': {}}
    for d, dt, dx in [(0.2, 0.05, 0.1), (0.2, 0.02, 0.05), (0.1, 0.05, 0.1), (0.3, 0.05, 0.1)]:
        r = level_matched(KARIN_2025_HUMAN, d=d, dt=dt, dx=dx)
        r['crossing'] = crossing(r)
        out['runs'][f'd={d},dt={dt},dx={dx}'] = r
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Snapshot identifiability in a saturating-removal (SR) damage model.

Synthetic teaching model only: parameters are illustrative, calibrated so the
baseline curve has a human-like median and Gompertz-like slope. They are NOT
fitted to any cohort, are not clinical estimates, and say nothing about any
real intervention.

Model (Karin, Alon et al., Nat Commun 2019 form):
    dX = (eta*t - beta*X/(kappa+X)) dt + sqrt(2*eps) dW,  X >= 0 (reflecting),
    death at first passage X = Xc (absorbing).

Questions answered exactly or numerically here:
 1. Level matching: under the quasi-steady approximation the damage level is
    X*(t) = kappa*r/(1-r) with r = eta*t/beta. Lowering production eta by a
    factor (1-d) and raising removal beta by 1/(1-d) give the SAME X*(t) for all
    t, so any readout that is a monotone function of the level alone cannot
    tell them apart.
 2. Recovery separates them: the local relaxation rate
    lambda = beta*kappa/(kappa+X*)^2 differs by exactly 1/(1-d).
 3. Outcome separates them: first-passage survival (implicit Fokker-Planck)
    differs even though the levels coincide.
 4. A threshold change (Xc) moves survival without moving level or recovery.
 5. A one-off removal pulse lowers the level transiently; it decays toward
    the untreated trajectory with the relaxation time.
Uses only the Python standard library so it runs in the pinned CI env.
"""
import json
import math

BASE = {'eta': 0.065, 'beta': 5.0, 'kappa': 0.5, 'eps': 5.0, 'xc': 17.0}


def quasi_steady_level(t, eta, beta, kappa):
    """X* solving eta*t = beta*X/(kappa+X); infinite once eta*t >= beta."""
    if min(eta, beta, kappa) <= 0 or t < 0:
        raise ValueError('positive eta, beta, kappa and nonnegative t required')
    r = eta * t / beta
    return math.inf if r >= 1 else kappa * r / (1 - r)


def relaxation_rate(x, beta, kappa):
    """d/dX of the removal term: local return rate after a small perturbation."""
    if beta <= 0 or kappa <= 0 or x < 0:
        raise ValueError('positive beta, kappa and nonnegative x required')
    return beta * kappa / (kappa + x) ** 2


def identify_beta_kappa(x1, lam1, x2, lam2):
    """Recover (beta, kappa) from level+relaxation at two distinct levels.

    lam = beta*kappa/(kappa+x)^2  =>  sqrt(lam1/lam2) = (kappa+x2)/(kappa+x1).
    """
    if x1 == x2 or min(lam1, lam2) <= 0:
        raise ValueError('two distinct levels with positive rates required')
    s = math.sqrt(lam1 / lam2)
    kappa = (x2 - s * x1) / (s - 1)
    beta = lam1 * (kappa + x1) ** 2 / kappa
    return beta, kappa


def _thomas(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m if i < n - 1 else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def survival_curve(params, t_end=120.0, dt=0.05, dx=0.1, start=None, pulse=None):
    """Implicit upwind Fokker-Planck; returns [(t, S(t), mean X among alive)].

    start: (t0, params_after) switches parameters at age t0 (intervention).
    pulse: (t0, delta) shifts the density down by delta at t0 (one-off removal).
    """
    p0 = dict(params)
    if min(p0.values()) <= 0 or dt <= 0 or dx <= 0:
        raise ValueError('positive parameters and steps required')
    n = int(round(p0['xc'] / dx))
    xs = [i * dx for i in range(n)]          # node n (=Xc) is absorbing, p=0
    p = [0.0] * n
    p[0] = 1.0 / dx
    out, t, cur, pulsed = [], 0.0, p0, False
    steps = int(round(t_end / dt))
    for k in range(1, steps + 1):
        t = k * dt
        if start and t > start[0] and cur is p0:
            cur = dict(start[1])
            m = int(round(cur['xc'] / dx))
            if m != n:                        # threshold change: resize grid
                p = (p + [0.0] * m)[:m]
                n, xs = m, [i * dx for i in range(m)]
        if pulse and not pulsed and t > pulse[0]:
            shift = int(round(pulse[1] / dx))
            p = [sum(p[:shift + 1])] + p[shift + 1:] + [0.0] * shift
            pulsed = True
        e, b, kap, eps = cur['eta'], cur['beta'], cur['kappa'], cur['eps']
        # face drifts f_{i+1/2}, i = 0..n-1 (last face leads to absorbing node)
        f = [e * t - b * (x + dx / 2) / (kap + x + dx / 2) for x in xs]
        D = eps / dx ** 2
        a, bb, c = [0.0] * n, [0.0] * n, [0.0] * n
        for i in range(n):
            # outflow through right face i+1/2
            fr = f[i]
            out_r = (max(fr, 0) / dx + D)
            in_r = (-min(fr, 0) / dx + D) if i < n - 1 else 0.0
            bb[i] += out_r
            if i < n - 1:
                c[i] -= in_r
                # same face seen from cell i+1
                bb[i + 1] += in_r
                a[i + 1] -= out_r
        a = [dt * v for v in a]
        c = [dt * v for v in c]
        bb = [1 + dt * v for v in bb]
        p = _thomas(a, bb, c, p)
        alive = sum(p) * dx
        mean_x = sum(x * q for x, q in zip(xs, p)) * dx / alive if alive > 0 else math.nan
        out.append((t, alive, mean_x))
    return out


def summarize(curve):
    def s_at(age):
        return min(curve, key=lambda r: abs(r[0] - age))
    median = next((t for t, s, _ in curve if s < 0.5), math.nan)
    life_exp = sum(s for _, s, _ in curve) * (curve[1][0] - curve[0][0])
    h = lambda a, w=2.5: math.log(s_at(a - w)[1] / s_at(a + w)[1]) / (2 * w)
    slope = math.log(h(85) / h(60)) / 25
    return {'median_age_at_death': round(median, 2), 'life_expectancy': round(life_exp, 2),
            'gompertz_slope_60_85': round(slope, 4),
            'S70': round(s_at(70)[1], 4), 'S90': round(s_at(90)[1], 4),
            'mean_X_alive_at_70': round(s_at(70)[2], 4), 'mean_X_alive_at_61': round(s_at(61)[2], 4)}


def damage_age(untreated, value, lo=20.0):
    """Age at which the untreated survivors' mean damage equals `value`."""
    prev = None
    for t, _, m in untreated:
        if t < lo:
            continue
        if prev and (prev[1] - value) * (m - value) <= 0 and m != prev[1]:
            return round(prev[0] + (value - prev[1]) * (t - prev[0]) / (m - prev[1]), 2)
        prev = (t, m)
    return math.nan


def match_removal_to_level(target, age=70.0, t0=60.0, lo=0.0, hi=0.6, iters=18, **kw):
    """Bisection on removal boost d_b so survivors' mean X at `age` equals target."""
    b = dict(BASE)
    def level(db):
        c = survival_curve(b, start=(t0, {**b, 'beta': b['beta'] / (1 - db)}), t_end=age + 1e-9, **kw)
        return c[-1][2], c
    for _ in range(iters):
        mid = (lo + hi) / 2
        if level(mid)[0] > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def scenarios(d=0.2, t0=60.0, pulse_delta=1.0, **kw):
    b = dict(BASE)
    lower_prod = {**b, 'eta': b['eta'] * (1 - d)}
    raise_rem = {**b, 'beta': b['beta'] / (1 - d)}
    raise_thr = {**b, 'xc': b['xc'] + 1.0}
    runs = {'untreated': survival_curve(b, **kw),
            'lower_production': survival_curve(b, start=(t0, lower_prod), **kw),
            'raise_removal': survival_curve(b, start=(t0, raise_rem), **kw),
            'raise_threshold': survival_curve(b, start=(t0, raise_thr), **kw),
            'removal_pulse': survival_curve(b, pulse=(t0, pulse_delta), **kw)}
    return {k: summarize(v) for k, v in runs.items()}, runs


def main():
    b, d, t = BASE, 0.2, 70.0
    xa = quasi_steady_level(t, b['eta'] * (1 - d), b['beta'], b['kappa'])
    xb = quasi_steady_level(t, b['eta'], b['beta'] / (1 - d), b['kappa'])
    la = relaxation_rate(xa, b['beta'], b['kappa'])
    lb = relaxation_rate(xb, b['beta'] / (1 - d), b['kappa'])
    summary, runs = scenarios(d=d)
    target = summary['lower_production']['mean_X_alive_at_70']
    db = match_removal_to_level(target)
    matched = summarize(survival_curve(b, start=(60.0, {**b, 'beta': b['beta'] / (1 - db)})))
    un = runs['untreated']
    damage_ages = {k: {'at_61': damage_age(un, v['mean_X_alive_at_61']),
                       'at_70': damage_age(un, v['mean_X_alive_at_70'])} for k, v in summary.items()}
    matched_x = matched['mean_X_alive_at_70']
    print(json.dumps({
        'status': 'synthetic SR teaching model; illustrative parameters, not fitted or clinical',
        'parameters': b, 'intervention_fraction_d': d, 'intervention_age': 60.0,
        'quasi_steady_at_70': {'lower_production_X': xa, 'raise_removal_X': xb,
                               'lower_production_relaxation_per_year': la,
                               'raise_removal_relaxation_per_year': lb,
                               'relaxation_ratio': lb / la},
        'first_passage_summaries': summary,
        'damage_age_of_survivor_mean_on_untreated_curve': damage_ages,
        'level_matched_at_70': {
            'lower_production_d': d, 'raise_removal_d_matched': round(db, 4),
            'lower_production': summary['lower_production'], 'raise_removal_matched': matched,
            'local_relaxation_at_survivor_mean': {
                'lower_production': relaxation_rate(target, b['beta'], b['kappa']),
                'raise_removal_matched': relaxation_rate(matched_x, b['beta'] / (1 - db), b['kappa'])}}},
        indent=2))


if __name__ == '__main__':
    main()

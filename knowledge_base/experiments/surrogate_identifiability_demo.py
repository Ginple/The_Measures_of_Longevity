#!/usr/bin/env python3
"""Synthetic counterexample: perfect marker/outcome correlation is not surrogacy.

Construct two deterministic potential-outcome worlds with identical baseline
and treated marker values for each unit and identical untreated outcomes.
A favorable marker change coexists with opposite clinical effects. This toy
has no real participants, no uncertainty model, and no clinical application.
"""
from math import sqrt


def correlation(xs, ys):
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("paired vectors of length >= 2 required")
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    x = [v - mx for v in xs]
    y = [v - my for v in ys]
    denom = sqrt(sum(v*v for v in x) * sum(v*v for v in y))
    if denom == 0:
        raise ValueError("zero variance")
    return sum(a*b for a, b in zip(x, y)) / denom


def run():
    # Lower means better for both the hypothetical marker S and outcome Y.
    u = [float(x) for x in range(10)]
    s0 = u[:]
    s1 = [v - 1 for v in u]
    y0 = u[:]
    y1_benefit = [v - 1 for v in u]
    y1_harm = [v + 1 for v in u]
    mean = lambda xs: sum(xs) / len(xs)
    s_effect = mean(s1) - mean(s0)
    benefit = mean(y1_benefit) - mean(y0)
    harm = mean(y1_harm) - mean(y0)
    assert s_effect == -1 and benefit == -1 and harm == 1
    assert abs(correlation(s0, y0)-1) < 1e-12
    assert abs(correlation(s1, y1_benefit)-1) < 1e-12
    assert abs(correlation(s1, y1_harm)-1) < 1e-12
    assert s0 == u and s1 == [v-1 for v in u]
    print(f"S treatment effect in both worlds: {s_effect:+.0f} (lower is better)")
    print(f"Y treatment effect, beneficial world: {benefit:+.0f}")
    print(f"Y treatment effect, harmful world:    {harm:+.0f}")
    print("Within-arm marker/outcome Pearson r = 1 in both worlds and arms.")
    print("Conclusion: equal favorable marker effects and perfect correlations do not identify clinical effect.")
    print("Synthetic deterministic example, not data; no empirical surrogacy estimate.")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Null FWER counterexamples to 90%-variance PCA effective-test thresholds.

For m equicorrelated standard normal test statistics with nonnegative rho,
we know their eigenvalues and can integrate the two-sided global-null FWER.
No study data, estimated correlations, or claims about a real paper's FWER.
Numerical integration uses Simpson's rule over a standard-normal latent factor.
"""
from math import exp, pi, sqrt
from statistics import NormalDist

NORMAL = NormalDist()


def pca90(m, rho):
    if not isinstance(m, int) or m < 2 or not 0 <= rho < 1:
        raise ValueError('require integer m>=2 and 0<=rho<1')
    eigenvalues = [1 + (m - 1) * rho] + [1 - rho] * (m - 1)
    total = 0.0
    for i, value in enumerate(eigenvalues, start=1):
        total += value
        if total >= 0.9 * m - 1e-12:
            return i
    raise ArithmeticError('PCA count did not converge')


def fwer_independent(m, threshold):
    if not isinstance(m, int) or m < 1 or not 0 <= threshold <= 1:
        raise ValueError('invalid number of tests or threshold')
    return 1 - (1 - threshold) ** m


def fwer_equicorrelated(m, rho, threshold, intervals=6000, limit=9.0):
    """Probability >=1 of m two-sided normal tests is below threshold.

    X_i = sqrt(rho)*Z + sqrt(1-rho)*E_i; all Z/E_i are iid N(0,1).
    Conditional on Z, E_i are independent. Integrate conditional probability.
    Truncation at +/-9 loses less than 3e-19 of normal mass; quadrature error
    is assessed empirically in tests and should not be confused with CI.
    """
    if not isinstance(m, int) or m < 1 or not 0 <= rho < 1:
        raise ValueError('invalid m or rho')
    if not 0 < threshold < 1 or intervals < 2 or intervals % 2 or limit <= 0:
        raise ValueError('invalid threshold or integration grid')
    cutoff = NORMAL.inv_cdf(1 - threshold / 2)
    a, b = sqrt(rho), sqrt(1-rho)

    def integrand(z):
        inside = NORMAL.cdf((cutoff-a*z)/b) - NORMAL.cdf((-cutoff-a*z)/b)
        return (1 - max(0.0, min(1.0, inside))**m) * exp(-z*z/2) / sqrt(2*pi)

    h = 2 * limit / intervals
    result = integrand(-limit) + integrand(limit)
    for i in range(1, intervals):
        result += (4 if i % 2 else 2) * integrand(-limit + i*h)
    return result * h / 3


def main():
    m, alpha = 16, 0.05
    for rho in (0.0, 0.9):
        k = pca90(m, rho)
        raw = fwer_equicorrelated(m, rho, alpha)
        by_k = fwer_equicorrelated(m, rho, alpha/k)
        by_m = fwer_equicorrelated(m, rho, alpha/m)
        print(f'rho={rho:.1f} m={m} PCs90={k}: FWER nominal={raw:.6f}; '
              f'alpha/PCs={by_k:.6f}; alpha/m={by_m:.6f}')
    print('Synthetic normal global-null calculations, not an estimate of TranslAGE error rates.')
    print('Bonferroni alpha/m has strong FWER control with valid p-values under arbitrary dependence.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact steady-state stock/flow examples; not actual tissue data."""
from fractions import Fraction as F
import json


def equilibrium(input_rate, exit_hazard):
    j, k = F(input_rate), F(exit_hazard)
    if j < 0 or k <= 0:
        raise ValueError('input must be nonnegative and exit hazard positive')
    return j/k


def balance(stock, input_rate, exit_hazard):
    stock, j, k = F(stock), F(input_rate), F(exit_hazard)
    if stock < 0 or j < 0 or k < 0:
        raise ValueError('stock, input and hazard must be nonnegative')
    return j-k*stock


def main():
    worlds = [(1, 1), (2, 1), (2, 2)]
    print(json.dumps([{'input_rate': j, 'exit_hazard': k,
                       'equilibrium_stock': str(equilibrium(j, k)),
                       'net_change_at_equilibrium': str(balance(equilibrium(j, k), j, k))}
                      for j, k in worlds], indent=2))


if __name__ == '__main__':
    main()

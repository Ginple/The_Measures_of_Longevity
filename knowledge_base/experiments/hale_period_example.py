#!/usr/bin/env python3
"""Exact synthetic period life-table arithmetic; no WHO data or projections."""
from fractions import Fraction as F
import json


def hale(n, person_years, lost_fractions):
    if type(n) is not int or n <= 0:
        raise ValueError('positive cohort required')
    if len(person_years) != len(lost_fractions) or not person_years:
        raise ValueError('one loss fraction per nonempty interval')
    p, d = tuple(map(F, person_years)), tuple(map(F, lost_fractions))
    if any(x < 0 for x in p) or any(not 0 <= x <= 1 for x in d):
        raise ValueError('nonnegative person-years and loss fractions in [0,1] required')
    le = sum(p, F(0)) / n
    loss = sum((a*b for a, b in zip(p, d)), F(0)) / n
    return le, le-loss, loss


def slope_difference(change, start_year, end_year):
    if type(start_year) is not int or type(end_year) is not int or end_year <= start_year:
        raise ValueError('years must be distinct increasing integers')
    change = F(change)
    return change/F(end_year-start_year), change/F(end_year-start_year+1)


def main():
    le, healthy, loss = hale(100, [1000, 800], [F(1, 10), F(1, 4)])
    elapsed, inclusive = slope_difference(F(13, 2), 2000, 2019)
    print(json.dumps({'scope': 'SYNTHETIC life table; not WHO data',
                      'life_expectancy': str(le), 'healthy_equivalent': str(healthy),
                      'equivalent_loss': str(loss),
                      'illustrative_rounded_global_6_5_change_div_19': str(elapsed),
                      'illustrative_rounded_global_6_5_change_div_20': str(inclusive)}, indent=2))


if __name__ == '__main__':
    main()

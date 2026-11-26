"""Estimator-aware percentage screening. Arithmetic diagnostics, not truth checks."""
from decimal import Decimal,localcontext,ROUND_HALF_UP,InvalidOperation


def check_percentage(printed_percent, denominator, estimator):
    """Use integer k/N compatibility ONLY for crude, unweighted binary proportions.

    Printed values use declared decimal precision and ROUND_HALF_UP. Weighted,
    adjusted, standardized and survival estimates need their own estimand contracts.
    """
    if estimator != 'crude_unweighted_binary':
        return {'status':'requires_estimand_specific_check','applied_integer_rule':False,'not_a_pass':True}
    if type(denominator) is not int or denominator <= 0:
        raise ValueError('positive_integer_denominator_required')
    p=Decimal(str(printed_percent))
    if not p.is_finite() or not 0<=p<=100:raise ValueError('percentage_out_of_range')
    if 'e' in str(printed_percent).lower():raise ValueError('explicit_decimal_printing_required')
    precision=max(0,-p.as_tuple().exponent)
    if precision>12:raise ValueError('printing_precision_budget')
    with localcontext() as ctx:
        ctx.prec=max(50,len(str(denominator))+30)
        step=Decimal(1).scaleb(-precision)
        central=p*denominator/100
        # Monotone rounding: if any integer matches, one adjacent to central does.
        candidates={int(central),int(central)+1}
        matches=[k for k in sorted(candidates) if 0<=k<=denominator and (Decimal(100)*k/denominator).quantize(step,rounding=ROUND_HALF_UP)==p]
    return {'status':'compatible_with_printed_rounding' if matches else 'incompatible_with_crude_count',
            'applied_integer_rule':True,'example_compatible_numerators':matches,
            'rounding':'ROUND_HALF_UP','precision':precision,'semantic_validity':'not_checked'}


def execution_contract(records,min_ran=1):
    """Count executed blocking checks, not skipped/advisory rows. No vacuous pass."""
    if type(min_ran) is not int or min_ran<1:raise ValueError('positive_min_ran_required_in_this_project')
    allowed={'ran_pass','ran_fail','skipped','not_applicable'}
    if any(r.get('status') not in allowed or type(r.get('blocking')) is not bool for r in records):raise ValueError('invalid_execution_record')
    ran=[r for r in records if r['blocking'] and r['status'] in ('ran_pass','ran_fail')]
    failures=[r for r in records if r['blocking'] and r['status']=='ran_fail']
    unresolved=[r for r in records if r['blocking'] and r['status'] in ('skipped','not_applicable')]
    return {'status':'pass_encoded_execution_contract_only' if len(ran)>=min_ran and not failures and not unresolved else 'fail',
            'executed_blocking_checks':len(ran),'min_ran':min_ran,
            'blocking_failed':len(failures),'blocking_not_run':len(unresolved),
            'scientific_truth':'not_computed'}

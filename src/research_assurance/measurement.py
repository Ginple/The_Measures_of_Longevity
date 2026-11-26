"""Small diagnostic contracts; examples do not estimate a biological treatment effect."""
import itertools
import math


def numeric_distances(trajectories):
    if not trajectories or len({len(r) for r in trajectories}) != 1:
        raise ValueError('nonempty_rectangular_trajectories_required')
    return [math.sqrt(sum((x-y)**2 for x, y in zip(a, b))) for a, b in itertools.combinations(trajectories, 2)]


def nominal_distances(trajectories):
    """One-hot Euclidean distance for observed states, with no missing state support.

    Categorical disagreement contributes two. No claim of validated biological distance.
    """
    if not trajectories or len({len(r) for r in trajectories}) != 1 or any(x is None for r in trajectories for x in r):
        raise ValueError('rectangular_fully_observed_states_required')
    return [math.sqrt(2*sum(x != y for x, y in zip(a, b))) for a, b in itertools.combinations(trajectories, 2)]


def nominal_relabelling_audit(trajectories, max_labels=6):
    labels = sorted(set(x for row in trajectories for x in row))
    if len(labels) > max_labels:
        return {'state': 'unknown', 'reason': 'factorial_budget', 'actual_reanalysis': False}
    base = numeric_distances(trajectories)
    control = nominal_distances(trajectories)
    runs = []
    for perm in itertools.permutations(labels):
        mapping = dict(zip(labels, perm))
        changed = [[mapping[x] for x in row] for row in trajectories]
        dist = numeric_distances(changed)
        runs.append({'mapping': [[k, v] for k, v in mapping.items()],
                     'numeric_distances': dist, 'numeric_invariant': all(math.isclose(x, y) for x, y in zip(base, dist)),
                     'onehot_distance_invariant': nominal_distances(changed) == control})
    return {'state': 'audited', 'runs': runs, 'numeric_invariant_all': all(r['numeric_invariant'] for r in runs),
            'onehot_invariant_all': all(r['onehot_distance_invariant'] for r in runs),
            'meaning': 'conditional representation test; not biological validation or empirical reanalysis'}


def founder_bounds(founders):
    """Binary target, fixed cohort. Unknown is neither observed failure nor success.

    Each founder contributes at most once. Divisions require a predeclared lineage
    estimand; this helper rejects attempts to count descendants as original founders.
    Conditional descriptive bounds only, not a causal effect or confidence interval.
    """
    if not founders or len({r['founder_id'] for r in founders}) != len(founders):
        raise ValueError('nonempty_unique_founders_required')
    allowed = {'target_observed', 'non_target_observed', 'death_confirmed', 'lost_unknown'}
    if any(r['state'] not in allowed for r in founders):
        raise ValueError('unknown_event_state')
    n = len(founders)
    success = sum(r['state'] == 'target_observed' for r in founders)
    unknown = sum(r['state'] == 'lost_unknown' for r in founders)
    return {'N_baseline_founders': n, 'target_observed': success, 'lost_unknown': unknown,
            'target_fraction_bounds': [success/n, (success+unknown)/n],
            'assumptions': 'Fixed baseline cohort; observed targets/non-targets/deaths correctly classified; death predeclared non-target for this toy binary estimand.',
            'not_established': ['tracking validity', 'target validity', 'death from lost tracking', 'causal effect', 'functional rejuvenation']}


def weighted_fraction(values, weights):
    if not values or len(values) != len(weights) or any(not math.isfinite(v) or not 0 <= v <= 1 for v in values) or any(not math.isfinite(w) or w <= 0 for w in weights):
        raise ValueError('bounded_fractions_and_positive_finite_weights_required')
    return sum(v*w for v, w in zip(values, weights))/sum(weights)

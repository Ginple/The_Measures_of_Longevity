"""Lexical discourse topology, NOT causal/semantic knowledge discovery.

A caller supplies already-reviewed units and concept hits. Empty detections are
kept out of the observed graph and explicitly reported, not relabelled discoveries.
"""
from collections import Counter
from itertools import combinations
import math
import networkx as nx


def classify(metrics):
    """Historical v2 heuristic; unvalidated and NOT a psychological diagnosis."""
    m = metrics
    if m['outside_largest_component'] > .20 or (m['Q'] >= .55 and m['cross_weight_share'] < .10):
        return 'dispersed'
    if m['largest_strength_share'] >= .60 and m['Q'] < .25:
        return 'biased_single_cluster_dominance_only'
    if m['communities'] >= 3 and m['Q'] >= .30 and m['largest_strength_share'] <= .50:
        return 'diversified'
    return 'focused'


def analyze(units, ontology, seed=0, resolution=1., min_support=1, prose_only=False):
    if type(min_support) is not int or min_support < 1 or resolution <= 0:
        raise ValueError('positive_support_and_resolution_required')
    concept_ids = [c['id'] for c in ontology]
    if len(concept_ids) != len(set(concept_ids)) or len({u['id'] for u in units}) != len(units):
        raise ValueError('duplicate_ids')
    known = set(concept_ids)
    support, edges, by_node, by_edge = Counter(), Counter(), {}, {}
    selected = [u for u in units if not prose_only or u['kind'] == 'prose']
    for u in selected:
        hit = sorted(set(u['concept_ids']))
        if not set(hit) <= known:
            raise ValueError('unknown_concept')
        for c in hit:
            support[c] += 1
            by_node.setdefault(c, []).append(u['id'])
        for pair in combinations(hit, 2):
            edges[pair] += 1
            by_edge.setdefault(pair, []).append(u['id'])
    G = nx.Graph()
    G.add_nodes_from(sorted(support))
    for (a, b), w in sorted(edges.items()):
        if w >= min_support:
            G.add_edge(a, b, weight=w, distance=1/w)
    if G.number_of_edges():
        cs = nx.community.louvain_communities(G, seed=seed, resolution=resolution, weight='weight')
    else:
        cs = [{n} for n in G]
    cs = sorted([sorted(c) for c in cs], key=lambda c: tuple(c))
    partition = {n: i for i, c in enumerate(cs) for n in c}
    strength = dict(G.degree(weight='weight'))
    total = sum(strength.values())
    Q = nx.community.modularity(G, cs, weight='weight', resolution=1) if G.number_of_edges() else 0.
    cross = sum(d['weight'] for a, b, d in G.edges(data=True) if partition[a] != partition[b])
    m = {'Q': Q, 'communities': len(cs),
         'outside_largest_component': 1 - max(map(len, nx.connected_components(G)), default=0)/len(G) if G else 0.,
         'largest_strength_share': max((sum(strength[n] for n in c)/total for c in cs), default=0.) if total else (max(map(len, cs), default=0)/len(G) if G else 0.),
         'cross_weight_share': cross/G.size(weight='weight') if G.number_of_edges() else 0.}
    bc = nx.betweenness_centrality(G, weight='distance')
    nodes = []
    for n in sorted(G):
        per = Counter()
        for x, e in G[n].items():
            per[partition[x]] += e['weight']
        nodes.append({'id': n, 'units': support[n], 'unit_ids': sorted(by_node[n]),
                      'strength': strength[n], 'betweenness': bc[n],
                      'participation': 1-sum((s/strength[n])**2 for s in per.values()) if strength[n] else 0.})
    pairs = []
    for i, j in combinations(range(len(cs)), 2):
        possible = len(cs[i])*len(cs[j])
        actual = sum(G.has_edge(a, b) for a in cs[i] for b in cs[j])
        missing = []
        for a in cs[i]:
            for b in cs[j]:
                if not G.has_edge(a, b):
                    missing.append({'a': a, 'b': b, 'common_neighbors': sorted(nx.common_neighbors(G, a, b)),
                                    'shortest_unweighted_path': nx.shortest_path(G, a, b) if nx.has_path(G, a, b) else None,
                                    'endpoint_units': [sorted(by_node[a]), sorted(by_node[b])],
                                    'status': 'structural_candidate_requires_semantic_review'})
        pairs.append({'communities': [i, j], 'actual_edges': actual, 'possible_edges': possible,
                      'density': actual/possible, 'zero_cross_edges': actual == 0, 'missing_endpoint_pairs': missing})
    return {'semantics': 'undirected_unit_cooccurrence_only', 'parameters': {'seed': seed, 'resolution': resolution, 'min_support': min_support, 'prose_only': prose_only},
            'metrics': m, 'local_heuristic_state': classify(m) if G else 'not_applicable_empty_graph',
            'communities': cs, 'nodes': nodes,
            'edges': [{'a': a, 'b': b, 'weight': d['weight'], 'unit_ids': sorted(by_edge[(a, b)])} for a, b, d in G.edges(data=True)],
            'components': sorted([sorted(c) for c in nx.connected_components(G)]), 'isolates': sorted(nx.isolates(G)),
            'cluster_pairs': pairs, 'low_support': sorted(n for n in G if support[n] <= 2),
            'zero_detected_vocabulary_entries': sorted(known-set(G)),
            'warning': 'Zero detections are not vocabulary-external discoveries; states unvalidated; centrality is not causal importance.'}


def adjusted_rand(left, right):
    a = {n: i for i, c in enumerate(left) for n in c}
    b = {n: i for i, c in enumerate(right) for n in c}
    if set(a) != set(b):
        return None  # Avoid silently comparing a smaller overlap as full stability.
    n = len(a)
    if n < 2:
        return 1.
    c2 = lambda x: x*(x-1)/2
    cells = Counter((a[k], b[k]) for k in a)
    ca, cb = Counter(a.values()), Counter(b.values())
    x, u, v = sum(map(c2, cells.values())), sum(map(c2, ca.values())), sum(map(c2, cb.values()))
    expected = u*v/c2(n)
    den = .5*(u+v)-expected
    return (x-expected)/den if den else 1.


def sensitivity(units, ontology, seeds=(0, 1, 2), resolutions=(.75, 1., 1.25), supports=(1, 2)):
    base = analyze(units, ontology)
    runs = []
    for support in supports:
        for res in resolutions:
            for seed in seeds:
                result = analyze(units, ontology, seed=seed, resolution=res, min_support=support)
                runs.append({'parameters': result['parameters'], 'metrics': result['metrics'],
                             'state': result['local_heuristic_state'],
                             'ARI_to_seed0_r1_support1': adjusted_rand(base['communities'], result['communities'])})
    return {'runs': runs, 'states': dict(sorted(Counter(r['state'] for r in runs).items())),
            'warning': 'Parameter robustness is not construct validity; only listed modes were tested.'}

"""Seven local task families. No calls to InfraNodus or claims of validated diversity scores."""
from .topology import analyze, sensitivity


def generate_topical_clusters(units, ontology):
    return analyze(units, ontology)['communities']


def optimize_text_structure(units, ontology):
    result = analyze(units, ontology)
    return {'metrics': result['metrics'], 'local_heuristic_state': result['local_heuristic_state'],
            'sensitivity': sensitivity(units, ontology), 'edits_applied': False,
            'warning': 'Diagnosis candidates, not an objective function for scientific quality.'}


def generate_content_gaps(units, ontology):
    return analyze(units, ontology)['cluster_pairs']


def develop_conceptual_bridges(units, ontology):
    return [m for pair in generate_content_gaps(units, ontology) for m in pair['missing_endpoint_pairs']]


def develop_latent_topics(units, ontology):
    result = analyze(units, ontology)
    return {'low_observed_support': result['low_support'],
            'zero_detected_in_declared_vocabulary': result['zero_detected_vocabulary_entries'],
            'vocabulary_external_topics': 'not_detected_by_this_algorithm'}


def generate_knowledge_graph(units, ontology):
    result = analyze(units, ontology)
    return {'nodes': result['nodes'], 'edges': result['edges'],
            'relation': 'cooccurs_with_not_causes', 'causal_knowledge_graph': False}


def generate_research_questions(contracts):
    """Render human-authored research contracts; never invent validity or novelty."""
    required = {'id', 'question', 'source_ids', 'alternatives', 'discriminating_observation', 'next_information', 'stop_conditions'}
    out = []
    for c in contracts:
        if not required <= set(c) or any(not c[k] for k in required):
            raise ValueError('incomplete_research_contract')
        out.append({**c, 'status': 'proposed_not_implemented_not_novelty_certified'})
    return out

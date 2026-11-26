"""Evidence-bound bookkeeping, NOT an automatic scientific truth evaluator."""
from pathlib import Path
import difflib
import hashlib
import json
from collections import deque


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def confined(root, name):
    """Reject absolute paths, traversal and symlink escapes, including missing targets."""
    root = Path(root).resolve()
    if Path(name).is_absolute():
        raise ValueError('absolute_path_forbidden')
    target = (root / name).resolve()
    if target == root or root not in target.parents:
        raise ValueError('path_escape')
    return target


def read_span(data, start, end):
    """UTF-8 exact bytes; 1-based half-open line range. No whitespace normalization."""
    if type(start) is not int or type(end) is not int:
        raise ValueError('line_numbers_must_be_integers')
    lines = data.decode('utf-8').splitlines(keepends=True)
    if not 1 <= start < end <= len(lines) + 1:
        raise ValueError('span_out_of_range')
    return ''.join(lines[start - 1:end - 1])


def validate(project):
    from jsonschema import Draft202012Validator
    schema = json.loads((Path(__file__).with_name('project.schema.json')).read_text())
    errors = sorted(Draft202012Validator(schema).iter_errors(project), key=lambda e: str(e.path))
    problems = [{'path': list(e.path), 'reason': e.message} for e in errors]
    if problems:
        return problems
    for group in ('artifacts', 'claims', 'evidence', 'reviews', 'debts'):
        ids = [x.get('id') for x in project.get(group, []) if isinstance(x, dict)]
        if len(ids) != len(set(ids)):
            problems.append({'path': [group], 'reason': 'duplicate_ids'})
    all_ids = [x.get('id') for group in ('artifacts', 'claims', 'evidence', 'reviews', 'debts') for x in project.get(group, []) if isinstance(x, dict)]
    if len(all_ids) != len(set(all_ids)):
        problems.append({'path': [], 'reason': 'ids_must_be_globally_unique'})
    return problems


def claim_record_hash(claim, evidence):
    """Bind the proposition/context AND selected evidence metadata, not just raw files."""
    record = {k: v for k, v in claim.items() if k != 'assessment'}
    record['selected_evidence_records'] = [evidence.get(eid, {'missing': eid}) for eid in claim['evidence_ids']]
    return sha256(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())


def reviewed_claim_hash(claim, evidence):
    """External review binds the assessed record as well as its proposition/evidence."""
    payload = {'record': claim_record_hash(claim, evidence), 'assessment': claim['assessment']}
    return sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())


def inspect_project(project, root):
    """Only consistency, byte bindings and recorded release prerequisites are checked.

    Human judgements remain human assertions, even with perfectly matching hashes.
    No global pass flag called correct/true/certified is ever emitted.
    """
    errors = validate(project)
    if errors:
        return {'schema_valid': False, 'issues': errors, 'scientific_truth': 'not_computed'}
    artifacts = {a['id']: a for a in project['artifacts']}
    claims = {c['id']: c for c in project['claims']}
    evidence = {e['id']: e for e in project['evidence']}
    issues, raw, drift = [], {}, []
    for aid, artifact in artifacts.items():
        try:
            raw[aid] = confined(root, artifact['path']).read_bytes()
            if sha256(raw[aid]) != artifact['sha256']:
                drift.append(aid)
                issues.append({'id': aid, 'reason': 'artifact_hash_drift'})
        except (ValueError, OSError) as exc:
            drift.append(aid)
            issues.append({'id': aid, 'reason': 'artifact_unavailable_or_unsafe', 'detail': str(exc)})
    for group in ('claims', 'evidence'):
        for obj in project[group]:
            aid = obj['artifact_id']
            if aid not in artifacts:
                issues.append({'id': obj['id'], 'reason': 'unknown_artifact'})
                continue
            if aid not in raw:
                continue
            try:
                span = read_span(raw[aid], *obj['lines_1based_halfopen'])
                if span != obj['text']:
                    issues.append({'id': obj['id'], 'reason': 'exact_span_mismatch'})
            except (ValueError, UnicodeError) as exc:
                issues.append({'id': obj['id'], 'reason': 'invalid_span', 'detail': str(exc)})
    if project['coverage']['registered_claims'] != len(claims):
        issues.append({'id': project['project_id'], 'reason': 'registered_claim_count_mismatch'})
    for item in project['evidence']:
        if item['artifact_id'] in artifacts and artifacts[item['artifact_id']]['access_depth'] == 'metadata':
            issues.append({'id': item['id'], 'reason': 'metadata_not_evidence_for_full_claim'})
    dependencies = []
    for obj in project['claims'] + project['evidence']:
        dependencies.append((obj['artifact_id'], obj['id']))
    for claim in claims.values():
        for eid in claim['evidence_ids']:
            if eid not in evidence:
                issues.append({'id': claim['id'], 'reason': 'unknown_evidence', 'evidence_id': eid})
            dependencies.append((eid, claim['id']))
        a = claim['assessment']
        if a['state'] in ('supported', 'refuted', 'mixed'):
            if a['record_sha256'] != claim_record_hash(claim, evidence):
                issues.append({'id': claim['id'], 'reason': 'assessment_record_binding_mismatch'})
            if not claim['evidence_ids']:
                issues.append({'id': claim['id'], 'reason': 'resolved_state_without_evidence'})
            # Invalidation applies to recorded judgements, not merely source visibility.
            expected = {claim['artifact_id']}
            expected |= {evidence[eid]['artifact_id'] for eid in claim['evidence_ids'] if eid in evidence}
            if set(a['bound_hashes']) != expected:
                issues.append({'id': claim['id'], 'reason': 'assessment_binding_set_incomplete'})
            for aid in expected:
                if aid not in artifacts or a['bound_hashes'].get(aid) != artifacts[aid]['sha256']:
                    issues.append({'id': claim['id'], 'reason': 'assessment_hash_binding_mismatch', 'artifact_id': aid})
            if not a['reviewer'] or not a['rationale']:
                issues.append({'id': claim['id'], 'reason': 'judgement_without_accountability'})
        # Declared minimum dimensions, not a universal scalar evidence ladder.
        # This screens internal records only; it cannot validate the human judgements.
        required_dimensions = {
            'reported': ('source_support', 'extraction'),
            'descriptive': ('measurement', 'extraction'),
            'statistical': ('measurement', 'extraction', 'statistical_inference'),
            'causal': ('measurement', 'extraction', 'statistical_inference', 'causal_identification'),
            'transport': ('transportability',),
            'decision': ('net_benefit',),
        }
        if a['state'] == 'supported':
            for needed in required_dimensions.get(claim['kind'], ()):
                if a['dimensions'].get(needed, 'unknown') != 'supported':
                    issues.append({'id': claim['id'], 'reason': 'required_dimension_not_supported', 'dimension': needed})
    impacted = impact(dependencies, drift + [x['id'] for x in issues if x.get('id') in claims or x.get('id') in evidence])
    for rid in project['reviews']:
        for cid in rid['claim_ids']:
            if cid not in claims:
                issues.append({'id': rid['id'], 'reason': 'review_unknown_claim', 'claim_id': cid})
    external = set()
    authors = set(project['authors'])
    for review in project['reviews']:
        # Independence is declared, not externally authenticated by this program.
        if not (review['independence_declared'] and review['reviewer'] not in authors
                and review['receipt'] and review['response_complete']):
            continue
        bound = review['bound_hashes']
        if not bound or any(aid not in artifacts or artifacts[aid]['sha256'] != h or aid in drift for aid, h in bound.items()):
            continue
        for cid in review['claim_ids']:
            if cid not in claims:
                continue
            required = {claims[cid]['artifact_id']}
            required |= {evidence[e]['artifact_id'] for e in claims[cid]['evidence_ids'] if e in evidence}
            if required <= set(bound) and review['claim_record_hashes'].get(cid) == reviewed_claim_hash(claims[cid], evidence):
                external.add(cid)
    critical = {c['id'] for c in claims.values() if c['critical']}
    blockers = []
    if issues:
        blockers.append('integrity_or_contract_issues')
    if not critical:
        blockers.append('critical_claim_scope_empty')
    if not project['coverage']['human_inventory_complete']:
        blockers.append('claim_inventory_not_declared_complete')
    unresolved = [c['id'] for c in claims.values() if c['critical'] and
                  (c['assessment']['state'] != 'supported' or c['id'] in impacted)]
    if unresolved:
        blockers.append('critical_claims_unresolved_or_stale')
    review_missing = sorted(critical - external)
    if review_missing:
        blockers.append('independent_review_record_missing_or_stale')
    if any(d['blocks_formal_release'] and d['status'] != 'closed' for d in project['debts']):
        blockers.append('blocking_debts_open')
    return {'schema_valid': True, 'issues': issues, 'artifact_drift': sorted(drift),
            'stale_nodes': impacted, 'critical_unresolved': sorted(unresolved),
            'independent_review_missing_for': review_missing,
            'formal_release_record_check': 'blocked' if blockers else 'recorded_prerequisites_present_not_certification',
            'blockers': blockers, 'source_families': sorted({a['family'] for a in artifacts.values() if a['role'] == 'source'}),
            'coverage': project['coverage'], 'scientific_truth': 'not_computed',
            'warning': 'Human support and independence declarations are not machine-verified scientific truth.'}


def impact(dependencies, changed):
    """Upstream artifact -> evidence -> claim -> synthesis; transitive even in cycles."""
    graph = {}
    for source, target in dependencies:
        graph.setdefault(source, set()).add(target)
    seen = set(changed)
    queue = deque(sorted(seen))
    while queue:
        for target in sorted(graph.get(queue.popleft(), ())):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return sorted(seen)


def document_diff(baseline, candidate):
    a, b = baseline.splitlines(keepends=True), candidate.splitlines(keepends=True)
    hunks = []
    for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != 'equal':
            hunks.append({'operation': tag, 'before_lines_1based_halfopen': [i+1, j+1],
                          'after_lines_1based_halfopen': [k+1, l+1], 'old': ''.join(a[i:j]),
                          'new': ''.join(b[k:l]), 'state': 'unknown_requires_review'})
    return {'state': 'changed_requires_review' if hunks else 'unchanged_not_truth_certified',
            'hunks': hunks, 'scientific_truth': 'not_computed'}


def freeze(root, paths, destination, reason):
    """Create a NEW byte manifest; never overwrite an existing trust baseline."""
    if not reason.strip() or not paths:
        raise ValueError('explicit_reason_and_nonempty_paths_required')
    target = confined(root, destination)
    entries = {name: sha256(confined(root, name).read_bytes()) for name in sorted(set(paths))}
    if destination in entries:
        raise ValueError('self_manifest_forbidden')
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('x', encoding='utf-8') as stream:
        json.dump({'reason': reason, 'meaning': 'bytes_only_not_review_approval', 'hashes': entries}, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    return entries

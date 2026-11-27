#!/usr/bin/env python3
"""Development-only, fully disclosed fixture comparison, not independent evaluation.

Only one known synthetic project/claim. The reviewer-created oracle is an
illustrative convention; this test cannot estimate real-world performance.
Never write to the checked-in fixture: all mutations happen in temporary copies.
"""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from research_assurance.core import confined, read_span, sha256, claim_record_hash, inspect_project

spec=importlib.util.spec_from_file_location('assurance_metrics',ROOT/'knowledge_base/experiments/assurance_benchmark_metrics.py')
metrics=importlib.util.module_from_spec(spec);spec.loader.exec_module(metrics)

CASES=(
 ('unchanged','control','valid'),
 ('irrelevant_append','locality','valid'),
 ('source_number_changed','source','stale'),
 ('source_rewritten_and_rebound','source','stale'),
 ('claim_context_changed','context','stale'),
 ('required_dimension_unknown','dimensions','stale'),
 ('missing_source','availability','stale'),
)


def _artifact(project, aid): return next(a for a in project['artifacts'] if a['id']==aid)


def _read_a(root, project, aid):
    return confined(root,_artifact(project,aid)['path']).read_bytes()


def apply_case(root,project,case):
    if case not in {entry[0] for entry in CASES}:
        raise ValueError('unknown fixture case')
    source=confined(root,_artifact(project,'A-source')['path'])
    claim=project['claims'][0]; ev=project['evidence'][0]
    if case=='unchanged': pass
    elif case=='irrelevant_append':
        source.write_bytes(source.read_bytes()+b'Unrelated synthetic appendix.\n')
    elif case in ('source_number_changed','source_rewritten_and_rebound'):
        text=source.read_text()
        if '3 of 10' not in text:
            raise ValueError('fixture source no longer contains the expected baseline text')
        source.write_text(text.replace('3 of 10','7 of 10'))
        if case=='source_rewritten_and_rebound':
            _artifact(project,'A-source')['sha256']=sha256(source.read_bytes())
            ev['text']=ev['text'].replace('3 of 10','7 of 10')
            # Assessment and manuscript remain unchanged; deliberately no trust refresh.
    elif case=='claim_context_changed': claim['context']['unit']='synthetic organoid instead of founder'
    elif case=='required_dimension_unknown': claim['assessment']['dimensions']['source_support']='unknown'
    elif case=='missing_source':source.unlink()
    else: raise ValueError('unknown fixture case')


def detect(project,baseline,root,mode):
    """Outputs stale/valid/abstain; E invokes production inspector, NOT release gate."""
    ids=('A-source','A-book')
    try:
        if mode=='A':
            return 'valid' if all(confined(root,_artifact(project,aid)['path']).is_file() for aid in ids) else 'stale'
        if mode=='B':
            return 'valid' if all(sha256(_read_a(root,project,aid))==_artifact(baseline,aid)['sha256'] for aid in ids) else 'stale'
        if mode in ('C','D'):
            # Frozen referenced span and frozen location; moving text is conservatively stale.
            for obj in baseline['evidence']+baseline['claims']:
                actual=read_span(_read_a(root,project,obj['artifact_id']),*obj['lines_1based_halfopen'])
                if actual!=obj['text']:return 'stale'
            if mode=='D':
                current=project['claims'][0]; old=baseline['claims'][0]
                current_ev={e['id']:e for e in project['evidence']}
                old_ev={e['id']:e for e in baseline['evidence']}
                if claim_record_hash(current,current_ev)!=claim_record_hash(old,old_ev):return 'stale'
            return 'valid'
        if mode=='E':
            r=inspect_project(project,root)
            if not r['schema_valid']:return 'abstain'
            # One-claim fixture: issue list denotes actual consistency contract issues;
            # open review/debt is constant and deliberately not scored as new staleness.
            return 'stale' if r['issues'] or 'C1' in r['stale_nodes'] else 'valid'
        raise ValueError('unknown mode')
    except (OSError,UnicodeError,ValueError,KeyError,StopIteration):
        return 'abstain'


def run():
    original=ROOT/'examples/toy';baseline=json.loads((original/'project.json').read_text())
    output={m:[] for m in 'ABCDE'}
    for case,family,oracle in CASES:
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'toy';shutil.copytree(original,root)
            project=copy.deepcopy(baseline);apply_case(root,project,case)
            for mode in output:
                output[mode].append({'id':case,'family':family,'oracle':oracle,
                                     'decision':detect(project,baseline,root,mode)})
    return {'scope':'same 7 developer-known synthetic cases; not an independent or production performance evaluation',
            'cases':output,'scores':{m:metrics.score(rows) for m,rows in output.items()}}


if __name__=='__main__': print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))

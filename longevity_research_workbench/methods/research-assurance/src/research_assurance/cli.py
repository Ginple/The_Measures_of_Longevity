import argparse
import json
from pathlib import Path
from .core import inspect_project, document_diff
from .corpus import extract_units, apophatic_scan
from .topology import analyze, sensitivity
from .measurement import nominal_relabelling_audit, founder_bounds, weighted_fraction


def main():
    parser = argparse.ArgumentParser(description='Research assurance records, NOT automatic truth evaluation')
    commands = parser.add_subparsers(dest='command', required=True)
    a = commands.add_parser('check'); a.add_argument('project')
    a = commands.add_parser('diff'); a.add_argument('before'); a.add_argument('after')
    a = commands.add_parser('topology'); a.add_argument('document'); a.add_argument('ontology')
    commands.add_parser('diagnostics')
    args = parser.parse_args()
    if args.command == 'check':
        p = Path(args.project)
        out = inspect_project(json.loads(p.read_text()), p.parent)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        # A valid provisional pack can have blockers; CI checks plumbing, not scientific approval.
        return 0 if out.get('schema_valid') and not out['issues'] else 2
    if args.command == 'diff':
        # Bytes decode without universal-newline normalization.
        out = document_diff(Path(args.before).read_bytes().decode('utf-8'), Path(args.after).read_bytes().decode('utf-8'))
    elif args.command == 'topology':
        onto = json.loads(Path(args.ontology).read_text())
        units = extract_units(Path(args.document).read_bytes().decode('utf-8'), onto)
        out = {'adapter': 'markdown_blocks/0.1', 'units': units,
               'all': analyze(units, onto), 'prose_only': analyze(units, onto, prose_only=True),
               'sensitivity': sensitivity(units, onto), 'apophatic': apophatic_scan(units, onto)}
    else:
        out = {'all_constructed_not_empirical': True,
               'relabelling': nominal_relabelling_audit([[7,7,7],[10,10,10],[11,11,11]]),
               'founder_bounds': founder_bounds([{'founder_id': str(i), 'state': s} for i, s in enumerate(['target_observed']*3+['non_target_observed']*2+['death_confirmed']*1+['lost_unknown']*4)]),
               'weighting': {'fractions': [.1,.9], 'equal_weight': weighted_fraction([.1,.9],[1,1]),
                             'unequal_weight': weighted_fraction([.1,.9],[9,1]),
                             'meaning': 'An unchanged per-cell distribution can yield different copy/capture-weighted aggregates.'}}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

"""One real historical claim migration; read frozen v6, mutate temporary copies ONLY.

Requires sibling /home/user/corpus_engine_v6 (or pass its path). No source pipeline
is executed. Third-party full source is NOT redistributed with this toolkit.
"""
from pathlib import Path
import json
import tempfile
import shutil
import sys
from research_assurance.core import sha256, inspect_project

P = Path(__file__).resolve().parents[1]


def main():
    old = Path(sys.argv[1]) if len(sys.argv) > 1 else P.parent/'corpus_engine_v6'
    source = old/'evidence/HipSci_code/WeiWei060512-HipSci_mtDNA_paper-19b42e5/scripts/variantFilter.py'
    doc = old/'优先欠债_第6轮_原代码与可识别性审计.md'
    if not source.exists() or not doc.exists():
        print(json.dumps({'status':'not_run_missing_history','scientific_truth':'not_computed'}))
        return 3
    src, book = source.read_bytes(), doc.read_bytes()
    slines, blines = src.decode().splitlines(keepends=True), book.decode().splitlines(keepends=True)
    si = next(i for i, line in enumerate(slines) if 'df6 = df5[' in line)
    di = next(i for i, line in enumerate(blines) if '|`variantFilter.py / filter_DP_HF`|' in line)
    base = json.loads((P/'examples/toy/project.json').read_text())
    base['project_id'] = 'real-v6-single-claim-binding-pilot'
    base['authors'] = ['same-session-assistant-not-independent']
    base['artifacts'][0].update(path='source.py',sha256=sha256(src),family='10.1038/s41467-021-25482-x',access_depth='code',version='19b42e513e6dd5a0e96aa6229bd5587984092e74',url='https://zenodo.org/records/5136677')
    base['artifacts'][1].update(path='report.md',sha256=sha256(book),family='historical-session-v6',version='frozen-v6')
    base['evidence'][0].update(lines_1based_halfopen=[si+1,si+3],text=''.join(slines[si:si+2]))
    claim = base['claims'][0]
    claim.update(lines_1based_halfopen=[di+1,di+2],text=blines[di])
    claim['context'].update(population='archived function, not published participant data',time='static archived code',estimand='reported implementation observation only',unit='source function',design='source reading with historical isolated harness',domain='specified public archive')
    claim['assessment'].update(state='unknown',reviewer='',rationale='This pilot checks version/locator plumbing; historical scientific judgement is not promoted into a new independent review.',bound_hashes={},record_sha256='')
    claim['assessment']['dimensions'] = {k:'unknown' for k in claim['assessment']['dimensions']}
    base['coverage'].update(scope='One existing v6 table-row claim; not all text or all code.',candidate_units=1,registered_claims=1,human_inventory_complete=False,note='Temporary mutation tests; real source bytes, not real scientific reanalysis.')
    base['debts'][0]['id'] = 'D-pilot-independent-review'
    runs = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root/'source.py').write_bytes(src); (root/'report.md').write_bytes(book)
        r = inspect_project(base, root)
        runs.append({'case':'original_real_bytes','integrity_issues':r['issues'],'formal_release':r['formal_release_record_check']})
        (root/'report.md').write_bytes(book+b'\nAll published results are now proven wrong.\n')
        r = inspect_project(base, root)
        runs.append({'case':'new_claim_outside_selected_span','detected':'A-book' in r['artifact_drift'] and 'C1' in r['stale_nodes']})
        (root/'report.md').write_bytes(book)
        (root/'source.py').write_bytes(src.replace(b'return df5',b'return df6',1))
        r = inspect_project(base, root)
        runs.append({'case':'source_return_mutation','detected':'A-source' in r['artifact_drift'] and 'C1' in r['stale_nodes']})
    out = {'status':'executed','source_original_sha256':sha256(src),'manuscript_original_sha256':sha256(book),
           'source_original_path':str(source),'source_member_lines_1based_halfopen':[si+1,si+3],
           'source_excerpt':' '.join(''.join(slines[si:si+2]).split()),'report_lines_1based_halfopen':[di+1,di+2],
           'runs':runs,'all_expected_observations':not runs[0]['integrity_issues'] and all(x['detected'] for x in runs[1:]),
           'new_empirical_scientific_findings':False,'debt_change':'D01 plumbing generalized on one real historical claim only; D08/D09/D10 remain unresolved.',
           'scientific_truth':'not_computed','independent_review':'not_performed'}
    (P/'results/REAL_BINDING_PILOT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
    assert out['all_expected_observations']
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

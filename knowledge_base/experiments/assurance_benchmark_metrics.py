#!/usr/bin/env python3
"""Metrics for reviewed binary oracle labels and tri-state detector decisions.

No detector results are provided here. These are evaluation mechanics, not an
independent benchmark or proof of tool performance.
"""
from collections import defaultdict

ORACLES={'stale','valid'}
DECISIONS={'stale','valid','abstain'}


def score(rows):
    counts=defaultdict(int); families=defaultdict(lambda: defaultdict(int));seen=set()
    for row in rows:
        if set(row) != {'id','family','oracle','decision'}:
            raise ValueError('each row needs exactly id, family, oracle, decision')
        if not isinstance(row['id'],str) or not row['id'].strip() or row['id'] in seen:
            raise ValueError('case ids must be nonempty and unique')
        if not isinstance(row['family'],str) or not row['family'].strip():
            raise ValueError('family must be nonempty')
        if row['oracle'] not in ORACLES or row['decision'] not in DECISIONS:
            raise ValueError('unknown oracle or decision; resolve oracle disagreement before scoring')
        seen.add(row['id'])
        if row['decision']=='abstain': label='abstain_'+row['oracle']
        elif row['decision']=='stale': label='TP' if row['oracle']=='stale' else 'FP'
        else: label='FN' if row['oracle']=='stale' else 'TN'
        counts[label]+=1;families[row['family']][label]+=1
    def summarize(d):
        tp,fp,fn,tn=(d[k] for k in ('TP','FP','FN','TN'))
        us,uv=d['abstain_stale'],d['abstain_valid']
        def ratio(num,den):return num/den if den else None
        return {'TP':tp,'FP':fp,'FN':fn,'TN':tn,'abstain_stale':us,'abstain_valid':uv,
                'total':tp+fp+fn+tn+us+uv,
                'precision_among_flags':ratio(tp,tp+fp),
                'recall_among_decided_stale':ratio(tp,tp+fn),
                'recall_all_stale_treating_abstain_as_not_detected':ratio(tp,tp+fn+us),
                'abstention_rate':ratio(us+uv,tp+fp+fn+tn+us+uv)}
    return {'overall':summarize(counts),'by_family':{k:summarize(v) for k,v in sorted(families.items())}}


if __name__=='__main__':
    import json
    example=[{'id':'synthetic-1','family':'example','oracle':'stale','decision':'abstain'},
             {'id':'synthetic-2','family':'example','oracle':'valid','decision':'valid'}]
    print('Fabricated example; not measured detector performance:')
    print(json.dumps(score(example),indent=2))

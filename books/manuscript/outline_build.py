"""Build the DEC-011 chapter map from a human assignment table plus source-bound corpus headings.

Human judgement lives only in CHAPTERS and ASSIGN. Titles, line numbers and file hashes are
extracted from the frozen corpus at build time and re-checked by tests, so a hand-typed constant
cannot silently drift from the source (08_LINEAGE §3, failure 2). The mapping is a chapter-title
classification, not a paragraph-level content audit.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    'V6': 'corpus/longevity_v6/长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md',
    'V7': 'corpus/longevity_v7/长寿研究_V7_谁在变年轻.md',
}
HEADING = re.compile(r'^## (\d\d)｜(.+?)\s*$')

VOLUMES = [('Ⅰ', '尺度'), ('Ⅱ', '身体'), ('Ⅲ', '生活')]
PARTS = [  # (part number, volume, title, first chapter, last chapter)
    (1, 'Ⅰ', '问题', 1, 4), (2, 'Ⅰ', '四个尺度', 5, 9),
    (3, 'Ⅱ', '维护身体', 10, 13), (4, 'Ⅱ', '辨认年轻', 14, 17), (5, 'Ⅱ', '干预与代价', 18, 22),
    (6, 'Ⅲ', '生活的条件', 23, 27), (7, 'Ⅲ', '判断与行动', 28, 30), (8, 'Ⅲ', '可修订的知识', 31, 33),
]
# chapter -> (title, evidence class, paper tags, demo draft file stem or '')
# Evidence: S = mostly published/measured, M = mixed, H = hypothesis-led (synthetic or contract only).
CHAPTERS = {
    1: ('长寿到底在衡量什么', 'M', '', 'CH01'),
    2: ('年龄不是唯一的时钟', 'S', '', ''),
    3: ('解释、预测、控制与获益', 'M', '', ''),
    4: ('什么算证据：分母、来源家族与复制', 'S', 'P3', ''),
    5: ('测量合同：预测、响应、机制、替代', 'M', 'PI', 'CH15'),
    6: ('水平：一次读数说明什么', 'S', 'PI', ''),
    7: ('速率：斜率不是状态', 'S', 'PI', ''),
    8: ('恢复：扰动之后才看得见的能力', 'M', 'PI', ''),
    9: ('余量：离阈值还有多远', 'M', 'PI', ''),
    10: ('维护、修复、替换与补偿', 'M', '', ''),
    11: ('损伤与修复的代价', 'M', '', ''),
    12: ('器官、界面与环境', 'M', '', ''),
    13: ('身体内部的竞争', 'M', '', ''),
    14: ('身份：谁在变年轻', 'M', 'PI', ''),
    15: ('样本年轻与实体年轻：状态周转', 'M', 'PI', 'CH23'),
    16: ('汇总指标的权重', 'M', 'PI', ''),
    17: ('历史与记忆：修好这一次还剩多少下一次', 'H', 'P5', 'CH24'),
    18: ('标志物与结局分道扬镳', 'S', 'PI', ''),
    19: ('重编程与衰老细胞：清除之后谁来接班', 'M', '', 'CH22'),
    20: ('营养、运动、预防与医疗的证据分层', 'S', '', ''),
    21: ('容量核算 I：谁替谁维护、何时到位', 'H', 'P4', 'CH19+CH20'),
    22: ('容量核算 II：有余量却用不上', 'H', 'P4', 'CH21'),
    23: ('居住、环境与基础设施', 'S', '', ''),
    24: ('照护、依赖与自主', 'M', '', ''),
    25: ('身体体验与技术监控', 'M', '', ''),
    26: ('艺术、关系与意义', 'M', '', ''),
    27: ('不平等与分配', 'M', '', ''),
    28: ('不同人的不同权衡', 'M', '', ''),
    29: ('临床与个人决策', 'S', '', ''),
    30: ('双账本与 LIFE OS 最小安全架构', 'M', '', ''),
    31: ('如何读相互冲突的研究', 'S', 'P3', ''),
    32: ('未知与异常日志', 'M', '', ''),
    33: ('可撤回的知识', 'M', '', ''),
}
# Human classification of every numbered source chapter to exactly one primary target chapter.
# 2026-11-27 §7.2 ch5 pilot: V7-06 moved 6 -> 5. Its body states the four properties in ch5's title
# (prediction, mechanism specificity, responsiveness, surrogate status) plus usage rules; see
# knowledge_base/pilots/ch05_measurement_contract/README.md.
ASSIGN = {
    'V6': {1: 1, 2: 3, 3: 3, 4: 2, 5: 12, 6: 10, 7: 10, 8: 11, 9: 19, 10: 12, 11: 19, 12: 18,
           13: 20, 14: 20, 15: 5, 16: 8, 17: 29, 18: 29, 19: 23, 20: 23, 21: 27, 22: 25, 23: 26,
           24: 26, 25: 24, 26: 30, 27: 28, 28: 32, 29: 30, 30: 25, 31: 28, 32: 29, 33: 33},
    'V7': {1: 4, 2: 3, 3: 16, 4: 16, 5: 15, 6: 5, 7: 13, 8: 18, 9: 13, 10: 19, 11: 12, 12: 11,
           13: 11, 14: 12, 15: 12, 16: 17, 17: 8, 18: 17, 19: 14, 20: 20, 21: 2, 22: 16, 23: 14,
           24: 16, 25: 11, 26: 20, 27: 17, 28: 13, 29: 32, 30: 32, 31: 31, 32: 29, 33: 26, 34: 21,
           35: 22, 36: 19, 37: 15, 38: 17, 39: 31},
}
BUDGET = {'Ⅰ': 90_000, 'Ⅱ': 135_000, 'Ⅲ': 105_000, 'frame': 20_000}  # characters, planning only


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def extract_headings(path):
    out = {}
    for i, line in enumerate((ROOT / path).read_text(encoding='utf-8').splitlines(), 1):
        m = HEADING.match(line)
        if m:
            n = int(m.group(1))
            if n in out:
                raise ValueError(f'duplicate numbered heading {n} in {path}')
            out[n] = (i, m.group(2))
    return out


def build():
    inherited, sources = {}, {}
    for key, path in SOURCES.items():
        heads = extract_headings(path)
        if set(heads) != set(ASSIGN[key]):
            raise ValueError(f'{key}: assignment keys {sorted(set(ASSIGN[key]) ^ set(heads))} differ from source')
        sources[key] = {'path': path, 'sha256': sha256(path), 'numbered_chapters': len(heads)}
        for n, (line, title) in sorted(heads.items()):
            inherited[f'{key}-{n:02d}'] = {'line': line, 'title': title, 'to': ASSIGN[key][n]}
    chapters = []
    for part, vol, ptitle, first, last in PARTS:
        for c in range(first, last + 1):
            title, ev, papers, demo = CHAPTERS[c]
            chapters.append({'n': c, 'volume': vol, 'part': part, 'part_title': ptitle, 'title': title,
                             'evidence': ev, 'papers': papers, 'demo_draft': demo,
                             'inherits': sorted(k for k, v in inherited.items() if v['to'] == c)})
    return {'decision': 'DEC-011', 'status': 'working_draft_not_reviewed',
            'mapping_scope': 'chapter-title classification only; not a paragraph-level content audit',
            'volumes': [{'id': v, 'title': t} for v, t in VOLUMES], 'budget_chars': BUDGET,
            'sources': sources, 'chapters': chapters, 'inherited': inherited}


def render_md(data):
    vt = dict((v['id'], v['title']) for v in data['volumes'])
    L = ['# 《长寿的尺度》章节地图 v1（DEC-011）', '',
         '> **由 `outline_build.py` 生成，请勿手改。** 状态：工作草稿，未经独立审阅（D05 open）。'
         '继承列只按编号章**标题**归类（每章取一个主要落点），不是逐段内容核对；源文件 hash 见 `outline_v1.json`，'
         '由 `tests/test_outline_source_binding.py` 复核。决定理由见 [架构决定](../ARCHITECTURE_DECISION_2026-11-27.md)。', '',
         '证据类别：S＝以已发表/实测为主；M＝混合；H＝以假说、合成模型或实验合同为主。', '']
    cur_v = cur_p = None
    for c in data['chapters']:
        if c['volume'] != cur_v:
            cur_v = c['volume']
            L += [f"## 卷{cur_v} · {vt[cur_v]}（预算约 {data['budget_chars'][cur_v] // 1000}k 字）", '']
        if c['part'] != cur_p:
            cur_p = c['part']
            L += [f"### 第{cur_p}部 · {c['part_title']}", '',
                  '| 章 | 标题 | 证据 | 论文 | 示范稿 | 继承（V6/V7 编号章） |', '|---|---|---|---|---|---|']
        inh = '、'.join(f"{k}《{data['inherited'][k]['title']}》" for k in c['inherits']) or '—（新写）'
        L.append(f"| {c['n']} | {c['title']} | {c['evidence']} | {c['papers'] or '—'} | {c['demo_draft'] or '—'} | {inh} |")
        if c['n'] in (4, 9, 13, 17, 22, 27, 30, 33):
            L.append('')
    n3 = sum(1 for c in data['chapters'] if c['volume'] == 'Ⅲ')
    new = [str(c['n']) for c in data['chapters'] if not c['inherits']]
    L += ['## 结构检查（生成时计算）', '',
          f"- 章数 {len(data['chapters'])}；卷三 {n3} 章（{n3 / len(data['chapters']):.0%}）。卷三章数或实际字数低于 28% 时，停止扩写卷二，先补卷三。",
          f"- 没有继承编号章、需要新写的章：{'、'.join(new)}。",
          '- 非编号内容（V6 导论/终章/出处说明/S6.1–S6.6，V7 导读/结语/附录 A–C/第十部引言）未纳入本表，须另行核对，不得自动合并。',
          f"- V6 {data['sources']['V6']['numbered_chapters']} 章、V7 {data['sources']['V7']['numbered_chapters']} 章各有且只有一个主要落点。", '']
    return '\n'.join(L)


def main(write=True):
    data = build()
    js = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    md = render_md(data)
    if write:
        (ROOT / 'books/manuscript/outline_v1.json').write_text(js, encoding='utf-8')
        (ROOT / 'books/manuscript/OUTLINE_v1.md').write_text(md, encoding='utf-8')
    return js, md


if __name__ == '__main__':
    main(write='--check' not in sys.argv)

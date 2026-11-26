"""Combine first-party method docs for convenient reading; no evidence baselines modified."""
from pathlib import Path
import re
P=Path(__file__).resolve().parents[1]
names=['01_POSITIONING.md','02_METHODOLOGY.md','03_WORKFLOW.md','04_DATA_CONTRACTS.md','05_CORPUS_ENGINE.md','06_VALIDATION.md','07_ADAPTATION.md','08_LINEAGE.md','09_LIMITATIONS.md','10_SKILL_DISTILLATION.md','GLOSSARY.md','INTEGRATION.md']
intro='''# 证据约束型研究工程：通用方法与技能手册
# Evidence-Bound Research Engineering · Method & Skill Handbook

**0.1.0｜可运行工程草案，不是独立审定的科学方法标准。**

这是本Session corpus_engine V1–V6积累的通用提炼，不是作品V6/V7重写。建议总称为“研究工程框架与工具包 / Research Engineering Framework & Toolkit”；corpus_engine保留为跨阶段的语料结构与证据审计子系统。

本文是docs中方法文件的合订阅读版，机器实现、Skill、模板和实际回执在配套仓库目录中。关键词保留中英文；本轮及后续不再交付STATE_DASHBOARD.HTML。

## 阅读地图 / Reading Map

'''
for i,name in enumerate(names,1):
 title=(P/'docs'/name).read_text().splitlines()[0].lstrip('# ')
 intro+=f'{i}. [{title}](docs/{name})\n'
parts=[intro]
for name in names:
 text=(P/'docs'/name).read_text()
 # Demote headings outside fenced blocks; do not corrupt code comments.
 in_fence=False;lines=[]
 for line in text.splitlines():
  if line.startswith('```'):in_fence=not in_fence
  if not in_fence and line.startswith('#'):line='#'+line
  lines.append(line)
 parts.append('\n---\n\n'+'\n'.join(lines)+'\n')
(P/'METHOD_HANDBOOK_ZH_EN.md').write_text('\n'.join(parts))
print('handbook bytes',(P/'METHOD_HANDBOOK_ZH_EN.md').stat().st_size)

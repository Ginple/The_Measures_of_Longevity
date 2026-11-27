# 分选后比例能否还原总体？条件敏感性示例

2026-11-27｜择取 [PR #2 固定头的说明](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/knowledge_base/SORTED_SAMPLE_SENSITIVITY_2026-11-27.md)、[脚本](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/knowledge_base/experiments/sorted_sample_sensitivity.py)和[测试](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/tests/test_sorted_sample_sensitivity.py)；移入本分支[脚本](sorted_sample_sensitivity.py)和[测试](test_sorted_sample_sensitivity.py)，额外检验正纳入概率网格、q边界及无效输入。同助手定向核读，不是独立外审、论文重算或临床建议。

## 真实研究说了什么

[2025在线发表的uPAR小鼠肠道研究](https://www.nature.com/articles/s43587-025-01022-w) Results报告，老龄小鼠分选后分析9,430个uPAR+及7,379个uPAR−细胞；用SenMayo计算识别的细胞中，约60%属于表面uPAR+。分母是**该分选测序样本中的计算标签阳性**，不是所有uPAR+细胞，也不是组织中真正“应被清除”的细胞。[Fig 1h–k图注](https://www.nature.com/articles/s43587-025-01022-w/figures/1)写每组4鼠合并为两个重复，细胞不是独立动物。作者还有流式、组织学和功能实验，不能靠此一比例否定全篇；动物干预未随机、未盲等限制见[已存证据审计](../SELECTIVITY_EVIDENCE_AUDIT_2026-11-27.md)。

[正类雄鼠GEO条目](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7913144)与[负类雄鼠条目](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7913146)都描述先分选、每样本调整以目标捕获8,000个细胞。目标捕获数不是实际回收率，也不证明真实正负类相对纳入概率大于或小于1。[GSE233431](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE233431)还列其他条件样本，不能将整个系列看作只有四个分选样本。本次只核上述网页及图注，未下载矩阵、未重跑R或核60%的原始计数、池内动物映射与门控计数。GEO和固定脚本的QC口径仍有待澄清（X71），不因此判定发表结果错误。

## 简单模型与精确算术

在**人为指定的总体**中，假设每个单元都有固定可比的二元标签 `S` 和 `U`，并令 `R` 表示最终被纳入；只看 `S+`。设总体 `t=P(U+|S+)`、所选总体 `q=P(U+|S+,R=1)`，两类纳入概率分别 `p+`、`p−` 均严格大于零，且 `r=p+/p−`。则由条件概率

`q = r*t/(r*t + 1-t)`；`t = q/(q + r*(1-q))`。

`q`是选择机制对应的总体概率或无限样本比例，不自动等于有限样本观察值；如果使用样本比例代入，抽样、动物/池和测序误差仍须另行建模。正纳入概率要求重要：一类概率为零时该反演不适用；`S+`也必须在所选及未选总体中有同一、稳定、可定义的含义。实际计算标签来自测序和相依的模块评分，未经验证不能假设同一算法可无误用于未采集细胞；模型把这些难题简化，而不是解决它们。`r` 是在 `S+` 内综合各选择过程后的相对概率，未假定已知来自单一分选步骤。

下表虚构 `q=3/5`，数值与文中约60%相近**仅为方便说明**，不是把作者统计量代入真实校正：

| 假定 `r` | 相容的总体 `t` | 一种实际可行的 `(p+,p−)` |
|---:|---:|---:|
| 1/10 | 15/16 = 93.75% | (1/10, 1) |
| 1 | 3/5 = 60% | (1, 1) |
| 10 | 3/23 ≈ 13.04% | (1, 1/10) |

若**额外假定** `1/2≤r≤2`，`t` 只能在 `[3/7, 3/4]`：反演式随 `r` 单调下降、两端由 `r=2`、`r=1/2` 实现，连续的中间值也可实现。这个锐界只对指定模型与准确的 `q` 成立，不是数据驱动的可信范围或置信区间。对 `0<q<1`，仅给出 `r>0` 时，任一 `0<t<1` 均可通过取 `r=q(1-t)/(t(1-q))` 实现，0、1仅是极限；在正纳入率且准确 `q` 的理想模型下，`q=0` 则 `t=0`、`q=1` 则 `t=1`。这不意味着真实有限样本出现全零/全一就排除了稀有未观测类型。

## 如何更接近可识别

若目标是指定组织中明确细胞及标签的占比，需记录取材区域、细胞类型、所有分选门与分选前后计数、存活/解离/捕获及QC、动物和池映射；用可比的独立表型与代表性取样评估标签及纳入过程，记录不确定性。单细胞测序标签所包含的 `Plaur` 与表面uPAR分选的潜在重叠及未执行脚本问题另见[代码审计](../UPAR_SCORING_CODE_AUDIT_2026-11-27.md)，不能把标签当独立功能真值或据基因重叠量化偏差。对流式样本而言，定义与目标总体不同也不能直接当 `r`。上述选择模型不推断真实偏差大小、方向或CAR T清除净收益。

运行 `python knowledge_base/experiments/sorted_sample_sensitivity.py`；用 `python -m unittest discover -s knowledge_base/experiments -p test_sorted_sample_sensitivity.py` 测试。六项测试覆盖精确反演、假设端点、有限网格、概率边界及无效输入；同开发过程的代数回归不是独立数学证明或患者、动物数据分析。

# PR #2 移植审计逐份复核（2026-11-27）

**性质：** 对 `knowledge_base/imported_pr2/` 中 14 份审计逐份复核，判断其结论是否站得住、是否与本库台账重复。
- 这不是独立外审（D05 仍为 open）。
- 本轮重新核对了 4 处一手来源：
  - LoDoCo2 PMC 作者稿 Results；
  - FIND 骨折报告摘要（Bone 2026）；
  - WHO 证据地图发布说明；
  - CALERIE 补表 S3 的分母，用整数穷举重算。
- 其余数字沿用 PR #2 的转述，台账中已逐条注明。

## 判定总表

| 文件 | 判定 | 去向 |
|---|---|---|
| LODOCO2_AUDIT | 保留。PR2-X40 已对原文逐字核实；PR2-X19 与本库 X19 重复 | 新增 **X102**；X19 不变 |
| CANTOS_TET2_CLINICAL_INTERACTION | 保留"亚组显著 ≠ 交互确立"。hs-CRP 单位问题与本库 X73 重复 | 并入 **X103** |
| COLCOT_LODOCO2_TRIANGULATION | 保留。COLCOT 数字来自预印本，已标注 | **X104** |
| CALERIE_LIPID_MEDIATION_2026 | 保留，降为"作者工作假说"；家族误差的合成例已在 experiments 中 | **X105** |
| CALERIE_TRAJECTORY_MISSINGNESS_FIGSHARE | 保留。本轮独立重算：在 N∈[100,400] 中只有 191 与 10 组百分比都相容 | **X106**（扩展 X60） |
| EPI_CLONE_X33_FOLLOWUP | 保留，只作假说与设计；已标注 MethylTree 和 PCDH 条码等相近工作 | **X107** |
| SORTED_SAMPLE_SENSITIVITY | 保留，属于合成的识别论证 | **X108** |
| HARP_PROTOCOL_REGISTRY_RECHECK | 保留新增的三处口径差异；首次与重复跌倒问题与 X44 重复 | **X109** |
| FIND_CANCER_FALLS_FRACTURES | 保留。骨折 HR 已核摘要；癌症表 2/表 3 问题与 X55 重复 | **X110** |
| AGE_FRIENDLY_EVIDENCE_SCOPE | 保留。WHO 数字已核；Cochrane 部分与 X45/X46 重复 | **X111**（resolved） |
| CALERIE_X31_VERSION_AUDIT | 与本库 X31 重复。交集精确等式只在"并集 = 母集"时成立，已在原文件中写明 | 不新增编号；X31 保持 open |
| CAPABLE_RECHECK | 与 X20/X79/X80 重复；"对照接触 73/148 对 141/152"可作写作素材 | 不新增编号 |
| TPE_ALLOCATIONS_AND_CLOCK_UNITS | 与 X05/X77/X78 重复 | 不新增编号 |
| RESEARCH_BRIDGE | 综合性文件，无独立新断言；其中的 EPI-Clone 假说已并入 X107 | 不新增编号 |

## 编号映射

PR #2 与本库共用部分编号（如 X19、X31、X33、X40），但两边含义不同。本库编号以 `knowledge_base/CLAIM_LEDGER.md` 为准，PR #2 的编号在台账中统一写成 `PR2-Xnn`：

| PR #2 编号 | 去向 |
|---|---|
| PR2-X40 | X102 |
| PR2-X33 | X107 |
| PR2-X19 | 等同本库 X19 |
| PR2-X31 | 等同本库 X31 |

## 横向发现

4 份文件（CANTOS、LoDoCo2、COLCOT、FIND）指向同一类错误：
- 同一试验的多篇论文、多个剂量、多个结局，被当成多次复现；
- "一组显著、另一组不显著"被当成组间差异。

这两点应写入断言卡（THE-235）的写作规则，不需要逐条处理。

## 未做

- 未联系任何作者。
- 未取得个体数据。
- COLCOT 的 *Circulation* 正文与 CANTOS 原文本轮未重读。
- 合成例都只检验算术。

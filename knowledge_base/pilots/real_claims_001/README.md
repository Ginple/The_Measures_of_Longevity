# 真实共享断言试点001 / Real shared-claims pilot 001

**独立增量，2026-11-25，pilot 0.1.0。** 不改主工作台上一轮文件、原稿、工具组件及旧ZIP；不称新V8或完整论文。

## 本轮交付 / Deliverables

- **2个真实段落级记录**：V6身体功能LIFE试验；V7血液mtDNA机制。登记在project.json；11条原文提取来自2项研究，而非11项独立证据。
- 取得两份来源完整网页，**仅定向阅读**相关方法/结果/讨论；full acquisition不等full reading。公开增量包不含第三方全文HTML。
- 明确估计目标/分母/时间/对象，区分“忠实报告作者结论”和“独立证明结论正确”。
- 两份可审阅示范模块与三篇论文的证据角色映射；变化后传播到被声明引用的稿件，不自动重写结论。
- 精确算例：一个汇总比例减半可对应三种不同机制；构造结果不是原研究实测。
- 独立审阅任务包；**尚无真实外审、无新增人类人审**，发布保持blocked。

## 阅读入口 / Start here

1. [综合报告](docs/PILOT_REPORT.md)
2. [两张断言卡](docs/CLAIM_CARDS.md)
3. [功能示范模块](drafts/V6_FUNCTION_MODULE.md) · [可见性示范模块](drafts/V7_VISIBILITY_MODULE.md)
4. [论文证据接口](drafts/PAPER_EVIDENCE_INTERFACES.md)
5. [估计目标与数据合同](docs/ESTIMAND_AND_DATA_CONTRACTS.md)
6. [独立审阅包](review/INDEPENDENT_REVIEW_PACKET.md)

## 安装位置与运行 / Placement and validation

此目录应位于上轮主工作台的：

```text
longevity_research_workbench/
  methods/research-assurance/          # 上轮0.1.1候选，继续使用，不复制第二活跃源码
  knowledge_base/pilots/real_claims_001/  # 本次新增
```

从本目录运行：

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
```

依赖已安装时无需第一条；验证不联网。不要求本会话缓存或旧历史目录。它检查便携提取绑定、稿件映射、变异、算例和移目录复现，**不会声称全文缓存已验证**。

本会话中可追加：

```bash
python scripts/validate.py --source-cache /home/user/longevity_source_cache_001 --history-workspace /home/user
```

这一模式另核原网页hash、可复算的正文规范化、提取字符位置，以及旧历史字节。没有缓存时不能换成新网页并刷新预期hash。网页更新应作为新版本重新接收、比较和审阅。页面外壳变化也可能触发保守失效，不等科学结论被推翻。

## 记录边界 / Boundaries

`reviewer`字段明确为同助手来源对读，不冒充人类或独立审阅者；reviews=[]。supported仅用于reported类型的忠实报告/提取；其他科学维度unknown。没有把所有书稿登记为完整清单。

`provenance/BUILD_INITIAL_RECORDS_DO_NOT_RERUN.py.txt`仅保留最初建记录过程；不是验收命令，含本会话路径，不应运行以重签或覆盖记录。正常验收不更新任何信任基线。

上轮根目录FILE_MANIFEST/目录树仍表示上轮冻结交付；本增量有独立清单。若要发布新的整体版本，需维护者审核后显式更新主索引、版本和整体清单，不能把旧清单冒充当前完整仓库清单。

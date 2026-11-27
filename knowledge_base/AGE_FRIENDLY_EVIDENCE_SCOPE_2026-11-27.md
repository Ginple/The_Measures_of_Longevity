# 年龄友好环境：证据地图与跌倒综述的范围核对

本轮重读 WHO 于 2026-11-10 的 [发布说明](https://www.who.int/news/item/10-11-2026-who-releases-global-mega-map-on-age-friendly-environments)及其[地图页面](https://www.who.int/initiatives/decade-of-healthy-ageing/evidence-gap-map/afe-megamap)，并对照 [Cochrane 2023 综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/)的 Summary of findings 1、说明及 [PR #1 固定版本 X45](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/knowledge_base/CLAIM_LEDGER.md)。**远端先前已记录 Cochrane 引用重叠与表格异常；本轮不是首次发现。**

- WHO 说明所收是 2002–2025 年发表的 **1,542 篇系统综述和 3 张 evidence/gap maps**，不是 1,545 项独立随机试验，也不能把相互重叠的综述中的原始试验相加。WHO 说明只找到两篇针对整个年龄友好城市/社区项目的综述，并称交通、公民参与/就业、尊重和社会包容等证据相对较少；公平和经济结局少见，部分综述报告不完整。该地图是证据分布与空白的导航，不排序最佳干预。本轮读取发布说明及地图静态页面；未逐条导出 1,542 记录、核去重、质量分布或独立复现地图统计。地图页本身声明可访问性限制：某些控件需要鼠标或指针；并非本轮无障碍测试。
- 能力进路已有较长理论史。[Stanford Encyclopedia of Philosophy 2025 修订条目开头](https://plato.stanford.edu/entries/capability-approach/)区分实际做到的 functioning、如果选择即可实现的 capability 和转换条件，并指出 Sen、Nussbaum 等人的贡献。这里的“机会账本”是本项目工作框架，而不是把整套能力进路重新命名或说实测参与频次就是完整的可行选择集。该条目是一篇二级综述；未全读历史原始著作或裁决其内部分歧。
- Cochrane 综述总体含 22 项研究 8,463 人，**居家跌倒危险因素减少**的跌倒发生率合并则是 12 项、5,293 人，RaR 0.74（95% CI 0.61–0.91），GRADE 中等，因异质性（I²=83%）降级；这不是“22 项都证明减少 26%”。高风险预设亚组 RaR 0.62（0.56–0.70；9 项、1,513 人），未按高风险选择者 1.05（0.96–1.16；6 项、3,780 人）；两亚组是试验层分组，试验间差异和可迁移性仍重要。至少一次跌倒的比例是另一结局，总体 RR 0.89（0.82–0.97；12 项 5,253 人），不是首次跌倒 Cox HR。综述收录 Stark 2021/HARP，因此 **HARP 不能与这份综合证据当成彼此独立研究相加或复现**。
- Summary of findings 1 中高风险“至少一次跌倒”显示基线 550/1,000、RR 0.74，但对应干预人数写 461/1,000；简单乘法 550×0.74=407，未在此推断成因，也不改印数字。表中骨折 RR 1.00（0.98–1.02）及其 205/1,000 与主文其他统计是否相符，需逐引用核源；远端 X45 已有多处此类差异。本轮不使用这些异常表项导出绝对效果或 NNT。总体 I² 高、不同干预及纳入 HARP 等均应限制迁移。
- [SEP《残障与福祉》2026](https://plato.stanford.edu/entries/disability-well-being/)开头区分社会障碍与多种关于残障及福祉关系的哲学观点，提醒不可假定残障必然意味着低福祉；是二级理论来源，不代表残障人士立场一致。本轮只查其导论与目录，未系统核各立场原著。第 24 章的关系自主属于明确规范立场，不是该条目认证的唯一答案，也不是对各地法律的论断。

## PR #1 新 head 的补充核对（2026-11-27）

PR1@`dfd23562149b88e82c6c4c9ea0aedaf4e1dc3c61` 的 [跌倒深核](https://github.com/Ginple/The_Measures_of_Longevity/blob/dfd23562149b88e82c6c4c9ea0aedaf4e1dc3c61/knowledge_base/FALLS_STUDIES_DEEP_AUDIT_2026-11-27.md)早已登记 Cochrane 附录与 HARP 分母方向相反；本次重新读[综述附录5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/table/CD013258-tblf-0004/)与[HARP 表2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8408671/table/zoi210656t2/)：前者干预 67/140、对照 74/135；后者 67/135、74/140。机械未调整比约 .873 与 .939，**不知汇总模型实际所用输入，不是荟萃复算**。对照 [高风险总结表](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/table/CD013258-tbl-0001/)的 550/1000、RR .74，乘积 407 与印出的 461 不一致；其原因和实际汇总数据不明，不用这个表格项计算 NNT。

[OTIS 原始结果](https://www.ncbi.nlm.nih.gov/books/NBK571976/)明确 430 分配干预、382 记录访视（其中 381 在 12 个月内）；两组至少一次跌倒比例默认缺失月份无跌倒。本地 `COUNTEREXAMPLES_AND_DENOMINATORS_2026-11-27.md` 之前误把分配数说成接受数，现已改正。随机后 23 人无任何跌倒数据被作为 0 次/0.1 月纳入主要模型，不能称完整观察或据此决定偏差方向；两篇环境试验与包含二者的汇总非三项独立复制。保留 PR1:X46/X47 为远端命名空间，未合并两个台账。

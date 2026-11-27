# uPAR肠道论文：单细胞评分脚本静态审读

2026-11-27｜只读脚本，**未运行R、未下载表达矩阵、未复现图或验证作者全部分析**。这不是计算错误认定，也不是细胞衰老的金标准评估。关联 [X66/X68](SELECTIVITY_EVIDENCE_AUDIT_2026-11-27.md)。

## 版本与范围

2025 [Nature Aging原文](https://www.nature.com/articles/s43587-025-01022-w)列两处代码。GitHub API查询2026-11-27时默认分支的最新提交分别为：

- [Regen_CAR-T @ 37d02fd32d90c9dd14981da8b8e9f7edc6037179](https://github.com/Vyoming/Regen_CAR-T/tree/37d02fd32d90c9dd14981da8b8e9f7edc6037179)，2025-06-30；本次定位阅读其中 `UPAR_Sort_scRNA.R`（并扫读另三个脚本目录/关键字）。
- [Nature-Aging-Intestinal-Senescence @ fdc728ac7ed6665d79384cb72cb1afa35dba25fd](https://github.com/AmorLab/Nature-Aging-Intestinal-Senescence/tree/fdc728ac7ed6665d79384cb72cb1afa35dba25fd)，2025-05-30；定向读 `bulk_rnaseq_code_intestine.R` 前段。版本固定不保证就是论文实际执行版本或其完整环境。

## 评分、条件方向与复现依赖

`UPAR_Sort_scRNA.R` [约32–35行](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L32-L35)读取本地男女×阳性/阴性四个10X矩阵；文章 Fig 1h–k 描述每组4只小鼠合并成两个重复。输入矩阵及池化样本映射未获得。

同脚本[205–220行](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L205-L220)列 SenMayo 相关基因，包含 `Plaur`（uPAR编码基因）；[489–519行](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L489-L519)调用 `AddModuleScore`、以 `sen_mayo1 > .02` 定义 `sen_cells`，再在 `table(Treatment, sen_cells)` 中使用 `margin=2`，即在各 `sen_cells` 列内归一。结构上支持本文将约60%理解为「计算标签阳性中 uPAR 分选阳性的比例」，而不是反向比例。算法是表达模块阈值，不是对该细胞是否应删除的功能真值。

同时，标签的基因表包含分选表面靶点的编码基因 `Plaur`，因此基因表与分选特征存在潜在重叠，可能影响两者一致性解读；表面蛋白分选不等于mRNA表达，单个基因在模块及对照中的实际权重需运行后评估，**不能仅凭基因名单认定此重叠导致观察结果或量化偏差**。应预先记录阈值来源、分数控制基因、版本和随机种子；用预定替代方案（含排除Plaur、改变阈值及分细胞类型）做敏感性分析，并与独立组合表型对照。敏感性分析不是自动纠错或性能认证。

局部静态阅读也发现：脚本引用作者机器的绝对路径、`~/analysis/split_violin.R`，出现 `cart_obj`、`sen_BRD4` 等未见在该脚本先前定义的对象；[242–243行](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L242-L243)对未命名 `list(sen_mayo, Inflammatory_score_new)` 的 `names` 迭代，按通常R语义该循环不执行。可能依赖交互式工作空间、脚本次序或未列辅助文件；没有执行、环境/数据或作者确认，**不据此判断发表图表错误**。仅靠此脚本还不能在干净机器一键重建全部对象。必须取得输入、sessionInfo/依赖版本、外部函数与实际运行顺序后复现。

另在[179–180行](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L179-L180)看到Seurat `FindMarkers` 使用MAST并把性别列为协变量；该局部调用并未显式指定动物/池级随机效应。细胞共源且有池化，需结合图表、预处理和推断目标评估重复单位；未经运行/映射，不能断言具体论文检验的p值计算错误或所有分析均未考虑池化。

另一个仓库的 `bulk_rnaseq_code_intestine.R` 创建4条件各两列的设计 `~condition`；它是另一类bulk分析，不能用来替代单细胞结果、或证明样本处理与脚本一致。条件列顺序假定计数矩阵顺序，需检查矩阵及元数据；未获得输入、未运行DESeq2。

## 进一步对读

[Demaria 2014鼠伤口研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349629/) Fig 6 的特定清除+PDGF-AA补充是已有救援试验，不是本项目新提议。补充改善伤口闭合速度、肌成纤维细胞指标；原文称未明显解决纤维化，补图未复算。两处“替代”不能混为同一设想或套用于uPAR：本项目的清除×保护/替代完整2×2仍未实施，而其他修复替代试验已经存在。

> **PR #2 移植件**（来源：[PR #2 固定头 `b8434e2` 原路径 `review/PR1_INCREMENTAL_AUDIT_52DD494_2026-11-27.md`](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/review/PR1_INCREMENTAL_AUDIT_52DD494_2026-11-27.md)；移植于 2026-11-27，用户批准“选择性移植后关闭 PR #2”）。文中 X 编号、章号、ANOM 等属于 **PR #2 命名空间**（引用时写作 PR2-X32 等），与本分支 `knowledge_base/CLAIM_LEDGER.md` 的同号条目**不同义**。未经本分支逐条复核，不作为正文、KERNEL 或论文的证据；指向未移植文件的相对链接已改为固定提交的 GitHub 永久链接。

# PR #1 增量审计：52dd494

2026-11-27｜审计固定头 `52dd494357963181e4008a0df9b842fa7478c1ec`；相对 `78834bfce863ced1ba3cf31cb682a713f56974d0` 为1个提交、13路径，新增第22章、uPAR定向证据及代码审读、人工概率/中介反例。此为同助手定向审计，不是系统综述、独立外审，也没有运行真实数据分析。

## 新发现：公开 QC 文档与固定脚本参数待厘清（P2，可复现性，不裁定图表错误）

PR 新的 [uPAR 代码审计](https://github.com/Ginple/The_Measures_of_Longevity/blob/52dd494357963181e4008a0df9b842fa7478c1ec/knowledge_base/UPAR_SCORING_CODE_AUDIT_2026-11-27.md)正确提示没有原矩阵、运行环境及实际执行次序，不能认定发表结果错误。本次进一步对读 [GEO 分选阳性雄性 `GSM7913144`](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7913144)、[分选阴性雄性 `GSM7913146`](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7913146)、[作者代码固定版本](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L44-L52)及[论文方法](https://www.nature.com/articles/s43587-025-01022-w)：

- 两个 GEO 条目均写剔除线粒体转录本超过15%、feature counts 少于100 **或表达基因少于8000**的细胞；作者固定脚本对读入的四个 uPAR 分选矩阵依次保留 `percent.mt < 5`、`250 < nCount_RNA < 30000`、`nFeature_RNA > 2000`。这些阈值、严格/非严格界及所写度量不同；不能仅将两个版本视为等价。GEO 描述的8000基因下限尤其值得向作者确认是否转录、排版或分析阶段差异，**未据此推定哪个正确**。
- 同一 GEO 条目称每样本调整以目标捕获8000细胞；这与上段 GEO “8000 genes”是不同量，不能自行合并或把前者当成对后者的纠正。
- 稿件方法描述选择2500个高变基因，但该固定脚本对分选数据调用 `SelectIntegrationFeatures(..., nfeatures=3000)`。GEO与稿件可能为通用方法、脚本可能不同版本或不同阶段；静态比较不能确定发表图的实际输入或阈值。

建议请作者提供分选数据对应的最终运行提交、每步筛选前后按样本的细胞数量、QC门限及会话环境，澄清 GEO、方法和脚本的关系，然后在同一输入/种子下预设门限敏感性分析。GEO 条目与脚本均为公开对象，但尚未下载矩阵或执行R、未核判 60%及图表数值，也没有判定该研究错误。

## 已核来源与尚未解决

- [Fig 2f](https://www.nature.com/articles/s43587-025-01022-w/figures/2)：年轻两组各10，老龄对照13、CAR 14；两独立实验，口服4小时血浆归一化荧光。论文统计方法明确小鼠未随机，采集分析未盲、观察小鼠状态另有盲法人员；Fig 2f 不等于自然寿命或人群效果。第22章对此保留限制。2025为线上发表年份，GEO 期刊引文是2026年卷期，两者非必然冲突。
- [Fig 1](https://www.nature.com/articles/s43587-025-01022-w/figures/1) 和正文确将小鼠 uPAR 正负分选，计算标签阳性中约60%属于阳性组；9430/7379是捕获的两组细胞数，而非真实组织比例。GEO列阳/阴×雄/雌四样本，须另核池与门控。第22章正确区分条件概率及功能真值；更进一步应明确前者也是**分选、捕获后的样本**，并非未经权重校正的组织覆盖率。[局部固定脚本](https://github.com/Vyoming/Regen_CAR-T/blob/37d02fd32d90c9dd14981da8b8e9f7edc6037179/UPAR_Sort_scRNA.R#L489-L519) `margin=2` 支持所称条件方向，基因表含 `Plaur` 的重叠影响未被量化。
- [Deng Fig 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC13620297/figure/acel70742-fig-0006/)和[Fig 7](https://pmc.ncbi.nlm.nih.gov/articles/PMC13620297/figure/acel70742-fig-0007/)确报告三猕猴相关面板、两次后续采样与不同结果描述；Fig 7D 的 liver 与正文 skeletal muscle 不一致。未见完整个体级数据，不能强行归因标签错误或将样本当同质重复给药队列。正文称一只重复方案首剂后AST 108、ALT 134、食欲减退，异常3天内消退；不是人体或长期安全证据。
- [Demaria Fig 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349629/figure/F6/)与[正文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349629/)支持特定鼠伤口的PDGF-AA闭合救援（n=5；另一双敲模型n=3），作者讨论纤维化改善很小；与拟议2×2方案不同。Grosse 2020 本次仅读[摘要](https://pubmed.ncbi.nlm.nih.gov/32485135/)，未审核全文。

## 模型与本地实质推进

固定 PR 代码的两个虚构条件概率表和4个随机化观测组合均经计算核对；独立穷举0–7四格、双分母非零的3976个整数表，计算方向吻合。`M=P` 的两个世界观测四格一致，但在设定 `C=1,P=0` 的离支持 `do(M)` 下差异分别20和0；证明依赖完全无重叠和允许直接路径，非真实实验结果。

在当前分支另写[分选样本敏感性说明](../../knowledge_base/imported_pr2/SORTED_SAMPLE_SENSITIVITY_2026-11-27.md)、精确算术脚本及4项测试：假设相对纳入比为 `r`、采样比例 `q`，总体比例 `t=q/(q+r(1-q))`；虚构 `q=.6` 在 `r=1/10、1、10` 下分别为 `15/16、3/5、3/23`。若人为假定r在[1/2,2]，模型锐界[3/7,3/4]，不是可信区间或真实uPAR范围；若r无界，任何内部比例相容。保护本地已有不同版本，没有整体导入PR章节或账本。

## 隔离检查和远程状态

- 固定头 `git archive` 在 Python 3.11.2、networkx 3.6.1、jsonschema 4.26.0、beautifulsoup4 4.15.0 下根验证 **85 project / 85 experiments / 21 pilot**；跨双种子、搬迁测试数与三个CLI输出一致，29历史断链、0新增。此环境不是固定锁文件（其 networkx 3.7 需要 Python ≥3.12）；不代表 CI、科学认证或独立审稿。
- 当前工作树临时副本主测试 **168**、独立 pilot 原位与搬迁各21项通过，三个CLI一致、22历史断链/0新增，快照 `python -O` 通过；人工新例测试只检验代数。
- 固定头相对基线146路径、本地22相同/33不同/91缺失，仍有大小写仪表盘碰撞；[比较明细](PR1_SNAPSHOT_52DD494_COMPARISON_2026-11-27.json)。两远程job `140663494283`、`140663473877` 注释皆因付款失败或额度不足**未启动**；状态 `UNSTABLE`。`git diff --check 78834bf 52dd494` 通过；未更新仪表盘、未合并或推送。

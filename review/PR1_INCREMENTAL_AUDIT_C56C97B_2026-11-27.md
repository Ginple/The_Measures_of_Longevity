# PR #1 增量审计｜c56c97b

审计固定头 `c56c97bc91b254af48df9343f73af3aedb370d7e`，相对上次审计 `370dd15f9122933290338df7028556045c33e855` 的三个提交、25路径；结果不自动适用于后续头。未切换分支、覆盖本地草稿、合并或推送 PR。本文系同助手审计，不是独立外审或出版批准。

## 按优先级排列的发现

### 1｜模型文字将总输入写成每段输出（新增，低风险但须修）

[`TIMING_CAPACITY_INTERACTION_2026-11-27.md` 第15行](https://github.com/Ginple/The_Measures_of_Longevity/blob/c56c97bc91b254af48df9343f73af3aedb370d7e/knowledge_base/experiments/TIMING_CAPACITY_INTERACTION_2026-11-27.md#L15)写“输出在两个时段均为2”。四格均为**两时段总输入为2**，不是每段输入或输出均为2；保留上限时累计处理2，减少上限时累计处理1.5、期末积压0.5。建议改为“两种时序的两段总输入均为2”；如要比较输出，分列各格累计处理和期末存量。代码、表格及差中差0.5在其规则下正确；不能把文字误差当作计算崩溃或临床发现。

### 2｜标称测试依赖无法装到 CI 的 Python 3.11（基线已存在，不是本次新增）

[`requirements-tested.txt` 第1行](https://github.com/Ginple/The_Measures_of_Longevity/blob/c56c97bc91b254af48df9343f73af3aedb370d7e/requirements-tested.txt#L1)固定 `networkx==3.7`，本次实际在全新 Python 3.11.2 venv 执行 `pip install -r requirements-tested.txt` 失败：该版本声明需要 Python ≥3.12。此文件在基线 `6be77be` 即相同，并非本次新增。PR [CI](https://github.com/Ginple/The_Measures_of_Longevity/blob/c56c97bc91b254af48df9343f73af3aedb370d7e/.github/workflows/ci.yml#L10-L14)选择 Python 3.11，但安装的是 `-e .` 的宽范围依赖和 Beautiful Soup，**没有安装该固定文件**；因此 CI 若能够启动，也不能证明锁定环境可在3.11复现。基线也存在宽范围安装；PR 只增加 Beautiful Soup，未造成此差异。

本次手动用 Python 3.11.2、networkx 3.6.1、jsonschema 4.26.0、Beautiful Soup 4.15.0 完成工程验证；这不是固定依赖文件测试，也不是 GitHub Actions 实际执行。建议明确受支持 Python 与各版本的锁定方案，添加从干净环境安装各锁定文件的矩阵；若只为某一 Python 测试固定版本，应在文件名和说明注明，并对其他版本提供验证过的组合。不要仅把需要3.12的包直接放进3.11 CI。账单修复是 CI 能启动的另一个独立问题。

## 研究核读与待核，不作为代码错误裁决

- HALE：复核 [Garmany/Terzic 2024原文PDF](https://www.healthreformgroup.au/wp-content/uploads/2025/01/JAMA-HealthspanLifespanGap_garmany_2024_oi_241395_1733259944.03263.pdf) 统计方法确写 `(2019−2000)/20`，两同日期端点相隔19年；PR 将其保留为条件口径问题合理，未取得作者代码，不自行改数。WHO [当前元数据](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752)明确说明 Sullivan 健康等效年及新版不可直接与旧版比较；当前元数据不能反证2024版本的完整计算。
- 该论文 Figure 3A 方法定义横轴 `(LE+HALE)/2`、纵轴 `LE−HALE`，两轴共享变量；将其关系描述为“与长寿相关”时须谨慎：对任何同一国家集，`Cov((LE+HALE)/2, LE−HALE) = (Var(LE)−Var(HALE))/2`，故线性协变部分由两个指标的方差结构决定，不是独立暴露—结局关系或因果证明。这是我们对该图的新增方法限制，不指称 PR 第1章已作这种因果断言，不假定真实方差或重新计算数据。
- 论文把 `均值 ± 1.96×国家间SD` 称“95% CI”，并用于 Bland–Altman 风格图的横线；若 SD 确指各国家差值的标准差，这种界限与通常针对平均值的 `标准误` 置信区间不同；它可能用作描述差异分布的界限，但其解释仍需核原始方法、公式/作者代码和分布假设，不是据此否定所有研究结论。PR 已将此列作未决，本次补具体原因；**未复算区间**。
- [2023 心肌 EV 原文](https://www.nature.com/articles/s41467-023-40680-5)方法确述组织分离用0.8 μm过滤、培养巨噬细胞20–24小时阳性细胞比例；Fig.7 n=5独立实验、每次至少100细胞，培养共定位和心肌切片不是同一连续跟踪。Fig.8人类数据共4个独立供体、其中2名 Danon 患者；这些支持 PR 在稿中保留的范围限制，但没有完成源数据或全部图的复审。
- [2025 预印本](https://www.preprints.org/manuscript/202512.0724)标 Hypothesis/未同行评审，摘要结论肯定优越、限制段承认尚未头对头；[Martens 2018](https://www.nature.com/articles/s41467-018-03421-7)为小规模NR交叉试验，并未测试该组合顺序。PR 将叙述限定为假说而非处方正确；并未系统证明领域内不存在其他试验。第19、20章及骨架是候选稿，非作者定稿；仍需领域、方法与读者独立审阅。

## 软件审阅与验证

审读新增4个纯合成脚本及相应15项测试、3篇数学说明：人工生命表18/15/3、固定容量四格差中差1/2、动态容量同变反例、货物守恒界的公式与所列例子相符，受其列示假设约束；此核查不是研究结果实测。另在归档副本穷举货物边际及其他出口上下界小整数网格 **3125** 例，与半单位步长可行集端点一致；对两个队列函数检查 **2048** 个非负小整数方案的守恒与非负。非穷尽真实输入、不证明任何生物模型有效。

`git archive` 的独立临时目录执行该提交自带 `scripts/run_validation.py`：project 85、experiments 73、pilot 21 项；两种种子及搬迁计数、三个 CLI 字节一致；示例输入和 schema 一致；29条历史断链、0新增。初次尝试引用旧 `/tmp` venv 失败（环境不持久）；建立新 venv 后按固定依赖安装又遇上述版本限制，最终安装兼容依赖后成功。`git diff --check 370dd15 c56c97b` 通过。远程 checks `140550851129`、`140550823741` 的 annotations 均显示付款或额度原因，**任务未启动**，无远程测试结果；未重跑。

[相对基线的字节快照](PR1_SNAPSHOT_C56C97B_COMPARISON_2026-11-27.json)：128路径、当时本地24相同/29不同/75缺席，未统计本地额外文件；PR 中 `STATE_DASHBOARD.HTML` 和 `STATE_DASHBOARD.html` 大小写冲突仍需跨平台解决。本轮未生成、更改或展示仪表盘。患者数据、完整源码和独立科学审稿未取得。

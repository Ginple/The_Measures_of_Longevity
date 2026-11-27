# PR #2 定向审计及对 PR #1 的选择性整合

2026-11-27｜审计对象 [PR #2](https://github.com/Ginple/The_Measures_of_Longevity/pull/2) 固定头 `b8434e22ec62ba21814546560a33fc38f4939e9f`，基线 `6be77be2b2b8d7cfd8182faa936853cc5b45111e`；整合前 PR #1 固定头 `bbec79c095bbd7bad66510a004dfcd0f0593704f`。这是同助手定向审计，不是逐条科学认证、系统综述或独立外审；只读抓取提交对象，未切换分支，不合并或关闭 PR #2。以后 PR #2 更新时应重审新增提交。

## 优先发现

| 优先 | 发现与证据 | 对 PR #1 的处理及未决 |
|---|---|---|
| P1 编辑/合并风险 | 以相同基线比较，PR2 154个变更路径中，当前头22个字节相同、106个当前仍等于基线（其中包含缺席路径）、26个双方不同；这是字节分类，不等于语义重复或逐文件全面审查。PR2 `X32` 为成熟退出术语，PR1 `X32` 为 TranslAGE 多钟；PR2 `X39` 是 CAPABLE 资格，PR1 `X39` 为成熟退出术语。PR2 候选32章与 PR1 40槽的第23/24章含义不同。 | 不整树合并、覆盖账本或按编号自动去重。以固定来源 SHA 命名追溯，新增项目使用 PR1 X71–X74；生活/照护素材单独存放，作者仍须决定结构。 |
| P2 可复现 | PR2 根 `requirements-tested.txt` 固定 networkx 3.7，CI 选择 Python 3.11 并安装宽依赖而非该文件。本次 Python 3.11 的 `pip download --no-deps networkx==3.7` 因要求 Python ≥3.12（另排除3.14.1）失败。固定文件在共同基线已存在，不是 PR2 新引入。 | 此次验证用3.6.1等兼容版本，不称固定依赖复现；历史依赖/收据未重写。需要为支持的 Python 版本制定并验证独立依赖锁及干净安装矩阵，账单恢复后再核远程 CI。 |
| P2 快照范围 | PR2 单独 verifier 修复 `assert`/空清单问题且 `-O` 检查通过；其根 `scripts/run_validation.py` 并不调用 verifier，故根验证通过不表示来源快照已核。manifest 与文件同处本地，匹配不等于外部签名或原论文使用版本证明。 | 择取 verifier 和负向测试；PR1 根验证现明确执行本地与搬迁副本的普通/`-O` 快照一致性检查，并作为成功条件；无改动既有来源文件或 manifest。 |
| P2 审核与版本差异 | PR2 对 PR1@52dd494 的审计指出 GEO 和固定脚本的 QC 阈值、整合特征数不同；本次读雄性阳性条目与固定脚本，确认文字差异。PR2 同时指出 CALERIE 表2组内变化和交互的条件算术不闭合、CANTOS hs-CRP 同单位数值差10倍。 | 分别记 [X71–X73](../knowledge_base/CLAIM_LEDGER.md)，保留不同版本/模型、分母及作者核实要求，不裁定论文或效应错误。未运行R、取原矩阵或复算患者数据。 |
| P3 数值/文字 | PR2 检查发现 PR1 时间×容量说明误把两段总输入说成每段输出；图6F审计将 Fig 5 图注的珠子 MFI 写作总荧光。本次复核[Fig 5](https://pmc.ncbi.nlm.nih.gov/articles/PMC8963880/figure/fig5/)图注并对照模型。 | [时间例](../knowledge_base/experiments/TIMING_CAPACITY_INTERACTION_2026-11-27.md)改为总输入2和处理1.5/2；[空间审计](../knowledge_base/SPATIAL_ACCESS_EVIDENCE_AUDIT_2026-11-27.md)及第21章改作MFI并保留24小时汇总方式未核。表和数据不变。 |

这些等级是本项目的处理优先级，不是对研究价值或作者诚信的判定。PR2 的保护现有源码字节、禁用历史打包器以及不称本地检查为科学认证是合理边界；其唯一 `git diff --check` 输出是上游原样保存的 `PACEProjector.R` 文件尾空行，未擅改快照。其他 106/26 路径**并非全部已审或无价值**；本轮未导入者仍可从固定提交逐项再审。

## 已整合到当前 PR #1 分支

1. PR2 的显式失败快照验证器、安装烟测、独立 pilot 零测试失败逻辑及对应负向测试；PR1 保留现有双仪表盘合同和独立的三套测试架构，不用 PR2 的根验证器整体覆盖。CI 加 standalone pilot。`install_smoke` 在打印成功前核模块/分发路径、版本、schema、CLI issues及发布门；测试模拟子进程，另做真实本地安装。
2. [两类捕获/共同幸存者边界](../knowledge_base/experiments/PR2_CAPTURE_AND_SURVIVAL_BOUNDS_2026-11-27.md)及代码、测试：保留有限总体、正捕获权重和单调性等条件；增加 `monotone` 的严格布尔校验。抽样不确定性、失访和真实对象不由该模型解决。PR2 的人造模型与 PR1 已有混合权重模型不同，不声称首创或独立数学证明。
3. [P3 评价合同](../papers/P3_research_assurance/PR2_EVALUATION_PLAN_2026-11-27.md)及人造指标计数代码，区分字节失效和科学判断、计入拒绝、预设项目簇防泄漏；尚无独立盲测和性能结果。
4. [生活环境和照护编辑素材](../books/PR2_生活环境与照护_编辑素材_2026-11-27.md)，保留决定权、辅助与照护者成本；不冒充正文或改变第23章。PR2 的 FIND 骨折和 CAPABLE 方案差异可作为线索，未取得全部原材料，不直接采用未经本轮核实的数值。
5. [X74](../knowledge_base/CLAIM_LEDGER.md) 区分 GUT26 首次损伤期阻断与形成记忆后的操作，限定真实药效未测；为第24章提供候选研究素材，非已实施方案。

## 检验记录和仍须处理

- `git archive` 固定 PR2 头在 Linux、Python 3.11.2、networkx 3.6.1、jsonschema 4.26.0 的兼容环境运行其自带根验证：168项通过、CLI双种子/搬迁字节一致、22旧/0新断链、无HTML；独立pilot原位及搬迁各21项通过，`python -O` 独立快照校验通过。该根验证器未检查搬迁测试套件，也未调用快照验证器；是软件验证，不是源数据重跑。
- PR1 整合后的根验证：项目106、实验89、pilot21项，双种子及搬迁测试数相同、三条CLI输出字节一致；本地及搬迁快照一致性在普通与优化模式均通过，29旧/0新断链。独立pilot在原位和搬迁各21项通过。负向测试在临时副本改坏快照、删空测试，并模拟安装子进程的不合格结果，未改历史收据。
- PR2 幸存者 oracle 在 `N=1…6` 三值、单调/非单调共19,390个边际/假设组合通过；同开发过程的有限穷举，不代表独立数学证明。真实 `python -O tools/install_smoke.py` 初次因虚拟环境缺 wheel 失败，安装 wheel 与符合构建要求的 setuptools 后通过；依赖预装、无干净联网安装，正式发布门仍 blocked。
- PR2 checks `140668452951` 和 `140668361947` 的 annotations 均称账户付款失败或需提高额度，job 未启动；PR2 检查状态为 failure，不能称远程 CI 已通过。PR1 也有历史同类账单阻塞；新提交的远程结果需另查。
- 两个 `STATE_DASHBOARD` 路径仅大小写不同，PR1 在大小写不敏感系统存在 checkout 风险；本轮不擅删历史路径。29历史断链、发布打包流程、依赖锁、作者澄清、真实数据复算和独立审阅仍开放。

## 后续：修复记忆择要整合

以同一固定头 `b8434e22ec62ba21814546560a33fc38f4939e9f` 的研究审计及候选稿为线索，另核指定原文，按本分支章节安排重写 [第24章](../books/manuscript/CH24_修好这一次还剩多少下一次_示范稿.md)，不导入对方冲突章号与X项；详细范围、竞争解释及残留问题见[时间窗审计](../knowledge_base/RECOVERY_MEMORY_CAUSAL_AUDIT_2026-11-27.md)和[自查](CHAPTER_24_SELF_REVIEW_2026-11-27.md)。COLON体外撤药与体内同时诱导不拼接；GUT Fig 7的前一日开始与正文后续给药措辞差异、药效仍待核。另添加自行构造的[恢复资格反例](../knowledge_base/experiments/RECOVERY_ELIGIBILITY_COUNTEREXAMPLE_2026-11-27.md)，不是PR2原文数据。登记 X75–X76，X74补充；均未关闭。未做独立外审、数据复算或系统综述。

## 后续：TPE 时间与推断单位

依据PR2固定头的TPE审计线索，本分支由同一助手重新定向核对指定原文、当前登记与作者固定代码，[记录范围和未决事项](../knowledge_base/TPE_TIMING_ALLOCATION_CLOCK_UNIT_AUDIT_2026-11-27.md)；撤回X05将发表版35/36差异视作仅跨版本且已解决的判断，新增X77/X78并升级KERNEL v0.9.7、纠正前沿F6。新合成重复时钟示例受PR2启发、不使用真实试验数据，不证明发表数值错误；历史冻结文件及pilot语料未改，外部独审与复算仍未进行。

## 后续：CAPABLE 和CI依赖

[CAPABLE续审](../knowledge_base/CAPABLE_OUTCOMES_ELIGIBILITY_AUDIT_2026-11-27.md)重新核设计文、当前登记、结果文，按本分支新增X79/X80；2025出院后研究仅读摘要，暂不定量综合。用户修复账单后，PR1@375fe09的两条旧配置 Actions 均实际成功；本轮新增Python 3.11版本清单和干净环境安装验证，范围及PR2旧检查重跑受权限阻塞见 [CI回执](CI_DEPENDENCY_REPRODUCIBILITY_2026-11-27.md)。新配置在 PR1 `dd47ce68a5bad07d814c3685786e12d601327c49` 的 push 和 pull_request 两条远端检查均已成功；GitHub 对 Actions Node.js 20 发出弃用警告。之后用户报告 Actions 权限可能修复，再次尝试 PR2 两次旧检查仍无法重跑，API 再次返回 403，详见CI回执。

## 后续：共同组分与七例开发回归

按同一 PR2 固定头继续审查：择取[共同组分联合界](../knowledge_base/experiments/PR2_SHARED_COMPONENT_BOUNDS_2026-11-27.md)、精确算术脚本与有限网格测试，保留额外共同假设及不可行情况；测试另补两个边界。择取 P3 的七例[开发比较夹具](../knowledge_base/experiments/assurance_fixture_comparison.py)与测试，使用临时副本，修改 `assert` 为显式失败，避免 `-O` 静默跳过；范围与不同 oracle 下的解释见[P3 合同](../papers/P3_research_assurance/PR2_EVALUATION_PLAN_2026-11-27.md)。首次使用系统 Python 因未安装 jsonschema 报错，改用此前已安装固定清单的隔离环境复跑；隔离环境下根验证通过：项目110、实验98、pilot21，双种子及搬迁一致、0新增/29历史断链、快照普通与 `-O` 一致；夹具测试在普通和 `-O` 模式各4项通过，共同组分测试4项通过。这些是人工演示及开发回归，不是独立评估、真实数据分析或 P1/P2 论文结构的作者裁决。

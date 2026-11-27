> **PR #2 移植件**（来源：[PR #2 固定头 `b8434e2` 原路径 `review/PR1_RECONCILIATION_2026-11-27.md`](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/review/PR1_RECONCILIATION_2026-11-27.md)；移植于 2026-11-27，用户批准“选择性移植后关闭 PR #2”）。文中 X 编号、章号、ANOM 等属于 **PR #2 命名空间**（引用时写作 PR2-X32 等），与本分支 `knowledge_base/CLAIM_LEDGER.md` 的同号条目**不同义**。未经本分支逐条复核，不作为正文、KERNEL 或论文的证据；指向未移植文件的相对链接已改为固定提交的 GitHub 永久链接。

# 本地与 PR #1 的快照核对｜2026-11-27

**结论：存在分叉，不能直接合并覆盖。** 本地当前分支 `arena/61c999d8-the-measures-of-longevity` 的 HEAD 为 `6be77be2b2b8d7cfd8182faa936853cc5b45111e`；它的已保存工作成果主要是未提交工作树，不等于 HEAD。只读 `git ls-remote` 显示当前分支在远端没有同名 ref；本地 `main` 与远端 main 均为上述基线。PR #1 的远端 head 在本轮只读取并 fetch 到 `FETCH_HEAD`，固定为 [`5d544dbc4256058807f44c4c2c13748f30ee7721`](https://github.com/Ginple/The_Measures_of_Longevity/commit/5d544dbc4256058807f44c4c2c13748f30ee7721)；当前分支没有切换或重置，未 cherry-pick、合并、推送或覆盖文件。PR 仍 open；随时可能有新 head，后续整合前重新核对。

[逐文件字节快照](PR1_SNAPSHOT_COMPARISON_2026-11-27.json)只比较相对于共同 HEAD 在远端改动过的 68 条路径与本地工作树：**15 字节相同、30 不同、23 本地缺席**。本地缺席包括远端小写 dashboard；用户本轮已取消生成仪表盘，不能复制或修改它。30 个不同包含尚未接入的远端变更及双方均修改的路径，不能全部称为本地新成果或直接判为冲突解决。快照还列出当时远端变动路径之外的本地未跟踪文件，不是全仓逐 blob 证明；比对只管字节，不能证明科学结论或内容源头独立。JSON 是执行比对时刻的不可变快照，之后增加的本轮工作不在该列表中。

历史上本地工作树接入的是旧 PR 补丁，远端此后有九个提交（从 `7013600` 至 `5d544db`）；远端自身累计 13 个提交。**不把这些既有提交或其已写研究当作本轮新发现。** 后续若整合，保留固定 SHA、逐文件对比，尤其是 validator、pilot、依赖、CI、快照文件和历史回执；对已有本地变更作三方审阅，禁止覆盖或重签历史测试。

## 登记编号碰撞：必须带命名空间

以下均为当前两边原有编号，不是新分配号码。`L:` 表示本地工作树台账；`PR1@5d544db:` 表示固定 PR 版本台账；除相同主题外，不得使用不带来源的编号做跨快照引用。L:X32 与 PR1:X39 同为周转 m 术语问题，仅是候选同一问题，措辞及证据范围还需人工合并。

| 编号 | 本地工作树 `L:` | 远端 `PR1@5d544db:` |
|---|---|---|
| X32 | 周转 m 误写 | TranslAGE 多钟方向分类 |
| X33 | EPI-Clone 干预扰动标签假说 | TranslAGE 与 RCT 综述 estimand |
| X34 | CALERIE 时点口径 | MTO 青少年论文撤稿替换 |
| X35 | 结肠类器官洗脱与体内共时干预 | p16-3MR 清除争议 |
| X36 | GUT26 残余药效 | TranslAGE 多重性与 PCA |
| X37 | CAPABLE 对照接触与缺失 | methylCIPHER 许可及 PoAm38 包装器 |
| X38 | CAPABLE 主终点版本 | DO-HEALTH 标准化换算 |
| X39 | CAPABLE 收入/住房资格 | 周转 m 误写 |
| X40 | LoDoCo2 导入期区间 | BASE-II 预测模型与选择 |
| X41–X45 | 本地尚无 | 多癌筛查及模型统计、HARP、Cochrane |

X30/X31 主题大致共同，但远端后来增加内容；即便编号相同也不能假定文字或核查程度一致。计划未来形成有稳定标识的合并对照、逐项核来源与历史依赖，必要时人工修正下游引用；未完成前不将两台账相加或宣称已合并。用户取消新仪表盘后保留原历史文件不做更新，其台账快照自然不会反映本轮继续工作。

## 远端已有、当前工作树没有的研究与工程

固定版本中的 [来源与跌倒审计](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/knowledge_base/MCED_CODE_AND_HOME_FALLS_AUDIT_2026-11-27.md)、[筛查与预测审计](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/knowledge_base/SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)、[多重性与功能审计](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/knowledge_base/MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)、[DO-HEALTH 单位审计](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/knowledge_base/DO_HEALTH_UNIT_CONVERSION_AUDIT_2026-11-27.md)、[持续时间诊断](https://github.com/Ginple/The_Measures_of_Longevity/blob/5d544dbc4256058807f44c4c2c13748f30ee7721/review/EXECUTION_DURATION_REVIEW_2026-11-27.md)及若干合成脚本/测试均是远端先前成果。远端与本地的验证器、实验和完整性合同不同，测试数不可直接相加。未将其完整落地，避免未解决的引用和合同覆盖；可从固定 commit 安全读取并在隔离副本运行。此报告之外的本轮来源核读明确标为新增而非远端已有内容。

## CI 与执行时长

PR 的最新两项 Actions 在 2026-11-27 11:35 UTC 返回 failure，但 job steps 均为空；读取 [job annotation](https://github.com/Ginple/The_Measures_of_Longevity/actions/runs/45991763039/job/140481055296) 明示账户近期付款失败或需提高支出限额，**job 未启动**。需要账户管理者检查账单与额度；没有重跑。失败不能推断项目代码通过或不通过。

用户指出的提前收束有事实依据：离线工程验证秒级且不执行文献复算、真实实验或独审，不应将其当成阶段结束。本会话暂存的 `/tmp` 虚拟环境本次恰好仍在，**不能假设新环境永远保留它**；必要时按 `pyproject.toml` 在临时目录重建。远端早有诊断和任务队列，本文件在此基础上比对当前两个分支，不宣称诊断为本轮首次提出。

## 本轮选择性工程修复（不是整合 PR）

仅在确认以下六个本地文件仍与共同 HEAD **字节相同**后，移植固定 PR 版本：`tools/run_validation.py` 统一验证入口；`tools/install_smoke.py` 在临时副本安装、不写历史回执；`tools/verify_history.py` 使用当前 `corpus` 路径、缺失源/目标判 not_verified 且不写回执；两个旧 packager 显式禁用以防覆盖冻结 manifest/信任过期结果；pilot 验证器使用根目录布局且只打印当前结果。固定 PR 已有这些修复，不冒称最先发现。未复制远端其他同名文件。

另基于**本地已修改版本**手工调整：`scripts/run_validation.py` 不再写 `results` 里的历史回执，未知命令行参数报错、`--unit-only` 只执行单元测试，超时保护、空/跳过不当成功；旧 HTML 如存在只作历史文件静态检查，不要求存在，更不要求与持续更新的登记保持同步；不生成或更新它。pilot requirements 的 editable 路径修为根目录；CI 补装 pilot 的 BeautifulSoup、执行 pilot 验证。用户明确取消仪表盘需求优先于历史自动合同。

本地**隔离副本**新验证：主套件 104 项、pilot 21 项以及 pilot 移动副本 21 项均通过；主套件双种子/搬迁 CLI 字节一致、22 条历史断链且新增 0；pilot 的不可变输入未改、独立外审未做；安装烟测在预装依赖条件下通过，不等于干净在线安装或学术发布。第一次 pilot 运行因临时虚拟环境缺 BeautifulSoup 而报 4 错、版本元数据异常；装其声明依赖及 wheel 后重试通过，失败未隐藏。新增测试仍是软件/合成合同，不是原始数据复算。远端 CI 仍账单阻塞，本地通过不能替代远端 CI 绿灯。

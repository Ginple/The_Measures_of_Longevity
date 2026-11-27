> **PR #2 移植件**（来源：[PR #2 固定头 `b8434e2` 原路径 `review/PR1_CONTINUATION_AUDIT_2026-11-27.md`](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/review/PR1_CONTINUATION_AUDIT_2026-11-27.md)；移植于 2026-11-27，用户批准“选择性移植后关闭 PR #2”）。文中 X 编号、章号、ANOM 等属于 **PR #2 命名空间**（引用时写作 PR2-X32 等），与本分支 `knowledge_base/CLAIM_LEDGER.md` 的同号条目**不同义**。未经本分支逐条复核，不作为正文、KERNEL 或论文的证据；指向未移植文件的相对链接已改为固定提交的 GitHub 永久链接。

# PR #1 接续审计与修复｜2026-11-27

**审计性质**：当前助手定向审查，非独立审计，不能证明全库断言、临床安全或原创性。GitHub [PR #1](https://github.com/Ginple/The_Measures_of_Longevity/pull/1) 查询为 OPEN；当前分支源于 main 的 `6be77be2b2b8d7cfd8182faa936853cc5b45111e`，没有该 PR 的变更。读取 PR 4 个提交的完整 patch，检查可应用后应用到当前工作树；两个大小写不同的仪表盘文件排除，并新制单一大写 `STATE_DASHBOARD.HTML`。未合并、关闭或改动原 PR；本工作树也不是原 PR 的分支，未来合并需处理重复差异。

## 发现及处置

| 发现 | 修复 / 限制 |
|---|---|
| KERNEL I6 将 `m` 写成迁移；原模型定义 m=成熟退出、d=其他丢失，不包含迁移 | 修复并登记 X32；其他文稿未全面查完。|
| MASTER 顶部撤回 DEC-003/004，但表格仍显示已采纳；历史审计称 36 章，实际 40 | 修改决策表与压缩方案表述；新增 32 章工作地图，仅为明确可审的候选，不代表独审、作者定稿或 X17 已关闭。历史报告保留并有醒目撤回说明。|
| PR 同时增加大小写同名 HTML，大小写不敏感文件系统冲突 | 仅生成 `STATE_DASHBOARD.HTML`，无小写副本。|
| 仓库迁移后 README 命令与测试 fixture 路径仍指旧的 `methods/research-assurance`；CI 禁止任何 HTML | 修复工作台路径、测试 fixture 和 CI 的 HTML 合同，只允许根目录本次授权文件；历史验证结果不被更新为新结论。|
| 历史 HANDOFF 与上游 playbook 包含失效链接 | 精确列入 `review/legacy_broken_links.json`，验证输出仍报告，新增断链会失败；这是明确的临时债务而非全库链接已修复。|
| 原 KERNEL 把观察关联称为“保护因子” | 改为关联，保持因果限制；其他未经审阅的候选条目仍不得用于正式引用。|
| 验证试验的 denominator X31 | 本轮复读原文 Main 和 Fig.1 说明与更正；在明确同集合假设下边界不一致仍待澄清，未判断哪一个数字错误，也未验证疗效。|
| 根级 V6/V7 与 corpus 当前稿均存在 | 根级 README 标注遗留、禁止编辑；正文不删除不覆盖，原本与附件相同的哈希见下。|

## 附件与外部边界

附件 README、HANDOFF、BOOK_PROPOSAL 和三份 PROTOCOL 与仓库对应基线文件 SHA-256 一致；V6、V7 附件正文与 corpus 对应正文一致（V6 `81b5410839b32602f7bba6d078274d9695ba644541c28540875924c5c3c330f2`；V7 `a388a8fb91203f00739cae93a21c8d30c0a35ec4403745ed30c37fe29009b85e`）。旧 HTML 是历史快照，不能覆盖当前稿。其余附件未逐项比较，不以附件本身证明科学正确。

指定的 `Ginple/THE_LIVING_FACE_OS` GitHub API 返回 403 Resource not accessible by integration；无法读取其目录/核心文件，未用其他项目代替。若需要，请扩展该仓库的 GitHub 集成权限或提供材料。PR #1 可读不代表其他仓库亦可读。

## 后续

D05 仍 open；高风险定量锚点逐项回查原始版本和完整 Methods，X31 请求图表/数据字典/作者解释；两份正文逐段映射，三篇增量门槛独立审阅；P3 预注册盲评及第二项目；第三方 PDF/源表的再分发和公开许可审查。关联 Linear THE-227/229/233/234/236/237 已添加进度评论、未更改其状态。

## 验证回执（软件范围）

- 首次运行暴露旧测试路径和缺少依赖；修复路径后在临时虚拟环境安装仓库声明依赖，并在 `/tmp` 仓库副本运行 `scripts/run_validation.py`，通过：79 项当时测试、两种 hash seed 和移动副本输出一致、示例未改、schema 相同；29 项已知历史断链有明细、意外断链 0；仅一个授权 HTML。此检查不证明历史断链已修复。
- 人工验证了仪表盘 15 个链接的本地目标均存在；其后加入自动化链接测试，最终在另一临时副本复跑 80 项，0 失败、0 错误；软件验证与两个 hash seed/移动副本一致性均通过。外部 URL 的权限/持续可用性不在本地检查之内。
- 两个 PR 人工演示脚本均运行成功；DunedinPACE 快照与 `review/local_source_snapshot.sha256` 校验成功。前者不是生物数据，后者仅是相对于已记录哈希的字节一致性，非科学或历史真实性认证。未覆盖写历史 results/baseline。

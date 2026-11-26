# 本轮敌对与复杂输入审查 / Adversarial and complex-input review

日期2026-11-25。**同一助手的本地自查，不是独立外审。** 无新生物实验、无临床疗效验证。最终计数/环境/重放结果以主仓库 `artifacts/VALIDATION.json` 为准。

## F01 / 冻结toolkit0.1.0的维度一致性漏检

输入：toy已登记reported断言，assessment.state=supported，但dimensions.source_support=refuted。其余来源/断言字节绑定维持一致，并用明确标记的合成审阅记录满足原格式，去除toy演示性开放债，声明inventory complete。

原版实测：`issues=[]`，`formal_release_record_check=recorded_prerequisites_present_not_certification`。这不是科学认证，但内部合同存在不一致的漏检。见 `artifacts/PRIOR_TOOLKIT_ADVERSARIAL.json` 和 `tools/audit_prior_toolkit.py`。

处理：原包不改；派生副本增加6类claim kind最低维度检查与测试，版本0.1.1候选。reported/descriptive/statistical/causal/transport/decision的合同见组件README。冲突状态不被自动修成supported；必须人审。

回归：组件55→56测试；新增一个测试函数遍历source_support/extraction与4种非supported状态。主项目另有测试遍历全部声明最低维度，且重签合法记录hash以隔离维度本身的影响。通过不意味着同一人故意错签supported时程序能发现科学错误。

## F02 / CGEE未测试PreToolUse模板的有限覆盖缺口

只对接收hash固定的附件中已经阅读的Python钩子（起始535行）进行临时目录重放。记录提取代码hash，stdin为模拟工具JSON；各Bash.command字符串**仅作数据，未被shell执行**。

8个案例：普通读允许；kb重定向写被拒；tools/.github/.claude三种写命令文本返回0；起草读tests/.git被拒；无脚手架书稿Write被拒。8/8符合预期观察，其中3项就是已复现漏拦截，不是“安全测试全通过”。见 `artifacts/ATTACHMENT_HOOK_AUDIT.json`。

边界：未启用真实Claude配置，未测试OS权限/容器/凭据/审批/分支保护，不能声称穿透系统隔离。模板的保护路径名单与Bash写入正则覆盖不一致；应采用真实权限边界而非继续宣称正则等于沙箱。

## 复杂输入与合法输入 / Coverage

主仓库23测试函数覆盖：500断言登记与外审缺失、6类维度矩阵、UTF-8组合字符与CRLF精确片段、非法编码拒绝、symlink越界、裁决变化令外审过期、证据中的指令文本不执行；未加权舍入合法/不合法、weighted/adjusted/survival分派、半舍入、非法N、空跑/跳过/建议性结果不绿。

合计组件56 + 主仓库23 = **79测试函数**；此外附件8项定向重放与原版1项反例，不计入79。测试函数数不是独立实验样本量；循环内断言不是新增人审或发表级统计证据。

## 集成失败保留 / Preserved integration failure

首次主工作台整体验收时，79测试已过，但README链接的目录树尚未生成，链接检查因此正确失败；原始结果保留为 `artifacts/FIRST_VALIDATION_FAILURE.json`。生成实际目录树后重跑通过。没有删掉该失败或通过修改断言hash掩盖问题。

## 仍未覆盖 / Residual limitations

没有随机fuzzing、跨OS/多Python版本、对抗并发/TOCTOU、恶意超大文件资源预算、真实平台输入变体、独立身份认证、完整语义与依赖抽取、二进制表/图坐标、多领域科学真值或盲评。Python路径校验不能单独抵御拥有本地写权限的并发攻击。

P3正式评估须冻结未见集、对照与oracle，报告误报漏报，而非拿本轮开发回归集充当独立测试。新补丁本身仍需外审；原科学债D02–D10未因这些测试关闭。

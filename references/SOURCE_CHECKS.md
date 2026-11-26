# 定向来源核验 / Targeted source checks

访问日期2026-11-25。不是系统综述，未完整核验两附件所有引文。附件精确凭证见 `attachment_receipts.json`；未分发附件全文。

## 本轮定向读取的官方/原始来源

1. **SkillsBench arXiv v4** — https://arxiv.org/abs/2602.12670v4 。读取摘要/版本页首块，并非论文实验表格和代码全面复核。摘要报告87任务/8域/18 model-harness配置、33.9%→50.5%、+16.6个百分点；不用于保证本项目效果。附件40.7%尚需查其原引用版本、分母和定义，未据此裁造假。题名 *SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks*。
2. **GitHub Secure use reference** — https://docs.github.com/en/actions/reference/security/secure-use 。定向读取chunk0、1（全页6块），包括最小权限、脚本注入、不可信代码检出和第三方action来源。官方警告pull_request_target/workflow_run结合检出不可信代码的风险；不是“用了其中一种trigger就必定被攻破”。没有本轮复现真实远端攻击。工作流依赖lockfile/完整SHA等建议也需按平台当时功能与本仓库适配。
3. **ICMJE AI use by authors** — https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html 。全文网页读取：披露AI使用，AI不列作者，人负责准确/完整/原创及引用，AI生成材料不作为主要原始来源。目标期刊仍可更严格。
4. **ICMJE AI use by reviewers** — https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-reviewers.html 。全文网页读取：遵守期刊政策或事先许可，保密，披露并验证AI辅助内容。没有据本轮页面断言其精确政策首次生效日期。

## 本轮没有完成的核验

- 附件中撤稿数量、Zenodo入口版本、所有35经验/14平台事实、价格/水印/会话榜单、许可主张；不自动迁移为可信事实。
- 拟题唯一性：只做有限关键词检索，不能证明无重名或商标可用。
- 旧研究科学债：LoDoCo2计数与CI、HipSci系数/实际执行路径、SenSCOUT真实数据真值、配对矩阵等仍待核。

## 延续上轮的方法边界

W3C PROV概览、NASEM2019可重现性/可重复验证讨论与PRISMA2020仅按上一轮记录的定向访问深度使用；本轮不声称重新完整复核。引用指南不等实现PROV兼容/PRISMA合规/科学认证。

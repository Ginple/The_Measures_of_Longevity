# 平台适配器 / Platform adapters

状态：**未安装、未启用**。本轮无Claude Code/WSL2权限部署，无GitHub远端写入、Linear/Notion/Google写入。

附件hook模板已在临时目录作有限重放，不复制至活动配置。确认返回0的样例只是钩子未阻断，不等真实主机可以写成功。OS权限、凭据、容器、分支保护、审批人与签名均须另行设计和测试。

建议未来权限分离：分析执行环境无生产密钥；不可信PR只能在低权限、一次性环境运行；评审/发布流程不执行其代码；审批记录绑定commit/对象hash及批准者身份。`base/`和`pr_data/`同级不是物理隔离，正则Bash解析器也不是安全边界。

根目录目前不附自动CI workflow，避免把未设好的权限/动作来源当已部署。内嵌toolkit `.github/`是上游历史软件CI示例，主仓库不会自动发现为根工作流。手动建库后先复跑、审核依赖和actions来源，再设计 `contents: read` 的普通pull_request测试；禁止向不可信代码注入secret。CI绿不等基线不可变，更不等科学正确。

GitHub官方安全参考的定向核验见主仓库 `references/SOURCE_CHECKS.md`。平台API会变化，本轮没有测试Claude工具输入格式与实际运行时兼容性。

# CI：Python 3.11 依赖版本固定与验证回执

2026-11-27｜针对 PR #1；工程合同不认证科学结论或正式发布。用户报告账单已修复；提交 `375fe0913ba029992d1c3d3f72272c464e062baa` 的 PR #1 两个 Actions 检查 `140678623139` / `140678601074` 已于 18:30 UTC 实际执行且 success。它们运行的是旧的宽依赖工作流，不等于本次新版本清单的远端验证。

## 修复与范围

- 历史共同基线 `requirements-tested.txt` 钉 `networkx==3.7`，无法在 Python 3.11 安装；不重写历史清单或回执。新增 [requirements-ci-py311.txt](../requirements-ci-py311.txt)固定本次解析的直接、传递、构建依赖版本，包括 networkx 3.6.1。CI 依次安装这些版本、本项目 `--no-build-isolation --no-deps`、`pip check` 和 `pip freeze --all`、根验证、独立pilot，以及真实安装 smoke 正常及 `-O`。
- 本地以 CPython 3.11.2 Linux x86_64 新建隔离 venv、使用 pip 23.0.1，通过允许的包索引安装清单（包可能来自本机缓存），从本仓库工作树进行可编辑安装；`pip check` 无冲突。根验证项目106、实验94、pilot21，0新增/29历史断链，两个哈希种子和搬迁版结果一致，快照原位/搬迁普通及优化模式通过。独立pilot原位/搬迁各21通过；本地真实 smoke 正常及优化通过。
- 这固定的是**版本**，未验证哈希签名，不固定 pip、系统、Python补丁版或 Actions mutable tags，不证明同名工件永远同字节；不是完全确定性构建、无网或其他平台验证。`pyproject.toml` 的宽范围与 >=3.10 支持声明未更改；本轮未测试3.10/3.12/3.13。`pip check`不证明源码安全或全部测试覆盖。`install_smoke` 项目安装为 no-deps/no-build-isolation，依赖在干净环境此前联网安装，仍非发布批准。

## PR #2 的旧检查及重跑权限

PR #2 固定头 `b8434e22` 的两次历史检查仍为因账单未启动的失败。修复账单不会自动重跑；本轮对旧的两个 run 各尝试 `gh run rerun --failed`，CLI 提示无法重跑。进一步查询 Actions rerun API 返回 HTTP 403 `Resource not accessible by integration`；这是集成权限限制，不等于账单仍坏，也不是测试失败。需要具备 Actions 重跑权限的用户从 GitHub UI 重跑，或在 Arena 重新连接并授权 GitHub Actions；此处未切换或推送 PR2 分支。随后用户报告 Actions 权限可能已修复，2026-11-27 再次对两个 run 调用 `gh run rerun --failed` 均仍显示无法重跑；对 `46046945270` 的 rerun API 再查仍为 HTTP 403 `Resource not accessible by integration`。不能确定权限变更尚未生效还是当前集成缺少所需授权；结果依旧是未重跑。不要将 PR #1 新检查成功当作 PR #2 的测试成功。

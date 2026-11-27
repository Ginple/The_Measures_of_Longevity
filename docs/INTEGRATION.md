# GitHub目录集成 / GitHub Repository Integration

## 独立目录作为仓库根

本包本身可作为仓库根。`pyproject.toml`、`src/`、`tests/`和`.github/workflows/ci.yml`路径已按此安排。这里只准备本地组件；当前工具查询GitHub连接返回unsupported，因此没有创建远端或push。

## 嵌入已有仓库

建议：

```text
your-repository/
├── README.md
├── methods/
│   └── research-assurance/   # 本包完整放这里
├── projects/
│   └── your-study/          # 真实项目账本和有许可的相对路径
└── .github/workflows/
    └── research-assurance.yml
```

GitHub Actions只发现根目录`.github/workflows/`，不会自动执行`methods/research-assurance/.github/workflows/`。将工作流复制到仓库根并给两个run步骤加：

```yaml
working-directory: methods/research-assurance
```

setup-python和checkout不是run步骤，不需要working-directory。真实项目数据应按权利与敏感性政策分开存储；不要因示例可公开就上传原始临床数据。

Agent Skill加载器的自动发现路径因宿主而异。本包`SKILL.md`和子Skill是内容合同，不宣称每个宿主都能直接自动安装。可按宿主要求复制／链接对应目录，同时保留指向docs和templates的可达路径与权限边界。

## 正式发布前

- 决定许可证与维护者，核第三方权利；当前未替用户决定。
- 修改示例Project Charter并创建新项目账本，不把toy supported判断当真实研究结论。
- `requirements-tested.txt` 为历史记录，不兼容当前Python 3.11 CI；新 [CI 依赖清单](../requirements-ci-py311.txt)只固定Linux/CPython 3.11的软件版本，未锁哈希或所有支持平台，详见[验证回执](../review/CI_DEPENDENCY_REPRODUCIBILITY_2026-11-27.md)。
- 保留session历史回执作为来源，不把缺旧目录时的“未复验”改成通过。
- 真实独立方法审阅／跨域试点仍欠；README必须继续暴露这一点。

# Research Assurance Toolkit — 0.1.1 candidate / 候选修订版

这是冻结0.1.0的**派生副本**，不是对原交付原位覆盖。原版README保留为 `UPSTREAM_0_1_0_README.md`；原版结果移至 `history/upstream_0_1_0_results/`，仅是旧运行记录，不是本轮输出。原版方法手册、session与交付文档是历史说明，涉及0.1.0测试数/交付路径/发布状态时不得当作本轮回执。

## 增量修复 / Patch

`core.inspect_project`现在检查supported断言与最低裁决维度的一致性：

|kind|本地合同最低维度|
|---|---|
|reported|source_support, extraction|
|descriptive|measurement, extraction|
|statistical|measurement, extraction, statistical_inference|
|causal|measurement, extraction, statistical_inference, causal_identification|
|transport|transportability|
|decision|net_benefit|

这是当前类型合同，不是通用证据等级。transport/decision不由程序隐含推断所有因果前提；复杂主张应拆分并显式链接其前提。该矩阵会使部分旧supported记录被拒绝：需要重审，不得自动把unknown改成supported来适配版本。

本修复只筛查内部不一致，无法保证判断内容为真。review身份与independence仍是声明，不是外部认证。

## 运行

从此目录：

```bash
PYTHONPATH=src python scripts/run_validation.py
```

建议从主工作台运行 `python tools/run_validation.py`，同时覆盖项目复杂输入与类型化数值/执行契约。本轮候选库56测试，加主工作台23测试；当前结果以主工作台 `artifacts/VALIDATION.json` 为准。

旧 `scripts/build_*`、toy生成器和历史session脚本不是验收前自动运行的步骤；不能重生成信任基线来掩盖失败。内嵌 `.github/`仅保留上游普通软件测试示例，不在主仓库根层，不会自动构成远端安全执法。见主工作台 `platform_adapters/README.md`。

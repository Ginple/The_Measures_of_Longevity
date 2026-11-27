# P3 评价合同：从 PR #2 选择性整合

2026-11-27｜改写自 [PR2 固定版本评价方案](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/papers/P3_research_assurance/EVALUATION_DESIGN_2026-11-27.md)。这是方案，不是已完成的独立盲测、项目发布批准或真实性检测。

## 两个不同目标

**字节和规则绑定是否失效**可按冻结合同与版本检查；**科学判断是否仍成立**需要领域审阅，hash 变更可以只是格式，hash 不变也无法排除新证据推翻。系统的拒绝或未知不能当通过；独立审查主体的身份和利益冲突不能由布尔字段自行证明。

## 防泄漏与对照

预先定义各基线能读取什么、操作规则、允许的输出及成本；同一项目、证据和近似变体按项目簇分配，避免开发集与终测集泄漏。测试集应含开发者未见项目与未见变异族；两名独立标注者先按冻结合同判断，记录分歧、仲裁与无法裁决的比例。语义标签不能全部由被测工具生成。来源版本、数据许可、路径与变异的审计材料须留档；当前未获得这些独立资源。

## 不把拒绝隐藏在分母外

对已裁决的 stale/valid 事实契约，输出 stale/valid/abstain；分别列 TP/FP/FN/TN 及两种 oracle 下的 abstain，并同时报告决定者中召回和把拒绝视为未检出的全部 stale 召回。分母为零报告未定义；按族与项目数分层，项目内相关性及真实基准率未知时，开发集 precision 不能直接解释为部署效果。另报人工复核成本和因拒绝而阻断的比例。含未裁决 oracle 的个案先单列，不能强制塞进真值。

[虚构示例与指标脚本](../../knowledge_base/experiments/assurance_benchmark_metrics.py)、[测试](../../tests/test_assurance_benchmark_metrics.py)仅检验计数合同。真实基准、目标与 oracle 需预注册并独立执行。

## PR2 七例开发回归，不是独立评测

择取自[固定 SHA 的设计](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/papers/P3_research_assurance/EVALUATION_DESIGN_2026-11-27.md)的[比较脚本](../../knowledge_base/experiments/assurance_fixture_comparison.py)及[测试](../../tests/test_assurance_fixture_comparison.py)，复制同一已知 toy 项目到临时目录，对七个开发者已知情景按自定义 oracle 比较路径存在、全文 hash、冻结片段、片段加记录绑定，以及 `inspect_project` 的一种映射；E 并非完整发布门。执行 `python knowledge_base/experiments/assurance_fixture_comparison.py` 可重放案例与计数。我们将 PR2 用来验证输入文本的 `assert` 改为显式异常，并测试普通和 `-O` 下缺失基线文本时失败。

指定 oracle 将引用段以外的追加标为 valid，因此 B 和 E 对它报 stale 在该**局部目标**下计为 FP；E 对全文件 hash 变更报警却符合其严格字节合同，不是实现错误。若目标是任意源文件变更须失效，oracle 与计数须更改，不能把两种目标混为一谈。缺失文件时 B/C/D 的 abstain 保留在分母中；开发夹具不是未见数据、独立标注、真实世界准确率或科学真实性评测。

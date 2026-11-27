# PCA 维数与多重检验：纯合成可运行反例

在仓库根目录运行：

```sh
python knowledge_base/experiments/multiplicity_pca_counterexample.py
(cd knowledge_base/experiments && python -m unittest -v test_multiplicity_pca_counterexample.py)
```

输入为 16 个双侧标准正态真零假设统计量；`X_i = sqrt(rho) Z + sqrt(1-rho) E_i`，公共因子 Z 和误差 E_i 相互独立、均标准正态。90% PCA 数按协方差/相关矩阵特征值直接计算。条件给定 Z 后，以标准正态 CDF 求无拒绝概率并用 Simpson 积分得到至少一次拒绝的概率。积分在 ±9 截断，测试对 ρ=0 核独立闭式解、对 ρ=.9 比较网格加密。无随机抽样及外部包。

这仅证明“把 90% 方差 PC 数作为 Bonferroni 分母”**不普遍保证** FWER≤0.05，不能估计任何真实研究的 FWER；标准 Bonferroni 保障还要求各真零检验 P 值有效。更多来源及论文原话与待核项见 [专项审计](../MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)。

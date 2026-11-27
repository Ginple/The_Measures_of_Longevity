# CALERIE 体重轨迹：补表舍入与条件分母

2026-11-27｜以 [PR #2 固定版本续审](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/knowledge_base/CALERIE_TRAJECTORY_MISSINGNESS_FIGSHARE_2026-11-27.md)为线索，重新核读 [Figshare v1元数据](https://api.figshare.com/v2/articles/31244800)、[S3补表可提取文本](https://ndownloader.figshare.com/files/61614040)、[体重轨迹论文 Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13094879/) 和 [同一母试验另一篇脂质报告的样本](https://pmc.ncbi.nlm.nih.gov/articles/PMC13482398/)；不声称首次取得S3，本分支此前已读并登记X60。这是同一助手定向核对，不是独立外审、作者回复、系统综述或患者数据重算。

## 条件算术

体重轨迹论文称分析190人：120限食、70对照。S3列基线胰岛素AUC缺失 **57（29.8%）**；以190为分母是30.0%（四舍五入一位小数）。这里不把两者不同直接判为错误：真实百分比生成过程及其总体未确认。

**如果假定**表中该行的百分比来自 `100×57/N`，`N` 为正整数，采用最接近的0.1个百分点舍入，则放宽两个舍入边界均包含的条件可得：

`29.75 ≤ 5700/N ≤ 29.85`，即 `5700/29.85 ≤ N ≤ 5700/29.75`。

端点约为190.955和191.597，因此在所有正整数中只有 **N=191** 可满足这个必要条件。`57/191×100≈29.843%`，离29.8足够近，并非舍入平局。S3其他抽核行（包括葡萄糖AUC和其他变量、不同时间点）的数字在同一191及该舍入约定下也相容，见[脚本](experiments/rounded_percentage_denominators.py)。这只是“这些摘要数字与191相容”，**不证明研究真实使用191人、其人群身份、混合模型分母或缺失原因**；不同舍入方式、预处理、分母或转录与定义都需核查。即使所有行都相容一个N，也不能因此证明所有行用相同样本。

[另一篇2026 CALERIE代谢组报告](https://pmc.ncbi.nlm.nih.gov/articles/PMC13482398/) Results 的最终分析样本为191人（120限食、71对照），但这只是同一母试验另一分析中的数字；没有参与者映射，不能推断它与S3分母是同一批人，也不是独立复制。两篇论文目标、纳入及数据流可能不同，不能把其他论文的组人数静默套入本表。

## 与完整记录界的关系

在单一固定总体、3个时间点各自缺失数57、33、6且均针对**同一变量及同一批N人**的额外假设下，[既有集合界](experiments/COMPLETE_CASE_BOUNDS_CALERIE_2026-11-27.md)为 `max(0,N−57−33−6)` 到 `N−57`：

| 假定总体 | 三时点全有值的条件界 | 解释 |
|---|---:|---|
| N=190 | 94–133 | 正文190人不证明这些缺失数在同一总体。 |
| N=191 | 95–134 | 与舍入算术相容，不证明表实际使用191。 |

每个界的上下端在其**各自**假设下可构造；不应将它们当实际完整例数、有效配对数或混合模型样本数。混合模型可以使用部分时点，缺失交集和机制也无法从边际数确定；不存在从这些界直接推断效应方向或大小的依据。X59（轨迹阈值与随机后选择）、X60（分母和FDR）和X72（组内与交互模型口径）继续开放，须核作者数据字典、各时间/各组数据流、模型和代码、补表可视版本及作者说明。

## 工具边界

[精确分数计算器](experiments/rounded_percentage_denominators.py)与[测试](experiments/test_rounded_percentage_denominators.py)择取自PR2固定头对应[脚本](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/knowledge_base/experiments/rounded_percentage_denominators.py)和[测试](https://github.com/Ginple/The_Measures_of_Longevity/blob/b8434e22ec62ba21814546560a33fc38f4939e9f/tests/test_rounded_percentage_denominators.py)，并补空观测拒绝、纯十进制输入校验、交集和不相容行测试。输入为转录的汇总计数与显示百分比，不包含身份或原始记录。程序在给定**有限闭区间**枚举候选，同时对舍入平局两侧都保留，因此候选可能是某种具体平局规则下的保守超集；空候选仅说明给定范围和规则下无解。57（29.8%）的全正整数唯一性来自上面的解析不等式，不依赖程序的1000搜索上限。

运行 `python knowledge_base/experiments/rounded_percentage_denominators.py`，测试 `python -m unittest discover -s knowledge_base/experiments -p test_rounded_percentage_denominators.py`。软件测试是条件算术回归，不能确认来源真实分母、排除作者使用其他口径或完成科学认证。

# 下轮真实数据接收合同 / Next-Round Data Acceptance Contracts

这不是声称数据已收到。目标是让取得数据后的第一个动作有确定判别标准，而不是再次漫无边界地搜索或生成报告。阈值／功效需领域专家预先确定，以下不填虚构数值。

## A. D03／D09：真实轨迹、度量与死亡资格

### 最小合法包 / Minimum Legitimate Package

1. **分组与全基线登记**：donor_id、batch_id、treatment、field_id、baseline_founder_id、入组时间／排除及理由。不能只提供成功可追踪者。
2. **轨迹表**：track_id、baseline_founder_id（及真实链接证据）、frame/time、detection_id、parent_id、名义cluster_id或实际连续feature向量、观测状态。
3. **事件表**：observed/lost/left_field/occluded/segmentation_failure/divided/death_confirmed及独立参考来源；未知原因保留unknown。
4. **模型切分映射**：donor/batch/field/cell/time→train/validation/final_test；最终测试是否参与模型选择／早停。
5. **度量／预处理说明**：实际响应CSV、列意义、是否原簇编号、缺失编码、距离、Ward实现和参数、版本。
6. **独立参考**：逐事件死亡／身份复标、复标者盲态与不确定性；与形态模型独立的实测功能终点及自然老化桥接（若目标是返老）。

### 入库即查 / Intake Checks

- ID唯一性／外键，时间顺序与单位；baseline不随后续可测性重新定义。
- 后代不能默认为独立原细胞；分裂后的目标估计量需预先声明。
- lost_unknown不能填death_confirmed，0不能同时代表真实簇与缺失。
- 若输入是名义ID，预设重编码集合做不变性挑战；不变性成立后仍需测量／生物学验证。
- 样本n分层报告：供者、批次、视野、founder、检测、时间点；不可互换。
- 数据未覆盖自然老年目标域时，不把年轻诱导模型外推写成已证实。

### 第一轮实际分析 / First Analysis When Data Arrive

核完整性→固定基线分母→观测／未知事件分开→按真实group评估追踪／死亡代理→实际特征与名义编码对照→稳定性和误差→再讨论生物响应。只做这一步需要的分析，不先堆复杂模型。

**关闭边界**：收到CSV不等D09关闭；证明名义距离问题影响实际结果才可量化改变；独立死亡与功能真值、目标域桥接仍各自未偿。

## B. D04／D08／D10：图点到实际测量链

必须字段：fig_panel、variant_index、donor/cell_line、POS、REF、ALT、assay、library/sample_id、analysis_set/QC、raw_or_processed_path、value_scale、HF、作图统计量与版本hash。

接受前核对：
- `(panel, variant_index)`是否唯一且覆盖源表所有点；不能只给好匹配的行。
- 不同assay是否真来自可比较单位；源表点n不当供者n。
- 补充表已有sample metadata，不代表上述键已自动齐全。
- copy number/capture权重和样本选择是否与目标估计量一致。
- 作者实际执行版本、环境、函数return和shell问题处理记录；区分公开示例、归档与实际运行版本。
- 原始数据许可与访问资格真实可用；不根据相近HF、行顺序或共享供者名字猜测crosswalk。

首分析先按作者给定定义原样复算，再做明确标注敏感性。不删除index83或挑变换使r／r²接近图值。无法解释的冲突继续open。

## C. D02：LoDoCo2源冲突闭环

需要正式更正、作者／统计维护者解释或原模型输出，明确CI方向、估计量、分析集、780／783对应口径。注册current或“查不到更新”不满足关闭。没有新事实触发时不反复相同查询制造进度。

## D. D05／M01：独立审阅接收

真实独立责任人、版本范围、独立取源／复标／复算、意见、回应及必要复审。对本研究与对通用方法的审阅分别记录；不能让一个局部代码审查签字变成整本书或整个方法框架认证。请求目前全部未发送／未签收。

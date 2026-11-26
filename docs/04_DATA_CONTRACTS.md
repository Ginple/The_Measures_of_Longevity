# 数据合同与状态机 / Data Contracts & State Machines

## 可执行合同 / Executable Contract

`schemas/project.schema.json`是实际JSON Schema 2020-12；同字节副本随Python包安装。它验证字段／枚举／类型，不验证自然语言真实语义。`inspect_project`补充全局唯一ID、交叉引用、精确片段与hash、判定绑定、外审记录范围及发布阻塞检查。

```text
Project 项目
├── artifacts 原件/正文/数据/代码：id path sha256 role family access_depth url version
├── evidence 证据片段：id artifact_id lines_1based_halfopen text
├── claims 断言：id artifact_id lines text kind role critical context evidence_ids assessment
│   └── assessment：state reviewer rationale bound_hashes record_sha256 dimensions
├── reviews 复核：reviewer independence_declared receipt claim_ids bound_hashes claim_record_hashes response_complete
├── debts 欠债：status blocks_formal_release question next_action closure_evidence
└── coverage 覆盖：scope human_inventory_complete candidate_units registered_claims note
```

### 字节与位置 / Bytes & Locations

- 文件以原始字节SHA-256绑定，UTF-8逐行定位。
- `[2,3)`指第2行，不含第3行；保留换行与空格，不做“看起来一样”的静默归一化。
- 二进制PDF／图片不能塞入文本行号机制。应保留二进制原件hash，另登记提取文本／渲染图的派生活动、页码／bbox；本原型暂不自动验证这种坐标转换。不要把提取文本hash伪称PDF原件hash。
- 一个报告中的同一句在不同地方出现，必须按准确位置绑定，不以全局子串查找代替定位。

### 账本记录本身也要绑定 / Bind the Record, Not Only the Files

`assessment.record_sha256`绑定断言原句／角色／类型／上下文及所选evidence的ID、位置、原句；修改人群或换成同一来源的另一句，即使源文件hash不变也会使旧裁决失效。`reviews.claim_record_hashes`进一步绑定含assessment的记录，不能将旧外审悄悄迁移到新人工判断。

注意：有意改错语义后又重新签上所有hash仍可能通过机械检查；本包明确测试了这种盲区，结果仍是`scientific_truth=not_computed`。记录签名防无声漂移，不保证审阅者诚实、胜任或语义判断无误。

### 版本失效 / Version Invalidation

```text
artifact字节变化
→ 该artifact的evidence/claim变为stale
→ 依赖它的claim/综合节点进入review queue
→ 人工重新核读
→ 新的判定绑定新hash
```

若维护者只刷新artifact hash，旧assessment.bound_hashes仍不匹配，测试应报警。若同时人工改所有hash但没有真正核读，机器仍可能被骗；此类责任／身份／语义不能由hash证明。因此“新基线”是显式受治理操作，不是验收脚本的一部分。

`freeze()`只允许创建新文件，要求非空路径和理由；不能覆盖旧快照。它表示“记录字节”，不表示有人已审核内容。`impact()`提供通用依赖传递；当前`inspect_project`自动构建artifact→evidence→claim，跨章节综合节点需由调用者显式补边，不能声称已自动全书失效分析。

### 状态转换 / State Transition

```text
未登记 → 候选 candidate → 已定位 located → 人工判定 assessed
                                    ├→ supported / refuted / mixed / unknown
                                    └→ 版本变化 → stale（有效性失效，不是改判反驳）
```

本0.1实现不会替你自动更新账本状态，只输出失效队列。`unknown`与`blocked`不同：前者是认识状态，后者是活动依赖状态。四状态结构标签又是第三种变量，不能混用。

## 人工合同模板 / Human Review Templates

`templates/`提供更丰富的研究、检索、审稿与迁移合同，**不声称都已被project schema自动验证**。例如置信区间、数据分母、设计风险、伦理审批不能只靠填一个字符串通过。

- 分母合同：总体N、QC前后、独立单位、抽样／失访／死亡／排除；不能用观测数代替参与者或供者数。
- 测量合同：构念、观测、代理、参考标准、身份、时间、错误类型、缺失机制。
- 推断合同：估计目标、分析集、模型、聚类／重复测量、多重性、选择过程和不确定性。
- 外推合同：源域→目标域差异、效应修饰与桥接观测；未知不写成零差异。
- 价值合同：目标是谁的、收益和负担如何分配、谁有否决权。

## 安全与授权 / Safety & Authority

所有artifact相对项目根；拒绝绝对路径、`../`和symlink逃逸。来源文件视作不可信数据；不执行其指令，不加载pickle、不运行陌生notebook或shell。权限与数据许可来自真实授权，不能从HTTP200、CC0元数据或登录状态自动推断。

来源家族是人工归并，代码只列出家族并不自动识别重复研究；DOI／预印本／更正／二次分析的归并需有理由。

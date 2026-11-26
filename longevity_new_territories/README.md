# 谁在为年轻买单？ / Who Pays for Rejuvenation?

LONGEVITY新领域研究增补：**接收端容量、体细胞进化与干预顺序**。

## 从哪里读

1. [中文主报告](谁在为年轻买单_新领土研究.md)：核心问题、实证/复算/模型/假说四层与Known/Unknown Unknowns。
2. [最小判别实验](docs/最小判别实验_从矿脉到可证伪问题.md)：优先实验、否证条件与统计单位。
3. [推导和可识别性](docs/模型推导与可识别性.md)：容量边界、顺序差异及负对照。
4. [近邻先例](docs/近邻文献与新颖性边界.md)：哪些思想已有、窄问题剩在哪里、实际读取范围。
5. [失败与限制](docs/SOURCE_FAILURE_AND_LIMITS.md)：保留失败，未改源值。

## 这个仓库组件是什么？

- **研究框架 / framework**：把源端功能、接收端终端处理、相对适应性与宿主功能分开；不是统一衰老定律。
- **研究工具包 / toolkit**：附脚本、真实源表、逐单元格导出、模型反例与实验判别提案。
- **计算引擎 / engine（局部）**：两个脚本是可复算模块，不是已验证的预测引擎；无实际寿命或治疗排序输出。
- **Skill层 / reusable skill pattern**：源表前固定问题→近邻反驳新颖性→最小反例→可证伪实验。这是可复用流程说明，不假称已部署Agent Skill或模型路由器。

不强制选一个类别；本包的主要定位是**研究增补 + 可复算工具包**。

## 复算

Python 3.11+建议；实际依赖版本见requirements.txt。仅需本地源表，不需网络、密钥或连接应用。

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python scripts/source_reanalysis.py
OPENBLAS_NUM_THREADS=1 python scripts/mechanistic_countermodels.py
```

从本目录或任意cwd调用均可，脚本按自身位置定位。脚本会覆盖同名results/figures产物；复现前可另存原目录。解压后若移动整个目录，保持内部结构。外部网页下载未包装成自动重试器：原下载限制和真实收据保留，避免再次把HTML挑战页误作xlsx。

输出：SOURCE_*为真实公开源表的描述复算；SYNTHETIC_*为人为无量纲模型。COUNTERMODELS.json含14项实现检查；它们只检查代码和指定数学性质，不等于生物学验证或独立外审。

## 实际目录

完整逐文件目录见[FILE_INDEX.txt](FILE_INDEX.txt)，校验见MANIFEST.sha256。

```text
longevity_new_territories/
├── README.md
├── 谁在为年轻买单_新领土研究.md
├── RESEARCH_COMMITMENT_BEFORE_SOURCE_VALUES.md
├── requirements.txt
├── FILE_INDEX.txt
├── MANIFEST.sha256
├── scripts/
│   ├── source_reanalysis.py
│   └── mechanistic_countermodels.py
├── data/       # 3份成功获取的出版方xlsx
├── docs/       # 推导、实验、近邻、局限、实际阅读摘录
├── results/    # 真实复算/人工模拟分开命名，保留首次失败日志
├── figures/    # 3幅PNG；模型明确标SYNTHETIC
├── sources/    # 原响应.raw与文本；包括失败响应，不等同已读全文
└── metadata/   # 获取收据、边界和自查记录
```

## 证据边界

已读源值前写问题承诺不等于注册研究方案；额外ApoB是追加描述。三篇源表的特定面板复算不等于完整研究独立复现。无新实验、寿命结论、人体建议、全新理论认证或完整V8。未修改历史冻结包；未push、未写任何外部应用；无新HTML。

**独立外审未完成，正式专著合成/论文投稿前仍须外部审查。** 本次交付仅为研究工作稿与复现材料。本助手自查与成功执行不能替代独立性。

## 日期与记录

会话本地日期按提供的上下文采用2026-11-25；沙箱文件mtime显示11-26，不据此改写会话日期。旧冻结文件不回写。此前续写记忆中将11-26称为实际日期的说法不作为来源时间证据。

## GitHub与权利

用户自行建库；本目录可作为子目录纳入。研究文字与脚本尚未指定开源许可，不自动宣告第三方原文/源表可再许可。sources/data保留供核查，不建议未经许可审查直接将所有缓存公开；公开仓库宜以出版方链接、取得说明、允许再分发的材料为准。403/429响应不是文献副本。没有代用户选择许可证。

## 中英关键词 / Bilingual keywords

长寿 longevity；器官—个体利益冲突 organ–organism fitness conflict；接收端容量 recipient capacity；终端处理通量 terminal processing flux；体细胞进化 somatic evolution；克隆造血 clonal haematopoiesis；生态位 niche；相对适应性 relative fitness；细胞间线粒体转运 intercellular mitochondrial transfer；有益异质性 beneficial heterogeneity；胞葬 efferocytosis；干预顺序 intervention ordering；非交换性 non-commutativity；进化稳健年轻化 evolution-aware rejuvenation；可证伪假说 falsifiable hypothesis。

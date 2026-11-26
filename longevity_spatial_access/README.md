# 有余量，却用不上 / Inaccessible Reserve

LONGEVITY小型研究增补：空间可达性、局部瓶颈，以及离体细胞测定可能遗漏的原位维护问题。

主文：[有余量却用不上_空间可达性的研究盲点.md](有余量却用不上_空间可达性的研究盲点.md)。

## 定位

这是研究框架的一项可复算增补，不是新平台、统一理论或已部署Skill。源表描述、标准最大流反模型与实验提案分层；不冒称新实验或已发现年轻化治疗的失败。

## 复算

```bash
OPENBLAS_NUM_THREADS=1 python analyze.py
```

依赖numpy、pandas、scipy、matplotlib；复用前轮环境与版本，不新增大型依赖。脚本按自身位置定位，在任意cwd运行；会覆盖同名计算输出。

23项实现检查通过；移目录执行后5份数值CSV/JSON逐字节一致。它们是助手自查，不是独立外审或生物学验证。

## 真实源表与人为模型

- `SOURCE_*.csv`：出版方两份小CSV的描述统计，带复制层级；悬液对照只有技术重复，不能变成动物n。
- `SYNTHETIC_*.csv`与`spatial_counterexample.png`：人为网络，不拟合生物数据。
- `RESULTS.json`：分开的源表差异、网络参数、流量/最小割和模型限制。
- `BEFORE_VALUES.md`：读新源值前固定的范围；已知定性结论，不是盲分析或预注册。

## 目录

```text
longevity_spatial_access/
├── README.md
├── 有余量却用不上_空间可达性的研究盲点.md
├── BEFORE_VALUES.md
├── analyze.py
├── data/                         # 两份小CSV、两张出版方原图（核轴用）
├── ACQUISITION.json              # CSV URL、状态、SHA-256
├── CAPTION_ACQUISITION.json      # 网页壳与API成功获取的区别
├── FIGURE_CAPTIONS_READ.txt
├── fig6_API_EXCERPT.json
├── fig6s2_API_EXCERPT.json
├── METHODS_READ_EXCERPTS.json    # 相关图注与方法，不冒充全文通读
├── SOURCE_SUMMARIES.csv
├── SOURCE_VALUES_LONG.csv
├── SYNTHETIC_BRIDGE_SWEEP.csv
├── SYNTHETIC_NETWORK_ARCS.csv
├── RESULTS.json
├── spatial_counterexample.png
├── SELF_CHECK.json
├── RUN.log
└── RUN.stderr
```

不新建HTML，不重打大ZIP，不覆盖前轮冻结包。出版方原图/源表保留供个人研究核查，公开仓库发布前须核来源许可与署名要求；不自动替用户选择开源许可。

**独立外审仍未完成，不能正式合成进专著。** 优先外审问题：源表层级是否正确；空间操作能否与识别/终端处理分离；“分离细胞测定遗漏空间瓶颈”的具体年轻化应用是否已有直接先例。

## 中英关键词

空间可达性 spatial accessibility；不可达余量 inaccessible reserve；局部瓶颈 local bottleneck；驻留巨噬细胞 tissue-resident macrophage；触附运动 haptokinesis；组织巡查 tissue surveillance；最大流—最小割 max-flow min-cut；原位—离体错配 in situ–ex vivo mismatch；终末处理 terminal processing；可证伪实验 falsifiable experiment。

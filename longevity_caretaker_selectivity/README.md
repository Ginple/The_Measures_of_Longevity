# 清除者，也在靶标里 / When the Caretaker Is Also a Target

LONGEVITY小型研究增补：功能选择性、维护能力保留，以及正确靶向但未必净获益的清除干预。

主文：[清除者也在靶标里_保留维护能力的年轻化.md](清除者也在靶标里_保留维护能力的年轻化.md)

## 本轮与前轮不同

重点是对读原始获益/反例文献，并提出有识别力的实验；没有再次下载源表或复制网页/PDF，也没有把新计算例子当作新实证。

- 2014 phagoptosis、2017标记可逆性、2020 p16High内皮清除；
- 2025 uPAR CAR-T肠道获益与2026 GFD构建的暴露相关毒性/获益；
- 严格区分识别特异性、细胞状态与宿主功能；
- 提议同时测源输入变化与维护能力，而非只测标记下降。

论文构建、组织、效应时间不同，不作为简单的直接复现冲突。实际阅读仅限READING_RECORD记录的摘要/正文部分，不声称全文Methods/SI通读。

## 计算

`python condition_check.py`，仅Python标准库，无额外安装。人为无量纲参数，未拟合生物数据；a是输入通量减少比例，b是有效容量损失比例，都不是细胞清除百分比。

8项代数实现检查及110个精确有理数参数组合通过。代码只验证条件恒等式，不预测药效、安全阈值或寿命。

## 目录

```text
longevity_caretaker_selectivity/
├── README.md
├── 清除者也在靶标里_保留维护能力的年轻化.md
├── READING_RECORD.md
├── condition_check.py
├── SYNTHETIC_CONDITIONS.json
├── SYNTHETIC_EXAMPLES.csv
├── SELF_CHECK.json
├── RUN.log
└── RUN.stderr
```

定位：已有研究框架中的小型证据/实验设计工具包；不是新引擎、已部署Skill或统一理论。独立外审未完成，不做正式专著合成。未选开源许可证、未写外部应用；没有HTML、大附件或新ZIP。

## 中英关键词

功能选择性 functional selectivity；维护保留 maintenance preservation；照护细胞 caretaker cells；靶点正确组织错误 on-target off-tissue；吞噬性细胞死亡 phagoptosis；清除衰老细胞 senolysis；肝窦内皮 liver sinusoidal endothelium；标记可逆性 marker reversibility；替代能力 replacement capacity；可撤回性 reversibility of intervention；抗原特异性 antigen specificity。

# 平均未超载，为什么仍会积压？
## Beyond Mean Capacity

上一轮“谁在为年轻买单？”的小型研究续篇；不修改旧包，不复制源表/网页缓存，不新增大ZIP。

主文：[研究增补](平均未超载_为什么仍会积压.md)。

实际目录：
```text
longevity_capacity_timing/
├── README.md
├── 平均未超载_为什么仍会积压.md
├── pulse_counterexample.py
├── RESULTS.json
├── SYNTHETIC_PULSE_TRACES.csv
├── pulse_counterexample.png
├── RUN.log
└── RUN.stderr
```

运行：`OPENBLAS_NUM_THREADS=1 python pulse_counterexample.py`。依赖numpy、pandas、scipy、matplotlib；本轮复用前轮已验证环境，不新增大型库。运行覆盖同名计算输出。

21项实现检查通过；全部参数人为无量纲，无生物拟合、剂量或人体建议；独立外审未完成。数学上使用已有凹函数/Jensen结果，不申报新定理；新研究问题是具体细胞接收端的处理余量是否依赖任务历史与输入节律。

关键词：处理余量 processing reserve；脉冲负荷 pulsed load；连续胞葬 continual efferocytosis；接收者状态 recipient state；饱和处理 saturating processing；适应与占用 adaptation versus occupancy；平均滞留 mean backlog；峰值暴露 peak exposure；可证伪机制 falsifiable mechanism。

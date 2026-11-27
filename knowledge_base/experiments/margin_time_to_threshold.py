"""余量换算为时间：线性下降与比例下降两种模型的对照（合成算例，不是个体预测）。

性质：描述性代数加公开参数的算例，不是观察结果，也不是干预效果估计。

公开参数（核读深度见 CLAIM_LEDGER X129–X131）：
- 阈值 T：Paterson 等 1999（MSSE 31:1813，摘要）给出 85 岁时与独立生活相容的最低有氧能力，
  男性约 18、女性约 15 mL/kg/min。这是"仍独立者"的下包络，不是测得的失效阈值。
- 线性下降 b：同一研究的横断面斜率，男性 0.31、女性 0.25 mL/kg/min/年（55–86 岁）。
- 比例下降 r：Fleg 等 2005（Circulation 112:674，摘要）的纵向估计，70 多岁时每 10 年下降 >20%，
  且各身体活动四分位的速率相近。取 r = -ln(0.8)/10 ≈ 0.0223/年；因为原文是 ">20%"，所以这是 r 的下界，
  由它算出的剩余年数是比例模型下的上界。

比例模型 V(t) = V0·exp(-r t)：剩余年数 = ln(V0/T)/r。由此可得：
- 水平提高到 g 倍，增加 ln(g)/r 年，与当前离阈值多远无关；
- 速率降低比例 c，增加 t·c/(1-c) 年，与剩余年数 t 成正比；
- 两者相等的位置是 t* = ln(g)(1-c)/(c·r)。
"""
from __future__ import annotations

import json
import math

T_MEN = 18.0
B_LINEAR_MEN = 0.31
R_PROP = -math.log(0.8) / 10.0


def years_linear(v0: float, threshold: float = T_MEN, b: float = B_LINEAR_MEN) -> float:
    if v0 <= threshold:
        return 0.0
    return (v0 - threshold) / b


def years_proportional(v0: float, threshold: float = T_MEN, r: float = R_PROP) -> float:
    if v0 <= threshold:
        return 0.0
    return math.log(v0 / threshold) / r


def gain_from_level(g: float, r: float = R_PROP) -> float:
    return math.log(g) / r


def gain_from_rate(t: float, c: float) -> float:
    return t * c / (1.0 - c)


def crossover_years(g: float, c: float, r: float = R_PROP) -> float:
    return math.log(g) * (1.0 - c) / (c * r)


def run() -> dict:
    rows = []
    for v0 in (20.0, 25.0, 30.0, 35.0):
        t_prop = years_proportional(v0)
        rows.append({
            'V0': v0,
            'years_linear_cross_sectional': round(years_linear(v0), 1),
            'years_proportional_longitudinal_upper': round(t_prop, 1),
            'gain_level_plus10pct': round(gain_from_level(1.1), 1),
            'gain_rate_minus10pct': round(gain_from_rate(t_prop, 0.1), 1),
        })
    plus10 = {
        'claim': 'Shephard 类表述：训练使 VO2max 提高约 10 mL/kg/min，可推迟失去独立最多约 20 年',
        'from_V0': 25.0,
        'years_linear': round(years_linear(35.0) - years_linear(25.0), 1),
        'years_proportional_upper': round(years_proportional(35.0) - years_proportional(25.0), 1),
    }
    return {
        'nature': 'synthetic algebra with published parameters; not an individual prediction',
        'r_proportional_per_year': round(R_PROP, 4),
        'grid_men': rows,
        'crossover_years_g1.1_c0.1': round(crossover_years(1.1, 0.1), 1),
        'shephard_plus10_check': plus10,
    }


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))

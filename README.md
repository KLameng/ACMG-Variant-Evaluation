# ACMG-Variant-Evaluation · 单基因病点突变 ACMG 评级技能群

一套用于**孟德尔疾病相关基因序列变异 ACMG/AMP 致病性分类**的可复用技能包。基于 ACMG/AMP 2015 框架，覆盖单基因病点突变评级的完整证据码流程。

## 简介

- **23 个技能**，含 `acmg-total-scheduler`（总调度层 / 唯一入口）与 `ev-*` 证据码子技能（PVS1/PS1-PS4/PM1-PM6/PP1-PP4/BS1-BS4/BP1-BP7 等）。
- 变异身份归一化 → 遗传方式前置判定 → 逐证据码判定 → 收尾层证据方向一致性 + 累分衔接校验。
- 判据外置：证据码规则集中管理，改判据不动流程，加案例不动代码。
- 互斥矩阵只存在于收尾技能 `acmg-conflict-summary-output`，各 `ev-*` 子技能不携带证据互斥内容。

## 软件架构

```
acmg-total-scheduler/          # 总调度层（唯一入口）
  ├── SKILL.md                 # 强制流程：变异归一化 → 遗传方式前置 → 逐码判定 → 收尾
  └── references/              # 判据与规则数据
ev-*/                          # 证据码子技能（PVS1 / PS1-PS4 / PM1-PM6 / PP1-PP4 / BS* / BP*）
acmg-conflict-summary-output/  # 收尾技能：互斥矩阵 + 证据方向一致性
config/                        # golden / thresholds 配置
scripts/                       # 辅助脚本
```

## 快速开始

1. 从 `acmg-total-scheduler/SKILL.md` 进入（唯一入口）。
2. 按强制流程走完：变异身份归一化 → 遗传方式前置判定 → 逐证据码判定 → 收尾层累分衔接。
3. 涉及单病变异评级，先走 `acmg-total-scheduler` 评级群。

## 参与贡献

欢迎提交脱敏变异案例与评审意见，帮助 ratify 证据码判据。详见各技能目录 `CONTRIBUTING.md`。

## 许可

- 许可证：**Apache License 2.0**，版权署名 **KLameng**。详见 `LICENSE`。
- 维护者：**KLameng** · 联系邮箱：**911712412@qq.com**

---

*Copyright (c) 2026 KLameng <911712412@qq.com> · Released under Apache-2.0.*

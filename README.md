# 单基因病点突变 ACMG 评级技能群

给单基因病相关基因序列变异做致病性分类的完整技能群，基于 ACMG/AMP 2015 指南与 ClinGen 共识。

## 技能群结构

| 技能 | 作用 |
|---|---|
| `acmg-total-scheduler` | 总调度层（唯一入口）——评级任何变异都从这里开始 |
| `acmg-conflict-summary-output` | 收尾层——证据互斥矩阵消解冲突，输出最终评级 |
| `arad-inheritance-judgment` | AR/AD 遗传模式判断 |
| `ev-variant-standardization` | 变异身份归一化 |
| `ev-disease-info` | 疾病表型/外显率/发病率检索 |
| `ev-gene-identity` | 基因别名/假基因核实 |
| `ev-gnomad-constraint` | gnomAD 基因约束指标查询 |
| `ev-pvs1` | PVS1 非常强致病证据（LOF） |
| `ev-ps1-pm5` | PS1/PM5 错义证据 |
| `ev-ps2-pm6` | PS2/PM6 新发变异证据 |
| `ev-ps3-bs3` | PS3/BS3 功能实验证据 |
| `ev-ps4` | PS4 病例对照频率证据 |
| `ev-pm1` | PM1 热点区域证据 |
| `ev-pm2` | PM2 等位基因频率证据 |
| `ev-pm3` | PM3 反式位置致病变异证据 |
| `ev-pm4` | PM4 蛋白长度变化证据 |
| `ev-pp1` | PP1 共分离证据 |
| `ev-pp2` | PP2 错义为主致病机制基因证据 |
| `ev-pp3-bp4` | PP3/BP4 计算机预测证据 |
| `ev-pp4` | PP4 表型高度符合证据 |
| `ev-bs1-bs2` | BS1/BS2 强良性证据 |
| `ev-variant-literature-patient` | 携带该变异的患者文献检索 |
| `clingen-vcep` | ClinGen VCEP 知识库（基因特异性评级标准） |

## 使用方式

在豆包工作模式里安装本技能群，然后输入一个变异（如"BRCA1 c.5266dupC"），技能群会自动走完：
1. 变异身份归一化
2. 遗传方式前置判定
3. 各证据码逐码判定
4. 证据互斥矩阵消解
5. 输出最终评级（致病/可能致病/意义不明确/可能良性/良性）

## 许可

Creative Commons Attribution 4.0（CC BY 4.0），署名 **KLameng**。

---

*Copyright (c) 2026 KLameng <911712412@qq.com> · Released under CC BY 4.0.*

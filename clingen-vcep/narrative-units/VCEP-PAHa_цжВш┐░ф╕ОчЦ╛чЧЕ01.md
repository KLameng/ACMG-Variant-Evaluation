> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN006 — Phenylketonuria Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0009861**（遗传方式：未指定）

### 通用说明
            Version 2.0

### 不适用证据码
PS4、PM6、PP2、PP5、BP1、BP2、BP3、BP6
### 附件关键数据

#### PP3 REVEL评分详细说明（PAH PP3 REVEL data explanation）

**PAH变异REVEL评分分布：**

| REVEL评分范围 | 变异数量 | 分类分布 |
|-------------|---------|---------|
| ≥0.932 | 151个 | 32 P, 70 LP, 49 VUS |
| 0.773-0.932 | 91个 | 26 P, 41 LP, 24 VUS |
| 0.644-0.773 | 30个 | 2 P, 12 LP, 16 VUS（仅5个应用PP3） |
| <0.644 | 30个 | 8 P, 7 LP, 14 VUS, 1 LB（仅2个应用PP3） |

**PP3应用建议：**
- REVEL ≥0.932：强烈建议应用PP3_Strong
- REVEL 0.773-0.932：建议应用PP3_Moderate
- REVEL 0.644-0.773：谨慎应用PP3，需结合其他证据
- REVEL <0.644：通常不应用PP3

#### PS3功能检测数据（PAH PS3 functional data）

**已批准的功能检测方法：**

| 检测方法 | PMID | 建议强度 |
|---------|------|---------|
| 重组PAH在大肠杆菌中表达，测定苯丙氨酸羟化为酪氨酸的酶活性 | 18477464 | PS3_Supporting |
| 位点定向突变分析（如Y179F、Y179A） | 14999516 | PS3_Supporting |
| 人PAH cDNA突变体构建与酶动力学分析 | 15917086 | PS3_Supporting |
| 大鼠PAH活性位点残基突变分析 | 12733906 | PS3_Supporting |
| PKU诱导突变体（Arg158Gln、Glu280Lys）功能分析 | 11368310 | PS3_Supporting |

**关键PAH变异功能数据阈值：**
- PS3_Strong：PAH酶活性 <10% WT
- PS3_Moderate：PAH酶活性 10-25% WT
- PS3_Supporting：PAH酶活性 25-50% WT
- BS3_Strong：PAH酶活性 >85% WT

**重要功能域残基：**
- 活性位点残基：Tyr138, Arg158, Val245, Tyr268, Thr278, Pro279, Glu289, Ala300, Asp315, Phe331, Ala345, Gly346, Ser349, Tyr377
- 底物结合残基：46-48, 63-69

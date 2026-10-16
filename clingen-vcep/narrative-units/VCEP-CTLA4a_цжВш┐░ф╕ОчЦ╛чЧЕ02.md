> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

| 表型符合基因但非高度特异且遗传异质性高 | 0.5分 | 0.25分 |
| 表型不符合基因 | 0分 | 0分 |

| 证据强度 | 积分阈值 |
|---------|---------|
| PS2_Very Strong / PM6_Very Strong | ≥2分 |
| PS2_Strong / PM6_Strong | ≥1分 |
| PS2_Moderate / PM6_Moderate | ≥0.5分 |
| PS2_Supporting / PM6_Supporting | ≥0.25分 |

#### 功能检测关键数据（CTLA4 Functional Assay Research PS3 BS3）

**PS3_Strong批准检测：**
- OddsPath >18.7的体外检测异常结果

**PS3_Moderate批准检测：**
- ≥11个总对照变异（包括致病和良性）的体外检测异常结果

**PS3_Supporting批准检测（基于非患者细胞）：**
1. CD80或CD86反式内吞/可溶性CD80或CD86配体摄取
2. 细胞表面CTLA4表达
3. 蛋白质定位/转运
4. 体外T细胞抑制

**关键计算器阈值：**
- PP3阈值：REVEL >0.75，CADD PHRED >20
- BP4阈值：REVEL <0.25，CADD PHRED <20
- SpliceAI阈值：<0.1（无剪接影响）

# VCEP知识库核实报告

> 完成日期：2026-06-14
> 核实范围：SCN8A深度核实 + 5基因抽检
> 数据来源：ClinGen CSpec官网（cspec.genome.network）+ 本地知识库文件

---

## ⚠️ 重大发现：GN编号与基因名称严重错配

在执行抽检任务时，发现**用户提供的5个GN编号全部与指定基因不匹配**。这是一个系统性错误，影响整个抽检任务的可执行性：

| 用户指定基因 | 用户指定GN编号 | 实际GN编号对应的基因/规范 | 该基因的正确GN编号 |
|-------------|---------------|------------------------|------------------|
| MYBPC3 | GN055 | **MYO7A**（Hearing Loss VCEP） | **GN095**（Cardiomyopathy VCEP） |
| COL1A1 | GN021 | **ACADVL**（ACADVL VCEP） | ❌ 无VCEP规范 |
| TSC2 | GN106 | **RPGR**（X-linked IRD VCEP） | ❌ 无VCEP规范 |
| BRCA2 | GN005 | **CDH23/COCH/GJB2等9基因**（Hearing Loss VCEP） | **GN097**（ENIGMA VCEP） |
| LMNA | GN049 | **BRAF**（RASopathy VCEP） | ❌ 无VCEP规范 |

**影响**：
- 按用户提供的URL访问，会获取到完全不同基因的规范，对比结果毫无意义
- COL1A1、TSC2、LMNA在ClinGen CSpec中**不存在**独立的VCEP规范文档
- 本地文件VCEP-COL1A1.md、VCEP-TSC2.md、VCEP-LMNA.md**不存在**

**纠正措施**：本次报告对MYBPC3和BRCA2使用其**正确的GN编号**（GN095和GN097）进行官网对比，其余3个基因因无VCEP规范无法对比。

---

## 任务1：SCN8A (GN070) 深度核实

### 版本号核实

- **本地记录版本**：v2.0.0
- **官网当前版本**：**v2.0.0**（发布日期：1/7/2025）
- ⚠️ **用户声称官网已更新到v2.1.0，但经核实官网仍为v2.0.0**。静态抓取可能遗漏JS动态渲染的版本号更新，但搜索也未找到SCN8A v2.1.0的任何公开记录。

### 逐条证据码对比结果

#### ✅ 完全一致的证据码（规则文本无差异）

| 证据码 | 强度层级 | 对比结论 |
|--------|---------|---------|
| PS1 | Strong/Moderate/Supporting | 一致（同源基因规则、剪接规则完整匹配） |
| PS2 | Very Strong/Strong/Moderate/Supporting | 一致（积分规则、表型特异性评分完整匹配） |
| PS4 | Very Strong/Strong/Moderate/Supporting | 一致（积分阈值16+/4-15.5/2-3.5/1-1.5完整匹配） |
| PM1 | Moderate | 一致（PERs引用PM1 Table） |
| PM2 | Supporting | 一致（≤1 allele, ≥10,000 alleles assessed） |
| PM4 | Moderate | 一致 |
| PM6 | Strong/Moderate/Supporting | 一致（积分0.5/phenotype规则完整匹配） |
| PP1 | Strong/Moderate/Supporting | 一致（≥7/5-6/3-4 meioses） |
| PP3 | Moderate/Supporting | 一致（REVEL+PM1限制条件完整匹配） |
| BA1 | Stand Alone | 一致（>0.01%, ≥5 alleles） |
| BS1 | Strong | 一致（>0.0002%, ≥5 alleles） |
| BS2 | Strong | 一致 |
| BP2 | Supporting | 一致 |
| BP3 | Supporting | 一致 |
| BP5 | Supporting | 一致 |
| BP7 | Supporting | 一致 |

#### ⚠️ 有差异的证据码（本地文件缺失内容）

**1. PVS1 — 本地缺失VCEP Specifications前言说明**

官网VCEP Specifications包含3条重要说明，本地文件**全部缺失**：
- "Most terminal codon expected to undergo nonsense-mediated decay: **p.Thr1582**"（NMD边界定义）
- "For splice sites, this criterion should not be applied with PP3."（PVS1与PP3互斥规则）
- "For a full gene deletion, a pathogenic classification is warranted."（全基因删除的致病性判定）

**影响**：p.Thr1582是NMD判定的关键阈值位置，缺失可能导致PVS1强度判定错误。

**2. PS3 — 本地缺失VCEP Specifications前言说明**

官网包含：
> "If a variant is found to have differences from wildtype of multiple levels of strength (example: strong level of evidence in peak current and moderate level of evidence in persistent current), use the highest level of evidence (capping at strong). If a variant has been studied in multiple publications, use the strongest level of evidence available."

本地文件**缺失**此"取最高强度、封顶Strong"的优先级规则。

**3. PM5 — 本地缺失Rule Combining Stipulation**

官网在PM5的VCEP Specifications中包含：
> "Rule Combining Stipulation: If PM5_Strong is reached, and the variant falls within a PM1 region, then do not add PM1 with PM5_Strong."

本地文件PM5部分**缺失**此PM5_Strong与PM1互斥规则。

**4. BS3/BS4/BP1 — 本地仅标记"不适用"，缺失官网的详细说明**

| 证据码 | 官网Not Applicable说明 | 本地文件 |
|--------|----------------------|---------|
| BS3 | 详细说明：细胞电生理"无影响"值尚未充分表征；动物模型缺乏癫痫表型不足以支持良性 | 仅"不适用" |
| BS4 | "Reduced penetrance and phenocopies" | 仅"不适用" |
| BP1 | "Missense variants are common cause of disease" | 仅"不适用" |

**5. BP4 — 本地缺失注释**

官网BP4 Not Applicable下有注释：
> "Replicating methodologies by Pejaver et al, 2022 and Johnston et al, 2021 (PMID: 33767344), REVEL scores could not be obtained for Benign calculations."

本地文件**缺失**此注释。

**6. PP4 — 本地缺失Not Applicable原因说明**

官网PP4 Not Applicable注释："Phenotypic specificity incorporated into PS2, PM6, PS4"

本地文件仅标记"不适用"，未说明原因。

### SCN8A核实总结

| 维度 | 结论 |
|------|------|
| 版本号 | 官网仍为v2.0.0，未发现v2.1.0更新 |
| 核心阈值数据 | PS3阈值（72.7%/80.6%峰值电流等）、PS2/PS4/PM6积分、BA1/BS1频率阈值**全部一致** |
| 规则文本缺失 | PVS1前言（p.Thr1582/PP3互斥/全基因删除）、PS3优先级规则、PM5互斥规则**本地缺失** |
| 不适用码说明 | BS3/BS4/BP1/BP4/PP4的详细不适用原因**本地缺失** |

### 建议操作

1. **高优先级**：补充PVS1的p.Thr1582 NMD边界定义和PP3互斥规则
2. **高优先级**：补充PM5的"PM5_Strong与PM1互斥"规则
3. **中优先级**：补充PS3的"取最高强度、封顶Strong"优先级规则
4. **低优先级**：补充各Not Applicable证据码的官网说明文本
5. **需确认**：官网是否确实存在v2.1.0版本（建议使用浏览器直接访问确认）

---

## 任务2：5个"一致"基因抽检

### 抽检基因1：MYBPC3

- **正确GN编号**：GN095（Cardiomyopathy VCEP）
- **官网版本**：v1.0.0（发布日期：4/22/2024）
- **本地文件**：VCEP-MYBPC3.md（存在）

#### 对比结果：**基本一致，有少量缺失**

**✅ 完全一致的证据码**（核心规则文本匹配）：
PVS1、PS1、PS2、PS3、PS4、PM1、PM2、PM4、PM5、PM6、PP1、PP3、BA1、BS1、BS3、BS4、BP2、BP4、BP7

**⚠️ 有差异的证据码**：

| 证据码 | 差异类型 | 详细说明 |
|--------|---------|---------|
| PP2 | 本地缺失Not Applicable原因 | 官网注释："Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh et al. 2019 PMID:30696458) rather than the missense constraint score in gnomAD. For MYBPC3, there is evidence for regional enrichment of rare missense variants (see PM1 specifications)." 本地仅标记"不适用" |
| BS2 | 本地缺失Not Applicable原因 | 官网注释："Inherited cardiomyopathies generally display reduced penetrance, variable expressivity, and adult-onset." 本地仅标记"不适用" |
| BP1 | 本地缺失Not Applicable原因 | 官网注释："For the current genes where null variants are a known mechanism, pathogenic missense variants have also been reported." 本地仅标记"不适用" |
| BP3 | 本地缺失Not Applicable原因 | 官网注释："Not applicable to the current genes." 本地仅标记"不适用" |
| BP5 | 本地缺失Not Applicable原因 | 官网注释："Co-occurrence with an established pathogenic or likely pathogenic variant for a non-cardiomyopathy related disease does not reduce the likelihood that a variant is independently disease-causing for cardiomyopathy." 本地仅标记"不适用" |
| PP4 | 本地缺失Not Applicable原因 | 官网注释："Inherited cardiomyopathies have high locus heterogeneity as well as non-genetic etiologies." 本地仅标记"不适用" |

**📋 本地有但官网无的内容**：本地文件包含了详细的参考附件链接，与官网Files & Images部分一致。

**📋 官网有但本地缺失的内容**：Rules for Combining Criteria（组合规则）部分。官网列出了详细的Pathogenic/Likely Pathogenic/Benign/Likely Benign组合条件，本地文件未包含。

---

### 抽检基因2：COL1A1

- **用户指定GN编号**：GN021（实际对应ACADVL）
- **正确GN编号**：❌ **不存在VCEP规范**
- **本地文件**：VCEP-COL1A1.md **不存在**

#### 对比结果：**无法执行**

- ClinGen CSpec中**没有COL1A1的独立VCEP规范文档**
- 本地知识库中**没有VCEP-COL1A1.md文件**
- GN021实际对应的是**ACADVL**（very long chain acyl-CoA dehydrogenase deficiency），版本v2.1.0
- 首轮核对将此基因标记为"一致"可能是基于错误的GN编号映射

---

### 抽检基因3：TSC2

- **用户指定GN编号**：GN106（实际对应RPGR）
- **正确GN编号**：❌ **不存在VCEP规范**
- **本地文件**：VCEP-TSC2.md **不存在**

#### 对比结果：**无法执行**

- ClinGen CSpec中**没有TSC2的独立VCEP规范文档**
- 本地知识库中**没有VCEP-TSC2.md文件**
- GN106实际对应的是**RPGR**（X-linked inherited retinal disease），版本v1.0.0
- TSC2可能有其他类型的ClinGen curation（如gene-disease validity），但无VCEP variant interpretation规范

---

### 抽检基因4：BRCA2

- **正确GN编号**：GN097（ENIGMA BRCA1 and BRCA2 VCEP）
- **官网版本**：v1.2.0（发布日期：1/9/2025）
- **本地文件**：VCEP-BRCA2.md（存在）

#### 对比结果：**基本一致，有结构性差异**

**✅ 完全一致的证据码**（核心规则文本匹配）：
PVS1（Very Strong/Strong/Moderate/Supporting）、PS1、PS3、PS4、PM2、PM3、PM5、PP1、PP3、PP4、BA1、BS1、BS2、BS3、BS4、BP1、BP4、BP5、BP7

**⚠️ 有差异的内容**：

| 差异类型 | 详细说明 |
|---------|---------|
| PS2 | 官网标注Not Applicable，注释"BRCA1/2-related cancers occur relatively commonly. No information to calibrate the predictive capacity of de novo occurrences." 本地文件标注为"不适用"但**缺失此原因说明** |
| PM1 | 官网标注Not Applicable，注释"Considered as component of bioinformatic analysis (PP3/BP4)." 本地文件标注为"不适用"但**缺失此原因说明** |
| PM4 | 官网标注Not Applicable，注释"Considered as component of bioinformatic analysis (PP3/BP4)." 本地文件标注为"不适用"但**缺失此原因说明** |
| PM6 | 官网标注Not Applicable，注释同PS2。本地文件标注为"不适用"但**缺失此原因说明** |
| PP2 | 官网标注Not Applicable，注释"High frequency of benign missense variants." 本地文件标注为"不适用"但**缺失此原因说明** |
| BP2 | 官网标注Not Applicable，注释"Applied only in the context of BS2." 本地文件标注为"不适用"但**缺失此原因说明** |
| BP3 | 官网标注Not Applicable，注释"Captured by bioinformatic tool prediction, and domain analysis. See Appendix J for details." 本地文件标注为"不适用"但**缺失此原因说明** |
| VCEP Specifications前言 | 官网多个证据码有详细的VCEP Specifications前言（如PVS1的flowchart说明、PS1的splicing scenarios、PS3的Figure 1C说明等），本地文件有部分简化 |
| 组合规则 | 官网的Rules for Combining Criteria中Pathogenic和Likely Pathogenic为空（引用附件文档），Benign和Likely Benign有规则。本地文件未包含此部分 |
| 附件差异 | 官网附件命名为"Supplementary_Tables_V1.2"等（V1.2版本），本地文件引用的附件名称一致 |

**📋 本地有但官网无的格式化内容**：
- 本地文件包含了PM5_PTC外显子权重表的结构化提取
- 本地文件包含了PS3功能检测表的结构化提取
- 本地文件包含了PM3积分表的结构化提取
- 这些内容在官网是以附件Excel文件形式存在，本地文件将其内联展示，属于**增值内容**，不构成差异

---

### 抽检基因5：LMNA

- **用户指定GN编号**：GN049（实际对应BRAF）
- **正确GN编号**：❌ **不存在VCEP规范**
- **本地文件**：VCEP-LMNA.md **不存在**

#### 对比结果：**无法执行**

- ClinGen CSpec中**没有LMNA的独立VCEP规范文档**
- 本地知识库中**没有VCEP-LMNA.md文件**
- GN049实际对应的是**BRAF**（RASopathy VCEP），版本v2.3.0
- LMNA可能有Cardiomyopathy VCEP的覆盖（需查GN002等），但无独立VCEP规范

---

## 总结与建议

### 问题严重度排序

| 严重度 | 问题 | 影响范围 |
|--------|------|---------|
| 🔴 严重 | GN编号与基因名称系统性错配（5/5全错） | 抽检任务基础数据错误 |
| 🔴 严重 | COL1A1/TSC2/LMNA无VCEP规范但被标记为"一致" | 首轮核对可信度存疑 |
| 🟡 中等 | SCN8A本地缺失PVS1关键说明（p.Thr1582等） | 可能影响PVS1判定准确性 |
| 🟡 中等 | SCN8A本地缺失PM5互斥规则 | 可能导致PM1+PM5_Strong重复计分 |
| 🟡 中等 | 各基因Not Applicable码缺失原因说明 | 影响规则可解释性 |
| 🟢 低 | BRCA2/MYBPC3组合规则未收录 | 可通过附件文档补充 |

### 建议操作

1. **立即**：审查首轮核对的GN编号-基因名称映射表，纠正所有错配
2. **立即**：从"一致"列表中移除COL1A1、TSC2、LMNA（无VCEP规范）
3. **高优先级**：补充SCN8A的PVS1前言（p.Thr1582/PP3互斥/全基因删除）
4. **高优先级**：补充SCN8A的PM5_Strong与PM1互斥规则
5. **中优先级**：统一补充所有Not Applicable证据码的官网原因说明
6. **中优先级**：确认SCN8A官网版本是否确实存在v2.1.0（建议浏览器直接访问）
7. **低优先级**：补充各基因的Rules for Combining Criteria

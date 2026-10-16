# ClinGen VCEP基因特异性规范：ABCA4

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN164 — ABCA4 Variant Curation Expert Panel 

### 覆盖疾病
- **MONDO:0800406**（遗传方式：Autosomal recessive inheritance）

### 通用说明
> 官网版本：Version 1.0（Released 11/14/2025；DOI 10.5281/zenodo.21434773）。

This rule set uses the point counting classification system introduced by Tavtigian, et al. (PMID: 32720330) in lieu of the rule combining recommendations in Richards, et al (PMID:  25741868).

#### 主积分分类表（Point Based Variant Classification Categories）

| 分类 | 积分区间 |
|------|----------|
| Pathogenic（致病） | ≥ 10 |
| Likely Pathogenic（可能致病） | 6 – 9 |
| Uncertain Significance（意义不明确） | 0 – 5 |
| Likely Benign（可能良性） | -6 – -1 |
| Benign（良性） | ≤ -7 |

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Please use the SVI WG decision tree modified for the _ABCA4_ gene.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Comparison missense variant must reach a pathogenic classification using the _ABCA4_ VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect via SpliceAI or other splice predictor.

**OR**

Comparison splicing variant must reach a pathogenic classification using the _ABCA4_ VCEP specifications and both variants must share the same predicted splicing effect. 

**OR**

See Walker, et al 2023 (PMID: 37352859) Figure 5 to use this rule code for variants with RNA sequencing data.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **VCEP前置限定**：先证者必须携带第二个按 ABCA4 VCEP 规则分类指南判定的 ABCA4 变异方可使用本码；若第二个 ABCA4 变异为意义不明确变异（VUS），先证者积分减半；当所有先证者的相位（phase）未知时，本码强度封顶为 Moderate。详见下方 PS2 Guidance。
- **Strong** ✅：Use proposed SVI point recommendations for “Phenotype consistent with gene but not highly specific” for probands with Stargardt disease. Use proposed SVI point recommendations for “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” for probands with other ABCA4-related retinopathies (e.g. - retinitis pigmentosa, cone-rod dystrophy, etc.).
- **Moderate** ✅：Use proposed SVI point recommendations for “Phenotype consistent with gene but not highly specific” for probands with Stargardt disease. Use proposed SVI point recommendations for “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” for probands with other ABCA4-related retinopathies (e.g. - retinitis pigmentosa, cone-rod dystrophy, etc.).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Loss of function of ABCA4 protein in transgenic mice measured by autofluorescence and/or A2E production.
- **Supporting** ✅：Default Point Value: 1. See list of approved functional assays in PS3/BS3 Guidance spreadsheet below.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Enrichment analysis was performed for all likely bi-allelic _ABCA4_ variants that were published up to December 31, 2020 compared to population matched gnomAD data from [Cornelis et al., 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8948157/pdf/main.pdf)<sup>1</sup>. This code can be applied to variants with an OR > or = 5, where the CI does not contain 1.
- **Moderate** ✅：Enrichment analysis was performed for all likely bi-allelic _ABCA4_ variants that were published up to December 31, 2020 compared to population matched gnomAD data from [Cornelis et al., 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8948157/pdf/main.pdf)<sup>1</sup>. This code can be applied to variants with an OR greater or equal to 3 and less than 5, where the CI does not contain 1.
- **Supporting** ✅：Default Point Value: 1.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Total MAF \<0.0001 in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **VCEP前置限定**：两个变异均不得满足 BS1 或 BA1 标准方可使用本码。
- **Very Strong** ✅：Use proposed SVI point recommendations. Both variants must be classified using _ABCA4_ Rule Specifications.
- **Strong** ✅：Use proposed SVI point recommendations. Both variants must be classified using _ABCA4_ Rule Specifications.
- **Moderate** ✅：Use proposed SVI point recommendations. Both variants must be classified using _ABCA4_ Rule Specifications.
- **Supporting** ✅：Use proposed SVI point recommendations. Both variants must be classified using _ABCA4_ Rule Specifications.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：This code can be applied for >1 amino acid deletion/insertion or a stop loss variant, or >1 nucleotide with PhyloP ≥7.367 (https://www.medrxiv.org/content/10.1101/2023.04.24.23288782v1).
- **Supporting** ✅：This code can be applied for 1 amino acid deletion/insertion or a stop loss variant, or 1 nucleotide with PhyloP ≥7.367 (https://www.medrxiv.org/content/10.1101/2023.04.24.23288782v1).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Comparison variant must reach a pathogenic classification using the _ABCA4_ VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect via SpliceAI or other splice predictor.
- **Supporting** ✅：Comparison variant must reach a likely pathogenic classification using the _ABCA4_ VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect via SpliceAI or other splice predictor.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **VCEP前置限定**：反式（in trans）非截短变异必须按 ClinGen ABCA4 VCEP 规则策展并达到致病或可能致病分类；反式截短变异无需进一步策展。
- **Strong** ✅：Segregations in proband plus >2 affected relatives.

*   Affected relatives must have both variants identified in proband..
- **Moderate** ✅：Segregation in proband plus 2 affected relatives.

*   Affected relatives must have both variants identified in proband.
- **Supporting** ✅：Segregation in proband plus 1 affected relative.

*   Affected relatives must have both variants identified in proband.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：This code is applicable for missense variants with a REVEL score of >0.772 or for synonymous or indel variants with a CADD score of greater or equal to 28.1 (https://www.medrxiv.org/content/10.1101/2023.04.24.23288782v1). This code is also applicable for variant with a SpliceAI score of greater than or equal to 0.8.
- **Supporting** ✅：This code is applicable for missense variants with a REVEL score between 0.644-0.772 or for synonymous or indel variants with a CADD score between 25.3-28.0 (https://www.medrxiv.org/content/10.1101/2023.04.24.23288782v1). This code is also applicable for variant with a SpliceAI score of greater than or equal to 0.2.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：This code is applicable when a single proband can be awarded 8 or more phenotype points.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Gprmax allele frequency cutoff of greater than 0.163 in gnomAD.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **VCEP前置说明**：BS1 规则基于 Whiffen-Ware 计算器，采用患病率 1/7500、等位与基因异质性均为 1、外显率 0.5。以下变异排除于本规则码（详见下方 BS1 排除变异列表）。
- **Strong** ✅：Grpmax allele frequency cutoff of greater than 0.0163 in gnomAD.
- **Supporting** ✅：Grpmax allele frequency cutoff of greater than 0.00163 in gnomAD.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：This code is applicable when there are two affected family members without the variant of interest.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Moderate** ✅：This code is applicable for missense variants with a REVEL score of <0.184 or for synonymous or indel variants with a CADD score of less than or equal to 17.3 (PMID: 40225145).
- **Supporting** ✅：This code is applicable for missense variants with a REVEL score between 0.184-0.290 or for synonymous or indel variants with a CADD score between 17.4-20 (PMID: 40225145). This code is also applicable for intronic variants where BP7 is not applicable and the SpliceAI score is \< or = 0.1.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **VCEP联用限定**：BP4 不得与本码联用（BP4 is not used in combination with this rule code）。
- **Moderate** ✅：Rule code is applicable to intronic (outside of canonical -21 to +7) or synonymous variant when Splice AI prediction is <0.1 (PMID: 40225145). This code does not apply when conflicting minigene or other functional data is available.

### 不适用证据码
PM1、PM6、PP2、PP5、BS2、BP1、BP2、BP3、BP5、BP6
### 附件关键数据

#### PP4评分表（ABCA4 PP4 Proband Scoring Table）

**使用PP4的必要条件（每项0.5分）：**
- 影像学检查发现黄斑斑点或眼底自发荧光
- 发病年龄<18岁
- 存在至少2个ABCA4变异

**特异性ABCA4表型发现列表（每项2分）：**
- 视乳头周围保留（Peripapillary sparing）
- 既往外显子组、基因组或100+视网膜营养不良基因panel检测未发现其他病因

**符合ABCA4表型发现列表（每项0.5或1分）：**
| 发现 | 积分 |
|------|------|
| 缺失或降低的杆体和/或锥体视网膜电图反应 | 0.5 |
| 视神经苍白 | 0.5 |
| 牛眼黄斑病变 | 1 |
| 脉络膜毛细血管营养不良 | 1 |
| 色素性视网膜病变伴血管变细 | 0.5 |
| 彩色眼底照片中类似眼底白点症的白/黄点（1分） | 1 |
| 后囊下白内障 | 0.5 |
| RPE斑驳 | 0.5 |
| 黄斑萎缩 | 0.5 |
| 存在囊样黄斑水肿 | 0.5 |
| 周边视野下降 | 1 |
| 夜盲/暗适应障碍 | 0.5 |
| 中心视力下降 | 1 |
| 脉络膜视网膜病变 | 1 |
| 暗点 | 0.5 |

**表型评分阈值：**
- PP4_Moderate（中等）：>8分
- PP4（支持）：3-7.5分

#### PM3积分指导（ABCA4 PM3 Guidance）

| 其他变异的分类/合子性 | 确认反式排列（每先证者积分） | 相位未知（每先证者积分） |
|----------------------|---------------------------|----------------------|
| 致病性或可能致病性变异（P） | 1.0 | 0.5 |
| 可能致病性变异（LP） | 0.5 | 0.25 |
| 纯合子 | 0.5 | N/A |
| 意义不明确变异（VUS） | 0.25 | 0.0 |

| PM3强度 | 总积分阈值 |
|---------|-----------|
| PM3_Very Strong | ≥4分 |
| PM3_Strong | ≥2分 |
| PM3 | ≥1分 |
| PM3_Supporting | ≥0.5分 |

#### PS2/PM6积分指导（ABCA4 PS2 Guidance）

| 表型一致性 | 确认de novo（积分） | 推定de novo（积分） |
|-----------|-------------------|-------------------|
| 表型高度特异于基因 | 2 | 1 |
| 表型符合基因但非高度特异 | 1 | 0.5 |
| 表型符合基因但非高度特异且遗传异质性高 | 0.5 | 0.25 |
| 表型不符合基因 | 0 | 0 |

| 证据强度 | 积分阈值 |
|---------|---------|
| PS2_Very Strong / PM6_Very Strong | ≥2分 |
| PS2_Strong / PM6_Strong | ≥1分 |
| PS2_Moderate / PM6_Moderate | ≥0.5分 |
| PS2_Supporting / PM6_Supporting | ≥0.25分 |

#### 功能检测指导（ABCA4 Functional assay Guidance）

**已批准的功能检测方法：**

| 检测方法 | 正常阈值 | 异常阈值 | 建议强度 |
|---------|---------|---------|---------|
| Western blot蛋白表达检测 | ≥80% WT水平 | <80% WT水平（减少>20%为致病支持） | PS3_Supporting |
| ATPase活性检测 | ≥80% WT水平 | <80% WT水平 | PS3_Supporting或BS3_Supporting |
| 免疫荧光定位 | 与WT相似，80% | 与WT不同 | PS3_Supporting或BS3_Supporting |
| 转基因小鼠实验 | 无自身荧光增加 | 自身荧光增加、A2E增加 | PS3_Strong |

#### BS1排除变异列表（ABCA4 BS1 Exclusion Variants）

以下变异因已知与较轻表型相关，排除BS1规则码：

| ABCA4变异 | GrpMax总MAF |
|----------|-------------|
| c.2588G>C, p.Gly863Ala | 0.008753 |
| c.5603A>T, p.Asn1868Ile | 0.06693 |
| c.5882G>A, p.Gly1961Glu | 0.01768 |
| c.3113C>T, p.Ala1038Val | 0.001985 |
| c.6320G>A, p.Arg2107His | 0.01986105 |
| c.4685T>C, p.Ile1562Thr | 0.001878 |
| c.4253+43G>A | 0.005726 |

### 参考附件
- [ABCA4 PP4 Proband Scoring Table](https://cspec.genome.network/cspec/File/id/cf416b5f-1067-48a6-8eea-a5780d13535b/data)
- [ABCA4 PVS1 Flowchart](https://cspec.genome.network/cspec/File/id/9ec053f7-edce-47b6-9c93-dd7bae874e46/data)
- [ABCA4 Functional assay Guidance](https://cspec.genome.network/cspec/File/id/bb2de50c-0c15-48f2-af86-411f58248adb/data)
- [ABCA4 PM3 Guidance](https://cspec.genome.network/cspec/File/id/50de5c47-22f4-4470-9a25-eaec41e7a592/data)
- [Functional assay Guidance](https://cspec.genome.network/cspec/File/id/7493e562-8000-426b-bac7-5200488cdce2/data)
- [BS1 Exclusion Variants](https://cspec.genome.network/cspec/File/id/7e62e4e3-c058-4e11-9df1-b86950216f41/data)
- [ABCA4 PS2 Guidance](https://cspec.genome.network/cspec/File/id/8f7dd93c-8aa8-446f-a24e-ae145ef4309c/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN164)

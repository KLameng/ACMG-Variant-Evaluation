# ClinGen VCEP基因特异性规范：SERPINC1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v1.1（DOI: 10.5281/zenodo.21434018；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN084 — Thrombosis Variant Curation Expert Panel 

### 覆盖疾病
- **MONDO:0013144**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use decision tree as per SVI WG with specified “regions critical to protein function”.
- **Strong** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".
- **Moderate** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".
- **Supporting** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **VCEP Specifications**：Use caution not to compare variants being curated to variants that are potential cryptic slice sites.
- **Strong** ✅：Use with no specification except comparison variant must be classified as pathogenic using _SERPINC1_ rule specifications from the Thrombosis VCEP.
- **Moderate** ✅：Use with no specification except comparison variant must be classified as likely pathogenic using _SERPINC1_ rule specifications from the Thrombosis VCEP.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **VCEP Specifications**：Any proband must meet the PP4 defined antithrombin deficiency laboratory phenotype (see PP4/PS4 description below).
- **Very Strong** ✅：Use proposed SVI point recommendations for "Phenotype highly specific for gene." See de novo rule code guidance attached. Required 4 points.
- **Strong** ✅：Use proposed SVI point recommendations for "Phenotype highly specific for gene." See de novo rule code guidance attached. Required 2 points.
- **Moderate** ✅：Use proposed SVI point recommendations for "Phenotype highly specific for gene." See de novo rule code guidance attached. Required 1 point.
- **Supporting** ✅：Use proposed SVI point recommendations for "Phenotype highly specific for gene." See de novo rule code guidance attached. Required 0.5 point.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **VCEP Specifications**：Model organism do not tend to recapitulate the phenotype of interest and are not used for curation.
- **Supporting** ✅：See attached spreadsheet for list of approved assays to use for this rule code. Below is a general description of assays that can be used:

 * _In vitro_ functional studies in COS-1, HEK293T, HEK-EBNA cells demonstrating abnormal activity levels:

 - Antithrombin activity levels measured by FXa inhibition activity assay

 - Antithrombin activity levels measured by thrombin inhibition activity assay

 OR

 \- _In vitro_ functional studies in COS-1, HEK293T, HEK-EBNA cells demonstrating abnormal antigen levels:

 - Antithrombin antigen levels measured by ELISA

     - Immunofluorescence assay – intracellular retention and secretion defects

 OR

 \- _In vivo_ studies demonstrating rescue of antithrombin levels would be considered, but no studies are known to be available at this time.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **VCEP Specifications**：This code requires the use of proband points. Please see attached guidance on tallying proband points for this phenotype. Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count proband used for PP4 in this code's proband count.
- **Very Strong** ✅：Appropriate to use code when there 8 or more proband points that meet the defined antithrombin deficiency laboratory phenotype.
- **Strong** ✅：Appropriate to use code when there 4-7 proband points that meet the defined antithrombin deficiency laboratory phenotype.
- **Moderate** ✅：Appropriate to use code when there 2-3 proband points that meet the defined antithrombin deficiency laboratory phenotype.
- **Supporting** ✅：Appropriate to use code when there is 1 proband point that meets the defined antithrombin deficiency laboratory phenotype.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：This code is applicable for variants disrupting cystine residues involved in disulfide bridges (Cys40, Cys53, Cys127, Cys160, Cys279, Cys462)<sup>1</sup>, variants that would impact heparin binding site residues (Ile39, Arg56, Pro73, Arg79), variants involving reactive site residues (Ala414 and Ala416)<sup>2</sup>, and variants involving the N-glycosylation site (Asn224)<sup>3</sup>.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Use code for variants with a popmax MAF of \<0.00002 in gnomAD.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：No specification

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use code when previously reported variant reaches a pathogenic classification using the _SERPINC1_ rule specifications from the Thrombosis VCEP.
- **Supporting** ✅：Use code when previously reported variant reaches a likely pathogenic classification using the _SERPINC1_ rule specifications from the Thrombosis VCEP.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Appropriate to use there are 7 or more meioses across more than one family.
- **Moderate** ✅：Appropriate to use there are 4-6 meioses across one or more families.
- **Supporting** ✅：Appropriate to use when there are 2-3 meioses across one or more families.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.6. For potential splicing variants, SpliceAI must predict a damaging impact with a score greater or equal to 0.5.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：Proband must have an antithrombin activity level of < 0.8 IU/mL (or below the lower limit of a laboratory’s assays reference range). confirmed on repeated independent samples. An abnormal crossed immunoelectrophoresis assay demonstrating decreased antithrombin function may be used in lieu of low activity levels, which is typically caused by type II variants.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Appropriate to use for variants with a popmax MAF of greater than or equal to 0.002 in gnomAD.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Appropriate to use for variants with a Popmax MAF of >0.0002 in gnomAD.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：This evidence code is available when the variant is identified in 2 or more heterozygotes or 1 or more homozygotes with normal antithrombin levels \[> 0.8 IU/mL (or above the lower limit of a laboratory’s assays reference range)\].
- **Supporting** ✅：This evidence code is available when the variant is identified in 1 heterozygote with normal antithrombin levels \[> 0.8 IU/mL (or above the lower limit of a laboratory’s assays reference range)\].

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Appropriate to use when the variant is found not to segregate in a minimum of four relatives with abnormal antithrombin activity levels \[\< 0.8 IU/mL (or below the lower limit of a laboratory’s assays reference range)\] within the same family, **OR** the variant does not segregate in 2 or more families. Non-segregation defined by having abnormal antithrombin activity levels without _SERPINC1_ variant of interest.

- **Supporting** ✅：Appropriate to use when the variant is found not to segregate in a minimum of two relatives with abnormal antithrombin activity levels [< 0.8 IU/mL (or below the lower limit of a laboratory's assays reference range)] within the same family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：This rule can be applied when a _SERPINC1_ variant is _in cis_ with another pathogenic _SERPINC1_ variant. The pathogenic variant must be evaluated using ClinGen _SERPINC1_ specified rules. This rule cannot be applied to a variant _in trans_ with a pathogenic variant, as this scenario could reasonably occur and increase the risk of venous thrombosis.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Use this code for missense variants with a REVEL score of \< or equal to 0.30 and no evidence of a potential splicing effect using the Splice AI prediction tool (less than or equal to 0.1), or for non-canonical intronic variants with no evidence of a potential splicing effect using the Splice AI prediction tool.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Use Splice AI to rule out a predicted splicing effect (less than or equal to 0.1). Evolutionary conservation is defined as a PhyloP > 0.1 **OR** the reference nucleotide is present in 3 mammals or 1 primate.

### Rules for Combining Criteria（组合规则）

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND 1 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS4, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND 1 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS4) AND 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP7)
- ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP7)

### 不适用证据码
PM3、PM6、PP2、PP5、BS3、BP1、BP3、BP5、BP6
### 附件关键数据

#### PS4/PP4表型评分规则（SERPINC1 Phenotype rules PS4PP4 guidance）

**PP4应用条件：**
- 单个先证者的抗凝血酶活性水平 <0.8 IU/mL（或低于实验室检测参考范围下限）
- 多次独立样本检测均显示抗凝血酶活性水平异常
- 可用交叉免疫电泳法显示抗凝血酶功能降低（通常由II型变异引起）

**PS4积分系统：**

| 条件 | 积分 |
|------|------|
| 抗凝血酶活性水平<0.8 IU/mL（多次独立样本确认） | 1分 |
| 抗凝血酶活性水平<0.8 IU/mL（无重复确认但有家族史） | 1分 |
| 交叉免疫电泳法显示抗凝血酶功能降低 | 1分 |
| 抗凝血酶活性水平<0.8 IU/mL（无重复确认，无家族史） | 0.5分 |

| PS4强度 | 所需积分 |
|---------|---------|
| PS4_Supporting | 1分 |
| PS4_Moderate | 2-3分 |
| PS4 | 4-7分 |
| PS4_Very Strong | ≥8分 |

#### 功能检测列表（SERPINC1 functional assay list）

**已批准的功能检测方法：**

| 检测方法 | PMID | 材料 | 建议强度 |
|---------|------|------|---------|
| AT活性测定（FXa抑制活性测定） | 23809926 | COS-1细胞 | PS3_Supporting |
| AT活性测定（FXa抑制活性测定） | 27098529 | HEK-EBNA细胞 | PS3_Supporting |
| 抗凝血酶活性测定 | 30237862 | HEK-EBNA细胞 | PS3_Supporting |
| AT抗原测定（ELISA） | 23809926 | COS-1细胞 | PS3_Supporting |
| AT抗原测定（ELISA） | 23117546 | HEK293T细胞 | PS3_Supporting |

**检测阈值：**
- 正常读数：与WT相似
- 异常读数：与WT不同

#### De novo规则指导（SERPINC1 De novo rule guidance）

**表型一致性：**
使用"表型高度特异于基因"（第1选项）

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

**De novo规则要求：**
- PS2_Strong：需要≥2分（表型高度特异的确认de novo）
- PS2_Moderate：需要≥1分（表型高度特异的确认de novo）

### 参考附件
- [Phenotype rules (PS4/PP4) guidance](https://cspec.genome.network/cspec/File/id/581411a8-a42f-4903-a580-838fdbdf2bbd/data)
- [SERPINC1 functional assay list](https://cspec.genome.network/cspec/File/id/931dda8a-8331-46ec-9747-fccb2126bc14/data)
- [SERPINC1 Rule code combination rules](https://cspec.genome.network/cspec/File/id/e38bd3b2-cb99-4440-94c2-d59c181ee46a/data)
- [De novo rule guidance](https://cspec.genome.network/cspec/File/id/4604a80f-7af3-45ac-8fc3-e58ea4895b66/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN084)

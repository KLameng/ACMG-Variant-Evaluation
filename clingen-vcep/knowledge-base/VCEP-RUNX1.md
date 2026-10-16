# ClinGen VCEP基因特异性规范：RUNX1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN008 — Myeloid Malignancy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0011071**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Release notes:
(1) New gnomAD MAF threshold for PM2_supporting ≤ 0.00005 to account for larger population in gnomAD v4.
(2) Upgraded strength of PM1 to PM1_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added a caveat to not use PM5/PS1 at any level if PM1 was applied.
(3) Upgraded strength of PM4 to PM4_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added an allowance to use PM4 for stop-loss variants.
(4) Established PVS1_variable (RNA) and BP7_variable (RNA) to be used when RNA data is available for splicing variants. PS1 is now able to be used for splicing variants with the same predicted splicing event as a known pathogenic/likely pathogenic splicing variant.
(5) Conservation data is no longer considered when applying BP7. BP7 is limited to intronic variants, and synonymous variants which don’t occur in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site.
(6) Revised PM5 to account for Grantham scores when evaluating missense variants.
            
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects.
- **Strong** 📋：Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects.
- **Moderate** 📋：Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：**PS1:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**For splice site variants:** 

**PS1\_Variable:** Follow recommendations from the ClinGen SVI Splicing Subgroup (Walker et al., 2023, PMID: 37352859 [<sup>5</sup>](#PMID_37352859))
- **Moderate** 📋：**PS1\_Moderate:** Same amino acid change as a previously established likely pathogenic variant regardless of nucleotide change.

**For splice site variants:** 

**PS1\_Variable:** Follow recommendations from the ClinGen SVI Splicing Subgroup (Walker et al., 2023, PMID: 37352859 [<sup>5</sup>](#PMID_37352859))

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** 📋：**PS2\_Moderate:** ≥ 2 proven _de novo_ occurrences (both maternity and paternity confirmed) in patients with FPD/AML phenotype.
- **Supporting** 📋：**PS2\_Supporting**: 1 proven _de novo_ occurrence (both maternity and paternity confirmed) in a patient with FPD/AML phenotype.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：**PS3:** Transactivation assays demonstrating altered transactivation (\<20% of wt, and/or reduced to levels similar to well established pathogenic variants such as R201Q or R166Q) AND data from a secondary assay demonstrating altered function. Not applicable if variant meets **PVS1**. If variant meets **PVS1\_strong**, upgrade to **PVS1**.
- **Moderate** 📋：**PS3\_Moderate:** Transactivation assays demonstrating altered transactivation (\<20% of wt and/or reduced to levels similar to well established pathogenic variants such as R201Q or R166Q) OR ≥ 2 secondary assays demonstrating altered function.
- **Supporting** 📋：**PS3\_Supporting:** Transactivation assays demonstrating enhanced transactivation (>115% of wt).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：**PS4:** ≥ 4 probands meeting at least one of the \_RUNX1\_-phenotypic criteria (OR 127.1).
- **Moderate** 📋：**PS4\_Moderate:** 2-3 probands meeting at least one of the \_RUNX1\_-phenotypic  criteria (OR 63.5-95.3).
- **Supporting** 📋：**PS4\_Supporting:** 1 proband meeting at least one of the \_RUNX1\_-phenotypic criteria (OR 31.8).

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** 📋：**PM1\_strong:** Variant affecting one of the following 13 AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.
- **Supporting** 📋：**PM1\_Supporting**: Variant affecting one of the other AA residues 89-204 within the RHD.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：**PM2\_Supporting:** Minor allele frequency  ≤ 0.00005 with at least 2000 alleles tested around and 20x coverage at the position.

Caveat: 

\*We recommend evaluating PM2\_supporting using the GrpMax FAF when it is available in gnomAD v4.1.0. If a GrpMax FAF value is not available, we recommend requiring that all subpopulations meet the PM2\_supporting threshold.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** 📋：**For in-frame/indel variants:**

**PM4\_strong:** In-frame deletion/insertion impacting at least one of the following AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.

**For stop loss variants:**

**PM4:** Stop-loss variant causing a protein extension.
- **Moderate** 📋：In-frame deletion/insertion impacting at least one of the following amino acid residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.
- **Supporting** 📋：**PM4\_Supporting:**

In-frame deletion/insertion impacting at least one of the other AA residues 89-204 within the RHD.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：**PM5\_Strong:** Missense change at an AA residue where ≥ 2 different missense changes which have been determined to be pathogenic before (after accounting for Grantham scores).

Caveats:

\*Of note, the variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.

\*The nonsense/frameshift variants before c.98 only affect one of the _RUNX1_ functional transcript. PVS1 is also not appliable in this region based on the _RUNX1_ PVS1 decision tree.

\*PM5 cannot be used if PM1 was applied at any strength level.
- **Moderate** 📋：**PM5:** Missense change at an AA residue where a different missense change which has been determined to be pathogenic before (after accounting for Grantham scores).

Caveats:

\*Of note, the variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.

\*The nonsense/frameshift variants before c.98 only affect one of the _RUNX1_ functional transcript. PVS1 is also not appliable in this region based on the _RUNX1_ PVS1 decision tree.

\*PM5 cannot be used if PM1 was applied at any strength level.
- **Supporting** 📋：**PM5\_Supporting**: Missense change at an AA residue where a different missense change which has been determined to be likely pathogenic before (after accounting for Grantham scores).

**PM5\_Supporting** is also applied to nonsense/frameshift variants that are downstream of c.98 (in transcript NM\_001754.4).

Caveats:

\*Of note, the variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.

\*The nonsense/frameshift variants before c.98 only affect one of the _RUNX1_ functional transcript. PVS1 is also not appliable in this region based on the _RUNX1_ PVS1 decision tree.

\*PM5 cannot be used if PM1 was applied at any strength level.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：_**RUNX1**_ **Specification:**

Following the SVI guidance, assumed _de novo_ _RUNX1_ variants will be scored at the third tier of the point-based system with maximum allowable value of 1 point contributing to overall score:

**PM6**: ≥ 4 assumed _de novo_ occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype.
- **Supporting** 📋：_**RUNX1**_ **Specification:**

Following the SVI guidance, assumed _de novo_ _RUNX1_ variants will be scored at the third tier of the point-based system with maximum allowable value of 1 point contributing to overall score:

**PM6\_Supporting**: 2 or 3 assumed _de novo_ occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：**PP1\_Strong**: ≥ 7 meioses observed within one or across multiple families.
- **Moderate** 📋：**PP1\_Moderate**: 5 or 6 meioses observed within one or across multiple families.
- **Supporting** 📋：**PP1**: 3 or 4 meioses observed within one or across multiple families.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：**For missense variants:**

**PP3:** REVEL score  ≥ 0.88 or SpliceAI ≥ 0.38, including the creation of cryptic novel splice sites.

**For synonymous and intronic (intron 4-8) variants:**

**PP3:** SpliceAI ≥ 0.38, including the creation of cryptic novel splice sites.

Caveats:

\*Do not use for variants with a predicted splicing effect that is proven by RNA analysis. See **PVS1\_Variable (RNA)**.

\*Do not use for for canonical splice site variants.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：_**RUNX1**_ **Specification:**

**BA1:** Minor allele frequency ≥ 0.0015 (0.15%) in any general continental population dataset with ≥ 2,000 alleles tested and variant present in ≥ 5 alleles.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：**MM-VCEP notes:**

Similarly, for the **BS1** calculation, we utilized the Whiffin/Ware calculator (http://cardiodb.org/allelefrequencyapp/) with a prevalence of 1 in 40, a conservative unascertained penetrance estimate of 85%, an allelic heterogeneity of 100% and a maximum genetic heterogeneity of 1% (one magnitude lower than for **BA1**). A 95% confidence interval was used to develop the threshold. We developed a range for application of **BS1** for variants with a minor allele frequency between 0.00015 (0.015%) and 0.0015 (0.15%). 

1.  The MM-VCEP also adopted the SVI recommendation that the variant be present in any general continental population dataset with a minimum number of 2,000 alleles and variant present in ≥ 5 alleles.
2.  The variant can be classified as likely benign based on **BS1** alone if there is no contradictory evidence supporting pathogenicity.

_**RUNX1**_ **Specification:**

**BS1:** Minor allele frequency between 0.00015 (0.015%) and 0.0015 (0.15%) in any general continental population dataset with ≥ 2,000 alleles tested and variant present in ≥ 5 alleles.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：**BS3:** Transactivation assays demonstrating normal transactivation (80-115% of wt) AND data from a secondary assay demonstrating normal function.
- **Supporting** 📋：**BS3\_Supporting:** Transactivation assays demonstrating normal transactivation (80-115% of wt).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：**BS4:** Applicable when observed in ≥ 2 informative meioses.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：**For missense variants:**

**BP4:** REVEL score \< 0.50 AND SpliceAI ≤ 0.20

**For synonymous and Intronic variants:**

**BP4:** SpliceAI ≤ 0.20

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：**BP7:** Applicable for

*   Synonymous variants – excluding those in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site – with SpliceAI ∆ scores ≤ 0.20.
*   Intronic variants with SpliceAI ∆ scores ≤ 0.20.

**BP7\_Variable (RNA):** 

*   Applicable for variants with RNA data, with weighting based on the quality of the available RNA data.

### 点系统分类（Tavtigian 贝叶斯框架，v3.1 浏览器实页核实 2026-02-13）

本规范采用 Tavtigian et.al., 2020 贝叶斯适配的点系统。各证据码强度对应的 Default Point Value 如下：

**致病方向（正分）**

| 积分 | 证据码强度 |
|---|---|
| +8 | PVS1（Very Strong） |
| +4 | PVS1_Strong、PS1、PS3、PS4、PM1_Strong、PM4_Strong、PM5_Strong、PP1_Strong |
| +2 | PVS1_Moderate、PS1_Moderate、PS2_Moderate、PS3_Moderate、PS4_Moderate、PM4、PM5、PM6、PP1_Moderate |
| +1 | PS2_Supporting、PS3_Supporting、PS4_Supporting、PM1_Supporting、PM2_Supporting、PM4_Supporting、PM5_Supporting、PM6_Supporting、PP1、PP3 |

**良性方向（负分）**

| 积分 | 证据码强度 |
|---|---|
| Stand Alone（不记分，独立判良性） | BA1 |
| -4 | BS1、BS3、BS4（Strong） |
| -1 | BS3_Supporting、BP2、BP4、BP7 |

**Point Based Variant Classification Categories（积分分类切分）**

| 分类 | 积分区间 |
|---|---|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤ -7 |

### 不适用证据码
PM3、PP2、PP4、PP5、BS2、BP1、BP3、BP5、BP6
### 参考附件
- [MM-VCEP RUNX1 Pilot Results](https://cspec.genome.network/cspec/File/id/a189947d-f25d-46f3-9dd9-42dca0b5e91e/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN008)

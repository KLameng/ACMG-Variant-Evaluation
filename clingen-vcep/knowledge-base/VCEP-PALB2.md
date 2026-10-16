# ClinGen VCEP基因特异性规范：PALB2

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：GN077 v1.2（Released，官网页面未发布 DOI，2026-10-09 官网实页核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN077 — Hereditary Breast, Ovarian and Pancreatic Cancer Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0700272**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0012565**（遗传方式：Autosomal recessive inheritance）

### 通用说明
Release notes v1.3

Further clarified use of BP4 in the presence of RNA data (BP4+BP7(RNA) is allowed, v1.2 had conflicting information)
Provided additional guidance on use of gnomAD data
Clarified Boolean operators in PS4
Clarified PM5_sup to include p.Tyr1183\*
Clarified additional variant types can meet PM5_sup
Included clarification on predicted vs observed for splice variants.
Updated PVS1 decision tree for duplications involving WD40 to align with the written description
Uploaded supporting documents by individual codes (PVS1, PS1, PM3/BS2) instead of one packet with all code specifications.
No other changes to criteria or attachments.

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Use PALB2 PVS1 Decision Tree
- **Strong** 📋：Use PALB2 PVS1 Decision Tree.
- **Moderate** 📋：Use PALB2 PVS1 Decision Tree.
- **Supporting** 📋：Use PALB2 PVS1 Decision Tree

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Use PALB2 PS1 Splicing table
- **Moderate** 📋：Use PALB2 PS1 Splicing table
- **Supporting** 📋：Use PALB2 PS1 Splicing table

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：Case-control studies; p-value ≤.05 AND (Odds ratio, hazard ratio, or relative risk  ≥3 OR lower 95% CI ≥1.5).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Frequency ≤ 1/300,000 (**0.000333%**) in gnomAD subpopulation with the highest frequency

Exception: If >0.000333% but n=1 in a single subpopulation (not present in any other subpopulation), that is sufficiently rare and PM2_supporting would apply.

> 隐藏注释（官网 NA-NOTE）：PM2_Supporting is not considered a conflicting piece of evidence to an otherwise benign body of evidence; Coverage must be >30X at the locus.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：PM3\_VeryStrong **≥ 8** points

See Fanconi Anemia PM3 tables for approach to assign points per proband.
- **Strong** 📋：PM3\_Strong **≥ 4** points

See Fanconi Anemia PM3 tables for approach to assign points per proband.
- **Moderate** 📋：PM3 = **2** points

See Fanconi Anemia PM3 tables for approach to assign points per proband.
- **Supporting** 📋：PM3\_Supporting = **1** point

See Fanconi Anemia PM3 tables for approach to assign points per proband.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** 📋：*   Apply to all NMD-prone, truncating variants receiving PVS1 (must be at VeryStrong) with premature termination codons upstream of p.His1184.
*   Apply to all observed (not predicted) NMD-prone, truncating variants receiving PVS1(RNA) (must be at VeryStrong with high-quality RNA data) with premature termination codons upstream of p.His1184. This is not applicable for predicted splice impact without RNA data or PVS1(RNA) at reduced strength.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：*   AD Condition: LOD ≥1.26 or Bayes Factor (LR) ≥18:1
*   AR Condition: Segregation in ≥3 affected relatives
- **Moderate** 📋：*   AD Condition: LOD ≥.60 or Bayes Factor (LR) ≥4:1
*   AR Condition: Segregation in 2 affected relatives
- **Supporting** 📋：*   AD Condition: LOD ≥0.3 or Bayes Factor (LR) ≥2:1
*   AR Condition: Segregation in 1 affected relative

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: Do not use.
*   Splicing: Predicted impact via splicing (SpliceAI **≥0.2**) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Grpmax Filtering AF **\>.1%** in gnomAD v4 dataset

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Grpmax Filtering AF **\>.01%** in gnomAD v4 dataset

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：BS2 **≥ 4** points

See Fanconi Anemia BS2 tables for approach to assign points per proband.
- **Moderate** 📋：BS2\_Moderate = **2** points

See Fanconi Anemia BS2 tables for approach to assign points per proband.
- **Supporting** 📋：BS2\_Supporting = **1** point

See Fanconi Anemia BS2 tables for approach to assign points per proband.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：LOD ≤ -1.28 or Bayes Factor (LR) ≤.053:1
- **Moderate** 📋：LOD ≤ -.64 or Bayes Factor (LR) ≤.23
- **Supporting** 📋：LOD ≤-.32 or Bayes Factor (LR) ≤.48

#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Supporting** 📋：Apply to all missense variants.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: Do not use. 
*   Splicing: No predicted impact via splicing (SpliceAI **≤0.1**). Do not apply for missense variants.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：BP7\_Strong(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.
- **Moderate** 📋：BP7\_Moderate(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.
- **Supporting** 📋：*   BP7: Use for synonymous and deep intronic variants defined as further than (but not including) +7 and further than (but not including) -21 at donor and acceptor sites, respectively.
*   BP7(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.

### Rules for Combining Criteria

#### Pathogenic
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

#### Likely Pathogenic
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Very Strong (PVS1) AND 1 Supporting (PVS1_Supporting, PS1_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)

#### Benign
- ≥ 2 Strong
- 1 Stand Alone

#### Likely Benign
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting
- 1 Strong (BS1, BS2, BS4, BP7_Strong)

### 不适用证据码
PS2、PS3、PM1、PM4、PM6、PP2、PP4、PP5、BS3、BP2、BP3、BP5、BP6
### 参考附件
- [ClinGen HBOP ACMG Specifications PALB2 version 1.2](https://cspec.genome.network/cspec/File/id/97c2b3b2-b9d6-454b-ac20-0c8d3e2c208d/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN077)

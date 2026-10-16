# ClinGen VCEP基因特异性规范：F9

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.1（DOI: 10.5281/zenodo.21433987；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN080 — Coagulation Factor Deficiency Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010604**（遗传方式：X-linked inheritance）

### 通用说明
When pathogenic and benign rule codes are applied, see guidance below for the point counting variant classification system rather than defer to classification of variant of uncertain significance.

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.
- **Strong** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.
- **Moderate** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.
- **Supporting** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on _F9_ gene rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.

**OR**

When two or more variants are share the same predicted splicing effect and one comparison splicing variant reaches a pathogenic classification or 2 comparison variants reach a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications modified from Walker, et al 2023 (PMID: 37352859).
- **Moderate** 📋：This evidence code can be applied when there is 1 likely pathogenic variants at the same residue based on _F9_ gene rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.

**OR**

When the comparison variant shares the same predicted splicing effect and the comparison splicing variant reaches a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications based on Walker, et al 2023 (PMID: 37352859).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：Use the SVI recommendations for de novo cases; 4 points. Use de novo guidance below to determine point value.
- **Strong** 📋：Use the SVI recommendations for de novo cases; 2 points. Use de novo guidance below to determine point value.
- **Moderate** 📋：Use the SVI recommendations for de novo cases; 1 point. Use de novo guidance below to determine point value.
- **Supporting** 📋：Use the SVI recommendations for de novo cases; 0.5 point. Use de novo guidance below to determine point value.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：Abnormal factor IX activity level (\<40 IU/dL or 40%) in a cell line and/or mouse model.

\--OR--

Abnormal factor IX activity level (\<40 IU/dL or 40%) studied in an animal model setting other than mouse (i.e. – bovine factor IX activity levels compared to factor X levels).

\--OR--

Absent or significantly reduced factor IX antigen level compared to wildtype using conformation-specific reporter assay in cell lines.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：≥8 probands meet criteria described below
- **Strong** 📋：4-7 probands meet criteria described below
- **Moderate** 📋：2-3 probands meet criteria described below
- **Supporting** 📋：1 proband meets criteria described below

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** 📋：This code can be used for variants affecting any of the 3 catalytic residues (H267, D315 or S411) and 2 activation residues (R191-A192 and R226-V227) in the _F9_ gene (PMID: 12554099).
- **Moderate** 📋：This code should be applied when the variant is within exons 3, 4 or 5.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Variant must be absent in males in population databases, such as gnomAD.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Use code with no specification.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on _F9_ rule specification from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.
- **Supporting** 📋：This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on _F9_ rule specifications Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect. A “highly suspicious” VUS is defined as a variant that is 1 supporting code away from reaching a likely pathogenic classification.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：This code is applicable when there ≥4 meioses across ≥2 families.
- **Moderate** 📋：This code is applicable when there are at least 3 meioses across one or more families.
- **Supporting** 📋：This code is applicable when there 2 meioses in one family **OR** 1 meiosis between 2 affected siblings.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Code can be applied for variants where the REVEL score is greater than or equal to 0.6 or a SpliceAI score of greater than or equal to 0.2.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** 📋：Proband must meet hemophilia B phenotype criteria AND have full gene sequencing and deletion/duplication analysis.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：MAF cutoff of greater than or equal to 0.0000556 (or 0.00556%).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：MAF cutoff of greater than or equal to 0.00000556 (or 0.000556%).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：This evidence code can be used when a _F9_ variant is observed in a male with a normal factor IX activity level (at least >40% IU or as defined by laboratory cut off).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：This code can be used for _F9_ gene variants studied in a cell line or mouse model setting that confer a normal factor IX activity AND normal factor IX antigen levels **OR** normal Western Blot.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：This evidence code can be used when a _F9_ variant is observed in a male with a family history of hemophilia B and has a normal factor IX activity level.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：This code can be applied for variants reaching a REVEL score of 0.3 or below AND a Splice AI score of less than or equal to 0.1.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay and a SpliceAI score of less than or equal to 0.1.
- **Supporting** 📋：Splicing prediction score of less than or equal to 0.1 is required. Conservation should be assess using PhyloP (cutoff less than 0.1) and PhastCons (cutoff less than 0.5).

### Rules for Combining Criteria

> 注：本 VCEP 对致病变异与良性证据码并存的情形采用 point-counting policy（见附件“Rule Guidance for Combining Pathogenic and Benign Codes”），而非默认归入 VUS。

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND 1 Supporting (PVS1_Supporting, PS2_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS2_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS2_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS3, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS3, BS4) AND 1 Supporting (BP4, BP7)
- ≥ 2 Supporting (BP4, BP7)

### 不适用证据码
PM3、PM6、PP2、PP5、BP1、BP2、BP3、BP5、BP6
### 参考附件
- [F9 Functional Assays](https://cspec.genome.network/cspec/File/id/bea7b592-808a-47dd-8abe-d320a0dfa10d/data)
- [Pilot Study Results for F8 and F9](https://cspec.genome.network/cspec/File/id/d2c1e05e-bdfb-4819-b5ee-0c01700da9e3/data)
- [Rule Guidance for Combining Pathogenic and Benign Codes](https://cspec.genome.network/cspec/File/id/03399d8c-5b0b-4333-a0ca-2104951c1d69/data)
- [PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/8f07661f-8109-44b9-b72d-680fe4f60dd3/data)
- [Guidance for Combined De Novo Rule Code (PS2/PM6)](https://cspec.genome.network/cspec/File/id/0f64055a-f21a-44fb-887e-628f0280d2d2/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN080)

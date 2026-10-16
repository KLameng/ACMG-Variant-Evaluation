# ClinGen VCEP基因特异性规范：FOXG1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-14
> 规范版本：未随包声明（数据日期：2026-06-14；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v6.0.0（Released 2026-05-01）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN035 — Rett and Angelman-like Disorders Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100040**（遗传方式：Autosomal dominant inheritance）

### 版本更新说明（v6.0.0）
- 1 Strong AND 3 Supporting added to benign criteria code
- 1 Strong added to likely benign criteria code

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group (PMID:30192042).
*   PVS1 is applicable for
    *   Null variants up to p.S468 [<sup>1</sup>](#PMID_30525188)
    *   A full gene deletion
- **Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   PVS1\_Strong is applicable for any truncating variant from p.G469 to p.Q480 [<sup>2</sup>](#PMID_29655203).
- **Moderate** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   PVS1\_Moderate is applicable for any truncating variant distal of p.Q480.
- **Supporting** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   PVS1\_Supporting is applicable for initiation codon variants in _FOXG1._

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **VCEP Specifications**：Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo). Because of the very high de novo rate of pathogenic variants in FOXG1, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.
- **Very Strong** ✅：De novo (maternity and paternity confirmed) in a patient with the disease and no family history.

*   ≥2 independent occurrences of PS2.
*   ≥2 independent occurrences of PM6 and one occurrence of PS2.
*   Evidence from literature must be fully evaluated to support independent events.
- **Strong** ✅：De novo (maternity and paternity confirmed) in a patient with the disease and no family history.

*   1 occurrence of PS2.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.

*   RNA studies that demonstrate abnormal splicing and an out-of-frame transcript.
*   Do not use for canonical splice site variants and when PVS1 is used.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.

*   RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section).
*   See included table for acceptable functional studies.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **VCEP Specifications**：Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum. Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (RettBASE). However independent case has to be confirmed to be a different patient than yours (compare gender/age). Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* 5+ observations.
- **Moderate** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* 3-4 observations.
- **Supporting** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* Use for 2nd independent occurrence.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain.

*   Forkhead: aa 181-275[<sup>3</sup>](#PMID_18571142)<sup>,</sup>[<sup>4</sup>](#PMID_28661489)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.
* Use if absent, zero observations in control databases.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*   Do not use PM4 for in-frame deletions/insertions in the Histidine-rich region (p.37-p.57), Proline- and Glutamine-rich region (p.58-p.86) and Proline-rich region (p.105-p.112).
- **Supporting** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
* Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
* ≥2 different missense changes affecting the amino acid residue.
* Do not apply PM1 in these situations.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** ✅：Confirmed de novo without confirmation of paternity and maternity.
* ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events.
- **Strong** ✅：Confirmed de novo without confirmation of paternity and maternity.
* ≥2 independent occurrences of PM6.
* Evidence from literature must be fully evaluated to support independent events.
- **Moderate** ✅：Confirmed de novo without confirmation of paternity and maternity.

*   1 occurrence of PM6.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members.

*   ≥5 informative meiosis
- **Moderate** ✅：Co-segregation with disease in multiple affected family members.

*   3-4 informative meiosis
- **Supporting** ✅：Co-segregation with disease in multiple affected family members.

*   2 informative meiosis

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

*   For missense variants use REVEL with a score ≥ 0.644.
*   For splice site variants use SpliceAI with a score ≥ 0.2.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：Phenotype specific for disease with single genetic etiology.
* See gene specific clinical phenotype guidelines.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Use large population databases (i.e. gnomAD).
*   Use if variant is present at ≥0.000083 (0.0083%) in any sub-population.
*   Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Use large population databases (i.e. gnomAD).
*   Use if variant is present at ≥0.0000083 (0.00083%) and \<0.000083 (0.0083%) in any sub-population.
*   Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in the heterozygous/hemizygous state in a healthy adult.

*   2 unaffected (related or unrelated) heterozygotes.
- **Supporting** ✅：Observed in the heterozygous/hemizygous state in a healthy adult.

*   1 unaffected (related or unrelated) heterozygote

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function.

*   RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data.
*   Not applicable for other functional studies.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.

*   Absent in a similarly affected family member, when seen in two or more families
- **Supporting** ✅：Lack of segregation in affected members of a family.

*   Absent in a similarly affected family member

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **VCEP Specifications**：Knock-out results in embryonic lethality/drastic phenotype [PMID:14704420]
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern.

*   Applicable for _in trans_ state

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants use REVEL with a score ≤ 0.290.
*   For splice site variants use SpliceAI with a score ≤ 0.1.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：Variant found in a case with an alternate molecular basis for disease.
* ≥3 cases with alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

*   1 case with alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

*   Defined 'not highly conserved' regions in BP7 as those with PhastCons score \<1 and/or PhyloP score \<0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species.
*   For splice site variants use SpliceAI with a score ≤ 0.1.

### Rules for Combining Criteria（v6.0.0）

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND 1 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS3, BS4, BP5_Strong)
- 1 Stand Alone (BA1)
- 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) AND 3 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7)

#### Likely Benign
- ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7)
- 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong)

### 不适用证据码
PM3、PP2、PP5、BP1、BP6

### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function
 * Inframe expansions or deletions in _FOXG1_ repetitive regions: poly His (p.His47-p.His57), poly Gln (p.Gln70-p.Gln73) and poly Pro (p.Pro58-p.Pro61; p.Pro65-p.Pro69; p.Pro74-p.Pro80)
 * BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene.

### 参考附件
- [PVS1 Flowchart for FOXG1](https://cspec.genome.network/cspec/File/id/99c012f0-650e-4e4b-ae47-6c31a46864fb/data)
- [Clinical Phenotype Guidelines for FOXG1](https://cspec.genome.network/cspec/File/id/0f44c3a0-b4cd-4a92-8ab0-84a3e7e3561b/data)
- [FOXG1 Functional Assays](https://cspec.genome.network/cspec/File/id/ca55d8a5-88e8-4801-9ddb-066c170e6894/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN035)

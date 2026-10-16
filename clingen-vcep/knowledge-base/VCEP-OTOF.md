# ClinGen VCEP基因特异性规范：OTOF

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN023 — Hearing Loss Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0019497**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Null variant in a gene with established LOF as a disease mechanism; see PVS1_Strong, PVS1_Moderate, PVS1_Supporting for reduced evidence applications.
PVS1 should also be considered for both of the genes OTOF and MYO15A with variants falling in two exons being exceptions to this rule: OTOF: NM_194248.2 Exon 46 (c.5841 to c.5994; PMID: 19250381) and MYO15A: NM_016239.3 Exon 8 (c.4033 to c. 4038; PMID: 10552926) and Exon 26 (c.5911 to c.5964; PMID: 30096381 and high frequency LOF variant https://gnomad.broadinstitute.org/variant/17-18046894-G-A?dataset=gnomad_r2_1)
- **Strong** 📋：See PVS1 flow chart for PVS1_Strong variants in gene where LOF is a known mechanism of disease.
- **Moderate** 📋：See PVS1 flowchart for PVS1_Moderate variants in gene where LOF is a known mechanism of disease.
- **Supporting** 📋：See PVS1 flowchart for PVS1_Supporting variants in gene where LOF is a known mechanism of disease.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Same amino acid change as an established pathogenic variant; OR splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant.
* Established variant must meet criteria for pathogenicity by the HL specifications.
* Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant.
  * Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T.
* No additional hearing loss specifications for missense variants. Follow recommendations as outlined in Richard 2015 and/or the Sequence Variant Interpretation working group within ClinGen.
* Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：4 points per tables 5a and 5b:
Examples: 2 proven de novo occurrences; OR
1 proven + 2 assumed de novo occurrences; OR
4 assumed de novo occurrences.
- **Strong** 📋：2 points per tables 5a and 5b:
Examples: 1 proven de novo occurrence; OR 2 assumed de novo occurrences.

* OTOF and MYO15A are associated with autosomal recessive conditions. Therefore, de novo variants are expected to be an unlikely occurrence. It is recommended that de novo evidence is only awarded when phase with another variant (VUS, Likely Pathogenic, or Pathogenic) can be confirmed in trans. This is to avoid inappropriately awarding de novo evidence, which would lead to potentially incorrect classification.

* Follow recommendations as specified by the Sequence Variant Interpretation working group within ClinGen, as outlined below
  
* Determine number of points per proband using table 1 below. Sum the total number of points for all probands, and determine the strength of the evidence by using table 2.

  * Please note, the phenotype for de novo occurrences for MYO15A and OTOF are not considered “highly specific”.
- **Moderate** 📋：1 point per tables 5a and 5b:
Examples: 1 proven de novo occurrence (phenotype consistent but not specific to gene); OR
1 assumed de novo occurrence; OR 2 assumed de novo occurrences (phenotype/gene not specific).
- **Supporting** 📋：0.5 points per tables 5a and 5b:
Example: 1 assumed de novo occurrence (phenotype/gene not specific).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Knock-in mouse model demonstrates the phenotype.
* Recommend that functional evidence, except for a variant specific mouse model, is not used as strong evidence, due to the absence of well-established functional studies for hearing loss genes.
* There are no specific assays for OTOF or MYO15A. However, PS3_Supporting can be applied for other functional analyses if
  * The assay has been validated by a known pathogenic and benign variant AND
  * There is plausible reason that the function the assay is testing relates to the phenotype AND
  * The assay conditions are likely to mimic the physiological environment.
- **Moderate** 📋：Validated functional studies show a deleterious effect (none are defined for OTOF and MYO15A).
- **Supporting** 📋：Functional studies with limited validation show a deleterious effect.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：Fisher Exact or Chi-Squared analysis shows statistical increase in cases over controls.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：Mutational hot spot or well-studied functional domain without benign variation (None defined for OTOF and MYO15A).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Absent/Rare in population databases (absent or ≤0.00007 (0.007%) for autosomal recessive).

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：4 points awarded from tables 7a and 7b.
Example: Detected in trans in ≥4 probands with a pathogenic variant (recessive).
- **Strong** 📋：2 points awarded from tables 7a and 7b.
Example: Detected in trans in 2 probands with a pathogenic variant (recessive).
- **Moderate** 📋：1 point awarded from tables 7a and 7b
Example: Detected in trans with a pathogenic variant (recessive).
- **Supporting** 📋：0.5 points awarded from tables 7a and 7b
Examples: 
Two variants that meet PM2_Supporting detected in trans; OR
a homozygous variant meeting PM2_Supporting.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Protein length change due to an in-frame deletion or insertion that are not located in repetitive regions.
No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Missense change at same codon as two different pathogenic missense variants.
Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria for based on independent data).
* Caveat: Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.
- **Moderate** 📋：Missense change at same codon as another pathogenic missense variant.
No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：See PS2 above.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Segregation in three affected relatives for recessive.
- **Moderate** 📋：Segregation in two affected relatives for recessive.
- **Supporting** 📋：Segregation in one affected relative for recessive.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan.
* Use REVEL and MAXENTSCAN
 * For missense variants, award PP3 if REVEL score is ≥0.7
 * If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3
* For splice variants (except for canonical -/+1 or 2), use MAXENTSCAN.
  * For -/+ 1 or 2 splice variants, do not use PP3 if you are using PVS1

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** 📋：Patient's phenotype highly specific for gene or fully sequenced gene set (see specifications in Table 7).
* The HL-EP applied this rule to HL syndromes if all causative genes have been sequenced and the detection rate at least doubles when the added clinical feature is present.
* See table below for applicable gene-disease phenotypes.
* Advise against using PP4 for patients with nonsyndromic or apparently nonsyndromic hearing loss, given genetic heterogeneity.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：MAF of ≥0.005 (0.5%) for autosomal recessive.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Very Strong** 📋：MAF of ≥0.003 (0.3%) for autosomal recessive. Likely benign, provided there is no conflicting evidence.
- **Supporting** 📋：MAF of ≥0.0007 (0.07%) for autosomal recessive.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Observation of variant (biallelic with known pathogenic variant for recessive) in controls inconsistent with disease penetrance.
* Advise caution when using this rule, since most of hearing loss is autosomal recessive, and autosomal dominant hearing loss could display reduced penetrance or variable expression.
* However, if biallelic observations in controls are inconsistent with disease penetrance, this may be applicable. Ensure age of the unaffected individual is appropriate. MYO15A and OTOF are expected to cause congenital or childhood onset hearing loss. Therefore, an adult (ie >18 years) may be an appropriate individual to consider application of this criteria. Please see additional considerations listed under BS4 “Genotype+/phenotype-”.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：Functional study shows no deleterious effect (none are defined for OTOF and MYO15A).
* Recommend that functional evidence is not used as strong evidence, due to the absence of well-established functional studies for hearing loss genes.

* No specific assays are listed for OTOF or MYO15A. However, BS3_Supporting can be used for functional analyses if
  * The assay has been validated by a known pathogenic and benign variant AND
  * There is plausible reason that the function the assay is testing relates to the phenotype AND
  * The assay conditions are likely to mimic the physiological environment.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Non-segregation with disease.
* Phenotype+/genotype-
 * Strong evidence for benign.
 * Be cautious when using this as the possibility for phenocopy is high. The hearing loss phenotype should be consistent within the family to consider it a non-segregation, though intra-familial variability has been reported. Factors to consider are:
  * Age of onset (ie. congenital/early childhood vs. adult onset)
   * Hearing loss prevalence increases significantly with age. A congenital hearing loss in a child and a late onset hearing loss in a grandparent would not be a consistent phenotype.
  * Severity (ie - mild vs. profound)
   * Minor differences may exist among family members.
   * Keep in mind that progression in older individuals may account for a discrepancy between individuals.
  * Audiogram shape
   * May not be completely consistent among family members even with same etiology.
- Genotype+/phenotype-
* Confounding variables to applying this rule: Age-related penetrance, variable expressivity, etc.
* If the gene is associated with later onset and individual with the non-segregation is beyond the expected age that the hearing loss would occur, consider applying BS4_Supporting
.
* Recommend only using for fully penetrant genes (typically genes associated with AR hearing loss)
o Must be confident that patient is truly unaffected and a hearing loss is not missed or subclinical. Be cautious if only phenotyping was newborn hearing screening. Diagnostic audiometric testing (auditory brainstem response (ABR) or audiogram should be required).

* Any evidence for reduced penetrance, do not use BS4.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in trans with a dominant variant/observed in cis with a pathogenic variant (use with caution).
* Use with caution. For genes that are associated with both dominant and recessive hearing loss, consider whether an earlier onset/more severe phenotype could be present if variant is identified in trans with a dominant variant.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** 📋：In-frame indels in repeat region without known function.
* No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Computational evidence suggests no impact; REVEL score ≤0.15 or no impact to splicing in MaxEntScan.
* Use REVEL, award BP4 if score is 0.15 or lower. Make sure to also check MAXENTSCAN to rule out the creation of a cryptic splice site.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Silent variant with no predicted impact to splicing.
* No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

### 不适用证据码
PP2、PP5、BP1、BP5、BP6

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN023)

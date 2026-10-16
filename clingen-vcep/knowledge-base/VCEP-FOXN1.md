# ClinGen VCEP基因特异性规范：FOXN1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.3（2026-06-01，SCID VCEP）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN113 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0011132**（遗传方式：Semidominant inheritance）

### 通用说明
All observations of FOXN1 variants may be curated under this single set of specifications and classified for T-cell immunodeficiency, congenital alopecia, and nail dystrophy with semidominant inheritance.

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical forkhead domain (amino acids 270-367; Newman et al., 2020; PMID: 31914405) based on recommendations from Walker et. al., 2023 (PMID: 37352859).
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications:

*   For variants not predicted to undergo nonsense-mediated decay, but removing >10% of protein, (i.e. variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), at least one pathogenic variant must be present downstream in order to apply PVS1\_Strong
*   PVS1\_Strong can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the transactivation domain (amino acids 511-563; Schlake et al., 2000 PMID: 10767081).
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay, but removing >10% of protein, (i.e. variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), when at least one pathogenic variant is not present downstream downgrade to PVS1\_Moderate

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Applicable for a same amino acid change if previously established variant is classified as pathogenic by SCID VCEP specifications for _FOXN1._

Can also be applied for variants with the same predicted splicing event as a known Pathogenic variant (as classified by the SCID VCEP specifications for _FOXN1_), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: [37352859](https://pubmed.ncbi.nlm.nih.gov/37352859)) for determining when PS1 should be applied at PS1\_Strong, \_Moderate, or \_Supporting.
- **Moderate** ✅：Applicable for a same amino acid change if previously established variant is classified as likely pathogenic by SCID VCEP specifications for _FOXN1._

Can also be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (as classified by the SCID VCEP specifications for _FOXN1_), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: [37352859](https://pubmed.ncbi.nlm.nih.gov/37352859)) for determining when PS1 should be applied at PS1\_Strong, \_Moderate, or \_Supporting.
- **Supporting** ✅：Can be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (as classified by the SCID VCEP specifications for _FOXN1_), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: [37352859](https://pubmed.ncbi.nlm.nih.gov/37352859)) for determining when PS1 should be applied at PS1\_Strong, \_Moderate, or \_Supporting.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：PS3 may be applied at the strong level for evidence from an animal model expressing the variant of interest and recapitulating FOXN1 deficiency (i.e. a mouse model with T cell lymphopenia).
- **Moderate** ✅：PS3 may be applied at the moderate level based on a luciferase assay showing reduced (\<50%) activity, as part of a validated assay with pathogenic and benign controls (PMID: 37419334).
- **Supporting** ✅：PS3 may be applied at the supporting level based on a luciferase assay, without sufficient validation controls, showing reduced (\<50%) activity, such as those reported in PMIDs: 31566583, 33464451, 34860543.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Sum of case scores ≥8 points (see instructions below)
- **Strong** ✅：Sum of case scores 4-7.75 points (see instructions below)
- **Moderate** ✅：Sum of case scores 2-3.75 points (see instructions below)
- **Supporting** ✅：Sum of case scores 1-1.75 points (see instructions below)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Applicable for variants in the DNA binding forkhead domain (amino acids 270-367), which is a well-established functional domain (Newman et al., 2020; PMID: 31914405) of _FOXN1_ with low tolerance for benign variation.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD Grpmax filtering allele frequency ≤0.00002412

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Sum of case scores ≥8 points (see instructions below)
- **Strong** ✅：Sum of case scores 4-7.75 points (see instructions below)
- **Moderate** ✅：Sum of case scores 2-3.75 points (see instructions below)
- **Supporting** ✅：Sum of case scores 1-1.75 points (see instructions below)

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Additional requirement that when applied to deletion variants, the deleted region must contain a known pathogenic or likely pathogenic variant that is not predicted/observed to alter splicing.
- **Supporting** ✅：Additional requirement that when applied to deletion variants, the deleted region must contain a known VUS variant that is not predicted/observed to alter splicing.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5\_Strong should be downgraded to PM5\_Moderate if PVS1 is applied at any strength. 

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.
- **Moderate** ✅：Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5\_Supporting if previously established variant is classified as likely pathogenic.   
PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5\_Moderate may not be combined with PVS1\_VeryStrong (should be downgraded to PM5\_Supporting if PVS1\_VeryStrong is applied).

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.
- **Supporting** ✅：Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5\_Supporting if previously established variant is classified as likely pathogenic. Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Can be applied when there is a 32:1 likelihood ratio (LOD score ≥1.5, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a. See instructions for calculating the estimated LOD score.
- **Moderate** ✅：Can be applied when there is a 16:1 likelihood ratio (LOD score 1.2-\<1.5, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a. See instructions for calculating the estimated LOD score.
- **Supporting** ✅：Can be applied when there is a 4:1 likelihood ratio (LOD score 0.6-\<1.2, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a. See instructions for calculating the estimated LOD score.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Moderate evidence can be applied for a REVEL score of ≥0.932, downgraded from the recommendation of Strong in Pejaver et al., 2022 (PMID: 36413997).
- **Supporting** ✅：*   Supporting evidence can be applied for a REVEL score of ≥0.644 (to \<0.932), based on recommendations of Pejaver et al., 2022 (PMID: 36413997).
*   Also applicable to missense, synonymous, or intronic variants predicted to impact splicing by SpliceAI ∆ score ≥0.2

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Patient score of ≥2 points (see instructions below)
- **Supporting** ✅：Patient score of 1-\<2 points (see instructions below)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD Grpmax filtering allele frequency >0.00447

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD Grpmax filtering allele frequency >0.00141 OR a bottle-necked population with a MAF >0.00141 may be used for this criterion. Caveat: If the variant is known to be a founder variant in the bottle-necked population do not consider the frequency in that population for BS1.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Applicable only when observed in cis with a pathogenic variant in any inheritance pattern, with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _FOXN1._

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：•Supporting evidence can be applied for a REVEL score of \<0.290 based on recommendations of Pejaver et al., 2022 (PMID: 36413997).

•Also applicable to synonymous or intronic variants not predicted to impact splicing by SpliceAI ∆ score ≤0.1

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Use with no specification.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant, or deep intronic variant affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions, for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site (SpliceAI ∆ score ≤0.1) AND the nucleotide is not highly conserved.

### Rules for Combining Criteria

> 证据码强度集合：
> - Very Strong = (PVS1, PS2_Very Strong, PS4_Very Strong, PM3_Very Strong)
> - Strong = (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong)
> - Moderate = (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
> - Supporting = (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)

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
- 1 Strong AND 2 Moderate
- 1 Very Strong AND 1 Supporting

#### Benign
- ≥ 2 Strong (BS1, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- ≥ 2 Supporting (BP2, BP4, BP5, BP7)
- 1 Strong (BS1, BS4)

### 不适用证据码
PP2、PP5、BS2、BS3、BP1、BP3、BP6
### 参考附件
- [PS3](https://cspec.genome.network/cspec/File/id/b2fd1113-2754-4a6c-8935-e3be2e2e6e2e/data)
- [FOXN1 Corrections](https://cspec.genome.network/cspec/File/id/8b6d2445-9170-4780-903e-c7fbb5913037/data)
- [PVS1 flowchart](https://cspec.genome.network/cspec/File/id/494f7894-af60-4e69-ab33-f465faa40947/data)
- [PS2_PM6](https://cspec.genome.network/cspec/File/id/ed8cad6d-59a5-44ee-8b31-5ec046107cfd/data)
- [PS1_Splice](https://cspec.genome.network/cspec/File/id/dcc73737-2b5c-47f8-a33d-3ad04e73304c/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN113)

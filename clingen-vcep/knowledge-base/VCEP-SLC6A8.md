# ClinGen VCEP基因特异性规范：SLC6A8

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> VCEP版本标注：Version 2.1（2026-07-06 发布；Release Notes：删除SVI响应附件，规则内容较 v2.0 无实质变化；Tavtigian 2020 贝叶斯积分法，PMID:32720330）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN027 — Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010305**（遗传方式：X-linked inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：*   See attached PVS1 decision tree, adapted from Tayoun, et.al. 2018 \[PMID:30192042\] for nonsense, frameshift, predictions for canonical splice variants, deletions, duplications and initiation codon variants.
*   See attached PVS1 decision tree, adapted from Walker, et. al. 2023 \[PMID:37352859\] for observed RNA splicing defects from functional splicing assays (minigene assay, RNA Sequencing, transcriptome analysis, etc) \[PMID: 39418753\]
- **Strong** 📋：*   See attached PVS1 decision tree, adapted from Tayoun, et.al. 2018 \[PMID:30192042\] for nonsense, frameshift, predictions for canonical splice variants, deletions, duplications and initiation codon variants.
*   See attached PVS1 decision tree, adapted from Walker, et. al. 2023 \[PMID:37352859\] for observed RNA splicing defects from functional splicing assays (minigene assay, RNA Sequencing, transcriptome analysis, etc) \[PMID: 39418753\]
- **Moderate** 📋：*   See attached PVS1 decision tree, adapted from Tayoun, et.al. 2018 \[PMID:30192042\] for nonsense, frameshift, predictions for canonical splice variants, deletions, duplications and initiation codon variants.
*   See attached PVS1 decision tree, adapted from Walker, et. al. 2023 \[PMID:37352859\] for observed RNA splicing defects from functional splicing assays (minigene assay, RNA Sequencing, transcriptome analysis, etc) \[PMID: 39418753\]
- **Supporting** 📋：*   See attached PVS1 decision tree, adapted from Tayoun, et.al. 2018 \[PMID:30192042\] for nonsense, frameshift, predictions for canonical splice variants, deletions, duplications and initiation codon variants.
*   See attached PVS1 decision tree, adapted from Walker, et. al. 2023 \[PMID:37352859\] for observed RNA splicing defects from functional splicing assays (minigene assay, RNA Sequencing, transcriptome analysis, etc) \[PMID: 39418753\]

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：PS1 is applicable as described.

*   PS1 may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region.  See “PS1\_SpliceVariants” for applicable points, from Walker, [et.al](http://et.al). PMID:37352859
*   Splice AI score must be \<0.1 for both the variant under review and the previously reported variant to apply this code.
- **Moderate** 📋：*   PS1 is applicable as described 
*   PS1\_Moderate may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region.  See “PS1\_SpliceVariants” for applicable points
- **Supporting** 📋：*   PS1 is applicable as described
*   PS1\_Supp may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region.  See “PS1\_SpliceVariants” for applicable points

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** 📋：Is applicable in the case of a hemizygous male or a heterozygous female minimally meeting PP4\_Supporting with a de novo variant

*   confirmation of maternity only is sufficient in male probands
*   confirmation of both maternity and paternity is necessary in female probands
- **Moderate** 📋：Is applicable in the case of a newly hemizygous male with variant identified de novo in asymptomatic mother when one of the following conditions are met

*   Identified in male proband minimally meeting PP4\_Supporting if the biological mother (asymptomatic or affected) has a de novo SLC6A8 variant confirmed by parental testing in her parents
*   Identified in male proband minimally meeting PP4\_Supporting if the biological mother (asymptomatic or affected) has a mosaic SLC6A8 (≤30% variant allele frequency)

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Moderate** 📋：Creatine transport deficient mouse models have biochemical findings including reduced/absent creatine in brain \[PMID:21249153, 25485098, 33389772\], which has been recapitulated in brain-specific creatine transport knockout models \[PMID:22751104\].  PS3\_Moderate is applicable when the variant under review is used to generate a mouse knock-in model and assessment of brain creatine demonstrates significantly reduced or absent brain creatine when compared to wildtype littermates.
- **Supporting** 📋：Creatine transport assay using site directed mutagenesis to introduce the variant under review into _SLC6A8_ deficient cell line, and results in \<10% creatine transport compared to wildtype cells when using ≤125uM creatine, or ≤25% when using creatine >125uM.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：*   8 independent probands with elevated urine creatine/creatinine ratio on one  occasion at minimum, in addition to any proband used for PP4. 
*   Affected females may be counted if meeting PP4\_Supporting
*   Variant must meet PM2\_Supporting criterion for PS4 to apply.
- **Strong** 📋：*   4 independent probands with elevated urine creatine/creatinine ratio on one  occasion at minimum, in addition to any proband used for PP4. 
*   Affected females may be counted if meeting PP4\_Supporting
*   Variant must meet PM2\_Supporting criterion for PS4 to apply.
- **Moderate** 📋：*   2 independent probands with elevated urine creatine/creatinine ratio on one  occasion at minimum, in addition to any proband used for PP4. 
*   Affected females may be counted if meeting PP4\_Supporting
*   Variant must meet PM2\_Supporting criterion for PS4 to apply.
- **Supporting** 📋：*   1 independent proband with elevated urine creatine/creatinine ratio on one  occasion at minimum, in addition to any proband used for PP4. 
*   Variant must meet PM2\_Supporting criterion for PS4 to apply.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Applicable when Grpmax Filtering Allele Frequency is ≤0.00002 (0.002%) AND 0 homo- or hemizygotes are present in the most current version of gnomAD available at the time of curation

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Protein length changes as a result of in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：*   Same as described.
*   Splice AI score must be \<0.1 for both the variant under review and the previously reported variant to apply this code.
- **Supporting** 📋：Novel missense change at an amino acid residue where a different missense change determined to be Likely pathogenic has been seen before.  Example: Arg156His is Likely pathogenic; now you observe Arg156Cys

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：See criteria in PS2.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：4 segregations
- **Moderate** 📋：*   2 segregations
- **Supporting** 📋：*   1 segregations

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Applicable for missense variants with REVEL >0.75
*   Applicable for canonical splice, splice region, or deep intronic variants with SpliceAI delta score ≥0.20

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** 📋：See attached PP4 table for phenotypes in males and/or female probands required to meet PP4 criteria. Point total for applicable PP4 criteria should be summed.

**PP4\_Strong (+4):** = 4 points  

*   Two or more data types are required to reach strong. 
*   An individual used to assign PP4, at any weight, cannot be also included for PS4 count. If multiple  unrelated probands with the variant have been identified, it is recommended that the case with the  highest PP4 points is assigned the appropriate weight for PP4, and the other cases are used for PS4.
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength. 
*   For PP4 to be applied at strong, full _SLC6A8_ gene sequencing, including all coding exons and intron/exon boundaries must have been carried out. If not, downgrade by one strength level.
*   Total locus evidence for PP1+PP4 must be capped at 5.0 points per allele
- **Moderate** 📋：See attached PP4 table for phenotypes in males and/or female probands required to meet PP4 criteria. Point total for applicable PP4 criteria should be summed.

**PP4\_Moderate (+2):** = 3 points

*   An individual used to assign PP4, at any weight, cannot be also included for PS4 count. If multiple  unrelated probands with the variant have been identified, it is recommended that the case with the  highest PP4 points is assigned the appropriate weight for PP4, and the other cases are used for PS4.
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength.
*   Total locus evidence for PP1+PP4 must be capped at 5.0 points per allele
- **Supporting** 📋：See attached PP4 table for phenotypes in males and/or female probands required to meet PP4 criteria. Point total for applicable PP4 criteria should be summed.

**PP4** (+1): = 1-2 points 

*   An individual used to assign PP4, at any weight, cannot be also included for PS4 count. If multiple  unrelated probands with the variant have been identified, it is recommended that the case with the  highest PP4 points is assigned the appropriate weight for PP4, and the other cases are used for PS4.
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength.
*   Total locus evidence for PP1+PP4 must be capped at 5.0 points per allele

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Applicable when Grpmax Filtering Allele Frequency is ≥0.002 (0.2%) OR ≥10 homo- or hemizygotes (or the sum of total hemi- and homozygotes) are present in the most current version of gnomAD available at the time of curation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Applicable when Grpmax Filtering Allele Frequency is ≥0.0002 (0.02%)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Applicable when the variant is observed in ≥2 homo- or hemizygotes in the most current version of gnomAD available at the time of curation OR the variant is identified in a male with documented normal urine creatine/creatinine ratio

*   BS1 and BS2 should not be co-applied based on the number of homo- or hemizygotes present in gnomAD
- **Supporting** 📋：Can be used if the variant is identified in a male with creatine transport studies ≥80% compared to wildtype if ≤125uM creatine was used in the study.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：*   Creatine transport assay demonstrating ≥50% normal transport activity compared to controls when using ≤125uM creatine.  Any study using >125uM creatine for creatine transporter assays cannot be used as Benign evidence.
*   RT-PCR evidence demonstrating no observable effect of splicing for canonical splice, splice region, and deep intronic variants
*   Expression assay demonstrating wildtype transcript levels

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Asymptomatic, variant positive females should NOT be used as benign segregation evidence

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   REVEL score ≤ 0.20
*   For variants potentially impacting splicing, Splice AI score \<0.10

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：Use as described.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site 

*   SpliceAI score ≤0.10
*   May also be applied in conjunction with PB4 for an intronic variant outside the splice region (beyond -4bp or +7 bp)

### 不适用证据码
PM1、PM3、PP2、PP5、BP1、BP2、BP3、BP6
### 参考附件
- [SLC6A8 PP4 V2](https://cspec.genome.network/cspec/File/id/f44b46ad-2724-46e6-9c3a-352edb57745f/data)
- [SLC6A8 PS1 Splice Variants](https://cspec.genome.network/cspec/File/id/668182ae-c5f3-48c0-94fc-b57b30fc486f/data)
- [SLC6A8_PVS1_v2.1_033026](https://cspec.genome.network/cspec/File/id/3f531dd9-769b-4936-82ae-5ed359811447/data)
- [SLC6A8 Functional Assay SVI documentation](https://cspec.genome.network/cspec/File/id/fbedc952-741b-48fe-ac90-a1adbc82a841/data)
- [SLC6A8_Bayesian Points System_033026](https://cspec.genome.network/cspec/File/id/cef623a8-f1ae-45e0-bb89-385a59ec1dfe/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN027)

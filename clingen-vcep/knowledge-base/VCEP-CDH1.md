# ClinGen VCEP基因特异性规范：CDH1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN007 — Gastric Cancer Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0007648**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Per modified CDH1 PVS1 decision tree.
- **Strong** 📋：Per modified CDH1 PVS1 decision tree.
Other CDH1 caveats:
 * Use PVS1_Strong as the default strength of evidence for canonical splice site variants and follow the site-specific recommendations in the splicing table. 
 * CDH1 Exonic deletions or tandem duplications of in-frame exons (exon 4,5,8,9,12,13,15).
- **Moderate** 📋：Per modified CDH1 PVS1 decision tree.
Other CDH1 caveats:
 * G to non-G variants disrupting the last nucleotide of an exon.
 * Canonical splice sites predicted or demonstrated experimentally to result in in-frame partial skipping/insertion (e.g., Exon 3 donor site).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：≥Two patients meet the HDGC individual phenotype criteria w/ parental confirmation.
- **Strong** 📋：One patient meets the HDGC individual phenotype criteria w/ parental confirmation.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：RNA assay demonstrating abnormal out-of-frame transcripts.
- **Moderate** 📋：RNA assay demonstrating abnormal in-frame transcript.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：≥Sixteen families meet HDGC criteria.
- **Strong** 📋：Four - Fifteen families meet HDGC criteria.
- **Moderate** 📋：Two - three families meet HDGC criteria.
- **Supporting** 📋：One family meets HDGC criteria.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：≤ One out of 100,000 alleles in gnomAD cohort; if present in ≥2 individuals within a subpopulation, must be present in ≤ One out of 50,000 alleles.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Only apply to stop-loss variants
Variant example: CDH1 c.2647T>C (p.Ter883Glnext*29).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** 📋：PM5_supporting is applicable to nonsense and frameshift variants that are predicted/proved to undergo NMD or located upstream of the last known pathogenic truncating variant. Site-specific recommendations for the application of PM5_Supporting for canonical splicing variants.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** 📋：Four patients meet the HDGC individual phenotype criteria w/o parental confirmation.
- **Strong** 📋：≥Two patients meet the HDGC individual phenotype criteria w/o parental confirmation.
- **Moderate** 📋：One patient meets the HDGC individual phenotype criteria w/o parental confirmation

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：≥Seven informative meioses across ≥2 families.
- **Moderate** 📋：Five-six informative meioses across ≥1 family.
- **Supporting** 📋：Three-four informative meioses across ≥1 family.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** 📋：Variants affecting the same splice site as a well-characterized variant with similar or worse in silico/ RNA predictions.
- **Supporting** 📋：At least three in silico splicing predictors in agreement (SpliceAI, MaxEntScan, SSF, GeneSplicer, HSF, TraP, varSEAK).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：MAF cutoff of 0.2%.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：MAF cutoff of 0.1%.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Variant seen in ≥10 individuals w/o GC, DGC, gSRC tumors, or LBC & whose families do not suggest HDGC.
- **Supporting** 📋：Variant seen in ≥3 individuals w/o GC, DGC, SRC tumors, or LBC & whose families do not suggest HDGC.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Functional RNA studies demonstrating no impact on transcript composition.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Per original ACMG/AMP guidelines.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** 📋：Variant observed in trans w/known pathogenic variant (phase confirmed) OR observed in the homozygous state in individual w/o personal &/or family history of DGC, LBC, or SRC tumors.
- **Supporting** 📋：Variant is observed in cis (or phase is unknown) w/ a pathogenic variant
OR observed in the homozygous state in gnomAD.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Splicing predictions only. At least three in silico splicing predictors in agreement (SpliceAI, MaxEntScan, SSF, GeneSplicer, HSF, TraP, varSEAK).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：Per original ACMG/AMP guidelines.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Synonymous and intronic variants at or beyond +7 to -21 locations.

### 不适用证据码
PS1、PM1、PM3、PP2、PP4、PP5、BP1、BP3、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN007)

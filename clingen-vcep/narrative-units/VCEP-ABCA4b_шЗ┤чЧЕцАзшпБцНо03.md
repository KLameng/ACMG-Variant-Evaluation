> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

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

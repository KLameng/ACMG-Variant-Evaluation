> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Use without disease-specific modification if case-control studies are available.   
While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for _DYSF_. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Apply if the Grpmax variant allele frequency / upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency in gnomAD is \<0.0001. Do not use data for which the variant does not pass quality control filters. 

*   If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
*   If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency


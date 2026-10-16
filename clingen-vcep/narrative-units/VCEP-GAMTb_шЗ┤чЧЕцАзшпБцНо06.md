> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：PS3\_Supporting can be assigned if a variant is expressed in GAMT-deficient fibroblasts, HeLa cells and has \<15% of the control value, for values published in Mercimek-Mahmutoglu et al, 2014, PMID 24415674; Mercimek-Mahmutoglu et al, 2016, PMID 26319512; or DesRoches et al, 2016, PMID 26003046.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：**Allele frequency \<0.0004 (\<0.04%) in all populations in gnomAD.**

It is acceptable for a GAMT variant to be present in controls, if heterozygous, because GAMT-D is a recessive disorder. Homozygotes should not be seen in a population database, such as gnomAD, because the penetrance of this condition in individuals with biallelic pathogenic variants is expected to be 100% and the condition is expected to present with severe symptoms early in life.

GAMT specifications:

*   All subpopulations in gnomAD v4.0 must have a maximum allele frequency less than 0.0004 (the highest population minor allele frequency of the most common pathogenic GAMT variant, c.327G>A, in gnomAD). Any variant with a frequency below this cutoff will meet PM2\_Supporting.
*   If homozygotes are observed, or variant is confirmed in trans with a known pathogenic variant, the variant will meet BS2 (assuming 100% penetrance for an individual with 2 pathogenic variants in trans).



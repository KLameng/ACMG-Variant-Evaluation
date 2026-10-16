> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：Case-control studies; p-value ≤.05 AND (Odds ratio, hazard ratio, or relative risk  ≥3 OR lower 95% CI ≥1.5).


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Frequency ≤ 1/300,000 (**0.000333%**) in gnomAD v4 dataset


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

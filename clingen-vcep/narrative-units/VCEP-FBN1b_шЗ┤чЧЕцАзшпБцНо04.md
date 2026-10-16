> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：* Threshold: <5.0E-6 (<0.0005%).
* Use the highest ethnic population allele frequency.
* Caveat: PVS1 + PM2_Supportive may reach Likely Pathogenic.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：* Add caveat: cannot be applied simultaneously with PVS1 (at any strength level)


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：* Add caveat: Use argument with caution when the original missense variant created a cysteine especially in a cbEGFlike domain (cfr PM1_strong) as this may increase the
pathogenicity level of this variant improperly.
* Add caveat: original variant should be pathogenic according to the (modified) ACMG guidelines for variant classification.


#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** 📋：4 points
- **Strong** 📋：2-3 points.
- **Moderate** 📋：1 point.
- **Supporting** 📋：0.5 points.


#### PP1
- 默认强度：Pathogenic Supporting

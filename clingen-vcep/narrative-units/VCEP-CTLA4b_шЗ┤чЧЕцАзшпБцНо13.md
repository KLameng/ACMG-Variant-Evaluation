> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Met for total allele frequency lower than 1.43 x 10<sup>-7</sup> (0.000000143) across all populations in gnomAD v4.1.0.
*   Threshold is based on the experts’ estimate of CTLA-4 insufficiency prevalence of 1/200,000 – 1/1,000,000 people and 45-70% penetrance. The lower end of the prevalence estimate (1 in 1,000,000) and the higher end of the penetrance estimate (70%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data) but can be used together with PM1.
*   Met at default strength (PM4) by an in-frame deletion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is \<0.2.
*   Met at default strength (PM4) by an in-frame insertion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is \<0.2.
*   The region of the protein affected by the variant is key to consider. If variants within this region occur in healthy populations, the region is polymorphic. Incomplete penetrance should also be considered as a caveat for polymorphism.


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.

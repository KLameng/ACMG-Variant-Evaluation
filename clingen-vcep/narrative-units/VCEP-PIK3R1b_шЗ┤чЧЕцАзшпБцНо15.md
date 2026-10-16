> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：*   Used at PM2\_Supporting strength.
*   Applicable to variants with a total allele frequency \<0.00000132 across all populations in gnomAD v4.1.0.
*   Population allele frequency threshold has been determined using the Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for primary immunodeficiency and the inheritance tailored to the autosomal dominant mode of inheritance):
    *   Prevalence: 1 in 4000
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 0.95


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data).
*   Met at default strength (PM4) by an **in-frame deletion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (PhyloP score greater than or equal to 2.0).
*   Met at default strength (PM4) by an **in-frame insertion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (PhyloP score greater than or equal to 2.0).
*   Met at default strength (PM4) by a **stop-loss variant** resulting in the addition of 2 or more amino acids to the C-terminus.
*   The region of the protein affected by the variant is key to consider. If only benign or likely benign variants are known to be located within this region, the region is polymorphic and PM4 does not apply.


#### PM5
- 默认强度：Pathogenic Moderate

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

1.  Alternatively, this is equivalent to the variant NOT being observed more than once (≤1 allele) in gnomAD v.2.1.1 in one of the non-founder populations (e.g., absence required from the Other and Ashkenazi Jewish subpopulations).
2.  Applying a threshold of ≤0.00004 (upper bound of 95% CI of the allele frequency in gnomAD) is equivalent to the variant being seen in a single subpopulation and that subpopulation meets any of the following:
    *   **Allele Count (AC) in Allele Number (AN)**
    *   ≤1 in ≥120,000
    *   ≤2 in ≥160,000
    *   ≤3 in ≥195,000
    *   ≤4 in ≥230,000

gnomAD is the preferred database for this calculation, but currently only displays the filtering allele frequency (FAF), which is equivalent to a lower bound estimate of the 95% CI, when the upper bound is what is needed.

*   Confidence interval tools, such as [Confit-de-MAF](https://www.genecalculators.net/confit-de-maf.html), can be used to determine the upper bound of the 95% CI of the observed allele frequency.

Due to current technical limitations of next generation sequencing technologies, minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented in population databases.

Caution should be used when a variant is only identified, or over-represented, in one of the smaller gnomAD populations, as the gnomAD allele frequencies may not accurately represent the true population frequency.

Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

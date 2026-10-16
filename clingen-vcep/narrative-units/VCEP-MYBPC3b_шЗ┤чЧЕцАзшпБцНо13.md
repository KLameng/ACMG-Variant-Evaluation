> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：The values used to calculate the PM2 thresholds were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/500 or lower), where the most frequent pathogenic variant accounts for no more than 2% of cases (e.g., has an allele frequency of ≤0.02 in cases based on the upper bound of 95% CI), and where the penetrance of a pathogenic variant is expected to be at least 50% (Kelly _et al._ 2018[<sup>15</sup>](#pmid_29300372)).

A threshold of **≤0.00004** in the subpopulation with the highest frequency when using the upper bound of the 95% CI activates this rule.

1.  Alternatively, this is equivalent to the variant NOT being observed more than once (≤1 allele) in gnomAD v.2.1.1 in one of the non-founder populations (e.g., absence required from the Other and Ashkenazi Jewish subpopulations).
2.  Applying a threshold of ≤0.00004 (upper bound of 95% CI of the allele frequency in gnomAD) is equivalent to the variant being seen in a single subpopulation and that subpopulation meets any of the following:
    *   **Allele Count (AC) in Allele Number (AN)**
    *   ≤1 in ≥120,000
    *   ≤2 in ≥160,000
    *   ≤3 in ≥195,000
    *   ≤4 in ≥230,000

gnomAD is the preferred database for this calculation, but currently only displays the filtering allele frequency (FAF), which is equivalent to a lower bound estimate of the 95% CI, when the upper bound is what is needed.

*   Confidence interval tools, such as [Confit-de-MAF](https://www.genecalculators.net/confit-de-maf.html), can be used to determine the upper bound of the 95% CI of the observed allele frequency.


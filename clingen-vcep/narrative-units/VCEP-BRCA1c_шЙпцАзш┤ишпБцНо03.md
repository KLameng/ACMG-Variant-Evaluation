> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Strong** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4 - LR ≤0.05:1

BS4\_VeryStrong – LR ≤0.00285:1
- **Moderate** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4\_Moderate - LR ≤0.23:1
- **Supporting** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4\_Supporting  - LR ≤0.48:1


#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Strong** ✅：**Apply BP1\_Strong** for silent substitution, missense or in-frame insertion, deletion or delins variants outside a (potentially) clinically important functional domain AND no splicing predicted (SpliceAI ≤0.1). As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857. See Specifications Figure1A and Appendix J for details.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

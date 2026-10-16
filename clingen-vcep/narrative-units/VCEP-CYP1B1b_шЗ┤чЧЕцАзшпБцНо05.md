> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：2 affected segregations or 1 affected segregation AND ≥ 5 unaffected segregations or ≥ 10 unaffected segregations.
- **Supporting** ✅：1 affected segregation or ≥ 5 unaffected segregations.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：For missense variants: REVEL score of ≥ 0.932
- **Moderate** ✅：For missense variants: REVEL score of 0.773-0.931
- **Supporting** ✅：For missense variants: SpliceAI ≥ 0.2 OR REVEL score of 0.644-0.772

For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI ≥ 0.2

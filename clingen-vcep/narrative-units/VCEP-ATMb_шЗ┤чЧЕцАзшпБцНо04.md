> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：AR Condition: Segregation in ≥3 affected relatives
- **Moderate** 📋：AR Condition: Segregation in 2 affected relatives
- **Supporting** 📋：AR Condition: Segregation in 1 affected relative


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: REVEL **\>.7333**
*   Splicing: Predicted impact via splicing (SpliceAI **≥0.2**) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites.

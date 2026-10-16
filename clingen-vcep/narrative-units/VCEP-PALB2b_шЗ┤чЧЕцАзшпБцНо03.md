> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** 📋：*   Apply to frameshifting or truncating variants with premature termination codons upstream of p.Tyr1183.
*   Apply to splice variants as with premature termination codons upstream of p.Tyr1183 where PVS1\_VS(RNA) is applied based on high quality observed splicing impact and must be NMD prone.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：*   AD Condition: LOD ≥1.26 or Bayes Factor (LR) ≥18:1
*   AR Condition: Segregation in ≥3 affected relatives
- **Moderate** 📋：*   AD Condition: LOD ≥.60 or Bayes Factor (LR) ≥4:1
*   AR Condition: Segregation in 2 affected relatives
- **Supporting** 📋：*   AD Condition: LOD ≥0.3 or Bayes Factor (LR) ≥2:1
*   AR Condition: Segregation in 1 affected relative


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: Do not use.
*   Splicing: Predicted impact via splicing (SpliceAI **≥0.2**) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites.

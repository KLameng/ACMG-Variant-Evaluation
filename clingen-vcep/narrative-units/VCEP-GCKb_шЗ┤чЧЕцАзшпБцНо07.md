> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/32 (5 meioses)
*   \>1 Family : ≤ 1/16 (4 meioses)
- **Moderate** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/16 (4 meioses)
*   \>1 Family : ≤ 1/8 (3 meioses)
- **Supporting** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/8 (3 meioses)
*   \>1 Family : ≤ ¼ (2 meioses)


#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** 📋：Apply to all missense variants in GCK. gnomAD missense constraint score for _GCK_ is 3.07 (observed/expected= 0.5), which is significant.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use REVEL score of ≥0.70 as supportive evidence of pathogenicity. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is at least 0.2[<sup>9</sup>](#pmid_32123317),[<sup>10</sup>](#pmid_30661751)


#### PP4

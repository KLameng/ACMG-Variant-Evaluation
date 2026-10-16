> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** 📋：Also applicable when in cis or trans with a likely pathogenic variant.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use a REVEL score of ≤0.15 as supportive evidence of no predicted impact on the gene or gene product. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is below 0.2[<sup>3</sup>](#pmid_30661751),[<sup>4</sup>](#pmid_32123317).


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：A variant in another monogenic diabetes gene is Pathogenic/Likely Pathogenic.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Apply BP7 when the predicted change from SpliceAI is below 0.2 AND phyloP100 way \< 2.0.

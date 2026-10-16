> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN019 — Glaucoma Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Allele frequency ≥ 0.01 in population databases.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Allele frequency ≥ 0.001 in population databases.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** 📋：Applies to variants showing solubility or secretion in functional assays for studies with OddsPath \<0.23 as per the SVI recommendations.
- **Supporting** 📋：Applies to variants showing solubility or secretion in functional assays for studies with OddsPath \<0.48 as per the SVI recommendations.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** 📋：REVEL score of ≤ 0.016
- **Moderate** 📋：REVEL score of 0.017-0.183
- **Supporting** 📋：*   For missense variants: REVEL score of 0.184-0.290
*   For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI ≤ 0.1


#### BP7
- 默认强度：Benign Supporting

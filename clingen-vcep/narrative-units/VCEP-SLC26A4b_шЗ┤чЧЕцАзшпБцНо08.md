> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan.
* Use REVEL and MAXENTSCAN.
 * For missense variants, award PP3 if REVEL score is ≥0.7.
 * If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3.
* For splice variants (except for canonical -/+1 or 2), use MAXENTSCAN.
 * For -/+ 1 or 2 splice variants, do not use PP3 if you are using PVS1.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** 📋：Patient's phenotype highly specific for gene or fully sequenced gene set (see specifications in Table 7).

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc)

*   REVEL and SpliceAI are the preferred predictors
*   Apply this code if REVEL score is greater than or equal to 0.75.
*   Use SpliceAI to look for a possible splicing defect. Apply this code if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is greater than or equal to 0.2 (PMID: 37352859).


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

*   QT prolongation above 480ms AND
*   Swimming-associated events OR
*   Treadmill stress test result (PMID: 21699858) OR
*   T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844)

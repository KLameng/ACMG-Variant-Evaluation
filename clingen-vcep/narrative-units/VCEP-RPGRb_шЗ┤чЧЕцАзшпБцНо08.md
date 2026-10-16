> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：Applies to missense variants with a REVEL score above 0.932, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the strong level.
- **Moderate** ✅：Applies to missense variants with a REVEL score between 0.773 and 0.931, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the moderate level.
- **Supporting** ✅：Applies to missense variants with a REVEL score between 0.644 and 0.772 that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2).

For variants with SpliceAI scores greater than or equal to 0.2, in the two first or last two bases in an exon or the 6 intronic bases flanking an exon, this code is met at the supporting level.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：\> 8 phenotype points required; two specific criteria must be met
- **Supporting** ✅：4-7 phenotype points required; one specific criterion must be met.

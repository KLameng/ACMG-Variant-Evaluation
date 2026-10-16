> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Not applicable to _KCNQ1_ due to biallelic cases (Jervell and Lange-Nielsen syndrome)


#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function

*   Not applicable to _KCNQ1_


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.) 

*   REVEL and SpliceAI are the preferred predictors
*   Apply this code for a missense variant if the REVEL score is \<0.25 AND no splicing defect is predicted according to SpliceAI.
*   Use SpliceAI to look for a possible splicing defect. Apply this code if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is \<0.1 (in addition to REVEL score \<0.25).
*   Apply this code for a synonymous or intronic variant if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is \<0.1 (PMID: 37352859).


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease


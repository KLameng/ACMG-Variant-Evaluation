> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

*   For missense variants use REVEL with a score ≤ 0.290.
*   For splice site variants use SpliceAI with a score ≤ 0.1.


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：Variant found in a case with an alternate molecular basis for disease.
* ≥3 cases with alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

*   1 case with alternate molecular basis for disease


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

*   Defined 'not highly conserved' regions in BP7 as those with PhastCons score \<1 and/or PhyloP score \<0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species.
*   For splice site variants use SpliceAI with a score ≤ 0.1.

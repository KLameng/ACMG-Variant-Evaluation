> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

*   Use when variant is found to be is cis with another pathogenic variant
*   The “in-cis” variant should also be curated by the Perox VCEP to apply rule.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants, use REVEL with a score of ≤ 0.5 AND SpliceAI with a score \< 0.1
*   For variants with splicing impact (exonic and intronic variants, not applicable for UTR variants), use SpliceAI with a score \< 0.1


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Can be applied to synonymous variants meeting BP4 criteria OR intronic variants meeting BP4 criteria and are beyond the Walker et. al. (PMID 37352859) defined splice region of +7/-21

*   Conservation does not have to be considered for this code to apply

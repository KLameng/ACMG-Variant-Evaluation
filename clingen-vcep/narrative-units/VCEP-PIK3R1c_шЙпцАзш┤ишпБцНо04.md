> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   BP4 is met by a missense variant with both REVEL less than or equal to 0.290 and CADD less than or equal to 21.5, as well as SpliceAI Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss \<0.1.
*   The VCEP will try to determine during the pilot whether higher strength levels of BP4 are appropriate for _PIK3R1_ variants.
*   BP4 is met by synonymous or intronic variants not predicted to impact splicing by SpliceAI (Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss \<0.1 (PMID: 37352859)).
*   BP4 can be used in combination with BP7 for synonymous or intronic variants without being considered double-counting (PMID: 37352859).


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：At least 2 cases with an alternative molecular basis for disease are required to mitigate the reliance on assertions of variant pathogenicity in genes outside of the purview of the Antibody Deficiencies VCEP.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：*   BP7\_Strong (RNA) is met by variants with experimental evidence of no impact on splicing.

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：**Stand Alone** criteria applies to:

Missense variants: REVEL ≤ 0.003 with SpliceAI ≤ 0.1

**Strong criteria** applies to:

Missense variants: REVEL between 0.004 and 0.016 with SpliceAI ≤ 0.1
- **Moderate** ✅：Applies to:

Missense variants: REVEL between 0.017 and 0.183 with SpliceAI ≤ 0.1
- **Supporting** ✅：Applies to:

Missense variants: REVEL between 0.184 and 0.290 with SpliceAI ≤ 0.1

or 

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Applies to splicing assay data demonstrating a variant is not associated with aberrantly spliced transcript(s) relative to transcript profiles in controls. See RS1 PVS1 Decision Tree.  As per Walker et al, 2023 (PMID 37352859) guidance.
- **Supporting** ✅：Applies to:

Synonymous variants or noncoding variants  with no impact on splicing (SpliceAI ≤ 0.1)

AND

PhyloP \< 0.1 for conservation

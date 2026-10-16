> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   One or both variants are absent in a similarly affected family member.


#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in cis with a Pathogenic variant.

*   Use code if the variant of interest is _in cis_ with a Pathogenic or Likely Pathogenic variant. The other variant must meet a Likely Pathogenic or Pathogenic classification using these rule specifications.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For a missense variant use REVEL, requires a score between 0.183 - 0.290. In addition, highest SpliceAI delta score should also be below cutoff of 0.1.

For a silent / intronic variant outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon, BP4 can be met if the highest of the four delta scores within SpliceAI is below the cutoff of ≤0.1. See AIPL1-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Please note that BP7 can be met as well.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

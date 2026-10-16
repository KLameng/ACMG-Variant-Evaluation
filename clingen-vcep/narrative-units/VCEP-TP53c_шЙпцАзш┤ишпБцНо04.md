> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：**Missense variants** _(See flowchart for application of PP3 and BP4 rules for missense variants):_

BayesDel \< 0.16 and > -0.008 irrespective of aGVGD score (except C65, this case do not apply BP4) AND no predicted differences in splicing (SpliceAI \< 0.2)

**Single amino acid inframe deletions** _(See single aa BayesDel spreadsheet):_

BayesDel score \< 0.16 AND no predicted splicing impact (Splice AI \< 0.2)

**Silent or Intronic Variants (outside ± 1,2 positions):**

SpliceAI ≤ 0.1


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) outside of the core splice motif (last three nucleotides and first nucleotide of the exon) or intronic variant at or beyond +7 to -21 positions for which SpliceAI predicts no impact to the splice consensus nor the creation of a new splice site (BP4 is met, SpliceAI ≤ 0.1). No requirement to assess for nucleotide conservation for rule application as per evidence and recommendations in Walker et al., 2023  (PMID: 37352859).

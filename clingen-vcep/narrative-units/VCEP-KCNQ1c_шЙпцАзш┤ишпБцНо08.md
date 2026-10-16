> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Caveat: BP5 is not applicable when the phenotypes (ie: trigger type; PMID: 32882399, 11136691, 18373596 or treadmill stress test; PMID: 21699858) indicate _KCNQ1_ as the cause. BP5 is only applicable when the phenotypes match another form of LQTS (caused by a variant in _KCNH2_, _SCN5A_, or _KCNE1_, PMID: 19862833, PMID: 31941373, PMID: 33517668) or when phenotype details are not sufficiently specific.
*   Note: The rate of cases with multiple suspected deleterious variants in the same or different LQTS-associated genes may be relatively high (5.2% in one cohort, PMID: 24667783). The group will consider this possibility during the pilot.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

*   Use SpliceAI to look for suspected splicing defects (cutoff Δ score \<0.1).
*   Use PhyloP to check for conservation (cutoff \<2.0).
*   Please note that SpliceAI Δ score \<0.1 AND PhyloP score \<2.0 must both be met.
*   This code can be met by synonymous variants except for variants in the last 3 nucleotides of an exon, or in the 1st nucleotide of an exon.
*   This code can be met by intronic variants except for variants in positions +1 to +6 or -1 to -20, which are considered part of the splice donor and splice acceptor sites (PMID: 37352859).

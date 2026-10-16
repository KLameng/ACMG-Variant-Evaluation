> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants, use REVEL with a score ≤0.1 AND SpliceAI with a score ≤0.05.

For variants that may affect splicing, use SpliceAI with a score ≤0.05. Splice AI scores can be calculated here: [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/)

For any variant with RNA or other experimental data indicating no impact on splicing, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：For any variant that has been experimentally shown to have no splice impact, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “Experimental splice data”. Apply BP7\_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out.
- **Supporting** ✅：For splice predictions, use SpliceAI with a score ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor).

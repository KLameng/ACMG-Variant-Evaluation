> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** 📋：Variant observed in trans w/known pathogenic variant (phase confirmed) OR observed in the homozygous state in individual w/o personal &/or family history of DGC, LBC, or SRC tumors.
- **Supporting** 📋：Variant is observed in cis (or phase is unknown) w/ a pathogenic variant
OR observed in the homozygous state in gnomAD.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Splicing predictions only. At least three in silico splicing predictors in agreement (SpliceAI, MaxEntScan, SSF, GeneSplicer, HSF, TraP, varSEAK).


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：Per original ACMG/AMP guidelines.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Synonymous and intronic variants at or beyond +7 to -21 locations.

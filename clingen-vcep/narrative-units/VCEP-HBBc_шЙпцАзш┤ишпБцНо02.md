> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.


#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed _in_ _cis_ with a pathogenic variant in any inheritance pattern.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.)

For missense: REVEL score \< 0.7 AND SpliceAI DS ≤ 0.3 (if REVEL score is not available, use CADD PHRED score ≤ 20, instead) 

For non-coding, synonymous, inframe indels, stop-lost: CADD PHRED score ≤ 11  AND SpliceAI DS ≤ 0.3


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.


#### BP7
- 默认强度：Benign Supporting

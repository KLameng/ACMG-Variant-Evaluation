> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caution is needed when considering any population cohorts that are smaller than the smallest subpopulations within gnomAD v.2.1.1 (e.g., ~5000 individuals or ~10,000 alleles). Despite this conservative nature of this threshold and approach, in smaller cohorts, the observed allele frequency may less accurately reflect the true allele frequency. Traditionally, once a variant is classified as Benign, it is rarely re-evaluated and so the highest confidence is needed to establish that classification on an allele frequency alone.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is **≥0.0002 for** _**MYBPC3**_ based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

Criterion BS1 may only be used as standalone evidence to classify a variant as Likely Benign in the absence of conflicting data. See SVI guidance (Tavtigian _et al._ 2018[<sup>18</sup>](#pmid_29300386); Tavtigian _et al._ 2020[<sup>19</sup>](#pmid_32720330)). 

See BA1 for additional specifications that also apply to BS1.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：See PS3 specifications.
- **Moderate** ✅：See PS3 specifications.
- **Supporting** ✅：See PS3 specifications.


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

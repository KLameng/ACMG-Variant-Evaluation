> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：This evidence code can be used when a _F8_ variant is observed in a male with a family history of hemophilia A and has a normal factor VIII activity level.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：This code can be applied for variants reaching a REVEL score of 0.3 or below AND a Splice AI score of less than or equal to 0.1.


#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay and a SpliceAI score of less than or equal to 0.1.
- **Supporting** 📋：Splice AI should be used to suggest no splicing impact. Splicing prediction score of less than or equal to 0.1 is required. Conservation should be assess using PhyloP (cutoff less than 0.1) and PhastCons (cutoff less than 0.5).

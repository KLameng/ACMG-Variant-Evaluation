> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：In a transgenic animal model, must demonstrate minimal to no function.


#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Disulfide bonds in GPIb are well-established as critical to function, both for interaction with GPIX (PMID: 12036872) and receptor binding to von Willebrand factor (PMID: 18647229). PM1 can be applied when the following cysteine residues (at which there are no known benign variants) are altered: 93, 95, 118, 141, and 147.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD MAF of less than or equal to 0.00006517.


#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use proposed SVI point recommendations. Both variants must be classified using these rule specifications, with the exception that a 22q11.2 deletion in trans ([https://www.ncbi.nlm.nih.gov/books/NBK1523/](https://www.ncbi.nlm.nih.gov/books/NBK1523/)) may be automatically scored 1pt with confirmation that deletion includes the _GP1BB_ gene.

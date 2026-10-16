> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199):

*   PM1\_Moderate: missense variant located in the **PHD domain** (amino acids 414-487);

Caveat: variant must not meet BS1, BS2, or BA1 criteria.
- **Supporting** ✅：Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199):

*   PM1\_Supporting: missense variant located in the **core domain** (amino acids 1-383);

Caveat: variant must not meet BS1, BS2, or BA1 criteria.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD popmax filtering allele frequency \<0.0000588  

*   An additional requirement is that **no homozygotes** have been observed in gnomAD.


#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _RAG2._
- **Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _RAG2._

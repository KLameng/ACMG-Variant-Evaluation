> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：PM2\_Supporting can be applied for variants either absent from gnomAD or with \<= 0.00000156 (0.000156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release). If no GroupMax Filtering Allele Frequency is calculated (ex. due to a single variant present), PM2\_Supporting may also be applied.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：In-frame insertion / deletions in the B and alpha domains and stop-loss variants adding significant additional amino acids to VHL [<sup>15</sup>](#pmid_20560986) cites multiple pathogenic cases and experimental evidence of stop loss extensions in VHL that are associated with Type 2A VHL disease).  The functional domains are: Beta (β) domain (AA 63 - 155, Nuclear Export), Alpha (ɑ) domain (AA 156-192, Elongin C binding), and Second Beta (β) domain (AA 193-204). 

PM4 does not apply to in-frame indels prior to codon 54 that do not alter the Met54 VHL p19 codon and beyond.


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

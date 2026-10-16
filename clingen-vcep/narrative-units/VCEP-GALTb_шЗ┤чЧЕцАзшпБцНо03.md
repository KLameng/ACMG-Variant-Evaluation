> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

    *   PS1 can by applied at varying strengths (strong, moderate, supporting) in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/-1,2, dinculeotide position). Specific combinations are outlined in table 2 Walker et al., 2023, PMID: 37352859.
*   PS1\_Supporting will apply for splicing variants only, used Table 2 in Walker et al., 2023, PMID: 37352859


#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：Applicable for up to 20% enzyme activity in a model system


#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：PM1 applied at moderate strength for variants that occur in the active site from Phe171 to Gln188


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Can only be used at the supporting level 
*   Use the PopMax filtering allele frequency (FAF) from gnomAD.
*   Use if variant is present at ≤ 0.0005 or 0.05% 
    *   One order of magnitude below BS1

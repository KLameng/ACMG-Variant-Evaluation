> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points


#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Variant is located within a Pathogenic Enriched Region. See specific amino acid residues noted in the attached “PM1 Table".


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：One or fewer alleles, if a minimum of 10,000 alleles assessed in population databases, such as the Genome Aggregation Database (gnomAD). Caveat: Population data for indels may be poorly called by next generation sequencing.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**Rule Combining Stipulation**: If PM5_Strong is reached, and the variant falls within a PM1 region, then do not add PM1 with PM5_Strong.


> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. Not applicable for splicing effects (replaced by PVS1\_Strength (RNA))

See attached table for acceptable functional studies.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.

*   Used if the gnomAD total allele frequency is ≤ 4.0 x 10<sup>-4</sup>.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*    Protein length change of ≥2 amino acids that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP>2.0).
- **Supporting** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*    Protein length change of 1 amino acid that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acid adjacent to at least one conserved residue (PhyloP>2.0).


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

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
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

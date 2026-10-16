> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Due to current technical limitations of next generation sequencing technologies, minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented in population databases.

Caution should be used when a variant is only identified, or over-represented, in one of the smaller gnomAD populations, as the gnomAD allele frequencies may not accurately represent the true population frequency.

Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Strength of rule should be carefully considered and may require downgrading to SUPPORTING based on the predicted impact of the variant, including the size of the deletion/insertion, its location, and conservation of the region. 

For genes where PVS1 is not applicable (i.e., where there is no evidence that pLOF variants cause disease), consider using this rule at MODERATE or SUPPORTING strength for truncating variants that do NOT undergo nonsense mediated decay (NMD).


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：This criterion can be used at MODERATE if a different missense variant at the same codon has been classified as _pathogenic_ using these modified guidelines without application of PM5.


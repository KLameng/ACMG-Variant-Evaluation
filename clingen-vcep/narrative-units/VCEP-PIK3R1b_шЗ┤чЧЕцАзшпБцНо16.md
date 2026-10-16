> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Use PM5 at the default (moderate) strength level for a missense variant when another missense variant encoding a different amino acid change in the same codon was classified as Pathogenic by Antibody Deficiencies VCEP specifications for _PIK3R1_ without using PM5.
*   Neither the variant of interest nor the Pathogenic comparison variant should be predicted to affect splicing (all SpliceAI Δ scores \<0.2 for both variants).
*   The variant of interest must have a higher Grantham score than the Pathogenic comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
*   Do not apply at codon where any benign variants are known.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   Use PM5\_Supporting for a missense variant when another missense variant encoding a different amino acid change in the same codon was classified as Likely Pathogenic by Antibody Deficiencies VCEP specifications for _PIK3R1_ without using PM5.
*   Neither the variant of interest nor the Likely Pathogenic comparison variant should be predicted to affect splicing (all SpliceAI Δ scores \<0.2 for both variants).
*   The variant of interest must have a higher Grantham score than the Likely Pathogenic comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
*   Do not apply at codon where any benign variants are known.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.


#### PP1
- 默认强度：Pathogenic Supporting

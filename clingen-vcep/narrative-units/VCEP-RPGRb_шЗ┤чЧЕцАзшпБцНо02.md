> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：PVS1\_Moderate designation for initiation codon variants with upstream pathogenic variants of closest potential in-frame start codon or for variants in NM\_00328.3 which remove  less than 10% of the protein and are not expected to lead to NMD.
- **Supporting** ✅：PVS1\_Supporting designation for initiation codon variants without upstream pathogenic variants of closest potential in-frame start codon.


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established Pathogenic variant regardless of nucleotide change.

*   Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as a pathogenic variant and classified as such.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

Same predicted splicing impact as a previously classified Pathogenic variant.

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated Pathogenic.
*   Used in conjunction with PVS1 for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide that has been designated Pathogenic.  
    Specific combinations are found in \_RPGR\_-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).

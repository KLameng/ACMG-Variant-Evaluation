> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN141 — Antibody Deficiencies Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Use at the default level (PS1) for missense variants when other variant was classified as Pathogenic for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score \<0.2).
- **Moderate** ✅：*   Use at the PS1\_Moderate level for missense variants when other variant was classified as Likely Pathogenic for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score \<0.2).


#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

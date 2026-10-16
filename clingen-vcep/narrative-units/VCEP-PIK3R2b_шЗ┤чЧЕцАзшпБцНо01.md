> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN018 — Brain Malformations Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：No change.


#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** 📋：Award the PS2_Strong point if Criteria 1 AND Criteria 2 are fulfilled.  

  Criteria 1. The variant is present at a detectable allele fraction but is absent from parental samples with confirmed maternity and paternity.

  Criteria 2. The variant is present at a detectable allele fraction in an affected tissue sample but is absent from or detected at a lower allelic fraction in another tissue (e.g. if present in 5% of brain tissue but absent from the blood or skin this point can be awarded).

For the sake of implementation, these criteria are intended to apply to high-confidence somatic mutations identified by the reporting CLIA laboratory. The expert panel recognizes that in practice there may be significant heterogeneity in the technical methods and thresholds used to identify such variants as 'high confidence', and flags the need to establish consensus statistical frameworks (e.g. Phred-scaled genotype qualities) or experimental approaches (e.g., confirmation of somatic variants by sequencing on orthogonal platforms) by which quality thresholds can be consistently applied.

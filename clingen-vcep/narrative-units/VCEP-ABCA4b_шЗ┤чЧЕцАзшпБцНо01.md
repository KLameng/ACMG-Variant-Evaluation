> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN164 — ABCA4 Variant Curation Expert Panel 

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Please use the SVI WG decision tree modified for the _ABCA4_ gene.


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Comparison missense variant must reach a pathogenic classification using the _ABCA4_ VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect via SpliceAI or other splice predictor.

**OR**

Comparison splicing variant must reach a pathogenic classification using the _ABCA4_ VCEP specifications and both variants must share the same predicted splicing effect. 

**OR**

See Walker, et al 2023 (PMID: 37352859) Figure 5 to use this rule code for variants with RNA sequencing data.


#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

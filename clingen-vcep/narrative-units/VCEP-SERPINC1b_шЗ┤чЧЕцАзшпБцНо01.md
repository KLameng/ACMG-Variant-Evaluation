> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN084 — Thrombosis Variant Curation Expert Panel 

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use decision tree as per SVI WG with specified “regions critical to protein function”.
- **Strong** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".
- **Moderate** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".
- **Supporting** ✅：Use decision tree as per SVI WG with specified "regions critical to protein function".


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **VCEP Specifications**：Use caution not to compare variants being curated to variants that are potential cryptic slice sites.
- **Strong** ✅：Use with no specification except comparison variant must be classified as pathogenic using _SERPINC1_ rule specifications from the Thrombosis VCEP.

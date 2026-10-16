> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN006 — Phenylketonuria Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Applicable as described in Tayoun et al. 2018.

*   Any nonsense or frameshift variant occurring upstream of c.1285
*   Any canonical splice site predicted to disrupt reading frame and undergo nonsense mediated decay

PVS1 (RNA): splicing assay data - assays demonstrating a variant leads to aberrant splicing profile that can be categorized against a PVS1 decision tree

*   Use the PVS1 decision tree to determine code strength
*   Applicable as described in Walker et al. (PMID: 36865205)
- **Strong** ✅：Use PVS1\_strong with:

*   Any nonsense or frameshift variant occurring downstream of c.1285
*   Any canonical splice site predicted to preserve reading frame (skipping of exons 1, 9, 10) or affect the last exon (exon 13)
*   Initiator codon variant


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

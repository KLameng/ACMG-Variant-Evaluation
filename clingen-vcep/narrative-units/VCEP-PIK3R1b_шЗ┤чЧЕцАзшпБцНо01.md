> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN160 — Antibody Deficiencies Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   If a nonsense or frameshift variant introduces a premature stop codon between c.917 and c.1890, which is predicted to trigger nonsense mediated decay, and the exon is present in all 3 biologically-relevant transcripts (NM\_181523.3, NM\_181504.4, and NM\_181524.2),, apply PVS1.
*   If a canonical splicing variant is predicted to result in skipping of exon 8, 10, or 12, which would disrupt the frame and be predicted to trigger nonsense-mediated decay, apply PVS1.
*   If a nonsense or frameshift variant introduces a premature stop codon between c.4 and c.916, which is predicted to trigger nonsense-mediated decay but the exon is present only in the MANE transcript NM\_181523.3 but absent from NM\_181504.4 and NM\_181524.2, do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.

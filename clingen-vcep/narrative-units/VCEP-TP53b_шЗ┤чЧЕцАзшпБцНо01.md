> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN009 — TP53 Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Please utilize the PVS1 decision tree for application of PVS1 code. The decision tree details the specific strengths each type of null variant may be applied at. Please see below for some additional helpful summary details for application of PVS1 code:

*   Initiation codon:
    *   PVS1 may be applied to initiation codon variants
*   Nonsense or frameshift variants:
    *   PVS1 applies to variants predicted to result in nonsense-mediated decay (NMD) for nonsense variants upstream of p.Lys351 and for frameshift induced premature termination codon (PTC) upstream of p.Lys351
    *   PVS1\_Strong applies to variants not predicted to undergo NMD (nonsense variants downstream of codon 350 or frameshift induced PTC in exon 11 or in the 3’ most 50 nucleotides of exon 10) in variants located in the p.Lys351 to p.Ala 355 range
    *   PVS1\_Moderate applies to variants not predicted to undergo NMD (nonsense variants downstream of codon 350 or frameshift induced PTC in exon 11 or in the 3’ most 50 nucleotides of exon 10) in variants located in the p.Gly356 to p.Asp393 range

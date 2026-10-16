> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN024 — DICER1 and miRNA-Processing Gene Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Follow SVI guidance, using DICER1-specific information. Per the PVS1 workflow guidance provided in Tayoun et al. 2018[<sup>1</sup>](#pmid_30192042), the following will apply:

*   Nonsense or frameshift variants:
*   PVS1 applies to variants predicted to result in nonsense-mediated decay (NMD); the predicted NMD cutoff for DICER1 occurs at p.Pro1850.
*   PVS1\_Moderate applies to variants resulting in protein truncation 3’ of this cutoff
*   Canonical splice variants (+/- 1,2 intronic positions): PVS1 applies with the following exceptions:
*   Exon 10 SDS/SAS: PVS1\_Strong (in-frame but exon includes >10% protein)
*   Exons 5, 15, 18, 22 SDS/SAS: PVS1\_Moderate (in-frame and each \<10% of protein)
*   Exon 27 SAS: PVS1\_Moderate (final exon)
*   Exon 1: no criteria (non-coding)

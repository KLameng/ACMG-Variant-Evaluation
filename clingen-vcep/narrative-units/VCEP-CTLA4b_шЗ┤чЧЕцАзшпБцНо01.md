> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN122 — Antibody Deficiencies Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   For truncating variants located in the isoform-specific exon 3, apply PVS1 if nonsense mediated decay is predicted (truncation at codon 172 or lower) and PVS1\_strong if NMD is not predicted (truncation at codon 173 or higher). While this recommendation already matches the SVI guidance, it is specified here because similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452), despite the fact that exon 3 is omitted from an alternative transcript (NM\_001037631.3) that encodes the soluble isoform (PMID: 40168991).
*   If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score greater than or equal to 0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3\_Supporting and evaluate PVS1 instead (PMID: 37352859).
*   In order to avoid over-weighing loss-of-function evidence, PP3 and PS3 are mutually exclusive with PVS1 at the default (very strong) level. These additional codes cannot be applied for a variant that has already met PVS1.

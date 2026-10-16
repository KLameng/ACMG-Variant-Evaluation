> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN124 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications:

*   Given that the _RAG2_ protein is encoded by a single exon (based on MANE Select transcript NM\_000536.4) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG2 variants (indicated by the red boxes in the Flowchart), **except** in the case of full gene deletion **or** removing/altering critical domain: the PHD domain and core domain (indicated by the purple in the Flowchart). 
*   PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay when removing/altering the critical PHD domain (spanning amino acids 414-487) and core domain (amino acids 1-383)  based on recommendations from Walker et al., preprint.
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:


> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN129 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   PVS1 at default strength (Very Strong) can be applied to variants not predicted to undergo nonsense-mediated decay but truncating the transmembrane domain (which begins at amino acid 255) or any distal region (i.e. cytoplasmic domain) due to the lack of functionality of the protein expressed with this defect.
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), at least one pathogenic variant **must be** present downstream in order to apply PVS1\_Strong
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:


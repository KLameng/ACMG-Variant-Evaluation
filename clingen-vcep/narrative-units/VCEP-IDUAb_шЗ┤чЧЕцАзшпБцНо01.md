> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN091 — Lysosomal Diseases Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   All nonsense and frameshift variants will meet PVS1 (Very Strong), unless the variant is predicted to be undetected by nonsense-mediated decay (NMD) i.e. if the resulting premature termination codon is in the last exon (exon 14) or in the last 50 nucleotides of the penultimate exon (exon 13; after c.1778, codon 592). In this case, PVS1\_Moderate will be applied because \<10% of the primary amino acid sequence is predicted to be lost (in this case, ~9.3%).
*   For all variants involving either the +1 or +2 position of GT donor splice sites, the exon immediately 5’ of the variant is predicted to be skipped, and for all variants involving either the -1 or -2 position of AG acceptor splice sites, the exon immediately 3’ of the variant is predicted to be skipped, unless indicated otherwise by RT-PCR or in silico prediction. For the predicted in frame/out of frame consequences for skipping any exon in IDUA, and recommended weight for PVS1, see Appendix 1.

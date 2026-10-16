> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN026 — Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：**Nonsense-mediated decay predicted**

**Nonsense and frameshift variants**

*   All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 6) or the last 50 bases of the penultimate exon of the gene (exon 5, c.520). In that case, PVS1\_Strong or PVS1\_Moderate will be applied, depending on whether >10% or \<10% of the protein is lost.

**Splice site variants (+1, +2, -1, -2)**

*   All canonical splice site pairs in GAMT are GT-AG.
*   For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants.
*   For the predicted in frame/out of frame consequences of exon skipping and assigned strength of PVS1, see Appendix 1.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.

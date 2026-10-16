> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN025 — Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：**Nonsense-mediated decay predicted.**

CCDS VCEP notes:  
Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D ([https://databases.lovd.nl/shared/variants/GATM/unique](https://databases.lovd.nl/shared/variants/GATM/unique)). The specifications below are based on the PVS1 decision tree (see Appendix 1) (based on Figure 1, Abou Tayoun et al, 2018, PMID 30192042).

GATM specifications:  
**Nonsense and frameshift variants**  
\* All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 9) or the last 50 bases of the penultimate exon (exon 8, 3’ of c.1109). In that case, please refer to the PVS1 flowchart for guidance on PVS1 weight (Appendix 1).

**Splice site variants (+1, +2, -1, -2)**  
\* All canonical splice site pairs in GATM are GT-AG.  

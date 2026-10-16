> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 6) or the last 50 bases of the penultimate exon of the gene (exon 5, c.520). In that case, PVS1\_Moderate will be applied if \<10% of the protein is lost.

**Splice site variants (+1, +2, -1, -2)**

*   All canonical splice site pairs in GAMT are GT-AG.
*   Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing. 
*   For any canonical splice site variant (+1, +2, -1, -2), if RT-PCR data predicts in-frame loss of \<10% of the protein, apply PVS1\_Moderate.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.
*   Non-canonical splice variants, such as +3 or -3, will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Initiator codon variants**

*   All initiator codon variants will meet PVS1\_Moderate. The next in-frame methionine is at amino acid position 42 (based on NP\_000147.1).

**Deletions (single or multi exon)**

*   If a single or multi-exon deletion results in an out of frame consequence, use PVS1 unless not predicted to undergo NMD. 
*   If not predicted to undergo NMD, use PVS1\_Strong if >10% of the protein is predicted to be removed, and use PVS1\_Moderate if \<10% of the protein is predicted to be removed.
*   If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. Use PVS1\_Strong if more than 10% of the protein is removed and PVS1\_Moderate if \<10% of the protein is removed.
*   If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.  
    Appendix 1 can be used to predict the consequences of single exon deletions.

**Duplications**


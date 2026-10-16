> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants.
*   Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing. 
*   For considerations for strength at which PVS1 may be applied see Appendix 1.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.
*   Non-canonical splice variants, such as +3 or -3, will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Deletions (single or multi exon)**

*   If a single or multi-exon deletion results in an out of frame consequence, use PVS1 unless not predicted to undergo NMD.
*    If not predicted to undergo NMD, use PVS1\_Strong if >10% of the protein is predicted to be removed, and use PVS1\_Moderate if \<10% of the protein is predicted to be removed.
*   If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. Use PVS1\_Strong if more than 10% of the protein is removed and PVS1\_Moderate if \<10% of the protein is removed.
*   If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.  
    Appendix 1 can be used to predict the consequences of single exon deletions.

**Duplications**

*   Use the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042) to assess the impact of duplications.
- **Moderate** 📋：**Single exon or larger deletion resulting in loss of \<10% of the protein.**   

**Nonsense and frameshift variants**


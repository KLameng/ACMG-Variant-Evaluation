> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D ([https://databases.lovd.nl/shared/variants/GATM/unique](https://databases.lovd.nl/shared/variants/GATM/unique)). The specifications below are based on the PVS1 decision tree (see Appendix 1) (Figure 1, Abou Tayoun et al, 2018, PMID 30192042).

GATM specifications:  
**Nonsense and frameshift variants**  
\* All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 9) or the last 50 bases of the penultimate exon (exon 8, 3’ of c.1109). In that case, please refer to the PVS1 flowchart for guidance on PVS1 weight (Appendix 1).

**Splice site variants (+1, +2, -1, -2)**  
\* All canonical splice site pairs in GATM are GT-AG.  
\* For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants. However, it is recommended to use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing.   
\* For considerations for strength at which PVS1 may be applied see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss) .  
\* If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.  
\* Non-canonical splice variants, such as +3 or -3, may also meet PVS1 - refer to Walker et al, PMID: 37352859.

**Deletions (single or multi exon)**  

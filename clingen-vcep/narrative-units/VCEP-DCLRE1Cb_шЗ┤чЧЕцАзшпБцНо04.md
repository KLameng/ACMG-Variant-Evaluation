> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

        *   Pannicke et al., 2004 (PMID: 15071507)
        *   Ege et al., 2005 (PMID: 15731174)
        *   Felgentreff et al., 2015 (PMID: 25917813)
        *   Volk et al., 2015 (PMID: 26476407)
- **Supporting** ✅：The strength of evidence from cellular models/_in vitro_ studies is dependent upon abnormal results in _in vitro_ DNA repair activity and V(D)J recombination assays: 

*   PS3\_Supporting: Abnormal result in an _in vitro_ V(D)J recombination assay (same threshold, \<25% of wild-type activity).
*   Approved assay instances:
    *   DNA repair activity assay 
        *   Felgentreff et al., 2015 (PMID: 25917813)
    *   V(D)J recombination assay 
        *   Pannicke et al., 2004 (PMID: 15071507)
        *   Ege et al., 2005 (PMID: 15731174)
        *   Felgentreff et al., 2015 (PMID: 25917813)
        *   Volk et al., 2015 (PMID: 26476407)


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD popmax filtering allele frequency  \<0.00003266 

*   An additional requirement is that **no homozygotes** have been observed in gnomAD.


#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _DCLRE1C._

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   If the variant is likely pathogenic, use PM5\_Supporting.
- **Supporting** 📋：*   This criterion is applicable for any variant resulting in a different amino acid change, at the same amino acid position, as a variant that has been previously established as likely pathogenic by the CCDS VCEP, by assessment using these criteria, regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.  
*   If the variant is likely pathogenic, use PM5.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** 📋：Missense variant with a REVEL score equal to or >0.932 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
- **Moderate** 📋：Missense variant with a REVEL score 0.773-0.932 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
- **Supporting** 📋：*   Missense variant with a REVEL score 0.644-0.773 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
*   In frame deletion or insertion predicted deleterious by PROVEAN and MutationTaster. Results must be consistent to count.

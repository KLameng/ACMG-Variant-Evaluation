> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.


#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Downgraded to PM2\_Supporting
*   Applicable to variants with a total allele frequency \<0.00000132 across all populations in gnomAD v4.1.0.
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for autosomal dominant PIK3CD-related immune disease):
    *   Prevalence: 1 in 4000 (a conservative estimate for primary immunodeficiency diseases from PMID: 17577648, PMID: 23201919)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 0.95 (a conservative estimate based on multiple reports of incomplete but nearly complete penetrance in PMID: 27555459, PMID: 36749229, PMID: 37390899)


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

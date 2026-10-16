> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

If the variant being assessed does not meet any population rule codes (PM2, BA1, BS1) **AND** has a total allele frequency >0.00003 with no single genetic ancestry group having multiple alleles with a frequency >0.00004, curators should recalculate the total allele frequency based on the number of alleles with variant allele fraction (VAF) >0.35 to assess whether PM2 may be met after excluding the low VAF alleles which are likely to represent clonal hematopoiesis of indeterminant potential (CHIP) contamination in the database. This can be done by visualizing the “allele balance” for heterozygotes under the genotype quality metrics for a given variant. By hovering over the histogram bars, the number of variant carriers for each bar between 0.35 and 0.65 can be totaled and this can be used to revise the allele count to determine the allele frequency that can be used to assess if PM2\_Supporting can be met.

In general, the most recent version of gnomAD should be used when available; however, other population databases or earlier versions of gnomAD may be utilized if they are able to provide information the curator deems necessary for optimal variant classification (e.g, they would provide superior information for a particular variant type; have a larger sample size; or better representation for certain subpopulations, etc.)


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense variant at an amino acid residue where 1 different missense variant previously determined to be pathogenic according to the _TP53_ VCEP’s specifications has been seen before.

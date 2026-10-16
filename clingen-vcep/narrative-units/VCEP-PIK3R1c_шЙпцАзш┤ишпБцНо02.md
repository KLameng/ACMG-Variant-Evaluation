> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.000316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   The BS1 threshold was derived by decreasing the BA1 cutoff (greater than or equal to 0.00316) by one order of magnitude.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：*   BS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and failing to recapitulate the phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
*   BS3 will be applied for a non-damaging result in an approved _in vitro_ assay with an OddsPath \<0.053 (PMID: 31892348). No such assays have yet been identified in the _PIK3R1_ literature.
- **Moderate** ✅：*   BS3\_Moderate will be applied for a non-damaging result in an approved _in vitro_ assay with at least 11 known pathogenic or benign variant controls (classified using these specifications, PMID: 31892348).
*   While one such _in vitro_ assay has been identified in the _PIK3R1_ literature (PMID: 40543502), the authors have recommended a non-damaging result in their assay of the ratio of enrichment of the variant in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells for BS3\_Supporting, based on their calculated OddsPath of 0.25.

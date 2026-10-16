> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use as originally specified, but the comparison variant must reach a pathogenic classification using these rule specifications in order to apply code.
- **Supporting** ✅：Use as originally specified, but the comparison variant must reach a likely pathogenic classification using these rule specifications in order to apply code.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：See instructions below for scoring system. Total segregation score 3+ points.
- **Moderate** ✅：See instructions below for scoring system. Total segregation score 2-2.75 points.
- **Supporting** ✅：See instructions below for scoring system. Total segregation score 1-1.75 points.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：REVEL score of ≥0.644 (to \<0.773), based on recommendations of Pejaver et al., 2022 (PMID: 36413997),

OR suggested splicing affect using SpliceAI greater than or equal to 0.5.


#### PP4
- 默认强度：Pathogenic Supporting

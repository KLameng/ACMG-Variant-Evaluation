> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus ≥3 similarly affected relatives
- **Moderate** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus 2 similarly affected relatives
- **Supporting** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus 1 similarly affected relative


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For a missense variant use REVEL, requires a score of 0.644 - 0.773.
*   For a variant in an untranslated region use CADD, requires a score of ≥ 20.0

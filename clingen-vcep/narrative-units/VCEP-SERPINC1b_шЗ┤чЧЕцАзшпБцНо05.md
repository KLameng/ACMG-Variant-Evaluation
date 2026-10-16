> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use code when previously reported variant reaches a pathogenic classification using the _SERPINC1_ rule specifications from the Thrombosis VCEP.
- **Supporting** ✅：Use code when previously reported variant reaches a likely pathogenic classification using the _SERPINC1_ rule specifications from the Thrombosis VCEP.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Appropriate to use there are 7 or more meioses across more than one family.
- **Moderate** ✅：Appropriate to use there are 4-6 meioses across one or more families.
- **Supporting** ✅：Appropriate to use when there are 2-3 meioses across one or more families.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.6. For potential splicing variants, SpliceAI must predict a damaging impact with a score greater or equal to 0.5.

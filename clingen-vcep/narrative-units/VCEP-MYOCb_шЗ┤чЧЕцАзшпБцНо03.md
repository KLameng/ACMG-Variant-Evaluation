> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Same residue as 2 previously established pathogenic variants or 1 previously established pathogenic and 2 likely pathogenic variants or 4 previously established likely pathogenic variants (all assessed independently of PM5)
- **Moderate** 📋：Same residue as a previously established pathogenic variant (assessed independently of PM5) or 2 previously established likely pathogenic variants (both assessed independently of PM5)
- **Supporting** 📋：Same residue as a previously established likely pathogenic variant (assessed independently of PM5)


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：≥7 meioses in >1 family
- **Moderate** 📋：≥ 5 meioses regardless of the number of families
- **Supporting** 📋：≥ 3 meioses regardless of the number of families


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** 📋：REVEL score of ≥ 0.932
- **Moderate** 📋：REVEL score of 0.773-0.931

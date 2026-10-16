> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Missense change at same codon as two different pathogenic missense variants.
Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria for based on independent data).
* Caveat: Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.
- **Moderate** 📋：Missense change at same codon as another pathogenic missense variant.
No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.


#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：See PS2 above.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Segregation in three affected relatives for recessive.
- **Moderate** 📋：Segregation in two affected relatives for recessive.
- **Supporting** 📋：Segregation in one affected relative for recessive.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan.
* Use REVEL and MAXENTSCAN

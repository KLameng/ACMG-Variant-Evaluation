> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5\_Supporting if other variant is Likely Pathogenic due to a missense alteration.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5\_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration.


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> >18.7​ in ≥2 families.
- **Moderate** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>​f</sup> >4.3 & ≤18.7.
- **Supporting** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> >2.08 & ≤4.3.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

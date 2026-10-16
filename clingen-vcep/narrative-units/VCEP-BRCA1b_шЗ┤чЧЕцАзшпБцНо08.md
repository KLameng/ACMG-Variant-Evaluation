> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

PP1 - LR ≥2.08:1


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Apply PP3 for missense or in-frame insertion, deletion or delins variants inside a (potentially) clinically important functional domain and predicted impact via protein change (BayesDel no-AF score ≥0.28). As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857.

Apply PP3 for predicted splicing (SpliceAI ≥0.2) for silent, missense/in-frame (irrespective of location in clinically important functional domain) and for intronic variants outside of donor and acceptor 1,2 sites.

See Specifications Figure1A and Appendix J for details.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：Breast cancer is very common and has a high degree of genetic heterogeneity (caused by pathogenic variants in numerous genes). Use ONLY to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

PP4\_Strong – LR ≥18.7:1

PP4\_Very Strong – LR ≥350:1


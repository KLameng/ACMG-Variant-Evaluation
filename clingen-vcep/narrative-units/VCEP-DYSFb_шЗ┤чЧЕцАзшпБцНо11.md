> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：Segregations should be counted across families, with the total number of segregations determining the strength level. Apply PP1\_Moderate for 2 affected segregations (in addition to proband; may be from a single family). When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate).
- **Supporting** ✅：Segregations should be counted across families, with the total number of segregations determining the strength level. Apply PP1 (Supporting) for 1 affected segregation (in addition to proband). When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate).


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants, use REVEL with a score ≥0.7. 

For variants that may affect splicing, use SpliceAI with a score ≥0.5.

For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

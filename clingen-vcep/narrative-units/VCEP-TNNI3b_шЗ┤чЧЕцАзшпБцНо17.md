> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis.  

Important considerations include:

1.  Segregation of a variant within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant.  If linkage disequilibrium is a concern, consider downgrading strength of segregation. 
2.  Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1 (see below).
3.  Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype. 
4.  Caution is needed when distantly related (≥3<sup>rd</sup> degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：As many _in silico_ algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.

Use of REVEL (Ioannidis _et al._ 2016[<sup>13</sup>](#pmid_27666373)) is recommended at thresholds of **≥0.70 for PP3**.

Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data.


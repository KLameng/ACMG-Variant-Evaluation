> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：As many _in silico_ algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.

Use of REVEL (Ioannidis _et al._ 2016[<sup>12</sup>](#pmid_27666373)) is recommended at thresholds of **≥0.70 for PP3**.

Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data.

Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions.

[SpliceAI](https://spliceailookup.broadinstitute.org)[<sup>13</sup>](#pmid_30661751) is recommended for evaluation of predicted splice impacts.


#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Not Applicable** ✅：This rule is not applicable to ACTC1 as it is not a gene that is highly constrained for missense variation.

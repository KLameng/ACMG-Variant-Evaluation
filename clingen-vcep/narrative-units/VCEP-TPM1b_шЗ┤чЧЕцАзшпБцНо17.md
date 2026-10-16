> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh _et al._ 2019[<sup>12</sup>](#pmid_30696458)) rather than the missense constraint score in gnomAD. 

On the basis of data from Walsh _et al._ 2019[<sup>12</sup>](#pmid_30696458), **PP2 is currently** **only applicable to** _**TPM1**_ **for HCM** (transcripts ENST00000403994 and NM\_001018005.2)_._

Data from HCM case cohorts was used to derive these cluster regions. Therefore, this rule should NOT be applied when additional evidence for the variant supports that the variant causes a phenotype other than HCM (e.g., variant seen in multiple DCM cases).

Enrichment was not observed for DCM in any genes.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：As many _in silico_ algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.

Use of REVEL (Ioannidis _et al._ 2016[<sup>13</sup>](#pmid_27666373)) is recommended at thresholds of **≥0.70 for PP3**.

Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data.


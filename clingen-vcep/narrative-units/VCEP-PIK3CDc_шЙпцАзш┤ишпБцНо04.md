> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   BS4\_Supporting is met if only 1 affected family member lacks segregation of the genotype.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (BP4) level by a missense variant with REVEL score less than or equal to 0.290 and CADD PHRED score less than or equal to 22.7.
*   SpliceAI Δ scores should be checked for missense variants as well. Variants with a predicted impact on splicing (SpliceAI Δ score greater than or equal to 0.2) should not be evaluated using these specifications, but rather using alternative specifications for autosomal recessive disease with a loss-of-function mechanism, unless functional evidence indicates a gain-of-function effect. The current specifications are written for a PIK3CD gain-of-function disease mechanism that has so far not been reported in association with variants that disrupt splicing.
*   Met at the default (BP4) level by a synonymous or intronic variant not predicted to impact splicing by SpliceAI (SpliceAI Δ score \<0.1, PMID: 37352859).
*   Higher strength levels of BP4\_Moderate or BP4\_Strong have not been recommended due to pilot data indicating poor performance and significant discordance between REVEL and CADD predictions for established benign and gain-of-function PIK3CD variants.


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.


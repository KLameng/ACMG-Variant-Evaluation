> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (PP3) level by a missense variant with REVEL score greater than or equal to 0.644 and CADD PHRED score greater than or equal to 25.3.
*   Higher strength levels of PP3\_Moderate or PP3\_Strong have not been recommended due to pilot data indicating poor performance and significant discordance between REVEL and CADD predictions for established benign and gain-of-function _PIK3CD_ variants.
*   SpliceAI scores should be checked for missense variants, but there currently is no evidence of variants causing autosomal dominant disease through a splicing mechanism, so PP3 cannot be met by a variant located in the boundary exonic/intronic region with a predicted splicing impact. A variant with a predicted impact on splicing (SpliceAI Δ score greater than or equal to 0.2) should not be evaluated using these specifications, but rather using alternative specifications for autosomal recessive disease with a loss-of-function mechanism, unless functional evidence indicates a gain-of-function effect.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

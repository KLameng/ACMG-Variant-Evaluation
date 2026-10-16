> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be 'likely pathogenic' has been seen before.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product.
 * REVEL score >0.7 for missense variants.
 * In frame deletion or insertion predicted deleterious by 2 out of 3 tools (PROVEAN, MutationTaster, MutPred-InDel).
 * Predicted impact on splicing by SpliceAI (score >0.5).


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Phenotype specific for disease with single genetic etiology.
 * Points-based system. See main specifications document
- **Supporting** ✅：Phenotype specific for disease with single genetic etiology.
 * Points-based system. See main specifications document

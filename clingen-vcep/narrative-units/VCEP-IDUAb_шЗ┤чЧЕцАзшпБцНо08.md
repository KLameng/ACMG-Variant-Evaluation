> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be likely pathogenic has been seen before.

Stop loss variant if another stop loss variant has been determined to be likely pathogenic.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Any missense changes with a REVEL score between 0.644 - 0.773 will meet PP3 (Pejaver et al., PMID: 3641399)
*   For in frame insertions and deletions, use Mutation Taster ([http://www.mutationtaster.org/](http://www.mutationtaster.org/) ; count if “disease-causing”), and MutPred-Indel ([https://mutpred2.mutdb.org/mutpredindel/](https://mutpred2.mutdb.org/mutpredindel/) ; score >0.5 for “pathogenic”). Apply PP3 if both predictors indicate that the variant is deleterious.
*   For non-canonical splice site variants (e.g., +3, -3), use SpliceAI ([https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) ). A score of >0.2 is taken to indicate disruption of the splice site allowing PP3 to be applied (based on Walker et al, PMID: 37352859). Evidence for use of a cryptic splice site and the impact on the gene product should also be assessed. PP3 for splicing variants will be applied only in the absence of functional (RNA analysis) data.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

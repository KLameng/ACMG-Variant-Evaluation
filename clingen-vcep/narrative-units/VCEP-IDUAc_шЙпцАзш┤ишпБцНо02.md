> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

BS3\_Supporting can be applied for expression of IDUA sequence variants in cultured cells and subsequent measurement of enzyme activity provided that there is no other evidence to suggest that the variant could be disease-causing e.g. mislocalization (see Appendix 3 for thresholds for specific studies: >10% activity (Beesley et al, 2001, PMID: 11735025; Yogalingam et al, 2004, PMID: 15300847; Matte et al, 2003); >~10% activity / enzyme abundance (Yu et al, 2020. PMID: 33198351).


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Missense changes with a REVEL score \< 0.290 (threshold based on Pejaver et al; however, BP4 will only be applied at the supporting level). 
*   For in frame insertions and deletions, use PROVEAN ([http://provean.jcvi.org/seq_submit.php](http://provean.jcvi.org/seq_submit.php) ; score >-2.5), Mutation Taster ([http://www.mutationtaster.org/](http://www.mutationtaster.org/) ; count if “polymorphism”, and MutPred-Indel ([http://mutpredindel.cs.indiana.edu/](http://mutpredindel.cs.indiana.edu/) ; score \<0.5. Apply BP4 if all predictors indicate that the variant is benign.
*   For non-canonical splice site variants, use SpliceAI ([https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) ) to assess the impact of variants that are not +/-1 or 2 canonical splice site variants. This criterion can be applied as PP3 (Splicing) for SpliceAI scores ≤0.1 (based on Walker et al, PMID: 37352859). 

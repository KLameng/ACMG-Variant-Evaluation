> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   If only 1 affected family member lacks segregation of the genotype, downgrade to BS4\_Supporting.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (BP4) level by a missense variant with REVEL score \<0.25, CADD PHRED score \<20, and SpliceAI Δ score \<0.1.
*   The above requirement for agreement between two _in silico_ tools was reached following a pilot study of suspected pathogenic and suspected benign variants (assembled from ClinVar submissions and published assertions of pathogenicity). Some suspected pathogenic _CTLA4_ variants fall in REVEL’s benign range while some suspected benign _CTLA4_ variants fall in CADD’s pathogenic range. All false positive and false negative predictions in the test set could be avoided by requiring that both tools agree in order for PP3 or BP4 to be Met.
*   Applicable to both synonymous variants and all intronic variants outside the +/-1,2 dinucleotide positions not predicted to impact splicing by SpliceAI (SpliceAI Δ score \<0.1, PMID: 37352859).


#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：*   Two such cases are required to mitigate the VCEP’s concern over relying on other groups’ classifications of pathogenic variants in genes such as _LRBA_.


#### BP7
- 默认强度：Benign Supporting

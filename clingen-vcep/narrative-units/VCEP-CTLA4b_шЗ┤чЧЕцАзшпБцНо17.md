> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (PP3) level by a missense variant with REVEL score greater than or equal to 0.75 and CADD PHRED score greater than or equal to 20.
*   The above requirement for agreement between two _in silico_ tools was reached following a pilot study of suspected pathogenic and suspected benign variants (assembled from ClinVar submissions and published assertions of pathogenicity). Some suspected pathogenic _CTLA4_ variants fall in REVEL’s benign range while some suspected benign _CTLA4_ variants fall in CADD’s pathogenic range. All false positive and false negative predictions in the test set could be avoided by requiring that both tools agree in order for PP3 or BP4 to be Met.
*   Met by missense, synonymous, or intronic variants outside the +/-1,2 dinucleotide positions that are predicted as damaging using SpliceAI (cutoff Δ score greater than or equal to 0.2).


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   In order to be counted for PP4\_Moderate, a proband must;
    *   score at least 10 phenotype points in the PS4 counting rubric
    *   AND

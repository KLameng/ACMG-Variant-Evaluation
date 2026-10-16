> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Met at the Supporting level if the variant co-segregates with the affected phenotype across the proband and one affected first degree relative (1 meiosis).


#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   PP3 is met by a missense variant with both REVEL greater than or equal to 0.644 and CADD greater than or equal to 26.0.
*   The VCEP will try to determine during the pilot whether higher strength levels of PP3 are appropriate for _PIK3R1_ variants.
*   PP3 is met by missense, synonymous, or intronic variants outside the +/-1,2 dinucleotide positions that are predicted as damaging using SpliceAI (Δ score for donor gain, donor loss, acceptor gain, or acceptor loss score greater than or equal to 0.2, PMID: 37352859).
*   Splice impact must be assessed for every missense, small in-frame insertion and/or deletion, synonymous, or intronic variant.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   PP4\_Moderate is met when a proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping that did not identify an alternative basis for disease at the _PIK3CD_ locus AND has patient cell-based evidence of abnormally high activity of the disease-relevant PI3K delta pathway.

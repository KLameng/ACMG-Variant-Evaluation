> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Apply **PS1**, for predicted **missense** substitutions, where a previously classified **pathogenic** variant is considered to act via protein change (no confirmed or predicted effect on mRNA splicing (SpliceAI≤0.1)).

Apply **PS1**, for exonic and intronic variants with same predicted impact on **splicing,** as a previously classified **pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant. 

See Specifications Table 5 and Appendix E, J and K for details.
- **Moderate** ✅：Apply **PS1\_Moderate**, for predicted **missense** substitutions, where a previously classified **likely pathogenic** variant is considered to act via protein change (no confirmed or predicted effect on mRNA splicing (SpliceAI≤0.1)).

Apply **PS1\_Moderate**, for exonic and intronic variants with same predicted impact on **splicing**, as a previously classified **(likely) pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant.

See Specifications Table 5 and Appendix E, J and K for details.
- **Supporting** ✅：Apply **PS1**, for exonic and intronic variants with same predicted impact on **splicing**, as a previously classified **(likely) pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant.

See Specifications Table 5 and Appendix E, J and K for details.


#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

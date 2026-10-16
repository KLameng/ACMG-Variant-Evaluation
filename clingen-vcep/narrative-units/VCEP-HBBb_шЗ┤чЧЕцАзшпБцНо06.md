> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

For missense: REVEL score > 0.8 OR SpliceAI > 0.3. If REVEL score is not available, use CADD PHRED score > 23.5 

For non-coding, synonymous, inframe indels, stop-lost: CADD PHRED score > 12 OR SpliceAI DS > 0.3 

Should not be used for LOF variants considered in PVS1.

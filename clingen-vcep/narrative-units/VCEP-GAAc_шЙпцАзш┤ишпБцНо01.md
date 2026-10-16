> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN010 — Lysosomal Diseases Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Common in population databases.
 * Highest minor allele frequency >0.01 (>1%) in any continental population in gnomAD with >2000 alleles.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disease.
 * Highest minor allele frequency >0.005 (>0.5%) in any continental population in gnomAD with >2000 alleles.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established in vitro or in vivo functional studies show no damaging effect on protein function.
 * >60% normal GAA activity when the variant is expressed in a heterologous cell type.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function.
 * >50% activity when the variant is expressed in a heterologous cell type, or >30% activity if there is also evidence of normal synthesis and processing.


#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in cis with a pathogenic variant.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)

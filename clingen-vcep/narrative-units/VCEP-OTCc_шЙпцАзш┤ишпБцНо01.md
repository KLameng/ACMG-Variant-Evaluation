> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN156 — Urea Cycle Disorders Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency above 0.010000 (1.0%), Grpmax Filtering Allele Frequency OR ≥10 (female) homozygotes or (male) hemizygotes in the most current version of gnomAD available at the time of curation.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：An allele frequency >0.002000 (0.2%), Grpmax Filtering Allele Frequency in the  most current version of gnomAD available at the time of curation. 

Note: Both BS1 and BS2 cannot be applied if the same dataset is used to assess population data


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：The variant is observed in >5 (female) homozygotes or 5 (male) hemizygotes in the most current version of gnomAD available at the time of curation.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** ✅：BS3\_Moderate  is applicable when growth of the variant strain is ≥80% when compared to strains containing the wildtype OTC gene.
- **Supporting** ✅：Yeast growth assays in which the ARG3 open reading frame of a yeast strain is replaced with human OTC coding sequence, and site directed mutagenesis utilized to introduce variant of interest (PMID: 37146589) 


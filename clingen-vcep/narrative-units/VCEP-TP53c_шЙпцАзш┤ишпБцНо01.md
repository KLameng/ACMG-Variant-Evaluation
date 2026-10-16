> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN009 — TP53 Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Filtering allele frequency (FAF) of ≥ 0.001 or 0.1% in gnomAD continental subpopulations of a single genetic ancestry group (excluding genetic ancestry groups influenced by founder effects, such as Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and “Remaining”). Genetic ancestry group must have ≥2,000 alleles tested and a minimum of 2 alleles present. Caution should be exerted if the majority of alleles have a variant allele fraction ("allele balance" in gnomAD) below 0.35.  To set the stand-alone benign FAF cutoff, we used the FAF cutoff established for BS1 (0.0003) and increased this cutoff by one order of magnitude to come to a value of 0.001. 

In general, the most recent version of gnomAD should be used when available; however, other population databases or earlier versions of gnomAD may be utilized if they are able to provide information the curator deems necessary for optimal variant classification (e.g, they would provide superior information for a particular variant type; have a larger sample size; or better representation for certain subpopulations, etc.)


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.

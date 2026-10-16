> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN104 — Glaucoma Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency ≥ 0.05 in population databases.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is ≥ 0.01 (1%) in population databases.


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Non-segregations with PCG, ASD or JOAG. Use caution and consider phenotypes of the affected segregations, age at diagnosis and pedigree structure before applying to non-segregations with JOAG or POAG.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of ≤ 0.016
- **Moderate** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of 0.017-0.183
- **Supporting** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of 0.184-0.290


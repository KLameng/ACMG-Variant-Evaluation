> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN077 — Hereditary Breast, Ovarian and Pancreatic Cancer Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Grpmax Filtering AF **\>.1%** in gnomAD v4 dataset


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Grpmax Filtering AF **\>.01%** in gnomAD v4 dataset


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：BS2 **≥ 4** points

See Fanconi Anemia BS2 tables for approach to assign points per proband.
- **Moderate** 📋：BS2\_Moderate = **2** points

See Fanconi Anemia BS2 tables for approach to assign points per proband.
- **Supporting** 📋：BS2\_Supporting = **1** point

See Fanconi Anemia BS2 tables for approach to assign points per proband.


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：LOD ≤ -1.28 or Bayes Factor (LR) ≤.053:1
- **Moderate** 📋：LOD ≤ -.64 or Bayes Factor (LR) ≤.23
- **Supporting** 📋：LOD ≤-.32 or Bayes Factor (LR) ≤.48


#### BP1
- 默认强度：Benign Supporting

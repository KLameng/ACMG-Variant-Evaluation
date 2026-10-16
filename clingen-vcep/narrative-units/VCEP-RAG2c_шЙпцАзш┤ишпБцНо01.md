> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN124 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD popmax filtering allele frequency >0.00872


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD popmax filtering allele frequency  >0.00195<sup>1</sup>

<sup>1</sup> Consider also bottleneck populations.


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2\_Strong: Can be applied at Strong level if observed in at least 3 homozygotes.
- **Supporting** ✅：Only to be used when the variant is observed in the homozygous state in a healthy adult.

BS2\_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote.


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Can be applied without additional specifications.


#### BP7
- 默认强度：Benign Supporting

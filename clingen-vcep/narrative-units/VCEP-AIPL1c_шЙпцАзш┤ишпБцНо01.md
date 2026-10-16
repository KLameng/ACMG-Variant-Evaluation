> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN208 — Leber Congenital Amaurosis/early onset Retinal Dystrophy Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Use gnomAD Grpmax FAF if available, cutoff of  ≥0.0057

*   Use large population databases (i.e. gnomAD).


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disorder. Use gnomAD Grpmax FAF if available.

*   Allele frequency of 0.00057 - 0.00569


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Variant is present in ≥ 3 homozygotes without any features of the phenotype. This rule applies to individuals found in the literature who have been well-phenotyped and are unaffected by age 40. Alternatively, this strength can be applied if the variant is present in ≥ 6 homozygotes in gnomAD v.4.1.0 or later.
- **Supporting** ✅：Variant is present in ≥ 3 homozygotes in gnomAD v.4.1.0 or later.


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.


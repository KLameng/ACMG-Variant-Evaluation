> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN114 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD popmax filtering allele frequency >0.00721.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD popmax filtering allele frequency >0.00161<sup>1</sup>

<sup>1</sup> Consider also bottleneck populations.


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Supporting** ✅：Only to be used when the variant is observed in the homozygous state in a healthy adult.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：The strength of evidence from cellular models/_in vitro_ studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): 

*   BS3\_Supporting: Expressed ADA enzyme activity ≥4.8% of wild-type activity (based on group IV).


#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

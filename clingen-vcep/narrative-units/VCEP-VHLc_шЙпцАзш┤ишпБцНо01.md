> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN078 — VHL Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Use a BA1 cut off of >=0.000156 (0.0156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release).


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Use BS1 cut off of  >=0.0000156 (0.00156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4).


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：VHL is not highly penetrant _at an early age._ BS2 can be applied if: There are at least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**with full phenotyping and screening**_ for the absence of VHL-related cancers.
- **Supporting** 📋：VHL is not highly penetrant _at an early age._ BS2\_Supporting can be applied if: At least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**lacking full phenotyping and screening**_, with no noted VHL-related cancers


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：• HIF 1/2a assay replicates WT function and/or

• VBC complex stability is not affected and/or 

• ECM formation/fibronectin binding is unaffected 


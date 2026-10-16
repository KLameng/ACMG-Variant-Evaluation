> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN122 — Antibody Deficiencies Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Met for GrpMax Filtering Allele Frequency greater than or equal to 1.11 x 10<sup>-5</sup> (0.0000111) in gnomAD, with at least 5 alleles total across all populations in gnomAD (gnomAD v4.1.0).
*   Threshold is based on the experts’ estimate of CTLA-4 insufficiency prevalence of 1/200,000 – 1/1,000,000 people and 45-70% penetrance. A higher prevalence estimate (1 in 100,000) and the lower end of the penetrance estimate (45%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Met for GrpMax Filtering Allele Frequency greater than or equal to 1.11 x 10<sup>-6</sup> (0.00000111) in gnomAD, with at least 3 alleles total across all populations in gnomAD (gnomAD v4.1.0).
*   If GrpMax filtering allele frequency is not listed for the variant, this code is evaluated in relation to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian), but requires **at least 3 alleles total** across all populations in gnomAD (gnomAD v4.1.0) to be met.

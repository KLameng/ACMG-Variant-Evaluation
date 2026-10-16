> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN086 — Monogenic Diabetes Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001)


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：gnomAD Grpmax FAF ≥ 1:25,000 (0.004% or 0.00004)


#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：We expect to see hyperglycemia at birth in an individual with \_GCK\_-MODY and therefore consider an individual unaffected if euglycemic in childhood or adulthood.  Since individuals typically do not present with symptoms of diabetes, evidence that someone is “nondiabetic” is insufficient; fasting glucose must be tested and found to be within normal limits (\<100 mg/dl / 5.5 mmol/L).


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of normal splicing (see BP4).
- **Supporting** 📋：Use GCK PS3 decision tree, which incorporates the relative activity index (RAI), relative stability index (RSI) and assays that measure the impact of variants on binding with GKRP and GKA.

Evidence of no impact on function:

*   Normal RAI (>0.5) + normal RSI (>0.5) + normal inhibition/activation with GKRP/GKA = BS3\_Supporting 

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN141 — Antibody Deficiencies Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.00316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for PIK3CD-related immune disease and the inheritance tailored to the autosomal recessive rather than autosomal dominant mode of inheritance, associated with complete penetrance):
    *   Inheritance: biallelic
    *   Prevalence: 1 in 100,000 (calculated at 1 in 7,500,000 based on the USIDNET cohort, PMID: 34352450, but adjusted based on expectation that cases are actually more common, resulting in a much more frequent / more aggressive prevalence estimate of 1 in 100,000 in order to generate a more conservative estimate)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 1


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.000316 in gnomAD v4.1.0.

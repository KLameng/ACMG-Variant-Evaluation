> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN160 — Antibody Deficiencies Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.00316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters:
    *   Inheritance: biallelic (in order to generate a higher / more stringent threshold that would rule out a variant as a credible cause of either autosomal dominant or autosomal recessive disease)
    *   Prevalence: 1 in 100,000 (calculated at 1 in 7,500,000 based on the USIDNET cohort, PMID: 34352450, but adjusted based on expectation that cases are actually more common, resulting in a much more frequent / more aggressive prevalence estimate of 1 in 100,000 in order to generate a more conservative estimate)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 1
*   Please note that the values cited above (e.g. complete penetrance) are not asserted to be true for this condition. Rather, they are used in order to derive the most rigorous thresholds possible for a disease for which there are incomplete population epidemiology data.


#### BS1
- 默认强度：Benign Strong

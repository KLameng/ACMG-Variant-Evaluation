> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN088 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Common in population databases.

*   gnomAD popmax filtering allele frequency >0.00400
    *   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following parameters:
        *   Prevalence: 1:5,000
        *   Allelic heterogeneity: 1
        *   Genetic heterogeneity: 0.04 (based on the contribution of _RMRP_ variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
        *   Penetrance: 50%
    *   Use caution when applying BA1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of _RMRP_. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is greater than expected for disorder.  

*   gnomAD popmax filtering allele frequency >0.00089
    *   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following parameters:
        *   Prevalence: 1:50,000
        *   Allelic heterogeneity: 1

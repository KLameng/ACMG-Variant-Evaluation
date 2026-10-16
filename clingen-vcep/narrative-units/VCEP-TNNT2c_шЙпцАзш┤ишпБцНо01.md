> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN099 — Cardiomyopathy Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency is **≥0.001** based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

The values used to calculate the BA1 threshold were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/300 or lower).

The threshold is applicable when assessing variants in the context of autosomal dominant cardiomyopathy. 

gnomAD is the preferred database for this calculation. If a subpopulation specific FAF other than the popmax is needed, this value can be calculated using the AlleleFrequencyApp on the [CardioDB website](https://cardiodb.org/allelefrequencyapp/).

1.  Using the Inverse AF tab, enter in the population size and the number of alleles identified and it will calculate the FAF.  
2.  Set confidence to 0.95 (95%).
3.  If the FAF is ≥0.001, this rule can be applied.

The FAF by platform (e.g., exome vs. genome; v.2.1.1 vs. v.3.1.1) should be considered, the larger population is most likely to have the most accurate representation of “true” population allele frequency.


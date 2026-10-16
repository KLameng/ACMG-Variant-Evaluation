> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN020 — Hereditary Breast, Ovarian and Pancreatic Cancer Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Grpmax Filtering AF **\>.5%** in gnomAD v4 dataset


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Grpmax Filtering AF **\>.05%** in gnomAD v4 dataset


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** 📋：Use when a variant rescues both an ATM specifc feature (e.g. phosphorylation of ATM-specific targets) AND radiosensitivity.
- **Supporting** 📋：Use when a variant rescues EITHER an ATM specifc feature OR rescues radiosensitivity.


#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** 📋：BP2\_Strong **≤ -4** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Moderate** 📋：BP2\_Moderate = **\-2** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Supporting** 📋：BP2 = **\-1** point

See ATM PM3/BP2 table for approach to assign points per proband.


#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)

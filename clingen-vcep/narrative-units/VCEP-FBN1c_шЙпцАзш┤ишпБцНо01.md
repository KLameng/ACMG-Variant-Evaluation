> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN022 — FBN1 Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Allele frequency above 0.1% in ExAc and gnomAD
* Use the ethnic population with the highest allele frequency.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Allele frequency greater than expected for disease (>0.005%).
* Use the ethnic population with the highest allele frequency.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Use the ‘Funtional Assay SVI Documentation’ (https://clinicalgenome.org/working-groups/sequence-variant-interpretation/).
For step 2 assessment.
* Functional studies deemed appropriate:
 * cDNA analyses showing altered FBN1 sequence.
 * Functional studies showing altered FBN1 protein or RNA expression, proteolysis, folding, assembly, trafficking, secretion, Ca2+ binding, matrix deposition (cfr Dave Hollister assay), microfibril fragmentation/catabolism in an in vitro engineered system.
* Functional studies NOT deemed appropriate: non-specific altered TGF-beta signaling or histological hallmarks of medial degeneration, which are associated with many other types of variants in genes that are associated with MFS or HTAAD in general.

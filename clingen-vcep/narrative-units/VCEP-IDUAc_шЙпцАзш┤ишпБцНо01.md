> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN091 — Lysosomal Diseases Variant Curation Expert Panel

### 良性质证据规则（BS/BP/BA）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Any variant with Grpmax >0.005 in the most recent version of gnomAD (95% confidence interval, lower bound) (version # will be stated in the written summary)

BA1 minor allele frequency cut-off calculated using [http://cardiodb.org/allelefrequencyapp](http://cardiodb.org/allelefrequencyapp) with prevalence = 1 in 40,000 (PMID: 33208168), genetic heterogeneity = 1.0 (IDUA is the only gene known to cause MPS1), allelic heterogeneity = 1.0, and penetrance = 1.0.


#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Any variant with Grpmax >0.0025 in the most recent version of gnomAD (95% confidence interval, lower bound) (version # will be stated in the written summary).

BS1 minor allele frequency cut-off calculated using [http://cardiodb.org/allelefrequencyapp](http://cardiodb.org/allelefrequencyapp) with prevalence = 1 in 40,000 (PMID: 33208168), genetic heterogeneity = 1.0 (IDUA is the only gene known to cause MPS1), allelic heterogeneity = ~0.5 (frequency of the most common known pathogenic variants in patients with MPS1 (PMID: 28595941, 29393969), and penetrance = 1.0.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：The same assays outlined for PS3 will be used for BS3. Please see PS3 guidance for additional information on these assays. 


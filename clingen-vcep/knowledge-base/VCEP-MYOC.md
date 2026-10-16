# ClinGen VCEP基因特异性规范：MYOC

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN019 — Glaucoma Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0005338**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Same amino acid change as previously established pathogenic variant
- **Moderate** 📋：Same amino acid change as a previously established likely pathogenic variant

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** 📋：*   ≥2 confirmed de novo in JOAG
- **Moderate** 📋：*   ≥2 confirmed de novo in POAG
*   Or 1 confirmed de novo in JOAG
*   Or ≥2 assumed _de novo_ in JOAG
- **Supporting** 📋：*   1 confirmed de novo in POAG
*   Or ≥2 assumed _de novo_ in POAG
*   Or 1 assumed _de novo_ in JOAG

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Assays with OddsPath >18.7 as per the SVI recommendations.[<sup>1</sup>](#PMID_31892348)
- **Moderate** 📋：Assays with OddsPath >4.3 as per the SVI recommendations.[<sup>1</sup>](#PMID_31892348)
- **Supporting** 📋：Assays with OddsPath >2.1 as per the SVI recommendations.[<sup>1</sup>](#PMID_31892348)

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：≥ 15 probands from multiple independent studies.
- **Moderate** 📋：≥ 6 probands from multiple independent studies.
- **Supporting** 📋：≥ 2 probands from multiple independent studies.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Allele frequency ≤ 0.0001 in population databases.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：In-frame del/ins, stop-loss variants and truncating variants involving >10% of the protein and located within the conserved olfactomedin domain (AA 246-502).
- **Supporting** 📋：In-frame del/ins, stop-loss variants and truncating variants involving ≤10% of the protein and located within the conserved olfactomedin domain (AA 246-502).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Same residue as 2 previously established pathogenic variants or 1 previously established pathogenic and 2 likely pathogenic variants or 4 previously established likely pathogenic variants (all assessed independently of PM5)
- **Moderate** 📋：Same residue as a previously established pathogenic variant (assessed independently of PM5) or 2 previously established likely pathogenic variants (both assessed independently of PM5)
- **Supporting** 📋：Same residue as a previously established likely pathogenic variant (assessed independently of PM5)

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：≥7 meioses in >1 family
- **Moderate** 📋：≥ 5 meioses regardless of the number of families
- **Supporting** 📋：≥ 3 meioses regardless of the number of families

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** 📋：REVEL score of ≥ 0.932
- **Moderate** 📋：REVEL score of 0.773-0.931
- **Supporting** 📋：REVEL score of 0.644-0.772

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Allele frequency ≥ 0.01 in population databases.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Allele frequency ≥ 0.001 in population databases.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** 📋：Applies to variants showing solubility or secretion in functional assays for studies with OddsPath \<0.23 as per the SVI recommendations.
- **Supporting** 📋：Applies to variants showing solubility or secretion in functional assays for studies with OddsPath \<0.48 as per the SVI recommendations.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** 📋：REVEL score of ≤ 0.016
- **Moderate** 📋：REVEL score of 0.017-0.183
- **Supporting** 📋：*   For missense variants: REVEL score of 0.184-0.290
*   For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI ≤ 0.1

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Apply to intronic/noncoding and synonymous (silent) exonic variants if BP4 is met

### 不适用证据码
PVS1、PM1、PM3、PM6、PP2、PP4、PP5、BS2、BS4、BP1、BP2、BP3、BP5、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN019)

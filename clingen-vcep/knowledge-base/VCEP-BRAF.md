# ClinGen VCEP基因特异性规范：BRAF

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.3（DOI: 10.5281/zenodo.21433906；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN049 — RASopathy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0021060**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in _BRAF_ and _RAF1_.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：4 Points.
- **Strong** ✅：2 Points.
- **Moderate** ✅：1 Point.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Moderate** ✅：Two or more different approved assays.
- **Supporting** ✅：One approved assay.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：≥5 points.
- **Moderate** ✅：≥3 points.
- **Supporting** ✅：≥1 points.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Applicable only to critical and well-established functional domains available in the supplementary table (exon 6, exon 11, P-loop \[AA 459-474\], CR3 activation segment \[AA 594-627\]). Not applicable to specific amino acid residues (see PM5).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：The variant must be absent from controls (gnomAD).

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：No known repetitive areas in gene. Use as described.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：≥2 different \[likely\] pathogenic residues changes at the same codon observed in ≥5 probands.
- **Moderate** ✅：1 \[likely\] pathogenic residue change at the same codon.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：2 Points.
- **Moderate** ✅：1 Point.
- **Supporting** ✅：0.5 Points.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：≥7 informative meioses.
- **Moderate** ✅：≥5 informative meioses.
- **Supporting** ✅：≥3 informative meioses.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：Missense z score is >3.09 in gnomAD.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：GnomAD filtering allele frequency ≥0.05%.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：GnomAD filtering allele frequency ≥0.025%.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：\-4 Points.
- **Supporting** ✅：\-1 Point.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Requires only one informative meiosis.

#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Supporting** ✅：This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi exon deletion) in genes without established LOF correlation to disease. See the supplemental material regarding dosage sensitivity information for each individual gene and potential association to disorders associated with LOF variants.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** ✅：≥ (-4) Points.
- **Moderate** ✅：≥ (-2) Points.
- **Supporting** ✅：≥ (-1) Point.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants: REVEL ≤0.3.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：≥ (-4) Points.
- **Moderate** ✅：≥ (-2) Points.
- **Supporting** ✅：≥ (-1) Point.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4.

### 不适用证据码
PVS1、PM3、PP4、PP5、BS3、BP3、BP6
### 参考附件
- [Approved Functional Studies](https://cspec.genome.network/cspec/File/id/c73514de-466a-4cda-b3bb-1185c98ace42/data)
- [Analogous Residues](https://cspec.genome.network/cspec/File/id/32f80d27-eb67-40f5-b85c-57d03eda7ca1/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN049)

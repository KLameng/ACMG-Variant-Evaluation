# ClinGen VCEP基因特异性规范：POLG

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN014 — Mitochondrial Diseases Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0044970**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Applied per PVS1 flowsheet of Abou Toyoun et al.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo in a patient with the disease and no family history

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Rarely, pathogenic variants cause disease in an AD manner. For these variants only, presence in: 2 unrelated probands will be considered supporting evidence, 4 unrelated probands will be considered moderate evidence, 16 unrelated probands will be strong evidence.
 * Note: This will only be utilized when there is segregation evidence supporting autosomal dominant inheritance

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Moderate** ✅：<0.0005 (<0.05% )

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Moderate** ✅：Use per SVI guidance.
Note: T251I and P587L are almost always in cis

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes as a result of in-frame deletions/insertions in a nonrepeat region or stop-loss variants

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：De novo in a patient with the disease and no family history
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Supporting** ✅：Further define “affected” as an individual in whom there is objective evidence of manifestations consistent with POLG-related disorders spectrum: Alpers-Huttenlocher syndrome (AHS), childhood myocerebrohepatopathy spectrum (MCHS), myoclonic epilepsy myopathy sensory ataxia (MEMSA), ataxia neuropathy spectrum (ANS), and/or progressive external ophthalmoplegia (PEO)

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Agree to utilize REVEL, with thresholds of >0.75 and <0.15 for PP3 and BP4, respectively
 * Will also utilize POLG pathogenicity prediction server if/when live again (PMID: 28480171); both tools (REVEL and server) will have to be in agreement to score

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：1. Mitochondrial DNA depletion showing ≤ 20% of controls, OR 
2. Multiple mitochondrial DNA deletions (NOTE:depletion and/or deletion analysis must be performed in muscle and/or liver; other tissues such as blood, fibroblast, and buccal are not acceptable; Must be performed in child, as defined as <18 years old) 
Note: For both scenarios 1 and 2, will only apply if other mtDNA maintenance disorders have been excluded (exome sequencing or comprehensive panel-based testing)
- **Supporting** ✅：1. Mitochondrial DNA depletion showing 20-50% of controls in children (< 18 years of age), AND/OR 
2. COX negative fibers in muscle in children and/or adults
Note: Will only apply if other mtDNA maintenance disorders have been excluded (exome sequencing or comprehensive panel-based testing)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：>0.01 (>1%)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：>0.005 (>0.5% - AR)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual in the homozygous state AND/OR Normal mtDNA content (1. Must be performed in muscle and/or liver; blood, fibroblast, and buccal not acceptable; 2. Must be performed in children only - defined as <18 years old; 3. A normal level is defined as >50%.)
- **Supporting** ✅：Lack of COX negative fibers in muscle (children and adults)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected and/or treated members of a family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Agree to utilize REVEL, with thresholds of >0.75 and <0.15 for PP3 and BP4, respectively. Will also utilize POLG pathogenicity prediction server if/when live again (PMID: 28480171); both tools (REVEL and server) will have to be in agreement to score

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved

### 不适用证据码
PS3、PM1、PP2、PP5、BS3、BP1、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN014)

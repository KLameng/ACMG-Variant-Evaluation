# ClinGen VCEP基因特异性规范：MTOR

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN018 — Brain Malformations Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0016054**（遗传方式：未指定）

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：No change.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** 📋：Award the PS2_Strong point if Criteria 1 AND Criteria 2 are fulfilled.  

  Criteria 1. The variant is present at a detectable allele fraction but is absent from parental samples with confirmed maternity and paternity.

  Criteria 2. The variant is present at a detectable allele fraction in an affected tissue sample but is absent from or detected at a lower allelic fraction in another tissue (e.g. if present in 5% of brain tissue but absent from the blood or skin this point can be awarded).

For the sake of implementation, these criteria are intended to apply to high-confidence somatic mutations identified by the reporting CLIA laboratory. The expert panel recognizes that in practice there may be significant heterogeneity in the technical methods and thresholds used to identify such variants as 'high confidence', and flags the need to establish consensus statistical frameworks (e.g. Phred-scaled genotype qualities) or experimental approaches (e.g., confirmation of somatic variants by sequencing on orthogonal platforms) by which quality thresholds can be consistently applied.
- **Moderate** 📋：Award the PS2_Moderate point if Criteria 1 is fulfilled, OR if parents are not available but Criteria 2 is fulfilled.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Follow recommendations set forth by the SVI in conjunction with specifications added by the BMVCEP for quality metrics and minimum validation controls required. (Supplemental Document 1) Animal models are considered in a different manner.

Award PS4_Strong if the animal model generated with the variant of interest expressed in neural progenitors shows a complementary brain phenotype.

Award PS3 if the functional assay meets the acceptability criteria delimited in (PMID: 31892348) with specifications added by the BMVCEP. Quality metrics and minimum validation controls required can be found in Supplementary Document 1.

Animal models are considered in a different manner. Award PS4_Strong if the animal model generated with the variant of interest expressed in neural progenitors show a complementary brain phenotype.

Caveat: Studies of cell lines derived from the affected patient as the only source of functional characterization are by themselves insufficient to provide strong evidence of pathogenicity. This is because cells derived from patient affected tissue are likely to exhibit the desired phenotype since the patient tissue exhibits the phenotype. It is therefore impossible to determine whether the variant of interest was solely responsible for that phenotype. Instead, functional readout of patient-derived cells are now included in PS4.
- **Moderate** 📋：Follow recommendations set forth by the SVI in conjunction with specifications added by the BMVCEP for quality metrics and minimum validation controls required (PMID: 31892348). Animal models are considered in a different manner. Award PS4_Moderate if the animal model generated with the variant of interest expressed in non-neural tissues show an increased cancer burden.
- **Supporting** 📋：Follow recommendations set forth by the SVI in conjunction with specifications added by the BMVCEP for quality metrics and minimum validation controls required (PMID: 31892348).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：Points are assigned for phenotype according to (Table 2A). Phenotype criteria can only be used if the variant meets criteria for (PM2). Strength of evidence is determined by points according to (Table 2B). PS4\_VeryStrong ≥ 16 points. For PS4, for cases reported in the literature, we recommend assigning each one to the SINGLE category below that is associated with the highest point value (Table 2A). The total score obtained for all reported cases with a particular variant will determine the strength of PS4 assigned according to the scale (Table 2B)<sup>*</sup>.

_PS4\_VeryStrong ≥ 16 points._

<sup>*</sup>Applicable if the variant is absent/rare from controls according to PM2 to ensure the variant is not simply present due to beinging common in the general population.
- **Strong** 📋：Points are assigned for phenotype according to (Table 2A). Phenotype criteria can only be used if the variant is absent from controls (PM2). Strength of evidence is determined by points according to (Table 2B). PS4_Strong = 3.5-15.75 points.
- **Moderate** 📋：Points are assigned for phenotype according to (Table 2A). Phenotype criteria can only be used if the variant is absent from controls (PM2). Strength of evidence is determined by points according to (Table 2B). PS4_Moderate = 1.5-3.25 points.
- **Supporting** 📋：Points are assigned for phenotype according to (Table 2A). Phenotype criteria can only be used if the variant is absent from controls (PM2). Strength of evidence is determined by points according to (Table 2B). PS4_Supporting = 0.5 – 1.25 points.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Supporting** 📋：Residues affecting critical functional domains provided in Table 4 for each gene.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Absent/rare from controls in an ethnically-matched cohort population sample ( ≥1).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：No change.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** 📋：Missense constraint computed in ExAC/gnomAD was utilized. Award PP2 if the z-score > 3.09. (applicable to MTOR, PIK3CA and AKT3 but not PIK3R2).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Allele frequency (>0.0926%). An allele frequency (>0.0926%) was approved.
 Note: this was adjusted from ACMG Guidelines due to maintaining the 5x threshold for benign (consistent with previously established guidelines)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Allele frequency (>0.0185%). An allele frequency (>0.0185%) was approved. (Supplemental Table 3).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Award BS2 if ≥3 homozygotes present in gnomAD or ≥3 heterozygous in well phenotyped family members.
Clinical laboratories are encouraged to accumulate more than 2 (≥3) instances of well phenotyped family members before applying this strong criterion. To be considered for this point, the variant should be either germline (most common), or somatic in a relevant tissue. Homozygous occurrences in gnomAD or ExAC can also be counted for this point (≥3).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Follow recommendations set forth by the SVI in conjunction with specifications added by the Brain Malformation Group for quality metrics and minimum validation controls required.
- **Supporting** 📋：Follow recommendations set forth by the SVI in conjunction with specifications added by the Brain Malformation Group for quality metrics and minimum validation controls required.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in cis or trans with a known pathogenic variant in the same gene.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Award BP4 for a synonymous, intronic positions (except canonical splice sites) or non-coding variants in the UTRs, if two out of three of the splicing prediction tools predicted no impact on splicing function.
Not applicable for any variant type except for synonymous, intronic positions (except canonical splice sites) and non-coding variants in the UTRs,. This criterion can be applied when two of three splicing prediction tools predict no splicing change. The splicing prediction tools used are: varSEAK, spliceAI and MaxEntScan.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：No change.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：For synonymous, intronic positions (except canonical splice sites) and non-coding variants in the UTRs, if the nucleotide is non-conserved award this point (PhyloP score <0.1).

### 不适用证据码
PVS1、PM3、PM4、PM6、PP1、PP3、PP4、PP5、BS4、BP1、BP3、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN018)

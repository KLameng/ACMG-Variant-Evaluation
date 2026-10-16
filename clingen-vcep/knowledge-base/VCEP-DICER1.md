# ClinGen VCEP基因特异性规范：DICER1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN024 — DICER1 and miRNA-Processing Gene Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100216**（遗传方式：Autosomal dominant inheritance）

### 通用说明
For more information, please see our open access publication: https://www.hindawi.com/journals/humu/2023/9537832/
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Follow SVI guidance, using DICER1-specific information. Per the PVS1 workflow guidance provided in Tayoun et al. 2018[<sup>1</sup>](#pmid_30192042), the following will apply:

*   Nonsense or frameshift variants:
*   PVS1 applies to variants predicted to result in nonsense-mediated decay (NMD); the predicted NMD cutoff for DICER1 occurs at p.Pro1850.
*   PVS1\_Moderate applies to variants resulting in protein truncation 3’ of this cutoff
*   Canonical splice variants (+/- 1,2 intronic positions): PVS1 applies with the following exceptions:
*   Exon 10 SDS/SAS: PVS1\_Strong (in-frame but exon includes >10% protein)
*   Exons 5, 15, 18, 22 SDS/SAS: PVS1\_Moderate (in-frame and each \<10% of protein)
*   Exon 27 SAS: PVS1\_Moderate (final exon)
*   Exon 1: no criteria (non-coding)
*   Variants that disrupt the translation start site (p.M1?): no criteria applied given p.M1 is not highly conserved, there are three in-frame possible alternate start codons (p.Met11, p.Met17, p.Met24), and multiple lab cases of p.Met1? without DICER1 phenotype. SDS = splice donor site; SAS = splice acceptor site. Refer to PS3 weight guidelines when a variant meets criterion for application of both PVS1 and PS3. A disease-specific PVS1 decision tree incorporating the above bullets is also included at the end of this document as an additional curation tool.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：For same AA change, must confirm there is no difference in splicing using RNA data or in-silico modeling data (concordance of MaxEntScan and SpliceAI). For non-canonical intronic splicing variants at same nucleotide should have equal or worse splicing impact.
This rule code can only be used to compare variants asserted as pathogenic by the ClinGen DICER1 VCEP. Likely pathogenic changes do not apply.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：≥4 de novo points
- **Strong** 📋：≥2 but less than 4 de novo points
- **Moderate** 📋：≥1 but less than 2 de novo points
- **Supporting** 📋：≥0.5 but less than 1 de novo points

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：RNA assay shows splicing impact that is out-of-frame, in-frame ≥193 residues, or in-frame with RNase IIIb disruption. (PS3\_Moderate if PVS1\_Strong is applied).
- **Moderate** 📋：RNA assay shows in-frame splicing impact with change in protein length \<193 residues AND RNase IIIb domain not disrupted.
- **Supporting** 📋：In vitro cleavage assay shows failure or severely reduced capacity to produce either 5p or 3p microRNAs from a premiRNA (positive and negative controls also performed).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：≥4 phenotype points
- **Moderate** 📋：2 – 3.5 phenotype points
- **Supporting** 📋：1 – 1.5 phenotype points

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：Putative missense variants at residues affecting metal ion-binding: codons p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, p.E1813
- **Supporting** 📋：Putative missense variants at residues in the RNase IIIb domain (p.Y1682 – p.S1846), besides the metal ion-binding residues (see PM1).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Allele frequency \<0.000005 across gnomAD with no more than one allele in any subpopulation and at least 20x coverage.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：In-frame indels with a residue within the RNase IIIb domain (p.Y1682 – p.S1846).
- **Supporting** 📋：In-frame indels outside of the RNase IIIb domain (p.Y1682 – p.S1846) and repeat regions (p.D606-p.D609; p.E1418-p.E1420; p.E1422-p.E1425).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：Missense variant under evaluation should have equal or worse Grantham score. Splicing should be ruled out with either RNA data or agreement in splicing predictors (MaxEntScan and SpliceAI) that show no splicing effects. The other variant must be interpreted as pathogenic by the ClinGen DICER1 VCEP. Likely pathogenic changes do not apply. This rule cannot be applied in combination with PM1 or PS1.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：≥7 meioses across ≥2 families
- **Moderate** 📋：5 – 6 meioses across ≥1 family
- **Supporting** 📋：3 – 4 meioses across ≥1 family

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：For missense variants, REVEL score ≥ 0.750 OR agreement in splicing predictors predict splicing effects. For splicing variants, concordance of MaxEntScan and SpliceAI.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** 📋：Somatic tumor testing identifies somatic hotspot second hit and no additional somatic LOF variants. Tumor testing[<sup>6</sup>](#pmid_30311369) of a neoplasm with known DICER1 association in a proband who carries the germline variant under evaluation reveals the following:

*   A previously reported somatic second hit of DICER1 in an RNase IIIb-disrupting “hotspot” codon (p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, or p.E1813) AND
*   Retention of the germline DICER1 variant under evaluation. PP4 is NOT applicable if:
*   The germline variant is a missense variant in one of the seven RNase IIIb “hotspot” codons (see PM1), OR
*   Somatic sequencing reveals additional DICER1 non-hotspot variants (could be consistent with sporadic tumorigenesis).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Frequency >0.003 (0.3%) in gnomAD subpopulations. Subpopulations must have >2,000 alleles tested and a minimum of 5 alleles present.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Frequency >0.0003 (0.03%) in gnomAD subpopulations. Subpopulations must have >2,000 alleles tested and a minimum of 5 alleles present.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：40+ unrelated females from a single source are tumor-free through age 50 (caveat: ratio of BS2-eligible females to PS4-eligible probands must be ≥ 40:1) 
OR 2+ observations of homozygosity in healthy individuals
OR 1+ observation(s) of homozygosity in a healthy individual with status confirmed by parental testing.
- **Supporting** 📋：10+ unrelated females from a single source are tumor-free through age 50 (caveat: ratio of BS2-eligible females to PS4-eligible probands must be ≥ 10:1) 
OR 2+ observations of homozygosity in individuals lacking clinical information

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：For intronic or synonymous variants, no splicing impact observed via RNA assay. (Should be observed more than once.)
- **Supporting** 📋：An in vitro cleavage assay must demonstrate the variant produces both 5p and 3p microRNAs from a pre-miRNA (positive and negative controls also performed). An example of an appropriate assay to which criteria could be applied is Wu et al. 2018[<sup>7</sup>](#pmid_28862265).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Family members should be phenotype-positive (must be high- or moderatespecificity phenotype; see phenotype table), genotype-negative 1st, 2nd, or 3rd degree relatives of the proband.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：≥1 observation in trans with P/LP DICER1 variant or ≥3
observations in cis or phase unknown with 2+ different
P/LP DICER1 variants.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：For missense variants, REVEL score \< 0.500 and agreement in splicing predictors that no splicing effects are predicted. For synonymous/intronic/non-coding variants concordance of MaxEntScan and SpliceAI.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Silent variant
OR Intronic variant at or beyond +7 to -21 positions
OR Other intronic or non-coding variant if the variant is the reference nucleotide in ≥1 primate and/or ≥4 mammalian species.
Caveat: Variant must meet BP4 to apply BP7

### 点系统分类（Tavtigian 贝叶斯框架，v1.4 浏览器实页核实 2026-10-08）

本规范（Version 1.4，Released 7/8/2025；Type: Tavtigian et.al., 2020 - Bayesian adaptation of Richards et.al., 2015；v1.4 起正式将规范类型登记为 Tavtigian 点系统）采用贝叶斯适配的点系统。各证据码强度对应的 Default Point Value 如下：

**致病方向（正分）**

| 积分 | 证据码强度 |
|---|---|
| +8 | PVS1（Very Strong）、PS2（Very Strong） |
| +4 | PS1、PS2_Strong、PS3_Strong、PS4_Strong、PP1_Strong |
| +2 | PS2_Moderate、PS3_Moderate、PS4_Moderate、PM1_Moderate、PM4_Moderate、PM5、PP1_Moderate |
| +1 | PS2_Supporting、PS3_Supporting、PS4_Supporting、PM1_Supporting、PM2_Supporting、PM4_Supporting、PP1_Supporting、PP3、PP4 |

**良性方向（负分）**

| 积分 | 证据码强度 |
|---|---|
| Stand Alone（不记分，独立判良性） | BA1 |
| -4 | BS1、BS2_Strong、BS3_Strong、BS4 |
| -1 | BS2_Supporting、BS3_Supporting、BP2、BP4、BP7 |

**Point Based Variant Classification Categories（积分分类切分，本规范为基因特异边界）**

| 分类 | 积分区间 |
|---|---|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | -1 – 5 |
| Likely Benign | -6 – -2 |
| Benign | ≤ -7 |

> 附加规则：当最终积分为 -1 时，若已应用至少 2 个良性证据码且唯一的致病方向证据码仅为 PM2_Supporting，可将该 -1 覆盖上调为 Likely Benign。

### 不适用证据码
PM3、PM6、PP2、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [PVS1](https://cspec.genome.network/cspec/File/id/c0fdf557-515c-4f9e-b5d6-5c9efddcd901/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN024)

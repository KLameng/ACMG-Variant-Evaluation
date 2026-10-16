# ClinGen VCEP基因特异性规范：F8

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.0（2026-01-20）；本规范采用贝叶斯积分体系（Tavtigian et al. 2020），各证据码标注 Default Point Value。
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN071 — Coagulation Factor Deficiency Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010602**（遗传方式：X-linked inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.
- **Strong** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.
- **Moderate** 📋：Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on _F8_ gene rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.

**OR**

When two or more variants are share the same predicted splicing effect and one comparison splicing variant reaches a pathogenic classification or 2 comparison variants reach a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications modified from Walker, et al 2023 (PMID: 37352859).
- **Moderate** 📋：This evidence code can be applied when there is 1 likely pathogenic variants at the same residue based on _F8_ gene rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggesting a splicing defect.

**OR**

When the comparison variant shares the same predicted splicing effect and the comparison splicing variant reaches a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications based on Walker, et al 2023 (PMID: 37352859).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：Use the SVI recommendations for de novo cases; 4 points. Use de novo guidance below to determine point value.
- **Strong** 📋：Use the SVI recommendations for de novo cases; 2 points. Use de novo guidance below to determine point value.
- **Moderate** 📋：Use the SVI recommendations for de novo cases; 1 point. Use de novo guidance below to determine point value.
- **Supporting** 📋：Use the SVI recommendations for de novo cases; 0.5 point. Use de novo guidance below to determine point value.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：Abnormal factor VIII activity (\<40 IU/dL or 40%) via one-stage or two-stage chromogenic assay in a cell line and/or mouse model.

\--OR--

Absent or significantly reduced factor VIII antigen levels compared to wildtype in a cell line by quantitative assay.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：≥8 probands meet criteria described below
- **Strong** 📋：4-7 probands meet criteria described below
- **Moderate** 📋：2-3 probands meet criteria described below
- **Supporting** 📋：1 proband meets criteria described below

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** 📋：This code can be applied at the strong level for variants involving the following residues: R391-S392, R759-S760, E1701-Q1705, R1708-S1709, Y1683, Y1689, Y737, Y742.
- **Moderate** 📋：This code can be applied at the moderate level for variants involving the following residues: 

Residues affecting secretion: Arg1667, Arg1332

FXa-binding residues: Gly2267-Gly2304 (with the exception of Ser2283)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Moderate** 📋：可用默认强度（Default Point Value: 2）。
- **Supporting** 📋：Variant must be absent in males in population databases, such as gnomAD.（Default Point Value: 1）

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** 📋：可用默认强度（Default Point Value: 4）。
- **Moderate** 📋：Use code with no specification.（Default Point Value: 2）
- **Supporting** 📋：可用默认强度（Default Point Value: 1）。

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
- **VCEP说明**：单一变异同时应用 PM1 与 PM5 时，两码合并权重最高只能等于 Strong。
- **Strong** 📋：可用默认强度（Default Point Value: 4）。
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on the _F8_ rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.
- **Supporting** 📋：This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on the _F8_ rule specifications from the Coagulation Factor Deficiency VCEP and where _in silico_ predictors do not suggest a splicing defect.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：The code is application when there are ≥4 meioses across ≥2 families.
- **Moderate** 📋：The code is application when there are at least 3 meioses across one or more families.
- **Supporting** 📋：The code is application when there are 2 meioses in one family **OR** 1 meiosis between 2 affected siblings.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** 📋：可用默认强度（Default Point Value: 4）。
- **Moderate** 📋：可用默认强度（Default Point Value: 2）。
- **Supporting** 📋：Code can be applied for variants where the REVEL score is greater than or equal to 0.6 or a SpliceAI score of greater than or equal to 0.2.（Default Point Value: 1）

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** 📋：可用默认强度（Default Point Value: 4）。
- **Moderate** 📋：Proband must meet hemophilia A phenotype criteria AND have full gene sequencing and deletion/duplication analysis.（Default Point Value: 2）

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：MAF cutoff of greater or equal to 0.0333% (or 0.000333).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：MAF cutoff of greater than or equal to 0.00333% (or 0.0000333).（Default Point Value: -4）
- **Moderate** 📋：可用默认强度（Default Point Value: -2）。
- **Supporting** 📋：可用默认强度（Default Point Value: -1）。

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：This evidence code can be used when a _F8_ variant is observed in a male with a normal factor VIII activity level (at least >40% IU or as defined by laboratory cut off) using a one stage and/or a chromogenic assay.

- **Moderate** 📋：可用默认强度（Default Point Value: -2）。
- **Supporting** 📋：可用默认强度（Default Point Value: -1）。（Strong 档 Default Point Value: -4）

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：This code can be used for _F8_ gene variants studied in a cell line or mouse model setting that confer a normal factor VIII activity level AND normal factor VIII antigen level OR normal Western Blot.
- **Supporting** 📋：This code can be used for _F8_ gene variants studied in a cell line or mouse model setting that confer the following results:                    

*   Normal factor VIII activity level, OR
*   Abnormal factor VIII activity level with abnormal 2N binding assay suggesting a diagnosis of VWD Normandy (VWD 2N) instead of hemophilia A.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：This evidence code can be used when a _F8_ variant is observed in a male with a family history of hemophilia A and has a normal factor VIII activity level.

- **Moderate** 📋：可用默认强度（Default Point Value: -2）。
- **Supporting** 📋：可用默认强度（Default Point Value: -1）。（Strong 档 Default Point Value: -4）

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：This code can be applied for variants reaching a REVEL score of 0.3 or below AND a Splice AI score of less than or equal to 0.1.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay and a SpliceAI score of less than or equal to 0.1.
- **Supporting** 📋：Splice AI should be used to suggest no splicing impact. Splicing prediction score of less than or equal to 0.1 is required. Conservation should be assess using PhyloP (cutoff less than 0.1) and PhastCons (cutoff less than 0.5).

### Point Based Variant Classification Categories

> 本规范采用贝叶斯积分框架（Tavtigian et al. 2020），各证据码按其强度赋予 Default Point Value（Very Strong=8、Strong=4、Moderate=2、Supporting=1；良性码取负分），按累积总分判定分类。

| Category | Point Ranges |
| --- | --- |
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤ -7 |

### 不适用证据码
PM3、PM6、PP2、PP5、BP1、BP2、BP3、BP5、BP6
### 参考附件
- [F8 Approved Functional Assays](https://cspec.genome.network/cspec/File/id/88400bdc-90e1-4748-b31e-650682e52553/data)
- [F8 Decision Tree for PVS1 Rule Code](https://cspec.genome.network/cspec/File/id/b4a2eb7c-9c04-4eb5-b418-acc58668fa2e/data)
- [F8/F9 Pilot Study Results](https://cspec.genome.network/cspec/File/id/68fea930-1cd0-4ccd-8340-914949a63bc3/data)
- [Guidance for Combined De Novo Rule Code (PS2/PM6)](https://cspec.genome.network/cspec/File/id/b39c38c9-77f7-48cd-9ef4-82d2c37cb05b/data)
- [Guidance for Combining Pathogenic and Benign Rule Codes](https://cspec.genome.network/cspec/File/id/afec2090-d843-4f6a-a59a-708da9f7c237/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN071)

# ClinGen VCEP基因特异性规范：GP9

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN083 — Platelet Disorders Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0009276**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use _GP9_ modified decision tree as per SVI WG.
- **Strong** ✅：Use _GP9_ modified decision tree as per SVI WG.
- **Moderate** ✅：Use _GP9_ modified decision tree as per SVI WG.
- **Supporting** ✅：Use _GP9_ modified decision tree as per SVI WG.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Use as originally specified, but the comparison variant must reach a pathogenic classification using the these rule specifications in order to apply code.
- **Moderate** ✅：Use as originally specified, but the comparison variant must reach a likely pathogenic classification using the these rule specifications in order to apply code.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- VCEP限定：Only applicable when proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant. Only use "highly specific phenotype" scoring if all three BSS genes were sequenced. Otherwise use the "consistent but not highly specific" scoring. More detailed instructions are below if needed.
- **Very Strong** ✅：Use proposed SVI point recommendations. See further instruction below. Total of 4 points.
- **Strong** ✅：Use proposed SVI point recommendations. See further instruction below. Total of 2 points.
- **Moderate** ✅：Use proposed SVI point recommendations. See further instruction below. Total of 1 point.
- **Supporting** ✅：Use proposed SVI point recommendations. See further instruction below. Total of 0.5 point.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：In a transgenic animal model, must demonstrate minimal to no function.
- **Supporting** ✅：Functional assays measuring quantity of GP9 expression on cell surface measured by flow cytometry analysis of GPIb and GPIX when there is absent or near absent expression, >75% reduction (see spreadsheet for more detail).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- VCEP限定：According to Bragadottir, et al, individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable, quantitative abnormalities relevant to the disease (PMID: 25370924). Caveats, (1) The variant must be sufficiently rare, meeting PM2_supporting (2) There must be an assumed unrelated biallelic BSS patient, meeting PP4, before heterozygotes are considered (3) A single proband of a family can be included in either PM3 (biallelic proband) or PS4 (monoallelic proband), not both (4) Any additional family members are not included in PS4, they may be considered for segregation in PP1. Scoring: significantly reduced surface expression of GP1b measured by flow cytometry – 0.5pt OR giant platelets (MPD >7 microns) or macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) – 0.25pt.
- **Moderate** ✅：See instructions below for scoring heterozygous individuals only. Moderate strength applicable for score of 2+ points.
- **Supporting** ✅：See instructions below for scoring heterozygous individuals only. Supporting strength applicable for scores ranging from 1-1.75.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD MAF of less than or equal to 0.0000329.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- VCEP限定：In trans variants classified as a variants of uncertain significance, as per the GP9 rule specifications, must meet PM2_supporting to be scored. Conversely, in trans variants that meet a pathogenic or likely pathogenic classification using the GP9 rule specifications do not have to meet PM2_supporting criteria; however, they cannot meet BS1 or BA1 criteria. See PM3 instructions below for further detail.
- **Very Strong** ✅：Use proposed SVI point recommendations (see below). Both variants must be classified using these rule specifications.
- **Strong** ✅：Use proposed SVI point recommendations (see below). Both variants must be classified using these rule specifications.
- **Moderate** ✅：Use proposed SVI point recommendations (see below). Both variants must be classified using these rule specifications.
- **Supporting** ✅：Use proposed SVI point recommendations (see below). Both variants must be classified using these rule specifications.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Use with no specification.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use as originally specified, but the comparison variant must reach a pathogenic classification using these rule specifications in order to apply code.
- **Supporting** ✅：Use as originally specified, but the comparison variant must reach a likely pathogenic classification using these rule specifications in order to apply code.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- VCEP限定：For Bernard-Soulier syndrome (BSS), segregation of the variant in a pedigree is considered informative in the case of both additional relatives with BSS and in heterozygous relatives with measurable, quantitative abnormalities relevant to the disease. Caveat, there must be a biallelic BSS patient, meeting PP4, before segregation points are awarded. Additionally, heterozygous relatives counted for PP1 must not be counted for PS4. Segregation scoring: (1) Proband – 0 points (proband should be accounted for in PP4 or PS4); (2) BSS affected relative with the same biallelic variant(s) identified in the proband – 1 pt; (3) Relative heterozygous for the variant under assessment with a relevant measurable, quantitative abnormality — Caveat: only score one parent of a homozygous proband in a consanguineous pedigree (官网原 caveat 已于独立复核补录)；significantly reduced surface expression of GP1b measured by flow cytometry 0.5 pt OR giant platelets (MPD >7 microns) / macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) 0.25pt.
- **Strong** ✅：See instructions below for scoring system. Total segregation score 3+ points.
- **Moderate** ✅：See instructions below for scoring system. Total segregation score 2-2.75 points.
- **Supporting** ✅：See instructions below for scoring system. Total segregation score 1-1.75 points.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：REVEL score of ≥0.773 based on recommendations of Pejaver et al., 2022 (PMID: 36413997).
- **Supporting** ✅：REVEL score of ≥0.644 (to \<0.773), based on recommendations of Pejaver et al., 2022 (PMID: 36413997),

OR suggested splicing affect using SpliceAI greater than or equal to 0.5.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Must meet both criteria: 

1.  Proband with platelet aggregation study absent for ristocetin and present for all other agonists OR flow cytometry or Western blot less than 10% expression of GPIba 
2.  Proband must have full sequencing of all three BSS genes (_GP1BA, GP1BB_ and _GP9_) and deletion/duplication analysis.
- **Supporting** ✅：Proband with platelet aggregation study absent for ristocetin and present for all other agonists, OR flow cytometry or Western blot less than 10% expression of GPIba.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD MAF of greater than or equal to 0.001 (or 0.1%).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD MAF of greater than or equal to 0.0007 but less than 0.001.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Use this rule with 1 or more homozygotes who are unaffected (proven with aggregometry OR flow cytometry AND normal platelet count AND normal platelet size).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Must demonstrate normal aggregometry in a transgenic mouse model
- **Supporting** ✅：In a heterologous cell line, must demonstrate BOTH normal expression and normal protein function as compared to wildtype.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Variant not tracking in an affected family member.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Use as written for recessive variants (i.e. - variant must be observed in cis with a pathogenic variant)

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：Use with no specification

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- VCEP限定：Determine REVEL and Splice AI cutoff before applying this code. Do not use if PP3 is applicable.
- **Supporting** ✅：For a missense variant apply when REVEL score is less than or = to 0.290, based on recommendations of Pejaver et al., 2022 (PMID: 36413997) AND SpliceAI score is zero.

OR for a synonymous or intronic variant apply when SpliceAI score is zero.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- VCEP限定：Can be used for intronic variants. Can be used along with BP4.
- **Supporting** ✅：Use SpliceAI to rule out possible splicing defect (score = 0.2 or less) and reference PhyloP (score = 1.5 or less) to assess conservation.

### Rules for Combining Criteria（组合规则）

**Pathogenic（致病）**
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**Likely Pathogenic（可能致病）**
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate

**Benign（良性）**
- ≥ 2 Strong
- 1 Stand Alone

**Likely Benign（可能良性）**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PM1、PM6、PP2、PP5、BP1、BP5、BP6
### 参考附件
- [PVS1 flowchart for GP9 gene](https://cspec.genome.network/cspec/File/id/8ce0446b-4ce6-4428-8e4a-55e765999b85/data)
- [Guidance for Combining Pathogenic and Benign Rule Codes](https://cspec.genome.network/cspec/File/id/4cfe0386-46c4-4f51-8e87-4486c5f3c5e5/data)
- [Instructions for PS2_PM6 code use](https://cspec.genome.network/cspec/File/id/9ed41ee0-0c2e-45d1-b138-4b2eb76ec118/data)
- [Instructions for PM3 code use](https://cspec.genome.network/cspec/File/id/ca104a1d-1abc-4b18-ac0f-e403eeb7628d/data)
- [PS3_Supporting Functional Assays](https://cspec.genome.network/cspec/File/id/95a31d5a-89da-4587-aea2-5b8e4c3d10b8/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN083)

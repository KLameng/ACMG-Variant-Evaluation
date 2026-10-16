# ClinGen VCEP基因特异性规范：PAH

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：v2.0（DOI: 10.5281/zenodo.21421465；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN006 — Phenylketonuria Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0009861**（遗传方式：未指定）

### 通用说明
            Version 2.0

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Applicable as described in Tayoun et al. 2018.

*   Any nonsense or frameshift variant occurring upstream of c.1285
*   Any canonical splice site predicted to disrupt reading frame and undergo nonsense mediated decay

PVS1 (RNA): splicing assay data - assays demonstrating a variant leads to aberrant splicing profile that can be categorized against a PVS1 decision tree

*   Use the PVS1 decision tree to determine code strength
*   Applicable as described in Walker et al. (PMID: 36865205)
- **Strong** ✅：Use PVS1\_strong with:

*   Any nonsense or frameshift variant occurring downstream of c.1285
*   Any canonical splice site predicted to preserve reading frame (skipping of exons 1, 9, 10) or affect the last exon (exon 13)
*   Initiator codon variant

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same predicted splicing impact as a previously classified (likely) pathogenic variant

Applicable as described in Walker et al. (PMID: 36865205)

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity. Only applicable when proband has a known pathogenic variant in trans with the de novo variant.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Moderate** ✅：Functional studies with sufficient analyses to calculate OddsPath reaching strong have not been identified. Therefore, the strength of this criteria is modified to PS3_moderate or PS3_supporting for future or existing studies.

*   In vitro enzyme activity <50% compared to wild type controls.
*   Expression systems placing the mutant (and wild-type) cDNAs into plasmid vectors and introducing these into human or other mammalian host cells, which is the closest available approximation to the in vivo situation (e.g., COS cells) (Trunzo et al. Gene. 2016. 594:138-143. PMID: 27620137).
*   With ≥11 benign/pathogenic variant controls used in assay
*   NOTE: no papers that meet PS3_Moderate criteria have been identified by the PAH VCEP at time of this specification update. However, there may be future studies that meet the above criteria where a moderate level of evidence can be applied.
- **Supporting** ✅：In vitro enzyme activity ≤50% compared to wild type controls

*   with ≤10 benign/pathogenic variant controls used in assay

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：*   Active site residues in PAH include: Tyr138, Arg158, Val245, Tyr268, Thr278, Pro279, Glu289, Ala300, Asp315, Phe331, Ala345, Gly346, Ser349, Tyr377
*   Substrate binding residues in PAH are: 46-48, 63-69
*   Cofactor binding residues in PAH are: His285, His290, Glu330, 246-266, 280-283, 322-326, 377-379
*   Do not apply if PP3\_Strong applies

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Threshold <0.0002 (0.02%)

*   The 0.0002 cutoff is based on disease frequency of 1:12,000 and the most common PAH pathogenic variant, R408W, the ExAC frequency is 0.0006594 (ExAC MAF: 0.001109 74/66718 European Non-Finnish) and gnomAD overall: 0.0009056 (gnomAD MAF: 0.001728 219/126,700 European Non-Finnish).

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Applicable as described in SVI recommendations for in trans criterion
- **Strong** ✅：Applicable as described in SVI recommendations for in trans criterion
- **Moderate** ✅：Applicable as described in SVI recommendations for in trans criterion
- **Supporting** ✅：Applicable as described in SVI recommendations for in trans criterion

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Applicable as described

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Applicable as described.
- **Supporting** ✅：Applicable when the different missense change is likely pathogenic.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：*   3 affected segregations + 0 unaffected segregations OR
*   2 affected segregations + 3 unaffected segregations
- **Moderate** ✅：*   2 affected segregations + 0 unaffected segregations
- **Supporting** ✅：*   1 affected family member + 3 unaffected segregations

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **VCEP Specifications**：Per SVI recommendations (PMID: 36865205), PP3 should not be used for variants with experimental evidence of altered splicing; for variants without experimental evidence of altered splicing, PP3 can be used for variants that have a SpliceAI delta score of ≥0.2.
- **Strong** ✅：Applicable as described in Pejaver et al (PMID: 36413997): REVEL score ≥0.932 for missense variants
- PP3 + PM1 should not exceed Strong
- **Moderate** ✅：Applicable as described in Pejaver et al (PMID: 36413997): REVEL score 0.773 - 0.932 for missense variants
- **Supporting** ✅：Applicable as described in Pejaver et al. (PMID: 36413997):

*   REVEL score of 0.644 - 0.733 for missense variants
*   In frame deletion or insertion predicted deleterious by 2 out of 3 tools (PROVEAN, MutationTaster, MutPred-InDel)
*   Predicted impact on splicing by SpliceAI (score >0.5)

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Plasma phenylalanine concentration persistently above 120 µmol/L (2mg/dL), and either normal urine pterins and normal DHPR activity, or sequencing of genes in the BH4 cofactor metabolism pathway to exclude a defect of BH4 cofactor metabolism.
- **Supporting** ✅：A plasma phenylalanine concentration persistently above 120umol/L (2mg/dL) without analysis of urine pterins, DHPR activity, or sequencing to exclude defects of BH4 cofactor metabolism.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：An allele frequency ≥0.015 (1.5%), which is calculated with genetic heterogeneity of 90% to account for defects of BH4 metabolism, and penetrance of 80% to account for individuals who come to attention after becoming clinically symptomatic.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency ≥0.002 (0.2%)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Only to be used when variant is observed in the homozygous state in a healthy adult.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：In vitro enzyme activity >85% compared to wild type

*   Expression systems: placing the mutant (and wildtype) cDNA into plasmid vectors and introducing these into host cells. Transiently transfected human or other mammalian host cells are the closest available approximation to the in vivo situation (e.g., COS cells) (Trunzo, et al. Gene. 2016. 594:138-143).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Applicable as described

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **VCEP Specifications**：BP4_very strong: applicable as described in Pejaver et al.
- **Strong** ✅：Applicable as described in Pejaver et al.
- **Moderate** ✅：Applicable as described in Pejaver et al.
- **Supporting** ✅：Applicable as described in Pejaver et al.

*   REVEL score of 0.183 - 0.290 for missense variants
*   In frame deletion or insertion predicted benign by PROVEAN, MutationTaster, and MutPred-InDel
*   No predicted impact on splicing by SpliceAI (score \<0.1)

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Applicable as described

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Applicable as described by Walker et al. (PMID: 36865205).
- **Supporting** ✅：Per SVI recommendations (PMID: 36865205), use BP7 only if BP4 is met; for variants with experimental evidence supporting that they do not alter splicing, use BP7\_strong (RNA)

*   intronic variants must be outside +7/-21 nt
*   exonic variants must be outside first and last 3 bases of exon

### Rules for Combining Criteria

#### Pathogenic
- 1 Very Strong (PVS1, PM3_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)
- 1 Very Strong (PVS1, PM3_Very Strong) AND ≥ 2 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Very Strong (PVS1, PM3_Very Strong) AND 1 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND 1 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Very Strong (PVS1, PM3_Very Strong) AND ≥ 2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND ≥ 3 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND 2 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND 1 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PM3_Very Strong) AND 1 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND 1 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND ≥ 2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- ≥ 3 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 2 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong) AND 2 Moderate (PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4, BP4_Strong, BP7_Strong)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS4, BP4_Strong, BP7_Strong) AND 1 Supporting (BS3_Supporting, BP4, BP5, BP7)
- ≥ 2 Supporting (BS3_Supporting, BP4, BP5, BP7)

### 不适用证据码
PS4、PM6、PP2、PP5、BP1、BP2、BP3、BP6
### 附件关键数据

#### PP3 REVEL评分详细说明（PAH PP3 REVEL data explanation）

**PAH变异REVEL评分分布：**

| REVEL评分范围 | 变异数量 | 分类分布 |
|-------------|---------|---------|
| ≥0.932 | 151个 | 32 P, 70 LP, 49 VUS |
| 0.773-0.932 | 91个 | 26 P, 41 LP, 24 VUS |
| 0.644-0.773 | 30个 | 2 P, 12 LP, 16 VUS（仅5个应用PP3） |
| <0.644 | 30个 | 8 P, 7 LP, 14 VUS, 1 LB（仅2个应用PP3） |

**PP3应用建议：**
- REVEL ≥0.932：强烈建议应用PP3_Strong
- REVEL 0.773-0.932：建议应用PP3_Moderate
- REVEL 0.644-0.773：谨慎应用PP3，需结合其他证据
- REVEL <0.644：通常不应用PP3

#### PS3功能检测数据（PAH PS3 functional data）

**已批准的功能检测方法：**

| 检测方法 | PMID | 建议强度 |
|---------|------|---------|
| 重组PAH在大肠杆菌中表达，测定苯丙氨酸羟化为酪氨酸的酶活性 | 18477464 | PS3_Supporting |
| 位点定向突变分析（如Y179F、Y179A） | 14999516 | PS3_Supporting |
| 人PAH cDNA突变体构建与酶动力学分析 | 15917086 | PS3_Supporting |
| 大鼠PAH活性位点残基突变分析 | 12733906 | PS3_Supporting |
| PKU诱导突变体（Arg158Gln、Glu280Lys）功能分析 | 11368310 | PS3_Supporting |

**关键PAH变异功能数据阈值：**
- PS3_Strong：PAH酶活性 <10% WT
- PS3_Moderate：PAH酶活性 10-25% WT
- PS3_Supporting：PAH酶活性 25-50% WT
- BS3_Strong：PAH酶活性 >85% WT

**重要功能域残基：**
- 活性位点残基：Tyr138, Arg158, Val245, Tyr268, Thr278, Pro279, Glu289, Ala300, Asp315, Phe331, Ala345, Gly346, Ser349, Tyr377
- 底物结合残基：46-48, 63-69
- 辅因子结合残基：His285, His290, Glu330, 246-266, 280-283, 322-326, 377-379

### 参考附件
- [PAH PP3 REVEL data explanation](https://cspec.genome.network/cspec/File/id/592db732-b7ba-451e-9320-8078c8a9bb4c/data)
- [PAH PVS1 decision tree](https://cspec.genome.network/cspec/File/id/a59fd1a9-7a6b-40ec-992f-1151eeb355e9/data)
- [PAH PP3 REVEL data explanation](https://cspec.genome.network/cspec/File/id/65746927-3763-43ce-8e46-1bac2ff242d0/data)
- [PAH PS3 functional data](https://cspec.genome.network/cspec/File/id/6af2ba64-e4b4-4415-9051-9ea9575cab33/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN006)

# ClinGen VCEP基因特异性规范：ADA

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN114 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0007064**（遗传方式：Autosomal recessive inheritance）

### 通用说明
> 官网版本：Version 2.2（Released 7/17/2026；DOI 10.5281/zenodo.21434426；SCID VCEP）。
> Release Notes（v2.2 关键变更）：
> - 重写组合规则，新增 1 Very Strong + 1 Supporting = Likely Pathogenic，以及 1 Strong Benign = Likely Benign。
> - 删除 PS3 关于"须有≥1先证者"方可在细胞模型/体外研究基础上适用 PS3 的前置要求。
> - 新增 BS2_Strong 强度，并补充适用各强度所需的纯合子计数。
> - 将 BS3 改为不适用（Not Applicable），并补充理由。
> - PM1 转为适用（Strong/Moderate/Supporting），均带"变异不得满足 BS1/BS2/BA1"限定。

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)).
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 12, or variants in the last 50 nucleotides of the penultimate exon after c.1028, codon 343, in exon 11), at least one pathogenic variant **must be** present downstream in order to apply PVS1\_Strong.
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 12, or variants in the last 50 nucleotides of the penultimate exon after c.1028, codon 343, in exon 11), when at least one pathogenic variant is **not** present downstream downgrade to PVS1\_Moderate.
- **Supporting** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T.

Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for _ADA._
- **Moderate** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T

Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for _ADA._

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：PS3 may potentially be applied at the default strength level of Strong for evidence from an animal model expressing the variant of interest and recapitulating the ADA-SCID phenotype.
- **Moderate** ✅：The strength of evidence from cellular models/_in vitro_ studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): 

*   PS3\_Moderate: ≤0.05% of wild-type activity (group I)

- **Supporting** ✅：The strength of evidence from cellular models/_in vitro_ studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612):

*   PS3\_Supporting: 0.06-0.6% of wild-type activity (groups II and III)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **VCEP限定**：变异不得满足 BS1、BS2 或 BA1 标准方可适用本码。
- **Strong** ✅：适用上述 ACMG PM1 定义；变异不得满足 BS1、BS2 或 BA1 标准。
- **Moderate** ✅：适用上述 ACMG PM1 定义；变异不得满足 BS1、BS2 或 BA1 标准。
- **Supporting** ✅：适用上述 ACMG PM1 定义；变异不得满足 BS1、BS2 或 BA1 标准。

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD popmax filtering allele frequency  \<0.0001742

*   An additional requirement is that **no homozygotes** have been observed in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _ADA._
- **Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _ADA._
- **Moderate** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _ADA._
- **Supporting** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _ADA._

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing.
- **Supporting** ✅：When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5\_Strong should be downgraded to PM5\_Moderate if PVS1 is applied at any strength. 

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.
- **Moderate** ✅：Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5\_Supporting if previously established variant is classified as likely pathogenic.   
PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5\_Moderate may not be combined with PVS1\_VeryStrong (should be downgraded to PM5\_Supporting if PVS1\_VeryStrong is applied).

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.
- **Supporting** ✅：Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5\_Supporting if previously established variant is classified as likely pathogenic. Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

**Notes**: The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet “+1 pathogenic variant downstream” on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2\_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria (see instructions below).

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations.
- **Moderate** ✅：Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations.
- **Supporting** ✅：Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score greater than or equal to 0.2.
*   **Do not apply to missense variants.**

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：A patient score of ≥ 6 points<sup>1</sup>. 

<sup>1</sup>CNV (Copy number variation) testing is required to consider PP4\_Strong in order to certify that the variant in question is the causative for the phenotype and not one CNV event corrected by gene therapy and not identified previously (see instructions below).
- **Moderate** ✅：A patient score of 2-\<6 points (see instructions below).
- **Supporting** ✅：A patient score of 1-\<2 points (see instructions below).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD popmax filtering allele frequency >0.00721.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD popmax filtering allele frequency >0.00161<sup>1</sup>

<sup>1</sup> Consider also bottleneck populations.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2_Strong: Can be applied at Strong level if observed in at least 3 homozygotes.
- **Supporting** ✅：Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote.

> ⚠️ 官网自身矛盾（2026-10-09 核验）：本码在 cspec 页面同时存在可见 Strong/Supporting 强度文本（如上，且 v2.2 release notes 明确新增 BS2_Strong 与纯合子计数）与 hidden 注释 "NA-NOTE(hidden): Does not apply due to reduced penetrance."。按"可见内容 + release notes 为有效规则"原则转录可见文本，hidden 注释为平台录入残留，仅供参考。

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **不适用（Not Applicable）** ✅：v2.2 起 BS3 改为不适用。
  - 理由：目前没有可靠的功能研究能够排除所有对蛋白功能的破坏效应。SCID VCEP 于 2025-12-19 会议讨论将 BS3 改为不适用：原 BS3_Supporting 基于"表达的 ADA 酶活性 ≥4.8% 野生型活性（group IV）"，但自 1998 年那篇文献后已有更多发表数据；Hershfield 博士 2024 年发表的新数据显示 group IV 活性范围一直延伸至野生型的 94.9%（Table 2）。该码此前仅应用于 3 个变异（仅 1 个已发表），且不会改变分类。已于 2025-12-19 经专家/遗传学家批准。

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Can be applied without additional specifications.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：*   Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions.
*   The variant should be predicted not to impact splicing by at least two out of three _in silico_ tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK).
*   Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7.

### 组合规则（Rules for Combining Criteria；官网 v2.2，Richards 2015 组合规则面板）

**Pathogenic（致病）**
1. 1 Very Strong AND ≥ 1 Strong
2. 1 Very Strong AND ≥ 2 Moderate
3. 1 Very Strong AND 1 Moderate AND 1 Supporting
4. 1 Very Strong AND ≥ 2 Supporting
5. ≥ 2 Strong
6. 1 Strong AND ≥ 3 Moderate
7. 1 Strong AND 2 Moderate AND ≥ 2 Supporting
8. 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**Likely Pathogenic（可能致病）**
1. 1 Very Strong AND 1 Moderate
2. 1 Strong AND 1 Moderate
3. 1 Strong AND ≥ 2 Supporting
4. ≥ 3 Moderate
5. 2 Moderate AND ≥ 2 Supporting
6. 1 Moderate AND ≥ 4 Supporting
7. 1 Strong AND 2 Moderate
8. 1 Very Strong AND 1 Supporting

**Benign（良性）**
1. ≥ 2 Strong
2. 1 Stand Alone

**Likely Benign（可能良性）**
1. ≥ 2 Supporting
2. 1 Strong

### 不适用证据码
PS4、PP2、PP5、BS3（v2.2 起改为不适用）、BP1、BP2、BP3、BP4、BP5、BP6
### 参考附件
- [SCID VCEP PS3_BS3 Functional Evidence (ADA)](https://cspec.genome.network/cspec/File/id/d557f242-8b30-4c26-a23a-8f7f18f3ceb0/data)
- [svi-proposal-for-pm3-criterion-version1](https://cspec.genome.network/cspec/File/id/b817332d-55d6-4812-ba7c-13ac315001b1/data)
- [PP4 - ADA](https://cspec.genome.network/cspec/File/id/be5b7fb6-d184-4efe-93f1-fda47a0dd57d/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN114)

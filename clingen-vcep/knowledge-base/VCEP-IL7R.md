# ClinGen VCEP基因特异性规范：IL7R

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.2（2026-06-01，SCID VCEP；v2.2 更新组合规则：新增 1 Very Strong + 1 Supporting = Likely Pathogenic，及 1 Strong Benign = Likely Benign）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN119 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0012163**（遗传方式：Autosomal recessive inheritance）

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
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), at least one pathogenic variant **must be** present downstream in order to apply PVS1\_Strong.
*   PVS1\_Strong can be applied to variants not predicted to undergo nonsense-mediated decay but causing truncation of the transmembrane domain (which begins at amino acid 240) or any distal region (i.e. cytoplasmatic domain).
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), when at least one pathogenic variant is **not** present downstream downgrade to PVS1\_Moderate.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T.

Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for _IL7R._
- **Moderate** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T

Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for _IL7R._

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
- **Strong** ✅：PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL7R-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
- **Supporting** ✅：PS3\_Supporting can be applied based on an abnormal result in **at least** **one** approved _in vitro_ assay (IL-7-induced Jak3 phosphorylation assay, IL-7 binding assay, IL-7-induced STAT5 DNA binding/transcriptional induction).

*   Approved assay instances:
    *   IL-7-induced Jak3 phosphorylation assay
        *   Roifman et al., 2000 (PMID: 11023514)
    *   IL-7 binding assay
        *   Puel et al., 1998 (PMID: 9843216)
    *   IL-7-induced STAT5 DNA binding/transcriptional induction
        *   Puel et al., 1998 (PMID: 9843216)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** ✅：Caveat: variant must not meet BS1, BS2, BA1 criteria
- **Moderate** ✅：Caveat: variant must not meet BS1, BS2, BA1 criteria
- **Supporting** ✅：Caveat: variant must not meet BS1, BS2, BA1 criteria

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：gnomAD popmax filtering allele frequency \<0.00004129.

*   An additional requirement is that **no homozygotes** have been observed in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _IL7R._
- **Strong** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _IL7R._
- **Moderate** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _IL7R._
- **Supporting** ✅：Use ClinGen SVI adapted recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for _IL7R._

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

<sup>1</sup>CNV (Copy number variation) testing is required if PP4\_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified  (see instructions below).
- **Moderate** ✅：A patient score of 2-\<6 points (see instructions below).
- **Supporting** ✅：A patient score of 1-\<2 points (see instructions below).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD popmax filtering allele frequency >0.00566.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD popmax filtering allele frequency >0.00126<sup>1</sup>

<sup>1</sup>Consider also bottleneck populations.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2\_Strong: Can be applied at Strong level if observed in at least 3 homozygotes.
- **Supporting** ✅：Only to be used when the variant is observed in the homozygous state in a healthy adult.

BS2\_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote.

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
*   Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7.

### Rules for Combining Criteria

> 证据码强度集合：
> - Very Strong = (PVS1, PS2_Very Strong, PM3_Very Strong)
> - Strong = (PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)
> - Moderate = (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)
> - Supporting = (PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)

#### Pathogenic
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

#### Likely Pathogenic
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate
- 1 Very Strong AND 1 Supporting

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- ≥ 2 Supporting (BS2_Supporting, BP7)
- 1 Strong (BS1, BS2, BS4)

### 不适用证据码
PS4、PP2、PP5、BS3、BP1、BP2、BP3、BP4、BP5、BP6
### 参考附件
- [PM3 Criterion](https://cspec.genome.network/cspec/File/id/cb8794b9-bfc8-4e3d-8741-cc8fd873e5b9/data)
- [PP4 - IL7R](https://cspec.genome.network/cspec/File/id/1fbda9df-ac24-4958-a8a2-def5c0250923/data)
- [SCID VCEP PS3_BS3 Functional Evidence (IL7R)](https://cspec.genome.network/cspec/File/id/d5d9b2fb-ad4a-43e5-ae84-b7f41abe787b/data)
- [PM3 Minor Amendments 12.12.2025](https://cspec.genome.network/cspec/File/id/e4343a22-1571-4a7b-9572-1e84099a1149/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN119)

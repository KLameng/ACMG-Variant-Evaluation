# ClinGen VCEP基因特异性规范：IL2RG

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v2.2（2026-06-01，SCID VCEP；v2.2 更新组合规则：新增 1 Very Strong + 1 Supporting = Likely Pathogenic，及 1 Strong Benign = Likely Benign）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN129 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010315**（遗传方式：X-linked inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   PVS1 at default strength (Very Strong) can be applied to variants not predicted to undergo nonsense-mediated decay but truncating the transmembrane domain (which begins at amino acid 255) or any distal region (i.e. cytoplasmic domain) due to the lack of functionality of the protein expressed with this defect.
- **Strong** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), at least one pathogenic variant **must be** present downstream in order to apply PVS1\_Strong
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), when at least one pathogenic variant is **not** present downstream downgrade to PVS1\_Moderate.
- **Supporting** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042))

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Strength modification depending upon classification of previously established variant (pathogenic vs. likely pathogenic).

Previously established variant must be classified using the SCID VCEP specifications for _IL2RG._
- **Moderate** ✅：Strength modification depending upon classification of previously established variant (pathogenic vs. likely pathogenic).

Previously established variant must be classified using the SCID VCEP specifications for _IL2RG._

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL2RG-SCID phenotype.
- **Supporting** ✅：Strength modification based on an abnormal result in **at least** one approved _in vitro_ assay.

*   Approved assay instances:
    *   Phosphorylation of JAK3/Co-Immunoprecipitation with JAK3 
        *   Sharfe et al., 1997 (PMID: 9399950)
        *   Kumaki et al., 1999 (PMID: 9933465) 
        *   Arcas-García et al., 2020 (PMID: 31799703)
    *   Cytokine binding
        *   Sharfe et al., 1997 (PMID: 9399950) 
        *   Kumaki et al., 1995 (PMID: 7632950)
    *   Surface expression of the gamma chain
        *   Kumaki et al., 1995 (PMID: 7632950)
    *   Interaction profiling-BioID
        *   Tuovinen et al., 2020 (PMID: 32072341)

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Sum of case scores >16 points (see instructions below)
- **Strong** ✅：Sum of case scores 4.5-16 points (see instructions below)
- **Moderate** ✅：Sum of case scores 2.5-4 points (see instructions below)
- **Supporting** ✅：Sum of case scores 1-2 points (see instructions below)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** ✅：Defined to include IL2RG-specific hot spots and functional domains.

Caveat: Variant must not meet BS1, BS2, or BA1 criteria.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Strength modification based on an abnormal result in at least one approved _in vitro_ assay.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Additional requirement that deletion variants must contain a known **pathogenic variant, likely pathogenic variant, or variant of uncertain significance** that is not predicted/observed to alter splicing in order to apply PM4, with the strength of evidence dependent upon the classification of the variant contained within the deletion.
- **Supporting** ✅：Additional requirement that deletion variants must contain a known **pathogenic variant, likely pathogenic variant, or variant of uncertain significance** that is not predicted/observed to alter splicing in order to apply PM4, with the strength of evidence dependent upon the classification of the variant contained within the deletion.

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
- **Strong** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.
- **Moderate** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.
- **Supporting** ✅：Use ClinGen SVI recommendations for _de novo_ criteria ([https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf](https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf)).

Phenotypic consistency determined using points-based system defined in PP4.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386), with strength dependent on number of affected segregations (see list below).
- **Moderate** ✅：Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386), with strength dependent on number of affected segregations (see list below).
- **Supporting** ✅：Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386), with strength dependent on number of affected segregations (see list below).

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score greater than or equal to 0.2.

*   **Do not apply to missense variants.**

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：A patient score of ≥ 6 points<sup>1</sup>. 

<sup>1</sup>CNV (Copy number variation) testing is required if PP4\_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified  (see instructions below).
- **Moderate** ✅：A patient score of ≥2.5-\<6 points (see instructions below).
- **Supporting** ✅：A patient score of 1-\<2.5 points (see instructions below).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD popmax filtering allele frequency >0.01110.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD popmax filtering allele frequency >0.00249<sup>1</sup>

<sup>1</sup> Consider bottleneck populations

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2\_Strong: Observed in >=3 (3 or more) hemizygotes in gnomAD.
- **Supporting** ✅：BS2\_Supporting: Can be applied at Supporting level of evidence if observed at least 2 hemizygotes in gnomAD.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Can be applied without additional specifications.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：*   Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions.
*   Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7.

### Rules for Combining Criteria

> 证据码强度集合：
> - Very Strong = (PVS1, PS2_Very Strong, PS4_Very Strong)
> - Strong = (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)
> - Moderate = (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)
> - Supporting = (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)

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
PM3、PP2、PP5、BS3、BP1、BP2、BP3、BP4、BP5、BP6
### 参考附件
- [PP4 - IL2RG](https://cspec.genome.network/cspec/File/id/5a0be3cc-45c8-4bd4-a9e1-1c0da0fdb831/data)
- [PVS1](https://cspec.genome.network/cspec/File/id/2a57fcfe-56cf-4eb3-a7d3-756f687e55fb/data)
- [PS2_PM6](https://cspec.genome.network/cspec/File/id/a4613b28-7451-4d8f-a9f7-7504e2f5c068/data)
- [PP1](https://cspec.genome.network/cspec/File/id/e4c50ea3-5c1f-45c3-8093-7a94b6e05a89/data)
- [SCID VCEP PS3_BS3 Functional Evidence](https://cspec.genome.network/cspec/File/id/1b8442ef-ced4-47d6-92bd-acc8287e261c/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN129)

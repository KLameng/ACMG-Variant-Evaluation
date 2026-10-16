# ClinGen VCEP基因特异性规范：KCNQ1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN112 — Potassium Channel Arrhythmia Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100316**（遗传方式：Autosomal dominant inheritance；Autosomal recessive inheritance）

### 通用说明
Long QT syndrome 1 and Jervell and Lange-Nielsen syndrome are both caused by loss-of-function variants in KCNQ1. As a result, families with homozygous or compound heterozygous individuals affected with Jervell and Lange-Nielsen syndrome can also have heterozygous family members with long QT syndrome. It is important to note that not all disease-causing variants in KCNQ1 are highly penetrant in the heterozygous state, so it is common to see incomplete penetrance among heterozygous family members. For most KCNQ1 variant curations, a pathogenic or likely pathogenic classification is equally applicable to both inheritance patterns. On the other hand, a number of hypomorphic KCNQ1 variants that cause Jervell and Lange-Nielsen syndrome (or QTc interval prolongation without hearing loss) in homozygosity or compound heterozygosity are not sufficient to cause long QT syndrome in the heterozygous state. For variants that fit this pattern, the VCEP adds a note to the evidence summary to clarify that the variant has only been observed to cause disease in the homozygous or compound heterozygous state.

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：For truncating variants, apply PVS1 at default (VeryStrong) level if the variant affects codons 1-581, since nonsense-mediated decay is predicted.

[https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1](https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1)
- **Moderate** ✅：Apply PVS1\_Moderate for truncating variants between codons 582 and 620, for which nonsense-mediated decay is not predicted. This region includes the subunits assembly domain (SAD) between residues 589-620, which mediates tetramerization, so that truncating variants that remove this region are reportedly unable to assemble and are disease-causing (PMID: 10654932).

[https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1](https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1)
- **Supporting** ✅：Apply PVS1\_Supporting for truncating variants between codons 621 and 676, for which nonsense-mediated decay is not predicted, and the SAD is retained. As a result, these distal variants may still yield functional channels. Please note that although one variant with good evidence of pathogenicity has been found within this region, (NM\_000218.3(KCNQ1):c.1893del (p.Arg632fs)) it appears to exert a pathogenic effect through a dominant negative (mistrafficking) mechanism rather than true null mechanism (PMID: 22739119).

[https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1](https://docs.google.com/presentation/d/1-Dz9jmvebv1z1QoSBdON3vbbNaH-V2-v/edit#slide=id.p1)

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

*   The comparison variant must reach a pathogenic classification using these rule specifications, and must have reached pathogenic without the use of the PS1 code.
*   SpliceAI must be used to ensure that the comparison variant is not causing a splicing defect.
- **Moderate** ✅：*   PS1 is met at the PS1\_Moderate level if the comparison variant reaches a likely pathogenic classification using these rule specifications, without the use of the PS1 code.
*   This code can also be met at the PS1\_Moderate level when the corresponding variant in the paralogous KCNQ2 gene meets criteria to be classified as Pathogenic by the KCNQ Channel Brain Disorders Variant Curation Expert Panel specifications. Curators should access paralogue data and regions of alignment and non-alignment between KCNQ1 and KCNQ2 at the site below: [https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1.](https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1.)
*   The corresponding variant in the paralogous gene must substitute the same amino acid as the variant being considered, not a different amino acid.
*   An example is that the NM\_000218.3(KCNQ1):c.430A>G (p.Thr144Ala) has a paralogous variant in NM\_172107.4(KCNQ2):c.340A>G (p.Thr114Ala). If the latter variant in _KCNQ2_ is classified Pathogenic in the future by the KCNQ Channel Brain Disorders Variant Curation Expert Panel specifications, the paralogous p.Thr144Ala variant in _KCNQ1_ will meet PS1\_Moderate.
*   The paralogous variant must have reached Pathogenic classification without the use of the PS1 code.
*   While this paralogue-based strategy has been approved for _KCNQ2_ only, this criterion may eventually apply to the _KCNQ3_, _KCNQ4_, and _KCNQ5_ genes too, following future specifications and variant classifications by the KCNQ Channel Brain Disorders Variant Curation Expert Panel.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：_De novo_ (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

*   For PS2, both maternity and paternity must be confirmed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years). Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, _etc._ can contribute to non-maternity. Cases and parents genotyped by trio whole exome sequencing are considered to have confirmed maternity and paternity.
*   The _de novo_ variant in question must be coding or flanking.
*   The PS2 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).![](https://lh6.googleusercontent.com/4dOzwji0rs6_gSczQOWVPcEOk-W6h4Ey-wBCZTtqRdLJizyKdB6AU08BvSlBsOQ0HOkPeRFn1xEL6ofBU7fc1B0awCfBVfKQYdboYFwdPZmyf1zH0vBaH4AE-eenxPhcIlpuAXes9kp9vlJQ9f-kcA)
- **Strong** ✅：_De novo_ (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

*   For PS2, both maternity and paternity must be confirmed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years). Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, _etc._ can contribute to non-maternity. Cases and parents genotyped by trio whole exome sequencing are considered to have confirmed maternity and paternity.
*   The _de novo_ variant in question must be coding or flanking.
*   The PS2 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).
- **Moderate** ✅：_De novo_ (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

*   For PS2, both maternity and paternity must be confirmed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years). Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, _etc._ can contribute to non-maternity. Cases and parents genotyped by trio whole exome sequencing are considered to have confirmed maternity and paternity.
*   The _de novo_ variant in question must be coding or flanking.
*   The PS2 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).
- **Supporting** ✅：_De novo_ (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

*   For PS2, both maternity and paternity must be confirmed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years). Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, _etc._ can contribute to non-maternity. Cases and parents genotyped by trio whole exome sequencing are considered to have confirmed maternity and paternity.
*   The _de novo_ variant in question must be coding or flanking.
*   The PS2 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1](https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet PS3 if the variant is co-expressed with KCNE1 and the current magnitude is outside the normal range defined by the paper and is statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for PS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for PS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)
- **Moderate** ✅：Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1](https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet PS3 if the variant is co-expressed with KCNE1 and the current magnitude is outside the normal range defined by the paper and is statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for PS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for PS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)
- **Supporting** ✅：Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1](https://docs.google.com/presentation/d/1YA_82T8orad_nAy_fjapiFFz3ZSITVwZ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet PS3 if the variant is co-expressed with KCNE1 and the current magnitude is outside the normal range defined by the paper and is statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for PS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for PS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls

*   In order to be evaluated for this criterion, the variant must not meet BS1.
*   PS4 is Met by 6 or more probands.
*   This code is not considered mutually exclusive with PM3. For example, variants associated with both dominant and recessive cases can meet both PS4 and PM3.
*   If probands are reported in at least 2 papers, and the author lists from the two papers contain any of the same authors names, definitely the patients are the same, so count only one case for PS4.
*   If the two lists of authors are totally distinct / different, usually you can count both cases for PS4.
*   Patients reported as affected must have QTc measurement greater than or equal to 460ms in order to be counted. Diagnosis of long QT syndrome by itself is not sufficient for inclusion.
- **Moderate** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls

*   In order to be evaluated for this criterion, the variant must not meet BS1.
*   PS4\_moderate is Met by 3-5 probands.
*   This code is not considered mutually exclusive with PM3. For example, variants associated with both dominant and recessive cases can meet both PS4 and PM3.
*   If probands are reported in at least 2 papers, and the author lists from the two papers contain any of the same authors names, definitely the patients are the same, so count only one case for PS4.
*   If the two lists of authors are totally distinct / different, usually you can count both cases for PS4.
*   Patients reported as affected must have QTc measurement greater than or equal to 460ms in order to be counted. Diagnosis of long QT syndrome by itself is not sufficient for inclusion.
- **Supporting** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls

*   In order to be evaluated for this criterion, the variant must not meet BS1.
*   PS4\_supporting is Met by 2 independent observations of the variant in probands.
*   This code is not considered mutually exclusive with PM3. For example, variants associated with both dominant and recessive cases can meet both PS4 and PM3.
*   If probands are reported in at least 2 papers, and the author lists from the two papers contain any of the same authors names, definitely the patients are the same, so count only one case for PS4.
*   If the two lists of authors are totally distinct / different, usually you can count both cases for PS4.
*   Patients reported as affected must have QTc measurement greater than or equal to 460ms in order to be counted. Diagnosis of long QT syndrome by itself is not sufficient for inclusion.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain (_e.g._ active site of an enzyme) without benign variation 

*   The variant must be rare (meeting PM2\_Supporting) in order to be considered for PM1.
*   Met by a rare variant within the pore helix (amino acids 300 to 320). This region is known to be a critical region of KCNQ1 and has been confirmed to show an absence of likely benign or benign variants listed in gnomAD.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

*   Supporting level only
*   Maximum allele frequency in gnomAD (in one of the 5 continental populations; African/African-American, East Asian, European non-Finnish, Latino/Admixed-American, or South Asian) \<0.00001 (0.001%)

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：For recessive disorders, detected in _trans_ with a pathogenic variant  Note: This requires testing of parents (or offspring) to determine phase

*   Can be used for variants seen in patients with Jervell and Lange-Nielsen syndrome, if the phenotype includes both long QT interval and congenital deafness.
*   This code is not considered mutually exclusive with PS4. For example, variants associated with both recessive and dominant cases can meet both PM3 and PS4.
*   Use the ClinGen SVI recommendations to determine evidence weight for this rule code.
*   Both variants must be classified using these rule specifications.

![](https://lh6.googleusercontent.com/k8TLTROZpnhrx_KFdTguCHToaXwLEnf9Kn9MqXkNr-AdlbStJ_8aGhhXI2u2CZhCuDWJY0FrfVsfOmSdd5Wu8rfHx7gxvGoj7u_j8uqLzURiWrcj8OZOZipYCcQfCkeZCWcJIsqtKnY8)
- **Strong** ✅：For recessive disorders, detected in _trans_ with a pathogenic variant  Note: This requires testing of parents (or offspring) to determine phase

*   Can be used for variants seen in patients with Jervell and Lange-Nielsen syndrome, if the phenotype includes both long QT interval and congenital deafness.
*   This code is not considered mutually exclusive with PS4. For example, variants associated with both recessive and dominant cases can meet both PM3 and PS4.
*   Use the ClinGen SVI recommendations to determine evidence weight for this rule code.
*   Both variants must be classified using these rule specifications.
- **Moderate** ✅：For recessive disorders, detected in _trans_ with a pathogenic variant  Note: This requires testing of parents (or offspring) to determine phase

*   Can be used for variants seen in patients with Jervell and Lange-Nielsen syndrome, if the phenotype includes both long QT interval and congenital deafness.
*   This code is not considered mutually exclusive with PS4. For example, variants associated with both recessive and dominant cases can meet both PM3 and PS4.
*   Use the ClinGen SVI recommendations to determine evidence weight for this rule code.
*   Both variants must be classified using these rule specifications.
- **Supporting** ✅：For recessive disorders, detected in _trans_ with a pathogenic variant  Note: This requires testing of parents (or offspring) to determine phase

*   Can be used for variants seen in patients with Jervell and Lange-Nielsen syndrome, if the phenotype includes both long QT interval and congenital deafness.
*   This code is not considered mutually exclusive with PS4. For example, variants associated with both recessive and dominant cases can meet both PM3 and PS4.
*   Use the ClinGen SVI recommendations to determine evidence weight for this rule code.
*   Both variants must be classified using these rule specifications.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants

*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data) but can be used together with PM1.
*   In-frame insertions or deletions of any size will meet PM4 at the moderate (default) level, due to the greater importance of the location of the variant rather than the size.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   Caveat: Residue must be highly conserved across all 5 human KCNQ paralogues in order to be considered for PM5. To confirm conservation, curators should access paralogue data and regions of alignment and non-alignment between KCNQ1 and KCNQ2, KCNQ3, KCNQ4, and KCNQ5  at the site below: [https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1](https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1).
*   Poor conservation (ineligibility for PM5) is defined whenever 1 or more KCNQ’s show a different amino acid at the position. 
*   Comparison variants must have a Pathogenic or Likely Pathogenic classification reached using these VCEP-specified rules without using PM5.
*   Variants at any codon where a likely benign / benign variant has been classified by the group are not eligible for PM5.
*   SpliceAI must be used to examine both variants for similar predicted effect or lack of effect on splicing (SpliceAI Δ score \<0.2).
*   Not used at the PM5\_Strong level.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：Assumed de novo, but without confirmation of paternity and maternity.

*   For PM6, maternity and paternity are not confirmed but assumed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years).
*   The _de novo_ variant in question must be coding or flanking.
*   The PM6 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).![](https://lh6.googleusercontent.com/4dOzwji0rs6_gSczQOWVPcEOk-W6h4Ey-wBCZTtqRdLJizyKdB6AU08BvSlBsOQ0HOkPeRFn1xEL6ofBU7fc1B0awCfBVfKQYdboYFwdPZmyf1zH0vBaH4AE-eenxPhcIlpuAXes9kp9vlJQ9f-kcA)
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.

*   For PM6, maternity and paternity are not confirmed but assumed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years).
*   The _de novo_ variant in question must be coding or flanking.
*   The PM6 strength level depends on the clinical phenotype specificity and number of probands as defined in Tables 1 and 2.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).![](https://lh6.googleusercontent.com/4dOzwji0rs6_gSczQOWVPcEOk-W6h4Ey-wBCZTtqRdLJizyKdB6AU08BvSlBsOQ0HOkPeRFn1xEL6ofBU7fc1B0awCfBVfKQYdboYFwdPZmyf1zH0vBaH4AE-eenxPhcIlpuAXes9kp9vlJQ9f-kcA)
- **Supporting** ✅：Assumed de novo, but without confirmation of paternity and maternity.

*   For PM6, maternity and paternity are not confirmed but assumed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years).
*   The _de novo_ variant in question must be coding or flanking.
*   The PM6 strength level depends on the clinical phenotype specificity and number of probands as defined in Table 1.
*   When using Table 1 to find the number of points per proband, if the proband has a phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), the row used should usually be "phenotype consistent with gene but not highly specific". During the pilot phase, curators should also note the genotyping method and whether comprehensive testing of all/other LQTS genes has been performed.
*   When using Table 1 to find the number of points per proband, if the proband meets PP4, so that the phenotype is sufficient to diagnose \_KCNQ1\_-specific LQTS (LQT 1), the number of points corresponding to "phenotype highly specific for gene" should be used instead. Note: This would require QTc prolongation above 480ms AND either swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844).![](https://lh6.googleusercontent.com/4dOzwji0rs6_gSczQOWVPcEOk-W6h4Ey-wBCZTtqRdLJizyKdB6AU08BvSlBsOQ0HOkPeRFn1xEL6ofBU7fc1B0awCfBVfKQYdboYFwdPZmyf1zH0vBaH4AE-eenxPhcIlpuAXes9kp9vlJQ9f-kcA)

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease  

*   Each affected family member must have Schwartz score (PMID: 36017572, Table 10) >3 or QTc greater than or equal to 480ms or syncope in order to be included / counted.
*   The proband + 7 affected family members with the variant meets PP1\_Strong.
*   The numbers above have been informed by PMID: 27236918.
*   If any family member is affected but does not harbor the variant, use BS4 (non-segregation) instead.
- **Moderate** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease  

*   Each affected family member must have Schwartz score (PMID: 36017572, Table 10) >3 or QTc greater than or equal to 480ms or syncope in order to be included / counted.
*   The proband + 5 affected family members with the variant meets PP1\_Moderate.
*   The numbers above have been informed by PMID: 27236918.
*   If any family member is affected but does not harbor the variant, use BS4 (non-segregation) instead.
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease  

*   Each affected family member must have Schwartz score (PMID: 36017572, Table 10) >3 or QTc greater than or equal to 480ms or syncope in order to be included / counted.
*   The proband + 3 affected family members with the variant meets PP1.
*   The numbers above have been informed by PMID: 27236918.
*   If any family member is affected but does not harbor the variant, use BS4 (non-segregation) instead.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease 

*   Not applicable due to presence of benign variation throughout the _KCNQ1_ gene (since the missense constraint Z-score in gnomAD is 1.83, lower than 3).

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc)

*   REVEL and SpliceAI are the preferred predictors
*   Apply this code if REVEL score is greater than or equal to 0.75.
*   Use SpliceAI to look for a possible splicing defect. Apply this code if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is greater than or equal to 0.2 (PMID: 37352859).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

*   QT prolongation above 480ms AND
*   Swimming-associated events OR
*   Treadmill stress test result (PMID: 21699858) OR
*   T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

*   Maximum allele frequency in gnomAD (in one of the 5 continental populations; African/African-American, East Asian, European non-Finnish, Latino/Admixed-American, or South Asian) greater than or equal to 0.004 (0.4%).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is greater than expected for disorder  

*   Maximum allele frequency in gnomAD (in one of the 5 continental populations; African/African-American, East Asian, European non-Finnish, Latino/Admixed-American, or South Asian) greater than or equal to 0.0004 (0.04%).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

*   Not applicable due to incomplete penetrance.
*   Please note that hearing loss and other phenotypes are not completely penetrant in homozygotes (PMID: 23392653, [https://www.ncbi.nlm.nih.gov/books/NBK1405/#jln.Summary](https://www.ncbi.nlm.nih.gov/books/NBK1405/#jln.Summary)).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established _in vitro_ or _in vivo_ functional studies show no damaging effect on protein function or splicing.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1](https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet BS3 if the variant is co-expressed with KCNE1 and if the variant current magnitude is within the normal range defined by the paper and is NOT statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for BS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for BS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)
- **Moderate** ✅：Well-established _in vitro_ or _in vivo_ functional studies show no damaging effect on protein function or splicing.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1](https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet BS3 if the variant is co-expressed with KCNE1 and if the variant current magnitude is within the normal range defined by the paper and is NOT statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for BS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for BS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)
- **Supporting** ✅：Well-established _in vitro_ or _in vivo_ functional studies show no damaging effect on protein function or splicing.

Please refer to the linked table below for strength level specifications:

[https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1](https://docs.google.com/presentation/d/1cdlToGFzYGRbyaTmseiIDQx9AlCKNPfJ/edit#slide=id.p1)

Caveats:

1.  Conflicting evidence from different papers - no points
2.  Same types of evidence (e.g RNA and Protein Metabolism) coming from the same paper - count 1
3.  No more than 2 pieces of evidence can be counted from the same paper
4.  Same finding in 2 papers from the same group – count 1
5.  Electrophysiology result can only meet BS3 if the variant is co-expressed with KCNE1 and if the variant current magnitude is within the normal range defined by the paper and is NOT statistically significantly different from the normal control.
6.  Please count Experimental / Structural / Functional Simulation (PMID: 29021305) only when the results align with a electrophysiology experiment.

Electrophysiology and Experimental / Structural / Functional Simulation assays approved by the VCEP for BS3 are:

(1) Manual patch-clamp (e.g. PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)

(2) Automated patch-clamp (e.g. PMID: 30571187)

(3) Microelectrode array analysis of hIPSC-cardiomyocytes (e.g. PMID: 35765105) 

(4) Experimental / Structural / Functional Simulation (e.g. PMIDs: 29021305, 35442947, 32096762)

RNA or Protein Metabolism assays approved by the VCEP for BS3 are:

(5) Cell Surface Localization by Flow Cytometry (e.g. PMID: 29532034)  

(6) Mislocalization by Immunofluorescence of KCNQ1 (e.g. PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (e.g. PMIDs: 19959132, 30591322)

(7) Total Cell Expression by Flow Cytometry (e.g. PMID: 29532034)

(8) Western Blotting (e.g. PMIDs: 21380488, 19114714)

(9) RNA Metabolism showing partial / incomplete disruption of splicing (e.g. PMIDs: 17292394, 28264985)

*   Functional assays are described at the following link: [https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446](https://docs.google.com/spreadsheets/d/12iWEYVxD5-wMutqqW10u-7RKupCoElij/edit#gid=1933102446)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family 

*   BS4 is met by absence of the variant in 2 or more affected family members
*   The family member must have QTc greater than or equal to 480ms or Schwartz score >3 or syncope.
*   Please use the European Society of Cardiology guidelines for 2022 (PMID: 36017572, Table 10) to calculate a modified Schwartz score.
- **Supporting** ✅：Lack of segregation in affected members of a family

*   BS4\_supporting is met by absence of the variant in 1 affected family member
*   The family member must have QTc greater than or equal to 480ms or Schwartz score >3 or syncope.
*   Please use the European Society of Cardiology guidelines for 2022 (PMID: 36017572, Table 10) to calculate a modified Schwartz score.

#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Supporting** ✅：Missense variant in a gene for which primarily truncating variants are known to cause disease

*   Not applicable, as pathogenic _KCNQ1_ variants are not limited to truncating variants, but can be missense as well.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

*   Not applicable to _KCNQ1_ due to biallelic cases (Jervell and Lange-Nielsen syndrome)

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function

*   Not applicable to _KCNQ1_

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.) 

*   REVEL and SpliceAI are the preferred predictors
*   Apply this code for a missense variant if the REVEL score is \<0.25 AND no splicing defect is predicted according to SpliceAI.
*   Use SpliceAI to look for a possible splicing defect. Apply this code if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is \<0.1 (in addition to REVEL score \<0.25).
*   Apply this code for a synonymous or intronic variant if delta score for donor gain, donor loss, acceptor gain, or acceptor loss is \<0.1 (PMID: 37352859).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease

*   Caveat: BP5 is not applicable when the phenotypes (ie: trigger type; PMID: 32882399, 11136691, 18373596 or treadmill stress test; PMID: 21699858) indicate _KCNQ1_ as the cause. BP5 is only applicable when the phenotypes match another form of LQTS (caused by a variant in _KCNH2_, _SCN5A_, or _KCNE1_, PMID: 19862833, PMID: 31941373, PMID: 33517668) or when phenotype details are not sufficiently specific.
*   Note: The rate of cases with multiple suspected deleterious variants in the same or different LQTS-associated genes may be relatively high (5.2% in one cohort, PMID: 24667783). The group will consider this possibility during the pilot.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

*   Use SpliceAI to look for suspected splicing defects (cutoff Δ score \<0.1).
*   Use PhyloP to check for conservation (cutoff \<2.0).
*   Please note that SpliceAI Δ score \<0.1 AND PhyloP score \<2.0 must both be met.
*   This code can be met by synonymous variants except for variants in the last 3 nucleotides of an exon, or in the 1st nucleotide of an exon.
*   This code can be met by intronic variants except for variants in positions +1 to +6 or -1 to -20, which are considered part of the splice donor and splice acceptor sites (PMID: 37352859).

### 不适用证据码
PP5、BP6
### 参考附件
- [PS3 BS3 functional assays KCNQ1](https://cspec.genome.network/cspec/File/id/665aab55-885d-4224-ae99-5d6e73f2ec83/data)
- [Updated results of KCNQ1 pilot curations](https://cspec.genome.network/cspec/File/id/b3d22c26-a7ce-4342-800b-12e16986751c/data)
- [KCNQ1 Rule Combination Guidance](https://cspec.genome.network/cspec/File/id/41fac7fc-f689-42f5-a119-fa4f3391b1cb/data)
- [KCNQ1 PS3 BS3 strength overview](https://cspec.genome.network/cspec/File/id/a970e710-6faf-430c-b858-2c5a50feb79b/data)
- [KCNQ1 PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/54e8cf5f-6bf6-4cfb-be40-38084043b3f5/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN112)

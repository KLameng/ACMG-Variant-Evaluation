# ClinGen VCEP基因特异性规范：CTLA4

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN122 — Antibody Deficiencies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0014493**（遗传方式：Autosomal dominant inheritance）

### 官网版本
- Version 2.0（Released）
- DOI: 10.5281/zenodo.21723733（https://doi.org/10.5281/zenodo.21723733）
- 核验日期：2026-10-09

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   For truncating variants located in the isoform-specific exon 3, apply PVS1 if nonsense mediated decay is predicted (truncation at codon 172 or lower) and PVS1\_strong if NMD is not predicted (truncation at codon 173 or higher). While this recommendation already matches the SVI guidance, it is specified here because similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452), despite the fact that exon 3 is omitted from an alternative transcript (NM\_001037631.3) that encodes the soluble isoform (PMID: 40168991).
*   If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score greater than or equal to 0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3\_Supporting and evaluate PVS1 instead (PMID: 37352859).
*   In order to avoid over-weighing loss-of-function evidence, PP3 and PS3 are mutually exclusive with PVS1 at the default (very strong) level. These additional codes cannot be applied for a variant that has already met PVS1.
- **Strong** ✅：*   For truncating variants located in the isoform-specific exon 3, apply PVS1 if nonsense mediated decay is predicted (truncation at codon 172 or lower) and PVS1\_strong if NMD is not predicted (truncation at codon 173 or higher). While this recommendation already matches the SVI guidance, it is specified here because similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452), despite the fact that exon 3 is omitted from an alternative transcript (NM\_001037631.3) that encodes the soluble isoform (PMID: 40168991).
- **Moderate** ✅：*   Apply PVS1\_Moderate for nonsense or frameshift variants between codons 202 and 223 of CTLA4, as these are predicted not to undergo nonsense-mediated decay and to result in C-terminal truncation of less than 10% of the protein product.
*   Apply PVS1\_Moderate for initiation codon variants, as there are no known alternative start codons and the closest potential in-frame start codon is at codon 38. There is at least one report of an initiation codon variant that leads to CTLA4 phenotypes and though there is no direct experimental evidence of loss of expression, the authors assert that there is a proximally located N-terminal nonsense variant (34 aa away) that results in no protein product, making it unlikely that there is alternative start codon usage (PMID: 25329329).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Use PS1 for missense variants when other variant was classified pathogenic by VCEP standards without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
*   Use at the default (PS1) level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant **at the same position** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the default (PS1) level for splicing variants in combination with **PVS1** if located **within** the splice donor/acceptor +/-1,2 dinucleotide positions with a comparable variant **within the same splice donor/acceptor +/-1,2 dinucleotide** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
- **Moderate** ✅：*   Use PS1\_Moderate for missense variants when the other variant was classified likely pathogenic by VCEP standards without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
*   Use at the PS1\_Moderate level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 with a comparable nucleotide variant **at the same position** that has been classified **likely pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the PS1\_Moderate level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 with a comparable variant **within the same splice region** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the PS1\_Moderate level for splicing variants in combination with **PVS1 (at reduced strength)** if located **within** the splice donor/acceptor +/-1,2 dinucleotide positions with a comparable variant **within the same splice donor/acceptor motif (but outside the +/-1,2 dinucleotide)** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
- **Supporting** ✅：*   Use at the PS1\_Supporting level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 with a comparable nucleotide variant **within the same motif** that has been classified l**ikely pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the PS1\_Supporting level in combination with **PVS1** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant at the **same nucleotide position** or **within the same donor/acceptor +/-1,2 dinucleotide** with the same predicted impact that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the PS1\_Supporting level in combination with **PVS1** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant **within the same splice region, but outside the donor/acceptor +/-1,2 dinucleotide**, with the same predicted impact that has been classified **pathogenic or likely pathogenic** by VCEP standards (PMID: 37352859).
*   Use at the PS1\_Supporting level in combination with **PVS1 (at reduced strength)** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant **within the same splice region, but outside the donor/acceptor +/-1,2 dinucleotide**, with the same predicted impact that has been classified **likely pathogenic** by VCEP standards (PMID: 37352859).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:

*   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
*   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
*   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Strong** ✅：The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:

*   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
*   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
*   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Moderate** ✅：The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:

*   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
*   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
*   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Supporting** ✅：The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:

*   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
*   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
*   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：*   PS3 will be applied at the default level of strength for an abnormal result in an approved _in vitro_ assay with a calculated OddsPath >18.7 (as recommended in PMID: 31892348). Example assays have not yet been found in published reports at the time of these specifications, but are anticipated in the future as additional studies are published.
- **Moderate** ✅：*   PS3 will be applied at the moderate level of strength for an abnormal result in an approved _in vitro_ assay with a minimum of 11 total pathogenic and benign variant controls (classified using these same specifications, as recommended in PMID: 31892348). Example assays with sufficient control variants have not yet been found in published reports at the time of these specifications, but are anticipated in the future as additional studies are published.
- **Supporting** ✅：*   An abnormal functional result by a _CTLA4_ variant in non-patient cells in an approved assay should be applied at PS3\_Supporting strength. Further details on how to interpret the assays can be found in the associated manuscript.
*   Functional assays can be found in the attached Excel file entitled CTLA4\_Functional Assay\_Research\_PS3\_BS3.
*   Assays approved by the VCEP for PS3\_Supporting are non-patient cell-based:
    *   (1)   CD80 or CD86 transendocytosis / soluble CD80 or CD86 ligand uptake in non-patient cells (i.e. PMID: 25329329, PMID: 25632005, PMID: 25367873, PMID: 27102614, PMID: 29375547, PMID: 15814706, PMID: 20870175)
    *   (2)   Cell surface expression of CTLA4 expressed in non-patient cell lines (i.e. PMID: 25367873, PMID: 14578884, PMID: 29375547, PMID: 7559643, PMID: 25213377)
    *   (3)   Protein localization / translocation by CTLA4 expressed in non-patient cell lines (i.e. PMID: 7559643, PMID: 20870175, PMID: 27102614, PMID: 25367873, PMID: 29375547, PMID: 15814706)
    *   (4)   _In vitro_ T cell suppression by CTLA4 expressed in non-patient cell lines (i.e. PMID: 29375547, PMID: 26478010, PMID: 25213377)
*   Please note that patient cell-based assays of CTLA4 function were also considered for inclusion in PS3\_Supporting, but were instead viewed as part of the proband phenotype and were incorporated into the PP4\_Moderate code instead.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
*   A proband would be excluded for this criterion if found to harbor homozygous or compound heterozygous _LRBA_ variants that are either rare VUS or have been classified Likely Pathogenic or Pathogenic.
*   PS4 at the default (Strong) level is Met by observation of the variant in at least 4 independent probands.
*   The probands used for PS4 cannot include the same proband used for PP4.
*   In order to be counted for this criterion, a proband must meet one of the following two requirements:
    *   To have reported phenotypes that score a minimum of 6 phenotype points, as well as genotyping of the _LRBA_ locus to confirm the absence of biallelic variants in _LRBA_ that have been classified either Likely Pathogenic or Pathogenic. Note: a monoallelic _LRBA_ variant can be tolerated.
    *   **OR**
    *   To have reported phenotypes that score a minimum of 10 phenotype points, in the absence of genotyping of the _LRBA_ locus.
*   Description of the phenotype point system can be found in the bullet points below or in a more detailed form in the attached table entitled “CTLA4 Phenotype Scoring Table”. The table includes a total of two 4-point criteria, one 3-point criterion, five 2-point criteria, and twelve 1-point criteria:
*   _Clinical criteria_
    *   Sinopulmonary findings 4
    *   Non-infectious gastrointestinal or hepatobiliary disease 4
    *   Immune-mediated cytopenias 2
    *   Nonmalignant Lymphoproliferation 2
    *   Severe, persistent, recurrent viral infections including skin warts 2
    *   Immune-mediated skin and hair findings 1
    *   Endocrinopathy 1
    *   Severe, persistent, recurrent, atypical, opportunistic bacterial, Mycobacterial or fungal infections 1
    *   Neurological findings 1
    *   Inflammatory findings (arthritis, vasculitis, recurrent fevers) 1
    *   Lymphoma 1
*   _Objective criteria_
    *   Hypogammaglobulinemia 2
    *   Lymphopenia 1
    *   Abnormal TBNK levels 1
    *   Presence of autoantibodies 1
    *   Defective antigen-specific immune responses 1
    *   Histopathology findings of lymphocytic / granulomatous tissue infiltration 1
*   _Patient cell-based assay data_
    *   Transendocytosis / Soluble CD80/CD86 ligand endocytosis (reduced) 3
    *   Ex vivo T cell suppression (reduced) 2
    *   Cell surface and/or intracellular CTLA4 expression (reduced) 1
- **Moderate** ✅：*   PS4\_Moderate is Met by observation of the variant in 2-3 independent probands.
*   The probands used for PS4\_Moderate cannot include the same proband used for PP4.
*   In order to be counted for this criterion, a proband must meet one of the following two requirements:
    *   To have reported phenotypes that score a minimum of 6 phenotype points, as well as genotyping of the _LRBA_ locus to confirm the absence of biallelic variants in _LRBA_ that have been classified either Likely Pathogenic or Pathogenic. Note: a monoallelic _LRBA_ variant can be tolerated.
    *   **OR**
    *   To have reported phenotypes that score a minimum of 10 phenotype points, in the absence of genotyping of the _LRBA_ locus.
*   Description of the phenotype point system can be found in the bullet points below or in a more detailed form in the attached table entitled “CTLA4 Phenotype Scoring Table”. The table includes a total of two 4-point criteria, one 3-point criterion, five 2-point criteria, and twelve 1-point criteria:
*   _Clinical criteria_
    *   Sinopulmonary findings 4
    *   Non-infectious gastrointestinal or hepatobiliary disease 4
    *   Immune-mediated cytopenias 2
    *   Nonmalignant Lymphoproliferation 2
    *   Severe, persistent, recurrent viral infections including skin warts 2
    *   Immune-mediated skin and hair findings 1
    *   Endocrinopathy 1
    *   Severe, persistent, recurrent, atypical, opportunistic bacterial, Mycobacterial or fungal infections 1
    *   Neurological findings 1
    *   Inflammatory findings (arthritis, vasculitis, recurrent fevers) 1
    *   Lymphoma 1
*   _Objective criteria_
    *   Hypogammaglobulinemia 2
    *   Lymphopenia 1
    *   Abnormal TBNK levels 1
    *   Presence of autoantibodies 1
    *   Defective antigen-specific immune responses 1
    *   Histopathology findings of lymphocytic / granulomatous tissue infiltration 1
*   _Patient cell-based assay data_
    *   Transendocytosis / Soluble CD80/CD86 ligand endocytosis (reduced) 3
    *   Ex vivo T cell suppression (reduced) 2
    *   Cell surface and/or intracellular CTLA4 expression (reduced) 1
- **Supporting** ✅：*   PS4\_Supporting is Met by 1 observation of the variant in a proband.
*   The proband used for PS4\_Supporting cannot be the same proband used for PP4.
*   In order to be counted for this criterion, a proband must meet one of the following two requirements:
    *   To have reported phenotypes that score a minimum of 6 phenotype points, as well as genotyping of the _LRBA_ locus to confirm the absence of biallelic variants in _LRBA_ that have been classified either Likely Pathogenic or Pathogenic. Note: a monoallelic _LRBA_ variant can be tolerated.
    *   **OR**
    *   To have reported phenotypes that score a minimum of 10 phenotype points, in the absence of genotyping of the _LRBA_ locus.
*   Description of the phenotype point system can be found in the bullet points below or in a more detailed form in the attached table entitled “CTLA4 Phenotype Scoring Table”. The table includes a total of two 4-point criteria, one 3-point criterion, five 2-point criteria, and twelve 1-point criteria:
*   _Clinical criteria_
    *   Sinopulmonary findings 4
    *   Non-infectious gastrointestinal or hepatobiliary disease 4
    *   Immune-mediated cytopenias 2
    *   Nonmalignant Lymphoproliferation 2
    *   Severe, persistent, recurrent viral infections including skin warts 2
    *   Immune-mediated skin and hair findings 1
    *   Endocrinopathy 1
    *   Severe, persistent, recurrent, atypical, opportunistic bacterial, Mycobacterial or fungal infections 1
    *   Neurological findings 1
    *   Inflammatory findings (arthritis, vasculitis, recurrent fevers) 1
    *   Lymphoma 1
*   _Objective criteria_
    *   Hypogammaglobulinemia 2
    *   Lymphopenia 1
    *   Abnormal TBNK levels 1
    *   Presence of autoantibodies 1
    *   Defective antigen-specific immune responses 1
    *   Histopathology findings of lymphocytic / granulomatous tissue infiltration 1
*   _Patient cell-based assay data_
    *   Transendocytosis / Soluble CD80/CD86 ligand endocytosis (reduced) 3
    *   Ex vivo T cell suppression (reduced) 2
    *   Cell surface and/or intracellular CTLA4 expression (reduced) 1

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：*   Not mutually exclusive with PM5.
*   Met by variants in the MYPPPY domain (residues 134-139), which is required for interaction with CD80 and CD86.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Supporting level only
*   Met for total allele frequency lower than 1.43 x 10<sup>-7</sup> (0.000000143) across all populations in gnomAD v4.1.0.
*   Threshold is based on the experts’ estimate of CTLA-4 insufficiency prevalence of 1/200,000 – 1/1,000,000 people and 45-70% penetrance. The lower end of the prevalence estimate (1 in 1,000,000) and the higher end of the penetrance estimate (70%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data) but can be used together with PM1.
*   Met at default strength (PM4) by an in-frame deletion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is \<0.2.
*   Met at default strength (PM4) by an in-frame insertion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is \<0.2.
*   The region of the protein affected by the variant is key to consider. If variants within this region occur in healthy populations, the region is polymorphic. Incomplete penetrance should also be considered as a caveat for polymorphism.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Do not apply for any variant that meets BS1 or BA1.
*   Not mutually exclusive with PM1.
*   Comparison variant must have a Pathogenic or Likely Pathogenic classification reached using these VCEP-specified rules without using PM5.
*   A Grantham score comparison can be used to determine whether the amino acid change introduced by the variant under evaluation is predicted to be as or more damaging (i.e., a Grantham score equal to or higher) than the established pathogenic amino acid change.
*   SpliceAI must be used to examine both variants for similar predicted effect or lack of effect on splicing (SpliceAI Δ score \<0.2).

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
    *   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Moderate** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
    *   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Supporting** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 and \<6 phenotype points in the PS4 counting rubric, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
    *   (C)  If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic _LRBA_ variants, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：*   Due to incomplete penetrance (45-70%), PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the PP1\_Strong level for co-segregation of the variant with the affected phenotype across at least 4 meioses in one family or combined across multiple unrelated families.
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
- **Moderate** ✅：*   Due to incomplete penetrance (45-70%), PP1\_Moderate will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the PP1\_Moderate level for co-segregation of the variant with the affected phenotype across at least two meioses in one family or combined across multiple unrelated families.
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
- **Supporting** ✅：*   Due to incomplete penetrance (45-70%), PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the supporting level for co-segregation of the variant with the affected phenotype across at least one meiosis (i.e. the variant is present in the proband + an affected relative).
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (PP3) level by a missense variant with REVEL score greater than or equal to 0.644 and CADD PHRED score greater than or equal to 25.3 (PMID: 36413997).
*   The above requirement for agreement between two _in silico_ tools was reached following a pilot study of suspected pathogenic and suspected benign variants (assembled from ClinVar submissions and published assertions of pathogenicity). Some suspected pathogenic _CTLA4_ variants fall in REVEL’s benign range while some suspected benign _CTLA4_ variants fall in CADD’s pathogenic range. All false positive and false negative predictions in the test set could be avoided by requiring that both tools agree in order for PP3 or BP4 to be Met.
*   Met by missense, synonymous, or intronic variants outside the +/-1,2 dinucleotide positions that are predicted as damaging using SpliceAI (cutoff Δ score greater than or equal to 0.2).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   In order to be counted for PP4\_Moderate, a proband must;
    *   score at least 10 phenotype points in the PS4 counting rubric
    *   AND
    *   have been genotyped using a method able to detect _LRBA_ variants without biallelic variants found AND
    *   have experimental data from the patient's cells showing a functional defect in the CTLA4 pathway such as defective CD80 and/or CD86 transendocytosis, defective Treg suppression of T cell proliferation, or reduced CTLA4 cell surface expression.
*   Patient cell-based assays approved for PP4\_Moderate are;
    *   (1)   CD80-GFP transendocytosis to CTLA4-expressing patient Tregs or memory CD4+ T cells (i.e. PMID: 25329329, PMID: 34111452, PMID: 28159733)
    *   (2)   Total expression of CTLA4 by patient Tregs and other T cells (i.e. PMID: 25213377, PMID: 25329329)
    *   (3)   Cell surface expression of CTLA4 by patient B cells or T cells (i.e. PMID: 25213377, PMID: 25329329, PMID: 34111452, PMID: 28159733)
*   This proband cannot be used for the PS4 code.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   In order to be counted for PP4 at the default (supporting) level of strength, a proband must;
    *   score at least 10 phenotype points in the PS4 counting rubric
    *   AND
    *   have been genotyped using a method able to detect _LRBA_ variants without biallelic variants found.
*   This proband cannot be used for the PS4 code.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Met for GrpMax Filtering Allele Frequency greater than or equal to 1.11 x 10<sup>-5</sup> (0.0000111) in gnomAD, with at least 5 alleles total across all populations in gnomAD (gnomAD v4.1.0).
*   Threshold is based on the experts’ estimate of CTLA-4 insufficiency prevalence of 1/200,000 – 1/1,000,000 people and 45-70% penetrance. A higher prevalence estimate (1 in 100,000) and the lower end of the penetrance estimate (45%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Met for GrpMax Filtering Allele Frequency greater than or equal to 1.11 x 10<sup>-6</sup> (0.00000111) in gnomAD, with at least 3 alleles total across all populations in gnomAD (gnomAD v4.1.0).
*   If GrpMax filtering allele frequency is not listed for the variant, this code is evaluated in relation to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian), but requires **at least 3 alleles total** across all populations in gnomAD (gnomAD v4.1.0) to be met.
*   Threshold is based on the experts’ estimate of CTLA-4 insufficiency prevalence of 1/200,000 – 1/1,000,000 people and 45-70% penetrance. An intermediate prevalence estimate (1 in 500,000) and the lower end of the penetrance estimate (45%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 0.5 were also assumed for the calculation.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：*   BS3 will be applied at the default level of strength for a normal result in an approved _in vitro_ assay with a calculated OddsPath \< 0.053 (as recommended in PMID: 31892348). Example assays have not yet been found in published reports at the time of these specifications, but are anticipated in the future as additional studies are published.
- **Moderate** ✅：*   BS3 will be applied at the moderate level of strength for an normal result in an approved _in vitro_ assay with a minimum of 11 total pathogenic and benign variant controls (classified using these same specifications, as recommended in PMID: 31892348). Example assays with sufficient control variants have not yet been found in published reports at the time of these specifications, but are anticipated in the future as additional studies are published.
- **Supporting** ✅：*   A normal result for a _CTLA4_ variant using one of the approved assays below cannot be interpreted to mean normal CTLA4 function by itself. BS3\_Supporting can only be applied when a second different assay also shows a normal result.
*   Functional assays can be found in the attached Excel file entitled CTLA4\_Functional Assay\_Research\_PS3\_BS3.
*   Although suspected benign variants are not present in all of the PMIDs below, assays approved by the VCEP for BS3\_Supporting are:
    *   (1)   CD80 or CD86 transendocytosis / soluble CD80 or CD86 ligand uptake in non-patient cells (i.e. PMID: 25329329, PMID: 25632005, PMID: 25367873, PMID: 27102614, PMID: 29375547, PMID: 15814706, PMID: 20870175)
    *   (2)   Cell surface expression of CTLA4 expressed in non-patient cell lines (i.e. PMID: 25367873, PMID: 14578884, PMID: 29375547, PMID: 7559643, PMID: 25213377)
    *   (3)   Protein localization / translocation by CTLA4 expressed in non-patient cell lines (i.e. PMID: 7559643, PMID: 20870175, PMID: 27102614, PMID: 25367873, PMID: 29375547, PMID: 15814706)
    *   (4)   _In vitro_ T cell suppression by CTLA4 expressed in non-patient cell lines (i.e. PMID: 29375547, PMID: 26478010, PMID: 25213377)
*   Please note that patient cell-based assays of CTLA4 function were also considered for inclusion in BS3\_Supporting, but were instead viewed as part of the proband phenotype.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：*   Due to incomplete penetrance (45-70%), BS4 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting lack of segregation.
*   Lack of segregation should be identified in more than 1 affected family member.
- **Supporting** ✅：*   Due to incomplete penetrance (45-70%), BS4\_Supporting will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting lack of segregation.
*   If only 1 affected family member lacks segregation of the genotype, downgrade to BS4\_Supporting.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (BP4) level by a missense variant with REVEL score less than or equal to 0.290, CADD PHRED score less than or equal to 22.7, and SpliceAI Δ score \<0.1 (PMID: 36413997).
*   The above requirement for agreement between two _in silico_ tools was reached following a pilot study of suspected pathogenic and suspected benign variants (assembled from ClinVar submissions and published assertions of pathogenicity). Some suspected pathogenic _CTLA4_ variants fall in REVEL’s benign range while some suspected benign _CTLA4_ variants fall in CADD’s pathogenic range. All false positive and false negative predictions in the test set could be avoided by requiring that both tools agree in order for PP3 or BP4 to be Met.
*   Applicable to both synonymous variants and all intronic variants outside the +/-1,2 dinucleotide positions not predicted to impact splicing by SpliceAI (SpliceAI Δ score \<0.1, PMID: 37352859).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：*   Two such cases are required to mitigate the VCEP’s concern over relying on other groups’ classifications of pathogenic variants in genes such as _LRBA_.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：*   BP7\_Strong (RNA) is met by variants with experimental evidence of no impact on splicing (PMID: 3735285).
- **Supporting** ✅：*   Apply only if BP4 is met.
*   Applicable to both synonymous variants and intronic variants not predicted to impact splicing by SpliceAI (SpliceAI Δ score \<0.1, PMID: 37352859).
*   Only applicable for intronic/non-coding variants located outside the donor/acceptor splice region (conservatively designated as intronic variants at or beyond positions +7/−21) or for synonymous exonic variants located outside of the first nucleotide or the last 3 nucleotides of the exon (PMID: 37352859).

### 不适用证据码
PM3、PP2、PP5、BS2、BP1、BP2、BP3、BP6
### 附件关键数据

#### 积分分类系统关键数据（CTLA4 Points System）

**变异分类阈值：**

| 分类 | 所需积分范围 |
|------|-------------|
| 致病（Pathogenic） | ≥10分 |
| 可能致病（Likely Pathogenic） | 6-9分 |
| 意义不明确（VUS） | 0-5分 |
| 可能良性（Likely Benign） | -1至-6分 |
| 良性（Benign） | ≤-7分 |

**关键证据码积分权重：**
- PVS1 = 4分
- PVS1_Strong = 2分
- PS1 = 1分
- PP4_Moderate = 2分

#### 表型评分表（PS4评分系统）

**临床标准：**

| 临床发现 | 积分 |
|---------|------|
| 鼻窦肺病变（Sinopulmonary findings） | 4分 |
| 非感染性胃肠或肝胆疾病 | 4分 |
| 免疫介导的细胞减少 | 2分 |
| 非恶性淋巴增殖 | 2分 |
| 严重、持续、反复发作的病毒感染（包括皮肤疣） | 2分 |
| 免疫介导的皮肤和毛发表现 | 1分 |
| 内分泌病 | 1分 |
| 严重、持续、反复、异型、条件性致病菌、分枝杆菌或真菌感染 | 1分 |
| 神经系统表现 | 1分 |
| 炎症表现（关节炎、血管炎、反复发热） | 1分 |
| 淋巴瘤 | 1分 |

**客观标准：**

| 客观发现 | 积分 |
|---------|------|
| 低丙种球蛋白血症 | 2分 |
| 淋巴细胞减少 | 1分 |
| 异常TBNK水平 | 1分 |
| 存在自身抗体 | 1分 |
| 抗原特异性免疫反应缺陷 | 1分 |
| 淋巴细胞/肉芽肿组织浸润的组织病理学表现 | 1分 |

#### PS2/PM6积分表（CTLA4 PS2 PM6 Table）

| 表型一致性 | 确认de novo | 推定de novo |
|-----------|-------------|-------------|
| 表型高度特异于基因 | 2分 | 1分 |
| 表型符合基因但非高度特异 | 1分 | 0.5分 |
| 表型符合基因但非高度特异且遗传异质性高 | 0.5分 | 0.25分 |
| 表型不符合基因 | 0分 | 0分 |

| 证据强度 | 积分阈值 |
|---------|---------|
| PS2_Very Strong / PM6_Very Strong | ≥2分 |
| PS2_Strong / PM6_Strong | ≥1分 |
| PS2_Moderate / PM6_Moderate | ≥0.5分 |
| PS2_Supporting / PM6_Supporting | ≥0.25分 |

#### 功能检测关键数据（CTLA4 Functional Assay Research PS3 BS3）

**PS3_Strong批准检测：**
- OddsPath >18.7的体外检测异常结果

**PS3_Moderate批准检测：**
- ≥11个总对照变异（包括致病和良性）的体外检测异常结果

**PS3_Supporting批准检测（基于非患者细胞）：**
1. CD80或CD86反式内吞/可溶性CD80或CD86配体摄取
2. 细胞表面CTLA4表达
3. 蛋白质定位/转运
4. 体外T细胞抑制

**关键计算器阈值：**
- PP3阈值：REVEL ≥0.644，CADD PHRED ≥25.3（PMID: 36413997）
- BP4阈值：REVEL ≤0.290，CADD PHRED ≤22.7（PMID: 36413997）
- SpliceAI阈值：<0.1（无剪接影响）

### 参考附件
- [Points system to reach final classification](https://cspec.genome.network/cspec/File/id/49436e75-05bb-40e0-94f6-0257b207168c/data)
- [VCEP updates in response to SVI review](https://cspec.genome.network/cspec/File/id/a9c236b2-981d-4e7a-9ac4-77556f027b45/data)
- [CTL4 Domains and Exons](https://cspec.genome.network/cspec/File/id/09b7779c-b30b-4ef5-812e-4909d4a39336/data)
- [PVS1 Decision Tree for CTLA4](https://cspec.genome.network/cspec/File/id/5e6aa8dc-2b51-4efe-a638-42c216aa7aa8/data)
- [PS2 / PM6 Table](https://cspec.genome.network/cspec/File/id/e63e9cc5-d8c7-4e79-98d9-1be11542eb1c/data)
- [CTLA4_Pilot_Results](https://cspec.genome.network/cspec/File/id/386adca2-8d84-4b6f-8361-1fcff1942815/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN122)

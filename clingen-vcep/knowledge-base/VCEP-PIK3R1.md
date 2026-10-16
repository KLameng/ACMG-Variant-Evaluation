# ClinGen VCEP基因特异性规范：PIK3R1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN160 — Antibody Deficiencies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:1060136**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Please note that the Antibody Deficiencies GCEP has changed the curated disease term from "immunodeficiency 36 with lymphoproliferation" (MONDO:0014453) to "PIK3R1-related immunodeficiency and SHORT syndrome" (MONDO:1060136).
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   If a nonsense or frameshift variant introduces a premature stop codon between c.917 and c.1890, which is predicted to trigger nonsense mediated decay, and the exon is present in all 3 biologically-relevant transcripts (NM\_181523.3, NM\_181504.4, and NM\_181524.2),, apply PVS1.
*   If a canonical splicing variant is predicted to result in skipping of exon 8, 10, or 12, which would disrupt the frame and be predicted to trigger nonsense-mediated decay, apply PVS1.
*   If a nonsense or frameshift variant introduces a premature stop codon between c.4 and c.916, which is predicted to trigger nonsense-mediated decay but the exon is present only in the MANE transcript NM\_181523.3 but absent from NM\_181504.4 and NM\_181524.2, do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   Do not apply PVS1 at any strength for initiation codon variants. There are two known alternative start codons located after codon 306 of _PIK3R1_ in the MANE transcript encoding the p85α isoform (PMID: 28802037). Although there are known disease-causing variants upstream of these alternative start codons, indicating that disruption of the p85α isoform alone is sufficient to cause disease, these variants have so far been published only in association with agammaglobulinemia 7 with autosomal recessive inheritance, and are not considered applicable for the current specifications.
*   If a canonical splicing variant is predicted to result in skipping of exon 1 (non-coding), exon 2 (which contains the start codon for the MANE transcript), exon 3 (in-frame), exon 4 (in-frame), exon 5 (in-frame), exon 6 (out-of-frame), or exon 7 (out-of-frame), do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score >0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3\_Supporting and evaluate PVS1(RNA) instead (PMID: 37352859).
- **Strong** ✅：*   If a nonsense or frameshift variant introduces a premature stop between codons 631 and 645, which is predicted to trigger nonsense mediated decay but located 45 nucleotides or less from the NMD prediction boundary, and the exon is present in all 3 biologically-relevant transcripts (NM\_181523.3, NM\_181504.4, and NM\_181524.2), apply PVS1\_Strong.
*   If a nonsense or frameshift variant introduces a premature stop between codons 646 and 718 that is not predicted to trigger nonsense mediated decay but disrupts the cSH2 domain, apply PVS1\_Strong.
*   If a canonical splicing variant is predicted to result in skipping of in-frame exon 9 or 11 (which encode the nSH2 domain), in-frame exon 13 or 14, (which encode the iSH2 domain), or either in-frame exon 15 or out-of-frame exon 16, (which encode the cSH2 domain, PMID: 38043374), apply PVS1\_Strong.
*   If a nonsense or frameshift variant introduces a premature stop codon between c.4 and c.916, which is predicted to trigger nonsense-mediated decay but the exon is present only in the MANE transcript NM\_181523.3 but absent from NM\_181504.4 and NM\_181524.2, do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   Do not apply PVS1 at any strength for initiation codon variants. There are two known alternative start codons located after codon 306 of _PIK3R1_ in the MANE transcript encoding the p85α isoform (PMID: 28802037). Although there are known disease-causing variants upstream of these alternative start codons, indicating that disruption of the p85α isoform alone is sufficient to cause disease, these variants have so far been published only in association with agammaglobulinemia 7 with autosomal recessive inheritance, and are not considered applicable for the current specifications.
*   If a canonical splicing variant is predicted to result in skipping of exon 1 (non-coding), exon 2 (which contains the start codon for the MANE transcript), exon 3 (in-frame), exon 4 (in-frame), exon 5 (in-frame), exon 6 (out-of-frame), or exon 7 (out-of-frame), do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score >0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3\_Supporting and evaluate PVS1(RNA) instead (PMID: 37352859).
- **Moderate** ✅：*   If a nonsense or frameshift variant introduces a premature stop between codons 719 and 724 that is not predicted to trigger nonsense mediated decay or to disrupt the cSH2 domain, apply PVS1\_Moderate.
*   If a nonsense or frameshift variant introduces a premature stop codon between c.4 and c.916, which is predicted to trigger nonsense-mediated decay but the exon is present only in the MANE transcript NM\_181523.3 but absent from NM\_181504.4 and NM\_181524.2, do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   Do not apply PVS1 at any strength for initiation codon variants. There are two known alternative start codons located after codon 306 of _PIK3R1_ in the MANE transcript encoding the p85α isoform (PMID: 28802037). Although there are known disease-causing variants upstream of these alternative start codons, indicating that disruption of the p85α isoform alone is sufficient to cause disease, these variants have so far been published only in association with agammaglobulinemia 7 with autosomal recessive inheritance, and are not considered applicable for the current specifications.
*   If a canonical splicing variant is predicted to result in skipping of exon 1 (non-coding), exon 2 (which contains the start codon for the MANE transcript), exon 3 (in-frame), exon 4 (in-frame), exon 5 (in-frame), exon 6 (out-of-frame), or exon 7 (out-of-frame), do not apply PVS1 at any strength in the context of this gene-disease relationship (MONDO:1060136). These variants have been published so far only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
*   If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score >0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3\_Supporting and evaluate PVS1(RNA) instead (PMID: 37352859).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Use PS1 for missense variants when other variant was classified pathogenic by VCEP standards without using PS1. Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
*   Use PS1 for canonical splice variants or variants predicted to disrupt splicing when the predicted impact is the same as a previously classified P / LP variant. The appropriate PS1 strength level is shown in the figure and table below (adapted from Table 2 in PMID: 37352859) based on the locations of the variant under assessment and the comparison variant within the splice donor or splice acceptor motif, as well as the classification of the comparison variant as Pathogenic (A) vs. LIkely Pathogenic (B). Please note that PS1 strength is reduced for variants disrupting a canonical splice site adjacent to an out-of-frame exon because PVS1 (very strong) has already been applied.
- **Moderate** ✅：*   Use PS1\_Moderate for missense variants when the other variant was classified likely pathogenic by VCEP standards without using PS1. Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
*   Use PS1 for canonical splice variants or variants predicted to disrupt splicing when the predicted impact is the same as a previously classified P / LP variant. The appropriate PS1 strength level is shown in the figure and table below (adapted from Table 2 in PMID: 37352859) based on the locations of the variant under assessment and the comparison variant within the splice donor or splice acceptor motif, as well as the classification of the comparison variant as Pathogenic (A) vs. LIkely Pathogenic (B). Please note that PS1 strength is reduced for variants disrupting a canonical splice site adjacent to an out-of-frame exon because PVS1 (very strong) has already been applied.
- **Supporting** ✅：*   Use PS1 for canonical splice variants or variants predicted to disrupt splicing when the predicted impact is the same as a previously classified P / LP variant. The appropriate PS1 strength level is shown in the figure and table below (adapted from Table 2 in PMID: 37352859) based on the locations of the variant under assessment and the comparison variant within the splice donor or splice acceptor motif, as well as the classification of the comparison variant as Pathogenic (A) vs. LIkely Pathogenic (B). Please note that PS1 strength is reduced for variants disrupting a canonical splice site adjacent to an out-of-frame exon because PVS1 (very strong) has already been applied.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 but \<6 phenotype points in the PS4 counting rubric and lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores greater than or equal to 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (C)  If the proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Strong** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 but \<6 phenotype points in the PS4 counting rubric and lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores greater than or equal to 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (C)  If the proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Moderate** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 but \<6 phenotype points in the PS4 counting rubric and lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores greater than or equal to 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (C)  If the proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.
- **Supporting** ✅：*   The “phenotypic consistency” used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
    *   (A)  If the proband scores greater than or equal to 4 but \<6 phenotype points in the PS4 counting rubric and lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (B)  If the proband scores greater than or equal to 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
    *   (C)  If the proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3CD_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：*   PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the immunodeficiency phenotype (PMID: 26974159, PMID: 28632845).
*   PS3 will be applied for an abnormal result in an approved _in vitro_ assay with an OddsPath >18.7 (PMID: 31892348). One example has been found in the literature:
    *   Ratio of variant enrichment in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells (PMID: 40543502)
- **Moderate** ✅：*   PS3\_Moderate will be applied for an abnormal result in an approved _in vitro_ assay with at least 11 known pathogenic or benign variant controls (classified using these specifications, PMID: 31892348).
- **Supporting** ✅：*   PS3\_Supporting can be applied based on an abnormal result in an approved _in vitro_ assay. Approved assay classes and specific assay instances include:
    *   Lipid kinase activity (PMID: 28167755)
    *   AKT kinase activity (PMID: 23810379, PMID: 25133428; PMID: 25488983; PMID: 28167755) 
    *   Protein binding (PMID: 25488983)
    *   Conformational dynamics (PMID: 28167755)
*   PS3\_Supporting will not be applied to mRNA splicing assays showing exon 11 skipping that affect all or nearly all transcripts (PMID: 27221134, PMID: 25133428, PMID: 25488983), as these can be used in combination with a SpliceAI prediction of disruption of a splice donor / acceptor site to meet PVS1\_Strong (RNA) instead.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：*   Use PS4 at the default level of strength when four or more probands meet the phenotype scoring criteria in **Table 3** and genetic testing requirements described below.
*   Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3R1-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3R1-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3CD_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Moderate** ✅：*   Use PS4\_Moderate when 2-3 probands meet the phenotype scoring criteria in **Table 3** and genetic testing requirements described below.
*   Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4\_Moderate.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3R1-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3R1-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3CD_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   Use PS4\_Supporting when one proband meets the phenotype scoring criteria in **Table 3** and genetic testing requirements.
*   Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4\_Supporting.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3R1-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3R1-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3CD_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Used at PM2\_Supporting strength.
*   Applicable to variants with a total allele frequency \<0.00000132 across all populations in gnomAD v4.1.0.
*   Population allele frequency threshold has been determined using the Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for primary immunodeficiency and the inheritance tailored to the autosomal dominant mode of inheritance):
    *   Prevalence: 1 in 4000
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 0.95

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data).
*   Met at default strength (PM4) by an **in-frame deletion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (PhyloP score greater than or equal to 2.0).
*   Met at default strength (PM4) by an **in-frame insertion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (PhyloP score greater than or equal to 2.0).
*   Met at default strength (PM4) by a **stop-loss variant** resulting in the addition of 2 or more amino acids to the C-terminus.
*   The region of the protein affected by the variant is key to consider. If only benign or likely benign variants are known to be located within this region, the region is polymorphic and PM4 does not apply.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Use PM5 at the default (moderate) strength level for a missense variant when another missense variant encoding a different amino acid change in the same codon was classified as Pathogenic by Antibody Deficiencies VCEP specifications for _PIK3R1_ without using PM5.
*   Neither the variant of interest nor the Pathogenic comparison variant should be predicted to affect splicing (all SpliceAI Δ scores \<0.2 for both variants).
*   The variant of interest must have a higher Grantham score than the Pathogenic comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
*   Do not apply at codon where any benign variants are known.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   Use PM5\_Supporting for a missense variant when another missense variant encoding a different amino acid change in the same codon was classified as Likely Pathogenic by Antibody Deficiencies VCEP specifications for _PIK3R1_ without using PM5.
*   Neither the variant of interest nor the Likely Pathogenic comparison variant should be predicted to affect splicing (all SpliceAI Δ scores \<0.2 for both variants).
*   The variant of interest must have a higher Grantham score than the Likely Pathogenic comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
*   Do not apply at codon where any benign variants are known.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
*   Met at the PP1\_Strong level if the variant co-segregates with the affected phenotype across at least 4 meioses, either in one family or combined across multiple unrelated families.
- **Moderate** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
*   Met at the PP1\_Moderate level if the variant co-segregates with the affected phenotype across the proband and two affected first degree relatives, across the proband and one affected second degree relative, or across two unrelated probands and one affected first degree relative each (2 meioses total).
- **Supporting** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
*   Met at the Supporting level if the variant co-segregates with the affected phenotype across the proband and one affected first degree relative (1 meiosis).

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   PP3 is met by a missense variant with both REVEL greater than or equal to 0.644 and CADD greater than or equal to 26.0.
*   The VCEP will try to determine during the pilot whether higher strength levels of PP3 are appropriate for _PIK3R1_ variants.
*   PP3 is met by missense, synonymous, or intronic variants outside the +/-1,2 dinucleotide positions that are predicted as damaging using SpliceAI (Δ score for donor gain, donor loss, acceptor gain, or acceptor loss score greater than or equal to 0.2, PMID: 37352859).
*   Splice impact must be assessed for every missense, small in-frame insertion and/or deletion, synonymous, or intronic variant.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   PP4\_Moderate is met when a proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping that did not identify an alternative basis for disease at the _PIK3CD_ locus AND has patient cell-based evidence of abnormally high activity of the disease-relevant PI3K delta pathway.
*   Patient cell-based experiments generally isolate T cells from affected and unaffected patients and often perform stimulation by anti-CD3 and anti-CD28 antibodies, followed by assessment of PI3K delta pathway function using western blotting or flow cytometry in combination with phospho-specific antibodies. These methods detect levels of AKT phosphorylation at Ser473 or Thr308 (PMID: 25133428, PMID: 25488983) and/or S6 phosphorylation at Ser235/Ser236 or Ser240/Ser244 (PMID: 25488983). Phosphorylation may be upregulated in cells from the affected patient relative to the healthy control.
*   Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   PP4 is met when a proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric (Table 3) AND has genotyping that did not identify an alternative basis for disease at the _PIK3CD_ locus.
*   Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.00316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters:
    *   Inheritance: biallelic (in order to generate a higher / more stringent threshold that would rule out a variant as a credible cause of either autosomal dominant or autosomal recessive disease)
    *   Prevalence: 1 in 100,000 (calculated at 1 in 7,500,000 based on the USIDNET cohort, PMID: 34352450, but adjusted based on expectation that cases are actually more common, resulting in a much more frequent / more aggressive prevalence estimate of 1 in 100,000 in order to generate a more conservative estimate)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 1
*   Please note that the values cited above (e.g. complete penetrance) are not asserted to be true for this condition. Rather, they are used in order to derive the most rigorous thresholds possible for a disease for which there are incomplete population epidemiology data.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.000316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   The BS1 threshold was derived by decreasing the BA1 cutoff (greater than or equal to 0.00316) by one order of magnitude.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：*   BS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and failing to recapitulate the phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
*   BS3 will be applied for a non-damaging result in an approved _in vitro_ assay with an OddsPath \<0.053 (PMID: 31892348). No such assays have yet been identified in the _PIK3R1_ literature.
- **Moderate** ✅：*   BS3\_Moderate will be applied for a non-damaging result in an approved _in vitro_ assay with at least 11 known pathogenic or benign variant controls (classified using these specifications, PMID: 31892348).
*   While one such _in vitro_ assay has been identified in the _PIK3R1_ literature (PMID: 40543502), the authors have recommended a non-damaging result in their assay of the ratio of enrichment of the variant in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells for BS3\_Supporting, based on their calculated OddsPath of 0.25.
- **Supporting** ✅：*   BS3\_Supporting can be applied based on a normal result in at least two different approved _in vitro_ assays. Approved assay classes and specific assay instances include:
    *   Lipid kinase activity (PMID: 28167755)
    *   AKT kinase activity (PMID: 23810379, PMID: 25133428; PMID: 25488983; PMID: 28167755) 
    *   Protein binding (PMID: 25488983)
    *   Conformational dynamics (PMID: 28167755)
*   BS3\_Supporting can be applied based on a normal result in the following approved _in vitro_ assay:
    *   Ratio of variant enrichment in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells (PMID: 40543502, OddsPath 0.25)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：*   Use caution in case the phenotype is not highly specific. Each of the affected family members lacking the variant must reach at least 6 points in the PS4 scoring table to be considered for this code.
*   BS4 is met at the default level of strength when at least 2 affected family members do not harbor the variant.
- **Supporting** ✅：*   Use caution in case the phenotype is not highly specific. The affected family member lacking the variant must reach at least 6 points in the PS4 scoring table to be considered for this code.
*   BS4\_Supporting is met if only 1 affected family member does not harbor the variant.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   BP4 is met by a missense variant with both REVEL less than or equal to 0.290 and CADD less than or equal to 21.5, as well as SpliceAI Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss \<0.1.
*   The VCEP will try to determine during the pilot whether higher strength levels of BP4 are appropriate for _PIK3R1_ variants.
*   BP4 is met by synonymous or intronic variants not predicted to impact splicing by SpliceAI (Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss \<0.1 (PMID: 37352859)).
*   BP4 can be used in combination with BP7 for synonymous or intronic variants without being considered double-counting (PMID: 37352859).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：At least 2 cases with an alternative molecular basis for disease are required to mitigate the reliance on assertions of variant pathogenicity in genes outside of the purview of the Antibody Deficiencies VCEP.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：*   BP7\_Strong (RNA) is met by variants with experimental evidence of no impact on splicing.
- **Supporting** ✅：*   Met by synonymous variants (except those located in the first nucleotide of an exon or last 3 nucleotides of an exon) not predicted to impact splicing by SpliceAI (all Δ scores \<0.1, PMID: 37352859).
*   Met by intronic variants (outside of the +1 to +6 and -1 to -20 positions relative to the exon) not predicted to impact splicing by SpliceAI (all Δ scores \<0.1, PMID: 37352859).
*   BP7 can be used in combination with BP4 for synonymous or intronic variants without being considered double-counting (PMID: 37352859).

### 点系统分类（Tavtigian 贝叶斯框架，v1.0 浏览器实页核实 2026-10-08）

本规范（Version 1.0，Released 4/29/2026；Type: Tavtigian et.al., 2020 - Bayesian adaptation of Richards et.al., 2015）采用贝叶斯适配的点系统。各证据码强度对应的 Default Point Value 如下：

**致病方向（正分）**

| 积分 | 证据码强度 |
|---|---|
| +8 | PVS1（Very Strong）、PS2（Very Strong） |
| +4 | PVS1_Strong、PS1、PS3、PS4、PP1_Strong |
| +2 | PVS1_Moderate、PS1_Moderate、PS2_Moderate、PS3_Moderate、PS4_Moderate、PM4、PM5、PP1_Moderate、PP4_Moderate |
| +1 | PS1_Supporting、PS2_Supporting、PS3_Supporting、PS4_Supporting、PM2_Supporting、PM5_Supporting、PP1_Supporting、PP3、PP4_Supporting |

**良性方向（负分）**

| 积分 | 证据码强度 |
|---|---|
| Stand Alone（不记分，独立判良性） | BA1 |
| -4 | BS1、BS3_Strong、BS4、BP7_Strong（RNA） |
| -2 | BS3_Moderate |
| -1 | BS3_Supporting、BS4_Supporting、BP4、BP5、BP7_Supporting |

**Point Based Variant Classification Categories（积分分类切分）**

| 分类 | 积分区间 |
|---|---|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤ -7 |

> 积分合成规则见参考附件《Rules for Combining Pathogenic / Benign Criteria》（Bayesian rules for combining pathogenic / benign criteria to reach final classification）。

### 不适用证据码
PM1、PM3、PM6、PP2、PP5、BS2、BP1、BP2、BP3、BP6
### 参考附件
- [Overview of recent updates](https://cspec.genome.network/cspec/File/id/93606d26-2d6b-49bc-91b9-ca111c420628/data)
- [PIK3R1 Functional Assays](https://cspec.genome.network/cspec/File/id/7ba9136e-d57d-48a6-8884-cdb5f204e297/data)
- [Rules for Combining Pathogenic / Benign Criteria](https://cspec.genome.network/cspec/File/id/7050b0fe-1b51-41f6-9864-989ac04a81f7/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN160)

# ClinGen VCEP基因特异性规范：PIK3CD

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN141 — Antibody Deficiencies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0014222**（遗传方式：Autosomal dominant inheritance）

### 通用说明
The current specifications for PIK3CD variant curation are written in relation to autosomal dominant rather than autosomal recessive forms of disease, with a gain-of-function rather than loss-of-function mechanism of pathogenicity. Unfortunately, there is no a priori way to exclude one mode of inheritance or the other, so both need to considered initially while assessing the variant. However, in general, only variants predicted to lead to a single missense amino acid substitution have thus far been shown to have a gain-of-function (GOF) effect in PIK3CD so any other types of variants should not enter this classification criteria.

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Use at the default level (PS1) for missense variants when other variant was classified as Pathogenic for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score \<0.2).
- **Moderate** ✅：*   Use at the PS1\_Moderate level for missense variants when other variant was classified as Likely Pathogenic for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score \<0.2).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：*   Use PS2\_VeryStrong when there are four or more _de novo_ occurrences according to the attached Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrences (Table 2).
*   The “phenotypic consistency” used on the attached Table 1 (Points awarded per _de novo_ occurrence) will be chosen for each proband by the number of phenotype points scored by the proband on the attached Phenotype scoring criteria per affected individual (Table 3):

1.  If the proband scores at least 4 and \<6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
2.  If the proband scores at least 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
3.  If the proband scores at least 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

*   PS2\_VeryStrong can only be applied if the variant does not meet BA or BS1.
- **Strong** ✅：*   Use PS2\_Moderate when there are 2 - 3 _de novo_ occurrences according to the attached Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrences (Table 2).
*   The “phenotypic consistency” used on the attached Table 1 (Points awarded per _de novo_ occurrence) will be chosen for each proband by the number of phenotype points scored by the proband on the attached Phenotype scoring criteria per affected individual (Table 3):

1.  If the proband scores at least 4 and \<6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
2.  If the proband scores at least 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
3.  If the proband scores at least 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

*   PS2 can only be applied if the variant does not meet BA or BS1.
- **Moderate** ✅：*   Use PS2\_Moderate when there is one de novo occurrence according to the attached Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrences (Table 2).
*   The “phenotypic consistency” used on the attached Table 1 (Points awarded per _de novo_ occurrence) will be chosen for each proband by the number of phenotype points scored by the proband on the attached Phenotype scoring criteria per affected individual (Table 3):

1.  If the proband scores at least 4 and \<6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
2.  If the proband scores at least 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
3.  If the proband scores at least 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

*   PS2\_Moderate can only be applied if the variant does not meet BA or BS1.
- **Supporting** ✅：*   Use PS2\_Supporting when there is one de novo occurrence according to the attached Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrences (Table 2).
*   The “phenotypic consistency” used on the attached Table 1 (Points awarded per _de novo_ occurrence) will be chosen for each proband by the number of phenotype points scored by the proband on the attached Phenotype scoring criteria per affected individual (Table 3):

1.  If the proband scores at least 4 and \<6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific and high genetic heterogeneity”.
2.  If the proband scores at least 6 phenotype points in the PS4 counting rubric but lacks genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype consistent with gene but not highly specific”.
3.  If the proband scores at least 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out variants in the _PIK3R1_ locus, use the number of _de novo_ points corresponding to “Phenotype highly specific for gene”.

*   PS2\_Supporting can only be applied if the variant does not meet BA or BS1.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：*   PS3 will be applied at the default level of strength for evidence from an animal model expressing the variant of interest and recapitulating the APDS phenotype. This strength level is considered particularly appropriate if multiple mouse models of the same variant recapitulate APDS features.
*   PS3 will be applied at the default level of strength for an abnormal result in an approved _in vitro_ assay with a calculated OddsPath >18.7 (as recommended in PMID: 31892348). One example has been found in the literature:
    *   Enrichment of the variant in high phospho-S6 and phospho-AKT T cells relative to low phospho-S6 and phospho-AKT T cells, within a next generation sequencing-based screen of donor T cells subjected to of CRISPR-mediated adenine base-editing (PMID: 40543502)
- **Moderate** ✅：*   PS3 will be applied at the moderate level of strength for an abnormal result in an approved _in vitro_ assay with a minimum of 11 total pathogenic and benign variant controls (classified using these same specifications, as recommended in PMID: 31892348). Example assays with sufficient control variants have not yet been found in published reports at the time of these specifications, but are anticipated in the future as additional studies are published.
- **Supporting** ✅：*   PS3\_Supporting can be applied based on an abnormal result in an approved _in vitro_ assay. These are described in detail in the attached Excel file entitled “PIK3CD\_Functional\_Assays\_PS3\_BS3”
    *   Approved assay classes and specific assay instances: 
        *   AKT kinase activity assay
            *   PMID: 24136356, PMID: 24165795, PMID: 28414062
        *   Lipid kinase activity 
            *   PMID: 24136356; PMID: 28167755;  PMID: 28414062
        *   Lipid vesicle affinity
            *   PMID: 24136356
        *   Conformational dynamics: 
            *   PMID: 28167755; PMID: 28414062
*   Please note that protein binding assays testing PIK3CD binding to PIK3R1 were also considered for inclusion in PS3\_Supporting, but were excluded based on lack of evidence of altered binding by disease-associated variants compared to wild-type controls (PMID: 24165795; PMID: 28414062).
*   Patient cell-based functional assays directly showing abnormally high activity of the disease-relevant PI3K delta pathway were considered for inclusion in the PS3\_Supporting code but are viewed as part of the proband phenotype and have been recommended for consideration under the PP4\_Moderate code instead.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：*   The strength of this code is defined in **Table 4**. Use PS4 at the default level of strength when four or more probands meet the phenotype scoring criteria in **Table 3** and genetic testing requirements described below. Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3CD-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3CD-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3R1_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Moderate** ✅：*   The strength of this code is defined in **Table 4**. Use PS4\_Moderate when 2-3 probands meet the phenotype scoring criteria in **Table 3** and genetic testing requirements described below. Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4\_Moderate.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3CD-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3CD-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3R1_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   The strength of this code is defined in **Table 4**. Use PS4\_Supporting when one proband meets the phenotype scoring criteria in **Table 3** and genetic testing requirements. Please note that a proband used for PP4 or PP4\_Moderate cannot be included in PS4\_Supporting.
*   Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband’s phenotypes are specific to PIK3CD-related immunodeficiency. Phenotypes have been grouped into categories such as “respiratory findings” or “gastrointestinal disease” to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3CD-related immunodeficiency.
*   A proband must reach greater than or equal to 6 points in the phenotype scoring criteria above (**Table 3**) and, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified no likely pathogenic or pathogenic variants in the _PIK3R1_ locus in order to be counted toward PS4
    *   Genome or exome sequencing is acceptable in lieu of a gene panel
    *   For genes associated with autosomal recessive disorders, carrier status is acceptable.
*   If no gene testing panel was performed, additional phenotypic features (reaching greater than or equal to 10 points) are required to count the proband toward PS4.
*   Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Downgraded to PM2\_Supporting
*   Applicable to variants with a total allele frequency \<0.00000132 across all populations in gnomAD v4.1.0.
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for autosomal dominant PIK3CD-related immune disease):
    *   Prevalence: 1 in 4000 (a conservative estimate for primary immunodeficiency diseases from PMID: 17577648, PMID: 23201919)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 0.95 (a conservative estimate based on multiple reports of incomplete but nearly complete penetrance in PMID: 27555459, PMID: 36749229, PMID: 37390899)

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Use at the default strength level (PM5) for missense variants when other variant was classified as Pathogenic for autosomal dominant PIK3CD-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PM5.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score ≤0.2).
*   Do not apply at codon where any benign variants are known.
*   The variant being evaluated must have a Grantham distance value greater than or equal to that of the known pathogenic variant, indicating that the variant residue is equally chemically different or more chemically different than the known pathogenic residue in comparison to the wild type residue.
- **Supporting** ✅：*   Use at PM5\_Supporting strength for missense variants when other variant was classified as Likely Pathogenic for autosomal dominant PIK3CD-related disease by Antibody Deficiencies VCEP specifications for _PIK3CD_ without using PM5.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Neither change should be predicted to affect splicing (SpliceAI Δ score \<0.2).
*   Do not apply at codon where any benign variants are known.
*   The variant being evaluated must have a Grantham distance value greater than or equal to that of the known likely pathogenic variant, indicating that the variant residue is equally chemically different or more chemically different than the known likely pathogenic residue in comparison to the wild type residue.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the PP1\_Strong level for co-segregation of the variant with the affected phenotype across at least 4 meioses in one family or combined across multiple unrelated families (PMID: 38103548).
*   The combined strength of the PP1 and PP4 codes is limited so that a variant that meets PP1\_Strong can meet PP4 but not PP4\_Moderate (PMID: 38103548).
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
- **Moderate** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the PP1\_Moderate level for co-segregation of the variant with the affected phenotype across at least two meioses in one family or combined across multiple unrelated families (PMID: 38103548).
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.
- **Supporting** ✅：*   PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
*   Met at the supporting level for co-segregation of the variant with the affected phenotype across at least one meiosis (i.e. the variant is present in the proband + an affected relative, PMID: 38103548).
*   PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (PP3) level by a missense variant with REVEL score greater than or equal to 0.644 and CADD PHRED score greater than or equal to 25.3.
*   Higher strength levels of PP3\_Moderate or PP3\_Strong have not been recommended due to pilot data indicating poor performance and significant discordance between REVEL and CADD predictions for established benign and gain-of-function _PIK3CD_ variants.
*   SpliceAI scores should be checked for missense variants, but there currently is no evidence of variants causing autosomal dominant disease through a splicing mechanism, so PP3 cannot be met by a variant located in the boundary exonic/intronic region with a predicted splicing impact. A variant with a predicted impact on splicing (SpliceAI Δ score greater than or equal to 0.2) should not be evaluated using these specifications, but rather using alternative specifications for autosomal recessive disease with a loss-of-function mechanism, unless functional evidence indicates a gain-of-function effect.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   PP4\_Moderate is met when a proband scores greater than or equal to 10 phenotype points in the PS4 counting rubric AND has genotyping to rule out a variant in the _PIK3R1_ locus AND has patient cell-based functional assays directly showing abnormally high activity of the disease-relevant PI3K delta pathway.
*   Patient cell-based functional experiments generally isolate T cells from affected and unaffected patients and often perform stimulation by anti-CD3 and anti-CD28 antibodies, followed by assessment of PI3K delta pathway function using western blotting or flow cytometry in combination with phospho-specific antibodies. These methods detect levels of AKT phosphorylation at Ser473 (PMID: 24136356, PMID: 28414062, PMID: 28428270) or Thr308 (PMID: 24165795) and/or S6 phosphorylation at Ser235/Ser236 (PMID: 28428270) or Ser240/Ser244 (PMID: 28414062). Phosphorylation may be upregulated by 1.2-fold to 7.5-fold in cells from the affected patient relative to the healthy control, and in some assays may be shown to be abrogated by PI3K-specific inhibitor (PMID: 28428270).
*   Please note that a proband used for PP4\_Moderate cannot be included in PS4.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.
- **Supporting** ✅：*   In order to be counted for this criterion, a proband must score greater than or equal to 10 phenotype points in the PS4 counting rubric **(Table 3)** AND have genotyping to rule out a variant in the _PIK3R1_ locus.
*   Please note that a proband used for PP4 cannot be included in PS4.
*   In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.00316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following estimated parameters (with the prevalence estimated for PIK3CD-related immune disease and the inheritance tailored to the autosomal recessive rather than autosomal dominant mode of inheritance, associated with complete penetrance):
    *   Inheritance: biallelic
    *   Prevalence: 1 in 100,000 (calculated at 1 in 7,500,000 based on the USIDNET cohort, PMID: 34352450, but adjusted based on expectation that cases are actually more common, resulting in a much more frequent / more aggressive prevalence estimate of 1 in 100,000 in order to generate a more conservative estimate)
    *   Allelic heterogeneity: 1
    *   Genetic heterogeneity: 1
    *   Penetrance: 1

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Applicable to variants with a GrpMax filtering allele frequency greater than or equal to 0.000316 in gnomAD v4.1.0.
*   If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
*   The BS1 threshold was derived by decreasing the BA1 cutoff (greater than or equal to 0.00316) by one order of magnitude.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：*   BS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and failing to recapitulate the APDS phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
- **Moderate** ✅：*   BS3 will be applied at the moderate level of strength for an normal result in an approved _in vitro_ assay with a minimum of 11 total pathogenic and benign variant controls (classified using these same specifications, as recommended in PMID: 31892348). Please note that an example assay with sufficient control variants has been identified in the literature, but was recommended for BS3\_Supporting instead based on OddsPath ratio (PMID: 40543502).
- **Supporting** ✅：*   BS3\_Supporting can be applied based on a normal result in at least two different approved _in vitro_ assays (from two separate approved assay classes). These are described in detail in the attached Excel file entitled “PIK3CD\_Functional\_Assays\_PS3\_BS3”.
*   Approved assay classes and specific assay instances:
    *   AKT kinase activity assay (PMID: 24136356, PMID: 24165795, PMID: 28414062)
    *   Lipid kinase activity (PMID: 24136356, PMID: 28167755, PMID: 28414062)
    *   Enrichment of the variant in high phospho-S6 and phospho-AKT T cells relative to low phospho-S6 and phospho-AKT T cells, within a next generation sequencing-based screen of donor T cells subjected to of CRISPR-mediated adenine base-editing (PMID: 40543502)
    *   Lipid vesicle affinity (PMID: 24136356)
    *   Conformational dynamics (PMID: 28167755; PMID: 28414062)
*   Please note that protein binding assays testing PIK3CD binding to PIK3R1 were also considered for inclusion in BS3\_Supporting, but were excluded based on lack of evidence of altered binding by disease-associated variants compared to wild-type controls (PMID: 24165795; PMID: 28414062).
*   Patient cell-based functional assays directly showing normal activity of the disease-relevant PI3K delta pathway were considered for inclusion in the BS3\_Supporting code but are viewed as part of the proband phenotype instead.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：*   Caution in case the phenotype is not highly specific. The patients lacking segregation must reach 6 or more points of the phenotypic scoring system described in **Table 4.**
*   Lack of segregation should be identified in more than 1 affected family member to meet BS4 at the default level of strength.
- **Supporting** ✅：*   Caution in case the phenotype is not highly specific. The patient lacking segregation must reach 6 or more points of the phenotypic scoring system described in **Table 4.**
*   BS4\_Supporting is met if only 1 affected family member lacks segregation of the genotype.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Met at the default (BP4) level by a missense variant with REVEL score less than or equal to 0.290 and CADD PHRED score less than or equal to 22.7.
*   SpliceAI Δ scores should be checked for missense variants as well. Variants with a predicted impact on splicing (SpliceAI Δ score greater than or equal to 0.2) should not be evaluated using these specifications, but rather using alternative specifications for autosomal recessive disease with a loss-of-function mechanism, unless functional evidence indicates a gain-of-function effect. The current specifications are written for a PIK3CD gain-of-function disease mechanism that has so far not been reported in association with variants that disrupt splicing.
*   Met at the default (BP4) level by a synonymous or intronic variant not predicted to impact splicing by SpliceAI (SpliceAI Δ score \<0.1, PMID: 37352859).
*   Higher strength levels of BP4\_Moderate or BP4\_Strong have not been recommended due to pilot data indicating poor performance and significant discordance between REVEL and CADD predictions for established benign and gain-of-function PIK3CD variants.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

At least two such cases are required to mitigate the reliance on assertions of variant pathogenicity in genes outside of the purview of the Antibody Deficiencies VCEP.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：*   Met for a synonymous variant if SpliceAI does not predict a splicing defect (cut-off \<0.1).
*   Synonymous variants in the first nucleotide of an exon or the final 3 nucleotides of an exon are not eligible for this code, as they are considered part of the splice region.
*   Met for an intronic variant if SpliceAI does not predict a splicing defect (cut-off \<0.1).
*   Intronic variants between +1 and +6 or between -1 and -20 are not eligible for this code, as they are considered part of the splice region (PMID: 37352859).

### 积分分类（贝叶斯点系统 / Point-Based Variant Classification）

> 本规范采用 Tavtigian et al. 2020 贝叶斯化框架（PMID: 32720330）：对每个适用证据码按其强度层级赋予 Default Point Value，累加后按下表阈值判定最终分类。

#### 最终分类点值区间（Point Based Variant Classification Categories）

| 分类 | 点值区间 |
|------|---------|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤ -7 |

#### 各证据码 Default Point Value（按强度层级）

| 证据码 | 强度层级 | 默认分值 |
|--------|---------|---------|
| PS1 | Strong | 4 |
| PS1 | Moderate | 2 |
| PS2 | Very Strong | 8 |
| PS2 | Strong | 4 |
| PS2 | Moderate | 2 |
| PS2 | Supporting | 1 |
| PS3 | Strong | 4 |
| PS3 | Moderate | 2 |
| PS3 | Supporting | 1 |
| PS4 | Strong | 4 |
| PS4 | Moderate | 2 |
| PS4 | Supporting | 1 |
| PM2 | Supporting | 1 |
| PM5 | Moderate | 2 |
| PM5 | Supporting | 1 |
| PP1 | Strong | 4 |
| PP1 | Moderate | 2 |
| PP1 | Supporting | 1 |
| PP3 | Supporting | 1 |
| PP4 | Moderate | 2 |
| PP4 | Supporting | 1 |
| BA1 | Stand Alone | -4 |
| BS1 | Strong | -4 |
| BS3 | Moderate | -2 |
| BS3 | Supporting | -1 |
| BS4 | Strong | -4 |
| BS4 | Supporting | -1 |
| BP4 | Supporting | -1 |
| BP5 | Supporting | -1 |
| BP7 | Supporting | -1 |

### 不适用证据码
PVS1、PM1、PM3、PM4、PM6、PP2、PP5、BS2、BP1、BP2、BP3、BP6
### 参考附件
- [PIK3CD_pilot_results](https://cspec.genome.network/cspec/File/id/3457f60f-028a-4cf4-9707-53a8ff44c68b/data)
- [Points system to reach final classification](https://cspec.genome.network/cspec/File/id/6ab8c5b3-d190-4162-800d-c7642738c452/data)
- [Summary_of_PIK3CD_updates](https://cspec.genome.network/cspec/File/id/1d4fcd09-a0c0-47ac-83fd-242174649f95/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN141)

# ClinGen VCEP基因特异性规范：RMRP

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN088 — Severe Combined Immunodeficiency Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0009595**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

*   Downgraded to PS1\_Supporting.
*   Applicable if a different nucleotide change at the same nucleotide position has been previously classified as pathogenic or likely pathogenic.
*   Cannot be applied if a different nucleotide change at the same position has been previously classified as benign or likely benign.
*   Previously established variants must be classified by SCID VCEP specifications for _RMRP_.

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
- **Strong** ✅：PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the Cartilage-hair hypoplasia (CHH) phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
- **Supporting** ✅：PS3\_Supporting can be applied based on an abnormal result in **at least** one approved _in vitro_ assay.

Approved assay instances:

*   Endonucleolytic cleavage activity assay (mRNA cleavage activity smaller than 0.9) 
    *   Thiel et al., 2005 (PMID: 16252239)
    *   Thiel et al., 2007 (PMID: 17701897)) **OR**
*   Luciferase reporter assay 
    *   Hermanns et al., 2005 (PMID: 16254002)) (luciferase activity higher than 7)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** ✅：*   Defined to include insertions/duplications between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). Caveat: All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM1 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent in population databases (or at extremely low frequency if recessive).

*   Downgraded to PM2\_Supporting.
*   gnomAD popmax filtering allele frequency \<0.0000447

The applicability of PM2 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use ClinGen SVI recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP.
- **Strong** ✅：Use ClinGen SVI recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP.
- **Moderate** ✅：Use ClinGen SVI recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP.
- **Supporting** ✅：Use ClinGen SVI recommendations for _in trans_ criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：*   Defined to include insertions/duplications of 6 or more nucleotides increasing the distance between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4).

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
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or

gene product (conservation, evolutionary, splicing impact, etc).

*   Use RNAsnp to access SNP effects on local RNA secondary structure ([https://rth.dk/resources/rnasnp/](https://rth.dk/resources/rnasnp/))
*   Use only for Single Nucleotide Polymorphism inside the gene (do not use for promoter sequence)
    *   Parameters utilized:
        *   Input sequence: FASTA (Ensembl NR\_\_003051.3)
        *   Insert SNP details
        *   Mode: 1
        *   Folding window: 100 nt
        *   Measure: “Distance” option
        *   Minimum length of the sequence interval: 50 
        *   Cut-off the base pair probabilities: 0.01

The p-value threshold significance should be considered 0.1 according to Sabarinathan et al., 2013. PMID: 23315997. If the value is less than 0.1, apply PP3 as a supporting level of evidence.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：A patient score of ≥2 points (see instructions below).
- **Supporting** ✅：A patient score of 1-\<2 points (see instructions below).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Common in population databases.

*   gnomAD popmax filtering allele frequency >0.00400
    *   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following parameters:
        *   Prevalence: 1:5,000
        *   Allelic heterogeneity: 1
        *   Genetic heterogeneity: 0.04 (based on the contribution of _RMRP_ variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
        *   Penetrance: 50%
    *   Use caution when applying BA1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of _RMRP_. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is greater than expected for disorder.  

*   gnomAD popmax filtering allele frequency >0.00089
    *   Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator ([https://www.cardiodb.org/allelefrequencyapp/](https://www.cardiodb.org/allelefrequencyapp/)) and the following parameters:
        *   Prevalence: 1:50,000
        *   Allelic heterogeneity: 1
        *   Genetic heterogeneity: 0.04 (based on the contribution of _RMRP_ variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
        *   Penetrance: 100%

Use caution when applying BS1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of _RMRP_. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2\_Strong: Observed in >=3 (3 or more) homozygotes in gnomAD.
- **Supporting** ✅：BS2\_Supporting: Can be applied at Supporting level of evidence if observed at least 2 homozygotes in gnomAD.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Can be applied without additional specifications. To apply the BS4 criteria, it is sufficient to have one affected family member without the segregation of the variant.

### Rules for Combining Criteria（组合规则，v1.3 浏览器实页核实 2026-05-01）

**Pathogenic**
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND ≥ 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND ≥ 2 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND 1 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）AND 1 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- ≥ 2 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND ≥ 3 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND 2 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND 1 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）AND ≥ 4 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）

**Likely Pathogenic**
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND 1 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND 1 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- ≥ 3 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）
- 2 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- 1 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）AND ≥ 4 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- 1 Very Strong（PS2_Very Strong, PM3_Very Strong）AND 1 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4）
- 1 Strong（PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong）AND 2 Moderate（PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate）

**Benign**
- ≥ 2 Strong（BS1, BS2, BS4）
- 1 Stand Alone（BA1）

**Likely Benign**
- ≥ 2 Supporting（BS2_Supporting）
- 1 Strong（BS1, BS2, BS4）

### 不适用证据码
PVS1、PS4、PM5、PP2、PP5、BS3、BP1、BP2、BP3、BP4、BP5、BP6、BP7
### 参考附件
- [PS2_PM6](https://cspec.genome.network/cspec/File/id/9cdf2f0b-5c8a-497d-bf46-466b9f9c6e91/data)
- [VCEP Comments](https://cspec.genome.network/cspec/File/id/3deb21df-c614-4b5c-bf71-73fdd990e978/data)
- [PS3_BS3](https://cspec.genome.network/cspec/File/id/21d193e9-d0c4-49b8-8f00-2521c8fc1420/data)
- [PM3](https://cspec.genome.network/cspec/File/id/f631b636-3cda-4ce7-8fa4-63135ce45093/data)
- [PP1](https://cspec.genome.network/cspec/File/id/9df6b612-bdf9-44da-b4ba-13d7475e1fe5/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN088)

# ClinGen VCEP基因特异性规范：VWF

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：GN081 v1.0 / GN090 v1.0（Released，DOI: 10.5281/zenodo.21435730 / 10.5281/zenodo.21435751，2026-10-09 官网实页核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN081 — von Willebrand Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015628**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0015629**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0015630**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0013304**（遗传方式：Undetermined mode of inheritance）
- **MONDO:0024574**（遗传方式：Other）

### 通用说明
Applying VWD type 2 variant curation guidance is complex. If you are unsure how to apply these rule specifications after reading guidance materials provided below, it may be best not to use these guidelines. Alternatively, you are welcome to submit variants for the ClinGen VWD VCEP to curate for you.            

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP.
- **Moderate** ✅：Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 4 points.
- **Strong** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 2 points.
- **Moderate** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 1 point.
- **Supporting** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**. If the proband meets **PP4\_Moderate criteria**, use a moderate or higher evidence weight (see above). See Table 1 attached. Required 0.5 point.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Either 

(1) In a transgenic animal model, must demonstrate minimal to no function.

OR

(2) The following types of assays using recombinant vWF are approved for each subtype:

Subtype 2A = A multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM, AND, to confirm this is consistent with the variant's mechanism of disease, there must be a patient harboring the variant with a clinical assay also showing loss of HMWMs. This evidence must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation.

Subtype 2B = A GP1b or platelet binding assay indicating gain of function by increased binding at low doses of ristocetin

Subtype 2M = Either (1) A GP1b or platelet binding assay OR (2) Collagen binding assay, indicating loss of function by decreased binding 

See attached spreadsheet for examples of approved assay instances to use for this rule code. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings.
- **Supporting** ✅：Subtype 2A = Either (1) a multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM. This evidence must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation. (2) a ADAMTS susceptibility assay indicating increased susceptibility relative to WT.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- VCEP Specifications：Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count proband used for PP4 in this code's proband count.
- **Very Strong** ✅：Appropriate to use code when there are 8 or more probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).
- **Strong** ✅：Appropriate to use code when there are 4-7 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).
- **Moderate** ✅：Appropriate to use code when there are 2-3 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. – all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4).
- **Supporting** ✅：Appropriate to use code when there is 1 proband that meets the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Use code for variants with a popmax MAF of \<0.0001 in gnomAD.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Use with no specification for type 2A and 2M. This rule code is not applicable to variants associated with type 2B disease, since type 2B is only associated with gain of function variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD.
- **Supporting** ✅：Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Moderate** ✅：Appropriate to use when there are multiple families each reported to have two or more meioses.
- **Supporting** ✅：Appropriate to use when there are 2 or more meioses within a single family.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.644 OR a SpliceAI score suggestive of a splicing defect (greater or equal to 0.5).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the moderate strength. See Table 2A for required and consistent laboratory values.
- **Supporting** ✅：The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the supporting strength. See Table 2B for required and consistent laboratory values.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Appropriate to use for variants with a Popmax MAF of >0.1 in gnomAD.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Appropriate to use for variants with a Popmax MAF of >0.01 in gnomAD.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.
- **Supporting** ✅：Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Use for missense variants that have a REVEL score of less than or equal to 0.290 AND SpliceAI cutoff of \<0.1. Use SpliceAI cutoff of \<0.1 for other variant types.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Use SpliceAI for splicing predictor with a cutoff score of \<0.1.

### 组合规则（Rules for Combining Criteria）

**Pathogenic（致病）**
1. 1 Very Strong (PS2_Very Strong, PS4_Very Strong) AND ≥ 1 Strong (PS1, PS2, PS3, PS4)
2. 1 Very Strong (PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)
3. 1 Very Strong (PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND 1 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
4. 1 Very Strong (PS2_Very Strong, PS4_Very Strong) AND ≥ 2 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
5. ≥ 2 Strong (PS1, PS2, PS3, PS4)
6. 1 Strong (PS1, PS2, PS3, PS4) AND ≥ 3 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)
7. 1 Strong (PS1, PS2, PS3, PS4) AND 2 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
8. 1 Strong (PS1, PS2, PS3, PS4) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)

**Likely Pathogenic（可能致病）**
1. 1 Very Strong (PS2_Very Strong, PS4_Very Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)
2. 1 Strong (PS1, PS2, PS3, PS4) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)
3. 1 Strong (PS1, PS2, PS3, PS4) AND ≥ 2 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
4. ≥ 3 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)
5. 2 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
6. 1 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)
7. 1 Strong (PS1, PS2, PS3, PS4) AND 2 Moderate (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate)

**Benign（良性）**
1. ≥ 2 Strong (BS1, BS4)
2. 1 Stand Alone (BA1)

**Likely Benign（可能良性）**
1. 1 Strong (BS1, BS4) AND 1 Supporting (BS4_Supporting, BP4, BP5, BP7)
2. ≥ 2 Supporting (BS4_Supporting, BP4, BP5, BP7)

### 不适用证据码
PVS1、PM1、PM3、PM6、PP2、PP5、BS2、BS3、BP1、BP2、BP3、BP6
### 参考附件
- [VWD type 2 PP4 rule guidance](https://cspec.genome.network/cspec/File/id/dea48cd6-39c3-46e5-838b-95f9bf4a17c7/data)
- [VWD 2A/2M/2N functional assays](https://cspec.genome.network/cspec/File/id/4a9767d1-02b0-4c99-a48a-db5bd1f217a7/data)
- [Introduction to von Willebrand disease](https://cspec.genome.network/cspec/File/id/0b35bd27-74c1-4a69-96c3-f7da441da93d/data)
- [VWD type 2 PS2/PM6 rule guidance](https://cspec.genome.network/cspec/File/id/9d75b4b0-6c9e-4613-bbf4-6ad671629204/data)
- [VWD type 2 List of Approved Functional Assays](https://cspec.genome.network/cspec/File/id/53d4d3a4-324c-4b89-998a-77f6e3a724d9/data)
- [VWD Type 2 Rule Set Instructions for Use](https://cspec.genome.network/cspec/File/id/415ddbc7-0e4c-4442-b8f6-899c71e4a118/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN081)

## 规范 2：GN090 — von Willebrand Disease  Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015631**（遗传方式：Autosomal recessive inheritance）

### 通用说明
Applying VWD type 2 variant curation guidance is complex. If you are unsure how to apply these rule specifications after reading guidance materials provided below, it may be best not to use these guidelines. Alternatively, you are welcome to submit variants for the ClinGen VWD VCEP to curate for you.

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP.
- **Moderate** ✅：Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：4 points required for Very Strong strength. See de novo rule code guidance.
- **Strong** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 2 points.
- **Moderate** ✅：Use proposed SVI point recommendations for **“Phenotype consistent with gene but not highly specific”** if the proband meets **PP4 criteria**.  Use **“Phenotype highly specific for gene”** phenotype consistency if the proband meets **PP4\_Moderate criteria**. See Table 1 attached. Required 1 point.
- **Supporting** ✅：0.5 points required for Supporting strength. If the proband has PP4 at a Moderate level, this can be elevated from Supporting to Moderate. See de novo rule code guidance.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Either (1) in a transgenic animal model, must demonstrate minimal to no function. (2) a Factor VIII binding assay using recombinant vWF resulting in decreased binding compared to WT.

See attached spreadsheet for examples of approved assay instances to use for this rule code. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Use code for variants with a popmax MAF of \<0.005 in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 4 points required.
- **Strong** ✅：Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 2 points required.
- **Moderate** ✅：Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 1 point required.
- **Supporting** ✅：Use SVI recommended point system for this code for probands with a VWD type 2N diagnosis. Total of 0.5 points required.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Use with no specification.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD.
- **Supporting** ✅：Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Appropriate to use when a proband has three affected family members.
- **Moderate** ✅：Appropriate to use when a proband has two affected family members.
- **Supporting** ✅：Appropriate to use when a proband has one affected family member.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.644 OR a SpliceAI score suggestive of a splicing defect (greater or equal to 0.5).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code, including a low factor VIII activity level and evidence of decreased VWF:FVIII binding.

Additional consistent information should be noted but is not required, including either normal or low VWF:Ag, normal high molecular weight multimers, and sequencing with duplication/deletion analysis of the F8 gene.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Appropriate to use for variants with a Popmax MAF of >0.1 in gnomAD.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Appropriate to use for variants with a Popmax MAF of >0.01 in gnomAD.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.

- **Supporting** ✅：Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family.
#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Use for missense variants that have a REVEL score of less than or equal to 0.290 AND SpliceAI cutoff of \<0.1. Use SpliceAI cutoff of \<0.1 for other variant types.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Use SpliceAI for splicing predictor with a cutoff score of 0.

### 组合规则（Rules for Combining Criteria）

**Pathogenic（致病）**
1. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong)
2. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)
3. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND 1 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
4. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
5. ≥ 2 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong)
6. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND ≥ 3 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)
7. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND 2 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
8. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)

**Likely Pathogenic（可能致病）**
1. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)
2. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND 1 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)
3. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND ≥ 2 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
4. ≥ 3 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)
5. 2 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
6. 1 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)
7. 1 Strong (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND 2 Moderate (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate)

**Benign（良性）**
1. ≥ 2 Strong (BS1, BS4)
2. 1 Stand Alone (BA1)

**Likely Benign（可能良性）**
1. 1 Strong (BS1, BS4) AND 1 Supporting (BS4_Supporting, BP4, BP5, BP7)
2. ≥ 2 Supporting (BS4_Supporting, BP4, BP5, BP7)

### 不适用证据码
PVS1、PS4、PM1、PM6、PP2、PP5、BS2、BS3、BP1、BP2、BP3、BP6
### 参考附件
- [VWD 2N functional assays](https://cspec.genome.network/cspec/File/id/3fbbad47-dd80-472c-bc3e-5a768e192d32/data)
- [VWD Type 2 Rule Set Instructions for Use](https://cspec.genome.network/cspec/File/id/eba67e6a-0cf4-4dbe-a2ea-a03a47cff376/data)
- [VWD type 2 PS2/PM6 rule guidance](https://cspec.genome.network/cspec/File/id/378b6be7-de88-4b05-8f2a-2ea1c9490a92/data)
- [SVI Recommendations for PM3](https://cspec.genome.network/cspec/File/id/4ff377ef-64f1-4445-9848-7287313e593a/data)
- [Intro the VWD](https://cspec.genome.network/cspec/File/id/1fb6620c-7cad-49ce-a70e-0c3be70df837/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN090)

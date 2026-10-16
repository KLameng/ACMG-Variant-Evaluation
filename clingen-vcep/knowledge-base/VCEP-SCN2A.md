# ClinGen VCEP基因特异性规范：SCN2A

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN068 — Epilepsy Sodium Channel Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100038**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Please disregard section on "Rules for combining criteria" section. Instead, please refer to "Combining Rules" attachment, as we have incorporated the points-based system. 

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- VCEP Specifications：
 * Most terminal codon expected to undergo nonsense-mediated decay: p.Thr1591
 * For splice sites, this criterion should not be applied with PP3.
- **Very Strong** ✅：Follow SVI guidance per workflow in Tayoun et al (2018), included as “PVS1 Decision Tree”.
- **Strong** ✅：Follow SVI guidance per workflow in Tayoun et al (2018), included as “PVS1 Decision Tree”.
- **Moderate** ✅：Follow SVI guidance per workflow in Tayoun et al (2018), included as “PVS1 Decision Tree”.
- **Supporting** ✅：Follow SVI guidance per workflow in Tayoun et al (2018), included as “PVS1 Decision Tree”.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same/identical amino acid change as previously reported (Caveat: beware of changes that impact splicing rather than at the amino acid/protein level).

*   Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.
*   **\>1** Identical amino acid change in paralogous gene previously established as **Pathogenic or Likely Pathogenic**, including NDD genes with equivalent constraint scores (SCN1A, SCN2A, SCN3A, SCN8A). See Paralogous Gene Table for corresponding amino acid positions.

Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al, 2023). 

*   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker, et al (2023) PMID: 37352859, also provided as a supplement ("PS1\_Variants impacting splicing").
- **Moderate** ✅：Same/identical amino acid change as previously reported (Caveat: beware of changes that impact splicing rather than at the amino acid/protein level).

*   Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al, 2023).

*   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker, et al (2023) PMID: 37352859, also provided as a supplement ("PS1\_Variants impacting splicing").
- **Supporting** ✅：Same/identical amino acid change as previously reported (Caveat: beware of changes that impact splicing rather than at the amino acid/protein level).

*   A single identical amino acid change in a paralogous gene previously established as **Pathogenic or Likely Pathogenic**, including NDD genes with equivalent constraint scores (SCN1A, SCN2A, SCN3A, SCN8A). See Paralogous Gene Table for corresponding amino acid positions.

Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al, 2023).

*   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker, et al (2023) PMID: 37352859, also provided as a supplement ("PS1\_Variants impacting splicing").

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Points based system for each unrelated proband determined by phenotypic specificity. Total of **4 points** will arrive at **Very Strong**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Points based system for each unrelated proband determined by phenotypic specificity. Total of **2 points** will arrive at **Strong**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Points based system for each unrelated proband determined by phenotypic specificity. Total of **1 point** will arrive at **Moderate**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Supporting** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Points based system for each unrelated proband determined by phenotypic specificity. Total of **0.5 points** will arrive at **Supporting**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：*   In patch clamping experiments: Peak current as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is less than or equal to 72.7% of wildtype.
*   In patch clamping experiments: Persistent current as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is greater than or equal to 135% of wildtype.
*   In patch clamping experiments: Voltage dependence of activation as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is shifted by at least 2.2 mV (absolute value).
*   In patch clamping experiments: Voltage dependence of inactivation as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is shifted by at least 4.1 mV (absolute value).
*   Mouse knock-in model displays spontaneous seizures.
- **Moderate** ✅：*   In patch clamping experiments: Peak current as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is less than or equal to 80.6% of wildtype.
*   In patch clamping experiments: Persistent current as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is greater than or equal to 125% of wildtype.
*   In patch clamping experiments: Voltage dependence of activation as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is shifted by at least 2.1 mV (absolute value).
*   In patch clamping experiments: Voltage dependence of inactivation as defined by FENICS ontology ([https://bioportal.bioontology.org/ontologies/FENICS](https://bioportal.bioontology.org/ontologies/FENICS)) is shifted by at least 3.0 mV (absolute value).
*   Zebrafish knock-in model displays spontaneous seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies
- **Supporting** ✅：Zebrafish knock-in model displays induced seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Present in multiple unrelated patients with consistent phenotypes and absent in controls. Points based system for each unrelated proband determined by phenotypic specificity. Total of **16+ points** will arrive at **Very Strong**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points
- **Strong** ✅：Present in multiple unrelated patients with consistent phenotypes and absent in controls. Points based system for each unrelated proband determined by phenotypic specificity. Total of **4 - 15.5 points** will arrive at **Strong**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points
- **Moderate** ✅：Present in multiple unrelated patients with consistent phenotypes and absent in controls. Points based system for each unrelated proband determined by phenotypic specificity. Total of **2 - 3.5 points** will arrive at **Moderate**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points
- **Supporting** ✅：Present in multiple unrelated patients with consistent phenotypes and absent in controls. Points based system for each unrelated proband determined by phenotypic specificity. Total of **1 - 1.5 points** will arrive at **Supporting**. 

*   Complex Neurodevelopmental Disorder: 1 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Variant is located within a Pathogenic Enriched Region. See specific amino acid residues noted in the attached “PM1 Table".

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：One or fewer alleles, if a minimum of 10,000 alleles assessed in population databases, such as the Genome Aggregation Database (gnomAD). Caveat: Population data for indels may be poorly called by next generation sequencing.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- Rule Combining Stipulation：If PM5_Strong is reached, and the variant falls within a PM1 region, then do not add PM1 with PM5_Strong.
- **Strong** ✅：Greater than or equal to 2 known pathogenic variants at same site as novel change (within the same gene).

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Novel missense change at an amino acid residue where a different missense change determined to be Pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：*   Novel missense change at an amino acid residue where a different missense change determined to be **Likely Pathogenic** has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. 
*   \>1 Non-Identical aa change in paralogous gene(s) where a different missense change determined to be **Pathogenic**or **Likely Pathogenic**, including NDD genes with equivalent constraint scores (SCN1A, SCN2A, SCN3A, SCN8A)

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：Assumed de novo, but without confirmation of paternity and maternity. Points based system for each unrelated proband determined by phenotypic specificity. Total of **2 points** will arrive at **Strong**. Total of **4 points** will arrive at **Very Strong**. 

*   Complex Neurodevelopmental Disorder: 0.5 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity. Points based system for each unrelated proband determined by phenotypic specificity. Total of **1 point** will arrive at **Moderate**. 

*   Complex Neurodevelopmental Disorder: 0.5 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points
- **Supporting** ✅：Assumed de novo, but without confirmation of paternity and maternity. Points based system for each unrelated proband determined by phenotypic specificity. Total of **0.5 points** will arrive at **Supporting**. 

*   Complex Neurodevelopmental Disorder: 0.5 points
*   Other phenotypes not consistent w/neurodevelopmental disorder: 0 points

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：\>=7 independent meioses
- **Moderate** ✅：5-6 independent meioses
- **Supporting** ✅：3-4 independent meioses

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Follow ClinGen’s recommendations ([PMID: 36413997](https://pubmed.ncbi.nlm.nih.gov/36413997/)), using REVEL as the computational tool, with the following stipulations:

1.  Strength should be capped at Moderate, and 
2.  limit the combination of PP3 and PM1 to reach no higher than strong
- **Supporting** ✅：Follow ClinGen’s recommendations ([PMID: 36413997](https://pubmed.ncbi.nlm.nih.gov/36413997/)), using REVEL as the computational tool, with the following stipulations:

1.  Strength should be capped at Moderate, and 
2.  limit the combination of PP3 and PM1 to reach no higher than strong

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency is above **0.01%** is gnomAD or other large population databases, must be greater than or equal to 5 alleles if a minimum of 10,000 alleles was assessed.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is above 0.0002% in GnomAD or other large population database, must be greater than or equal to 5 alleles if a minimum of 10,000 alleles was assessed.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual with full penetrance expected at an early age.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In frame-deletions/insertions in a repetitive region without a known function.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Follow ClinGen’s recommendations ([PMID: 36413997](https://pubmed.ncbi.nlm.nih.gov/36413997/)) using REVEL as the computational tool.
- **Supporting** ✅：Follow ClinGen’s recommendations ([PMID: 36413997](https://pubmed.ncbi.nlm.nih.gov/36413997/)) using REVEL as the computational tool.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### 不适用证据码
PM3、PP2、PP4、PP5、BS3、BS4、BP1、BP6
### 参考附件
- [Paralogous Gene Table](https://cspec.genome.network/cspec/File/id/01b67f25-bf59-454c-afbf-4075fff58bba/data)
- [PVS1_Decision Tree](https://cspec.genome.network/cspec/File/id/0ef06d92-cc62-4a9b-84a4-216020c4f7f4/data)
- [PVS1 alt transcripts &amp; exon numbering](https://cspec.genome.network/cspec/File/id/f1c91760-6209-46e5-a1c8-1eeb691ff4e5/data)
- [PS1_Variants impacting splicing](https://cspec.genome.network/cspec/File/id/1d7c5c99-f1e3-41f0-b15e-613ac20480b8/data)
- [Combining Rules](https://cspec.genome.network/cspec/File/id/af718212-77e8-4e3f-9118-67120d58795d/data)
- [PM1 Table](https://cspec.genome.network/cspec/File/id/d34cd4c0-577e-4844-9497-69cb691aa85d/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN068)

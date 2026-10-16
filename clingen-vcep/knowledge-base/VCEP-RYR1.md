# ClinGen VCEP基因特异性规范：RYR1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN012 — Malignant Hyperthermia Susceptibility Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0018493**（遗传方式：未指定）

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change
 * Previously established pathogenic variant must reach a classification of pathogenic without PS1
- **Moderate** ✅：Same amino acid change as a previously established likely pathogenic variant regardless of nucleotide change.
 * Previously established likely pathogenic variant must reach a classification of likely pathogenic without PS1.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, ≥8 points
- **Strong** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 4-7 points
- **Moderate** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 2-3 points
- **Supporting** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 1 point

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established functional studies supportive of a damaging effect on protein function
 * Knock-in mouse showing MH reaction in response to RYR1 agonist AND increased sensitivity to RYR1 agonists in ex vivo tisue/cells
- **Moderate** ✅：Well-established functional studies supportive of a damaging effect on protein function
 * Increased sensitivity to RYR1 agonist in HEK293 in vitro assay, Ca2+ release significantly increased compared to WT, controls to include known pathogenic and benign variants, n≥3.
 * Three or more independent ex vivo studies all showing release of Ca2+ in response to RYR1 agonist
 * Knock-in mouse showing MH reaction in response to RYR1 agonist OR increased sensitivity to RYR1 agonists in ex vivo tissue/cells (but not both, which would be PS3_strong)
- **Supporting** ✅：Well-established functional studies supportive of a damaging effect on protein function
 * Two independent ex vivo studies all showing release of Ca2+ in response to RYR1 agonist

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals significantly increased compared with the prevalence in controls.
* ≥7 MH case points. Probands with a personal or family history of an MH event are awarded 0.5 points, probands with a personal or family history of a positive (MHS) IVCT/CHCT are awarded an additional 0.5 points. Probands with multiple variants in RYR1 classified as VUS, likely pathogenic or pathogenic are not considered. Popmax in gnomAD ≤0.00006.
 * For variants with popmax MAF gnomAD >0.00006, an odds ratio of ≥18.7 when comparing MH case points to allele count in gnomAD can qualify. Popmax in gnomAD must be <0.0038.
- **Moderate** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
*  2-6 MH case points. Probands with a personal or family history of an MH event are awarded 0.5 points, probands with a personal or family history of a positive (MHS) IVCT/CHCT are awarded an additional 0.5 points. Probands with multiple variants in RYR1 classified as VUS, likely pathogenic or pathogenic are not considered. Popmax in gnomAD ≤0.00006.
* For variants with popmax MAF in gnomAD >0.00006, an odds ratio of ≥4.33 when comparing MH case points to allele count in gnomAD can qualify. Popmax in gnomAD must be <0.0038.
- **Supporting** ✅：The prevalence of the variant in affected individuals is significantly increased compared withthe prevalence in controls.
*  1 MH case point. Probands with a personal or family history of an MH event are awarded 0.5 points, probands with a personal or family history of a positive (MHS) IVCT/CHCT are awarded an additional 0.5 points. Probands with multiple variants in RYR1 classified as VUS, likely pathogenic or pathogenic are not considered. Popmax in gnomAD ≤0.00006.
For variants with popmax MAF in gnomAD >0.00006, an odds ratio of ≥2.08 when comparing MH case points to allele count in gnomAD can qualify. Popmax in gnomAD must be <0.0038.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well established functional domain.
* Residues 1-552 (N-terminal region) and 2,101-2,458 (central region) 
* PM1 should not be applied at a moderate weight with PS1/PM5, see PM1_Supporting.
- **Supporting** ✅：Located in a mutational hot spot and/or critical and well established functional domain.
* Residues 1-552 (N-terminal region) and 2,101-2,458 (central region), if PS1/PM5 applicable then PM1 should be used at supporting 
* Residues 4,631-4,991 (C-terminal region).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense varaint previously determined to be pathogenic
 * Previously established pathogenic variant must reach a classification of pathogenicity without PM5
 * Grantham score for alternate pathogenic variant must be less than for variant being assessed
- **Supporting** ✅：Missense change at an amino acid residue where a different missense variant previously determined to be pathogenic.
 * Previously established likely pathogenic variant can be considered supporting evidence, must reach a classification of likely pathogenic without PM5.
 * Grantham score for alternate likely pathogenic variant must be less than for variant being assessed.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, ≥8 points
- **Strong** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 4-7 points
- **Moderate** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 2-3 points
- **Supporting** ✅：Each proven de novo case, 2 points, each assumed de novo case, 1 point, a total of 1 point

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in ≥7 reported meioses
- **Moderate** ✅：Co-segregation with disease in 5-6 reported meioses
- **Supporting** ✅：Co-segregation with disease in 3-4 reported meioses

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product
 * Use REVEL score of >0.85

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Popmax allele frequency >0.0038 (0.38%)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Popmax allele frequency >0.0008 (0.08%)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder with full penetrance expected at an early age.
 * Two or more variant positive individuals with a negative IVCT/CHCT test
- **Moderate** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder with full penetrance expected at an early age.
 * One variant positive individual with a negative IVCT/CHCT test

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** ✅：Well-established functional studies show no damaging effect on protein function
 * Three or more independent ex vivo studies, NO significant release of Ca2+ in response to agonist
- **Supporting** ✅：Well-established functional studies show no damaging effect on protein function
 * No significant increased sensitivity to RYR1 agonist in an approved in vitro assay, Ca2+ release measured, n≥3
 * One or two independent ex vivo studies, NO significant release of Ca2+ in response to agonist
 * Knock-in mouse showing no MH reaction in response to RYR1 agonist AND no increased sensitivity to RYR1 agonists in ex vivo tissue/cells

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in cis with a pathogenic variant in any inheritance pattern

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Computational evidence suggest no impact on gene or gene product, REVEL score of <0.5

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved

### 不适用证据码
PVS1、PM2、PM3、PM4、PP2、PP4、PP5、BS4、BP1、BP3、BP5、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN012)

## 规范 2：GN150 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100150**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Note on multiple MOIs: In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it’s de novo, it’s much more likely to be AD and if it’s observed with a second variant, it’s much more likely to be AR. In general, loss of function variants are almost always associated with AR disease. If two missense variants are identified in trans, individuals are much more likely to have central core or minicore disease. Malignant hyperthermia is only associated with AD variants. However, there have been some examples of a missense MH variant in trans with a LOF variant, causing a blended phenotype of myopathy and MH susceptibility. The AD and AR specifications are listed separately. 
            
            

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：No change - use as originally described
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength.
- **Moderate** ✅：Some of the assays from PS3\_Supporting may be stacked to reach a Moderate Strength. One specific assay is currently suggested to be applied at Moderate:

Calcium Release\*\*: An abnormal readout consists of increased calcium release compared to controls or WT RYR1.

**\*\*Calcium Release assays and Single Channel Activity assays should not be stacked because they may not be assessing independent biological function.**
- **Supporting** ✅：Two specific assays are currently suggested to be applied at Supporting:

1.  Single Channel Activity\*\*: An abnormal readout consists of increased opening probability compared to controls or WT RYR1.
2.  Calstabin1/FKBP12 Binding: An abnormal readout consists of significantly reduced RYR1-FKBP12 binding compared to controls or WT RYR1.

If not listed above, it is acceptable to use PS3\_Supporting for other functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

**\*\*Calcium Release assays and Single Channel Activity assays should not be stacked because they may not be assessing independent biological function.**

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

RYR1 is associated with both autosomal recessive and autosomal dominant disease. If you are curating biallelic observations, please use the AR specifications. For case counting for AD disease, please see the PS4 chart.

at least 1 point, please see PS4 chart
- **Moderate** ✅：0.5 points, please see PS4 chart
- **Supporting** ✅：0.25 points, please see PS4 chart

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：The pore/transmembrane region of RYR1 is critical for protein function and missense variants that fall within this region (amino acids 4800-4950)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is absent (1 allele allowed) for autosomal dominant

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Supporting** ✅：No change - use as originally described

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：No change - use as originally described

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.
- **Supporting** ✅：No change - use as originally described

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：See segregation chart
- **Moderate** ✅：See segregation chart
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

See segregation chart

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.0000486** **for AD variants**. All populations used should have at least 2000 alleles and >1 observation. 

**BA1 exclusion variants** (well-known pathogenic variants that are above the specified BA1 or BS1 threshold) are as follows: 

NM\_000540.3:c.14524G>A (p.Val4842Met)

NM\_000540.3:c.325C>T (p.Arg109Trp)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.00000486 for AD variants**. All populations used should have at least 2000 alleles and >1 observation. 

**BA1/BS1 exclusion variants** (well-known pathogenic variants that are above the specified BA1 or BS1 threshold) are as follows: 

NM\_000540.3:c.14524G>A (p.Val4842Met)

NM\_000540.3:c.325C>T (p.Arg109Trp)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc) Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

BP4 is met if the REVEL score ≤ 0.15 or if the variant is not predicted to impact splicing using SpliceAI.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### Rules for Combining Criteria（组合规则）

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS3_Very Strong, PS4_Very Strong, PM3_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PS3_Very Strong, PS4_Very Strong, PM3_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS3_Very Strong, PS4_Very Strong, PM3_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND 1 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Very Strong (PVS1, PS2_Very Strong, PS3_Very Strong, PS4_Very Strong, PM3_Very Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS3_Very Strong, PS4_Very Strong, PM3_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)
- 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong) AND 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)
- ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)

### 不适用证据码
PVS1、PM3、PP2、PP4、PP5、BS3、BP1、BP3、BP6
### 参考附件
- [PS4 specification for RYR1_AD](https://cspec.genome.network/cspec/File/id/69f12669-eaf5-4f50-b193-9412a55453e8/data)
- [RYR1 approved functional assays](https://cspec.genome.network/cspec/File/id/2b389edc-5d4d-4c16-b3c0-26ec5d57aeaf/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN150)

## 规范 3：GN179 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100150**（遗传方式：Autosomal recessive inheritance）

### 通用说明
 Note on multiple MOIs: In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it’s de novo, it’s much more likely to be AD and if it’s observed with a second variant, it’s much more likely to be AR. In general, loss of function variants are almost always associated with AR disease. If two missense variants are identified in trans, individuals are much more likely to have central core or minicore disease. Malignant hyperthermia is only associated with AD variants. However, there have been some examples of a missense MH variant in trans with a LOF variant, causing a blended phenotype of myopathy and MH susceptibility. The AD and AR specifications are listed separately.            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Strong** ✅：In-frame deletions or in frame exon-skipping variants in the pore/transmembrane region of RYR1 should be scored at PVS1\_strong. (Amino acids 4800-4950, Exons 100-103)
- **Moderate** ✅：See PVS1 flowchart
- **Supporting** ✅：See PVS1 flowchart

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：No change - use as originally described
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength.
- **Supporting** ✅：There are no specified functional assay for AR RYR1-related myopathy. However, it is acceptable to use PS3\_Supporting for other functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：The pore/transmembrane region of RYR1 is critical for protein function and missense variants that fall within this region (amino acids 4800-4950)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is 

 ≤ 0.00000697 for autosomal recessive

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：4.0 points per the PM3 chart
- **Strong** ✅：2.0 points per the PM3 chart
- **Moderate** ✅：For recessive disorders, detected in trans with a pathogenic variant Note: This requires testing of parents (or offspring) to determine phase.

1.0 points per the PM3 chart
- **Supporting** ✅：0.5 points per the PM3 chart

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Supporting** ✅：No change - use as originally described

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：No change - use as originally described

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.
- **Supporting** ✅：No change - use as originally described

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：See segregation chart
- **Moderate** ✅：See segregation chart
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

See segregation chart

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：**To meet PP4, a congenital myopathy testing panel should be performed without identification of other causative variants and AT LEAST TWO of these features should be present**

*   **Presence on Muscle Biopsy of:** mini cores or central cores (histology or electron microscopy)
*   Exercise, heat, or anesthetic induced rhabdomyolysis
*   Ophthalmoplegia
*   Characteristic muscle imaging (see Figure 8, Saade et al 2019 PMID: 31060725)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.00697** **for AR variants**. All populations used should have at least 2000 alleles and >1 observation. 

**BA1 exclusion variants** (well-known pathogenic variants that are above the specified BA1 or BS1 threshold) are as follows: 

NM\_000540.3:c.6721C>T (p.Arg2241Ter)

NM\_000540.3:c.10348-6C>G

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.000697 for AR variants**. All populations used should have at least 2000 alleles and >1 observation. 

**BA1/BS1 exclusion variants** (well-known pathogenic variants that are above the specified BA1 or BS1 threshold) are as follows: 

NM\_000540.3:c.6721C>T (p.Arg2241Ter)

NM\_000540.3:c.10348-6C>G

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc) Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

BP4 is met if the REVEL score ≤ 0.15 or if the variant is not predicted to impact splicing using SpliceAI.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### Rules for Combining Criteria（组合规则）

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) AND 1 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- ≥ 3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)
- 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) AND 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)
- ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)

### 不适用证据码
PS4、PP2、PP5、BS3、BP1、BP3、BP6
### 参考附件
- [PM3 chart](https://cspec.genome.network/cspec/File/id/9db3efe0-318e-4873-89a2-bd453b846723/data)
- [PVS1 decision tree for RYR1](https://cspec.genome.network/cspec/File/id/6bd4b92c-3bbe-4031-bc1b-d89447e9ddfb/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN179)

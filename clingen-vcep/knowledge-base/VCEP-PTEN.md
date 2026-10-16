# ClinGen VCEP基因特异性规范：PTEN

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN003 — PTEN Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0017623**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Minor Changes:
1. Correct SpliceAI cutoff for BP4 rule   
2. Correct the Rules for Combining Criteria
3. Add BLOSUM matrix, Cleveland Clinic core and Pediatric score tables
4. Added disease name, MOI and added underscores for some greater than symbols
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use PTEN PVS1 decision tree.
- **Strong** ✅：Use PTEN PVS1 decision tree.
- **Moderate** ✅：Use PTEN PVS1 decision tree.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change OR different variant at same nucleotide position as a pathogenic splicing variant, where in silico models predict impact equal to or greater than the known pathogenic variant.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Two proven OR four assumed OR one proven + two assumed de novo observations in a patient with the disease and no family history.
- **Strong** ✅：De novo (both maternity and paternity confirmed) observation in a patient with the disease and no family history.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene or gene product.

*   RNA, mini-gene, or other assay shows impact on splicing
- **Moderate** ✅：Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene or gene product.

*   Phosphatase activity ≤ -1.11 per Mighell et al. 2018, PMID: 29706350.
- **Supporting** ✅：Phosphatase activity \<50% of wild-type or abnormal _in vitro_ cellular assay or transgenic model with phenotype different from wild type that does not meet PS3\_moderate.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Probands with specificity score ≥16 (see text).
- **Strong** ✅：Probands with specificity score 4-15.5 (see text) OR The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
- **Moderate** ✅：Probands with specificity score of 2-3.5 (see text).
- **Supporting** ✅：Phenotype specific for disease with single genetic etiology. Proband(s) with specificity score of 1-1.5 (see text).

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain. Defined to include residues in catalytic motifs: 90-94, 123-130, 166-168 (NP_ 000305.3)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent in population.

*   Databases present at <0.00001 (0.001%) allele frequency in gnomAD or another large sequenced population. If multiple alleles are present within any subpopulation, allele frequency in that subpopulation must be <0.00002 (0.002%).

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Applies to in-frame insertions or deletions impacting at least one residue in a catalytic motif (see PM1), and variants causing protein extension.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic or likely pathogenic has been seen before. In addition, variant being interrogated must have BLOSUM62 score equal to or less than the known variant.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** ✅：Two proven OR four assumed OR one proven + two assumed de novo observations in a patient with the disease and no family history.
- **Strong** ✅：Two probands with presumed _de novo_ occurrence (maternity/ paternity not confirmed) with the disease and no family history.

*   May also be used for a proband with presumed de novo occurrence for an individual with a highly specific phenotype (meets criteria to count towards PS4)
- **Moderate** ✅：Assumed _de novo,_ but without confirmation of paternity and maternity, in proband with the disease and no family history.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members, with ≥7 meioses observed across at least two families.
- **Moderate** ✅：Co-segregation with disease in multiple affected family members, with 5 or 6 meioses observed.
- **Supporting** ✅：Co-segregation with disease in multiple affected family members, with 3 or 4 meioses observed.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

*   Splicing variants: Concordance of SpliceAl and VarSeak
*   Missense variants: REVEL score > 0.7

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：gnomAD Filtering allele frequency >0.00056 (0.056%)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：gnomAD Filtering allele frequency from 0.000043 (0.0043%) up to 0.00056 (0.056%)
- **Supporting** ✅：Allele frequency from 0.0000043 (0.00043%) up to 0.000043 (0.0043%).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in the homozygous state in a healthy or PHTS-unaffected individual. One observation if homozygous status confirmed, two if not confirmed. To be applied at supporting evidence level if BS1 is also applied.
- **Supporting** ✅：Two homozygous observations with no clinical data provided, or meets criteria for BS2 but BS1 is also applied.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established _in vitro_ or _in vivo_ functional studies shows no damaging effect on protein function. To be applied to intronic or synonymous variants, RNA, mini-gene or other splicing assay demonstrating no splicing impact.
- **Supporting** ✅：_In vitro_ or _in vivo_ functional study or studies showing no damaging effect on protein function.

*   Phosphatase activity >0 per Mighell et al. 2018, PMID: 29706350.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of two or more families.
- **Supporting** ✅：Lack of segregation in affected members of one family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic or likely pathogenic PTEN variant OR at least three observations in cis and/or phase unknown with different pathogenic/likely pathogenic PTEN variants.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product. 

*   Splicing variants: Concordance of SpliceAl and VarSeak
*   Missense variants: REVEL scores \< 0.5

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease. Other gene/disorder must be considered highly penetrant AND patient’s personal/family history must demonstrate no overlap between other gene and PTEN.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) or intronic variant at or beyond +7/-21 for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice.

### Rules for Combining Criteria

#### Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)

#### Likely Pathogenic
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)

#### Benign
- ≥ 2 Strong (BS1, BS2, BS3, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- ≥ 2 Supporting (BS1_Supporting, BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)
- 1 Strong (BS1, BS2, BS3, BS4)

### 不适用证据码
PM3、PP4、PP5、BP1、BP3、BP6
### 参考附件
- [PVS1_DecisionTree](https://cspec.genome.network/cspec/File/id/def954a2-8224-4670-a67a-270b191af1d5/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN003)

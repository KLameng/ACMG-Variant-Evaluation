# ClinGen VCEP基因特异性规范：APC

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN089 — InSiGHT Hereditary Colorectal Cancer/Polyposis Variant Curation Expert Panel

> 官网版本：Version 2.1；DOI: 10.5281/zenodo.21434150；核验日期：2026-10-09

### 覆盖疾病
- **MONDO:0021056**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant in a gene where LOF is a known mechanism of disease. As per modified decision tree (**Figure 1**) \[Reference 1\].
- **Strong** ✅：Null variant in a gene where LOF is a known mechanism of disease. As per modified decision tree (**Figure 1**) \[Reference 1\].
- **Moderate** ✅：Null variant in a gene where LOF is a known mechanism of disease. As per modified decision tree (**Figure 1**) \[Reference 1\].
- **Supporting** ✅：Null variant in a gene where LOF is a known mechanism of disease. As per modified decision tree (**Figure 1**) \[Reference 1\].

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：The previously established variant was classified as Pathogenic according to the APC-specific modifications.

This criterion can be applied to both missense and splice variants in _APC_. 

**Missense variants:** when the variant under assessment results in the same amino acid change as previously established Pathogenic variant(s). 

There are currently only two Likely Pathogenic missense variants: c.3077A>G p.(Asn1026Ser) and c.3084T>A p.(Ser1028Arg). Other variants leading to the same missense change at these positions meet PS1\_Moderate. No missense variant has been classified as Pathogenic based on current evidence. 

**Splice variants**: when the variant under assessment affects splicing at the same nucleotide as a previously established Pathogenic variant. The splice prediction must be above defined thresholds (SpliceAI: loss ≥0.8, gain ≥0.2, see instructions) or similar to the previously established variant by multiple _in silico_ predictors.
- **Moderate** ✅：The previously established variant was classified as Likely Pathogenic according to the APC-specific modifications.

This criterion can be applied to both missense and splice variants in _APC_. 

**Missense variants:** when the variant under assessment results in the same amino acid change as previously established Likely Pathogenic variant(s). 

There are currently only two Likely Pathogenic missense variants: c.3077A>G p.(Asn1026Ser) and c.3084T>A p.(Ser1028Arg). Other variants leading to the same missense change at these positions meet PS1\_Moderate. No missense variant has been classified as Pathogenic based on current evidence. 

**Splice variants**: when the variant under assessment affects splicing at the same nucleotide as a previously established Likely Pathogenic variant. The splice prediction must be above defined thresholds (SpliceAI: loss ≥0.8, gain ≥0.2, see instructions) or similar to the previously established variant by multiple _in silico_ predictors.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：≥ 4 _de novo_ scores. For curation of _de novo_ score see **Tables 1** and **2**.
- **Strong** ✅：2-3.5 _de novo_ scores. For curation of _de novo_ score see **Tables 1** and **2**.
- **Moderate** ✅：1-1.5 _de novo_ score. For curation of _de novo_ score see **Tables 1** and **2**.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Very Strong** ✅：**RNA assays** show

1.  a premature stop codon  
    OR
2.  inframe skipping of exon 13 or 14

**AND** the absence of full-length transcript.
- **Strong** ✅：**RNA assays** show

1.  a premature stop codon  
    **OR**
2.  inframe skipping of exon 13 or 14

**AND** \< 10% of full-length transcript.
- **Moderate** ✅：**RNA assays** show 

1.  a premature stop codon AND reports of exon deletion/skipping/loss, insertion of intronic nucleotides  
    **OR**
2.  inframe skipping of exon 13 or 14 AND reports of exon deletion/skipping/loss, insertion of intronic nucleotides  
    **OR**
3.  other inframe skipping AND absent or \< 10% full-length transcript.
- **Supporting** ✅：**RNA assays** show 

1.  inframe skipping of exons other than exon 13 or 14 AND reports of exon deletion/skipping/loss, insertion of intronic nucleotides  
    **OR**
2.  over-expression of an alternative transcript (exons 10, 11 or 15)

**Protein assays** show

Increased β-catenin regulated transcription activity and/or decreased binding to β-catenin by surface plasmon resonance (only for variants within the β-catenin binding domain, which refers to codons 959-2129 of _APC_) \[Reference 2\].

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：≥ 16 phenotype points. For phenotype points curation see **Table 1**.
- **Strong** ✅：4-15.5 phenotype points. For phenotype points curation see **Table 1**.
- **Moderate** ✅：2-3.5 phenotype points. For phenotype points curation see **Table 1**.
- **Supporting** ✅：1-1.5 phenotype point. For phenotype points curation see **Table 1**.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Rare in controls, defined by an allele frequency ≤ 0.0003% (0.000003) if the allele count is > 1 OR by an allele frequency \< 0.001% (0.00001) if the allele count is ≤ 1.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：The reported missense variant was determined to be Pathogenic according to the APC-specific modifications.

There are currently only two Likely Pathogenic missense variants: c.3077A>G p.(Asn1026Ser) and c.3084T>A p.(Ser1028Arg). Other different missense variants at these positions meet PM5\_supporting. No missense variant has been classified as Pathogenic based on current evidence. 

Grantham´s distance of the variant under assessment must have an equal or higher score than the reported variant \[Reference 3\].
- **Supporting** ✅：The reported missense variant was determined to be Likely Pathogenic according to the APC-specific modifications.

There are currently only two Likely Pathogenic missense variants: c.3077A>G p.(Asn1026Ser) and c.3084T>A p.(Ser1028Arg). Other different missense variants at these positions meet PM5\_supporting. No missense variant has been classified as Pathogenic based on current evidence. 

Grantham´s distance of the variant under assessment must have an equal or higher score than the reported variant \[Reference 3\].

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：2-3.5 _de novo_ scores. For curation of _de novo_ score see **Tables 1** and **2**.
- **Moderate** ✅：1-1.5 _de novo_ scores. For curation of _de novo_ score see **Tables 1** and **2**.
- **Supporting** ✅：0.5 _de novo_ scores. For curation of _de novo_ score see **Tables 1** and **2**.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Variant segregates in ≥ 7 meioses in ≥ 2 families.
- **Moderate** ✅：Variant segregates in 5-6 meioses in ≥ 1 family.
- **Supporting** ✅：Variant segregates in 3-4 meioses in ≥ 1 family.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：**Missense variants:** Do not use computational prediction models for conservation, evolution, etc. _In silico_ splicing predictors should be used for presumed missense variants to reveal possible splicing effects.

**Non-canonical splicing variants:** Multiple _in silico_ splicing predictors support a deleterious effect.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：GnomAD Popmax Filtering Allele Frequency (AF) **≥ 0.1%** (0.001).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：GnomAD Popmax Filtering Allele Frequency (AF) **≥ 0.001%** (0.00001).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：≥ 10 points for healthy individuals **OR** ≥ 2 times in homozygous state.

A **healthy individual** worth 1 point is defined by:

Age ≥ 50 years   
\+ Less than 5 adenomatous polyps in a colonoscopy   
\+ Absence of features in Table 1

**OR**

Age ≥ 50 years   
\+ Colorectal cancer/polyposis was not the indication for testing

A **healthy individual** worth 0.5 points is defined by keywords including control, non-cancer, normal, unaffected population.
- **Supporting** ✅：≥ 3 points for healthy individuals.

A **healthy individual** worth 1 point is defined by:

Age ≥ 50 years   
\+ Less than 5 adenomatous polyps in a colonoscopy   
\+ Absence of features in Table 1

**OR**

Age ≥ 50 years   
\+ Colorectal cancer/polyposis was not the indication for testing

A **healthy individual** worth 0.5 points is defined by keywords including control, non-cancer, normal, unaffected population.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：**RNA assay** of a synonymous or intronic variant in constitutional patient sample demonstrates no mRNA aberration

**AND**

biallelic expression is shown and/or nonsense-mediated decay inhibition was used.
- **Supporting** ✅：**RNA assay** of a synonymous or intronic variant in constitutional patient sample demonstrates no mRNA aberration, without demonstration of biallelic expression or use of nonsense-mediated decay inhibition

**OR**

**Protein assay** show retention of β-catenin regulated transcription activity comparable to wild-type (only for variants within the β-catenin binding domain, which refers to codons 959-2129 of _APC_, see PMID: 33348689)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Affected member without the variant must score at least 1 phenotype point or at least two affected members without the variant must each score at least 0.5 phenotype points (see **Table 1**).
- **Supporting** ✅：Affected member without the variant must score at least 0.5 phenotype points (see **Table 1**).

#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Supporting** ✅：BP1 is applicable to APC with the exception of missense variants located in the first 15-amino acid repeat of the β-catenin binding domain (codon 1021-1035).

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed _in trans_ with a (Likely) Pathogenic _APC_ variant **OR** ≥ 3 times in an unknown phase with different (Likely) Pathogenic _APC_ variants.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：**Missense variants:** BP4 is not applicable.

**Synonymous (silent) or intronic variants**: Multiple in silico splicing predictors suggest no impact on gene or gene product.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Only applicable for an alternate genetic basis of the colorectal polyposis phenotype.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) or intronic variant at or beyond +7/–21 for which multiple splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site.

### 组合规则
- **Pathogenic**：
  - ≥ 2 Strong（PVS1_Strong/PS1/PS2/PS3/PS4/PM6_Strong/PP1_Strong）
  - 1 Strong（PVS1_Strong/PS1/PS2/PS3/PS4/PM6_Strong/PP1_Strong）AND ≥ 3 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Strong（同上）AND 2 Moderate（同上）AND ≥ 2 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
  - 1 Strong（同上）AND 1 Moderate（同上）AND ≥ 4 Supporting（同上）
  - 1 Very Strong（PVS1）AND ≥ 1 Strong（PS1/PS2/PS4/PM6_Strong/PP1_Strong）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND ≥ 1 Strong（PVS1_Strong/PS1/PS2/PS3/PS4/PM6_Strong/PP1_Strong）
  - 1 Very Strong（PVS1）AND ≥ 2 Moderate（PS1_Moderate/PS2_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND ≥ 2 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Very Strong（PVS1）AND 1 Moderate（PS1_Moderate/PS2_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）AND 1 Supporting（PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND 1 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）AND 1 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
  - 1 Very Strong（PVS1）AND ≥ 2 Supporting（PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND ≥ 2 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
- **Likely Pathogenic**：
  - 1 Strong（PVS1_Strong/PS1/PS2/PS3/PS4/PM6_Strong/PP1_Strong）AND 1 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Strong（同上）AND ≥ 2 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
  - ≥ 3 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 2 Moderate（同上）AND ≥ 2 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
  - 1 Strong（PVS1_Strong/PS1/PS2/PS3/PS4/PM6_Strong/PP1_Strong）AND 2 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Very Strong（PVS1）AND 1 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND 1 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）
  - 1 Very Strong（PVS1）AND 1 Supporting（PVS1_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1）
  - 1 Very Strong（PS2_Very Strong/PS3_Very Strong/PS4_Very Strong）AND 1 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
  - 1 Moderate（PVS1_Moderate/PS1_Moderate/PS2_Moderate/PS3_Moderate/PS4_Moderate/PM5/PM6/PP1_Moderate）AND ≥ 4 Supporting（PVS1_Supporting/PS3_Supporting/PS4_Supporting/PM2_Supporting/PM5_Supporting/PM6_Supporting/PP1/PP3）
- **Benign**：
  - 1 Stand Alone（BA1）
  - ≥ 2 Strong（BS1/BS2/BS3/BS4）
- **Likely Benign**：
  - ≥ 2 Supporting（BS2_Supporting/BS3_Supporting/BS4_Supporting/BP1/BP2/BP4/BP5/BP7）
  - 1 Strong（BS1/BS2/BS3/BS4）

> 注：官网面板 Pathogenic 12 条 / Likely Pathogenic 10 条（含 Very Strong 按 PVS1 与 PS2/PS3/PS4_Very Strong 区分的镜像规则），已按官网 HTML 面板原文完整转录。早期解析文本曾显示"规则重复"，经原始 HTML 核实为解析器丢失括号码映射所致，官网无重复。

### 不适用证据码
PM1、PM3、PM4、PP2、PP4、PP5、BP3、BP6
### 参考附件
- [Table 1&amp;2](https://cspec.genome.network/cspec/File/id/a530ae07-b2b7-401c-888f-06212822f7a6/data)
- [Supplementary material_V2](https://cspec.genome.network/cspec/File/id/a01cc6c1-0149-46b4-a766-054d5ba959c4/data)
- [APC-specifi c rules for combining criteria](https://cspec.genome.network/cspec/File/id/daa46462-b4f8-424f-b955-24a911c36faa/data)
- [Fig. 1](https://cspec.genome.network/cspec/File/id/930f6921-d46a-4d1c-bc49-c30b92f36320/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN089)

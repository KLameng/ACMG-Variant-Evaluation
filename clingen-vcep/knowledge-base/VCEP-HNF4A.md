# ClinGen VCEP基因特异性规范：HNF4A

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 4.0（DOI: 10.5281/zenodo.21434048；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN085 — Monogenic Diabetes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015967**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Upgrade initiation codon variants from PVS1_Moderate to PVS1_Strong on the basis that next methionine is Met71 and multiple variants not found in gnomAD have been reported in patients meeting diagnostic criteria for MODY (PMID: 23348805)       

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Use _HNF4A_ PVS1 decision tree.

*   Variants generating PTCs in exon 10 and last 55 nucleotides of exon 9 (c.1162-1216) are not expected to cause NMD[<sup>1</sup>](#pmid_24274751)
    *   The most 3’ nonsense or frameshift variant is c.1256C>G, p.S419X in the last exon. This variant has been classified as Pathogenic by the MDEP.  There are six other nonsense and frameshift variants in exon 10, none of which have case information and are all currently classified as VUS. The collective evidence supports applying PVS1 for variants at codon 419 (c.1257) and 5’ and PVS1\_Supporting for variants at c.1258 (G)/p.Gly420 and 3’.
*   “Exon skipping or use of a cryptic splice site that preserves reading frame” and “Single to multi-exon deletion that preserves reading frame”
    *   Exons 1, 2 (LRG 4), 3 (LRG 5), 4 (LRG 6), 6 (LRG 8): deletion or skipping causes frameshift: PVS1 
    *   Exons 5 (LRG 7), 7 (LRG 9), 8 (LRG 10), 9 (LRG 11) - deletion or skipping causes in-frame deletion, 52/52/79/51-79 AA deleted, that is >10 % of the protein in each case - PVS1\_Strong  
    *   Exon 10 (LRG 12) - 46 AA, contains the transactivation domain, includes stop loss - PVS1\_Strong
- **Strong** 📋：Use _HNF4A_ PVS1 decision tree.

*   “Exon skipping or use of a cryptic splice site that preserves reading frame” and “Single to multi-exon deletion that preserves reading frame” 
    *   Exons 5 (LRG 7), 7 (LRG 9), 8 (LRG 10), 9 (LRG 11) - deletion or skipping causes in-frame deletion, 52/52/79/51-79 AA deleted, that is >10 % of the protein in each case - PVS1\_Strong  
    *   Exon 10 (LRG 12) - 46 AA, contains the transactivation domain, includes stop loss - PVS1\_Strong
*   Apply PVS1\_Strong to initiation codon variants.  MDEP has classified two start codon variants as likely pathogenic (c.3G>A: PM2\_Supporting + PP4\_Moderate + PP1\_Strong + PVS1\_Moderate (c.1delA); c.1delA: PM2\_Supporting + PP1 + PP4\_Moderate + PVS1\_Moderate) and there are multiple P/LP variants before the next methionine, p.Met71.
- **Supporting** 📋：Use _HNF4A_ PVS1 decision tree.

Apply PVS1\_Supporting to nonsense or frameshift variants at c.1258 (G)/p.Gly420 and 3’.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Applicable for a same amino acid change if the previously established variant is classified as pathogenic by ClinGen MDEP specifications.

PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.
- **Moderate** 📋：Applicable for a same amino acid change if the previously established variant is classified as likely pathogenic by ClinGen MDEP specifications.

PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.
- **Supporting** 📋：PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Strong** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Moderate** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Supporting** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” per instructions.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing.
- **Supporting** 📋：List of approved functional studies and guidelines for interpretation:

*   EMSA for DNA binding
    *   “Decreased function” is defined as activity less than 60% of wildtype 
    *   Note: the effect of the variant on DNA binding will be highly dependent on whether the variant is located within the DNA binding domain.
*   Luciferase assays for transactivation 
    *   “Decreased function” is defined as activity less than 60% of wildtype  
    *   Note: this threshold is not 100% specific for transactivation (TA) activity and is complicated by the fact that TA activity will vary depend on many factors, for instance cell line that is used (HeLa, INS, MIN6 etc).
*   Western blotting and indirect immunofluorescence for protein expression (specifically levels and nuclear and cytoplasmic localization, respectively).
    *   Determining appropriate thresholds for protein expression is more difficult due to variability in results due to the complexity of the technique.  Sample preparations, gel loading, transfer efficiency, specificity of the antibody, choice of internal control and inaccurate detection and quantification are some of the factors that can contribute to varying and inconsistent results. If a reduction in protein expression is seen by immunoblotting, then further testing by quantitative PCR (qPCR) is recommended in order to measure the mRNA level and assess whether a reduction in amount of protein is due to a reduced mRNA level.
*   To use PS3\_Supporting, functional study must have been performed on a transfected variant.  If a study was performed on a cell line generated from a patient sample (and therefore contains the variant plus wild-type allele) does not count as PS3\_Supporting.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：7 (seven) or more unrelated occurrences = Strong. Variant should meet PM2\_Supporting in order to use PS4 at any level (careful review of gnomAD QC data may be necessary to assess whether variant is real or an artifact, especially if variant is in a polyC region).  Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology.

*   One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)[<sup>7</sup>](#pmid_21395678),[<sup>8</sup>](#pmid_28701371),[<sup>9</sup>](#pmid_30409810),[<sup>10</sup>](#pmid_31704690) 
*   Very low or negative C-peptide, defined as either fasting or non-fasting random C-peptide (\<200pmol/L or 0.6ng/mL)[<sup>11</sup>](#pmid_30225972),[<sup>12</sup>](#pmid_23771925) or urinary C-peptide/creatinine ratio \<0.2 nmol/mmol[<sup>8</sup>](#pmid_28701371),[<sup>9</sup>](#pmid_30409810)
- **Moderate** 📋：4-6 unrelated occurrences = Moderate. Variant should meet PM2\_Supporting in order to use PS4 at any level. Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology.

*   One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)[<sup>7</sup>](#pmid_21395678),[<sup>8</sup>](#pmid_28701371),[<sup>9</sup>](#pmid_30409810),[<sup>10</sup>](#pmid_31704690)
*   Very low or negative C-peptide, defined as either fasting or non-fasting random C-peptide (\<200pmol/L or 0.6ng/mL)[<sup>11</sup>](#pmid_30225972),[<sup>12</sup>](#pmid_23771925) or urinary C-peptide/creatinine ratio \<0.2 nmol/mmol[<sup>8</sup>](#pmid_28701371),[<sup>9</sup>](#pmid_30409810)

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：Applicable to amino acids that directly bind DNA and are necessary for Zinc-finger or homodimer formation[<sup>2</sup>](#pmid_18829458) 

*   Directly bind DNA: Asp43, His49, Tyr 50, Gly51, Asp56, Gly57, Lys59, Arg63, Arg64, Arg67, His70, Tyr72, Arg87, Asn88, Arg91, Arg94, Gln109, Arg112   
*   Homodimer: Arg75, Gln89, Glu111, Asp113 
*   Zinc finger: Cys38, Cys41, Cys55, Cys58, Cys74, Cys80, Cys90, Cys93

Applicable to variants within the promoter region that are direct HNF1A/HNF1B binding sites [<sup>15</sup>](#pmid_23332764), [<sup>16</sup>](#pmid_38909044):

*   c.-170 to c.-173 and c.-178 to c.-181 (NM\_175914.4)
- **Supporting** 📋：This criterion can be used for missense variants in well-conserved regions within the DNA and ligand-binding domains. It can also be used for variants within certain conserved transcription factor binding sites in the promoter (see below for details).

*   Promoter region: 
    *   c.-132 to c.-141 (HNF6/OC2 binding site)
    *   c.-143 to c.-149, c.-151 (PDX1 (formerly IPF1) binding site) 
    *   c.-169, c.-174, c.-176, and c.-177 (HNF1A/HNF1B binding site)
*   DNA binding: 
    *   codons 37-113 (NM\_175914.4:c.175C-339C p.Leu37-Asp113) (While the paper describing the crystal structure of _HNF4A_[<sup>2</sup>](#pmid_18829458) shows the sequence as amino acids 33-113, amino acids 33-36 do not bind DNA and the conserved sequence starts as Leu37.)
*   Ligand binding: 
    *   codons 180-220 and 300-350  
        *   (NM\_175914.4:c.538G-658G p.Ala180-Val220) 
        *   (NM\_175914.4:c.898T-1048G p.Tyr300-Glu350)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：gnomAD Grpmax FAF ≤ 1:333,000 (≤ 0.000003 or 0.0003%)

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：For deletions/insertions of more than one amino acid in a non-repeat region, use as moderate level of evidence.
- **Supporting** 📋：For single amino acid deletions/insertions, use as supporting level of evidence

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Applicable once two amino acid changes have been classified as pathogenic at the same amino acid residue.
- **Moderate** 📋：The novel amino acid change must have a Grantham distance greater than or equal to the previously classified pathogenic variant.
- **Supporting** 📋：Apply if the previously classified amino acid change is likely pathogenic (rather than pathogenic) or if the previously classified variant is pathogenic but has a greater Grantham distance than the novel variant.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Use thresholds suggested by Jarvik and Browning[<sup>5</sup>](#pmid_27236918)

*   Single Family : ≤ 1/32 (5 meioses)
*   \> 1 Family : ≤ 1/16 (4 meioses)
- **Moderate** 📋：Use thresholds suggested by Jarvik and Browning[<sup>5</sup>](#pmid_27236918)

*   Single Family : ≤ 1/16 (4 meioses)
*   \> 1 Family : ≤ 1/8 (3 meioses)
- **Supporting** 📋：Use thresholds suggested by Jarvik and Browning[<sup>5</sup>](#pmid_27236918)

*   Single Family : ≤ 1/8 (3 meioses)
*   \> 1 Family : ≤ ¼ (2 meioses)

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use REVEL score of ≥0.70 as supportive evidence of pathogenicity. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is at least 0.2 [<sup>4</sup>](#pmid_32123317),[<sup>3</sup>](#pmid_30661751).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** 📋：Phenotype: MODY Probability Calculator result ≥50% chance of testing positive[<sup>6</sup>](#url_187f5e4a-1941-5c2d-9c9f-1dc999cc5454) AND negative _HNF1A_ testing AND presence of at least one additional feature characteristic of \__HNF4A_\_-MODY:   

*   Antibody negative and/or persistent C-peptide after five years following T1DM diagnosis  
*   Personal or family history of persistent neonatal hypoglycemia  
*   Personal or family history of large for gestational age (LGA) infants or macrosomia in the absence of sufficient maternal hyperglycemia 
*   Response to low-dose SU (extreme response- hypoglycemia) 
*   Biochemical/Molecular phenotypic evidence from patient cell lines 
*   Fanconi phenotype in conjunction with c.187C>T p.R63W
- **Supporting** 📋：MODY Probability Calculator (MPC)<sup>6</sup> result ≥50% chance of testing positive AND negative _HNF1A_ testing

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：gnomAD Grpmax FAF  ≥ 1:30,000 (≥0.0033% or 0.000033)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Apply to normoglycemic individuals age 70 or older (i.e., genotype positive, phenotype negative)

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of normal splicing.
- **Supporting** 📋：List of approved functional studies and guidelines for interpretation of data.

*   EMSA for DNA binding 
    *   “No functional impact” is defined as ≥75% activity of wildtype 
    *   Note: the effect of the variant on DNA binding will be highly dependent on whether the variant is located within the DNA binding domain.
*   Luciferase assays for transactivation 
    *   “No functional impact” is defined as ≥75% activity of wildtype 
    *   Note: this threshold is not 100% specific for transactivation (TA) activity and is complicated by the fact that TA activity will vary depend on many factors, for instance cell line that is used (HeLa, INS, MIN6 etc). Assays should include controls for WT, T2DM and known MODY variants.
*   Western blotting and indirect immunofluorescence for protein expression (specifically levels and nuclear and cytoplasmic localization, respectively).   
    *   Determining appropriate thresholds for protein expression is more difficult due to variability in results due to the complexity of the technique.  Sample preparations, gel loading, transfer efficiency, specificity of the antibody, choice of internal control and inaccurate detection and quantification are some of the factors that can contribute to varying and inconsistent results. If a difference in protein expression compared to WT is seen by immunoblotting, then further testing by quantitative PCR (qPCR) is recommended in order to measure the mRNA level and assess whether the difference in amount of protein is due to a reduced mRNA level.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Applicable to family members without variant who have MPC<sup>6</sup> score ≥50% (i.e., genotype negative, phenotype positive).

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Also applicable when in cis or trans with a likely pathogenic variant.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use a REVEL score of ≤0.15 as supportive evidence of no predicted impact on the gene or gene product. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is below 0.2[<sup>3</sup>](#pmid_30661751),[<sup>4</sup>](#pmid_32123317).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：A variant in another monogenic diabetes gene is Pathogenic/Likely Pathogenic.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Apply BP7 when the predicted change from SpliceAI is below 0.2 AND phyloP100 way \< 2.0.

### Rules for Combining Criteria（组合规则）

**Pathogenic（致病）**
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**Likely Pathogenic（可能致病）**
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate

**Benign（良性）**
- ≥ 2 Strong
- 1 Stand Alone

**Likely Benign（可能良性）**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PM3、PM6、PP2、PP5、BP1、BP3、BP6
### 参考附件
- [HNF4A PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/a5f5beff-30d8-4c2b-9b60-5c8159179fdc/data)
- [PS2 De Novo Points Table](https://cspec.genome.network/cspec/File/id/cf0f5b7f-2560-4f0d-ab21-b6bc5479d829/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN085)

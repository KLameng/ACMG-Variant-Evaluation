# ClinGen VCEP基因特异性规范：VHL

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN078 — VHL Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0008667**（遗传方式：Autosomal dominant inheritance）

### 官网版本
- Version 1.1（Released）
- DOI: 10.5281/zenodo.21433974（https://doi.org/10.5281/zenodo.21433974）
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
- **Very Strong** 📋：**LINK TO PVS1 DECISION TREE DOCUMENT:** [**https://drive.google.com/file/d/1mGfChgxbGVbzYn6Ggmb9rYvoGGah25ll/view?usp=sharing**](https://drive.google.com/file/d/1mGfChgxbGVbzYn6Ggmb9rYvoGGah25ll/view?usp=sharing)

**Do not apply PVS1 for truncations that occur prior to Codon 54 (including frameshift events that start and end prior to Codon 54 but the truncation extends beyond Codon 54.)**

**Note1: Exon presence in biologically relevant transcripts:** In some transcripts exon 2 of _VHL_ is skipped and expressed at low levels. The function of this transcript is not fully known. Exon 2 comprises almost the entirety of the nuclear export function region of the Beta domain and is critical for known VHL function. Exon 1 contains the only initiator codons in _VHL_. Exon 3 contains the elongin binding function. _**All exons should be considered as "present in biologically relevant transcripts" in the PVS1 decision tree.**_

**Note 2: The 10% PVS1 downgrade to Moderate cannot apply to VHL** because of the small size.

**Nonsense Mediated Decay** [<sup>5</sup>](#pmid_22825683) [<sup>4</sup>](#pmid_20145706)  **NMD experimental evidence in 1st exon after codon 54 and to 5' region of 2nd exon (codon 138)**.\*\*

**Critical Domains:**

1st Beta (β) domain (63-154), especially Nuclear Export (114-155)

Alpha (ɑ) domain (155-192), especially Elongin C binding (157 - 172)

Second Beta domain (193-204)   

_Truncating variants after Met54 and predicted to undergo NMD (from AA55-AA136/c.408) or in the beta or alpha domains can receive PVS1, and those outside the second Beta domain (205-213) can receive PVS1\_Moderate downgrade to account for minimal loss of VHL protein. Notably a frame shift deletion at 205 is pathogenic in ClinVar (ID 18971) as are stop loss extension variants in the last codons (see PM4)._

**SPLICE: If any canonical exon is skipped, the variant receives PVS1.** If a cryptic splice disrupts the reading frame, and is in a critical domain (AA63-AA204) or is predicted to undergo NMD (AA55-AA136) it receives PVS1. If it is outside a critical domain and predicted to undergo NMD (AA55-62), it receives PVS1\_Strong (the second site outside of critical domains AA205-213 is not predicted to undergo NMD). If a cryptic splice does not alter the reading frame, and is in a critical domain (AA 63-204), it can receive PVS1\_Strong, and if it is outside the critical domain (AA 205-213) or  in an NMD prediction (AA 55-62), it receives PVS1\_Moderate. Note:  There is a cryptic exon (E1) in intron 1 [<sup>7</sup>](#pmid_31996412) [<sup>6</sup>](#pmid_29891534), and silent variants in exon 2 that are reported to cause skipping of exon 1. If there is functional evidence of exon skipping (RNA splice assay) then PVS1 can apply. Do not double count evidence. Ex. PVS1 should be used in place of PS3 functional evidence confirming splice alteration, but PS3 evidence code could still apply to other relevant assays confirming effect on HIF1/2a presence etc. 

**EXON DELETION:** SVI PVS1 decision tree modified for whole exon deletions. There are only 3 exons in _VHL_ and each has an important functional domain. Any exon deletion of _VHL_ receives PVS1. 

**EXON DUPLICATION:** Follow PVS1 decision tree. Note: few pathogenic exon duplications are reported in ClinVar.   (ID:417571, ID:584137). These have no literature cited. 

**INITIATION CODON:** VHL Met 1 (in VHL p30) truncation or missense would not affect VHL p19, as VHL has a second start at codon 54 (VHL p19), it cannot be scored in the PVS1 decision tree. After that, no other viable alternative starts are known. Start loss at codon 54 would presumably result in an impact, as VHL p30 and p19 would be truncated prior to any known functional domains (PVS1). Ong 2007 has 1 family (2 subjects) with Met54X and reports cerebellar hemangioblastomas. There is no functional study in the paper for this variant. Olschwang et al 1998 VHL Type 2A, one subject with 161insT (FS result). There is no functional study in the paper. Missense at Met 54 (VHL p19 initiation codon) would presumably not result in as strong an impact as the full length VHL p30 would still be produced (PVS1 decision tree = N/A). ClinVar has M54T (ID:819688) and M54L (ID:843990). M54T is uncertain, with no other evidence provided. M54L references M54I which segregates in homozygous state with erythrocytosis in individuals of Moroccan descent [<sup>9</sup>](#pmid_26224408) [<sup>8</sup>](#pmid_27578599), and those heterozygous for M54I did not present VHL phenotype [<sup>9</sup>](#pmid_26224408).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Applied only to variants with interpretation by the VHL VCEP or by a variant with pathogenicity established using VHL VCEP specifications.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：A single proband cannot be very strong evidence, but multiple probands can be combined to reach very strong (4+ points).
- **Strong** 📋：Phenotype highly specific for the gene (Danish Criteria) (≥2 but less than 4 _de novo_ points).
- **Moderate** 📋：Phenotype consistent but not highly specific. Ex. VHL spectrum cancer without family history or strong indication of VHL phenotype. (≥1 but less than 2 _de novo_ points)
- **Supporting** 📋：Phenotype consistent but not highly specific (≥0.5 but less than 1 _de novo_ points) Ex. subject included in a VHL cohort, but specific information on tumor types is not provided.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：Acceptable assays that display functional effect in VHL are the following:  

• HIF 1/2a degradation assays -- HIF1/2a is not degraded and/or 

• VBC complex stability is affected and/or

• Pathogenicity supported by abnormal ECM formation and impaired fibronectin binding [<sup>1</sup>](#pmid_9651579) , [<sup>2</sup>](#pmid_11331613) , [<sup>3</sup>](#pmid_11358843) , [<sup>17</sup>](#pmid_14706840)

Multiple studies and publications confirm the role of VHL in HIF1/2a regulation and VBC complex stability for VHL Type 1, and 2A/B, as well as fibronectin binding/deposition and assays evaluating extra-cellular matrix composition. In-vitro assays should display total loss of HIF1/2a degradation (i.e. HIF1/2a presence) for VHL Type 1, and 2A/B.  VHL Type 2C should display presence of HIF1/2a (with VBC complex stability variably affected and fibronectin deposition/extra cellular matrix composition affected). These assays are typically performed in Renal Cell Carcinoma (RCC) cells lacking VHL, introducing normal pVHL as a control in addition to a variant-VHL, then comparing HIF1/2a levels to WT pVHL. Brnich et al proposed 10 controls to achieve PS3\_Supporting and 11 for PS3\_Moderate [<sup>10</sup>](#pmid_31892348). We propose to _follow the workflow outlined in Brnich et al._  Type 2C VHL variants are typically missense variants in the alpha domain of VHL, and do not usually affect HIF1/2a. If HIF1/2a maintains presence and VHL Type 2C is suspected, assays evaluating fibronectin deposition or extracellular matrix assembly should be used. 

**SPLICING:** **PS3:** RNA transcripts carrying splicing mutation display splicing defects in patient cells. **PS3\_Moderate**: RNA transcripts carrying splicing mutation display splicing defects in in-vivo or in-vitro assays.   **Functional Assay Documentation** : [https://drive.google.com/file/d/1w8P8zs1fHUolaAYmBL1jw-vcjsX3N_yh/view?usp=sharing](https://drive.google.com/file/d/1w8P8zs1fHUolaAYmBL1jw-vcjsX3N_yh/view?usp=sharing)

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** 📋：**16+ points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**
- **Strong** 📋：**5-15 points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**
- **Moderate** 📋：**2 – 4 points the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**
- **Supporting** 📋：**1 point the PS4 cut-off and Proband Scoring Tables from a mix of any of the following phenotypes: specific, consistent and nonspecific.**

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：Putative missense variants that are known germline hotspots AND/OR in key functional domains AND/OR somatic variants that have ≥10 instances for the same AA in cancerhotspots.org. See the table of Germline and Somatic Hotspots.
- **Supporting** 📋：Putative missense variants seen in somatic databases, having \<10 instances for the same AA in cancerhotspots.org. See the table of Germline and Somatic Hotspots.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：PM2\_Supporting can be applied for variants either absent from gnomAD or with \<= 0.00000156 (0.000156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release). If no GroupMax Filtering Allele Frequency is calculated (ex. due to a single variant present), PM2\_Supporting may also be applied.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：In-frame insertion / deletions in the B and alpha domains and stop-loss variants adding significant additional amino acids to VHL [<sup>15</sup>](#pmid_20560986) cites multiple pathogenic cases and experimental evidence of stop loss extensions in VHL that are associated with Type 2A VHL disease).  The functional domains are: Beta (β) domain (AA 63 - 155, Nuclear Export), Alpha (ɑ) domain (AA 156-192, Elongin C binding), and Second Beta (β) domain (AA 193-204). 

PM4 does not apply to in-frame indels prior to codon 54 that do not alter the Met54 VHL p19 codon and beyond.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：Pathogenicity of prior variant is established by interpretation of the VHL VCEP or variants with pathogenicity established using VHL VCEP specifications. The Grantham distance should be used to compare variants. The variant under consideration must be equal or a larger distance than the classified pathogenic variant (Grantham, 1974, Table 2 [<sup>16</sup>](#pmid_4843792) ). Splice metapredictors should be used to ensure the variant is not predicted to have an effect on splicing.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：See PS2 evidence code for scoring and phenotypes. Assumed _de novo_ receives half the points as compared to maternity and paternity confirmed _de novo_. If paternity and maternity are not confirmed, score as the PM6 code. PM6 can receive “VeryStrong” strength. For example, if there are >4 de novo probands with Danish Criteria and none have paternity confirmed, this can receive PM6\_VeryStrong. Note: the VCI as of Nov 2022 does not allow PM6\_VeryStrong. Instead apply the PS2 evidence code and increase the strength to “VeryStrong” with a note that paternity and/or maternity is not confirmed.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：\>7 meioses across >=2 families
- **Moderate** 📋：5 – 6 meioses across ≥1 family.
- **Supporting** 📋：3 – 4 meioses across ≥1 family.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：For missense variants, use REVEL score >=0.664. 

For splice variants, concordance of Splice AI (>0.5) and VarSeak (class 4 or class 5).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Use a BA1 cut off of >=0.000156 (0.0156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4 release).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Use BS1 cut off of  >=0.0000156 (0.00156%) GroupMax Filtering Allele Frequency in gnomAD (based on gnomAD v4).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：VHL is not highly penetrant _at an early age._ BS2 can be applied if: There are at least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**with full phenotyping and screening**_ for the absence of VHL-related cancers.
- **Supporting** 📋：VHL is not highly penetrant _at an early age._ BS2\_Supporting can be applied if: At least 3 individuals, all >=65yo, unaffected, harboring the same variant, _**lacking full phenotyping and screening**_, with no noted VHL-related cancers

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：• HIF 1/2a assay replicates WT function and/or

• VBC complex stability is not affected and/or 

• ECM formation/fibronectin binding is unaffected 

This rule can be used and weighted as appropriate for functional tests of variants prior to codon 54 (which show the VHL19 product is not impacted). Evidence of benign effect for VHL Type 1 and 2A/B can be seen when HIF1/2a displays degradation (i.e. replicates WT function), and/or the VHL Elongin C, Elongin B, Cullin2 RBX1 (VCB-CR) E3 ubiquitin ligase complex stability is not affected and/or ECM formation/fibronectin binding is unaffected. Note: VHL Type 2C variants typically do not affect HIF1/2a; absence of HIF1/2a alone when testing a suspected VHL Type 2C variant should not be used for BS3. Functional studies of fibronectin and ECM formation are needed for VHL Type 2C. Follow modified SVI guidance for functional assays, general controls and benign controls. For splicing variants (and intronic/synonymous), RNA assays must demonstrate no impact on splicing.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Lack of segregation is seen in affected members of ≥2 families
- **Supporting** 📋：Lack of segregation is seen in 1 family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** 📋：i) -variant observed in trans with a known pathogenic variant (phase confirmed), in the absence of congenital polycythemia (clinical manifestations or molecular)

ii) -OR observed in the homozygous state in an individual without personal &/or family history of Von Hippel-Lindau disease or congenital polycythemia

iii) -OR observed _in cis_ or with unknown phase with three or more different pathogenic _VHL_ variants
- **Supporting** 📋：\-variant is observed _in cis_ (or phase is unknown) w/ a pathogenic _VHL_ variant

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** 📋：BP3 can be applied to the 8x GXEEX AA repeat motif in the 5’ end of VHL p30 (AA14-AA48). Otherwise, the rest of the coding regions in VHL do not contain repeats (and none contain LINE/SINE, low complexity or other repeat types as identified by RepeatMasker) and BP3 is not applicable.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Due to the lack of benign variants, and the drop in classification accuracy for benign VHL variants, missense predictors should not be used to assign the BP4 evidence code. 

BP4 can be applied to assess lack of splicing impact, with concordance of Splice AI (≤0.1) and VarSeak (Class 1 or Class 2).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：BP5 can be applied for two or more co-occurrences with pathogenic variants in a different gene that fully explained the patient's phenotype, but specific circumstances would need to be met in order for a case to be considered for inclusion. First, the variant in the other gene must be considered highly penetrant, with both the individual's age, tumour type and gender taken into consideration. Additionally, the patient's personal and family history (including up to 2nd degree relatives) should not overlap with features seen in VHL and VHL tumour histologies. As an example, an individual with a personal and family history of pheochromocytoma who harbored a _VHL_ variant in addition to a pathogenic SDHB variant BP5 would not apply, because pheochromocytoma is a known risk in VHL and the _VHL_ variant might have contributed to this individual's pheochromocytoma cancer risk. However, an individual with a personal and family history of chromophobic RCC who was positive for a _VHL_ variant as well as a pathogenic FLCN variant would be considered for BP5 application, as non-clear cell RCC is not associated with VHL disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：To evaluate splice prediction, use the BP4 code. If BP4 is met for lack of splice effect, BP7 can be applied to silent or intronic variants where the PhyloP score is ≤0.2.

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
PM3、PP2、PP4、PP5、BP1、BP6
### 参考附件
- [Functional Assay Documentation](https://cspec.genome.network/cspec/File/id/e1ce61d6-b9c7-4ca9-83c0-0975112b0a8b/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN078)

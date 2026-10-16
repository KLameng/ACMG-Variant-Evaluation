# ClinGen VCEP基因特异性规范：ENG

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v1.1.0（2024-03-20）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN136 — Hereditary Hemorrhagic Telangiectasia Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0008535**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use ENG PVS1 Decision Tree (see attachments)
- **Strong** ✅：Use ENG PVS1 Decision Tree (see attachments)
- **Moderate** ✅：Use ENG PVS1 Decision Tree (see attachments)

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：*   mRNA splicing assays can be used as strong functional evidence. 
    *   **Note:** level of evidence used may differ depending on whether the abnormal transcript is in-frame or out-of-frame, and whether there is complete or incomplete splicing impact.
    *   Do not use PS3 for splice variants that meet PVS1.
- **Moderate** ✅：See PS3\_Supporting and Instructions below.
- **Supporting** ✅：*   Protein expression assays: Metabolic label & IP, WB & FACS HUVECs/BOECs, FACs activated monocytes, cDNA transfect, WB & ML HEK293T/COS/NIH3T3, cDNA transfect & luciferase HepG2
    *   **Note:** Decreased protein expression can be used as supporting pathogenic evidence if experiment was not done in a single assay, and the corresponding densitometry of western blot reflects the conclusion drawn.
*   Intracellular signaling assays: BRE/CAGA-luciferase, Gal4 Smad1/Smad3 for TGF-beta/BMP9 signaling
*   Binding assays: BMP9 binding, transcription factor Sp1, BMP9 protein-protein interaction (BLI)
*   Subcellular protein localization
*   Morphology: Morphology & actin cytoskeleton, tubulogenesis
*   Somatic variant 2<sup>nd</sup> hit: In vivo evidence can be obtained as supporting functional evidence by identification of somatic variants in telangiectases´ biopsies using NGS, suggesting a second-hit mechanism leading to biallelic LOF (PMID: 31630786).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：4+ probands with phenotype consistent with HHT.
- **Moderate** ✅：2-3 probands with phenotype consistent with HHT.
- **Supporting** ✅：1 proband with phenotype consistent with HHT.
- **VCEP说明**：Variant must also meet PM2_Supporting. See HHT phenotype document in attachments for phenotype requirements.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **VCEP说明**：If the variant falls within a PM1 region, do not use PM1 with PM5_Strong. PM1 can still be combined with PM5.
- **Moderate** ✅：Apply if variant is located in a critical residue:

*   ENG:
    *   BMP9 binding sites: S278, F282 (PMIDs 28564608, 25312062)
    *   Cysteine residues either previously reported to be likely pathogenic or pathogenic:
        *   C207, C363, C382, C412, C549
    *   Or cysteine residues known to be important for ENG function:
        *   C350 (C350-C382 disulfide in ZP-N domain of ENG is required for secretion of its ZP module)
        *   C394 (makes a disulfide bond with C412 which is reported to be a mutated residue)
        *   C516 (involved in forming intermolecular disulfides that hold ENG homodimer together)
        *   C582 (involved in forming intermolecular disulfides that hold ENG homodimer together)

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：\<6 total alleles in gnomAD or \<0.00004 (0.004%) in gnomAD subpopulations.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：≥2 different missense changes at same codon have been determined to be likely pathogenic or pathogenic based on HHT VCEP rules.
- **Moderate** ✅：A different missense change at same codon has been determined to be likely pathogenic or pathogenic based on HHT VCEP rules.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：5+ meioses (1/32 likelihood)
- **Moderate** ✅：4 meioses (1/16 likelihood)
- **Supporting** ✅：3 meioses (1/8 likelihood)

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants: REVEL score ≥0.644 or SpliceAI score ≥0.2.
*   For synonymous and intronic variants: SpliceAI score ≥0.2.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Patient's phenotype meets consensus clinical diagnostic (Curaçao) criteria for HHT, and sequencing and large deletion/duplication analysis was performed for both _ENG_ and _ACVRL1_ with any other identified variants ruled out.
- **VCEP说明（组合限制）**：PP4_Moderate cannot be applied to variants that meet BS1_Supporting/BS1/BA1 criteria. If PP4_Moderate can be applied to a patient, they cannot be included in proband counting (PS4).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency is ≥1% in general population databases (e.g. gnomAD) based on Popmax FAF.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：\>0.2% to \<1% in general population databases (e.g. gnomAD) based on Popmax FAF, **or** if variant meets BS1\_Supporting and has ≥2 homozygotes.
- **Supporting** ✅：>0.08% to 0.2% (based on gnomAD Popmax FAF).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：*   mRNA splicing assays 
*   Intracellular signaling assays: BRE/CAGA-luciferase, Gal4 Smad1/Smad3 for TGF-beta/BMP9 signaling
*   Binding assays: BMP9 binding, transcription factor Sp1, BMP9 protein-protein interaction (BLI)
*   Subcellular protein localization
*   Morphology: Morphology & actin cytoskeleton, tubulogenesis

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic or likely pathogenic variant based on HHT VCEP rules.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants: REVEL score ≤0.15 and SpliceAI score ≤0.1.
*   For synonymous and intronic variants: SpliceAI score ≤0.1.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Apply if a likely pathogenic or pathogenic variant (based on HHT VCEP rules) is found in _ACVRL1_.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous or intronic variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site. Can be used together with BP4 evidence.

### Rules for Combining Criteria

#### Pathogenic
- 1 Very Strong (PVS1) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong)
- 1 Very Strong (PVS1) AND ≥ 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 1 Very Strong (PVS1) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) AND 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- 1 Very Strong (PVS1) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)

#### Likely Pathogenic
- 1 Very Strong (PVS1) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate)
- 1 Very Strong (PVS1) AND 1 Supporting (PM2_Supporting)

#### Benign
- ≥ 2 Strong (BS1, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS4) AND 1 Supporting (BS1_Supporting, BS3_Supporting, BP2, BP4, BP5, BP7)
- ≥ 2 Supporting (BS1_Supporting, BS3_Supporting, BP2, BP4, BP5, BP7)
- 1 Strong (BS1)

### 不适用证据码
PM3、PM6、PP2、PP5、BS2、BP1、BP3、BP6
### 参考附件
- [HHT Functional Assays](https://cspec.genome.network/cspec/File/id/50e346be-f8a1-48ae-a322-2ab5f3e9e1c3/data)
- [ENG PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/dd7ea90a-8689-47b5-bbf4-f47bd4cd9324/data)
- [HHT Phenotype](https://cspec.genome.network/cspec/File/id/bcf229dd-21d3-4b71-aff4-75b443739ede/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN136)

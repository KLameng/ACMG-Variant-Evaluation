# ClinGen VCEP基因特异性规范：MYO6

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：Hearing Loss VCEP v2.0（Released 2022-03-30）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN005 — Hearing Loss Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0019497**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Null variant in a gene with established LOF as a disease mechanism; see PVS1_Strong, PVS1_Moderate, PVS1_Supporting for reduced evidence applications.
- **Strong** 📋：See PVS1 flow chart for PVS1_Strong variants in gene where LOF is a known mechanism of disease.
* PVS1 should also be considered for the following genes with variants assessed in the Hearing Loss Variant Pilot: GJB2, CDH23, USH2A, SLC26A4, MYO6, MYO7A, TECTA, KCNQ4.
* For other genes, LOF must be an established disease mechanism, and the gene/disease association must be Strong or Definitive clinical validity level as outlined in Strande et al. 2017 (PMID: 28552198).
* If above criteria is met, follow PVS1 flowchart as recommended by the SVI.
- **Moderate** 📋：See PVS1 flowchart for PVS1_Moderate variants in gene where LOF is a known mechanism of disease.
- **Supporting** 📋：See PVS1 flowchart for PVS1_Supporting variants in gene where LOF is a known mechanism of disease.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Same amino acid change as an established pathogenic variant; OR
splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant.
* Established variant must meet criteria for pathogenicity by the HL specifications
 * Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant
  * Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
* No additional hearing loss specifications for missense variants. Follow recommendations as outlined in Richard 2015 and/or the Sequence Variant Interpretation working group within ClinGen.

* Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change)

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：4 points per tables 5a and 5b:
Examples: 2 proven de novo occurrences; OR 1 proven + 2 assumed de novo occurrences; OR
4 assumed de novo occurrences.
- **Strong** 📋：2 points per tables 5a and 5b:
Examples: 1 proven de novo occurrence; OR 2 assumed de novo occurrences.
- **Moderate** 📋：1 point per tables 5a and 5b:
Examples: 1 proven de novo occurrence (phenotype consistent but not specific to gene); OR
1 assumed de novo occurrence; OR 2 assumed de novo occurrences (phenotype/gene not specific).
- **Supporting** 📋：0.5 points per tables 5a and 5b:
Example: 1 assumed de novo occurrence (phenotype/gene not specific).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Knock-in mouse model demonstrates the phenotype.
- **Moderate** 📋：Validated functional studies show a deleterious effect (predefined list): GJB2: electrical coupling assays, dye transfer assays → PS3_Moderate
* Dye Transfer Assays: Expect results that compare the fluorescence of a variant-transfected cell to
both a negative control (or H2O injected control) and a wildtype-transfected cell. PS3_Moderate
would be applied if the variant results in no dye transfer or significantly different dye transfer when
compared to the wildtype.
* Electrical Coupling Assays: Expect results comparing the current of the variant-transfected cells to both a negative control (i.e. H2O injected control) and a wildtype-transfected cell. PS3_Moderate would be applied if the variant results in significantly different current compared to the wildtype, and the current is comparable to background levels/negative control.
- **Supporting** 📋：SLC26A4: Radio isotope and fluorescence assays → PS3_Supporting
* Radio Isotope Assays: PS3_Supporting would be applied when cells transfected with mutant SLC26A4 show a statistically significant decreased efflux of iodide compared to wildtype pendrin.
* Fluorescence Assays: PS3_Supporting would be applied when a cell transfected with the mutant SLC26A4 shows a statistically significant difference in fluorescence (ΔFmax %) compared to the wildtype protein, and when the fluorescence is not significantly different from that of an empty vector control.
COCH: Localization, secretion, and dimerization studies performed using immunofluorescence and
Western blotting techniques →PS3_Supporting
* Localization: PS3_Supporting would be applied if the mutant cochlin protein does not aggregate into extracellular deposits or in the perinuclear region, comparable to the localization of wildtype cochlin.
* Secretion: PS3_Supporting would be applied if cochlin protein containing the variant does not show secretion from transfected cells, but aggregates in cell regions such as the ER, Golgi and nucleus or is degraded.
* Dimerization: In a non-reducing environment, wildtype cochlin migrate quickly and appear smaller than in the reduced state because the structure is maintained by disulfide bonds. PS3_Supporting would be applied if the cochlin protein containing the variant forms more, or less, stable disulfide bonds when compared to the wildtype in non-reducing conditions.
* If not listed above, OK to use PS3_Supporting for other genes/functional analyses if
  * The assay has been validated by a known pathogenic and benign variant AND  
  * There is plausible reason that the function the assay is testing relates to the phenotype AND
  * The assay conditions are likely to mimic the physiological environment.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：Fisher Exact or Chi-Squared analysis shows statistical increase in cases over controls, OR
Autosomal dominant: ≥15 probands with variant, and variant meets PM2_Supporting.
- **Moderate** 📋：Autosomal dominant: ≥6 probands with variant, and variant meets PM2_Supporting.
- **Supporting** 📋：Autosomal dominant: ≥2 probands with variant, and variant meets PM2_Supporting.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Not Applicable（不适用）**：GN005（Hearing Loss VCEP v2.0，2022-03-30）仅对 KCNQ4（NM_004700.4）孔道区残基 aa271–292 定义可激活 PM1 的突变热点；MYO6（NM_004999.4）无基因特异热点域/关键功能结构域，故 PM1 对本基因不适用。
* ⚠️ 修订说明：本地旧版误将 KCNQ4 孔道区残基 271–292 逐字套用至 MYO6（张冠李戴），已删除；终裁为 PM1 Not Applicable，不得对 MYO6 错义变异激活 PM1。

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Absent/Rare in population databases (absent or ≤0.00007 (0.007%) for autosomal recessive, ≤0.00002 (0.002%) for autosomal dominant).
* Background: Rarity or absence in the general population is not robust evidence for pathogenicity, particularly for autosomal recessive disorders. However, the ACMG/AMP Guidelines were devised in such a way that absence or rarity were considered moderate evidence towards pathogenicity, and the framework requires multiple pieces of evidence to classify a variant as likely pathogenic or pathogenic.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：4 points awarded from tables 7a and 7b
Example: Detected in trans in ≥4 probands with a pathogenic variant (recessive).
- **Strong** 📋：2 points awarded from tables 7a and 7b
Example: Detected in trans in 2 probands with a pathogenic variant (recessive).
- **Moderate** 📋：1 point awarded from tables 7a and 7b.
Example: Detected in trans with a pathogenic variant (recessive).
- **Supporting** 📋：0.5 points awarded from tables 7a and 7b
Examples: Two variants that meet PM2_Supporting detected in trans; OR
a homozygous variant meeting PM2_Supporting.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Protein length change due to an in-frame deletion or insertion that are not located in repetitive regions.
* No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Missense change at same codon as two different pathogenic missense variants.
* Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria for based on independent data)
* Caveat: Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.
- **Moderate** 📋：Missense change at same codon as another pathogenic missense variant.
No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：See PS2 above

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Segregation in three affected relatives for recessive and five affected relatives for dominant.
- **Moderate** 📋：Segregation in two affected relatives for recessive and 4 affected relatives for dominant.
- **Supporting** 📋：Segregation in one affected relative for recessive and two affected relatives for dominant.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan.
* Use REVEL and MAXENTSCAN.
 * For missense variants, award PP3 if REVEL score is ≥0.7.
 * If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3.
* For splice variants (except for canonical -/+1 or 2), use MAXENTSCAN.
 * For -/+ 1 or 2 splice variants, do not use PP3 if you are using PVS1.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** 📋：Patient's phenotype highly specific for gene or fully sequenced gene set (see specifications in Table 7).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：MAF of ≥0.005 (0.5%) for autosomal recessive; MAF of ≥0.001 (0.1%) for autosomal dominant.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：MAF of ≥0.003 (0.3%) for autosomal recessive; MAF of ≥0.0002 (0.02%) for autosomal dominant. Likely benign, provided there is no conflicting evidence.
- **Supporting** 📋：MAF of ≥0.0007 (0.07%) for autosomal recessive. No BS1_Supporting criteria for autosomal dominant.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Observation of variant (biallelic with known pathogenic variant for recessive) in controls inconsistent with disease penetrance.
* Advise caution when using this rule, since most of hearing loss is autosomal recessive, and autosomal dominant hearing loss could display reduced penetrance or variable expression.
* However, if biallelic observations in controls are inconsistent with disease penetrance, this may be applicable.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：Functional study shows no deleterious effect (predefined list).
* Recommend that functional evidence is not used as strong evidence, due to the absence of well-established functional studies for hearing loss genes.
* Guidance on functional evidence at supporting level is as follows (see functional spreadsheets attached):
 * GJB2: electrical coupling assays, dye transfer assays → BS3_Supporting
  * Dye Transfer Assays: Expect results that compare the fluorescence of a variant-transfected cell to both a negative control (or H2O injected control) and a wildtype-transfected cell. BS2_Supporting can be applied if the variant results in dye transfer comparable to the wildtype.
  * Electrical Coupling Assays: Expect results comparing the current of the variant-transfected cells to both a negative control (or H2O injected control) and a wildtype-transfected cell. BS2_Supporting would be applied if the variant results in a current comparable to the wildtype.
 * SLC26A4: Radio isotope and fluorescence assays → BS3_Supporting
  * Radio Isotope Assays: BS3_Supporting would be applied if the variant results in iodide efflux levels comparable to the wildtype.
  * Fluorescence assay: BS3_Supporting would be applied if the variant results in fluorescence comparable to the wildtype
 * COCH: Localization, secretion, and dimerization studies performed using immunofluorescence and Western blotting techniques → BS3_Supporting
  * Localization: BS3_Supporting would be applied if the variant results in extracellular deposits comparable to the wildtype.
  * Secretion: BS3_Supporting would be applied if the variant results in secretion comparable to the wildtype.
  * Dimerization: In a non-reducing environment, wildtype cochlin migrate quickly and appear smaller than in the reduced state because the structure is maintained by disulfide bonds. BS3_Supporting would be applied if the variant results in molecular weight and size comparable to the wildtype.
* If not listed above, OK to use BS3_Supporting for other genes/functional analyses if
 * The assay has been validated by a known pathogenic and benign variant AND
 * There is plausible reason that the function the assay is testing relates to the phenotype AND
 * The assay conditions are likely to mimic the physiological environment.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Non-segregation with disease.
* Phenotype+/genotype-
 * Strong evidence for benign.
 * Be cautious when using this as the possibility for phenocopy is high. The hearing loss phenotype should be consistent within the family to consider it a non-segregation, though intra-familial variability has been reported. Factors to consider are:
  * Age of onset (ie. congenital/early childhood vs. adult onset).
 * Hearing loss prevalence increases significantly with age. A congenital hearing loss in a child and a late onset hearing loss in a grandparent would not be a consistent phenotype.
  * Severity (ie - mild vs. profound).
   * Minor differences may exist among family members.
   * Keep in mind that progression in older individuals may account for a discrepancy between individuals.
  * Sex -based differences (infertility, genes on X chromosomes)
 * Audiogram shape.
  * May not be completely consistent among family members even with same etiology.
* Genotype+/phenotype-
 * Confounding variables to applying this rule: Age-related/sex-related penetrance, variable expressivity, etc.
 * If the gene is associated with later onset and individual with the non-segregation is beyond the expected age that the hearing loss would occur, consider applying BS4_Supporting
 * Recommend only using for fully penetrant genes (typically genes associated with AR hearing loss).
 * Must be confident that patient is truly unaffected and a hearing loss is not missed or subclinical. Be cautious if only phenotyping was newborn hearing screening. Diagnostic audiometric testing (auditory brainstem response (ABR) or audiogram should be required).
 * Any evidence for reduced penetrance, do not use BS4

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in trans with a dominant variant/observed in cis with a pathogenic variant (use with caution).
Use with caution. For genes that are associated with both dominant and recessive hearing loss, consider whether an earlier onset/more severe phenotype could be present if variant is identified in trans with a dominant variant.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** 📋：In-frame indels in repeat region without known function.
No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Computational evidence suggests no impact; REVEL score ≤0.15 or no impact to splicing in MaxEntScan.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：Variant in an autosomal dominant gene found in a patient with an alternate explanation.
* Autosomal recessive: Do not use. An individual could be carrier of pathogenic variant and have an alternate cause. Therefore, BP5 shouldn’t be used as evidence for benign in this case.
* Autosomal dominant: Can use BP5 as outlined by Richards 2015.

 * Caveat: consider whether multiple pathogenic autosomal dominant variants could cause a more severe phenotype or whether multigenic inheritance is known to occur (example: Bardet-Biedl syndrome).

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Silent variant with no predicted impact to splicing.
No changes. Follow recommendations as outlined in Richard 2015 and/or ClinGen's Sequence Variant Interpretation working group.

### 不适用证据码
PP2、PP5、BP1、BP6、PM1
* PM1 不适用原因：GN005 仅对 KCNQ4 定义 PM1（孔区 aa271-292），MYO6 无基因特异热点域/关键功能结构域。

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN005)

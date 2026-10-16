# ClinGen VCEP基因特异性规范：GCK

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v3.1（DOI: 10.5281/zenodo.21434075；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN086 — Monogenic Diabetes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015967**（遗传方式：Semidominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Use _GCK_ PVS1 decision tree created based on PVS1 decision tree from ClinGen SVI group[<sup>1</sup>](#pmid_30096381)

*   Variants generating PTCs 3’ of c.1198 (p.Asp400) of NM\_000162.3, which includes the last 55 nucleotides of exon 9 and exon 10, are not expected to cause NMD[<sup>2</sup>](#pmid_24274751). The α13 helix (p.444-456), located at the C-end of the protein, has a critical role in GCK conformational change upon glucose binding.  Individuals with PTCs in exon 10 have a MODY phenotype. Therefore, a “very strong” level of evidence will be applied for PTCs in exon 10.
*   “Exon skipping or  “use of a cryptic splice site that preserves reading frame” and “Single to multi-exon deletion that preserves reading frame” 
    *   single exon deletions 
        *   deletion of exon 1 is in-frame but over 20 families with GCK-MODY phenotype and exon 1 deletion (some also have promoter deletions) --> PVS1 
        *   deletions of single **exons 2,3,6 and 7** cause frameshift --> **PVS1** 
        *   deletions or skipping of **exons 8 and 9** are in-frame and the proportion is >10 % (52 AA and 78 AA, respectively) --> **PVS1** 
        *   deletions or skipping of **exons 4 and 5** are in-frame and the proportion is \<10 % (40 AA and 32 AA, respectively). Exon 4 (p.122-161) and exon 5 (p.162-193) contain each a part of the active site that binds glucose /p.151-180[<sup>3</sup>](#pmid_23957911) according to Beck et al., Biochemistry 2013/ --> **PVS1** 
        *   deletion of exon 10 (47 AA) – There are a number of patients with a GCK-MODY phenotype with reported with missense, frameshift, PTC, splice acceptor, and stop loss variants in exon 10  --> **PVS1**
*   Apply PVS1\_Supporting to initiation codon variants given MDEP has only reviewed one variant and classified as VUS (c.3G>A, PVS1\_Supporting + PM2\_Supporting; one case submitted, dx.53 and no other info provided to lab).  The next methionine is at codon 8 and there are no variants classified as pathogenic 5' of p.Met8. 
*   Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.
- **Strong** 📋：Use _GCK_ PVS1 decision tree.

Per the SVI standard PVS1 decision tree, apply PVS1\_Strong to duplications ≥ 1 exon in size, contained completely within gene, presumed in tandem, reading frame presumed disrupted, and NMD predicted to occur.
- **Supporting** 📋：Use _GCK_ PVS1 decision tree.

*   Apply PVS1\_Supporting to initiation codon variants given MDEP has only reviewed one variant and classified as VUS (c.3G>A, PVS1\_Supporting + PM2\_Supporting; one case submitted, dx.53 and no other info provided to lab).  The next methionine is at codon 8 and there are no variants classified as pathogenic 5' of p.Met8. 
*   Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.

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
- **Very Strong** 📋：Use SVI-recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Strong** 📋：Use SVI-recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Moderate** 📋：Use SVI-recommended point-based system with specifications for “Phenotype Consistency” per instructions.
- **Supporting** 📋：Use SVI-recommended point-based system with specifications for “Phenotype Consistency” per instructions.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing.
- **Moderate** 📋：See list of approved functional studies and guidelines for interpretation of data.
- **Supporting** 📋：See list of approved functional studies and guidelines for interpretation of data (below).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：7 or more occurrences in unrelated individuals = Strong.
- **Moderate** 📋：4-6 occurrences in unrelated individuals = Moderate.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：Applicable for glucose- and ATP-binding sites (see attached chart for details).

Glucose-binding sites:  Ser151 - Pro153; Thr168 - Lys169;  Asn204 - Thr206; Ile225 - Asn231; Asn254 - Gly258; Gln287; Glu290

ATP-binding sites:  Asp78 - Arg85; Ser151; Lys169; Asp205; Ile225 - Gly229; Gly295 - Lys296; Glu331 - Arg333; Ser336; Gly410 - His416

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：gnomAD Grpmax FAF ≤ 1:333,000 (≤ 0.000003 or 0.0003%)

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：Use SVI-recommended point-based system.
- **Strong** 📋：Use SVI-recommended point-based system.
- **Moderate** 📋：Use SVI-recommended point-based system.
- **Supporting** 📋：Use SVI-recommended point-based system.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：For deletions/insertions of more than one amino acid in a non-repeat region, use as moderate level of evidence.
- **Supporting** 📋：Apply at the Supporting level when there is an insertion or deletion of a single amino acid in a non-repeat region.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Applicable once two amino acid changes have been classified as pathogenic at the same amino acid residue.
- **Moderate** 📋：The novel amino acid change must have a Grantham distance greater than or equal to the previously classified pathogenic variant.
- **Supporting** 📋：Apply if the previously classified amino acid change is likely pathogenic (rather than pathogenic) or if the previously classified variant is pathogenic but has a greater Grantham distance.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/32 (5 meioses)
*   \>1 Family : ≤ 1/16 (4 meioses)
- **Moderate** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/16 (4 meioses)
*   \>1 Family : ≤ 1/8 (3 meioses)
- **Supporting** 📋：Use thresholds suggested by Jarvik and Browning[<sup>8</sup>](#pmid_27236918)

*   Single Family : ≤ 1/8 (3 meioses)
*   \>1 Family : ≤ ¼ (2 meioses)

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** 📋：Apply to all missense variants in GCK. gnomAD missense constraint score for _GCK_ is 3.07 (observed/expected= 0.5), which is significant.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use REVEL score of ≥0.70 as supportive evidence of pathogenicity. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is at least 0.2[<sup>9</sup>](#pmid_32123317),[<sup>10</sup>](#pmid_30661751)

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** 📋：HbA1C 5.6 – 7.6% (38-60 mmol/mol) (if given multiple results, use maximum value) AND fasting plasma glucose always (FPG) 5.5-8 mmol/L (100-144 mg/dL) AND presence of any of the following additional features:

*   Pediatric patient (prepubertal or \<10 years) (picked up in the absence of symptoms, either incidentally during workup for an unrelated indication or during routine screening)
*   Multiple values (=persistent) of mild fasting hyperglycemia in PP4 range
    *   Either (≥ 1 HbA1c + ≥ 2 FPG) OR (≥ 2 HbA1c + ≥ 1 FPG)
    *   Only 1 HbA1c and 1 FPG in range but they are at least 6 months apart
    *   Patient in literature is described as having a multi-year history of impaired fasting glucose (IFG)
*   OGTT (oral glucose tolerance test) with 2-hour increment \<3 mmol/L (54 mg/dl) 
*   Antibody negative 
*   Macrosomia in normoglycemic offspring of hyperglycemic gestational parent
*   Low birthweight in hyperglycemic offspring of hyperglycemic gestational parent. 
*   Three-generation, dominant family history of diabetes or hyperglycemia (in a family not used for PP1)
- **Supporting** 📋：HbA1C 5.6 – 7.6% (38-60 mmol/mol) (if given multiple results, use maximum value) AND fasting plasma glucose always (FPG) 5.5-8 mmol/L (100-144 mg/dL)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：gnomAD Grpmax FAF ≥ 1:25,000 (0.004% or 0.00004)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：We expect to see hyperglycemia at birth in an individual with \_GCK\_-MODY and therefore consider an individual unaffected if euglycemic in childhood or adulthood.  Since individuals typically do not present with symptoms of diabetes, evidence that someone is “nondiabetic” is insufficient; fasting glucose must be tested and found to be within normal limits (\<100 mg/dl / 5.5 mmol/L).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of normal splicing (see BP4).
- **Supporting** 📋：Use GCK PS3 decision tree, which incorporates the relative activity index (RAI), relative stability index (RSI) and assays that measure the impact of variants on binding with GKRP and GKA.

Evidence of no impact on function:

*   Normal RAI (>0.5) + normal RSI (>0.5) + normal inhibition/activation with GKRP/GKA = BS3\_Supporting 
*   Normal RAI (>0.5) + normal RSI (>0.5) but no studies investigating GKRP/GKA = Cannot use PS3 or BS3

Gloyn, et al. 2005 [<sup>5</sup>](#pmid_15677479); Beer, et al. 2012 [<sup>6</sup>](#pmid_22611063); Raimondo, et al. 2014 [<sup>7</sup>](#pmid_25015100); Gloyn, et al. (2004)<sup>12</sup>.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Applicable to family members without variant who meet PP4 criteria (HbA1C 5.6 – 7.6% (38-60 mmol/mol) (if given multiple results, use maximum value) AND Fasting glucose 5.5-8 mmol/L (100-144 mg/dL))

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Also applicable when in cis or trans with a likely pathogenic variant.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use a REVEL score of ≤0.15 as supportive evidence of no predicted impact on the gene or gene product. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is below 0.2[<sup>9</sup>](#pmid_32123317),[<sup>10</sup>](#pmid_30661751).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：A variant in another monogenic diabetes gene is P/LP.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：Apply BP7 when the predicted change from SpliceAI is below 0.2 AND phyloP100 way \< 2.0.

### Rules for Combining Criteria

#### Pathogenic
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

#### Likely Pathogenic
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate

#### Benign
- ≥ 2 Strong
- 1 Stand Alone

#### Likely Benign
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PM6、PP5、BP1、BP3、BP6
### 参考附件
- [PS2 De Novo Points Table](https://cspec.genome.network/cspec/File/id/29b148f7-9fd0-40d8-87cd-e89b0e16cff7/data)
- [GCK Points Table for PM3](https://cspec.genome.network/cspec/File/id/0c32d973-6ca8-4d0f-b0b4-9b3a40a0ac11/data)
- [GCK PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/e837f420-840c-4de8-bbf1-17104bdae0a8/data)
- [GCK PM1 Residues](https://cspec.genome.network/cspec/File/id/c85251f4-45f4-475d-bfa8-bb2c4003c177/data)
- [GCK PS3/BS3 Decision tree](https://cspec.genome.network/cspec/File/id/d1e22508-52a7-435b-9842-4d952d34a017/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN086)

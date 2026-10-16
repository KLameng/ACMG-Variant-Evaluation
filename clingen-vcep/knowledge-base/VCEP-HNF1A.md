# ClinGen VCEP基因特异性规范：HNF1A

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN017 — Monogenic Diabetes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015967**（遗传方式：未指定）

### 官网版本
- Version 3.1（Released）
- DOI: 10.5281/zenodo.21421568（https://doi.org/10.5281/zenodo.21421568）
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
- **Very Strong** 📋：Use HNF1A PVS1 decision tree.

*   Apply PVS1 to nonsense or frameshift variants occurring 5' of c.1768. 
    *   Variants generating PTCs 3’ of c.1714 of NM\_000545.8, which includes the last 55 nucleotides of exon 9 and all of exon 10, are not expected to cause NMD [<sup>2</sup>](#pmid_24274751). The transactivation domain (TAD) of the protein overlaps with this region. The last 55 nucleotides of exon 9 (c.1714-1768) is enriched for disease-causing variants and loss-of function variants in this region have been found in patients/families with a MODY phenotype. Therefore, a “very strong” level of evidence will be used for loss-of-function variants 5’ of c.1768 regardless of where the premature termination codon occurs.
*   “Exon skipping or use of a cryptic splice site that preserves reading frame” and “Single to multi-exon deletion that preserves reading frame”
    *   Apply PVS1 for exon skipping or single to multi exon deletion involving exons 1-9
        *   Deletions of exon 1 would lead at least to loss of the initiation codon (see below for recommendations for initiation codon variants). Deletions of single exons 2, 3, 4, 5, 6, 8 or 9 all cause frameshift, and thus PVS1 would be used. In HNF1A, only exon 7 (LRG\_522t1) is surrounded by introns of the same phase. Skipping or deletion of exon 7 would remove 64 amino acids in the TAD, which is >10% of the protein and 18% of the TAD. Given the significance of the TAD, we support still using PVS1 instead of PVS1\_Strong in this situation.
*   Apply PVS1 to initiation codon variants. Four initiation codon variants have been identified in patients with a MODY phenotype. The closest potential in-frame start codon is p.Met118. Starting the protein at p.Met118 would remove 18% of the protein, including the entire dimerization domain. There are many P/LP variants upstream of p.Met118.
*   Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.
- **Strong** 📋：Use HNF1A PVS1 decision tree.

*   Apply PVS1\_Strong for nonsense variants at c.1803 (p.601) and 5’ and frameshift variants at c.1854 (p.618) and 5’. 
    *   The distinction of nonsense and frameshift variants was made following a careful review of the phenotypes of individuals with loss-of-function variants in exon 10, which lead to our prediction that the addition of new amino acids from a frameshift will disrupt the TAD and cause a MODY phenotype more so than the deletion of a small part of the end of the TAD. Moderate phenotypic evidence was applied to the c.1802del (p.601Ter) variant, but the individual with the next nonsense variant (p.Gln625Ter) was unaffected. Frameshift variants at p.Ile618 and 5’ have been identified in patients with a phenotype consistent with MODY.
*   “Exon skipping or use of a cryptic splice site that preserves reading frame” and “Single to multi-exon deletion that preserves reading frame”
    *   Apply PVS1\_Strong for deletions of exon 10 and splicing variants that would predict the skipping of exon 10.
        *   A deletion of exon 10 would remove part of the TAD but less than 10% of the protein. Since the TAD is critical to protein function, and variants that disrupt all of exon 10 have been found in patients with a MODY phenotype, we will use  This specification is in accordance with Tayoun’s recommendation to use PVS1\_Strong in cases in which the truncated region is critical to protein function.[<sup>17</sup>](#pmid_30192042)

Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.
- **Supporting** 📋：Use HNF1A PVS1 decision tree.

*   Apply PVS1\_Supporting levels for nonsense variants occurring 3’ of c.1803 (p.601) and frameshift variants occurring 3’ of c.1854 (p.618) as there is limited evidence of patients with MODY phenotype at this time.

Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：Applicable for a same amino acid change if the previously established variant is classified as pathogenic by ClinGen MDEP specifications.

PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.[<sup>3</sup>](#pmid_37352859)
- **Moderate** 📋：Applicable for a same amino acid change if the previously established variant is classified as likely pathogenic by ClinGen MDEP specifications.

PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.[<sup>3</sup>](#pmid_37352859)
- **Supporting** 📋：PS1 can also be applied for canonical and non-canoncial splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparision (likely) pathogenic variant. See Table 2 from [PMID: 37352859](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357475/table/tbl2/) for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.[<sup>3</sup>](#pmid_37352859)

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” described in PP4 specifications.
- **Strong** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” described in PP4 specifications.
- **Moderate** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” described in PP4 specifications.
- **Supporting** 📋：Use SVI recommended point-based system with specifications for “Phenotype Consistency” described in PP4 specifications.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing.
- **Moderate** 📋：Currently applicable for variants with luciferase assay data (evidence of decreased transactivation (≤ 40% of wild type) by the Gloyn/Oxford group[<sup>10</sup>](#pmid_32910913) ([Althari et al. 2020).](https://pubmed.ncbi.nlm.nih.gov/32910913/)  This upgrade from supporting is based on a validation conducted according to the guidelines by Brnich et al. 2019 [<sup>1</sup>](#pmid_31892348).
- **Supporting** 📋：PS3 should be applied at the supporting level for the following approved functional studies and cutoffs except as noted in the PS3\_Moderate specification: 

1.  Luciferase assays for transactivation: less than 40% activity of wildtype (WT). Assays should include controls for WT, T2DM-risk, and known MODY variants. 
2.  EMSA for DNA binding: less than 40% activity of WT. We recommend that at least two of the following variants be used as positive controls for reduced DNA binding activity: c.335C>T (p.Pro112Leu), c.608G>A (p.Arg203His), c.787C>T (p.Arg263Cys) and c.686G>A (p.Arg229Gln) [<sup>4</sup>](#pmid_11162430), [<sup>5</sup>](#pmid_12574234), [<sup>6</sup>](#pmid_24915262). 
3.  Western blotting and indirect immunofluorescence for protein expression and localization - Determining appropriate thresholds for protein expression is more difficult due to variability in results between experimental protocols. Altered protein expression can be indirectly captured through the read-out frame from transactivation assay, and reduced protein expression can provide an explanation for reduced transactivation. When exploring protein mis-localization, we recommend that the c.589\_615del (p.Lys197\_Lys205del) variant is included as a positive control for impaired nuclear localization (cytosolic retention).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：Seven or more unrelated occurrences = Strong.
- **Moderate** 📋：4-6 unrelated occurrences = Moderate.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：This criterion can be used for variants in residues that directly bind DNA:   Gln130, Arg131, Glu132, His143, Leu144, Ser145, Gln146, His147, Leu148, Asn149, Lys155, Thr156, Gln157, Lys158, Arg203, Phe204, Lys205, Trp206, Arg263, Val264, Tyr265, Asn270, Arg271, Arg272, Lys273
- **Supporting** 📋：Use for defined regions in the DNA binding and dimerization domains.

*   Dimerization: codons 1-32, NM\_000545.8
*   Subset of DNA binding domains: codons 107-174 and 201-280

It can also be used for variants within certain transcription factor binding sites of the promoter:

*   –c.-187 to c.-195 (AP1 binding site)
*   –c.-209 to c.-227 (Overlapping HNF3 & NF-Y sites)
*   –c.-238 to c.-259 (HNF1A binding site)
*   –c.-276 to c.-288 (HNF4A binding site)

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
- **Strong** 📋：Applicable once two amino acid changes have been classified as pathogenic at the same amino acid residue
- **Moderate** 📋：The novel amino acid change must have a Grantham distance greater than or equal to the previously classified pathogenic variant.
- **Supporting** 📋：Apply if the previously classified amino acid change is likely pathogenic (rather than pathogenic), or if the previously classified variant is pathogenic but has a greater Grantham distance.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：Use thresholds suggested by Jarvik and Browning[<sup>7</sup>](#pmid_27236918)

*   Single Family : ≤ 1/32 (5 meioses)
*   \>1 Family : ≤ 1/16 (4 meioses)
- **Moderate** 📋：Use thresholds suggested by Jarvik and Browning[<sup>7</sup>](#pmid_27236918)

*   Single Family : ≤ 1/16 (4 meioses)
*   \>1 Family : ≤ 1/8 (3 meioses)
- **Supporting** 📋：Use thresholds suggested by Jarvik and Browning[<sup>7</sup>](#pmid_27236918)

*   Single Family : ≤ 1/8 (3 meioses)
*   \>1 Family : ≤ ¼ (2 meioses)

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use REVEL score of ≥0.70 as supportive evidence of pathogenicity. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is above 0.2[<sup>8</sup>](#pmid_32123317),[<sup>9</sup>](#pmid_30661751).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** 📋：MODY Probability Calculator (MPC) result ≥50% chance of testing positive [https://www.diabetesgenes.org/mody-probability-calculator/](https://www.diabetesgenes.org/mody-probability-calculator/)) AND negative HNF4A testing AND presence of at least one additional feature characteristic of HNF1A-MODY:

*   Antibody negative and/or persistent C-peptide after five years post-T1DM diagnosis
*   Response to low-dose sulfonyurea (SU) (extreme response- hypoglycemia)
*   Low hsCRP in patient with clinical diagnosis of T2DM
*   Biochemical/Molecular phenotypic evidence from patient cell lines
*   Hepatocellular adenomas
- **Supporting** 📋：MODY Probability Calculator (MPC) result ≥50% chance of testing positive https://www.diabetesgenes.org/mody-probability-calculator/) AND negative HNF4A testing

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：gnomAD Grpmax FAF ≥ 1:30,000 (≥0.0033% or 0.000033)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Apply to normoglycemic individuals age 70 or older (i.e., genotype positive, phenotype negative)

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Applicable to non-canonical splice site variants that have RNA and in silico evidence of normal splicing.
- **Supporting** 📋：BS3 should be applied at the supporting level for the following approved functional studies and cutoffs: 

1.  Luciferase assays for transactivation: ≥ 75% activity of wildtype 
2.  EMSA for DNA binding:  ≥ 75% activity of wildtype. 
3.  Western blotting and indirect immunoflorescence for protein expression and localization - Determining appropriate thresholds for protein expression is more difficult due to variability in results between different experimental protocols. Altered protein expression can be indirectly captured through the read-out from a transactivation assay and reduced protein expression can provide an explanation for reduced transactivation.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Applicable to family members without variant who have MPC score >50% (i.e., genotype negative, phenotype positive).

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Also applicable when in cis or trans with a likely pathogenic variant.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：Use a REVEL score of ≤0.15 as supportive evidence of no predicted impact on the gene or gene product. We also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is below 0.2 [<sup>8</sup>](#pmid_32123317),[<sup>9</sup>](#pmid_30661751).

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：A variant in other monogenic diabetes gene is P/LP.

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
- 1 Very Strong AND 1 Supporting

**Benign（良性）**
- ≥ 2 Strong
- 1 Stand Alone

**Likely Benign（可能良性）**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PM3、PM6、PP2、PP5、BP1、BP3、BP6
### 参考附件
- [PS2 De Novo Points Table](https://cspec.genome.network/cspec/File/id/667441fd-a7cb-4a92-8592-86b8a0377c79/data)
- [HNF1A (NM_000545.8) PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/5af96ed6-b35b-4704-be42-fe069d5e7426/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN017)

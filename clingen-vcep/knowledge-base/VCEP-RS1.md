# ClinGen VCEP基因特异性规范：RS1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 1.0（DOI: 10.5281/zenodo.21434644；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN126 — X-linked Inherited Retinal Disease Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010725**（遗传方式：X-linked inheritance）

### 通用说明
In addition to the specific criteria for codes listed below, the VCEP has adopted the point-based combining scoring in Table 2 and Table 3 of PMID: 32720330. Table 2 assigns points for pathogenic (0 for indeterminate, 1 for supporting, 2 for moderate, 4 for strong, and 8 for very strong), and benign (0 for indeterminate, -1 for supporting, -2 for moderate, -4 for strong, and -8 for very strong) codes. Table 3 provides final categories of Pathogenic (>= 10), Likely Pathogenic (6-9), Uncertain (0-5), Likely Benign (-1 to -6), Benign (<=-7). This replaces the combining rules listed below.  
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use attached RS1-specific PVS1 Decision Tree file, which has been modified from Abou Tayoun, et al., 2018 (PMID 30192042) and incorporates splice site guidance from Walker et al, 2023 (PMID 37352859). This strength applies to nonsense, frameshift, splice site, and deletion variants in NM\_000330.4 c.1A to c.671C (p.Met1 to p.Cys223) and to duplications in NM\_000330.4 c.1 to c. 472 (p.Met1 to p.Asp158).

The structure of RS1 is important for function. The RS1 monomers have  cystine disulfide bonds within a RS1 monomer and bonds with the two neighboring monomers to form an octomer substructure and bonds to the second RS1 octomer that completes the paired octomer structure. Within this structure there are a number of sites that have been shown to function in other types of protein structure stabilization.
- **Strong** ✅：Use attached RS1-specific PVS1 Decision Tree file, which has been modified from Abou Tayoun, et al., 2018 (PMID 30192042) and incorporates splice site guidance from Walker et al, 2023 (PMID 37352859).  

This strength applies to frameshift variants, GT--AG splice variants, deletions, duplications or nonsense variants  in NM\_000330.4 c.672 to c.677 (p.Asp224 to p.\*225).
- **Moderate** ✅：Use attached RS1-specific PVS1 Decision Tree file, which has been modified from Abou Tayoun, et al., 2018 (PMID 30192042) and incorporates splice site guidance from Walker et al, 2023 (PMID 37352859).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established **Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as a Pathogenic variant and classified as such. For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

When evaluating splicing impact, as a previously classified Pathogenic variant, 

*   Use in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated **Pathogenic**.
*   Used in conjunction with PVS1 for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide that has been designated **Pathogenic**.

Specific combinations are found in RS1-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).
- **Moderate** ✅：Same amino acid change as a previously established **(Likely) Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as a Likely Pathogenic variant and classified as such. For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other. 

When evaluating splicing impact, with a previously classified Likely Pathogenic or Pathogenic variant, 

*   Use in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated **Likely Pathogenic**.
*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and have a comparable nucleotide variant within the same splice region with the same predicted impact that has been designated **Pathogenic**.
*   Use in conjunction with PVS1 at any strength for variants located within splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and a comparable nucleotide variant within the same splice motif region but outside the donor/acceptor +/-1,2 dinucleotide positions with the same predicted impact that has been designated **Pathogenic**.

Specific combinations are found in RS1-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).
- **Supporting** ✅：Same amino acid change as a previously established **(Likely) Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as a Likely Pathogenic variant and classified as such. For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other. 

When evaluating splicing impact, with a previously classified Likely Pathogenic variant, 

*   Use in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and have a comparable nucleotide variant variant within the same splice motif region but outside the donor/acceptor +/-1,2 dinucleotide positions with the same predicted impact that has been designated **Likely Pathogenic**.
*   Used in conjunction with PVS1 for variants located within the splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and have a comparable nucleotide variant at the same splice donor/acceptor +/-1,2 dinucleotide position with the same predicted impact that has been designated **Pathogenic**.
*   Use in conjunction with PVS1 for variants located within splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and a comparable nucleotide variant within the same splice motif region but outside the donor/acceptor +/-1,2 dinucleotide positions with the same predicted impact that has been designated either **Likely Pathogenic** or **Pathogenic**.
*   Use in conjunction with PVS1 at any strength for variants located within splice donor/acceptor +/-1,2 dinucleotide positions that have a SpliceAI score ≥0.2 and a comparable nucleotide variant within the same splice motif region but outside the donor/acceptor +/-1,2 dinucleotide positions with the same predicted impact that has been designated **Likely** **Pathogenic**.

Specific combinations are found in RS1-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 1 “Phenotype highly specific for gene.” Confirmed _de novo_ with confirmed maternity worth 2.0 points per proband. Assumed _de novo_ with assumed maternity worth 1.0 points per proband. Total 4.0 points to use at the very strong strength.
- **Strong** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 1 “Phenotype highly specific for gene.” Confirmed _de novo_ with confirmed maternity worth 2.0 points per proband. Assumed _de novo_ with assumed maternity worth 1.0 points per proband. Total 2.0 points to use at the strong strength.
- **Moderate** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 1 “Phenotype highly specific for gene.” Confirmed _de novo_ with confirmed maternity worth 2.0 points per proband. Assumed _de novo_ with assumed maternity worth 1.0 points per proband. Total 1.0 points to use at the moderate strength.
- **Supporting** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 1 “Phenotype highly specific for gene.” Confirmed _de novo_ with confirmed maternity worth 2.0 points per proband. Assumed _de novo_ with assumed maternity worth 1.0 points per proband. Total 0.5 points to use at the supporting strength.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Variants tested in high quality knock-out/knock-in variant mouse lines can meet PS3 at the strong level.
- **Supporting** ✅：Use at the supporting strength for most assays (see Functional Assays Table).

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Use of this code requires 9 or more probands, each with retinoschisis. PM2\_Supporting must be met.
- **Strong** ✅：Use of this code requires 5-8 probands, each with retinoschisis. PM2\_Supporting must be met.
- **Moderate** ✅：Use of this code at the moderate strength requires 3-4 probands diagnosed with retinoschisis. PM2\_Supporting must be met.
- **Supporting** ✅：Use of this code at the supporting strength requires 1 proband diagnosed with retinoschisis, and a second proband answering the PP4 requirements. PM2\_Supporting must be met.

Or 2 probands, each with retinoschisis. PM2\_Supporting must be met.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** ✅：Applies to variants in amino acids p.Cys40, p.Cys59, p.Cys63, p.Cys110, p.Cys142, p.Cys219, and p.Cys223 which form disulfide bridges required for structure of the retinoschisin monomer, dimers, or octamers.
- **Moderate** ✅：Applies to amino acids p.Glu72, p.Trp122, p.Trp163, p.Arg200, p.Glu215 which form salt bridges that are required for higher order structure of octamers and paired octamers.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：At low frequency in males in population databases. Use \<2.0x10<sup>-6 </sup> for cut off. This is defined relative to the BA1 cutoff.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：In-frame deletion/insertions smaller than one whole exon, in a non-repetitive region, or stop-loss variants. Variant must not be considered in any PVS1 criteria. Variant must also meet PM2.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Same residue as a previously established pathogenic variant classified using these specifications (assessed independently of PM5) . 

The novel change must not affect splicing (SpliceAI ≤ 0.2), must meet PP3, and have a Grantham score equal or greater than the previously published variants.
- **Supporting** ✅：Same residue as a previously established likely pathogenic variant classified using these specifications (assessed independently of PM5) . 

The novel change must not affect splicing (SpliceAI ≤ 0.2), must meet PP3, and have a Grantham score equal or greater than the previously published variants.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Use of this code requires ≥3 meioses in 1 or 2 families.

Only phenotype positive male relatives with the same variant identified in the proband should be counted as segregations.
- **Moderate** ✅：2 meioses in a family (e.g. 2 brothers and mother genotyped; 3 brothers without mother's genotype; or uncle and nephew)

Only phenotype positive male relatives with the same variant identified in the proband should be counted as segregations.
- **Supporting** ✅：1 meiosis in a family

Only phenotype positive male relatives with the same variant identified in the proband should be counted as segregations.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：Applies to missense variants with a REVEL score above 0.931, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the strong level.
- **Moderate** ✅：Applies to missense variants with a REVEL score between 0.773 and 0.931, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the moderate level.
- **Supporting** ✅：Applies to missense variants with a REVEL score between 0.644 and 0.772 that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：A male proband diagnosed with retinoschisis by the age of 13 with visual acuity impairment, showing schisis, and having retinal detachment.
- **Supporting** ✅：A male proband diagnosed with retinoschisis by the age of 13 with visual acuity impairment and showing schisis.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency ≥ 2x10<sup>-4</sup> in males in population databases (Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium) in the subpopulation with the highest frequency.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency ≥ 2x10<sup>-5</sup> in males in population databases.  
\- The highest allele frequency in population databases should be used

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Only count males over age 30 with a documented eye exam without retinoschisis.

BS2\_strong for variants observed in at least 3 unaffected males.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Supporting** ✅：Paternal inheritance is inconsistent with this gene. For RS1, unaffected males over age 10 who have been examined could be used to establish this code if they have no schisis and good acuity.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：**Stand Alone** criteria applies to:

Missense variants: REVEL ≤ 0.003 with SpliceAI ≤ 0.1

**Strong criteria** applies to:

Missense variants: REVEL between 0.004 and 0.016 with SpliceAI ≤ 0.1
- **Moderate** ✅：Applies to:

Missense variants: REVEL between 0.017 and 0.183 with SpliceAI ≤ 0.1
- **Supporting** ✅：Applies to:

Missense variants: REVEL between 0.184 and 0.290 with SpliceAI ≤ 0.1

or 

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Applies to splicing assay data demonstrating a variant is not associated with aberrantly spliced transcript(s) relative to transcript profiles in controls. See RS1 PVS1 Decision Tree.  As per Walker et al, 2023 (PMID 37352859) guidance.
- **Supporting** ✅：Applies to:

Synonymous variants or noncoding variants  with no impact on splicing (SpliceAI ≤ 0.1)

AND

PhyloP \< 0.1 for conservation

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
PM3、PM6、PP2、PP5、BS3、BP1、BP2、BP3、BP5、BP6
### 参考附件
- [RS1 Functional Evidence Assays for PS3 / BS3](https://cspec.genome.network/cspec/File/id/91284dd8-4d07-4d8a-854f-557aa1687a38/data)
- [RS1 PS2/PM6 Tables](https://cspec.genome.network/cspec/File/id/b18d6e1a-2677-4779-aefe-0a0d4e1bff25/data)
- [RS1 PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/c13b7566-09d0-4f42-ba20-922cae964c9a/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN126)

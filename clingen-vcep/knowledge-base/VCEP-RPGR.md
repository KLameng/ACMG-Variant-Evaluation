# ClinGen VCEP基因特异性规范：RPGR

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 1.0（Released；DOI 10.5281/zenodo.21434377；X-linked Inherited Retinal Disease VCEP；核验 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN106 — X-linked Inherited Retinal Disease Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100437**（遗传方式：X-linked inheritance）

### 通用说明
In addition to the specific criteria for codes listed below, the VCEP has adopted the point-based combining scoring in Table 2 and Table 3 of PMID: 32720330. Table 2 assigns points for pathogenic (0 for indeterminate, 1 for supporting, 2 for moderate, 4 for strong, and 8 for very strong), and benign (0 for indeterminate, -1 for supporting, -2 for moderate, -4 for strong, and -8 for very strong) codes. Table 3 provides final categories of Pathogenic (>= 10), Likely Pathogenic (6-9), Uncertain (0-5), Likely Benign (-1 to -6), Benign (<=7).       
There are two transcripts for RPGR:  NM_001034853.2 is the retinal specific transcript for which the gene-disease association has been defined and NM_000328.3 which is more broadly expressed in other tissues. The two transcripts overlap for exons 1 to 15.  NM_001034853.2 reads through the exon 15 terminal splice site and continues into ORF15.  NM_000328.3 splices from exon 15 to exon 16 and includes exons 16 to 19. These rules have been specified for the ORF15 transcript with ACMG/AMP default specifications for NM_000328.3 exons 16 to 19.
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Use SVI recommendations (PMID 30192042, and PMID 37352859) with modifications as shown in the RPGR PVS1 Decision Tree with splice guidance figures attached.

[**NM\_001034853.2**](https://www.ncbi.nlm.nih.gov/nuccore/NM_001034853.2/) **\-** Transcript isoform C reads through the splice site at the end of exon 15 (ORF15) creating a longer protein sequence with a repetitive region in the 3’ end. This is the transcript expressed in retina.

[**NM\_000328.3**](http://www.ncbi.nlm.nih.gov/nuccore/NM_000328.3) **\-** Transcript isoform A includes 19 exons and produces a shorter mRNA and protein sequence than isoform C. Variants in exons 16 to 19 are not associated with RPGR-related retinopathy.

**PVS1\_Met** designation for variants predicted to undergo NMD, nonsense or frameshift variants that disrupt the critical function of glutamylation in ORF15, or variants causing skipped or deleted exons that affect regions critical to protein function.
- **Strong** ✅：PVS1\_Strong designation for variants that remove more than 10% of the protein and are not expected to lead to NMD.
- **Moderate** ✅：PVS1\_Moderate designation for initiation codon variants with upstream pathogenic variants of closest potential in-frame start codon or for variants in NM\_00328.3 which remove  less than 10% of the protein and are not expected to lead to NMD.
- **Supporting** ✅：PVS1\_Supporting designation for initiation codon variants without upstream pathogenic variants of closest potential in-frame start codon.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established Pathogenic variant regardless of nucleotide change.

*   Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as a pathogenic variant and classified as such.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

Same predicted splicing impact as a previously classified Pathogenic variant.

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated Pathogenic.
*   Used in conjunction with PVS1 for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide that has been designated Pathogenic.  
    Specific combinations are found in \_RPGR\_-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).
- **Moderate** ✅：Same amino acid change as a previously established Likely Pathogenic variant regardless of nucleotide change.

*   Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as likely pathogenic variant and classified as such.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

Same predicted splicing impact as a previously classified Pathogenic variant.

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated Likely Pathogenic.
*   Used in conjunction with PVS1\_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor motif (but outside of the +/-1,2 dinucleotide) that has been designated Pathogenic.  
    Specific combinations are found in \_RPGR\_-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).
- **Supporting** ✅：*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant within the same motif that has been designated Likely Pathogenic.
*   Used in conjunction with PVS1 or PVS1\_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and have a comparable Likely Pathogenic or Pathogenic variant either within the same splice site donor/acceptor motif, outside the +/-1,2 dinucleotide, or at the +/-1,2 dinucleotide.

Specific combinations are found in \_RPGR\_-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 3 “Phenotype consistent with gene but not hightly specific and high genetic heterogeneity.” Confirmed _de novo_ with confirmed maternity worth 0.5 points per proband. Total 4.0 points to use at the very strong strength.
- **Strong** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 3 “Phenotype consistent with gene but not hightly specific and high genetic heterogeneity.” Confirmed _de novo_ with confirmed maternity worth 0.5 points per proband. Assumed de novo with assumed maternity worth 0.25 points per proband. Total 2.0 points to use at the strong strength.
- **Moderate** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 3 “Phenotype consistent with gene but not hightly specific and high genetic heterogeneity.” Confirmed _de novo_ with confirmed maternity worth 0.5 points per proband. Assumed de novo with assumed maternity worth 0.25 points per proband. Total 1.0 points to use at the moderate strength.
- **Supporting** ✅：Use SVI point scale for counting cases (see Table 1 on PS2\_PM6 table), use option 3 “Phenotype consistent with gene but not hightly specific and high genetic heterogeneity.” Confirmed _de novo_ with confirmed maternity worth 0.5 points per proband.  Assumed de novo with assumed maternity worth 0.25 points per proband. Total 0.5 points to use at the supporting strength.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：Assays with OddsPath >2.1 as per the SVI recommendations<sup>1</sup>

Applies to the following functional studies:

*   Protein-protein interaction (PMIDs: 30622176, 20631154, 10958648, 23213406, 9990021, 36445968)
*   Protein localization to connecting cilia (PMIDs: 30622176, 25630948).
*   Glutamylation assays (only applicable to truncating variants in exon 15, PMIDs: 27162334, 36445968)

> ⚠️ 官网自身矛盾（2026-10-09 核验）：本码在 cspec 页面同时存在可见 Supporting 强度文本（如上，含 OddsPath>2.1 与试验清单）与 hidden 注释 "NA-NOTE(hidden): This code is not currently applicable."。按"可见内容为有效规则"原则转录可见文本，hidden 注释为平台录入残留，仅供参考。

\-OR-

Animal models that replicate the phenotype.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：Use of this code requires ≥ 8 probands and PM2\_Supporting must be met.
- **Strong** ✅：Use of this code requires ≥ 6 probands and PM2\_Supporting must be met.
- **Moderate** ✅：Use of this code at the moderate strength requires 3-5 probands and PM2\_Supporting must be met.
- **Supporting** ✅：Use of this code at the supporting strength requires ≥ 2 probands and PM2\_Supporting must be met.

OR

**If PS4 Met at the PS4\_Supporting level by 1 proband (when a separate unrelated proband has been used for PP4):**

This variant has been reported in at least 1 proband meeting one of the PS4 requirements of a male with some functional vision impairment by age 30 and/or decreased or absent ERG responses, or a female with functional visual abnormality and documentation of a male relative affected with retinitis pigmentosa, as well as a second apparently unrelated proband previously used for the PP4 code.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Allele frequency in males ≤ 0.00005 (≤5x10<sup>-5</sup>) in population databases.

*   Highest allele frequency in a subpopulation should be used to assess this.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：Use for stop loss variants in aa 1153. These variants will produce a 38 amino acid extension which was shown to have a deleterious effect (PMID:33805381, variant in c.3457).
- **Moderate** ✅：Protein length changes in exons 1-14, due to in-frame deletions/insertions in a non-repeat region. Or, in ORF15 outside of the repetitive region in amino acids 585 to 1078, due to in-frame deletions/insertions in a non-repeat region.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Must have 2 comparison variants reaching pathogenic classification using these specifications. 

\- The novel change must not affect splicing (SpliceAI ≤ 0.2), must meet PP3, and have a Grantham score equal to or greater than the previously published variants.
- **Supporting** ✅：Same residue as a previously established likely pathogenic variant (assessed independently of PM5).

\- The novel change must not affect splicing (SpliceAI ≤ 0.2), must meet PP3, and have a Grantham score equal to or greater than the previously published variants.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Use of this code requires ≥4 meioses in >1 family

Only phenotype positive relatives with the same variant identified in the proband should be counted as segregations.
- **Moderate** ✅：≥ 3 meioses

In ≥ 1 families

Only phenotype positive relatives with the same variant identified in the proband should be counted as segregations.
- **Supporting** ✅：≥ 2 meioses in the same family

OR proband with affected mother

Only phenotype positive relatives with the same variant identified in the proband should be countedas segregations.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：Applies to missense variants with a REVEL score above 0.932, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the strong level.
- **Moderate** ✅：Applies to missense variants with a REVEL score between 0.773 and 0.931, that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2). This criteria is met at the moderate level.
- **Supporting** ✅：Applies to missense variants with a REVEL score between 0.644 and 0.772 that are not predicted to disrupt splicing (with a SpliceAI score less than 0.2).

For variants with SpliceAI scores greater than or equal to 0.2, in the two first or last two bases in an exon or the 6 intronic bases flanking an exon, this code is met at the supporting level.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：\> 8 phenotype points required; two specific criteria must be met
- **Supporting** ✅：4-7 phenotype points required; one specific criterion must be met.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency in males is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium in the subpopulation with the highest frequency.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency in males is greater than expected for the disorder. Use for alleles with frequency ≥8.3x10<sup>-5 </sup> (based on the most frequent pathogenic allele).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Only count males over age 30 with a documented eye examination with functional studies (normal ERG or FAF).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：For maternally inherited variants in _RPGR_, a variant present in a clinically verified (documented with a normal eye examination with functional studies including a normal ERG) unaffected male over age 30 could be used to establish this code. 

Inheritance is complicated in consanguineous families and in dual diagnoses situations so panel testing of unaffected members required to confirm presence of the variant.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：Use for ORF15 repetitive regions only (amino acids 585-1078). These events can be multiple and large (e.g. 9 plus 15 total 20-30 bp is known, a single 21bp event is common). Please note that ORF15 encompasses residues 585 through 1152, with UniProt identifying particularly disordered regions between 609-776, 790-906, and 989-1020.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：Stand Alone criteria applies to:

Missense variants: REVEL ≤ 0.003

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1

Strong criteria applies to:

Missense variants: REVEL between 0.004 and 0.016

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1
- **Moderate** ✅：Applies to:

Missense variants: REVEL between 0.017 and 0.183

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1
- **Supporting** ✅：Applies to:

Missense variants: REVEL between 0.184 and 0.290

Synonymous variants or noncoding variants: SpliceAI ≤ 0.1

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Applies to:

Synonymous variants or noncoding variants  with no impact on splicing (SpliceAI ≤ 0.2)

AND

PhyloP \< 0 for conservation

### 组合规则（Rules for Combining Criteria；官网 v1.0，Richards 2015 组合规则面板）

**Pathogenic（致病）**
1. 1 Very Strong AND ≥ 1 Strong
2. 1 Very Strong AND ≥ 2 Moderate
3. 1 Very Strong AND 1 Moderate AND 1 Supporting
4. 1 Very Strong AND ≥ 2 Supporting
5. ≥ 2 Strong
6. 1 Strong AND ≥ 3 Moderate
7. 1 Strong AND 2 Moderate AND ≥ 2 Supporting
8. 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**Likely Pathogenic（可能致病）**
1. 1 Very Strong AND 1 Moderate
2. 1 Strong AND 1 Moderate
3. 1 Strong AND ≥ 2 Supporting
4. ≥ 3 Moderate
5. 2 Moderate AND ≥ 2 Supporting
6. 1 Moderate AND ≥ 4 Supporting
7. 1 Strong AND 2 Moderate
8. 1 Very Strong AND ≥ 1 Supporting

**Benign（良性）**
1. ≥ 2 Strong
2. 1 Stand Alone

**Likely Benign（可能良性）**
1. 1 Strong AND 1 Supporting
2. ≥ 2 Supporting

### 不适用证据码
PM1、PM3、PM6、PP2、PP5、BS3、BP1、BP2、BP5、BP6
### 参考附件
- [RPGR PVS1 and PVS1 (RNA) Decision Tree](https://cspec.genome.network/cspec/File/id/08379701-e079-4e0c-bb34-32a633d501b6/data)
- [PVS1 Decision Tree for RPGR](https://cspec.genome.network/cspec/File/id/2539a96a-c1a1-4764-a1ab-35e4a387b92c/data)
- [Standard Operating Procedure - RPGR- V.7](https://cspec.genome.network/cspec/File/id/11e84a38-a26c-420c-b626-4335cba327b5/data)
- [Phenotype Features - RPGR Specifications](https://cspec.genome.network/cspec/File/id/3b7dc382-d858-41a7-999b-8d15fb4945a6/data)
- [c.730A-T Variant Report](https://cspec.genome.network/cspec/File/id/6c47c512-61aa-4e32-818e-9883d8ba3d97/data)
- [PS3 Functional Evidence - RPGR Specifications](https://cspec.genome.network/cspec/File/id/323abc59-d44f-4e44-bfd1-4d13f728e6a8/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN106)

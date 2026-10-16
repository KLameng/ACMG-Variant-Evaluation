# ClinGen VCEP基因特异性规范：RPE65

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：GN120 v1.0（Released，DOI: 10.5281/zenodo.21434471，2026-10-09 官网实页核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN120 — Leber Congenital Amaurosis/early onset Retinal Dystrophy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100368**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group [<sup>16</sup>](#pmid_30192042) and as updated by the ClinGen SVI Splicing Subgroup [<sup>17</sup>](#pmid_37352859)
*   Refer to RPE65-specific PVS1 Decision Tree, file attached.
    *   PVS1: Predicted splice defects at +/- 1,2 in exons 1-14
    *   PVS1: Single to multi-exon deletions, with or without predicted NMD. All exons are considered critical to protein function.
    *   PVS1: Nonsense or frameshift mutations from p.Ser2 through p.Gly528
    *   PVS1: Duplications of exons proven in tandem
    *   PVS1(RNA): RNA splicing data with evidence of alternative transcript production at complete levels, relative to normal allele.
- **Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group [<sup>16</sup>](#pmid_30192042) and as updated by the ClinGen SVI Splicing Subgroup [<sup>17</sup>](#pmid_37352859)
*   Refer to RPE65-specific PVS1 Decision Tree, file attached.
    *   PVS1\_Strong:Applied to variants in the initiation codon. The second in-frame methionine is located at residue 93, and there is no known study indicating that this methionine in _RPE65_ can be used as start codon. Variants affecting Met1 can lead to a complete absence of the protein product. Even though we cannot exclude the possibility of a 2nd Met being used as start codon, the translation efficiency maybe significantly reduced due to lack of other important elements (Kozak sequence, etc.). Also, there are multiple variants located upstream of Met93 having been reported as a pathogenic variant in HGMD and ClinVar, evidence that this region of the protein is functionally important.
    *   PVS1\_Strong: Nonsense or frameshift mutations from p.Leu529 through p.Ser533
    *   PVS1\_Strong: Duplications of exons presumed in tandem
    *   PVS1(RNA)\_Strong: RNA splicing data with evidence of alternative transcript production at near complete levels, relative to normal allele.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established Pathogenic variant regardless of nucleotide change.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

Same predicted splicing impact as a previously classified Pathogenic variant. 

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the **same position** that has been designated **Pathogenic**.
*   Used in conjunction with PVS1 for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide that has been designated Pathogenic.

Specific combinations are found in RPE65-specific PVS1 Decision Tree **part (b)** (Table 2 from Walker 2023).
- **Moderate** ✅：Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change。

*   Must have one comparison variant that reaches a Likely Pathogenic classification using this rule specification.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

Same predicted splicing impact as previously classified Likely Pathogenic variant.

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated Likely Pathogenic.
*   Used in conjunction with PVS1_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and have a comparable variant within the same splice donor/acceptor motif (but outside the +/-1,2 dinucleotide) that has been designated Pathogenic.

Specific combinations are found in RPE65-specific PVS1 Decision Tree **part (b)** (Table 2 from Walker 2023).
- **Supporting** ✅：

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant within the same motif that has been designated Likely Pathogenic.
*   Used in conjunction with PVS1 or PVS1_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and have a comparable Likely Pathogenic or Pathogenic variant either within the same splice site donor/acceptor motif, outside the +/-1,2 dinucleotide, or at the +/-1,2 dinucleotide.

Specific combinations are found in RPE65-specific PVS1 Decision Tree **part (b)** (Table 2 from Walker 2023).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file). Use option 3 “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” (maximum 0.5 points/proband)
*   Total of 4 or more points required for Very Strong level
- **Strong** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file). Use option 3 “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” (maximum 0.5 points/proband)
*   Total of 2.00 - 3.75 points required for Strong level
- **Moderate** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history。

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file). Use option 3 “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” (maximum 0.5 points/proband)
*   Total of 1.00 - 1.75 points required for Moderate level
- **Supporting** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history。

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See Table 1 within PS2/PM6 file). Use option 3 “Phenotype consistent with gene but not highly specific and high genetic heterogeneity” (maximum 0.5 points/proband)
*   Total of 0.50 - 0.75 points required for Supporting level

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. Not applicable for splicing effects (replaced by PVS1\_Strength (RNA))

See attached table for acceptable functional studies.

For studies reporting isomerhydrolase activity, cutoff is ≤10% of wild-type control.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain.

*   Met by variants encoding missense substitutions at His180, His182, His241, His313, Glu417, or His527, which are required residues located within the active site[<sup>16</sup>](#PMID_34492281).
*   Met by variants encoding missense substitutions between Ala107 and Gly125, which are known to mediate localization to the ER membrane[<sup>15</sup>](#PMID_36265895).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.

*   Used if the gnomAD PopMax Filtering Allele Frequency (FAF) is ≤ 2.0 x 10<sup>-4</sup>.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use SVI recommendations for in trans criterion（Table 1/Table 2，见附件 "PM3 Tables"）。

*   Points are calculated using Table 1. **≥ 4 points** from Table 1.
*   Both variants must be classified using these rule specifications.
- **Strong** ✅：Use SVI recommendations for in trans criterion（Table 1/Table 2，见附件 "PM3 Tables"）。

*   Points are calculated using Table 1. **2 to 3.75 points** from Table 1.
- **Moderate** ✅：Use SVI recommendations for in trans criterion（Table 1/Table 2，见附件 "PM3 Tables"）。

*   Points are calculated using Table 1. **1 to 1.75 points** from Table 1.
- **Supporting** ✅：Use SVI recommendations for in trans criterion（Table 1/Table 2，见附件 "PM3 Tables"）。

*   Points are calculated using Table 1. **0.5 to 0.75 points** from Table 1.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*    Protein length change of ≥2 amino acids that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP>2.0).
- **Supporting** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*    Protein length change of 1 amino acid that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acid adjacent to at least one conserved residue (PhyloP>2.0).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.
*   For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be likely pathogenic has been seen before.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another RPE65 variant are _in trans_.

*   Requires segregation in proband plus ≥3 similarly affected relatives
- **Moderate** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another RPE65 variant are _in trans_.

*   Requires segregation in proband plus 2 similarly affected relatives
- **Supporting** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another RPE65 variant are _in trans_.

*   Requires segregation in proband plus 1 similarly affected relative

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：For a missense variant use REVEL, requires a score of ≥ 0.774.
Splice variants use PP3 only at Supporting level.
- **Supporting** ✅：*   For a missense variant use REVEL, requires a score of 0.644 - 0.773.
*   For a predicted splicing variant use SpliceAI with max distance set to 500 bp. Highest delta score from SpliceAI must be ≥ 0.2 to use this code. See RPE65-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：8 phenotype points or more are required to use this code at the moderate strength for a single proband (see points list below).
Additionally, at least one specific criterion must be met (see below).
Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.
- **Supporting** ✅：*   4-7.5 phenotype points are required to use this code (see points list below).
*   Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Use gnomAD PopMax FAF if available, cutoff of  ≥8 x 10<sup>-3</sup>

*   Use large population databases (i.e. gnomAD).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disorder. Use gnomAD PopMax FAF if available.

*   Allele frequency of between 8x10<sup>-3</sup> and 8x10<sup>-4</sup>

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Variant is present in ≥ 3 homozygotes without any features of the phenotype. This rule only applies to individuals found in the literature who have been well-phenotyped  and are unaffected by age 40.

Presence in databases such as gnomAD are not considered.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. Not applicable for splicing effects (replaced by BP7_Strong (RNA)).

See attached table for list of acceptable functional studies.

For studies reporting isomerohydrolase activity, activity must be ≥50% of wild-type control.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.

*   One or both variants are absent in a similarly affected family member.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in cis with a Pathogenic variant.

*   Use code if the variant of interest is _in cis_ with a Pathogenic or Likely Pathogenic variant. The other variant must meet a Likely Pathogenic or Pathogenic classification using these rule specifications.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Moderate** ✅：For a missense variant use REVEL, requires a score of ≤0.183. In addition, highest SpliceAI delta score should also be below cutoff of 0.1.
- **Supporting** ✅：For a missense variant use REVEL, requires a score between 0.183 - 0.290. In addition, highest SpliceAI delta score should also be below cutoff of 0.1.

For a silent / intronic variant outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon, BP4 can be met if the highest of the four delta scores within SpliceAI is below the cutoff of ≤0.1. See RPE65-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Please note that BP7 can be met as well.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：BP7_Strong (RNA) Used to designate capture of splicing data (not BS3). See RPE65-specific PVS1 Decision Tree, file attached, for weighting and combining with other codes.
- **Supporting** ✅：Use for variants located outside of the donor/acceptor +/- 1,2 dinucleotide positions. 

If SpliceAI score ≤0.1, apply BP4 followed by assessment of BP7. See RPE65-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Positions **excluded** from BP7:
    *   Synonymous substitutions at the first base of an exon
    *   Synonymous substitutions in the last 3 bases of an exon
    *   +1 through +7 of donor sequence
    *   \-1 through -21 of acceptor sequence

### Rules for Combining Criteria（组合规则，v1.0 浏览器实页核实 2023-10-24）

**Pathogenic**
- 1 Very Strong（PVS1, PS2_Very Strong, PM3_Very Strong）AND ≥ 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）
- 1 Very Strong（PVS1, PS2_Very Strong, PM3_Very Strong）AND ≥ 2 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）
- 1 Very Strong（PVS1, PS2_Very Strong, PM3_Very Strong）AND 1 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）AND 1 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- 1 Very Strong（PVS1, PS2_Very Strong, PM3_Very Strong）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- ≥ 2 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND ≥ 3 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND 2 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND 1 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）AND ≥ 4 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）

**Likely Pathogenic**
- 1 Very Strong（PVS1, PS2_Very Strong, PM3_Very Strong）AND 1 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND 1 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- ≥ 3 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）
- 2 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）AND ≥ 2 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- 1 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）AND ≥ 4 Supporting（PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4）
- 1 Strong（PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong）AND 2 Moderate（PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate）

**Benign**
- ≥ 2 Strong（BS1, BS2, BS4, BP7_Strong）

**Likely Benign**
- 1 Strong（BS1, BS2, BS4, BP7_Strong）AND 1 Supporting（BS3_Supporting, BP2, BP4, BP7）
- ≥ 2 Supporting（BS3_Supporting, BP2, BP4, BP7）

### 不适用证据码
PS4、PM6、PP2、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [RPE65 Rule combination rules](https://cspec.genome.network/cspec/File/id/443c8f82-f88c-48d1-8ca9-63e1c9ec5613/data)
- [RPE65 Pilot Variants, Sept.11, 2023](https://cspec.genome.network/cspec/File/id/0fd093f2-c1ab-4192-ad6c-1038d68a6dc4/data)
- [PS2 PM6 Tables](https://cspec.genome.network/cspec/File/id/478f9917-41a1-489f-acaa-1a1b0bdf7e5e/data)
- [RPE65-specific PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/ddf3a5d9-be2f-4892-b1a9-8846ff83ebc1/data)
- [PP3 performance of multiple prediction models](https://cspec.genome.network/cspec/File/id/ac12237c-4e17-4ccc-bf35-87d34361a520/data)
- [PS3 Approved functional assays](https://cspec.genome.network/cspec/File/id/8b01f578-6989-4782-bd7a-21eecdbb9971/data)
- [PM3 Tables](https://cspec.genome.network/cspec/File/id/eb7fd87c-b11d-454f-97fa-eb906c5efe5a/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN120)

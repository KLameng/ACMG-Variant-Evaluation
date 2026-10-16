# ClinGen VCEP基因特异性规范：GUCY2D

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v1.0（DOI: 10.5281/zenodo.21434777；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN167 — Leber Congenital Amaurosis/early onset Retinal Dystrophy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100453**（遗传方式：Autosomal recessive inheritance）

### 通用说明
The GUCY2D gene gene encodes a retina-specific guanylate cyclase, which is a member of the membrane guanylyl cyclase family. Aliases for the protein (NP_000171.1) are numerous and include RetGC-1, RETGC-1; ROS-GC, ROS-GC1, RetGC, and CG-E.    
 
Note:  The point system of Tavtigian et al. (PMID 32720330) is being used for all classifications so the combining rules are not being utilized.          
            

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

*   Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018[<sup>16</sup>](#pmid_30192042)) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023[<sup>17</sup>](#pmid_37352859)).
*   Refer to GUCY2D-specific PVS1 Decision Tree, file attached.
    *   PVS1: Predicted splice defects at +/- 1,2 in exons 2-20
    *   PVS1: Single to multi-exon deletions, with or without predicted NMD. All exons are considered critical to protein function.
    *   PVS1: Applied to variants in the initiation codon. The second in-frame methionine is located at residue 218 and use of this as a start codon would eliminate the leader sequence which targets the protein to the endoplasmic reticulum. There is no known study indicating that this methionine in GUCY2D can be used as start codon. Variants affecting Met1 can lead to a complete absence of the protein product. Additionally, there are multiple variants located upstream of p.Met218 that have been reported as a pathogenic in HGMD and ClinVar, evidence that this entire region of the protein is functionally important.
    *   PVS1: Nonsense or frameshift mutations from p.Thr2 through p.Lys1068
    *   PVS1: Duplications of exons proven in tandem
    *   PVS1(RNA): RNA splicing data with evidence of alternative transcript production at complete levels, relative to normal allele.
- **Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018[<sup>16</sup>](#pmid_30192042)) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023[<sup>17</sup>](#pmid_37352859)).
*   Refer to GUCY2D-specific PVS1 Decision Tree, file attached.
    *   PVS1\_Strong: Nonsense or frameshift mutations from p.Pro1069 through p.Ser1103
    *   PVS1\_Strong: Duplications of exons presumed in tandem
    *   PVS1(RNA)\_Strong: RNA splicing data with evidence of alternative transcript production at near complete levels, relative to normal allele.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established Pathogenic variant regardless of nucleotide change.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.

Same predicted splicing impact as a previously classified Pathogenic variant. 

*   Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the **same position** that has been designated **Pathogenic**.
*   Used in conjunction with PVS1 for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide that has been designated Pathogenic.

Specific combinations are found in GUCY2D-specific PVS1 Decision Tree **part (b)** (Table 2 from Walker 2023).

- **Moderate** ✅：Same amino acid change as a previously established Likely Pathogenic variant regardless of nucleotide change.

Must have one comparison variant that reaches a Likely Pathogenic classification using this rule specification.

Same predicted splicing impact as previously classified Likely Pathogenic variant.

Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant at the same position that has been designated Likely Pathogenic.
Used in conjunction with PVS1_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and have a comparable variant within the same splice donor/acceptor motif (but outside the +/-1,2 dinucleotide) that has been designated Pathogenic.

Specific combinations are found in GUCY2D-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).
- **Supporting** ✅：Used in conjunction with PP3 for variants located outside the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant within the same motif that has been designated Likely Pathogenic.
Used in conjunction with PVS1 or PVS1_(reduced strength) for variants located at the splice donor/acceptor +/-1,2 dinucleotide positions and have a comparable Likely Pathogenic or Pathogenic variant either within the same splice site donor/acceptor motif, outside the +/-1,2 dinucleotide, or at the +/-1,2 dinucleotide.

 Specific combinations are found in GUCY2D-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).


#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file). 
*   Total of 4 or more points required for Very Strong level
- **Strong** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

*   Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file). 
*   Total of 2.00 - 3.75 points required for Strong level

- **Moderate** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See PS2-Table 1 within PS2/PM6 file).
Total of 1.00 - 1.75 points required for Moderate level
- **Supporting** ✅：De novo (**both** maternity and paternity confirmed) in a patient with the disease and no family history.

Use ClinGen SVI's recommendation for assigning weight to the PS2/PM6 codes (See Table 1 within PS2/PM6 file).
Total of 0.50 - 0.75 points required for Supporting level


#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. 

See attached table for acceptable functional studies. 

Eligible results include _Gucy2e−/−Gucy2f−/−_ knockout mice subretinally injected with adeno-associated virus-packaged constructs encoding a GUCY2D variant (Boye et al., 2016,[<sup>10</sup>](#pmid_27881908)) or mice with knock-in of a _GUCY2D_ variant (not yet available in the published literature). Results should include flat or nearly flat scotopic and photopic electroretinogram responses in comparison to wild-type injected control, absent or near-absent guanylate cyclase activity in comparison to wild-type injected control, and/or absent or near absent GUCY2D expression at the protein level despite approximately wild-type expression at the RNA level.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. Not applicable for splicing effects (replaced by PVS1\_Strength (RNA))

See attached table for acceptable functional studies.

For studies reporting guanylate cyclase activity, cutoff is ≤10% of wild-type control.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Met by active site residues that bind the GTP substrate or the Mg<sup>2+</sup> ion; Phe883, Asp885, Thr890, Leu905, Glu925, Ile927, Asp929, Met932, Arg976, Arg995, Cys997, Leu998, Phe999, Gly1000, Val1003, Asn1004, Arg1008, and Glu1010

- **Supporting** ✅：Met by variants not explicitly listed above, encoding missense substitutions between positions p.873-951. This region forms part of the guanylate cyclase catalytic domain and exhibits intolerance to missense variation.
Met by variants in the 6 bp CRX binding site located at position 17:8002593-8002598 (hg38)
 [<sup>13</sup>](#pmid_9391039).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.

*   Used if the gnomAD total allele frequency is ≤ 4.0 x 10<sup>-4</sup>.


#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Points are calculated using Table 1 from https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf (or attached file “PM3 Tables”)

≥4 points from Table 1
- **Strong** ✅：Points are calculated using Table 1 from https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf (or attached file “PM3 Tables”)

 2 to 3.75 points from Table 1
- **Moderate** ✅：Points are calculated using Table 1 from https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf (or attached file “PM3 Tables”)

 1 to 1.75 points from Table 1
- **Supporting** ✅：Points are calculated using Table 1 from https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf (or attached file “PM3 Tables”)

 0.5 to 0.75 points from Table 1

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
*   SpliceAI scores for both variants should be in the same category (\<0.1, between 0.1 and 0.2, >0.2)

- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Must have one comparison variant that reaches a Likely Pathogenic classification using this rule specification.
SpliceAI scores for both variants should be in the same category (<0.1, between 0.1 and 0.2, >0.2)


#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another GUCY2D variant are _in trans_.

*   Requires segregation in one proband plus ≥3 similarly affected relatives
- **Moderate** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another GUCY2D variant are _in trans_.

*   Requires segregation in one proband plus 2 similarly affected relatives
- **Supporting** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another GUCY2D variant are _in trans_.

*   Requires segregation in one proband plus 1 similarly affected relative

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：For a missense variant use REVEL, requires a score of ≥ 0.774.
Splice variants use PP3 only at Supporting level.
- **Supporting** ✅：*   For a missense variant use REVEL, requires a score of 0.644 - 0.773.
*   For a variant in an untranslated region use CADD, requires a score of ≥ 20.0
*   For a predicted splicing variant use SpliceAI with max distance set to 500 bp. Highest delta score from SpliceAI must be ≥ 0.2 to use this code. See GUCY2D-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

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
- **Stand Alone** ✅：Use gnomAD Grpmax FAF if available, cutoff of  >0.016

*   Use large population databases (i.e. gnomAD).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disorder. Use gnomAD Grpmax FAF if available.

*   Allele frequency of 0.0016 - 0.016

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Variant is present in ≥ 3 homozygotes without any features of the phenotype. This rule applies to individuals found in the literature who have been well-phenotyped and are unaffected by age 40. Alternatively, this strength can be applied if the variant is present in ≥ 6 homozygotes in gnomAD v.4.1.0 or later.
- **Supporting** ✅：Variant is present in ≥ 3 homozygotes in gnomAD v.4.1.0 or later.


#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：Not applicable for splicing effects (replaced by BP7_Strong (RNA)).

For studies reporting guanylate cyclase activity, cutoff is >50% of wild-type control. Studies included; Peshenko et al., 2020, Feng et al., 2020, Jacobson et al., 2021, Jacobson et al., 2020, Tucker et al., 2004, Jacobson et al., 2013, and Peshenko et al., 2015

See attached table of Approved PS3 Functional Assays for a list of acceptable functional studies including those that:

Report failure of GUCY2D to localize to the cell surface : Zulliger et al., 2015.
Report failure of GUCY2D to bind RD3: Zulliger et al., 2015.
Report failure of GCAP1, GCAP2, or RD3 to co-localize with GUCY2D at the cell surface: Peshenko et al., 2020, Jacobson et al., 2020, and Peshenko et al., 2015.

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

For a silent / intronic variant outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon, BP4 can be met if the highest of the four delta scores within SpliceAI is below the cutoff of ≤0.1. See GUCY2D-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Please note that BP7 can be met as well.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：BP7_Strong (RNA) Used to designate capture of splicing data (not BS3). See GUCY2D-specific PVS1 Decision Tree, file attached, for weighting and combining with other codes.
- **Supporting** ✅：Use not only for synonymous variants but also for intronic variants located outside of the donor/acceptor +/- 1,2 dinucleotide positions. 

If SpliceAI score ≤0.1, apply BP4 followed by assessment of BP7. See GUCY2D-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Positions **excluded** from BP7:
    *   Synonymous substitutions at the first base of an exon
    *   Synonymous substitutions in the last 3 bases of an exon
    *   +1 through +7 of donor sequence
    *   \-1 through -21 of acceptor sequence

### 点系统分类（Tavtigian 贝叶斯框架，v1.0 浏览器实页核实 2026-10-08）

本规范（Version 1.0，Released 1/22/2025）对所有分类采用 Tavtigian et al., 2020（PMID: 32720330）贝叶斯适配的点系统，不另行使用传统组合规则。各证据码强度对应的默认分值与积分切分定义于附件《GUCY2D Rule Combination Rules》（PDF Table 2 / Table 3）：

**各证据码强度默认分值（Table 2，按强度通用取值）**

| 强度 | 致病方向（正分） | 良性方向（负分） |
|---|---|---|
| Very Strong | +8 | -8 |
| Strong | +4 | -4 |
| Moderate | +2 | -2 |
| Supporting | +1 | -1 |
| Indeterminate | 0 | 0 |
| Stand Alone（不记分，独立判良性） | — | BA1 |

**Point Based Variant Classification Categories（积分分类切分，Table 3）**

| 分类 | 积分区间 |
|---|---|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -1 – -6 |
| Benign | ≤ -7 |

> 说明：该规范 live 文档页本身不内联数值积分表，各码分值与切分以官方附件《GUCY2D Rule Combination Rules》PDF（见参考附件）为准；附件另建议将点系统结果与 VCI 结果比对，冲突时以点系统为准。


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
PS4、PM6、PP2、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [GUCY2D Rule Combination Rules](https://cspec.genome.network/cspec/File/id/f23cf7f2-33c8-46d8-8e69-8fd4b1cba0d4/data)
- [PM3 Tables](https://cspec.genome.network/cspec/File/id/4aa8c4d2-c38c-4181-a211-b5937395d3f0/data)
- [GUCY2D-specific PVS1 decision tree](https://cspec.genome.network/cspec/File/id/5fa8c0e6-571f-49f6-8c2a-d3c0f71408b8/data)
- [PS3 Approved functional assays](https://cspec.genome.network/cspec/File/id/6c17ac3f-1fb3-4c4b-9dde-c355693d7cd5/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN167)

# ClinGen VCEP基因特异性规范：AIPL1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN208 — Leber Congenital Amaurosis/early onset Retinal Dystrophy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100438**（遗传方式：Autosomal recessive inheritance）

### 官网版本
- Version 1.0（Released）
- DOI: 10.5281/zenodo.21434858（https://doi.org/10.5281/zenodo.21434858）
- 核验日期：2026-10-09

### 通用说明
The point system of Tavtigian et al. (PMID:32720330) is being used for all classifications so the combining rules are not being utilized.  Refer to file: "AIPL1 Rule Combination Rules".
          

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

*   Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018[<sup>1</sup>](#pmid_30192042)) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023[<sup>2</sup>](#pmid_37352859)).
*   Refer to AIPL1-specific PVS1 Decision Tree, file attached.
    *   PVS1: Predicted splice defects at +/- 1,2 in exons 1-6
    *   PVS1: Single to multi-exon deletions, with or without predicted NMD. All exons are considered critical to protein function[<sup>6</sup>](#pmid_33067476).
    *   PVS1: Applied to variants in the initiation codon. The second in-frame methionine is located at residue 40 in exon 2. There is no known study indicating that this methionine in AIPL1can be used as start codon. There are multiple variants located upstream of p.Met40 that have been reported as a pathogenic in HGMD and ClinVar, evidence that this entire region of the protein is functionally important.
    *   PVS1: Nonsense variants from p.Thr2 through p.Ser328
    *   PVS1: Frameshift variants from p.Thr2 though p.Glu337 (The presence of extensive long ORFs may lead to significant additional protein length after frameshift[<sup>7</sup>](#pmid_10615133).)
    *   PVS1: Duplications of exons proven in tandem
    *   PVS1(RNA): RNA splicing data with evidence of alternative transcript production at complete levels, relative to normal allele [<sup>5</sup>](#pmid_26650897).
- **Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018[<sup>1</sup>](#pmid_30192042)) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023[<sup>2</sup>](#pmid_37352859)).
*   Refer to AIPL1-specific PVS1 Decision Tree, file attached.
    *   PVS1\_Strong: Nonsense variants from p.Glu329 through p.Ser346
    *   PVS1\_Strong: Frameshift variants from p.Pro338 through p.His384
    *   PVS1\_Strong: Duplications of exons presumed in tandem
    *   PVS1(RNA)\_Strong: RNA splicing data with evidence of alternative transcript production at near complete levels, relative to normal allele [<sup>5</sup>](#pmid_26650897).
- **Moderate** ✅：Null variant in a gene where loss of function is a known mechanism of disease.

*   Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018[<sup>1</sup>](#pmid_30192042)) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023[<sup>2</sup>](#pmid_37352859)).
*   Refer to AIPL1-specific PVS1 Decision Tree, file attached.
    *   PVS1\_Moderate: Nonsense variants from p.Ser347 through p.His384

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established Pathogenic variant regardless of nucleotide change.

*   Must have one comparison variant that reaches a Pathogenic classification using this rule specification.

Same predicted splicing impact as a previously classified variant. 

*   Refer to the  AIPL1-specific PVS1 Decision Tree **part (b)** (Table 2 from Walker 2023) for specific combinations.

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

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. Not applicable for splicing effects (replaced by PVS1\_Strength (RNA))

See attached table for acceptable functional studies.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.

*   Used if the gnomAD total allele frequency is ≤ 4.0 x 10<sup>-4</sup>.

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

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus ≥3 similarly affected relatives
- **Moderate** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus 2 similarly affected relatives
- **Supporting** ✅：Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are _in trans_.

*   Requires segregation in one proband plus 1 similarly affected relative

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：*   For a missense variant use REVEL, requires a score of ≥0.093.
*   Splice variants use PP3 only at Supporting level.
- **Moderate** ✅：*   For a missense variant use REVEL, requires a score of 0.774 - 0.092.
*   Splice variants use PP3 only at Supporting level.
- **Supporting** ✅：*   For a missense variant use REVEL, requires a score of 0.644 - 0.773.
*   For a variant in an untranslated region use CADD, requires a score of ≥ 20.0
*   For a predicted splicing variant use SpliceAI with max distance set to 500 bp. Highest delta score from SpliceAI must be ≥ 0.2 to use this code. See AIPL1-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

> 注：官网 PP3 Strong（REVEL≥0.093）与 Moderate（0.774-0.092）阈值文本疑为官网发布笔误（上下界颠倒），此处照录官网原文、未作改值；详见修订对照日志争议说明。

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   8 phenotype points or more are required to use this code at the moderate strength for a single proband (see points list below).
*   Additionally, at least one specific criterion must be met (see below).
- **Supporting** ✅：*   4-7.5 phenotype points are required to use this code (see points list below).
*   Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Use gnomAD Grpmax FAF if available, cutoff of  ≥0.0057

*   Use large population databases (i.e. gnomAD).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disorder. Use gnomAD Grpmax FAF if available.

*   Allele frequency of 0.00057 - 0.00569

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Variant is present in ≥ 3 homozygotes without any features of the phenotype. This rule applies to individuals found in the literature who have been well-phenotyped and are unaffected by age 40. Alternatively, this strength can be applied if the variant is present in ≥ 6 homozygotes in gnomAD v.4.1.0 or later.
- **Supporting** ✅：Variant is present in ≥ 3 homozygotes in gnomAD v.4.1.0 or later.

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
- **Moderate** ✅：*   For a missense variant use REVEL, requires a score of ≤0.183. In addition, highest SpliceAI delta score should also be below cutoff of 0.1.
- **Supporting** ✅：For a missense variant use REVEL, requires a score between 0.183 - 0.290. In addition, highest SpliceAI delta score should also be below cutoff of 0.1.

For a silent / intronic variant outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon, BP4 can be met if the highest of the four delta scores within SpliceAI is below the cutoff of ≤0.1. See AIPL1-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Please note that BP7 can be met as well.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：*   BP7\_Strong (RNA) Used to designate capture of splicing data (not BS3). See AIPL1-specific PVS1 Decision Tree, file attached, for weighting and combining with other codes.
- **Supporting** ✅：Use not only for synonymous variants but also for intronic variants located outside of the donor/acceptor +/- 1,2 dinucleotide positions. 

If SpliceAI score ≤0.1, apply BP4 followed by assessment of BP7. See AIPL1-specific PVS1 Decision Tree **part (a)** for SpliceAI flowchart.

*   Positions **excluded** from BP7:
    *   Synonymous substitutions at the first base of an exon
    *   Synonymous substitutions in the last 3 bases of an exon
    *   +1 through +7 of donor sequence
    *   \-1 through -21 of acceptor sequence

### 点系统分类（Tavtigian 贝叶斯框架，v1.0 浏览器实页核实 2026-10-08）

本规范（Version 1.0，Released 9/26/2025；Type: Tavtigian et.al., 2020 - Bayesian adaptation of Richards et.al., 2015）采用贝叶斯适配的点系统。各证据码强度对应的 Default Point Value 如下：

**致病方向（正分）**

| 积分 | 证据码强度 |
|---|---|
| +8 | PVS1（Very Strong）、PS2（Very Strong）、PM3（Very Strong） |
| +4 | PVS1_Strong、PS1、PS2_Strong、PP1_Strong、PP3_Strong |
| +2 | PVS1_Moderate、PS1_Moderate、PS2_Moderate、PM4、PM5、PP1_Moderate、PP3_Moderate、PP4_Moderate |
| +1 | PS1_Supporting、PS2_Supporting、PS3、PM2_Supporting、PM3_Supporting、PM4_Supporting、PM5_Supporting、PP1_Supporting、PP3_Supporting、PP4_Supporting |

**良性方向（负分）**

| 积分 | 证据码强度 |
|---|---|
| Stand Alone（不记分，独立判良性） | BA1 |
| -4 | BS1、BS2_Strong、BS4、BP7_Strong |
| -2 | BP4_Moderate |
| -1 | BS2_Supporting、BP2、BP4_Supporting |

**Point Based Variant Classification Categories（积分分类切分）**

| 分类 | 积分区间 |
|---|---|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤ -7 |

> 积分合成规则见参考附件《AIPL1 Rule combination rules》；PM3 各 in trans 出现次数计分见《PM3 Tables》。

### 不适用证据码
PS4、PM1、PM6、PP2、PP5、BS3、BP1、BP3、BP5、BP6
### 参考附件
- [AIPL1-specific PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/6b6de9d9-ba3b-47fd-b994-dd9e68d41dd7/data)
- [AIPL1 Rule combination rules](https://cspec.genome.network/cspec/File/id/4f00b9e5-71ba-4f67-ac8c-9b0ab5c037da/data)
- [PS3 Approved Functional assays](https://cspec.genome.network/cspec/File/id/5158a7f7-c128-40bd-b717-d924e17b8e26/data)
- [PS2/PM6 Tables](https://cspec.genome.network/cspec/File/id/32ee7fd1-f924-4ab6-9446-562fdbe56c0e/data)
- [PM3 Tables](https://cspec.genome.network/cspec/File/id/af56bf64-e281-43e1-93db-dab7a9fcb786/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN208)

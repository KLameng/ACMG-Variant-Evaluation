# ClinGen VCEP基因特异性规范：ABCD1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；附件文件名含版本日期线索：GN105_ABCD1_functional_assays_090225.xlsx；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN105 — Peroxisomal Disorders Variant Curation Expert Panel 

### 覆盖疾病
- **MONDO:0018544**（遗传方式：X-linked inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：The Perox VCEP will utilize SVI’s PVS1 recommendation for determining applicable PVS1 strength level (Abou Tayoun et al 2018; PMID: 30192042). Refer to the modified PVS1 decision tree attached.

PVS1 RNA is applicable for splicing defects demonstrated by RNA studies on patient mRNA or when a variant expressed in human/mammalian host cells. Strength level may be decided based on the assay as well as the abundance of normal splice products as recommended by Walker et al, 2023.

Exons 1 and 9 are in-frame. Exon skipping consequences for splice site variants are listed in the attached table.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
*   PS1 will be applied at the strong level for 1 previously established pathogenic variant 
*   PS1 can also be applied at the strong level for 1 previously established pathogenic canonical splice site variant (at the same position)
*   The other variant(s) used for evidence should also have been curated using Perox VCEP rule specifications and reach a pathogenic/likely pathogenic classification without using PS1.
- **Moderate** ✅：*   Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
*   PS1 will be applied at the moderate level for 1 previously established likely pathogenic variant 
*   PS1 can also be applied at the moderate level for 1 previously established likely pathogenic canonical splice site variant (at the same position)
*   The other variant(s) used for evidence should also have been curated using Perox VCEP rule specifications and reach a pathogenic/likely pathogenic classification without using PS1.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

*   Confirmed maternity and paternity by WES Trio or paternity and maternity testing for affected females. Confirmation of maternity is sufficient in the case of affected males. 
*   Use SVI-recommended point system at 2<sup>nd</sup> tier, “phenotype consistent with gene but not highly specific”, for probands meeting PP4 and at the 1<sup>st</sup> tier, “phenotype highly specific for gene”, for probands meeting PP4\_Moderate
*   See attached table.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：*   Applicable for beta-oxidation activity assays OR immunofluorescence assays showing absence or mislocalization of protein OR immunoblotting assay showing absence or reduced protein levels.
*   Note: for variants meeting PS1, functional studies on a different variant (different nucleotide change, same amino acid change) may be applicable to the variant being curated. PS3\_supporting may be used in addition to PS1.
*   There are not many benign variants to curate for functional evidence at this time. We would favor using PS3\_moderate in the event that more variants with functional evidence are classified as benign by the Peroxisomal Disorders VCEP.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：*   Applicable when multiple unrelated probands are reported with the same variant. All probands counted should meet at least PP4\_supporting phenotype criteria. When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) towards PS4.
*   PS4\_Very Strong applicable for ≥ 16 probands
*   Note: We caution against applying PS4 for >4 cases (meeting phenotype criteria D/E and F) with the same variant identified solely on newborn screening.
- **Strong** ✅：*   Applicable when multiple unrelated probands are reported with the same variant. All probands counted should meet at least PP4\_supporting phenotype criteria. When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) towards PS4.
*   PS4 applicable for 4 -15 probands
*   Note: We caution against applying PS4 for >4 cases (meeting phenotype criteria D/E and F) with the same variant identified solely on newborn screening.
- **Moderate** ✅：*   Applicable when multiple unrelated probands are reported with the same variant. All probands counted should meet at least PP4\_supporting phenotype criteria. When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) towards PS4.
*   PS4\_Moderate for 2-3 probands
*   Note: We caution against applying PS4 for >4 cases (meeting phenotype criteria D/E and F) with the same variant identified solely on newborn screening.
- **Supporting** ✅：*   Applicable when multiple unrelated probands are reported with the same variant. All probands counted should meet at least PP4\_supporting phenotype criteria. When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) towards PS4.
*   PS4\_Supporting for 1 proband
*   Note: We caution against applying PS4 for >4 cases (meeting phenotype criteria D/E and F) with the same variant identified solely on newborn screening.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

*        PM1 applied at moderate strength for variants within the Walker A (aa 507-520; c.1519-c.1560) and B (aa 617-641; c.1849-c.1923) domains

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   PM2\_Supporting can be applied if the variant is absent in hemizygotes AND has a maximum allele frequency of \<0.00017% (0.0000017) in heterozygotes in the latest version of gnomAD. Use the highest population MAF from a non-bottleneck population from the latest version of gnomAD.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

*   Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
*   PM5 will be applied at moderate strength for 1 pathogenic variant with no benign variation at the residue
*   The other variant(s) used for evidence should also have been curated using the Perox VCEP rule specifications and must reach a pathogenic/likely pathogenic classification without PM5
- **Supporting** ✅：*   PM5\_Supporting can be applied for 1 likely pathogenic variant with no benign variation at the residue.
*   The other variant(s) used for evidence should also have been curated using the Perox VCEP rule specifications and must reach a pathogenic/likely pathogenic classification without PM5

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.

*   See PS2 specification; Use SVI-recommended point system at 2<sup>nd</sup> tier for probands meeting PP4 and at the 1<sup>st</sup> tier for probands meeting PP4\_Moderate

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：*   Segregations can be counted across families. All individuals counted for segregation must be genotype positive AND phenotype positive. In the absence of a pedigree available to determine relationships, segregations among related individuals can be counted conservatively (assuming closest relationships).
*   PP1\_Strong: 3 affected segregations (in addition to proband)
- **Moderate** ✅：*   Segregations can be counted across families. All individuals counted for segregation must be genotype positive AND phenotype positive. In the absence of a pedigree available to determine relationships, segregations among related individuals can be counted conservatively (assuming closest relationships).
*   PP1\_Moderate: 2 affected segregation (in addition to proband)
- **Supporting** ✅：*   Segregations can be counted across families. All individuals counted for segregation must be genotype positive AND phenotype positive. In the absence of a pedigree available to determine relationships, segregations among related individuals can be counted conservatively (assuming closest relationships).
*   PP1\_supporting: 1 affected segregation (in addition to proband)

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants, use REVEL with a score of >0.85 
*   For variants with a splicing impact (loss of canonical splice sites AND creation of cryptic sites), use SpliceAI with a score of ≥ 0.5

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   Use PP4 table to determine the appropriate PP4 strength level 
*   When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) toward PS4.
- **Supporting** ✅：*   Use PP4 table to determine the appropriate PP4 strength level 
*   When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4\_supporting strength) toward PS4.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Use a Total Grpmax filtering allele frequency (FAF) cutoff of ≥0.017% (0.00017) from the most resent version of gnomAD. This frequency was calculated using the Whiffen-Ware calculator with a prevalence estimated at 1 in 5000 (actual prevalence in hemizygotes and heterozygotes is reported to be 1 in 16800, GeneReviews, Bezman et al 2001; however, a more conservative BA1 was designated based on a value 1 order of magnitude higher than the BS1 cut-off), penetrance at 60% (based on penetrance in heterozygotes by expert judgment, maximum allelic contribution and maximum genetic contribution at 100%).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Use a Total Grpmax filtering allele frequency (FAF) cutoff of ≥0.0017% (0.000017) from the most recent version of gnomAD. This frequency was calculated using the Whiffen-Ware calculator with a prevalence estimated at 1 in 50000 (upper limit of prevalence range in hemizygotes; GeneReviews), penetrance at 60% (based on penetrance in heterozygotes by expert judgment, maximum allelic contribution and maximum genetic contribution at 100%).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

*   This code is applicable when >10 hemizygous healthy adult (>40y) males are observed

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：*   BS3\_Supporting is applicable for beta-oxidation activity assay in ALD fibroblasts transfected with variant, showing >57% activity of WT (PMID: 34946879)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

*   Use as is when there is a lack of segregation in 1 affected male in the family in addition to the proband

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

*   Use when variant is found to be is cis with another pathogenic variant
*   The “in-cis” variant should also be curated by the Perox VCEP to apply rule.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants, use REVEL with a score of ≤ 0.5 AND SpliceAI with a score \< 0.1
*   For variants with splicing impact (exonic and intronic variants, not applicable for UTR variants), use SpliceAI with a score \< 0.1

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Can be applied to synonymous variants meeting BP4 criteria OR intronic variants meeting BP4 criteria and are beyond the Walker et. al. (PMID 37352859) defined splice region of +7/-21

*   Conservation does not have to be considered for this code to apply

### 不适用证据码
PM3、PP2、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [ABCD1 PP4 phenotype table](https://cspec.genome.network/cspec/File/id/c6d85516-7f34-484e-97bf-f4d9f080e8cc/data)
- [PS2 table](https://cspec.genome.network/cspec/File/id/3a808e96-8427-45c0-ad8a-3be6488eac14/data)
- [PVS1 tables](https://cspec.genome.network/cspec/File/id/202266ea-85ed-4544-b3f6-7714c6920ad2/data)
- [ABCD1_PVS1_decisiontree_090225](https://cspec.genome.network/cspec/File/id/14449d4f-38fc-43a5-b230-7e90869bcbac/data)
- [ABCD1 rules for combining criteria July 2023](https://cspec.genome.network/cspec/File/id/7f9a4710-a6aa-4b46-a79a-d3ad55f5d231/data)
- [ABCD1 functional assays_090225](https://cspec.genome.network/cspec/File/id/a3e9f972-a80d-4c7f-989f-037fcc55e55c/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN105)

# ClinGen VCEP基因特异性规范：TP53

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN009 — TP53 Variant Curation Expert Panel

> 官网版本：Version 2.4；DOI: 10.5281/zenodo.21421509；核验日期：2026-10-09；积分制（Tavtigian Bayesian，PV=8/4/2/1/-1/-2/-4）

### 覆盖疾病
- **MONDO:0018875**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Please utilize the PVS1 decision tree for application of PVS1 code. The decision tree details the specific strengths each type of null variant may be applied at. Please see below for some additional helpful summary details for application of PVS1 code:

*   Initiation codon:
    *   PVS1 may be applied to initiation codon variants
*   Nonsense or frameshift variants:
    *   PVS1 applies to variants predicted to result in nonsense-mediated decay (NMD) for nonsense variants upstream of p.Lys351 and for frameshift induced premature termination codon (PTC) upstream of p.Lys351
    *   PVS1\_Strong applies to variants not predicted to undergo NMD (nonsense variants downstream of codon 350 or frameshift induced PTC in exon 11 or in the 3’ most 50 nucleotides of exon 10) in variants located in the p.Lys351 to p.Ala 355 range
    *   PVS1\_Moderate applies to variants not predicted to undergo NMD (nonsense variants downstream of codon 350 or frameshift induced PTC in exon 11 or in the 3’ most 50 nucleotides of exon 10) in variants located in the p.Gly356 to p.Asp393 range
    *   PVS1\_Moderate may also be applied to frameshift induced PTC downstream of the natural stop codon
*   Canonical splice variants (+/- 1,2 intronic positions): 
    *   PVS1 applies to predicted splicing alterations that are PTC resulting in NMD (or in-frame but targeting critical domains or residues)
    *   PVS1 applies to predicted splicing alterations that target the start codon (Exon 2 donor)
    *   PVS1\_Moderate applied to splicing alterations that are predicted to shorten (\<10% of the protein removed) or expand a _TP53_ C-terminal end of unknown function (E10 donor or E11 acceptor)
*   Deletions
    *   Full gene deletions: PVS1
    *   Single- to multi-exon deletions that target the initiation codon, preserving the potential rescue ATG (p.Met40) in exon 4: PVS1
    *   Single- to multi-exon deletions that target the initiation codon and the potential rescue ATG (p.Met40) in exon 4: PVS1
    *   Single- to multi-exon deletion that disrupts the reading frame and is predicted to undergo NMD (nonsense or frameshift induced PTC upstream of p.Lys351): PVS1
    *   Single- to multi-exon deletion that disrupts the reading frame and is **NOT** predicted to undergo NMD (nonsense or frameshift inducted PTC downstream of p.Leu350): PVS1
    *   Single- to multi-exon deletion including the last exon where the truncated/altered region is critical to protein function (any multi-exon combination targeting exon 11): PVS1
        *   If the role of the region in protein function is unknown, if the variant removed \< 10% of the protein (deletion of exon 11): PVS1\_Moderate
    *   Single- to multi-exon deletion that preserves the reading frame where the truncated/altered region is critical to protein function: PVS1
*   Duplications (≥1 exon in size and must be completely contained within the _TP53_ gene)
    *   Proven in tandem. Reading frame is disrupted and NMD predicted to occur (nonsense upstream of p.Lys351 or frameshift-induced PTC upstream of p.Lys351): PVS1
    *   Presumed in tandem. Reading frame presumed disrupted and NMD predicted to occur (nonsense upstream of p.Lys351 or frameshift-induced PTC upstream of p.Lys351): PVS1\_Strong

For variants inducing aberrant transcripts identified via mRNA assay, apply as PVS1\_Variable Weight (RNA) following recommendations from Walker et al., 2023 (PMID: 37352859), downgrading one strength level if the assay data indicates leakiness.

_Caveats_: PS3 should not be applied at any strength if PVS1 is applied at full strength. PP3 should not be used in combination with PVS1.

For the purposes of unified curation, the TP53 domains/important motifs by amino acid range are defined as:

**TAD1**: aa 17-25

**TAD2**: aa 48-56

**Proline residues**: aa 64-92

**DNA binding domain**: aa 100-292

**Hinge domain**: aa 293-324

**Oligomerization domain**: aa 325-356

**C-terminal domain (Basic domain)**: aa 368-387

A disease-specific PVS1 decision tree incorporating the above bullets as well as a supplemental file for _TP53_ PVS1 Splicing Worksheet is also included as an additional curation tool and has more granular details. [PV=8]
- **Strong** ✅：See PVS1 flowchart for code application [PV=4]
- **Moderate** ✅：See PVS1 flowchart for code application [PV=2]

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Can be applied to variants asserted as Pathogenic following the _TP53_ VCEP’s specifications. [PV=4]
- **Moderate** ✅：Can be applied to variants asserted as Likely Pathogenic following the _TP53_ VCEP’s specifications. [PV=2]

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：≥ 8 points [PV=8]
- **Strong** ✅：4-7 points [PV=4]
- **Moderate** ✅：2-3 points [PV=2]
- **Supporting** ✅：1 point [PV=1]

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Non-functional on Kato et al. data **AND** loss of function (LOF) by the majority of other eligible assays [PV=4]
- **Moderate** ✅：Partially functional on Kato et al. data **AND** loss of function (LOF) by the majority of other available assays [PV=2]
- **Supporting** ✅：Non-functional on Kato et al. data **AND** abnormal on Kawaguchi et al. data regardless of other assays

PS3\_Supporting may also be applied to small deletions that demonstrate LOF on the majority of available assays [PV=1]

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：≥ 8 points [PV=8]
- **Strong** ✅：≥ 4-7.5 points [PV=4]
- **Moderate** ✅：2-3.5 points [PV=2]
- **Supporting** ✅：1-1.5 points [PV=1]

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Missense variants within the following codons using transcript NM\_00546.4: 175, 245, 248, 249, 273, 282. This code weight can also be used for germline missense variants seen in cancerhotspots.org with ≥ 10 somatic occurrences for the same amino acid change. [PV=2]
- **Supporting** ✅：Missense variants seen in cancerhotspots.org with 2-9 somatic occurrences for the same amino acid change. [PV=1]

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：This rule should be applied at supporting level. Variant should have an allele frequency of less than 0.00003 (0.003%) in gnomAD or another large sequenced population. If multiple alleles are present within any genetic ancestry group, allele frequency in that group must be \<0.00004 (0.004%). Genetic ancestry groups influenced by founder effects (such as Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and “Remaining”) should be ignored. 

If the variant being assessed does not meet any population rule codes (PM2, BA1, BS1) **AND** has a total allele frequency >0.00003 with no single genetic ancestry group having multiple alleles with a frequency >0.00004, curators should recalculate the total allele frequency based on the number of alleles with variant allele fraction (VAF) >0.35 to assess whether PM2 may be met after excluding the low VAF alleles which are likely to represent clonal hematopoiesis of indeterminant potential (CHIP) contamination in the database. This can be done by visualizing the “allele balance” for heterozygotes under the genotype quality metrics for a given variant. By hovering over the histogram bars, the number of variant carriers for each bar between 0.35 and 0.65 can be totaled and this can be used to revise the allele count to determine the allele frequency that can be used to assess if PM2\_Supporting can be met.

In general, the most recent version of gnomAD should be used when available; however, other population databases or earlier versions of gnomAD may be utilized if they are able to provide information the curator deems necessary for optimal variant classification (e.g, they would provide superior information for a particular variant type; have a larger sample size; or better representation for certain subpopulations, etc.) [PV=1]

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Missense variant at an amino acid residue where ≥2 different missense variants previously determined to be pathogenic according to the _TP53_ VCEP’s specifications have been seen before. [PV=4]
- **Moderate** ✅：Missense variant at an amino acid residue where 1 different missense variant previously determined to be pathogenic according to the _TP53_ VCEP’s specifications has been seen before. [PV=2]
- **Supporting** ✅：Missense variant at an amino acid residue where 1 different missense variant previously determined to be likely pathogenic according to the _TP53_ VCEP’s specifications has been seen before. **The previously seen likely pathogenic variant must have clinical data that demonstrates pathogenicity (i.e. PS2, PS4, PP1) in order for it to count towards PM5\_Supporting code application.** [PV=1]

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Cosegregation must be observed in ≥ 7 meioses across > 1 family [PV=4]
- **Moderate** ✅：Cosegregation must be observed in 5-6 meioses in/across 1 or more families [PV=2]
- **Supporting** ✅：Cosegregation must be observed in 3-4 meioses in/across 1 or more families [PV=1]

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：**Missense variants** _(See flowchart for application of PP3 and BP4 rules for missense variants)_

aGVGD Class C65 and BayesDel score ≥ 0.16 [PV=2]
- **Supporting** ✅：**Missense variants** _(See flowchart for application of PP3 and BP4 rules for missense variants)_

aGVGD class C25-C55 and BayesDel score ≥ 0.16

**Single amino acid inframe deletions** _(See single aa BayesDel spreadsheet)_

BayesDel score ≥ 0.16

**Exonic (including silent variants and apparent “missense” variants or “single amino acid inframe deletions” for which there is a predicted splice effect) or Intronic Splice Variants (excluding ± 1,2 positions):**

SpliceAI ≥ 0.2 [PV=1]

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：At least 2 independent observations of the variant with VAF 5-25%. [PV=2]
- **Supporting** ✅：Observation of the variant with VAF 5-35% (i.e., once or multiple times with VAF >25-35% and/or once with VAF 5-25%) [PV=1]

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Filtering allele frequency (FAF) of ≥ 0.001 or 0.1% in gnomAD continental subpopulations of a single genetic ancestry group (excluding genetic ancestry groups influenced by founder effects, such as Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and “Remaining”). Genetic ancestry group must have ≥2,000 alleles tested and a minimum of 2 alleles present. Caution should be exerted if the majority of alleles have a variant allele fraction ("allele balance" in gnomAD) below 0.35.  To set the stand-alone benign FAF cutoff, we used the FAF cutoff established for BS1 (0.0003) and increased this cutoff by one order of magnitude to come to a value of 0.001. 

In general, the most recent version of gnomAD should be used when available; however, other population databases or earlier versions of gnomAD may be utilized if they are able to provide information the curator deems necessary for optimal variant classification (e.g, they would provide superior information for a particular variant type; have a larger sample size; or better representation for certain subpopulations, etc.) [PV=Not Applicable]

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Filtering allele frequency (FAF) of ≥ 0.0003 but \< 0.001 in gnomAD continental subpopulations of a single genetic ancestry group (excluding genetic ancestry groups influenced by founder effects, such as Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and “Remaining”). Genetic ancestry group must have ≥2,000 alleles tested and a minimum of 2 alleles present. Caution should be exerted if the majority of alleles have a variant allele fraction ( “allele balance” in gnomAD) below 0.35. To set the strong benign FAF cutoff, we used a Whiffin-Ware calculation using prevalence of 1 in 5,000 (Lalloo, et al., 2006 PMID: 16644204). Genetic and allelic heterogeneity were set at 100% and penetrance at 30%. 

In general, the most recent version of gnomAD should be used when available; however, other population databases or earlier versions of gnomAD may be utilized if they are able to provide information the curator deems necessary for optimal variant classification (e.g, they would provide superior information for a particular variant type; have a larger sample size; or better representation for certain subpopulations, etc.) [PV=-4]

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：≥ 8 unrelated females who have reached at least 60 years of age without cancer. These individuals all must have come from a single source (single lab, database, etc). Cases cannot be counted across sources. Individuals with a diagnosis of sarcoma ≥ 61 years of age should not be counted towards the BS2 total. [PV=-4]
- **Moderate** ✅：4-7 unrelated females who have reached at least 60 years of age without cancer. These individuals all must have come from a single source (single lab, database, etc). Cases cannot be counted across sources. Individuals with a diagnosis of sarcoma ≥ 61 years of age should not be counted towards the BS2 total. [PV=-2]
- **Supporting** ✅：2-3 unrelated females who have reached at least 60 years of age without cancer. These individuals all must have come from a single source (single lab, database, etc). Cases cannot be counted across sources. Individuals with a diagnosis of sarcoma ≥ 61 years of age should not be counted towards the BS2 total. [PV=-1]

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Functional on Kato et al. data **AND** no loss of function (LOF) by the majority of available eligible assays [PV=-4]
- **Supporting** ✅：Partially functional on Kato et al. data **AND** no evidence of loss of function (LOF) by **all** available assays

BS3\_Supporting may also be applied to small deletions with available Kotler et al. data that are loss of function (LOF) by the majority of available assays [PV=-1]

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected family members (i.e. family members diagnosed with LFS-associated cancers as described in Table of LFS Cancers and Points for PS2 and PP1 Code Application). [PV=-4]

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Moderate** ✅：**Missense variants** _(See flowchart for application of PP3 and BP4 rules for missense variants):_

BayesDel ≤ -0.008 irrespective of aGVGD score (except C65, in this case do not apply BP4\_Moderate) **AND** no predicted differences in splicing (SpliceAI < 0.2) [PV=-2]
- **Supporting** ✅：**Missense variants** _(See flowchart for application of PP3 and BP4 rules for missense variants):_

BayesDel \< 0.16 and > -0.008 irrespective of aGVGD score (except C65, this case do not apply BP4) AND no predicted differences in splicing (SpliceAI \< 0.2)

**Single amino acid inframe deletions** _(See single aa BayesDel spreadsheet):_

BayesDel score \< 0.16 AND no predicted splicing impact (Splice AI \< 0.2)

**Silent or Intronic Variants (outside ± 1,2 positions):**

SpliceAI ≤ 0.1 [PV=-1]

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：A (synonymous) silent or intronic variant for which RNA splicing assay data demonstrates no splicing aberration, as per recommendations from Walker et al., 2023 (PMID: 37352859). [PV=-4]
- **Supporting** ✅：A synonymous (silent) outside of the core splice motif (last three nucleotides and first nucleotide of the exon) or intronic variant at or beyond +7 to -21 positions for which SpliceAI predicts no impact to the splice consensus nor the creation of a new splice site (BP4 is met, SpliceAI ≤ 0.1). No requirement to assess for nucleotide conservation for rule application as per evidence and recommendations in Walker et al., 2023  (PMID: 37352859). [PV=-1]

### 不适用证据码
PM3、PM4、PM6、PP2、PP5、BP1、BP2、BP3、BP5、BP6
### 参考附件
- [PVS1 Flowchart](https://cspec.genome.network/cspec/File/id/a59085f9-6c52-4c36-9c42-159f3f2c3694/data)
- [Single amino acid BayesDel spreadsheet](https://cspec.genome.network/cspec/File/id/950b0b53-b2a7-4d85-8cde-b6aaa7c7668c/data)
- [Table of LFS Cancers and Points for PS1 and PP1 Code Application](https://cspec.genome.network/cspec/File/id/ac924484-5a6f-43e2-8da7-a480b202f2aa/data)
- [Flowchart for application of PP3, BP4, and BP7](https://cspec.genome.network/cspec/File/id/683fd541-4d24-4aaf-9cfd-61c4fb9a6095/data)
- [Functional results for selected assays and corresponding preliminary functional codes for p53 missense variants](https://cspec.genome.network/cspec/File/id/f7b4de92-567a-497d-a8db-0f673c8bb36c/data)
- [Simplified table for tallying proband points for PS4](https://cspec.genome.network/cspec/File/id/0d65bfaa-d4d5-4bc8-9503-76bf43bea7e6/data)
- [Flowchart for application of functional rule codes](https://cspec.genome.network/cspec/File/id/16e04e7f-f7c7-4bff-953c-dfe31559d734/data)
- [PVS1 Splicing Worksheet](https://cspec.genome.network/cspec/File/id/811e59dd-d7b5-4ab1-9295-f8ff75f2dfb7/data)
- [Bioinformatics predictions and corresponding preliminary PP3 and BP4 codes for p53 missense variants](https://cspec.genome.network/cspec/File/id/f24d9c2f-5cb4-4c1a-bdf6-7d73331fc77b/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN009)

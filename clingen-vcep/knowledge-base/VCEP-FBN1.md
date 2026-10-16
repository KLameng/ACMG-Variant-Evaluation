# ClinGen VCEP基因特异性规范：FBN1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN022 — FBN1 Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0007947**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：* Nonsense/frameshift variants predicted to undergo NMD (not affecting last exon or 55 last nt of penultimate exon).
 * 1,2 splice site variants leading to exon skipping or use of a cryptic splice site disrupting the reading frame and predicted to undergo NMD.
 * Full gene deletion.
 * Single to multi-exon deletion disrupting the reading frame and predicted to undergo NMD.
 * Duplication (>=1 exon in size and completely contained within gene) proven in tandem and disrupting the reading frame and predicted to undergo NMD.
- **Strong** 📋：* Nonsense/frameshift variants predicted to escape NMD (affecting last exon, last 55nt of the penultimate exon).
 * 1,2 splice site variants leading to exon skipping or use of a cryptic splice site disrupting the reading frame and predicted to escape NMD.
 * 1,2 splice site variants leading to exon skipping or use of a cryptic splice site but preserving the reading frame.
 * Single to multi-exon deletion disrupting the reading frame and predicted to escape NMD.
 * Single to multi-exon deletion preserving the reading frame.
 * Duplication (>=1 exon in size and completely contained within gene) presumed in tandem and presumably disrupting the reading frame and predicted to escape NMD.
- **Moderate** 📋：* Initiation codon variant with 1 or more pathogenic variant(s) upstream of closest potential in-frame start codon.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：* Beware of changes that impact splicing rather than the amino acid. Splicing predictions should remain the same for WT and mutant alleles.
* Original variant should be pathogenic according to the (modified) ACMG guidelines for variant classification.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** 📋：Four points
- **Strong** 📋：Two-three points
- **Moderate** 📋：One point
- **Supporting** 📋：0.5 points

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Follow the ‘Funtional Assay SVI Documentation’
- **Moderate** 📋：Follow the ‘Funtional Assay SVI Documentation’
- **Supporting** 📋：Use the ‘Funtional Assay SVI Documentation’.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：* If ≥ 4 points.
- **Moderate** 📋：* If 2-3.5 points.
- **Supporting** 📋：* If 1-1.5 points.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** 📋：* Cys residues in cbEGF-like domains
* Add caveat: PM5/PS1 should not be used when this argument applies.
- **Moderate** 📋：* Cys in EGF-like domain, Cys in TB domain, Cys in hybrid domain, (D/N)-X-(D/N)-(E/Q)-Xm-(D/N)-Xn-(Y/F) substitution in cbEGF-like domain, invariant calcium-binding or hydroxylation residue in cbEGF-like domain, critical Gly between Cys2-Cys3 in cbEGF-like domain, Gly between Cys3-Cys4 if there is an upstream cbEGF domain, Cys-creating variants.
* Add caveat: N to S substitution in the second N of de consensus sequence and G to A might be tolerated, PM1 should not be used in these cases.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：* Threshold: <5.0E-6 (<0.0005%).
* Use the highest ethnic population allele frequency.
* Caveat: PVS1 + PM2_Supportive may reach Likely Pathogenic.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：* Add caveat: cannot be applied simultaneously with PVS1 (at any strength level)

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：* Add caveat: Use argument with caution when the original missense variant created a cysteine especially in a cbEGFlike domain (cfr PM1_strong) as this may increase the
pathogenicity level of this variant improperly.
* Add caveat: original variant should be pathogenic according to the (modified) ACMG guidelines for variant classification.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** 📋：4 points
- **Strong** 📋：2-3 points.
- **Moderate** 📋：1 point.
- **Supporting** 📋：0.5 points.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：≥5 affected individuals.
- **Moderate** 📋：4 affected individuals.
- **Supporting** 📋：2-3 affected individuals.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** 📋：Add caveat: if this argument is used pro-pathogenicity, there must be other arguments supporting pathogenicity, and no arguments supporting a benign assertion.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：* Recommended prediction program for missense variants: REVEL. Use 0.75 as a discriminatory cut-off value.
* Recommended prediction programs for splice variants: GeneSplicer, MaxEntscan, and NNSPLICE. The outcome of all 3 prediction programs need to be in concordance.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** 📋：* Use if patient fulfils revised Ghent criteria.
* Can be used if any of the family members have a highly specific phenotype.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Allele frequency above 0.1% in ExAc and gnomAD
* Use the ethnic population with the highest allele frequency.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Allele frequency greater than expected for disease (>0.005%).
* Use the ethnic population with the highest allele frequency.
* Caveat: Do not use Finnish, Ashkenazi Jewish, or “Other” populations in gnomAD.
* Minimum amount of studied alleles should be 2000.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Use the ‘Funtional Assay SVI Documentation’ (https://clinicalgenome.org/working-groups/sequence-variant-interpretation/).
For step 2 assessment.
* Functional studies deemed appropriate:
 * cDNA analyses showing altered FBN1 sequence.
 * Functional studies showing altered FBN1 protein or RNA expression, proteolysis, folding, assembly, trafficking, secretion, Ca2+ binding, matrix deposition (cfr Dave Hollister assay), microfibril fragmentation/catabolism in an in vitro engineered system.
* Functional studies NOT deemed appropriate: non-specific altered TGF-beta signaling or histological hallmarks of medial degeneration, which are associated with many other types of variants in genes that are associated with MFS or HTAAD in general.
For step 3 assessment: Studies should be performed in the presence of NMD inhibitor.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：* Caution is warranted when the phenotype is not highly specific. Lack of segregation should then be clear in >1 affected family member.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：* Observed in trans in multiple cases (+2) with co-occuring pathogenic variants and phenotype is not more severe than when seen in isolation.
* Observed in cis with a pathogenic variant, if the pathogenic variant has been seen in isolation in a patient with the disease phenotype.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：* Recommended prediction program for missense variants: REVEL. Use 0.326 as a discriminatory cut-off value.
* Recommended prediction programs for splice variants: GeneSplicer, MaxEntscan, and NNSPLICE. The outcome of all 3 prediction programs need to be in concordance.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** 📋：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** 📋：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
BP7 applicable as described.

### 不适用证据码
PM3、PP5、BS2、BP1、BP3、BP6

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN022)

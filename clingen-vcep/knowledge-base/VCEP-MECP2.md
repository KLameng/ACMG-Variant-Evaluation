# ClinGen VCEP基因特异性规范：MECP2

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 6.0（Released；DOI 10.5281/zenodo.21421705；Rett and Angelman-like Disorders VCEP；核验 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN036 — Rett and Angelman-like Disorders Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010726**（遗传方式：X-linked inheritance）

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

*   Use as defined by ClinGen SVI working group (PMID:30192042).
*   PVS1 is applicable for:
    *   Null variants up to p.E472
    *   Any frameshift variant that results in a read-through of the stop codon
    *   Canonical splice site variants predicted to result in an out-of-frame product
    *   Canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exon 3)
    *   A full gene deletion
*   PVS1 is **not** applicable for initiation codons.
- **Strong** ✅：*   PVS1\_Strong is applicable for:
    *   Canonical splice site variants or deletions (single exon to full gene deletion) resulting in exon skipping or use of a cryptic splice site that disrupts reading frame and is **NOT** predicted to undergo NMD, but the truncated/altered region is critical to protein function (exon 4).
- **Moderate** ✅：*   PVS1\_Moderate is applicable for any truncating variant distal of p.E472.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：De novo (maternity and paternity confirmed) in a patient with the disease and no family history.
* ≥2 independent occurrences of PS2.
* ≥2 independent occurrences of PM6 and one occurrence of PS2.
- **Strong** ✅：De novo (maternity and paternity confirmed) in a patient with the disease and no family history.

*   1 occurrence of PS2.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.
* RNA studies that demonstrate abnormal splicing and an out-offrame transcript.
* Do not use for canonical splice site variants and when PVS1 is used.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.

*   RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section).
*   See included table for approved functional studies.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* 5+ observations.
- **Moderate** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* 3-4 observations.
- **Supporting** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls.
* Use for 2nd independent occurrence.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain.

*   Methyl-DNA binding (MBD): aa 90-162
*   Transcriptional repression domain (TRD): aa 302-306

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/rare from controls in an ethnically-matched cohort population sample.
* Use if absent, zero observations in control databases.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：Protein length changes due to stop-loss variants. PM4_Strong is applicable to stop-loss variants in MECP2, as several stop-loss variants in this gene have been described in affected individuals.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

*   Do not use PM4 for in-frame deletions/insertions in the Proline-rich region of gene (p.381-p.405)
- **Supporting** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
* Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene).

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
* ≥2 different missense changes affecting the amino acid residue.
* Do not apply PM1 in these situations.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Very Strong** ✅：Confirmed de novo without confirmation of paternity and maternity.

*   ≥4 independent occurrences of PM6. 
*   Evidence from literature must be fully evaluated to support independent events.
- **Strong** ✅：Confirmed de novo without confirmation of paternity and maternity.

*   ≥2 independent occurrences of PM6.
*   Evidence from literature must be fully evaluated to support independent events.
- **Moderate** ✅：Confirmed de novo without confirmation of paternity and maternity.

*   1 occurrence of PM6.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members.

*   ≥5 informative meiosis
- **Moderate** ✅：Co-segregation with disease in multiple affected family members.

*   3-4 informative meiosis
- **Supporting** ✅：Co-segregation with disease in multiple affected family members.

*   2 informative meiosis

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

*   For missense variants use REVEL with a score ≥ 0.644.
*   For splice site variants use SpliceAI with a score ≥ 0.2.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：Phenotype specific for disease with single genetic etiology.
* See gene specific clinical phenotype guidelines.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：*   Use large population databases (i.e. gnomAD).
*   Use if variant is present at ≥0.000083 (0.0083%) in any sub-population.
*   Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：*   Use large population databases (i.e. gnomAD).
*   Use if variant is present at ≥0.0000083 (0.00083%) and \<0.000083 (0.0083%) in any sub-population.
*   Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in the heterozygous/hemizygous state in a healthy adult.

*   2 unaffected (related or unrelated) heterozygotes or hemizygotes.
- **Supporting** ✅：Observed in the heterozygous/hemizygous state in a healthy adult.

*   1 unaffected (related or unrelated) heterozygote or hemizygote

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function.

*   RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data.
*   Not applicable for other functional studies.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.

*   Absent in a similarly affected family member, when seen in two or more families
- **Supporting** ✅：Lack of segregation in affected members of a family.

*   Absent in a similarly affected family member

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function.
*   BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)

*   For missense variants use REVEL with a score ≤ 0.290.
*   For splice site variants use SpliceAI with a score ≤ 0.1.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：Variant found in a case with an alternate molecular basis for disease.
* ≥3 cases with alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

*   1 case with alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

*   Defined 'not highly conserved' regions in BP7 as those with PhastCons score \<1 and/or PhyloP score \<0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species.
*   For splice site variants use SpliceAI with a score ≤ 0.1.

### 组合规则（Rules for Combining Criteria；官网 v6.0，Richards 2015 组合规则面板）

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

**Benign（良性）**
1. ≥ 2 Strong
2. 1 Stand Alone
3. 1 Strong AND 3 Supporting

**Likely Benign（可能良性）**
1. ≥ 2 Supporting
2. 1 Strong

### 不适用证据码
PM3、PP2、PP5、BP1、BP6
### 参考附件
- [PVS1 Flowchart for MECP2](https://cspec.genome.network/cspec/File/id/0315aa23-bdd2-4537-85d6-d3347838e89b/data)
- [Clinical Phenotype Guidelines for MECP2](https://cspec.genome.network/cspec/File/id/a4f8da9f-058e-4e54-a275-3a5ff228abcc/data)
- [MECP2 Functional Assays](https://cspec.genome.network/cspec/File/id/a3435952-c929-42dd-ae02-d61b042daa40/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN036)

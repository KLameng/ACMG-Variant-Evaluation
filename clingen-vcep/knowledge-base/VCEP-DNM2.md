# ClinGen VCEP基因特异性规范：DNM2

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 1.0（DOI: 10.5281/zenodo.21434746；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN148 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0018947**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3' end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Not Applicable** ✅：Loss of function is not a mechanism of disease for DNM2-related AD Centronuclear myopathy

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：No change - use as originally described
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength.
- **Moderate** ✅：The two assays from PS3\_Supporting may be stacked to reach a Moderate Strength
- **Supporting** ✅：Two specific assays are currently suggested to be applied at Supporting:

1.  Oligomerization: An abnormal readout consists of integration of increased dynamin stability compared to WT dynamin.
2.  GTPase activity: An abnormal readout consists of increased GTPase activity or increased stability compared to wild type dynamin.

If not listed above, it is acceptable to use PS3\_Supporting for other functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Specific phenotypes for proband counting include:

**A Congenital myopathy panel should be run and negative for other variants (must include BIN1, RYR1, MTM1) AND at least two of these features:**

*   Presence on Muscle Biopsy of: Oxidative activity and/or radial stranding with spokes on a wheel appearance with centrally nucleated muscle fibers
*   Distal weakness
*   Characteristic muscle imaging (See Figure 9 of Saade et al 2019 PMID: 31060725 for example)
*   Ophthalmoparesis and Ptosis (both of these must be observed to count this as one phenotype criteria)

At least 1 point, please see PS4 chart
- **Moderate** ✅：0.5 points, please see PS4 chart
- **Supporting** ✅：0.25 points, please see PS4 chart

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is absent (1 allele allowed)

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Supporting** ✅：No change - use as originally described

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：No change - use as originally described

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.
- **Supporting** ✅：No change - use as originally described

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：At least five segregations
- **Moderate** ✅：Four segregations
- **Supporting** ✅：At least 2 segregations

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：DNM2 is a gene that is constrained for missense variation (gnomAD v4.1 z=4.87). PP2 may be used for missense variants.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：BS3\_Supporting is met if **both** of these assays have WT readouts:

Oligomerization Assay: DNM2 assembly/disassembly dynamics similar to wild type DNM2

GTPase Activity Assay: GTPase activity and stability similar to wild type DNM2

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc) Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

BP4 is met if the REVEL score ≤ 0.15 or if the variant is not predicted to impact splicing using SpliceAI.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

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
PVS1、PM1、PM3、PP4、PP5、BP1、BP3、BP6
### 参考附件
- [DNM2 PS4 rules](https://cspec.genome.network/cspec/File/id/9b088a33-0474-4527-8599-3b3eb0b02f21/data)
- [Segregation Chart](https://cspec.genome.network/cspec/File/id/cc7b4a19-853e-42a8-bbb6-ce576f75297f/data)
- [Approved functional assays for DNM2](https://cspec.genome.network/cspec/File/id/d5749ba5-1bb1-4791-b9e6-e8f2b0a6687f/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN148)

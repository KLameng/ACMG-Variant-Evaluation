# ClinGen VCEP基因特异性规范：ACTA1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：GN147 v2.0（DOI: 10.5281/zenodo.21434744）/ GN169 v1.0（DOI: 10.5281/zenodo.21434783），Released，2026-10-09 官网实页核验
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN169 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100084**（遗传方式：Autosomal recessive inheritance）

### 通用说明
*Note on multiple Modes of Inheritance: In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it’s de novo, it’s much more likely to be AD and if it’s observed with a second variant, it’s much more likely to be AR. Loss of function variants are almost always associated with AR disease. For truncating/putative LOF variants, this is easier to determine, but some missense variants are observed that may have LOF functional consequence. The AD and AR specifications are listed separately.          
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Strong** ✅：See PVS1 flowchart
- **Moderate** ✅：See PVS1 flowchart
- **Supporting** ✅：See PVS1 flowchart

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
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
- **Supporting** ✅：There are no specific functional assays listed for the ACTA1 AR specifications; all should be used for AD specifications. However, it is acceptable to use PS3\_Supporting for functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is 

≤ 0.000005 for autosomal recessive

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：4.0 points per the PM3 chart
- **Strong** ✅：2.0 points per the PM3 chart
- **Moderate** ✅：For recessive disorders, detected in trans with a pathogenic variant Note: This requires testing of parents (or offspring) to determine phase.

1.0 points per the PM3 chart
- **Supporting** ✅：0.5 points per the PM3 chart

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
- **Strong** ✅：See segregation chart
- **Moderate** ✅：See segregation chart
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

See segregation chart

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：PP4 follows the published SVI guidance from Biesecker et al 2023 (PMID:38103548). For ACTA1, a conservative estimate of the diagnostic yield is 33%, which corresponds to +2 points and a moderate strength in Table 2 of this guidance. However, if the proband meets PP4\_Moderate criteria and has had a comprehensive myopathy panel, exome, or genome testing that is negative for all other causes of myopathy, PP4 can be applied at strong, per the SVI guidance. 

The combination of PP1 and PP4 is capped at strong. PP1+PP4 combined cannot exceed Bayesian 5 points.
- **Moderate** ✅：PP4 follows the published SVI guidance from Biesecker et al 2023 (PMID:38103548). For ACTA1, a conservative estimate of the diagnostic yield is 33%, which corresponds to +2 points and a moderate strength in Table 2 of this guidance. 

PP4\_Moderate is met with the presence of any of these features

**Presence on Muscle Biopsy of:**

*   Accumulated thin filaments
*   Intranuclear rods
*   Cores, fiber type disproportion
*   Zebra bodies
- **Supporting** ✅：If a biopsy demonstrates a presence of nemaline rods, this is suggestive of ACTA1-related congenital myopathy and can be given PP4 at a supporting level.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0025 for AR variants**. All continental populations in gnomAD used should have at least 2000 alleles and >1 observation. 

**BA1 exclusion variants** (well-known pathogenic variants that are above the specified BA1 threshold) are as follows: 

NM\_001100.4(ACTA1):c.541del (p.Asp181fs)

NM\_001100.4(ACTA1):c.121C>T(p.Arg41\*)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00025 for AR** **variants**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

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
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### 组合规则（Rules for Combining Criteria）

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

**Likely Benign（可能良性）**
1. 1 Strong AND 1 Supporting
2. ≥ 2 Supporting

### 不适用证据码
PS4、PM1、PP2、PP5、BS3、BP1、BP3、BP6
### 参考附件
- [PVS1 flowchart for ACTA1](https://cspec.genome.network/cspec/File/id/ac3a9211-5556-4c57-87f6-f41c4653a37a/data)
- [PP1 segration table](https://cspec.genome.network/cspec/File/id/5ce07575-cbcd-4ac8-a521-25a2edd3f44d/data)
- [ACTA1 PM3 guidance](https://cspec.genome.network/cspec/File/id/c08b5680-6556-43e9-8be7-9e7af5aebbf4/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN169)

## 规范 2：GN147 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100084**（遗传方式：Autosomal dominant inheritance）

### 通用说明
*Note on multiple Modes of Inheritance: In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it’s de novo, it’s much more likely to be AD and if it’s observed with a second variant, it’s much more likely to be AR. Loss of function variants are almost always associated with AR disease. For truncating/putative LOF variants, this is easier to determine, but some missense variants are observed that may have LOF functional consequence. The AD and AR specifications are listed separately.
            
            
            
           

### 基因特异性证据规则

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
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
- **Supporting** ✅：Three specific assays are currently suggested to be applied at Supporting:

1.  Actin Localization: An abnormal readout consists of integration of actin into cytoplasmic or intranuclear aggregates or rods.
2.  Actin Polymerization: An abnormal readout consists of a significant reduction in levels of actin in insoluble fraction or absent or short polymerized actin filaments compared to WT.
3.  Actin Motility Assay: An abnormal readout consists of percent motility, velocity, and force generation statistically different from WT.

If not listed above, it is acceptable to use PS3\_Supporting for other functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：8 case observations
- **Moderate** ✅：4 case observations
- **Supporting** ✅：2 case observations

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is 

absent (1 allele allowed) for autosomal dominant

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
- **Strong** ✅：See segregation chart
- **Moderate** ✅：See segregation chart
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

See segregation chart

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：ACTA1 is a gene that is constrained for missense variation (gnomAD v4.1 z=6.09). PP2 may be used for missense variants with an autosomal dominant mode of inheritance.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：PP4 follows the published SVI guidance from Biesecker et al 2023 (PMID:38103548). For ACTA1, a conservative estimate of the diagnostic yield is 33%, which corresponds to +2 points and a moderate strength in Table 2 of this guidance. However, if the proband meets PP4\_Moderate criteria and has had a comprehensive myopathy panel, exome, or genome testing that is negative for all other causes of myopathy, PP4 can be applied at strong, per the SVI guidance.   


- **Moderate** ✅：PP4 follows the published SVI guidance from Biesecker et al 2023 (PMID:38103548). For ACTA1, a conservative estimate of the diagnostic yield is 33%, which corresponds to +2 points and a moderate strength in Table 2 of this guidance. 

PP4\_Moderate is met with the presence of any of these features

**Presence on Muscle Biopsy of:**

*   Accumulated thin filaments
*   Intranuclear rods
*   Cores, fiber type disproportion
*   Zebra bodies
- **Supporting** ✅：If a biopsy demonstrates a presence of nemaline rods, this is suggestive of ACTA1-related congenital myopathy and can be given PP4 at a supporting level.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0000781 for AD variants**. All continental populations in gnomAD used should have at least 2000 alleles and >1 observation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00000781 for AD variants**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

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
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### 组合规则（Rules for Combining Criteria）

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

**Likely Benign（可能良性）**
1. 1 Strong AND 1 Supporting
2. ≥ 2 Supporting

### 不适用证据码
PVS1、PM1、PM3、PP5、BS3、BP1、BP3、BP6
### 参考附件
- [PP1 segregation chart](https://cspec.genome.network/cspec/File/id/a90592af-5aac-408a-9f16-6baa1c40ffaf/data)
- [Approved AD ACTA1 functional assays](https://cspec.genome.network/cspec/File/id/d4edfefb-67f5-464d-8cb0-29dd922ff5ea/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN147)

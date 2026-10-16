# ClinGen VCEP基因特异性规范：HBA2

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v1.0.0（2026-03-20，Hemoglobinopathy VCEP；经浏览器 live 页核实）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN173 — Hemoglobinopathy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0100562**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.  

Caveats:  

Use caution interpreting LOF variants at the extreme 3’ end of a gene.

Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- **Strong** ✅：Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.  

Caveats:  

Use caution interpreting LOF variants at the extreme 3’ end of a gene.

Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- **Moderate** ✅：Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.  

Caveats:  

Use caution interpreting LOF variants at the extreme 3’ end of a gene.

Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
- **Moderate** ✅：The same change of an amino acid shown to be a pathogenic variant in a paralogue gene.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：_De novo_ (both maternity and paternity confirmed) in a patient with the disease or in a phenotypic trait individual and no family history.  

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, _etc._ can contribute to non-maternity.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：_In vitro_ or _in vivo_ functional studies supportive of a damaging effect on the gene, gene product, expression levels and protein function.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. Strength evidence is determined by points according to Appendix 3. Very Strong evidence requires ≥16 points
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. Strength evidence is determined by points according to Appendix 3. Strong evidence requires 3.5-15.99 points
- **Moderate** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. Strength evidence is determined by points according to Appendix 3. Moderate evidence requires 1.5-3.49 points.
- **Supporting** ✅：The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. Strength evidence is determined by points according to Appendix 3. Supporting evidence requires 0.5-1.49 points

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.  

*   AHSP binding (α32R, α104H, α118F, α120P)
*   Poly(A) signals: AATAAA sequence

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Allele frequency \<0.0001 (0.01%) in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：For recessive disorders, detected _in trans_ with a pathogenic or likely pathogenic variant in an affected patient 

Strength is determined using the ClinGen SVI guidelines.
- **Strong** ✅：For recessive disorders, detected _in trans_ with a pathogenic or likely pathogenic variant in an affected patient. Strength is determined using the ClinGen SVI guidelines.
- **Moderate** ✅：For recessive disorders, detected _in trans_ with a pathogenic or likely pathogenic variant in an affected patient. 

Strength is determined using the ClinGen SVI guidelines.
- **Supporting** ✅：For recessive disorders, detected _in trans_ with a pathogenic or likely pathogenic variant in an affected patient. 

Strength is determined using the ClinGen SVI guidelines.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes as a result of in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before, or base change at a non-coding position and previous pathogenic mutation has been seen before. 

Examples:  

Arg156His is pathogenic; now you observe Arg156Cys.  

Non-coding variant g.15300G>C is pathogenic, now you observe g. 15300G>A.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** ✅：Assumed _de novo_, but without confirmation of paternity and maternity.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease. Strong evidence requires LOD score >2.1.
- **Moderate** ✅：Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease. MODERATE evidence requires LOD score >1.5.
- **Supporting** ✅：Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease. SUPPORTING evidence requires LOD score >0.9.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

For missense: REVEL score > 0.8 OR SpliceAI > 0.3. If REVEL score is not available, use CADD PHRED score > 23.5 

For non-coding, synonymous, inframe indels, stop-lost: CADD PHRED score > 12 OR SpliceAI DS > 0.3 

Should not be used for LOF variants considered in PVS1.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency ≥0.005 (0.5%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency ≥0.001 (0.1%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Two independent occurrences in individuals (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age.
- **Supporting** ✅：Observation in one individual (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：_In vivo_ or _in vitro_ functional studies show no damaging effect on gene, gene product, expression levels and protein function.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed _in_ _cis_ with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.)

For missense: REVEL score \< 0.7 AND SpliceAI DS ≤ 0.3 (if REVEL score is not available, use CADD PHRED score ≤ 20, instead) 

For non-coding, synonymous, inframe indels, stop-lost: CADD PHRED score ≤ 11  AND SpliceAI DS ≤ 0.3

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### Rules for Combining Criteria

> 采用 Richards et al. 2015 标准组合规则（通用强度层级，未逐码枚举）。

#### Pathogenic
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting
- ≥ 2 Very Strong (PVS1, PS4_Very Strong, PM3_Very Strong)

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
PP2、PP4、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [Appendix 2_Functional Studies](https://cspec.genome.network/cspec/File/id/b2d81d6b-872d-46df-9c14-7b4b589b9f21/data)
- [Appendix 4_Exclusion variants](https://cspec.genome.network/cspec/File/id/000fe375-a0ba-4535-b3ea-8b77633d1218/data)
- [PVS1 decision tree](https://cspec.genome.network/cspec/File/id/e865ebfa-49b9-41d0-b9f0-06e534812b4b/data)
- [Appendix 3_Evaluation of phenotypes in heterozygotes_PS4](https://cspec.genome.network/cspec/File/id/32778569-0255-493e-83f9-e5ad2e482179/data)
- [Appendix 1_Segregation analysis](https://cspec.genome.network/cspec/File/id/37c11324-8b08-467c-863d-517d1d94e10b/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN173)

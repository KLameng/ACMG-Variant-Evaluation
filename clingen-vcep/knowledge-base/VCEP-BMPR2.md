# ClinGen VCEP基因特异性规范：BMPR2

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN125 — Pulmonary Hypertension Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0015924**（遗传方式：Autosomal dominant inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Caveats:

*   Use caution interpreting LOF variants at the extreme 3’ end of a gene.
*   Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.

\*\*Use the PVS1 decision tree guide.
- **Strong** ✅：Use the PVS1 decision tree guide.
- **Moderate** ✅：Use the PVS1 decision tree guide.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established _**pathogenic**_ variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Same amino acid change as a previously established _**likely pathogenic**_ variant regardless of nucleotide change. For splice variants outside splice donor/acceptor ± 1,2 dinucleotide positions but residing in the same splice donor motif (last 3 bases of the exon and intronic positions +3 to +6) or acceptor motif (first base of the exon and intronic positions -20 to -3) as a previously established _**pathogenic**_ variant. The splice motif coordinates are as defined by Walker et al 2023 (PMID: 37352859).
- **Supporting** ✅：For splice variants outside splice donor/acceptor ± 1,2 dinucleotide positions, same splice donor motif (last 3 bases of the exon and intronic positions +3 to +6) or acceptor motif (first base of the exon and intronic positions -20 to -3) as a previously established _**likely**_ _**pathogenic**_ variant. The splice motif coordinates are as defined by Walker et al 2023 (PMID: 37352859).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Use the BMPR2 functional assay document for guidance on allowable assays. The document is based on the recommendations by Brnich et al 2019 (PMID: 31892348). Known variant validation controls (i.e. established pathogenic and benign variants) are required. One exception is if the same functional assay has been performed for the same variant by two independent groups and demonstrated to have the same functional effect by both groups. Also applicable for non-canonical splice site variants when RNA splice site assay data is available demonstrating abnormal splicing; positive and negative controls are required, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive.
- **Supporting** ✅：Use the BMPR2 functional assay document for guidance on allowable assays as described above. If no known variant validation controls (i.e. established pathogenic and benign variants) were used, then score at the supporting strength.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Prior observation of the variant in >4 unrelated patients with the same phenotype, and its absence in controls.
- **Moderate** ✅：Prior observation of the variant in >3 unrelated patients with the same phenotype, and its absence in controls.
- **Supporting** ✅：Prior observation of the variant in >1 unrelated patients with the same phenotype, and its absence in controls.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Strong** ✅：Variant changes a _critical_ amino acid. Extracellular domain: p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123. Kinase domain: p.Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353 Glu386, Asp405, Gly410, Arg491. KD heterodimerization: p.Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, Leu492.

Note that Gly182Asp and Met186Val have been demonstrated _non-critical/not necessary_ for kinase activity based on a luciferase assay (PMID: 18321866) (apply BS3). We note that Glu503Asp has demonstrated lack of of effect on canonical signaling in one assay, this has not been replicated in an independent assay; in the absence of further investigation, this variant cannot be conclusively designated non-critical (do not apply BS3). While tested variants in the extracellular domain (p.Gln42Arg, Gly47Asn, Gln82His, Thr102Ala, Ser107Pro) have limited or no effect on canonical signaling, studies have indicated that they may play a role in disruption of non-canonical/SMAD-independent pathways (PMIDs: 14583445 and 16002577). In the absence of further investigation, these variants cannot be conclusively designated non-critical (do not apply BS3).
- **Moderate** ✅：Variant changes an amino acid in the extracellular domain (aa 33-131) or kinase domain (aa 203-504) but without functional evidence indicating critical or non-critical.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Present at \<0.01% among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts. Caveat: Population data for indels may be poorly called by next generation sequencing.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be _**pathogenic**_ has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.  Also applicable for variants affecting the same splice site as a confirmed splice variant with similar or worse splicing in silico predictions
- **Supporting** ✅：Novel missense change at an amino acid residue where a different missense change determined to be _**likely pathogenic**_ has been seen before.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in ≥7 affected family members.
- **Moderate** ✅：Co-segregation with disease in ≥5 affected family members.
- **Supporting** ✅：Co-segregation with disease in ≥3 affected family members.

#### PP2
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.
- **Supporting** ✅：PM2\_supporting and PP3 must be met.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Two out of three REVEL/AlphaMissense/CADD predictor scores must meet the thresholds for supporting as specified in Pejaver 2022 PMID: 36413997 (CADD) and Bergquist et al 2025 PMID: 40084623 (AlphaMissense, REVEL). CADD ≥25.3, AlphaMissense ≥0.792, REVEL ≥0.644. The criterion can also be used for non-canonical splice variants if SpliceAI ≥0.2.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency is above 1% in gnomAD, including any sub-population with at least 1,000 allele counts.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency ≥0.1% among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in ≥3 homozygotes in gnomAD controls or reported in the literature (healthy adult individuals).
- **Moderate** ✅：Observed in ≥2 homozygotes in gnomAD controls or reported in the literature (healthy adult individuals).
- **Supporting** ✅：Observed in ≥1 homozygote in gnomAD controls or reported in the literature (healthy adult individuals).

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Use the BMPR2 functional assay document for acceptable assays and guidance. Note that Gly182Asp and Met186Val have been demonstrated _non-critical/not necessary_ for kinase activity based on a luciferase assay (apply BS3). We note that Glu503Asp has demonstrated lack of of effect on canonical signaling in one assay, this has not been replicated in an independent assay; in the absence of further investigation, this variants cannot be conclusively designated non-critical (do not apply BS3). While tested variants in the extracellular domain (p.Gln42Arg, Gly47Asn, Gln82His, Thr102Ala, Ser107Pro) have limited or no effect on canonical signaling, studies have indicated that they may play a role in disruption of non-canonical/SMAD-independent pathways (PMIDs: 14583445 and 16002577). In the absence of further investigation, these variants cannot be conclusively designated non-critical (do not apply BS3).

Note that p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123, Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353 Glu386, Asp405, Gly410, Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, Arg491, and Leu492 have been demonstrated _critical_ (apply PM1\_strong).
- **Supporting** ✅：For variants that have demonstrated limited or no effect on canonical signaling but not tested for effect on non-canonical/SMAD-independent pathways (PMID: 14583445 and 16002577).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of variant segregation in affected members of a family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：No change - use as originally described

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In frame-deletions/insertions in a repetitive region without a known function.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Two out of three REVEL/AlphaMissense/CADD predictor scores must meet the thresholds for supporting as specified in Pejaver 2022 PMID: 36413997 (CADD) and Bergquist et al 2025 PMID: 40084623 (AlphaMissense, REVEL). CADD ≤22.7, AlphaMissense ≤0.169, REVEL ≤0.29. The criterion can also be used for non-canonical splice variants if SpliceAI ≤0.1; can be applied in conjunction with BP7. For synonymous variants, CADD ≤22.7 is sufficient since REVEL and AlphaMissense are not applicable.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：No change - use as originally described

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：If BP7 is met and negative RNA splicing assay data is available, then apply BP7\_strong. Acceptable splicing assays should have positive and negative controls, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive.
- **Supporting** ✅：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Applicable after assignment of BP4 for no adverse splicing predictions, and inclusive of exonic and intronic variants. Not applicable for synonymous variants located at the first base or the last three bases of an exon.

### 不适用证据码
PM3、PM6、PP4、PP5、BP1、BP6
### 参考附件
- [BMPR2 Functional assay guide related to PS3](https://cspec.genome.network/cspec/File/id/5a000534-0957-406e-a72e-06b64cdcf68a/data)
- [Data and citations related to PS4](https://cspec.genome.network/cspec/File/id/071c2e2d-b468-4e4c-b93f-dabdcea7d334/data)
- [Data and citations related to PM1](https://cspec.genome.network/cspec/File/id/beb60c91-00a9-48e3-bf82-5883c0abe6b4/data)
- [PH VCEP Pilot Results_BMPR2 final 1.2026](https://cspec.genome.network/cspec/File/id/7ad16ade-5c44-450e-9bfe-185c66b45cde/data)
- [Point-based system for variant classification](https://cspec.genome.network/cspec/File/id/137bdee2-ce1b-4856-8132-ac79e1078fc1/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN125)

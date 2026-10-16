# ClinGen VCEP基因特异性规范：IDUA

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：GN091 v1.1（Released，DOI: 10.5281/zenodo.21435812，2026-10-09 官网实页核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN091 — Lysosomal Diseases Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0001586**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   All nonsense and frameshift variants will meet PVS1 (Very Strong), unless the variant is predicted to be undetected by nonsense-mediated decay (NMD) i.e. if the resulting premature termination codon is in the last exon (exon 14) or in the last 50 nucleotides of the penultimate exon (exon 13; after c.1778, codon 592). In this case, PVS1\_Moderate will be applied because \<10% of the primary amino acid sequence is predicted to be lost (in this case, ~9.3%).
*   For all variants involving either the +1 or +2 position of GT donor splice sites, the exon immediately 5’ of the variant is predicted to be skipped, and for all variants involving either the -1 or -2 position of AG acceptor splice sites, the exon immediately 3’ of the variant is predicted to be skipped, unless indicated otherwise by RT-PCR or in silico prediction. For the predicted in frame/out of frame consequences for skipping any exon in IDUA, and recommended weight for PVS1, see Appendix 1.
*   Follow the recommendations of Walker et al (PMID: 37352859) for all variants occurring in splice motifs (the donor site motif = last 3 nucleotides of an exon and first 6 nucleotides of an intron; acceptor site motif = first nucleotide of an exon and 20 nucleotides upstream from the exon boundary).
*   If a single or multi-exon deletion results in an out-of-frame consequence, use PVS1 (Very Strong) if NMD is predicted to occur.
*   Initiation codon variants will meet PVS1.
    *   The next in-frame methionine is at position 133. If used as a start signal, the signal sequence (amino acids 1-27) would be lost ([https://www.uniprot.org/uniprotkb/P35475/entry](https://www.uniprot.org/uniprotkb/P35475/entry))
    *   There are 6 variants, upstream of Met133, that are classified as pathogenic in ClinVar (data accessed July 20, 2022) (Table 1).
*   If a deletion results in an in-frame consequence, the deletion must encompass one or more exons for PVS1 to apply. Consult Appendix 1 and use professional judgment regarding the strength of evidence to apply.
*   For duplications, consult the PVS1 decision tree and Appendix 1 to assess the impact of single and multi-exon duplications and apply PVS1 at the appropriate strength.
- **Strong** ✅：*   For frameshift variants at the 3’ end of IDUA that are not predicted to undergo NMD i.e. PTC downstream of c.1778, consider the length of abnormal amino acid sequence that is added due to the frameshift. If >10% of the length of the normal sequence is altered, PVS1 can be applied at strong.
*   For all variants involving either the +1 or +2 position of GT donor splice sites, the exon immediately 5’ of the variant is predicted to be skipped, and for all variants involving either the -1 or -2 position of AG acceptor splice sites, the exon immediately 3’ of the variant is predicted to be skipped, unless indicated otherwise by RT-PCR or in silico prediction. For the predicted in frame/out of frame consequences for skipping any exon in IDUA, and recommended weight for PVS1, see Appendix 1.
*   Follow the recommendations of Walker et al (PMID: 37352859) for all variants occurring in splice motifs (the donor site motif = last 3 nucleotides of an exon and first 6 nucleotides of an intron; acceptor site motif = first nucleotide of an exon and 20 nucleotides upstream from the exon boundary).
*   If a deletion results in an in-frame consequence, the deletion must encompass one or more exons for PVS1 to apply. Consult Appendix 1 and use professional judgment regarding the strength of evidence to apply.
*   For duplications, consult the PVS1 decision tree and Appendix 1 to assess the impact of single and multi-exon duplications and apply PVS1 at the appropriate strength.
- **Moderate** ✅：*   Any nonsense or frameshift variant that is predicted to be undetected by nonsense-mediated decay (NMD) i.e. if the resulting premature termination codon is in the last exon (exon 14) or in the last 50 nucleotides of the penultimate exon (exon 13; after c.1778, codon 592). In this case, PVS1\_Moderate will be applied because \<10% of the primary amino acid sequence is predicted to be lost ( ~9.3%).
*   For frameshift variants at the 3’ end of IDUA that are not predicted to undergo NMD i.e. PTC downstream of c.1778, consider the length of abnormal amino acid sequence that is added due to the frameshift. If \<10% of the length of the normal sequence is altered, PVS1 can be applied at moderate.
*   For all variants involving either the +1 or +2 position of GT donor splice sites, the exon immediately 5’ of the variant is predicted to be skipped, and for all variants involving either the -1 or -2 position of AG acceptor splice sites, the exon immediately 3’ of the variant is predicted to be skipped, unless indicated otherwise by RT-PCR or in silico prediction. For the predicted in frame/out of frame consequences for skipping any exon in IDUA, and recommended weight for PVS1, see Appendix 1.
*   Follow the recommendations of Walker et al (PMID: 37352859) for all variants occurring in splice motifs (the donor site motif = last 3 nucleotides of an exon and first 6 nucleotides of an intron; acceptor site motif = first nucleotide of an exon and 20 nucleotides upstream from the exon boundary).
*   If a deletion results in an in-frame consequence, the deletion must encompass one or more exons for PVS1 to apply. Consult Appendix 1 and use professional judgment regarding the strength of evidence to apply.
*   For duplications, see the PVS1 decision tree and Appendix 1 to assess the impact of single and multi-exon duplications and apply PVS1 at the appropriate strength.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.Splice region variants following Table 3 in Walker et al (PMID: 37352859).
- **Moderate** ✅：Same amino acid change as a previously established likely pathogenic variant regardless of nucleotide change. Splice region variants following Table 3 in Walker et al (PMID: 37352859).
- **Supporting** ✅：Splice region variants following Table 3 in Walker et al (PMID: 37352859).

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
VCEP说明：De novo variants are rarely reported in IDUA. The occurrence of de novo variants in IDUA is not a mechanism of disease for MPS 1, and the observation that a variant in IDUA has arisen de novo does not support its causality. Any de novo variants will be assessed based on the variant type, functional evidence, and in trans data as described in these guidelines.
- **Strong** ✅：Variant occurs de novo in an affected individual, and the biological relationship of the parent without the variant is confirmed e.g. if the father is not heterozygous for an IDUA variant that has been detected in the patient, paternity must be confirmed.
- **Moderate** ✅：Variant occurs de novo in an affected individual, and the biological relationship of the parent without the variant is not confirmed.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Moderate** ✅：When PS3\_Supporting is met for enzyme activity AND there is expression data (Western blot, pulse chase) showing a clear difference in synthesis and/or processing of alpha-iduronidase, PS3 will be applied at moderate (e.g. Matte et al, 2003, PMID:  12559846; see Appendix 3).
- **Supporting** ✅：_In vitro_ expression studies: After assessment of the parameters listed below, results from such studies can be used at PS3\_Supporting (see Appendix 3 for thresholds for specific studies; \<2% activity (Beesley et al, 2001, PMID: 11735025; Yogalingam et al, 2004, PMID: 15300847; Matte et al, 2003); \<1% activity / enzyme abundance (Yu et al, 2020. PMID: 33198351).

*   Were clones sequenced to verify that the variant is present and that no artifacts have been introduced during the site-directed mutagenesis process? 
*   Were appropriate controls included? Examples 
    *   Negative controls: Empty vector, antisense (at least one appropriate negative control is required); 
    *   Positive control: Wild type IDUA, normal cells (at least one appropriate positive control is required)
*   Was the experiment replicated?
*   If cells have intrinsic IDUA activity e.g., COS cells, the level of activity should be stated so that this can be taken into account.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Studies on functional domains (Bie et al, 2013, PMID: 24036510; Maita et al, 2013, PMID: 23959878; Saito et al, 2014, PMID: 24480078; Figueiredo et al, 2014, PMID: 25459762) have shown that the following residues are important to the function of IDUA:

Active site nucleophiles: Glu182 and Glu299

Active site pocket and substrate binding: Arg89, His91, Asn181, His262, Lys264, Asp301, Gly305, Trp306, Asp349, Arg363, Asn372.

PM1 will be applied to any missense substitutions or inframe deletions of the above residues.

There are no benign or likely benign missense or infame deletions of these residues in ClinVar, or common missense or inframe deletions of these residues in gnomAD v4.1.0 (ClinVar and gnomAD v4.1.0 data accessed on October 30, 2024).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：This criterion will be applied at the supporting level based on guidance from the ClinGen Sequence Variant Interpretation Working Group.

Minor allele frequency <0.025% (0.00025) in any continental population with >2000 alleles in the most recent version of gnomAD (version # will be stated in the written summary).

Variants may be observed in the homozygous state because MPS1 can present in adulthood, and some variants may be hypomorphic. However, the presence and number of homozygotes should be noted.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Detected in trans with a pathogenic variant. Points system based on [guidance](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf) from the ClinGen Sequence Variant Interpretation Working Group. See Appendix 4 for the Lysosomal Diseases VCEP's specification of PM3. Note that points will NOT be applied for any variants of uncertain significance confirmed in trans, due to the high number of pseudodeficiency variants in IDUA. 

These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
- **Strong** ✅：Detected in trans with a pathogenic variant. Points system based on [guidance](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf) from the ClinGen Sequence Variant Interpretation Working Group. See Appendix 4 for the Lysosomal Diseases VCEP's specification of PM3. Note that points will NOT be applied for any variants of uncertain significance confirmed in trans, due to the high number of pseudodeficiency variants in IDUA. 

These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
- **Moderate** ✅：Detected in trans with a pathogenic variant. Points system based on [guidance](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf) from the ClinGen Sequence Variant Interpretation Working Group. See Appendix 4 for the Lysosomal Diseases VCEP's specification of PM3. Note that points will NOT be applied for any variants of uncertain significance confirmed in trans, due to the high number of pseudodeficiency variants in IDUA. 

These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
- **Supporting** ✅：Detected in trans with a pathogenic variant. Points system based on [guidance](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf) from the ClinGen Sequence Variant Interpretation Working Group. See Appendix 4 for the Lysosomal Diseases VCEP's specification of PM3. Note that points will NOT be applied for any variants of uncertain significance confirmed in trans, due to the high number of pseudodeficiency variants in IDUA. 

These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Stop loss variants, and in frame deletion/insertions of two or more amino acids but less than one exon.
- **Supporting** ✅：In frame deletion/insertion of one amino acid.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Stop loss variant if another stop loss variant has been determined to be pathogenic.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be likely pathogenic has been seen before.

Stop loss variant if another stop loss variant has been determined to be likely pathogenic.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
VCEP说明：The combination of strengths for PP1 and PP4 MUST NOT exceed strong (2 x moderate, i.e. 4 points using Bayesian system) if cases are also being counted as probands under PM3.

Counting segregations:

*   Do not count probands as a segregation.
*   Affected segregations = # affected individuals in the family with the variants minus 1.
*   Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele.
*   Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants (or one variant in homozygosity) identified in the proband. These individuals should be either homozygous normal or heterozygous for only one variant.
*   Unaffected, carrier parents DO NOT count as unaffected segregations.

Sibships large enough to meet this criterion are extremely rare. In addition, because IDUA is the only gene involved in MPS 1, all patients are expected to be bi-allelic, regardless of whether the pathogenic variants can be, or have been, detected. A variant under assessment may not be the true pathogenic variant but instead in linkage disequilibrium with an unidentified pathogenic variant. For this reason, this criterion does not facilitate assessment of pathogenicity.
- **Moderate** ✅：See Appendix 5 for points system and guidance (based on PMID: 38103548).
- **Supporting** ✅：See Appendix 5 for points system and guidance (based on PMID: 38103548).

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Any missense changes with a REVEL score >0.773 will meet PP3_Moderate (Based on Pejaver et al, PMID: 3641399; Note that the VCEP has chosen not to apply PP3 at strong).
- **Supporting** ✅：*   Any missense changes with a REVEL score between 0.644 - 0.773 will meet PP3 (Pejaver et al., PMID: 3641399)
*   For in frame insertions and deletions, use Mutation Taster ([http://www.mutationtaster.org/](http://www.mutationtaster.org/) ; count if “disease-causing”), and MutPred-Indel ([https://mutpred2.mutdb.org/mutpredindel/](https://mutpred2.mutdb.org/mutpredindel/) ; score >0.5 for “pathogenic”). Apply PP3 if both predictors indicate that the variant is deleterious.
*   For non-canonical splice site variants (e.g., +3, -3), use SpliceAI ([https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) ). A score of >0.2 is taken to indicate disruption of the splice site allowing PP3 to be applied (based on Walker et al, PMID: 37352859). Evidence for use of a cryptic splice site and the impact on the gene product should also be assessed. PP3 for splicing variants will be applied only in the absence of functional (RNA analysis) data.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：3 or more of the following criteria are met:

*   Deficient IDUA activity, within the affected range (usually non-detectable or stated to be in the affected range by lab) in fibroblasts, leukocytes, or plasma.
    *   Do not count if one or more pseudodeficiency variants are reported to be present, or if the result was obtained on newborn screen without confirmatory enzyme testing.
*   Enzyme replacement therapy results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).
*   Elevated urinary and/or blood GAGs expressed as either total GAGs, specific GAG (heparan sulfate, dermatan sulfate, or endogenous biomarker) stated to be consistent with MPS I. 
*   An individual with clinical features specific to MPS I; At minimum at least 2 of the following: dysostosis multiplex, hepatosplenomegaly, arthropathy, corneal involvement, valvular thickening; AND/OR case reported within the context of a larger clinically-diagnosed MPS I cohort, when published by groups with demonstrated experience (as determined at the discretion of the VCEP) in lysosomal disorders and the clinical care of affected individuals. When detailed clinical information is limited, confidence in the phenotypic classification is strengthened when the report originates from groups with established familiarity in the diagnosis and longitudinal management of MPS I.
*   Bone marrow transplant results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).
- **Supporting** ✅：2 of the following criteria are met:

*   Deficient IDUA activity, within the affected range (usually non-detectable or stated to be in the affected range by lab) in fibroblasts, leukocytes, or plasma.
    *   Do not count if one or more pseudodeficiency variants are reported to be present, or if the result was obtained on newborn screen without confirmatory enzyme testing.
*   Enzyme replacement therapy results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).
*   Elevated urinary and/or blood GAGs expressed as either total GAGs, specific GAG (heparan sulfate, dermatan sulfate, or endogenous biomarker) stated to be consistent with MPS I.
*   An individual with clinical features specific to MPS I; At minimum at least 2 of the following: dysostosis multiplex, hepatosplenomegaly, arthropathy, corneal involvement, valvular thickening; AND/OR case reported within the context of a larger clinically-diagnosed MPS I cohort, when published by groups with demonstrated experience (as determined at the discretion of the VCEP) in lysosomal disorders and the clinical care of affected individuals. When detailed clinical information is limited, confidence in the phenotypic classification is strengthened when the report originates from groups with established familiarity in the diagnosis and longitudinal management of MPS I.
*   Bone marrow transplant results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Any variant with Grpmax >0.005 in the most recent version of gnomAD (95% confidence interval, lower bound) (version # will be stated in the written summary)

BA1 minor allele frequency cut-off calculated using [http://cardiodb.org/allelefrequencyapp](http://cardiodb.org/allelefrequencyapp) with prevalence = 1 in 40,000 (PMID: 33208168), genetic heterogeneity = 1.0 (IDUA is the only gene known to cause MPS1), allelic heterogeneity = 1.0, and penetrance = 1.0.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Any variant with Grpmax >0.0025 in the most recent version of gnomAD (95% confidence interval, lower bound) (version # will be stated in the written summary).

BS1 minor allele frequency cut-off calculated using [http://cardiodb.org/allelefrequencyapp](http://cardiodb.org/allelefrequencyapp) with prevalence = 1 in 40,000 (PMID: 33208168), genetic heterogeneity = 1.0 (IDUA is the only gene known to cause MPS1), allelic heterogeneity = ~0.5 (frequency of the most common known pathogenic variants in patients with MPS1 (PMID: 28595941, 29393969), and penetrance = 1.0.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：BS2 can be applied if there is clear documentation that an individual of any age is either homozygous for the variant, or has the variant confirmed in trans with a pathogenic or likely pathogenic variant and has IDUA activity in the unaffected range as documented by standard diagnostic laboratory-based activity determination. Values for IDUA activity and the reference range for the laboratory must be provided.

Note: Patients with late onset MPS1 can present late in life (5th-6th decade), can have mild symptoms, and may remain undiagnosed. Therefore, it is possible that individuals who are homozygous for hypomorphic IDUA variants could be present in population databases.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：The same assays outlined for PS3 will be used for BS3. Please see PS3 guidance for additional information on these assays. 

BS3\_Supporting can be applied for expression of IDUA sequence variants in cultured cells and subsequent measurement of enzyme activity provided that there is no other evidence to suggest that the variant could be disease-causing e.g. mislocalization (see Appendix 3 for thresholds for specific studies: >10% activity (Beesley et al, 2001, PMID: 11735025; Yogalingam et al, 2004, PMID: 15300847; Matte et al, 2003); >~10% activity / enzyme abundance (Yu et al, 2020. PMID: 33198351).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Non-segregation with disease in a family i.e. variant is absent in an affected individual.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   Missense changes with a REVEL score \< 0.290 (threshold based on Pejaver et al; however, BP4 will only be applied at the supporting level). 
*   For in frame insertions and deletions, use PROVEAN ([http://provean.jcvi.org/seq_submit.php](http://provean.jcvi.org/seq_submit.php) ; score >-2.5), Mutation Taster ([http://www.mutationtaster.org/](http://www.mutationtaster.org/) ; count if “polymorphism”, and MutPred-Indel ([http://mutpredindel.cs.indiana.edu/](http://mutpredindel.cs.indiana.edu/) ; score \<0.5. Apply BP4 if all predictors indicate that the variant is benign.
*   For non-canonical splice site variants, use SpliceAI ([https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) ) to assess the impact of variants that are not +/-1 or 2 canonical splice site variants. This criterion can be applied as PP3 (Splicing) for SpliceAI scores ≤0.1 (based on Walker et al, PMID: 37352859). 
*   If there is any evidence for possible creation of a cryptic splice site, this criterion should not be applied.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Experimental evidence (RT-PCR, RNA Seq, minigene) shows that the variant does not impact splicing. BP7_Strong (RNA) will be used only under strict circumstances in which it is clear that the allele with the variant is expressed at the normal level to avoid counting a "normal" result because the allele with the variant is absent due to nonsense-mediated decay (Walker et al, PMID: 37352859).
- **Supporting** ✅：BP7 can be applied if the variant is synonymous, unless the variant is in the first nucleotide or last three nucleotides of an exon, AND BP4 is met i.e. SpliceAI predicts no impact on splicing (score ≤ 0.10)

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
PS4、PM6、PP2、PP5、BP1、BP2、BP3、BP5、BP6
### 参考附件
- [Appendix 2_PVS1_Decision Tree_IDUA](https://cspec.genome.network/cspec/File/id/754fd9f3-8bc1-4fcd-bbc3-3fa9f95d79ae/data)
- [Appendix 5_PP1 guidance_IDUA](https://cspec.genome.network/cspec/File/id/a1157d4c-8d11-4c79-b6e7-2d4d57baf3b1/data)
- [Appendix 4_PM3 points system_IDUA](https://cspec.genome.network/cspec/File/id/91a4e003-be72-4c68-aa3a-884bb9a7cea2/data)
- [Appendix 3_Functional assays](https://cspec.genome.network/cspec/File/id/8f37e095-cc71-4089-adc3-db41b18d29ea/data)
- [Appendix 1_PVS1 strength_IDUA](https://cspec.genome.network/cspec/File/id/2290f052-7dc3-4563-a40f-e6a7d75e6b7b/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN091)

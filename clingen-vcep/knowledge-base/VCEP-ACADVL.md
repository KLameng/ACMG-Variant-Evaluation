# ClinGen VCEP基因特异性规范：ACADVL

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN021 — ACADVL Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0008723**（遗传方式：Autosomal recessive inheritance）

### 通用说明
> 官网版本：Version 2.2（Released 7/20/2026；DOI 10.5281/zenodo.21457671）。
> Release Notes：
> - v2.0：VCEP 复核所有证据码并更新措辞。
> - v2.0.1：VCEP 更新 PP3 与 BP4 措辞，仅保留对 SpliceAI 工具的引用。
> - 6/11/26：VCEP 新增规则 PVS1 + PM2(Supporting) = Likely Pathogenic。
> - 7/14/26：VCEP 重新加入 PVS1 + PM2(Supporting) = LP；该新增规则未改变任何试点分类。

Version 2.0
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Loss of function is a known mechanism for VLCAD Deficiency. The specifications below are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., (2018) PMID: 30192042). There are multiple transcripts for ACADVL. The major isoform, NM\_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., (1995) PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM\_000018.4 was designated as the most relevant transcript. Nonsense or Frameshift:

*   Use caution when interpreting LOF variants at the 3’ end of the gene.
*   NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19). 
*   Canonical Splice Site (+1, +2, -1, -2): All donor/acceptor sites follow the GT/AG rule, except for the donor splice site of intron 8, which begins with GC. PVS1 should not be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood. For +1 or +2 GT donor splice site variants, the exon immediately 5’ of the variant is predicted to be skipped. For -1 or -2 AG acceptor splice site variants, the exon immediately 3’ of the variants is predicted to be skipped.
*   Initiation codon: The next in-frame methionine is at position 6 (on transcript NM\_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein (Aoyama et al., (1995) PMID: 7668252). Therefore, initiator codon variants will meet PVS1\_Strong.
*   Well-established \_in vitro\_ or \_in vivo\_ functional studies supportive of a damaging effect \_as measured by effect on mRNA transcript profile (mRNA assay only).\_ Apply as PVS1 (RNA) at appropriate strength. 
*   See ACADVL PVS1 decision tree; cannot be combined with PM1
- **Strong** 📋：Loss of function is a known mechanism for VLCAD Deficiency. The specifications below are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., (2018) PMID: 30192042). There are multiple transcripts for ACADVL. The major isoform, NM\_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., (1995) PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM\_000018.4 was designated as the most relevant transcript. Nonsense or Frameshift:

*   Use caution when interpreting LOF variants at the 3’ end of the gene.
*   NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19). 
*   Canonical Splice Site (+1, +2, -1, -2): All donor/acceptor sites follow the GT/AG rule, except for the donor splice site of intron 8, which begins with GC. PVS1 should not be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood. For +1 or +2 GT donor splice site variants, the exon immediately 5’ of the variant is predicted to be skipped. For -1 or -2 AG acceptor splice site variants, the exon immediately 3’ of the variants is predicted to be skipped.
*   Initiation codon: The next in-frame methionine is at position 6 (on transcript NM\_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein (Aoyama et al., (1995) PMID: 7668252). Therefore, initiator codon variants will meet PVS1\_Strong.
*   Well-established \_in vitro\_ or \_in vivo\_ functional studies supportive of a damaging effect \_as measured by effect on mRNA transcript profile (mRNA assay only).\_ Apply as PVS1 (RNA) at appropriate strength. 
*   See ACADVL PVS1 decision tree; cannot be combined with PM1
- **Moderate** 📋：Loss of function is a known mechanism for VLCAD Deficiency. The specifications below are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., (2018) PMID: 30192042). There are multiple transcripts for ACADVL. The major isoform, NM\_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., (1995) PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM\_000018.4 was designated as the most relevant transcript. Nonsense or Frameshift:

*   Use caution when interpreting LOF variants at the 3’ end of the gene.
*   NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19). 
*   Canonical Splice Site (+1, +2, -1, -2): All donor/acceptor sites follow the GT/AG rule, except for the donor splice site of intron 8, which begins with GC. PVS1 should not be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood. For +1 or +2 GT donor splice site variants, the exon immediately 5’ of the variant is predicted to be skipped. For -1 or -2 AG acceptor splice site variants, the exon immediately 3’ of the variants is predicted to be skipped.
*   Initiation codon: The next in-frame methionine is at position 6 (on transcript NM\_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein (Aoyama et al., (1995) PMID: 7668252). Therefore, initiator codon variants will meet PVS1\_Strong.
*   Well-established \_in vitro\_ or \_in vivo\_ functional studies supportive of a damaging effect \_as measured by effect on mRNA transcript profile (mRNA assay only).\_ Apply as PVS1 (RNA) at appropriate strength. 
*   See ACADVL PVS1 decision tree; cannot be combined with PM1
- **Supporting** 📋：Loss of function is a known mechanism for VLCAD Deficiency. The specifications below are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., (2018) PMID: 30192042). There are multiple transcripts for ACADVL. The major isoform, NM\_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., (1995) PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM\_000018.4 was designated as the most relevant transcript. Nonsense or Frameshift:

*   Use caution when interpreting LOF variants at the 3’ end of the gene.
*   NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19). 
*   Canonical Splice Site (+1, +2, -1, -2): All donor/acceptor sites follow the GT/AG rule, except for the donor splice site of intron 8, which begins with GC. PVS1 should not be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood. For +1 or +2 GT donor splice site variants, the exon immediately 5’ of the variant is predicted to be skipped. For -1 or -2 AG acceptor splice site variants, the exon immediately 3’ of the variants is predicted to be skipped.
*   Initiation codon: The next in-frame methionine is at position 6 (on transcript NM\_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein (Aoyama et al., (1995) PMID: 7668252). Therefore, initiator codon variants will meet PVS1\_Strong.
*   Well-established \_in vitro\_ or \_in vivo\_ functional studies supportive of a damaging effect \_as measured by effect on mRNA transcript profile (mRNA assay only).\_ Apply as PVS1 (RNA) at appropriate strength. 
*   See ACADVL PVS1 decision tree; cannot be combined with PM1

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：*   Same amino acid change as a previously established pathogenic variant classified using the ACADVL specifications without application of PS1, regardless of nucleotide change OR Same amino acid change as ≥2 previously established likely pathogenic variants classified using the ACADVL specifications without application of PS1, regardless of nucleotide change.  
    *   Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change.
*   Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al., (2023) PMID: 37352859).
    *   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker, et al., (2023) PMID: 37352859.
- **Moderate** 📋：*   PS1\_Moderate: Same amino acid change as a previously established likely pathogenic variant classified using the ACADVL specifications without application of PS1, regardless of nucleotide change. 
    *   Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change.
*   Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al., (2023) PMID: 37352859).
    *   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker et al., (2023) PMID: 37352859.
- **Supporting** 📋：*   Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al.,  (2023) PMID: 37352859).
    *   PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker et al., (2023) PMID: 37352859.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Very Strong** 📋：*   Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. Apply patient-derived evidence in PP4.
*   Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
*   Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart). OddsPath analysis sufficient for very strong application.
- **Strong** 📋：*   Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. Apply patient-derived evidence in PP4.
*   Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
*   Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
- **Moderate** 📋：*   Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. Apply patient-derived evidence in PP4.
*   Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
*   Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
- **Supporting** 📋：*   Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. Apply patient-derived evidence in PP4.
*   Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
*   Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart). If an enzyme activity assay has >20% activity it cannot be weighted above PS3\_supporting regardless of flowchart results.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** 📋：*   See table PM1, curators may seek approval from the expert panel for identifying additional hotspots or critical regions as discovered in literature searches for inclusion. 
    *   Moderate
        *   p.1-40,mitochondrial signal peptide, PMIDs:  18227065\*, 20060901 
        *   p.214-223, nucleotide/substrate binding, PMIDs: 18227065\*, 20060901 
        *   p.249-251, nucleotide/substrate binding, PMIDs: 18227065\*, 20060901 
        *   p.R326, CpG dinucleotide, PMID: 9973285 
        *   p.381-382, FAD binding and salt-bridge interaction, PMID: 20060901 
        *   p.R429, CpG dinucleotide, PMID: 9973285 
        *   p.E441, Adjacent to FAD binding, on dimer formation loop, PMIDs: 20060901 
        *   p.R459, dimerization, PMID: 14517516 
        *   p.481-516, membrane binding, PMIDs: 18227065\*, 20060901 
        *   p.562, nucleotide/substrate binding, PMIDs: 18227065\*, 20060901 
        *   \*protein is described in mature protein nomenclature without signal peptide; add 40 amino acids to reach HGVS nomenclature

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Variants with a highest population minor allele frequency (MAF) \<0.001 (0.1%) in any continental population with >2000 alleles in gnomAD will meet PM2\_supporting.

*    Calculated using the Prevalence of 1:100,000, Allelic Contribution of 0.2, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCADD that may develop in adulthood. This was multiplied by 1.5 to account for mildly pathogenic variants being present in carriers within the population databases.
*   It is acceptable for an ACADVL variant to be present in controls because VLCAD deficiency is a recessive condition. It is also possible for homozygous ACADVL variants to be present in population databases due to later onset of the condition. If homozygous variants are present, the number should be noted and discussed with an expert.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：*   Details of the cDNA change must be used to describe any variants used as evidence for PM3. If the variant is described only as an amino acid change, this is not sufficient. Probands must also meet PP4 criteria to be counted.
*   If more than one case has the same genotype and the variants are not confirmed in trans, then only one case should be used for assigning points to avoid overcounting evidence if the variants are actually in cis and hence inherited together in multiple individuals or potentially counting the same case twice. If the variants are confirmed to be in trans, more than one individual with the same genotype can be counted as long as the reports do not represent the same case.
*   These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
*   For a variant to be “confirmed in trans” in a compound heterozygous patient, parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown. Parental testing is not required for homozygous cases.
*   See PM3 table
    *   PM3 score ≥ 4.0
- **Strong** 📋：*   Details of the cDNA change must be used to describe any variants used as evidence for PM3. If the variant is described only as an amino acid change, this is not sufficient. Probands must also meet PP4 criteria to be counted.
*   If more than one case has the same genotype and the variants are not confirmed in trans, then only one case should be used for assigning points to avoid overcounting evidence if the variants are actually in cis and hence inherited together in multiple individuals or potentially counting the same case twice. If the variants are confirmed to be in trans, more than one individual with the same genotype can be counted as long as the reports do not represent the same case.
*   These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
*   For a variant to be “confirmed in trans” in a compound heterozygous patient, parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown. Parental testing is not required for homozygous cases.
*   See PM3 table
    *   PM3 score ≥ 2.0 \< 4.0
- **Moderate** 📋：*   Details of the cDNA change must be used to describe any variants used as evidence for PM3. If the variant is described only as an amino acid change, this is not sufficient. Probands must also meet PP4 criteria to be counted.
*   If more than one case has the same genotype and the variants are not confirmed in trans, then only one case should be used for assigning points to avoid overcounting evidence if the variants are actually in cis and hence inherited together in multiple individuals or potentially counting the same case twice. If the variants are confirmed to be in trans, more than one individual with the same genotype can be counted as long as the reports do not represent the same case.
*   These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
*   For a variant to be “confirmed in trans” in a compound heterozygous patient, parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown. Parental testing is not required for homozygous cases.
*   See PM3 table 
    *   PM3 score ≥ 1.0 \< 2.0
- **Supporting** 📋：*   Details of the cDNA change must be used to describe any variants used as evidence for PM3. If the variant is described only as an amino acid change, this is not sufficient. Probands must also meet PP4 criteria to be counted.
*   If more than one case has the same genotype and the variants are not confirmed in trans, then only one case should be used for assigning points to avoid overcounting evidence if the variants are actually in cis and hence inherited together in multiple individuals or potentially counting the same case twice. If the variants are confirmed to be in trans, more than one individual with the same genotype can be counted as long as the reports do not represent the same case.
*   These variant interpretation guidelines should be used to determine the classification of the “other variant” in order to determine the appropriate number of points to assign.
*   For a variant to be “confirmed in trans” in a compound heterozygous patient, parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown. Parental testing is not required for homozygous cases.
*   See PM3 table 
    *   PM3 score ≥ 0.5 \< 1.0

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：*   See PM5 table. Note: Cannot be applied with PM1, apply criteria with the highest strength. If both are applicable at the same strength, apply PM5 as it is amino acid specific.
- **Moderate** 📋：*   See PM5 table. Note: Cannot be applied with PM1, apply criteria with the highest strength. If both are applicable at the same strength, apply PM5 as it is amino acid specific. 
    *   Two likely pathogenic variants at the same codon
    *   One pathogenic variant at the same codon
- **Supporting** 📋：*   See PM5 table. Note: Cannot be applied with PM1, apply criteria with the highest strength. If both are applicable at the same strength, apply PM5 as it is amino acid specific.   
    *   One likely pathogenic variant at the same codon

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** 📋：Assumed de novo, but without confirmation of paternity and maternity.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：*   See PP1 table. Probands are NOT counted toward segregation. Likewise, carrier parents DO NOT count as unaffected segregations. Affected segregations = # affected individuals in the family with the variants - 1. Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.
    *    Strong (32:1 Likelihood)
        *   A LOD score ≥ 1.50
- **Moderate** 📋：*   See PP1 table. Probands are NOT counted toward segregation. Likewise, carrier parents DO NOT count as unaffected segregations. Affected segregations = # affected individuals in the family with the variants - 1. Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.
    *     Moderate (16:1 Likelihood)
        *   A LOD score  \< 1.50 ≥ 1.20
- **Supporting** 📋：*   See PP1 table. Probands are NOT counted toward segregation. Likewise, carrier parents DO NOT count as unaffected segregations. Affected segregations = # affected individuals in the family with the variants - 1. Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.
    *   Supporting (4:1 Likelihood)
        *   An LOD score  \< 1.20 ≥ 0.60

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense changes with a REVEL scores >0.75 will meet PP3
*   For in-frame deletions and insertions, use Mutation Taster.
*   For non-canonical splice site variants, use Splice AI. Based on data from Jaganathan et al., (2019) PMID: 30661751, Houdayer et al., (2012) PMID: 22505045 and Tang et al., (2016) PMID: 27313609 and Walker et al., (2023) PMID:37352859, PP3 can be applied if there is, a SpliceAI “high score” (Δ Score ≥ 0.5 “confidently predicted splice variants”) (exclude any results with Δ Score ≤ 0.2 from consideration of pathogenicity, \<0.2 are not “predicted to alter splicing”).
*   For SpliceAI’s cryptic splice-site rules, the creation of a new splice-site with Δ Score ≥ 0.5 may be enough to produce a large proportion of aberrant transcripts.
*   If a new splice site is predicted to be generated, this rule can be applied if the newly generated splice site is significantly stronger than the wild type site (Δ Score ≥ 0.5 using SpliceAI).
*   Do not apply this rule for canonical splice site changes meeting PVS1.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** 📋：*   Abnormal tests that are consistent with VLCAD deficiency include deficient VLCAD enzyme activity in patient cells (leukocytes, fibroblasts, liver, heart, or skeletal muscle, or amniocytes), abnormal C14:1 acylcarnitine values from newborn screening (NBS), and abnormal acylcarnitine values from follow-up plasma analysis.
    *   2 points (See PP4 Table)
- **Supporting** 📋：*   Abnormal tests that are consistent with VLCAD deficiency include deficient VLCAD enzyme activity in patient cells (leukocytes, fibroblasts, liver, heart, or skeletal muscle, or amniocytes), abnormal C14:1 acylcarnitine values from newborn screening (NBS), and abnormal acylcarnitine values from follow-up plasma analysis.
    *   1 point (See PP4 Table)

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：*   Variants with a highest population minor allele frequency (MAF) ≥0.007 (0.7%) in any continental population with >2000 alleles in gnomAD will meet BA1.
    *   Calculated using the Prevalence of 1:30,000, Allelic Contribution of 1, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCADD that may develop in adulthood.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：*   Variants with a highest population minor allele frequency (MAF) ≥0.0035 (0.35%) in any continental population with >2000 alleles in gnomAD will meet BS1.
    *    Calculated using the Prevalence of 1:30,000, Allelic Contribution of 0.5, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCAD that may develop in adulthood.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** 📋：Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
- **Moderate** 📋：Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).
- **Supporting** 📋：Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** 📋：Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense changes with a REVEL score \<0.5 will meet BP4.
*   For in-frame deletions and insertions, use Mutation Taster. 
*   For non-canonical splice site variants, use Splice AI. Based on data from Jaganathan et al., 2019 (PMID: 30661751), Houdayer et al., 2012 (PMID: 22505045), Tang et al., 2016 (PMID: 27313609), and Walker et al., (2023) PMID:37352859, BP4 can be applied if there is a Δ Score ≤ 0.1.
*   Do not apply this rule if there is evidence for creation of a cryptic splice site.
*   Can be used with BP7 code.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：BP7\_Strong (RNA) in vitro evidence of no splicing impact for intronic or synonymous variants irrespective of position and predicted impact on splicing.
- **Supporting** 📋：*   A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved
*   Can be used for intronic variants that fall outside the minimal splice region (≥+7 or ≤-21)
*   Can be used with BP4 code.

### 组合规则（Rules for Combining Criteria，Richards 型）

**致病（Pathogenic）**
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**可能致病（Likely Pathogenic）**
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate
- **1 Very Strong (PVS1) AND 1 Supporting (PM2_Supporting)**（v2.2 新增）

**良性（Benign）**
- ≥ 2 Strong
- 1 Stand Alone

**可能良性（Likely Benign）**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PS2、PS4、PP2、PP5、BS2、BP1、BP3、BP5、BP6
### 参考附件
- [PP1 tables](https://cspec.genome.network/cspec/File/id/0e1561a1-787e-414b-92a2-3b75b87a6948/data)
- [PS3 functional assay](https://cspec.genome.network/cspec/File/id/294a7f39-8b1a-4fec-acfa-b12b33b98f10/data)
- [PM3 table](https://cspec.genome.network/cspec/File/id/3ba1c23e-45ad-46d9-af6e-5c3d47c48e6d/data)
- [PS3 and BS3 flowchart](https://cspec.genome.network/cspec/File/id/8abc9816-95f6-404a-b01b-5e1cd867ebf9/data)
- [PM1 table_updated](https://cspec.genome.network/cspec/File/id/148cdd3e-1d3e-4443-a3cf-7a208d47d23d/data)
- [PM5 table](https://cspec.genome.network/cspec/File/id/f44ec87a-6537-4ef6-8ea3-1eafd2a0247e/data)
- [PVS1 decision tree](https://cspec.genome.network/cspec/File/id/dd645ceb-ed6f-4f34-b02c-978992f7cb02/data)
- [PP4 points table](https://cspec.genome.network/cspec/File/id/16e7b93e-1774-4c63-b75a-f3e2afba481e/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN021)

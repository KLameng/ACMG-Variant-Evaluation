# ClinGen VCEP基因特异性规范：GAMT

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 2.0（Released；DOI 10.5281/zenodo.21421631；Cerebral Creatine Deficiency Syndromes VCEP；核验 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN026 — Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0012999**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：**Nonsense-mediated decay predicted**

**Nonsense and frameshift variants**

*   All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 6) or the last 50 bases of the penultimate exon of the gene (exon 5, c.520). In that case, PVS1\_Strong or PVS1\_Moderate will be applied, depending on whether >10% or \<10% of the protein is lost.

**Splice site variants (+1, +2, -1, -2)**

*   All canonical splice site pairs in GAMT are GT-AG.
*   For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants.
*   For the predicted in frame/out of frame consequences of exon skipping and assigned strength of PVS1, see Appendix 1.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.
*   Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing. Otherwise, the PVS1 strength should be reduced accordingly.
*   Non-canonical splice variants, such as +3 or -3, will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Deletions (single or multi exon)**

*   If a single or multi-exon deletion results in an out of frame consequence, use PVS1 unless not predicted to undergo NMD. 
*   If not predicted to undergo NMD, use PVS1\_Strong if >10% of the protein is predicted to be removed, and use PVS1\_Moderate if \<10% of the protein is predicted to be removed.
*   If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. Use PVS1\_Strong if more than 10% of the protein is removed and PVS1\_Moderate if \<10% of the protein is removed.
*   If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.  
    Appendix 1 can be used to predict the consequences of single exon deletions.

**Duplications**

*   Use the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042) to assess the impact of duplications.
- **Strong** 📋：**Single exon or larger deletion resulting in loss of >10% of the protein.** 

**Nonsense and frameshift variants**

*   All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 6) or the last 50 bases of the penultimate exon of the gene (exon 5, c.520). In that case, PVS1\_Strong will be applied if >10% of the protein is lost.

**Splice site variants (+1, +2, -1, -2)**

*   All canonical splice site pairs in GAMT are GT-AG.
*   For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants.
*   Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing. 
*   For considerations for strength at which PVS1 may be applied see Appendix 1.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.
*   Non-canonical splice variants, such as +3 or -3, will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Deletions (single or multi exon)**

*   If a single or multi-exon deletion results in an out of frame consequence, use PVS1 unless not predicted to undergo NMD.
*    If not predicted to undergo NMD, use PVS1\_Strong if >10% of the protein is predicted to be removed, and use PVS1\_Moderate if \<10% of the protein is predicted to be removed.
*   If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. Use PVS1\_Strong if more than 10% of the protein is removed and PVS1\_Moderate if \<10% of the protein is removed.
*   If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.  
    Appendix 1 can be used to predict the consequences of single exon deletions.

**Duplications**

*   Use the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042) to assess the impact of duplications.
- **Moderate** 📋：**Single exon or larger deletion resulting in loss of \<10% of the protein.**   

**Nonsense and frameshift variants**

*   All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 6) or the last 50 bases of the penultimate exon of the gene (exon 5, c.520). In that case, PVS1\_Moderate will be applied if \<10% of the protein is lost.

**Splice site variants (+1, +2, -1, -2)**

*   All canonical splice site pairs in GAMT are GT-AG.
*   Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing. 
*   For any canonical splice site variant (+1, +2, -1, -2), if RT-PCR data predicts in-frame loss of \<10% of the protein, apply PVS1\_Moderate.
*   If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.
*   Non-canonical splice variants, such as +3 or -3, will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Initiator codon variants**

*   All initiator codon variants will meet PVS1\_Moderate. The next in-frame methionine is at amino acid position 42 (based on NP\_000147.1).

**Deletions (single or multi exon)**

*   If a single or multi-exon deletion results in an out of frame consequence, use PVS1 unless not predicted to undergo NMD. 
*   If not predicted to undergo NMD, use PVS1\_Strong if >10% of the protein is predicted to be removed, and use PVS1\_Moderate if \<10% of the protein is predicted to be removed.
*   If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. Use PVS1\_Strong if more than 10% of the protein is removed and PVS1\_Moderate if \<10% of the protein is removed.
*   If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.  
    Appendix 1 can be used to predict the consequences of single exon deletions.

**Duplications**

*   Use the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042) to assess the impact of duplications.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：*   This criterion is applicable for any variant resulting in the same amino acid change as a variant that has been previously established as pathogenic by the CCDS VCEP, by assessment using these criteria, regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.
*   PS1 may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).
- **Moderate** 📋：*   This criterion is applicable for any variant resulting in the same amino acid change as a variant that has been previously established as likely pathogenic by the CCDS VCEP, by assessment using these criteria, regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.
*   PS1\_Moderate may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).
- **Supporting** 📋：PS1\_Supporting may be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：PS3\_Supporting can be assigned if a variant is expressed in GAMT-deficient fibroblasts, HeLa cells and has \<15% of the control value, for values published in Mercimek-Mahmutoglu et al, 2014, PMID 24415674; Mercimek-Mahmutoglu et al, 2016, PMID 26319512; or DesRoches et al, 2016, PMID 26003046.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：**Allele frequency \<0.0004 (\<0.04%) in all populations in gnomAD.**

It is acceptable for a GAMT variant to be present in controls, if heterozygous, because GAMT-D is a recessive disorder. Homozygotes should not be seen in a population database, such as gnomAD, because the penetrance of this condition in individuals with biallelic pathogenic variants is expected to be 100% and the condition is expected to present with severe symptoms early in life.

GAMT specifications:

*   All subpopulations in gnomAD v4.0 must have a maximum allele frequency less than 0.0004 (the highest population minor allele frequency of the most common pathogenic GAMT variant, c.327G>A, in gnomAD). Any variant with a frequency below this cutoff will meet PM2\_Supporting.
*   If homozygotes are observed, or variant is confirmed in trans with a known pathogenic variant, the variant will meet BS2 (assuming 100% penetrance for an individual with 2 pathogenic variants in trans).

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：*   Follow SVI guidance for PM3 ([https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf)).
*   Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed in order to confirm that the variants are in trans if the patient is compound heterozygous.
- **Strong** 📋：*   Follow SVI guidance for PM3 ([https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf)).
*   Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed in order to confirm that the variants are in trans if the patient is compound heterozygous.
- **Moderate** 📋：*   Follow SVI guidance for PM3 ([https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf)).
*   Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed in order to confirm that the variants are in trans if the patient is compound heterozygous.
- **Supporting** 📋：*   Follow SVI guidance for PM3 ([https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf)).
*   Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed in order to confirm that the variants are in trans if the patient is compound heterozygous.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：GAMT specifications: Use this rule “as is” for stop loss variant, and in frame deletions and insertions of 2 or more amino acids, but downgrade to PM4\_Supporting for single amino acid deletions and insertions.
- **Supporting** 📋：Downgrade to PM4\_Supporting for single amino acid deletions and insertions.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：*   This criterion is applicable for any variant resulting in a different amino acid change, at the same amino acid position, as a variant that has been previously established as pathogenic by the CCDS VCEP, by assessment using these criteria, regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing. 
*   If the variant is likely pathogenic, use PM5\_Supporting.
- **Supporting** 📋：*   This criterion is applicable for any variant resulting in a different amino acid change, at the same amino acid position, as a variant that has been previously established as likely pathogenic by the CCDS VCEP, by assessment using these criteria, regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.  
*   If the variant is likely pathogenic, use PM5.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** 📋：Missense variant with a REVEL score equal to or >0.932 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
- **Moderate** 📋：Missense variant with a REVEL score 0.773-0.932 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
- **Supporting** 📋：*   Missense variant with a REVEL score 0.644-0.773 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
*   In frame deletion or insertion predicted deleterious by PROVEAN and MutationTaster. Results must be consistent to count.
*   For non-canonical splice site variants (e.g., +3, -3), predict the impact on splicing by using SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) , and apply PP3 for a score equal to or >0.2 (as indicated in PMID: 37352859, Table 1 and Figure 4). Assess the possibility of activation of cryptic splice sites.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** 📋：4 points based on any combination of the following. Two or more data types are required to apply PP4\_Strong:

*   Elevated urine guanidinoacetate with or without low or low normal creatine (1 point).
*   Elevated plasma guanidinoacetate with or without low or low normal creatine (2 points).
*   Significantly decreased creatine peak in brain magnetic resonance spectroscopy with or without visible guanidinoacetate peak (3 points).
*   GAMT enzyme activity \<5% of normal (3 points).
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength.
*   For PP4 to be applied at strong, full GAMT gene sequencing, including all coding exons and intron/exon boundaries, must have been carried out. If not, consider downgrading.
- **Moderate** 📋：3 points based on any combination of the following. Two or more data types are recommended to apply PP4\_Moderate:

*   Elevated urine guanidinoacetate with or without low or low normal creatine (1 point).
*   Elevated plasma guanidinoacetate with or without low or low normal creatine (2 points).
*   Significantly decreased creatine peak in brain magnetic resonance spectroscopy with or without visible guanidinoacetate peak (3 points).
*   GAMT enzyme activity \<5% of normal (3 points).
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength.
- **Supporting** 📋：1-2 points based on: 

*   Elevated urine guanidinoacetate with or without low or low normal creatine (1 point).
*   Elevated plasma guanidinoacetate with or without low or low normal creatine (2 points).
*   Variant must meet PM2\_Supporting for PP4 to apply at any strength.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：*   Allele frequency >0.003 (0.3%) in gnomAD v4.0 in any continental population with >2000 alleles (based on the estimated prevalence 1 in 114,000, PMID 24071436) in gnomAD v4.0 (max allelic contribution = 100%; max genetic contribution = 100%).
*   Use the highest population minor allele frequency (MAF) in any given continental population with >2,000 alleles (European non-Finnish, African, East Asian, South Asian, Latino) (PMID 30311383).

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：*   Allele frequency >0.001 (0.1%) in gnomAD v4.0 in any continental population with >2000 alleles (based on the estimated prevalence 1 in 114,000 (PMID: 24071436) in gnomAD v4.0 (max allelic contribution = 40%; max genetic contribution = 100%).
*   Use the highest population minor allele frequency (MAF) in any given continental population with >2,000 alleles (European non-Finnish, African, East Asian, South Asian, Latino) (PMID 30311383).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Observed in the homozygous state in a healthy adult, or confirmed in trans with a variant that has been classified as pathogenic by the CCDS VCEP using these criteria.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：In vitro assays in which a variant is expressed in GAMT-deficient cultured cells (e.g. GAMT-deficient fibroblasts) or in-fusion High-Fidelity cloning of GAMT transcript and site directed mutagenesis to generate missense variant overexpressed in HeLa cells and measurement of GAMT activity in cells for wild-type and missense variant. Any variant with enzyme activity at or above 30% of normal in the following publications meets BS3\_Supporting (Mercimek-Mahmutoglu et al, 2014; PMID 24415674; Mercimek-Mahmutoglu et al, 2016, PMID 26319512; DesRoches et al, 2016, PMID 26003046).

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in cis with a pathogenic variant (to take AR inheritance into account).

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   REVEL score \<0.29 for missense variants (based on guidance from Pejaver et al, 2022, PMID: 36413997).
*   In frame deletion or insertion predicted benign by PROVEAN and MutationTaster.
*   No predicted impact on splicing by SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) , based on a score \<0.1 (as indicated in PMID: 37352859, Table 1 and Figure 4).

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：Experimental evidence, such as RT-PCR, shows no impact on splicing. Follow the decision tree outlined in Figure 5, Walker et al, 2023, PMID: 37352859. Note that splicing may appear normal in compound heterozygous patients if the splicing defect generates a transcript that is degraded by nonsense-mediated decay. Therefore, caution must be used when assessing the data prior to applying this code.
- **Supporting** 📋：A synonymous (silent) variant OR an intronic variant at or beyond positions +7 and -21, for which SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/), predicts no impact on splicing (score \<0.1).

### 组合规则（Rules for Combining Criteria；官网 v2.0，Richards 2015 组合规则面板）

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
2. 1 Strong AND ≥ 1 Moderate
3. 1 Strong AND ≥ 2 Supporting
4. ≥ 3 Moderate
5. 2 Moderate AND ≥ 2 Supporting
6. 1 Moderate AND ≥ 4 Supporting
7. 1 Very Strong AND 1 Supporting

**Benign（良性）**
1. ≥ 2 Strong
2. 1 Stand Alone

**Likely Benign（可能良性）**
1. 1 Strong AND 1 Supporting
2. ≥ 2 Supporting

### 不适用证据码
PS2、PS4、PM1、PM6、PP1、PP2、PP5、BS4、BP1、BP3、BP5、BP6
### 参考附件
- [Appendix 4_GAMT REVEL scores](https://cspec.genome.network/cspec/File/id/f327e09b-a40d-4956-9818-d551b6030ad8/data)
- [Appendix 3_GAMT MAF thresholds](https://cspec.genome.network/cspec/File/id/ee02dcaa-29f6-4e57-8eee-a3a25b38114b/data)
- [Appendix 2_GAMT functional studies](https://cspec.genome.network/cspec/File/id/1147ba10-1814-413a-a861-3bced9808ff7/data)
- [GAMT PVS1 flowchart](https://cspec.genome.network/cspec/File/id/2f75e1de-c648-47dc-b3ef-037373c67649/data)
- [Appendix 1_GAMT](https://cspec.genome.network/cspec/File/id/0e84bb79-dc88-4bcd-9f4d-e43166c29ac7/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN026)

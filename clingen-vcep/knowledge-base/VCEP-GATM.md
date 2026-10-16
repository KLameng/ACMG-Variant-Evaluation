# ClinGen VCEP基因特异性规范：GATM

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：Version 2.0（DOI: 10.5281/zenodo.21421625；核验日期 2026-10-09）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN025 — Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0012996**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：**Nonsense-mediated decay predicted.**

CCDS VCEP notes:  
Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D ([https://databases.lovd.nl/shared/variants/GATM/unique](https://databases.lovd.nl/shared/variants/GATM/unique)). The specifications below are based on the PVS1 decision tree (see Appendix 1) (based on Figure 1, Abou Tayoun et al, 2018, PMID 30192042).

GATM specifications:  
**Nonsense and frameshift variants**  
\* All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 9) or the last 50 bases of the penultimate exon (exon 8, 3’ of c.1109). In that case, please refer to the PVS1 flowchart for guidance on PVS1 weight (Appendix 1).

**Splice site variants (+1, +2, -1, -2)**  
\* All canonical splice site pairs in GATM are GT-AG.  
\* For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants. However, to apply PVS1 at the very strong level, splice site variants must have no detectable nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing, as predicted by SpliceAI. Otherwise, the PVS1 strength should be reduced accordingly.  
\* For the predicted in frame/out of frame consequences of exon skipping and considerations for strength of PVS1, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).  
\* If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.  
\* Non-canonical splice variants, such as +3 or -3, may also meet PVS1 - refer to Walker et al, PMID: 37352859.

**Deletions (single or multi exon)**  
\* If a single or multi-exon deletion results in an out of frame consequence, use PVS1 at the very strong level unless not predicted to undergo NMD. If not predicted to undergo NMD, please refer to Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).  
\* If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. For weight of PVS1, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss) .  
\* If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.

**Duplications**  
\* To assess the impact of duplications, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).
- **Strong** 📋：**In frame loss of >10% of the protein.**  
CCDS VCEP notes:  
Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D ([https://databases.lovd.nl/shared/variants/GATM/unique](https://databases.lovd.nl/shared/variants/GATM/unique)). The specifications below are based on the PVS1 decision tree (see Appendix 1) (Figure 1, Abou Tayoun et al, 2018, PMID 30192042).

GATM specifications:  
**Nonsense and frameshift variants**  
\* All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 9) or the last 50 bases of the penultimate exon (exon 8, 3’ of c.1109). In that case, please refer to the PVS1 flowchart for guidance on PVS1 weight (Appendix 1).

**Splice site variants (+1, +2, -1, -2)**  
\* All canonical splice site pairs in GATM are GT-AG.  
\* For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants. However, it is recommended to use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing.   
\* For considerations for strength at which PVS1 may be applied see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss) .  
\* If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.  
\* Non-canonical splice variants, such as +3 or -3, may also meet PVS1 - refer to Walker et al, PMID: 37352859.

**Deletions (single or multi exon)**  
\* If a single or multi-exon deletion results in an out of frame consequence, use PVS1 at the very strong level unless not predicted to undergo NMD. If not predicted to undergo NMD, please refer to Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).  
\* If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. For weight of PVS1, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss) .  
\* If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.

**Duplications**  
\* To assess the impact of duplications, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).
- **Moderate** 📋：**Single exon or larger deletion resulting in loss of \<10% of the protein, and initiator codon variants.**

CCDS VCEP notes:  
Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D ([https://databases.lovd.nl/shared/variants/GATM/unique](https://databases.lovd.nl/shared/variants/GATM/unique)). The specifications below are based on the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042).  

GATM specifications:

**Nonsense and frameshift variants**  
\* All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in the last exon (exon 9) or the last 50 bases of the penultimate exon (exon 8, 3’ of c.1109). In that case, please refer to the PVS1 flowchart for guidance on PVS1 weight (Appendix 1).

**Splice site variants (+1, +2, -1, -2)**  
\* All canonical splice site pairs in GATM are GT-AG.  
\* For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped i.e. upstream exon skipped for canonical donor splice site variants and downstream exon skipped for canonical acceptor splice site variants. However, it is recommended to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing.   
\* For considerations for strength at which PVS1 may be applied see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).  
\* If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used.  
\* Non-canonical splice variants, such as +3 or -3, may also meet PVS1 (refer to Walker et al, PMID: 37352859).

**Initiator codon variants**  
\* All initiator codon variants will meet PVS1\_Moderate. The next in-frame methionine is at amino acid position 130 (based on NP\_001473). 

**Deletions (single or multi exon)**  
\* If a single or multi-exon deletion results in an out of frame consequence, use PVS1 at the very strong level unless not predicted to undergo NMD. If not predicted to undergo NMD, please refer to Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).  
\* If the consequence is in frame, the deletion must encompass one or more exons for PVS1 to apply. For weight of PVS1, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss) .  
\* If the in frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.

**Duplications**  
\* To assess the impact of duplications, see Appendix 1 (PVS1 flowchart) and Appendix 2 (predicted impact of exon loss).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：*   This criterion is applicable as is for any variant resulting in the same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.
*   PS1 may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).
- **Moderate** 📋：*   This criterion is applicable as for any variant resulting in the same amino acid change as a previously established likely pathogenic variant regardless of nucleotide change.
*   If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing.
*   PS1\_Moderate may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).
- **Supporting** 📋：PS1\_Supporting may be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859).

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** 📋：AGAT activity data from an in vitro assay in which GATM variants were overexpressed in HeLa cells has been published (DesRoches et al, 2016; PMID 27233232). Any variant with AGAT activity at or below 15% of normal in this paper meets PS3\_Supporting (see Appendix 3 for further details on AGAT functional assays).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：**Allele frequency \<0.000055 (\<0.0055%) in all populations in gnomAD.**

CCDS VCEP notes: It is acceptable for a GATM variant to be present in controls, if heterozygous, because AGAT-D is a recessive disorder. Homozygotes should not be seen in a population database, such as gnomAD, because the penetrance of this condition in individuals with biallelic pathogenic variants is expected to be 100%. 

GATM specifications:

*   All subpopulations in gnomAD must have a maximum allele frequency less than 0.000055 (based on the prevalence of the most common suspected pathogenic variants, c.484+1G>T and p.Arg169Ter) (see Appendix 4). Use the current version recommended by SVI; version number will be stated in classification summary.
*   Note – PM2 will NOT be used at moderate strength; PM2 will only be applied as a Supporting criterion.
*   If homozygotes are observed, the variant will meet BS2 (assuming 100% penetrance for an individual with 2 pathogenic variants in trans).

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
- **Moderate** 📋：CCDS VCEP notes: Stop loss variants in GATM have not been reported, as far as we are aware. 

GATM specifications: Use this rule “as is” for in frame deletions and insertions of 2 or more amino acids, but downgrade to PM4\_Supporting for single amino acid deletions and insertions.
- **Supporting** 📋：Downgrade to PM4\_Supporting for in frame deletion/insertion of a single amino acid.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** 📋：If the pathogenicity of another missense change at the same amino acid residue is unknown, determine its pathogenicity using these specifications in order to determine if this criterion can be used. If the variant is pathogenic, use PM5. If the variant is likely pathogenic, use PM5\_Supporting.
- **Supporting** 📋：Missense change at an amino acid residue where a different missense change determined to be likely pathogenic has been seen before.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** 📋：Missense variant with a REVEL score >0.773 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
- **Supporting** 📋：*   Missense variant with a REVEL score 0.644-0.773 (based on guidance from Pejaver et al, 2022, PMID: 36413997).
*   In frame deletion or insertion predicted deleterious by PROVEAN and MutationTaster. Results must be consistent to count.
*   For non-canonical splice site variants (e.g., +3, -3), predict the impact on splicing by using SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) , and apply PP3 for a score equal to or >0.2 (as indicated in PMID: 37352859, Table 1 and Figure 4). Assess the possibility of activation of cryptic splice sites.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** 📋：4 or more points based on any combination of the following. Two or more data types are required to meet Strong:  
• Low urine guanidinoacetate with or without low or low normal creatine (1 point)  
• Low plasma guanidinoacetate with or without low or low normal creatine (2 points)  
• Significantly decreased creatine peak in brain magnetic resonance spectroscopy (3 points)  
• AGAT enzyme activity \<5% of normal (3 points)

\* Variant must meet PM2\_Supporting for PP4 to apply at any strength.  
\* For PP4 to be applied at strong, full GATM gene sequencing, including all coding exons and intron/exon boundaries, must have been carried out. If not, consider downgrading.
- **Moderate** 📋：3 points based on any combination of the following. Two or more data types are recommended to reach moderate:  
• Low urine guanidinoacetate with or without low or low normal creatine (1 point)  
• Low plasma guanidinoacetate with or without low or low normal creatine (2 points)  
• Significantly decreased creatine peak in brain magnetic resonance spectroscopy (3 points)  
• AGAT enzyme activity \<5% of normal (3 points)

Variant must meet PM2\_Supporting for PP4 to apply at any strength.
- **Supporting** 📋：1-2 points based on:  
• Low urine guanidinoacetate with or without low or low normal creatine (1 point)  
• Low plasma guanidinoacetate with or without low or low normal creatine (2 points)  
Variant must meet PM2\_Supporting for PP4 to apply at any strength.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：**GrpMax >0.0005 (0.05%) in gnomAD**

*   Any variant with a GrpMax (lower bound 95%ile) >0.0005 in gnomAD. Use the current version recommended by SVI; version number will be stated in classification summary. 
*   Threshold based on (max allelic contribution = 100% and max genetic contribution = 100% based on estimated prevalence of 1 in 3,450,000 (PMID 27233232), and penetrance of 100%) (PMID 30311383) (see Appendix 3)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：**GrpMax >0.0001 (0.01%) in gnomAD**

*   Any variant with a GrpMax (lower bound 95%ile) >0.0001 in gnomAD. Use the current version recommended by SVI; version number will be stated in classification summary.
*    Threshold based on max allelic contribution = 25% and max genetic contribution = 100% based on estimated prevalence of 1 in 3,450,000, (PMID 27233232), and penetrance of 100%) (PMID 30311383) (see Appendix 3).

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** 📋：Observed in the homozygous state in a healthy adult.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** 📋：In vitro assays in which a variant is expressed in AGAT-deficient cultured cells (e.g. AGAT-deficient fibroblasts) or in-fusion High-Fidelity cloning of GATM transcript and site directed mutagenesis to generate missense variant overexpressed in HeLa cells and measurement of AGAT activity in cells for wild-type and missense variant. Any variant with enzyme activity at or above 30% of normal in DesRoches et al, 2016, PMID 27233232, meets BS3\_Supporting.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** 📋：Observed in cis with a pathogenic variant (to take AR inheritance for AGAT deficiency into account).

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   REVEL score \<0.29 for missense variants (based on guidance from Pejaver et al, 2022, PMID: 36413997).
*   In frame deletion or insertion predicted benign by MutPredIndel and MutationTaster.
*   No predicted impact on splicing by SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/) , based on a score \<0.1 (as indicated in PMID: 37352859, Table 1 and Figure 4).

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：Experimental evidence, such as RT-PCR, shows no impact on splicing. Follow the decision tree outlined in Figure 5, Walker et al, 2023, PMID: 37352859. Note that splicing may appear normal in compound heterozygous patients with one allele that is degraded by nonsense-mediated decay as the results of a frameshift and premature termination codon due to splicing defect. Therefore. caution must be used in asessing the data prior to applying this code.
- **Supporting** 📋：A synonymous (silent) variant OR an intronic variant at or beyond positions +7 and -21, for which SpliceAI, [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/), predicts no impact on splicing (score \<0.1) (see Walker et al, 2023, PMID: 37352859).

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
- 1 Very Strong AND 1 Supporting

**Benign（良性）**
- ≥ 2 Strong
- 1 Stand Alone

**Likely Benign（可能良性）**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

### 不适用证据码
PS2、PS4、PM1、PM6、PP1、PP2、PP5、BS4、BP1、BP3、BP5、BP6
### 参考附件
- [Appendix 3_GATM (AGAT) _ functional studies](https://cspec.genome.network/cspec/File/id/e4569ff7-a707-441c-969d-6998b4dea8b3/data)
- [Appendix 4_GATM (AGAT) _ MAFs](https://cspec.genome.network/cspec/File/id/791caa57-0400-449e-992d-fab2104a9d55/data)
- [Appendix 2_GATM (AGAT) _ exons](https://cspec.genome.network/cspec/File/id/695ebdc0-cea2-4fb4-b24e-9442ca178c7c/data)
- [Appendix 1_GATM (AGAT) _ PVS1 decision tree](https://cspec.genome.network/cspec/File/id/9fc11ad8-a955-4b12-927d-eec103a58cd1/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN025)

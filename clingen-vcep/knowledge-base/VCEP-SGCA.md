# ClinGen VCEP基因特异性规范：SGCA

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN189 — Limb Girdle Muscular Dystrophy Variant Curation Expert Panel

> 官网版本：Version 2.0；DOI: 10.5281/zenodo.21434851；核验日期：2026-10-09；积分制（Tavtigian Bayesian，PV=8/4/2/1/-1/-4）

### 覆盖疾病
- **MONDO:0015152**（遗传方式：Autosomal recessive inheritance）

### 通用说明
Once criteria are applied and the strength level specified, the Bayesian points-based approach (PMID: 32720330) should be used to determine the final variant classification. Please disregard the "Rules for Combining Criteria" section and instead use the tables in the supplementary file "Bayesian points system".

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Please see attached _SGCA_ PVS1 flowchart. In addition, for any variant with RNA/splicing data, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=8]
- **Strong** ✅：Please see attached _SGCA_ PVS1 flowchart. In addition, for any variant with RNA/splicing data, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=4]
- **Moderate** ✅：Please see attached _SGCA_ PVS1 flowchart. In addition, for any variant with RNA/splicing data, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=2]
- **Supporting** ✅：Please see attached _SGCA_ PVS1 flowchart. In addition, for any variant with RNA/splicing data, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=1]

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：For missense variants for which the amino acid change is the expected mechanism of disease, apply at Strong for 1 pathogenic or 2 likely pathogenic variants resulting in the same amino acid change. The likely pathogenic or pathogenic variant(s) must have been classified using LGMD VCEP specifications, and potential splice effects must be excluded for the missense variant under curation and the variant(s) resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application.

For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. 

For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file “PS1 splicing". [PV=4]
- **Moderate** ✅：For missense variants for which the amino acid change is the expected mechanism of disease, apply at Moderate for 1 likely pathogenic variant resulting in the same amino acid change. The likely pathogenic variant must have been classified using LGMD VCEP specifications, and potential splice effects must be excluded for the missense variant under curation and the variant resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application.

For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. 

For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file “PS1 splicing". [PV=2]
- **Supporting** ✅：For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file “PS1 splicing". [PV=1]

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Supporting** ✅：Apply for confirmed _de novo_ occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. [PV=1]

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Variant-specific animal models are rare but may be assessed on a case-by-case basis and PS3 applied at a strength level that reflects how well the model recapitulates features observed in human patients. Apply PS3 at Strong for a variant-specific animal model that meets all of the following conditions, regardless of species: 

*   signs of myopathy or dystrophy are present in skeletal muscle 
*   an effect on gene or protein function is demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality)
*   behavioral signs of muscle weakness
*   progression over time

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level. [PV=4]
- **Moderate** ✅：Variant-specific animal models are rare but may be assessed on a case-by-case basis and PS3 applied at a strength level that reflects how well the model recapitulates features observed in human patients. Apply PS3\_Moderate for a variant-specific animal model that meets all of the following conditions, regardless of species: 

*   signs of myopathy or dystrophy are present in skeletal muscle 
*   an effect on gene or protein function is demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality)

PS3\_Moderate may be applied for sarcoglycan complex membrane localization assays that have been clinically validated with ≥11 control variants that meet criteria specified in Brnich et al. 2020 (PMID: 31892348) for the number of pathogenic and benign control variants. See supplementary file “PS3 assays\_SGCA”.

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level. [PV=2]
- **Supporting** ✅：PS3\_Supporting may be applied if the variant is expressed in heterologous cell lines/model organisms and shows absent membrane localization of the sarcoglycan protein complex and fewer than 11 control variants were used, in accordance with Brnich et al. 2020 (PMID: 31892348). See supplementary file “PS3 assays\_SGCA”.

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level. [PV=1]

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：Use without disease-specific modification if case-control studies are available.   
While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for _SGCA_. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease. [PV=4]

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Apply if the Grpmax variant allele frequency / upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency in gnomAD is \<0.00009. Do not use data for which the variant does not pass quality control filters. 

*   If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
*   If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency

Grpmax refers to the gnomAD subpopulation with the highest variant allele frequency. Use large, non-bottlenecked genetic ancestry groups for the Grpmax; avoid using the Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups as well as the genomes-only data for the Middle Eastern group.

The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Confidence interval tools, such as Confit-de-MAF ([https://www.genecalculators.net/confit-de-maf.html](https://www.genecalculators.net/confit-de-maf.html)), can be used.

Use the gnomAD version with the largest allele number. 

For larger deletions or duplications that may not be well represented in gnomAD (e.g., single- or multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the Database of Genomic Variants (DGV) ([https://dgv.tcag.ca/dgv/app/home](https://dgv.tcag.ca/dgv/app/home)). [PV=1]

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Use the SVI Working Group’s recommended point system to determine PM3 strength (see supplementary file “PM3 table”). ≥ 4 pts is required to apply PM3 at Very Strong. [PV=8]
- **Strong** ✅：Use the SVI Working Group’s recommended point system to determine PM3 strength (see supplementary file “PM3 table”). PM3\_Strong should be applied for ≥ 2 pts but \< 4 pts. [PV=4]
- **Moderate** ✅：Use the SVI Working Group’s recommended point system to determine PM3 strength (see supplementary file “PM3 table”). PM3 (Moderate) should be applied for ≥ 1 pt but \< 2 pts. [PV=2]
- **Supporting** ✅：Use the SVI Working Group’s recommended point system to determine PM3 strength (see supplementary file “PM3 table”). PM3\_Supporting should be applied for ≥ 0.5 pts but \< 1 pt. [PV=1]

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Use as is, regardless of the length of the in-frame insertion or deletion. [PV=2]

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score \<0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Strong for 2 pathogenic or 3 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application. [PV=4]
- **Moderate** ✅：Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score \<0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Moderate for 1 pathogenic or 2 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application. [PV=2]
- **Supporting** ✅：Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score \<0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Supporting for 1 likely pathogenic variant resulting in a different amino acid change at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application. [PV=1]

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Segregations should be counted across families, with the total number of segregations determining the strength level. Apply PP1\_Strong for 3 affected segregations (in addition to proband) across ≥2 families. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). [PV=4]
- **Moderate** ✅：Segregations should be counted across families, with the total number of segregations determining the strength level. Apply PP1\_Moderate for 2 affected segregations (in addition to proband; may be from a single family). When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). [PV=2]
- **Supporting** ✅：Segregations should be counted across families, with the total number of segregations determining the strength level. Apply PP1 (Supporting) for 1 affected segregation (in addition to proband). When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). [PV=1]

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants, use REVEL with a score ≥0.7. 

For variants that may affect splicing, use SpliceAI with a score ≥0.5.

For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=1]

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：Use the PP4 table (see supplementary file “PP4 table SGCA”) to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). [PV=4]
- **Moderate** ✅：Use the PP4 table (see supplementary file “PP4 table SGCA”) to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). If PP1\_Moderate is applied and the criteria for PP4\_Strong are also met, a downgraded PP4\_Moderate can be applied. [PV=2]
- **Supporting** ✅：Use the PP4 table (see supplementary file “PP4 table SGCA”) to determine the appropriate PP4 strength level.  Apply PP4 only once, for a patient meeting the highest possible strength level. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). [PV=1]

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is >0.002. This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters. See supplementary file “benign frequency exceptions” for a list of variants defined as exceptions to the benign frequency rules. Ongoing updates to this list will be available at the LGMD VCEP webpage: [https://clinicalgenome.org/affiliation/50061/.](https://clinicalgenome.org/affiliation/50061/.) Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP. [PV=Not Applicable]

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is >0.0009. This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters. See supplementary file “benign frequency exceptions” for a list of variants defined as exceptions to the benign frequency rules. Ongoing updates to this list will be available at the LGMD VCEP webpage: [https://clinicalgenome.org/affiliation/50061/.](https://clinicalgenome.org/affiliation/50061/.) Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP. [PV=-4]

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do not apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon. [PV=-4]

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Use when variant is found _in cis_ with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications. [PV=-1]

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：For missense variants, use REVEL with a score ≤0.1 AND SpliceAI with a score ≤0.05.

For variants that may affect splicing, use SpliceAI with a score ≤0.05. Splice AI scores can be calculated here: [https://spliceailookup.broadinstitute.org/](https://spliceailookup.broadinstitute.org/)

For any variant with RNA or other experimental data indicating no impact on splicing, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “experimental splice data”. [PV=-1]

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：For any variant that has been experimentally shown to have no splice impact, follow the SVI Working Group’s recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file “Experimental splice data”. Apply BP7\_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out. [PV=-4]
- **Supporting** ✅：For splice predictions, use SpliceAI with a score ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). [PV=-1]

### 不适用证据码
PM1、PM6、PP2、PP5、BS2、BS3、BP1、BP3、BP5、BP6
### 参考附件
- [PS3 assays SGCA](https://cspec.genome.network/cspec/File/id/1724d79f-69c2-4eb2-b48e-b83336adf4db/data)
- [benign frequency exceptions](https://cspec.genome.network/cspec/File/id/179223b3-15e3-48a1-9379-db1d5f4e6477/data)
- [PM3 table](https://cspec.genome.network/cspec/File/id/4395075a-a3be-4003-954b-fd105a0e934b/data)
- [PVS1 flowchart SGCA](https://cspec.genome.network/cspec/File/id/90c016bf-ef16-41aa-a7ab-335dcb4fa214/data)
- [PP4 table SGCA](https://cspec.genome.network/cspec/File/id/5bfc1aaf-e271-46a4-8ce3-361d3e1db77a/data)
- [PM3 co-application examples](https://cspec.genome.network/cspec/File/id/afd5cfd7-aa21-4c64-9fd2-5c283b8dc57f/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN189)

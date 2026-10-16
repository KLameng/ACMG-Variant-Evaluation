# ClinGen VCEP基因特异性规范：OTC

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；附件文件名含版本日期线索：GN156_OTC_Functional_Assay_120825.xlsx；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN156 — Urea Cycle Disorders Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0010703**（遗传方式：X-linked inheritance）

### 通用说明
 The UCD VCEP will use the Bayesian point system as described by Tavtigan, 2020 [PMID:32720330].  See attached “Points System OTC” for points scale.           

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：See “OTC VCEP PVS1 Decision tree” file
- **Strong** ✅：*   PVS1\_Strong is applicable for nonsense frameshift, and splice variants affecting nucleotide c.1033 and downstream
    *   Several variants downstream of c.1032 leading to frameshift, stop-loss, and protein extension are reported in affected individuals in the literature demonstrating the critical role of the C-terminal region of OTC for protein function \[PMID:9143919, 39256843, 23278509, 34014557, 34014569\]
*   See “OTC VCEP PVS1 Decision tree” file
- **Moderate** ✅：See “OTC VCEP PVS1 Decision tree” file

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Applicable when the previously reported variant is classified as Pathogenic using these OTC specifications.
- **Moderate** ✅：Applicable when the previously reported variant is classified as Likely Pathogenic using these OTC specifications.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：Use ClinGen Sequence Variant Interpretation (SVI) Review Committee recommended scoring system, attached “PS2.PM6\_Scoring”.
- **Strong** ✅：Use SVI recommended scoring system, attached “PS2.PM6\_Scoring”.
- **Moderate** ✅：Use SVI recommended scoring system, attached “PS2.PM6\_Scoring”.
- **Supporting** ✅：Use SVI recommended scoring system, attached “PS2.PM6\_Scoring”.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：PS3 at a strong level is not applicable for OTC enzyme activity assays. Please see PS3\_Moderate and PS3\_supporting below.
- **Moderate** ✅：Yeast growth assays -- applicable when growth of the ARG3 variant strain is ≤50% when compared to wildtype strains
- **Supporting** ✅：Yeast growth assays -- applicable when growth of the ARG3 variant strain is >50 and ≤65% when compared to wildtype strains

Enzyme activity in non-patient derived cell lines -- applicable if enzyme activity of the variant under review is \<20% compared to wildtype.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Very Strong** ✅：8 additional male or female probands observed - must meet PP4 criteria and/or have documented hyperammonemia or metabolic decompensation under physiological stress to be counted
- **Strong** ✅：4 additional male or female probands observed - must meet PP4 criteria and/or have documented hyperammonemia or metabolic decompensation under physiological stress to be counted
- **Moderate** ✅：2 additional male or female probands observed - must meet PP4 criteria and/or have documented hyperammonemia or metabolic decompensation under physiological stress to be counted
- **Supporting** ✅：One additional male or female proband observed - must meet PP4 criteria and/or have documented hyperammonemia or metabolic decompensation under physiological stress to be counted

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：The following residues are considered critical within OTC: 

Carbamoylphosphate binding site – amino acids: Ser-90, Thr-91, Arg-92, Thr-93, His-117, Arg-141, His-168, Gln-171, Leu-304, and Arg-330 

Ornithine binding site – amino acids: Leu-163, Asn-198, Asn-199, Asp-263, Ser-267, Met 268 

Catalytic site – amino acids: His-302, Cys-303, Leu-304 

Conserved amino acids important for OTC structure and function:  

Arg-277 - Affect Km for ornithine \[PMID: 9175746, 9065786\] 

Pro-305 - cis-proline that stabilizes the HCLP motif \[PMID: 9852088\] 

Gly-269 - part of the mobile SMG loop \[PMID: 8544185\]

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Applicable for variants in OTC with Grpmax Filtering Allele Frequency \<0.000015 (0.0015%) AND ≤1 homo- or hemizygote in the most current version of gnomAD available at the time of curation.  

Rationale: The most common pathogenic variant in population databases is p.Arg40Cys, which is associated with late onset OTC Deficiency (PMID: 23209112, 7860066, 11260212, others) and present in 17 heterozygotes and 6 hemizygotes in gnomAD(v4.0.0) (Mino Allele frequency=0.001586% in European populations).  Other commonly reported pathogenic variants (p.Arg277Trp, p.Arg141Gln, p.Arg141Ter) are rare or absent in population databases, therefore a threshold of 0.0015% is set for PM2\_Supporting.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：PM4 is applicable as described for in-frame loss or gain of ≥1 amino acid but less than an entire exon. For in-frame deletions or insertions ≥1 exon, defer to PVS1 flowchart.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：PM5 is applicable as described if the variant under review occurs at the same amino acid as a variant classified Pathogenic using these OTC specifications.
- **Supporting** ✅：PM5 is applicable as described if the variant under review occurs at the same amino acid as a variant classified Likely Pathogenic using these OTC specifications.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：Use PS2/PM6 criteria described under PS2.  Occurrences of de novo and presumed de novo are summed for a final PS2/PM6 evidence strength.
- **Moderate** ✅：Use PS2/PM6 criteria described under PS2.  Occurrences of de novo and presumed de novo are summed for a final PS2/PM6 evidence strength.
- **Supporting** ✅：Use PS2/PM6 criteria described under PS2.  Occurrences of de novo and presumed de novo are summed for a final PS2/PM6 evidence strength.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：≥5 informative segregations
- **Moderate** ✅：3-4 informative segregations
- **Supporting** ✅：2 informative segregations

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：Missense variants - REVEL score ≥0.932
- **Moderate** ✅：Missense variants - REVEL score ≥0.773 and \<0.932
- **Supporting** ✅：Missense variants - REVEL score ≥0.644 and \<0.773 

Splice region and intronic variants - spliceAI delta score ≥0.20

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Proband phenotype points total ≥1.5 points
- **Supporting** ✅：Proband phenotype points total >0.5 to \<1.5 points

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency above 0.010000 (1.0%), Grpmax Filtering Allele Frequency OR ≥10 (female) homozygotes or (male) hemizygotes in the most current version of gnomAD available at the time of curation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：An allele frequency >0.002000 (0.2%), Grpmax Filtering Allele Frequency in the  most current version of gnomAD available at the time of curation. 

Note: Both BS1 and BS2 cannot be applied if the same dataset is used to assess population data

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：The variant is observed in >5 (female) homozygotes or 5 (male) hemizygotes in the most current version of gnomAD available at the time of curation.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** ✅：BS3\_Moderate  is applicable when growth of the variant strain is ≥80% when compared to strains containing the wildtype OTC gene.
- **Supporting** ✅：Yeast growth assays in which the ARG3 open reading frame of a yeast strain is replaced with human OTC coding sequence, and site directed mutagenesis utilized to introduce variant of interest (PMID: 37146589) 

BS3\_Supporting is applicable when growth of the variant strain is >65% and \<80% growth when compared to strains containing the wildtype OTC gene.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Supporting** ✅：Presence of the variant under review in an unaffected male of a family if the age of the unaffected male is at or above the age of onset for other affected males in the family.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Applicable in females for which OTC deficiency is diagnosed and the variant under review is identified in trans or in cis with a known pathogenic variant, or if the variant under review is identified in cis in a male with OTC deficiency.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：Missense variants - REVEL score ≤0.016
- **Moderate** ✅：Missense variants - REVEL score >0.016 and ≤0.183
- **Supporting** ✅：Missense variants - REVEL score >0.183 and ≤0.290   
Splice region and intronic variants - spliceAI delta score \<0.1

Synonymous variants – spliceAI delta score \<0.1 if variant is not within the first or last three nucleotides of an exon.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Applicable when the variant of interest is identified in a male with an alternative molecular etiology of elevated hyperammonemia including biallelic pathogenic/likely pathogenic variants in autosomal recessive disease or a pathogenic/likely pathogenic variant for autosomal dominant or X-linked disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Applicable for potential splicing or intronic variants with experimental evidence demonstrating no splicing effect of the variant under review (BP7\_strong (RNA).
- **Supporting** ✅：Splicing / intronic variant -- applicable for intronic variants with spliceAI \<0.10 if the variant under review is outside splice region +7/-21 nucleotides.

Synonymous variants -- applicable when BP4\_Supporting is met and only if the synonymous variant is outside the first base of an exon and last 3 bases of an exon.

### 不适用证据码
PM3、PP2、PP5、BP1、BP3、BP6
### 参考附件
- [UCD VCEP PP3 table OTC](https://cspec.genome.network/cspec/File/id/60d1fd44-e6b1-4258-b965-8365ee96c266/data)
- [OTC VCEP response to SVI_093025](https://cspec.genome.network/cspec/File/id/908401fe-1a89-4961-a9b4-3a84dace36e8/data)
- [OTC Updates for CSpec_050125](https://cspec.genome.network/cspec/File/id/e1333306-65ac-45cd-8c36-f54aed4b9059/data)
- [OTC PVS1 Decision Tree_110425](https://cspec.genome.network/cspec/File/id/cc19a373-e725-4a88-836b-a43cdaa008c6/data)
- [OTC Step 3 Comments_110425](https://cspec.genome.network/cspec/File/id/386c0108-ce79-40c8-bacf-3479bf11654b/data)
- [Points System OTC](https://cspec.genome.network/cspec/File/id/f99df66f-465d-4230-bc43-34951254eb4d/data)
- [OTC functional supplement table_January2024](https://cspec.genome.network/cspec/File/id/5a13d1d8-eb2c-4a38-9a05-781e934dba33/data)
- [OTC Pilot data_110425](https://cspec.genome.network/cspec/File/id/1a019f68-d03b-484c-80e6-23c85ef614b6/data)
- [OTC splicing table_093025](https://cspec.genome.network/cspec/File/id/8704e6f4-95ba-4e17-8990-775e0a1ecb5a/data)
- [OTC_Functional_Assay_120825](https://cspec.genome.network/cspec/File/id/cbf124c4-6143-4bef-b515-fa7b984c147d/data)
- [OCT PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/7fd5ffff-7630-4e68-b5dd-73c79fb0a997/data)
- [UCD_VCEP_response_OTC_120825](https://cspec.genome.network/cspec/File/id/d0dfee44-fffe-4785-880a-4017d93222c4/data)
- [UCD VCEP BP4 table OTC](https://cspec.genome.network/cspec/File/id/43329367-7094-4e3f-8587-8c3b42403a58/data)
- [OTC PS2.PM6 scoring_093025](https://cspec.genome.network/cspec/File/id/47f336dc-e6de-47cc-8870-75155dd34bfc/data)
- [OTC PP4 points_093025](https://cspec.genome.network/cspec/File/id/ef86ae55-1dbe-4b1d-a059-e3345d6e05a9/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN156)

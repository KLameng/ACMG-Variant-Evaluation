# ClinGen VCEP基因特异性规范：GALT

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；附件文件名含版本日期线索：GN158_GALT_pilot_variants_111725.xlsx；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> 官网版本：v1.1（2026-07-23 发布；v1.1 更新：新增 PVS1 + PM2(Supporting)=Likely Pathogenic，新增 PM2 与 BP4/BP7 不视为冲突数据）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN158 — Galactosemia Variant Curation Expert Panel 

### 覆盖疾病
- **MONDO:0018116**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：*   The Galactosemia VCEP will utilize SVI’s PVS1 recommendation for determining applicable PVS1 strength level (Abou Tayoun et al 2018; PMID: 30192042). Refer to the modified PVS1 decision tree attached.
*   Exons 6, 7, and 9 are in-frame. Exon skipping consequences for splice site variants are listed in the attachment as well.
- **Strong** ✅：Refer to PVS1 decision tree attached.
- **Moderate** ✅：Refer to PVS1 decision tree attached.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
*   PS1 will be applied at the strong level for 1 previously established pathogenic missense variant or use Table 2 in Walker et al., PMID: 37352859 for splicing variant
*   The other variant(s) used for evidence should also have been curated using GALT VCEP rule specifications and reach a pathogenic/likely pathogenic classification without using PS1.
*   Same predicted impact on splicing as previously classified variant (refer to table 2 in Walker et al., 2023, PMID: 37352859).
    *   PS1 can by applied at varying strengths (strong, moderate, supporting) in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/-1,2, dinculeotide position). Specific combinations are outlined in table 2 Walker et al., 2023, PMID: 37352859.
- **Moderate** ✅：*   Same predicted impact on splicing as previously classified variant (refer to table 2 in Walker et al., 2023, PMID: 37352859).
    *   PS1 can by applied at varying strengths (strong, moderate, supporting) in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/-1,2, dinculeotide position). Specific combinations are outlined in table 2 Walker et al., 2023, PMID: 37352859.
*   PS1\_Moderate will apply for 1 previously established likely pathogenic variant or use Table 2 in Walker et al., 2023, PMID: 37352859 for splicing variant
- **Supporting** ✅：*   Same predicted impact on splicing as previously classified variant (refer to table 2 in Walker et al., 2023, PMID: 37352859).
    *   PS1 can by applied at varying strengths (strong, moderate, supporting) in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/-1,2, dinculeotide position). Specific combinations are outlined in table 2 Walker et al., 2023, PMID: 37352859.
*   PS1\_Supporting will apply for splicing variants only, used Table 2 in Walker et al., 2023, PMID: 37352859

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Supporting** ✅：Applicable for up to 20% enzyme activity in a model system

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：PM1 applied at moderate strength for variants that occur in the active site from Phe171 to Gln188

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：*   Can only be used at the supporting level 
*   Use the PopMax filtering allele frequency (FAF) from gnomAD.
*   Use if variant is present at ≤ 0.0005 or 0.05% 
    *   One order of magnitude below BS1
*   A curated list of _GALT_ variants known to be pathogenic despite not fulfilling the PM2 criterion has been developed (see PM2 exception list)

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Variant under investigation meets PM2, identified individuals meet PP4, and at least 4 PM3 points have been reached.
- **Strong** ✅：Variant under investigation meets PM2, identified individuals meet PP4, and at least 2 PM3 points have been reached.
- **Moderate** ✅：Variant under investigation meets PM2, identified individual(s) meet PP4, and at least 1 PM3 point has been reached.
- **Supporting** ✅：Variant under investigation meets PM2, identified individual(s) meet PP4, and at least 0.5 PM3 points have been reached.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：*   Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
*   PM5 will be applied at moderate strength for 1 pathogenic variant with no benign variation at the residue
*   The other variant(s) used for evidence should also have been curated using the GALT VCEP rule specifications and must reach a pathogenic/likely pathogenic classification without PM5.
*   Grantham should be used to compare the variants. The new variant must be equal or worse than the known pathogenic variant.
- **Supporting** ✅：*   PM5\_Supporting can be applied for 1 likely pathogenic variant with no benign variation at the residue.
*   The other variant(s) used for evidence should also have been curated using the GALT VCEP rule specifications and must reach a pathogenic/likely pathogenic classification without PM5
*   Grantham should be used to compare the variants. The new variant must be equal or worse than the known pathogenic variant.

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Moderate** ✅：Paternity and maternity must be confirmed. Patient must meet PP4.

Because there has only ever been one reported de novo occurrence of a _GALT_ variant and de novo occurrence is not expected to significantly contribute to disease, the VCEP will use PM6 and not PS2. PM6 will not be upgraded with number of occurrences.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Use general recommendations from Oza AM et al, 2018, PMID: 30311386, sufficient affected and unaffected segregations have been counted to reach likelihood of 32:1.
- **Moderate** ✅：Using general recommendations from Oza AM et al., 2018, PMID: 30311386, sufficient affected and unaffected segregations have been counted to reach likelihood of 16:1.
- **Supporting** ✅：Using general recommendations from Oza AM et al., 2018, (PMID: 30311386), sufficient affected and unaffected segregations have been counted to reach likelihood of 4:1.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants use REVEL with a score ≥0.7 
*   In-frame in/dels, Provean (“deleterious”) and MutationTaster (“Disease-causing”) must agree
*   For non-canonical splicing variants use SpliceAI with a score ≥0.2, look for cryptic splice sites.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：*   RBC GALT enzyme activity \<10%
*   In order to apply PP4 at the moderate level, newborn screen alone would not count, must have confirmatory testing. 
*   For PP4 to be applied at moderate level, full _GALT_ gene sequencing (exons and exon/intron boundaries) rather than _GALT_ panel testing must have been carried out.
*   Variants must meet PM2\_Supporting for PP4 to apply at any strength.
- **Supporting** ✅：*   RBC GALT enzyme activity \<10%
*   In order to apply PP4 at the supporting level, newborn screen alone would not count, must have confirmatory testing.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Use a minor allele frequency cutoff of ≥0.01 (1%) (use PopMax  FAF in gnomAD). This frequency was calculated using the Whiffen-Ware calculator with a prevalence estimated at 1 in 10,000, penetrance at 100%, maximum allelic contribution and maximum genetic contribution at 100%.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Use a minor allele frequency cutoff of ≥0.005 (0.5%) (use PopMax  FAF in gnomAD). This frequency was calculated using the Whiffen-Ware calculator with a prevalence estimated at 1 in 10,000, penetrance at 100%, maximum allelic contribution of 50% and maximum genetic contribution at 100%.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：This code is applicable when individual is confirmed to be unaffected by GALT activity levels

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：*   Can only be used at the supporting level 
*   Functional assay in non-patient material 
*   BS3\_Supporting is applicable for greater than 50% enzyme activity in a model system (cannot apply at strong level)

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Individual considered unaffected RBC GALT enzyme activity ≥25% with the caveat of no bone marrow transfusions in individual.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：*   Observed in cis with a likely pathogenic or pathogenic variant OR observed in trans with a pathogenic variant in an unaffected individual with RBC GALT enzyme activity in the carrier range
*   Pathogenicity of first variant must be determined using VCEP guidelines. 
*   Full gene sequencing including promoter region must have been completed to apply BP2

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：*   For missense variants use REVEL with a score of \<0.15 
*   In-frame in/dels, Provean (“neutral”) and MutationTaster (“polymorphism”) must agree

For non-canonical splicing variants use SpliceAI with a score of \<0.1, do not use if there is evidence of a cryptic splice site

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：*   Use “as is”, but no conservation requirement 
*   BP4 must be applied for BP7 to be used, the codes can be combined 
*   Do not use for silent variants in the first nucleotide or last 3 nucleotides of the exon
*   Can also be used for intronic variants at or beyond positions +7/-21 with no predicted effect on splicing.

### Rules for Combining Criteria

> 证据码强度集合：
> - Very Strong = (PVS1, PM3_Very Strong)
> - Strong = (PVS1_Strong, PS1, PM3_Strong, PP1_Strong)
> - Moderate = (PVS1_Moderate, PS1_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)
> - Supporting = (PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)

#### Pathogenic
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

#### Likely Pathogenic
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate
- 1 Strong (PVS1_Strong) AND 1 Supporting (PM2_Supporting)　〔v1.1 新增〕

#### Benign
- ≥ 2 Strong (BS1, BS2, BS4)
- 1 Stand Alone (BA1)

#### Likely Benign
- 1 Strong (BS1, BS2, BS4) AND 1 Supporting (BS3_Supporting, BP2, BP4, BP7)
- ≥ 2 Supporting (BS3_Supporting, BP2, BP4, BP7)

### 不适用证据码
PS2、PS4、PP2、PP5、BP1、BP3、BP5、BP6
### 参考附件
- [PVS1 for GALT VCEP](https://cspec.genome.network/cspec/File/id/04173bb8-7e0b-425a-9da5-fde882626898/data)
- [PP1 supporting for GALT VCEP](https://cspec.genome.network/cspec/File/id/23e591c0-1d52-4216-b923-3d3cf696a3f9/data)
- [GALT_PS3_functionalassay_071224](https://cspec.genome.network/cspec/File/id/60da2c30-095b-44b8-b36f-ab9d3dd80b7d/data)
- [Galactosemia VCEP SVI feedback response_042824](https://cspec.genome.network/cspec/File/id/6fbd2a6b-2a41-4fed-9712-89ef846312f9/data)
- [GALT_PM2_execption_list_111725](https://cspec.genome.network/cspec/File/id/0a5d3a01-d2e7-45bc-a875-7d359b32bbf4/data)
- [GALT VCEP PVS1 decision tree](https://cspec.genome.network/cspec/File/id/2fb8633d-7ad2-4b59-ac72-eed342e3478f/data)
- [Galactosemia VCEP pilot submission list_111725](https://cspec.genome.network/cspec/File/id/e53bf5d0-c320-4bcb-ae7b-643a780b1b3f/data)
- [GALT VCEP response to SVI feedback](https://cspec.genome.network/cspec/File/id/95ad6337-bb4b-48d4-af8b-f30de9490786/data)
- [GALT_pilot_variants_111725](https://cspec.genome.network/cspec/File/id/3c62f40c-81bf-4f59-bed3-480c7870b131/data)
- [PM3 moderate for GALT VCEP](https://cspec.genome.network/cspec/File/id/2e772578-4223-4942-ab03-bac24e7e7e6a/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN158)

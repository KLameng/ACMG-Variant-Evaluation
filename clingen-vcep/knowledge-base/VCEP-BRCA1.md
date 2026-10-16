# ClinGen VCEP基因特异性规范：BRCA1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN092 — ENIGMA BRCA1 and BRCA2 Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0700268**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Complete table of criteria combinations for variant classification is available in the Specifications word document attached.
            
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant (nonsense, frameshift, splice site (donor/acceptor +/−1,2), initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Apply at appropriate strength according to PVS1 flowchart, which considers knowledge of clinically important functional domains. See Specifications Table 4 and Appendix D for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.
- **Strong** ✅：Null variant (nonsense, frameshift, splice site (donor/acceptor +/−1,2), initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Apply at appropriate strength according to PVS1 flowchart, which considers knowledge of clinically important functional domains. See Specifications Table 4 and Appendix D for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.
- **Moderate** ✅：Null variant (nonsense, frameshift, splice site (donor/acceptor +/−1,2), initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Apply at appropriate strength according to PVS1 flowchart, which considers knowledge of clinically important functional domains. See Specifications Table 4 and Appendix D for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.
- **Supporting** ✅：Null variant (nonsense, frameshift, splice site (donor/acceptor +/−1,2), initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Apply at appropriate strength according to PVS1 flowchart, which considers knowledge of clinically important functional domains. See Specifications Table 4 and Appendix D for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Apply **PS1**, for predicted **missense** substitutions, where a previously classified **pathogenic** variant is considered to act via protein change (no confirmed or predicted effect on mRNA splicing (SpliceAI≤0.1)).

Apply **PS1**, for exonic and intronic variants with same predicted impact on **splicing**, as a previously classified **pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant. 

See Specifications Table 5 and Appendix E, J and K for details.
- **Moderate** ✅：Apply **PS1\_Moderate**, for predicted **missense** substitutions, where previously classified **likely pathogenic** variant is considered to act via protein change (no confirmed or predicted effect on mRNA splicing (SpliceAI≤0.1)).

Apply **PS1\_Moderate**, for exonic and intronic variants with same predicted impact on **splicing**, as a previously classified **(likely) pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant.

See Specifications Table 5 and Appendix E, J and K for details.
- **Supporting** ✅：Apply **PS1\_Supporting**, for exonic and intronic variants with same predicted impact on **splicing,** as a previously classified **(likely) pathogenic** variant. Vary weight depending on relative positions, and confidence in classification of the reference variant.

See Specifications Table 5 and Appendix E, J and K for details.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect. Apply PS3 for assays measuring effect via protein only OR mRNA and protein combined. See Specifications Table 9 for code recommendations from calibrated published assays. Also see Figure1C and Appendix E for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Case-control studies; p-value ≤0.05 and OR ≥4 (lower confidence interval excludes 2.0). See Appendix F for details.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent from controls in an outbred population, from gnomAD v2.1 (non-cancer, exome only subset) and gnomAD v3.1 (non-cancer). Region around the variant must have an average read depth ≥25. See Appendix G for details.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Strong** ✅：Apply for patient with phenotype consistent with BRCA1- or BRCA2-related Fanconi Anemia (FA), and co-occurrent variants in the same gene.Phenotype is considered consistent with BRCA1- or BRCA2-related FA if:

(i) Increased chromosome breakage (DEB, MMC, or spontaneous) and at least one clinical feature indicative of BRCA1/2-related FA, categorized under: physical features, pathology and laboratory findings, cancer diagnosis _≤5yr_.

(ii) Result unknown for chromosome breakage, and at least two clinical features indicative of BRCA1/2-related FA under at least two of the three categories: physical features, pathology and laboratory findings, cancer diagnosis ≤5yr.

See **Specifications Table 6** for approach to assign points per proband, and final PM3 code assignment based on the sum of PM3-related points. Also see Appendix H for additional details.

PM3\_Strong = ≥4 points
- **Moderate** ✅：Apply for patient with phenotype consistent with BRCA1- or BRCA2-related Fanconi Anemia (FA), and co-occurrent variants in the same gene.Phenotype is considered consistent with BRCA1- or BRCA2-related FA if:

(i) Increased chromosome breakage (DEB, MMC, or spontaneous) and at least one clinical feature indicative of BRCA1/2-related FA, categorized under: physical features, pathology and laboratory findings, cancer diagnosis _≤5yr_.

(ii) Result unknown for chromosome breakage, and at least two clinical features indicative of BRCA1/2-related FA under at least two of the three categories: physical features, pathology and laboratory findings, cancer diagnosis ≤5yr.

See **Specifications Table 6** for approach to assign points per proband, and final PM3 code assignment based on the sum of PM3-related points. Also see Appendix H for additional details.

PM3 = 2 points
- **Supporting** ✅：Apply for patient with phenotype consistent with BRCA1- or BRCA2-related Fanconi Anemia (FA), and co-occurrent variants in the same gene.Phenotype is considered consistent with BRCA1- or BRCA2-related FA if:

(i) Increased chromosome breakage (DEB, MMC, or spontaneous) and at least one clinical feature indicative of BRCA1/2-related FA, categorized under: physical features, pathology and laboratory findings, cancer diagnosis _≤5yr_.

(ii) Result unknown for chromosome breakage, and at least two clinical features indicative of BRCA1/2-related FA under at least two of the three categories: physical features, pathology and laboratory findings, cancer diagnosis ≤5yr.

See **Specifications Table 6** for approach to assign points per proband, and final PM3 code assignment based on the sum of PM3-related points. Also see Appendix H for additional details.

PM3\_Supporting = 1 point

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Protein termination codon (PTC) variant in an exon where a different proven pathogenic PTC variant has been seen before. Use to justify additional weight for PTC variants annotated as PVS1. See Specifications Table 4 for PM5\_PTC code strengths applicable per exon. See Appendix D for additional details.
- **Moderate** ✅：Protein termination codon (PTC) variant in an exon where a different proven pathogenic PTC variant has been seen before. Use to justify additional weight for PTC variants annotated as PVS1. See Specifications Table 4 for PM5\_PTC code strengths applicable per exon. See Appendix D for additional details.
- **Supporting** ✅：Protein termination codon (PTC) variant in an exon where a different proven pathogenic PTC variant has been seen before. Use to justify additional weight for PTC variants annotated as PVS1. See Specifications Table 4 for PM5\_PTC code strengths applicable per exon. See Appendix D for additional details.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

PP1\_Strong – LR ≥18.7:1

PP1\_Very Strong – LR ≥350:1
- **Moderate** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

PP1\_Moderate – LR ≥4.3:1
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

PP1 - LR ≥2.08:1

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Apply PP3 for missense or in-frame insertion, deletion or delins variants inside a (potentially) clinically important functional domain and predicted impact via protein change (BayesDel no-AF score ≥0.28). As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857.

Apply PP3 for predicted splicing (SpliceAI ≥0.2) for silent, missense/in-frame (irrespective of location in clinically important functional domain) and for intronic variants outside of donor and acceptor 1,2 sites.

See Specifications Figure1A and Appendix J for details.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：Breast cancer is very common and has a high degree of genetic heterogeneity (caused by pathogenic variants in numerous genes). Use ONLY to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

PP4\_Strong – LR ≥18.7:1

PP4\_Very Strong – LR ≥350:1

See Specifications Table7 and Appendix B for details.
- **Moderate** ✅：Breast cancer is very common and has a high degree of genetic heterogeneity (caused by pathogenic variants in numerous genes). Use ONLY to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

PP4\_Moderate – LR ≥4.3:1

See Specifications Table7 and Appendix B for details.
- **Supporting** ✅：Breast cancer is very common and has a high degree of genetic heterogeneity (caused by pathogenic variants in numerous genes). Use ONLY to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

PP4 - LR ≥2.08:1 

See Specifications Table7 and Appendix B for details.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Filter allele frequency (FAF) is above 0.1% (FAF > 0.001) in gnomAD v2.1 (non-cancer, exome only subset) and/or gnomAD v3.1 (non-cancer), non-founder population(s). See Appendix G for details.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Filter allele frequency (FAF) is above 0.01% (FAF > 0.0001) in gnomAD v2.1 (non-cancer, exome only subset) and/or gnomAD v3.1 (non-cancer), non-founder population(s). See Appendix G for details.
- **Supporting** ✅：Filter allele frequency (FAF) is above 0.002% (FAF > 0.00002) and less than or equal to 0.01% (FAF ≤ 0.0001) in gnomAD v2.1 (non-cancer, exome only subset) and/or gnomAD v3.1 (non-cancer), non-founder population(s). See Appendix G for details.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Applied in absence of features of recessive disease, namely Fanconi Anemia phenotype. See **Specifications Table 8** for additional stipulations, and approach to assign points per proband, and final BS2 code assignment based on the sum of BS2-related points. See Appendix H for additional details.

BS2 = ≥ 4 points
- **Moderate** ✅：Applied in absence of features of recessive disease, namely Fanconi Anemia phenotype. See **Specifications Table 8** for additional stipulations, and approach to assign points per proband, and final BS2 code assignment based on the sum of BS2-related points. See Appendix H for additional details.

BS2\_Moderate = 2 points
- **Supporting** ✅：Applied in absence of features of recessive disease, namely Fanconi Anemia phenotype. See **Specifications Table 8** for additional stipulations, and approach to assign points per proband, and final BS2 code assignment based on the sum of BS2-related points. See Appendix H for additional details.

BS2\_Supporting = 1 points

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. Assay measures effect via protein only OR mRNA and protein combined. See Specifications Table 9 for code recommendations from calibrated published assays. Also see Figure1C and Appendix E for details.

Well-established _in vitro_ or _in vivo_ functional studies supportive of no damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as BP7 (RNA) at appropriate strength. See Specifications Figure1B and Appendix E for details.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4 - LR ≤0.05:1

BS4\_VeryStrong – LR ≤0.00285:1
- **Moderate** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4\_Moderate - LR ≤0.23:1
- **Supporting** ✅：Lack of segregation in affected members of a family, as measured by a quantitative co-segregation analysis method. See Appendix I for details.

Apply weight as per Bayes Score:

BS4\_Supporting  - LR ≤0.48:1

#### BP1
- 默认强度：Benign Supporting
- ACMG原始定义：Missense variant in a gene for which primarily truncating variants are known to cause disease.
- **Strong** ✅：**Apply BP1\_Strong** for silent substitution, missense or in-frame insertion, deletion or delins variants outside a (potentially) clinically important functional domain AND no splicing predicted (SpliceAI ≤0.1). As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857. See Specifications Figure1A and Appendix J for details.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Missense or in-frame insertion, deletion or delins variants inside a (potentially) clinically important functional domain, and no predicted impact via protein change or splicing (BayesDel no-AF score ≤0.15 AND SpliceAI ≤0.1).

Silent variant inside a (potentially) clinically important functional domain, if no predicted impact via splicing (SpliceAI ≤0.1).

Intronic variants outside of the native donor and acceptor splice sites (i.e. not +/- 1,2 positions) AND no predicted impact via splicing (SpliceAI ≤0.1).

As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857. See Specifications Figure1A and Appendix J for details.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：Use ONLY to capture combined LR against pathogenicity, based on multifactorial likelihood clinical data.

BP5\_VeryStrong - LR ≤0.00285:1

BP5\_Strong - LR ≤0.05:1

Not applicable for co-observation: cases with pathogenic variants in two (or more) different known breast–ovarian cancer risk genes have no specific phenotype.
- **Moderate** ✅：Use ONLY to capture combined LR against pathogenicity, based on multifactorial likelihood clinical data.

BP5\_Moderate - LR ≤0.23:1

Not applicable for co-observation: cases with pathogenic variants in two (or more) different known breast–ovarian cancer risk genes have no specific phenotype.
- **Supporting** ✅：Use ONLY to capture combined LR against pathogenicity, based on multifactorial likelihood clinical data.

BP5 - LR ≤0.48:1

Not applicable for co-observation: cases with pathogenic variants in two (or more) different known breast–ovarian cancer risk genes have no specific phenotype.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function _as measured by effect on mRNA transcript profile – mRNA assay only._ Apply as BP7\_Strong (RNA) for intronic and silent variants, as well as missense/in-frame variants located outside a (potentially) clinically important functional domain. Missense variants located inside a (potentially) clinically important functional domain must meet BS3 to be eligible for BP7\_Strong (RNA). See Specifications Figure1B and Appendix E for details.

As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857. See Specifications Figure1A and Appendix J for details.
- **Supporting** ✅：Silent variant inside a (potentially) clinically important functional domain, IF BP4 met.

Intronic variants located outside conserved donor or acceptor motif positions (at or beyond positions +7/-21) IF BP4 met.

See Specifications Figure1A and Appendix J for additional details.

As justified in the appendices, (potentially) clinically important functional domains are defined as: BRCA1 RING aa 2-101; BRCA1 coiled-coil aa 1391-1424; BRCA1 BRCT repeats aa 1650-1857. See Specifications Figure1A and Appendix J for details.

### 不适用证据码
PS2、PM1、PM4、PM6、PP2、PP5、BP2、BP3、BP6
### 附件关键数据

#### PM5_PTC外显子特异性权重表（BRCA1/BRCA2 Specifications Table 4）

**BRCA1外显子PM5_PTC权重：**

| 外显子 | PM5_PTC权重 | 关键功能域 |
|-------|-------------|-----------|
| E1 | N/A | - |
| E2-E6 | Strong | RING domain (p.1-p.101) |
| E7 | Supporting | - |
| E8-E9 | N/A | - |
| E10-E11 | Strong | - |
| E12-E13 | Strong | - |
| E14-E23 | Strong | - |

**BRCA2外显子PM5_PTC权重：**

| 外显子 | PM5_PTC权重 | 关键功能域 |
|-------|-------------|-----------|
| E1 | N/A | - |
| E2-E5 | Strong | - |
| E6 | N/A | - |
| E7-E11 | Strong | - |
| E12 | N/A | - |
| E13-E27 | Strong | DBD domain |

**PVS1决策树关键规则：**
- 位于功能域内的LoF变异：PVS1_Very Strong
- 非功能域内的LoF变异：PVS1_Strong
- 内含子变异：根据对mRNA的影响程度确定

#### PS3功能检测表（BRCA1/BRCA2 Specifications Table 9）

**关键功能检测方法及其判读标准：**

| 检测方法 | 建议强度 | 阈值说明 |
|---------|---------|---------|
| Findlay et al. 2018 (饱和基因组编辑) | Strong | 变异功能评分与致病/良性对照相似 |
| Fernandes et al. 2019 (转录激活测定) | Moderate | 蛋白功能与致病变异相似 |
| Hart et al. 2019 (同源重组测定) | Strong | 蛋白功能与致病变异相似 |
| Richardson 2021 | Strong | 功能影响为"Damaging" |

**关键PMID参考：**
- Findlay et al. 2018, PMID: 30209399
- Fernandes et al. 2019, PMID: 30765603
- Hart et al. 2019, PMID: 29884841
- Richardson 2021, PMID: 33609447

#### PM3积分表（BRCA1/BRCA2 Supplementary Tables）

**Fanconi Anemia表型积分系统：**

| 表型特征类别 | 特征示例 | 积分 |
|------------|---------|------|
| 物理特征 | 典型FA表现 | 1分/项 |
| 病理和实验室发现 | 染色体断裂增加 | 1分/项 |
| 癌症诊断 | ≤5岁诊断癌症 | 1分/项 |

**PM3强度判定：**
| PM3强度 | 总积分阈值 |
|---------|-----------|
| PM3_Strong | ≥4分 |
| PM3 | ≥2分 |

**PM3应用条件：**
- 患者必须符合BRCA1/2相关Fanconi Anemia表型
- 染色体断裂增加（DEB、MMC或自发）+ 至少1个临床特征
- 或染色体断裂未知 + 至少2个临床特征（分布在不同类别）

### 参考附件
- [Specifications_V1.2](https://cspec.genome.network/cspec/File/id/11e62fec-23b0-4a3e-b2df-751855301746/data)
- [Supplementary_Tables_V1.2](https://cspec.genome.network/cspec/File/id/cb4a09fe-30f4-4aa8-9d76-d7ea407c9754/data)
- [Specifications_Table9_V1.2](https://cspec.genome.network/cspec/File/id/0a35d6a8-5050-44b6-8a9d-babe8cdc06b2/data)
- [Appendix_V1.2](https://cspec.genome.network/cspec/File/id/9e6119dc-90b9-42b5-a3b7-1a2eb28b1b12/data)
- [Specifications_Table4_V1.2](https://cspec.genome.network/cspec/File/id/ca5cf57b-94df-4ad6-a001-c62ceccb3845/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN092)

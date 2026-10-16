# ClinGen VCEP基因特异性规范：CYP1B1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN104 — Glaucoma Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0800472**（遗传方式：Autosomal recessive inheritance）

### 通用说明
> 官网版本：Version 2.0（Released 7/16/2026；DOI 10.5281/zenodo.21434369；Glaucoma VCEP，Tavtigian 贝叶斯积分）。
> Release Notes（v2.0 新增）：
> - PP3/BP4：当错义变异无法获得 REVEL 评分时（例如因改变 >1 个核苷酸），改用 AlphaMissense 判读。
> - PVS1(RNA)：对位于剪接供体/受体 ±1,2 二核苷酸之外的剪接致变变异，若体外分析显示可按 PVS1 决策过程解释的异常剪接谱，则套用 PVS1 决策树（按构建体实验设计降一级，替代 PP3）。

Modifications to the rules following pilot phase:
- PVS1_SA was added for full gene deletions (stand alone for Pathogenic classification).
- PS1: Specified that this rule does not apply to initiation codons
- PS3: Specified conditions for animal models of specific variants to meet PS3 if developed
- PM3: Piloted the use of VUS compound heterozygous in trans. VUS were used for applying PM3 to 3 variants & contributed to changing the final classification once (from LP to P). This rule is likely to be applied more often for variants with less evidence. The VCEP has decided to keep this rule but will reassess in the future as necessary.
- PM3: Specified that variants must not meet BP4 (instead of meeting PP3)
- PM3: Specified that individuals with multiple VUS/LP/P variants cannot be considered as evidence of either variant when the phase is unknown or variants are in cis
- PP1: Specified that compound heterozygous variants in affected segregations need to be in trans
- BA1: Threshold updated with justification
- BP4: Specified that the SpliceAI threshold applies to non-missense variants not meeting PVS1 or PM4
            
            
            
            

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **PVS1(RNA) 剪接致变规则（v2.0 新增）**：对位于剪接供体/受体 ±1,2 二核苷酸之外的剪接致变变异，若体外（in vitro）分析显示可按 PVS1 决策过程（参见 Walker et al.）解释的异常剪接谱，则套用 PVS1 决策树；按构建体实验设计的考量将 PVS1 降一级适用，此替代 PP3。
- **Very Strong** ✅：Applies to:

*   Nonsense/frameshifts variants predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)
*   GT-AG 1,2 splice sites variants leading to exon skipping or use of a cryptic splice site disrupting reading frame predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)
*   Full gene deletions and deletions removing exon 2 and/or exon 3
*   Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame, predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493), AND proven in tandem
- **Strong** ✅：Applies to:

*   Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame, predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493), AND presumed in tandem
- **Moderate** ✅：Applies to:

*   Nonsense/frameshifts variants NOT removing the haem-binding domain (aa494-Ter)
*   GT-AG 1,2 splice sites variants leading to exon skipping or use of a cryptic splice site disrupting reading frame and NOT predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)
*   Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame after the haem-binding domain (aa4934-Ter) AND proven in tandem
*   Initiation codon variants when there is no known alternative start codon in other transcripts and ≥1 pathogenic variant upstream of closest potential in-frame start codon
- **Supporting** ✅：Applies to:

*   Deletions removing exon 1 only
*   Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame after the haem-binding domain (aa4934-Ter) AND presumed in tandem

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established pathogenic variant.

For variants that affect splicing (SpliceAI > 0.2), refer to Table 3.[<sup>6</sup>](#PMID_37352859)
- **Moderate** ✅：For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established likely pathogenic variant.

For variants that affect splicing (SpliceAI > 0.2), refer to Table 3.[<sup>6</sup>](#PMID_37352859)
- **Supporting** ✅：For variants that affect splicing (SpliceAI > 0.2), refer to Table 3.[<sup>6</sup>](#PMID_37352859)

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：≥ 4.0 points
- **Strong** ✅：≥ 2.0 points
- **Moderate** ✅：≥ 1.0 points
- **Supporting** ✅：≥ 0.5 points

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Assays with OddsPath >18.7 as per the SVI recommendations

Animal models that replicate the glaucoma phenotype
- **Moderate** ✅：Assays with OddsPath >4.3 as per the SVI recommendations
- **Supporting** ✅：Assays with OddsPath >2.1 as per the SVI recommendations

As of 06/11/25, the following studies meet the criteria to apply PS3\_supporting: Chavarria-Soley et al. 2008[<sup>31</sup>](#PMID_18470941), Pasutto et al. 2010[<sup>33</sup>](#PMID_19643970) and Mammen et al. 2003[<sup>32</sup>](#PMID_12807732).

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Missense variants and in-frame indels in the hinge region (aa51-61) or the L-helix including the haem-binding domain (aa460-493).
- **Supporting** ✅：Missense variants and in-frame indels in the G helix (aa253-282) or the I helix (339-365).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Allele frequency ≤ 0.0005 in population databases.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：≥ 4.0 points
- **Strong** ✅：≥ 2.0 points
- **Moderate** ✅：≥ 1.0 points
- **Supporting** ✅：≥ 0.5 points

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Stop loss variants are not a known disease mechanism, therefore PM4 does not apply to that variant type

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same residue as 2 previously established pathogenic variants (in which case both variants must be assessed independently of PM5).
- **Moderate** ✅：Same residue as previously established pathogenic variant (assessed independently of PM5) or 2 previously established likely pathogenic variants (in which case both variants must be assessed independently of PM5).
- **Supporting** ✅：Same residue as previously established likely pathogenic variant (assessed independently of PM5).

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：≥ 3 affected segregations or 2 affected segregations AND ≥ 3 unaffected segregations or 1 affected segregation AND ≥ 8 unaffected segregations.
- **Moderate** ✅：2 affected segregations or 1 affected segregation AND ≥ 5 unaffected segregations or ≥ 10 unaffected segregations.
- **Supporting** ✅：1 affected segregation or ≥ 5 unaffected segregations.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Strong** ✅：For missense variants: REVEL score of ≥ 0.932
- **Moderate** ✅：For missense variants: REVEL score of 0.773-0.931
- **Supporting** ✅：For missense variants: SpliceAI ≥ 0.2 OR REVEL score of 0.644-0.772

For missense variants where REVEL scores are not available (e.g. due to changes of >1 nucleotide): AlphaMissense ≥ 0.792（v2.0 新增回退，暂按 PP3_Supporting 适用，待 VCEP 大样本验证）。

For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI ≥ 0.2

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Allele frequency ≥ 0.05 in population databases.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency is ≥ 0.01 (1%) in population databases.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Non-segregations with PCG, ASD or JOAG. Use caution and consider phenotypes of the affected segregations, age at diagnosis and pedigree structure before applying to non-segregations with JOAG or POAG.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Strong** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of ≤ 0.016
- **Moderate** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of 0.017-0.183
- **Supporting** ✅：For missense variants: SpliceAI ≤ 0.1 AND REVEL score of 0.184-0.290

For missense variants where REVEL scores are not available (e.g. due to changes of >1 nucleotide): AlphaMissense ≤ 0.169（v2.0 新增回退，暂按 BP4_Supporting 适用，待 VCEP 大样本验证）。

For all other variants (not meeting PVS1 or PM4) located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI ≤ 0.1

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：Applies to intronic/noncoding variants outside the donor/ acceptor splice region (intronic variants at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon if BP4 is met.

### 不适用证据码
PS4、PM6、PP2、PP4、PP5、BS2、BS3、BP1、BP2、BP3、BP5、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN104)

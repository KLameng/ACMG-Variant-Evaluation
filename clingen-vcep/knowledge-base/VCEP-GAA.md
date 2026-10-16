# ClinGen VCEP基因特异性规范：GAA

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN010 — Lysosomal Diseases Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0009290**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease or in frame loss of an exon that contains residues involved in the active site of GAA.
 * Any nonsense, frameshift, or splice variant creating a premature stop codon before codon 916.
 * In frame deletions of an entire exon containing critical active site/substrate binding residues (exons 8 and 10), or for which another variant removing the exon is known to be pathogenic (exons 2 and 18).
- **Strong** ✅：Null variant in a gene where loss of function is a known mechanism of disease.
 *  In frame loss of an exon which is part of the catalytic barrel domain and contains pathogenic/likely pathogenic nontruncating variants (exons 6 and 9).
 * Initiator codon variant.
- **Moderate** ✅：Null variant in a gene where loss of function is a known mechanism of disease.
 * Premature termination codon in the 3’ end of GAA (3’ to codon 916), not predicted to be detected by nonsense-mediated decay.
 * Predicted exon-skipping due to canonical splice variant or exon deletion resulting in an in frame deletion of <10% of the gene product (exons 17, 19, and 20).

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.
 * RT-PCR evidence of mis-splicing for non-canonical intronic variants with no evidence of normal splice products.
- **Moderate** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.
 * <5% wild type GAA activity when the variant is expressed in a heterologous cell type and evidence of abnormal GAA synthesis and/or processing.
 * RT-PCR evidence of mis-splicing for non-canonical intronic variants with evidence of normal splice products.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies supportive of a damaging effect.
 * <30% wild type GAA activity when the variant is expressed in a heterologous cell type.
 * RT-PCR evidence of mis-splicing for non-canonical intronic variants with evidence of normal splice products.

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.
 * Missense substitution or in frame deletion of residues important in the active site architecture and substrate binding of GAA: D282, W376, D404, L405, I441, W481, W516, D518, M519, R600, W613, D616, W618, F649, L650, H674.

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Moderate** ✅：Low frequency in population databases.
 * Minor allele frequency <0.1% (0.001) in all continental populations with >2000 alleles in gnomAD.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：Detected in trans with a pathogenic variant. Points-based system. See main specifications document.
- **Strong** ✅：Detected in trans with a pathogenic variant. Points-based system. See main specifications document.
- **Moderate** ✅：Detected in trans with a pathogenic variant. Points-based system. See main specifications document.
- **Supporting** ✅：Detected in trans with a pathogenic variant. Points-based system. See main specifications document.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a nonrepeat region or stop-loss variants.
 * In frame deletion/insertions of two or more amino acids but less than one exon.
- **Supporting** ✅：Protein length changes due to in-frame deletions/insertions in a nonrepeat region or stop-loss variants.
 * In frame deletion/insertions of one amino acid.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change determined to be 'likely pathogenic' has been seen before.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product.
 * REVEL score >0.7 for missense variants.
 * In frame deletion or insertion predicted deleterious by 2 out of 3 tools (PROVEAN, MutationTaster, MutPred-InDel).
 * Predicted impact on splicing by SpliceAI (score >0.5).

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：Phenotype specific for disease with single genetic etiology.
 * Points-based system. See main specifications document
- **Supporting** ✅：Phenotype specific for disease with single genetic etiology.
 * Points-based system. See main specifications document

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：Common in population databases.
 * Highest minor allele frequency >0.01 (>1%) in any continental population in gnomAD with >2000 alleles.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：Allele frequency greater than expected for disease.
 * Highest minor allele frequency >0.005 (>0.5%) in any continental population in gnomAD with >2000 alleles.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in the homozygous state in a healthy adult.
 * Homozygous individual of any age with normal GAA activity.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Supporting** ✅：Well-established in vitro or in vivo functional studies shows no damaging effect on protein function.
 * >50% activity when the variant is expressed in a heterologous cell type, or >30% activity if there is also evidence of normal synthesis and processing.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Supporting** ✅：Observed in cis with a pathogenic variant.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product.
 * REVEL score <0.5 for missense variants.
 * In frame deletion or insertion predicted benign by PROVEAN, MutationTaster, and MutPred-InDel.
 * No predicted impact on splicing by SpliceAI (score <0.2)

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### 不适用证据码
PS2、PS4、PM6、PP1、PP2、PP5、BS4、BP1、BP3、BP5、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN010)

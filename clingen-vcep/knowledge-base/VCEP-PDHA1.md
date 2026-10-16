# ClinGen VCEP基因特异性规范：PDHA1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 规范版本：未随包声明（数据日期：2026-06-13；真实官方 CSpec 版本号见 ClinGen 官网 cspec.genome.network，使用前请核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN014 — Mitochondrial Diseases Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0019169**（遗传方式：未指定）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Applied per PVS1 flowsheet of Abou Toyoun et al.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Strong** ✅：De novo in a patient with the disease and no family history

#### PM1
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
- **Moderate** ✅：Located in one of the following functional domains:
 * thiamine pyrophosphate (TPP) binding site (aa positions 118Y, 119R, 165G, 167V, 195G, 196D, 197G, 198A, 225N, 227Y, 292H).
 * α β heterodimer interface (aa positions 160F, 162G, 164N, 169A, 172P, 173L, 176G, 177I, 179L, 180A,183Y, 202G,203Q, 209N, 210M, 213L).
 * α2 β2 heterotetramer interface (aa positions 88R, 140G, 165G, 166I, 197G, 199A, 200N, 201Q, 202G, 205F, 209N, 213L, 228G, 229M, 230G, 231T, 245R, 296D, 300S).
  * Phosphorylation loop region (aa positions 287Y, 288R, 289Y, 290H, 291G, 292H, 293S, 295S, 296D, 297P, 298G, 299V, 300S, 301Y, 302R, 303T, 304R, 305E, 314S, 315D, 316P).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Moderate** ✅：0.0000092 (<0.00092%)

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** ✅：Protein length changes as a result of in-frame deletions/insertions in a nonrepeat region or stop-loss variants

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：De novo in a patient with the disease and no family history
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Supporting** ✅：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：No gene-specific predictors; agree to utilize REVEL, with thresholds of >0.75 and <0.15 for PP3 and BP4, respectively

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：One of the following criteria are met: 
(1) Pyruvate radioactive enzyme assay showing decreased (as defined as <3rd percentile of controls) for PDC, activated and decreased ratios (PDC/E3 and/or PDC/CS) in fibroblasts, muscle, and/or lymphocytes; 
(2) other assays showing decrease in PDC activity (ie: western blot, immunocapture, and activity; commercial kits for research); 
(3) abnormally high pyruvate and/or pyruvate/lactate ratio

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：>0.00092 (>0.092%)

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：>0.000092 (>0.0092%)

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in at least two healthy male adults. Note: Individual’s phenotype is well-characterized (not just seen in database of presumed healthy individuals) AND/OR ≥16 hemizygotes in gnomAD
- **Supporting** ✅：Observed in 4-15 hemizygotes in gnomAD AND/OR Pyruvate radioactive enzyme assay showing normal (defined as >3rd percentile of controls) for PDC, activated and normal ratios (PDC/E3 and/or PDC/CS) in fibroblasts with no evidence of skewed X-inactivation in fibroblasts.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected and/or treated members of a family.

#### BP3
- 默认强度：Benign Supporting
- ACMG原始定义：In frame-deletions/insertions in a repetitive region without a known function.
- **Supporting** ✅：In-frame deletions/insertions in a repetitive region without a known function

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：No gene-specific predictors; agree to utilize REVEL, with thresholds of >0.75 and <0.15 for PP3 and BP4, respectively

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved

### 不适用证据码
PS3、PS4、PM3、PP2、PP5、BS3、BP1、BP2、BP6
### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN014)

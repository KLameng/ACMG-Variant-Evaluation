# ClinGen VCEP基因特异性规范：ATM

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN020 — Hereditary Breast, Ovarian and Pancreatic Cancer Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0700270**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0008840**（遗传方式：Autosomal recessive inheritance）
- **MONDO:0018266**（遗传方式：Autosomal recessive inheritance）

### 通用说明
> 官网版本：Version 1.6（Released 9/18/2026；HBOC VCEP）。
> Release notes v1.6：
> - 进一步澄清 RNA 数据存在时 BP4 的使用（BP4+BP7(RNA) 允许联用，v1.5 曾有冲突表述）。
> - 补充 gnomAD 数据使用指引。
> - 澄清 PS4 中的布尔操作符。
> - 澄清 PM5_Supporting 纳入 p.Arg3047*。
> - 澄清可满足 PM5_Supporting 的其他变异类型。
> - 更正 PM3/BP2 附件中的复制粘贴笔误。
> - 其余规范与附件无变更。

历史说明（v1.5）：按各证据码（PVS1、PS1、PS3/BS3、PM3/BP2）分别上传支持文档，替代原合并包；将旧包中 PS3 说明移至 CSPEC；v1.5 未改动任何规范。

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** 📋：Use ATM PVS1 Decision Tree
- **Strong** 📋：Use ATM PVS1 Decision Tree.
- **Moderate** 📋：Use ATM PVS1 Decision Tree.
- **Supporting** 📋：Use ATM PVS1 Decision Tree

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：*   Use for missense changes as long as splicing is ruled-out for both alterations. 
*   Use ATM PS1 Splicing table for splicing variants with similar predictions or observations of splice defect.
- **Moderate** 📋：Use ATM PS1 Splicing table for splicing variants with similar predictions or observations of splice defect.
- **Supporting** 📋：Use ATM PS1 Splicing table for splicing variants with similar predictions or observations of splice defect.

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** 📋：Do not use as strong.
- **Moderate** 📋：Use when a variant fails to rescue both an ATM specifc feature (e.g. phosphorylation of ATM-specific targets) AND radiosensitivity.
- **Supporting** 📋：Use when a variant fails to rescue an ATM specifc feature, only (e.g. phosphorylation of ATM-specific targets). Do not use for radiosensitivity-only as that is not a feature specific to ATM deficiency

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** 📋：Case-control studies; p-value ≤.05 AND (Odds ratio, hazard ratio, or relative risk  ≥2 OR lower 95% CI ≥1.5).

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** 📋：Frequency **≤.001%** in gnomAD subpopulation with the highest frequency

Exception: If >0.001% but n=1 in a single subpopulation (not present in any other subpopulation), that is sufficiently rare and PM2\_supporting would apply.

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** 📋：PM3\_VeryStrong **≥ 8** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Strong** 📋：PM3\_Strong = **4** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Moderate** 📋：PM3 = **2** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Supporting** 📋：PM3\_Supporting = **1** point

See ATM PM3/BP2 table for approach to assign points per proband.

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Moderate** 📋：Use for stop-loss variants.

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** 📋：*   DNA 变异：适用于所有接受 PVS1（须为 Very Strong）、且无义突变密码子位于 p.Leu3048 上游的 NMD 倾向截短/移码变异（v1.6 边界由 p.Arg3047 上游改为 p.Leu3048 上游，即纳入 p.Arg3047*）。
*   剪接变异：仅适用于接受 PVS1(RNA)（须为基于高质量 RNA 数据的 Very Strong）、且无义突变密码子位于 p.Leu3048 上游的 NMD 倾向截短变异；若无 RNA 数据的预测性剪接效应，或 PVS1(RNA) 为降权强度，则不适用。

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** 📋：AR Condition: Segregation in ≥3 affected relatives
- **Moderate** 📋：AR Condition: Segregation in 2 affected relatives
- **Supporting** 📋：AR Condition: Segregation in 1 affected relative

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: REVEL **\>.7333**
*   Splicing: Predicted impact via splicing (SpliceAI **≥0.2**) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** 📋：Grpmax Filtering AF **\>.5%** in gnomAD v4 dataset

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** 📋：Grpmax Filtering AF **\>.05%** in gnomAD v4 dataset

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Moderate** 📋：Use when a variant rescues both an ATM specifc feature (e.g. phosphorylation of ATM-specific targets) AND radiosensitivity.
- **Supporting** 📋：Use when a variant rescues EITHER an ATM specifc feature OR rescues radiosensitivity.

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** 📋：BP2\_Strong **≤ -4** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Moderate** 📋：BP2\_Moderate = **\-2** points

See ATM PM3/BP2 table for approach to assign points per proband.
- **Supporting** 📋：BP2 = **\-1** point

See ATM PM3/BP2 table for approach to assign points per proband.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** 📋：*   Missense: REVEL score **≤.249**
*   Splicing: No predicted impact via splicing (SpliceAI **≤0.1**).
*   **BP4+BP7(RNA) 联用澄清（v1.6）**：当 RNA 数据显示无变异特异性影响时，BP4 可与 BP7_Variable(RNA)（即观察到 RNA 无缺陷）联用，以达到可能良性（Likely Benign）；BP4 的剪接预测权重不得与其他蛋白证据合并。当 RNA 数据显示存在显著变异特异性影响时，不得同时使用 PVS1(RNA) 与 PP3 或 BP4.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Strong** 📋：BP7\_Strong(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.
- **Moderate** 📋：BP7\_Moderate(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.
- **Supporting** 📋：*   BP7: Use for synonymous and deep intronic variants defined as further than (but not including) +7 and further than (but not including) -21 at donor and acceptor sites, respectively.
*   BP7(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality.

### 组合规则（Rules for Combining Criteria；官网 v1.6，Richards 2015 组合规则面板）

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
2. 1 Strong AND 1 Moderate
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
3. 1 Strong

### 不适用证据码
PS2、PM1、PM6、PP2、PP4、PP5、BS2、BS4、BP1、BP3、BP5、BP6
### 参考附件
- [ATM PVS1](https://cspec.genome.network/cspec/File/id/b88cc721-fbad-4a5a-9f8a-1660154630e1/data)
- [ATM PS1](https://cspec.genome.network/cspec/File/id/8adfd439-cb2d-4c79-9201-8e221313dd13/data)
- [ATM PM3_BP2](https://cspec.genome.network/cspec/File/id/c5546d50-27e9-4457-bcc9-4c4a04201a31/data)
- [ATM PS3_BS3](https://cspec.genome.network/cspec/File/id/9de6dffe-73c9-4a08-aa80-3a06ca6bcd00/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN020)

# ClinGen VCEP基因特异性规范：MTM1

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> 官网版本：GN149 v1.0（Released，DOI: 10.5281/zenodo.21434749，2026-10-09 官网实页核验）
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN149 — Congenital Myopathies Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0018947**（遗传方式：X-linked inheritance）

### 通用说明
           

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：See PVS1 flowchart
- **Strong** ✅：See PVS1 flowchart
- **Moderate** ✅：See PVS1 flowchart
- **Supporting** ✅：See PVS1 flowchart

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：No change - use as originally described
- **Strong** ✅：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength.
- **Moderate** ✅：Where indicated, some of the assays from PS3\_Supporting may be stacked to reach a Moderate Strength
- **Supporting** ✅：Five specific assays are currently suggested to be applied at Supporting:

1.  Phosphatase Activity: An abnormal readout consists of reduced phosphatase activity (measured via levels of PtdIns and PtdIns5p or increased levels of precursors)
2.  Myotubularin Localization**\*\***: An abnormal readout consists of altered localization (presence in spots/aggregates/extensions, loss of cytoplasmic localization)
3.  Myotubularin Translocation**\*\***: An abnormal readout consists of loss of MTM1 recruitment to late endosomal compartment following EGF stimulation
4.  Intracellular Trafficking (Trafficking of endosomal cargo is thought to require phosphoinositide conversion and may be disrupted by defective MTM1 activity): An abnormal readout consists of reduced localization/trafficking of receptor proteins
5.  Protein and Lipid Association: An abnormal readout consists of decreased association with known binding partner (BIN1, Desmin, hVPS34-PI 3-Kinase, MTMR12, Phosphoinositide, or EEA Membrane association)

**\*\*These two assays should not be stacked because they may not be assessing independent biological function**

If not listed above, it is acceptable to use PS3\_Supporting for other functional analyses if

*   The assay has been validated by a known pathogenic and benign variant AND
*   There is plausible reason that the function the assay is testing relates to the phenotype AND
*   The assay conditions are likely to mimic the physiological environment.

#### PS4
- 默认强度：Pathogenic Strong
- ACMG原始定义：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- **Strong** ✅：The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**5+ cases**
- **Moderate** ✅：3-4 cases
- **Supporting** ✅：2 cases

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：PM2\_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is absent (1 observation allowed in females only)

#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Supporting** ✅：No change - use as originally described

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Supporting** ✅：No change - use as originally described

#### PM6
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Assumed de novo, but without confirmation of paternity and maternity.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：Assumed de novo, but without confirmation of paternity and maternity.
- **Supporting** ✅：No change - use as originally described

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：At least five segregations
- **Moderate** ✅：3-4 segregations
- **Supporting** ✅：2 segregations

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PP3 is met if the REVEL score ≥ 0.7 or if the variant is predicted to impact splicing using SpliceAI score ≥0.5

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Supporting** ✅：**Affected Males (must be negative for BIN1, RYR1, and DNM2 variants)**

*   Muscle biopsy with rounded muscle fibers with a single centrally located nucleus surrounded by a halo devoid of contractile elements, but containing mitochondria

**Carrier Females (a panel test for neuromuscular disease to rule out other causes)**

*   Observation of myopathy (may be asymmetric) AND at least 1 other feature
    *   Unilateral skeletal asymmetry
    *   Narrow, elongated face
    *   High arched palate

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.000016**. All continental gnomAD populations used should have at least 2000 alleles and >1 observation.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0000016**. All continental gnomAD populations used should have at least 2000 alleles and >1 observation.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：No change - use as originally described

#### BP2
- 默认强度：Benign Supporting
- ACMG原始定义：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc) Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

BP4 is met if the REVEL score ≤ 0.15 or if the variant is not predicted to impact splicing using SpliceAI.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：No change - use as originally described
- **Moderate** ✅：No change - use as originally described
- **Supporting** ✅：Variant found in a case with an alternate molecular basis for disease.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

### 组合规则（Rules for Combining Criteria）

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
7. 1 Strong AND 2 Moderate

**Benign（良性）**
1. ≥ 2 Strong
2. 1 Stand Alone

**Likely Benign（可能良性）**
1. 1 Strong AND 1 Supporting
2. ≥ 2 Supporting

### 不适用证据码
PM1、PM3、PP2、PP5、BS3、BP1、BP3、BP6
### 参考附件
- [MTM1 approved functional assays](https://cspec.genome.network/cspec/File/id/073ec75e-3ed2-47c0-86fd-70f38df2a490/data)
- [MTM1 PVS1 guidance](https://cspec.genome.network/cspec/File/id/58e20b58-b1dc-4279-913b-4fe2c6f62173/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN149)

# ClinGen VCEP基因特异性规范：MSH6

> 来源：ClinGen Sequence Variant Interpretation (SVI) Criteria Specification Repository
> 数据日期：2026-06-13
> ⚠️ 智能分析结果，仅供参考。临床变异评级请以ClinGen官方最新版本为准。

## 规范 1：GN138 — InSiGHT Hereditary Colorectal Cancer/Polyposis Variant Curation Expert Panel

> 官网版本：Version 2.0；DOI: 10.5281/zenodo.21434726；核验日期：2026-10-09

### 覆盖疾病
- **MONDO:0005835**（遗传方式：Autosomal dominant inheritance）
- **MONDO:0010159**（遗传方式：Autosomal recessive inheritance）

### 基因特异性证据规则

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Nonsense/frameshift variant introducing Premature Termination Codon (PTC)<sup>a</sup> ≤ codon 1341 in _MSH6_. Refer to Appendix for details.

OR

Large genomic alterations<sup>a</sup> of single or multi-exon size.

OR

Variants at IVS±1 or IVS±2​<sup>a,c</sup> where exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration). If exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function<sup>b</sup> then use PVS1\_Strong. If exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD then use PVS1\_Moderate.

OR

Variants where mRNA assays using RNA derived from patient constitutional biological samples indicate that the variant allele results in a splicing aberration (with evidence that the variant allele produces no full-length/reference transcript) leading to premature stop codon or in-frame deletion disrupting a functional domain<sup>b</sup> or protein conformation. Splicing aberration must be confirmed in a minigene assay or an additional RNA assay from an independent laboratory if it is a non-canonical splice site variant.
- **Strong** ✅：Variants in the initiation codon of _MSH6_.

OR 

Presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications.

OR

G>non-G at last base of exon if first 6 bases of the intron are not GTRRGT. If confirmed to cause a splice defect, then PVS1 should be used instead.

OR

Variants at IVS±1 or IVS±2​<sup>a,c</sup> where exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function<sup>b</sup>. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration).
- **Moderate** ✅：Nonsense/frameshift variant introducing premature termination codon  between codons 1342 & 1360 in MSH6. Refer to Appendix for details.

#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change previously established by this VCEP as Pathogenic (not a predicted or confirmed splice defect).

OR

Variants affecting the same non-canonical splice nucleotide as a confirmed Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.
- **Moderate** ✅：A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change as a previously established Likely Pathogenic missense variant with normal RNA result\*, and PM2\_supporting is met.

\*Otherwise, if the previously established Likely Pathogenic missense variant truly is a splice defect, the new missense variant also has to be investigated on a functional level for RNA splicing.

OR

Variants affecting the same non-canonical splice nucleotide as a Likely Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.

#### PS2
- 默认强度：Pathogenic Strong
- ACMG原始定义：De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **Very Strong** ✅：≥ 4 _de novo_ points
- **Strong** ✅：2 - 3.5 _de novo_ points
- **Moderate** ✅：1 - 1.5 _de novo_ points
- **Supporting** ✅：0.5 _de novo_ points

#### PS3
- 默认强度：Pathogenic Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.
- **Strong** ✅：Calibrated functional assays with functional odds forpathogenicity > 18.7
- **Moderate** ✅：Calibrated functional assays with functional odds for pathogenicity >4.3 and \<= 18.7

OR 

MMR function defect following functional assay flowchart\*

OR 

Variants with monoallelic expression: complete loss of expression (\<10% of wild-type in cDNA without puromycin) of the variant allele. Full-length transcript should be analysed with and without NMD block.
- **Supporting** ✅：Calibrated functional odds for pathogenicity >2.08 and \<= 4.3

#### PM2
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.
- **Supporting** ✅：Absent/extremely rare allele frequency \<0.00002 (\<1 in 50,000 alleles ) in gnomAD v4 dataset

#### PM3
- 默认强度：Pathogenic Moderate
- ACMG原始定义：For recessive disorders, detected in trans with a pathogenic variant
Note: This requires testing of parents (or offspring) to determine phase.
- **Very Strong** ✅：≥ 4 points
- **Strong** ✅：2 - 3.5 points
- **Moderate** ✅：1 - 1.5 points
- **Supporting** ✅：\= 0.5 points

#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5\_Supporting if other variant is Likely Pathogenic due to a missense alteration.
- **Supporting** ✅：Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5\_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration.

#### PP1
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.
- **Strong** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> >18.7​ in ≥2 families.
- **Moderate** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>​f</sup> >4.3 & ≤18.7.
- **Supporting** ✅：Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> >2.08 & ≤4.3.

#### PP3
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.
- **Moderate** ✅：Missense variant with HCI prior probability for pathogenicity >0.81 as per [https://hci-priors.hci.utah.edu/PRIORS](https://hci-priors.hci.utah.edu/PRIORS)
- **Supporting** ✅：Missense variant with HCI prior probability for pathogenicity >0.68 & ≤0.81 as per [https://hci-priors.hci.utah.edu/PRIORS](https://hci-priors.hci.utah.edu/PRIORS) 

OR

Predicted splice defect for non-canonical splicing nucleotides using SpliceAI with delta score >= 0.2 as per Walker et al 2023.

#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Strong** ✅：≥3 independent CRC/Endometrial MSI-H tumors in ≥2 families using a standard panel of 5-10 markers​<sup>e</sup> ​or tumor genome **and/or**​ loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4\_Strong.  Independent tumors can be from the same patient/family.
- **Moderate** ✅：2 independent CRC/Endometrial MSI-H tumors using a standard panel of 5-10 markers​<sup>e</sup> or tumor genome ​**and/or**​ loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4\_Moderate.
- **Supporting** ✅：1 CRC/Endometrial MSI-H tumor using a standard panel of 5-10 markers<sup>e</sup> or tumor genome ​**and/or**​ loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4.

#### BA1
- 默认强度：Benign Stand Alone
- ACMG原始定义：Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
- **Stand Alone** ✅：GnomAD v4 Grpmax filtering allele frequency ≥ 0.0022 (0.22%) and variant is excluded as founder pathogenic variant.

#### BS1
- 默认强度：Benign Strong
- ACMG原始定义：Allele frequency is greater than expected for disorder.
- **Strong** ✅：GnomAD v4 Grpmax filtering allele frequency ≥ 0.00022 and \< 0.0022 (0.022-0.22%) and variant is excluded as founder pathogenic variant.

#### BS2
- 默认强度：Benign Strong
- ACMG原始定义：Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.
- **Strong** ✅：Co-occurrence _​in trans_ with a known pathogenic sequence variant in the same gene in a patient with colorectal cancer after age 45 (or other LS cancer above the median age of onset for that cancer in LS<sup>​d​</sup>), and who has no previous or current evidence of clinical manifestations of CMMRD as per Aronson et al 2022 (Refer to 'Table for CMMRD diagnosis.pdf'). Confirmation of phase requires testing of parents or offspring.

#### BS3
- 默认强度：Benign Strong
- ACMG原始定义：Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.
- **Strong** ✅：Calibrated functional assays with functional odds for Pathogenicity ≤ 0.05

OR

Synonymous substitutions and intronic variants with no associated mRNA aberration (either splicing or allelic imbalance) as determined by laboratory assays conducted with nonsense-mediated decay inhibition. Whenever abnormal transcripts are identified at similar levels in controls they will be considered naturally occurring isoforms and not mRNA aberrations.
- **Supporting** ✅：Calibrated functional assays with functional odds for Pathogenicity >0.05 & ≤0.48

OR

Variant-specific proficient function in protein and mRNA-based lab assays as per MMR functional assay flowchart.

#### BS4
- 默认强度：Benign Strong
- ACMG原始定义：Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.
- **Strong** ✅：Lack of co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> \<0.05​.
- **Supporting** ✅：Lack of co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio<sup>f</sup> >0.05 & ≤0.48.

#### BP4
- 默认强度：Benign Supporting
- ACMG原始定义：Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc)
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Missense variant with HCI-prior probability of pathogenicity \<0.11 as per https://hci-priors.hci.utah.edu/PRIORS

OR

For intronic and synonymous variants: SpliceAI predicts no splicing impact with delta score \<= 0.1 as per Walker et al 2023.

#### BP5
- 默认强度：Benign Supporting
- ACMG原始定义：Variant found in a case with an alternate molecular basis for disease.
- **Strong** ✅：​≥ 4 tumors: CRC/Endometrial tumors with MSS ​and/or​ no ​loss of MMR protein expression​ ​and/or LS spectrum tumors<sup>d</sup> with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation

OR

≥2 BRAF V600E (CRC only)/_MLH1_ methylation (in LS spectrum tumor only) with MSI-H/_MLH1_ loss.
- **Supporting** ✅：2 or 3 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors<sup>d</sup> with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation.

OR 

1 BRAF V600E (Colon only)/_MLH1_ methylation (in LS spectrum tumor only) with MSI-H/_MLH1_ loss.

#### BP7
- 默认强度：Benign Supporting
- ACMG原始定义：A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.
- **Supporting** ✅：A synonymous (silent) or intronic variant at or beyond -21/+7 (5′/3′ exonic). Variants may satisfy both BP7 and BP4.

### 组合规则
- **Pathogenic**：
  - 1 Very Strong AND ≥ 1 Strong
  - 1 Very Strong AND ≥ 2 Moderate
  - 1 Very Strong AND 1 Moderate AND 1 Supporting
  - 1 Very Strong AND ≥ 2 Supporting
  - ≥ 2 Strong
  - 1 Strong AND ≥ 3 Moderate
  - 1 Strong AND 2 Moderate AND ≥ 2 Supporting
  - 1 Strong AND 1 Moderate AND ≥ 4 Supporting
- **Likely Pathogenic**：
  - 1 Very Strong AND 1 Moderate
  - 1 Strong AND 1 Moderate
  - 1 Strong AND ≥ 2 Supporting
  - ≥ 3 Moderate
  - 2 Moderate AND ≥ 2 Supporting
  - 1 Moderate AND ≥ 4 Supporting
  - 1 Strong AND 2 Moderate
- **Benign**：
  - ≥ 2 Strong
  - 1 Stand Alone
- **Likely Benign**：
  - 1 Strong AND 1 Supporting
  - ≥ 2 Supporting

### 不适用证据码
PS4、PM1、PM4、PM6、PP2、PP5、BP1、BP2、BP3、BP6
### 参考附件
- [MMR Functional assay flowchart](https://cspec.genome.network/cspec/File/id/5dbacc58-9a5d-45bd-bff0-e345c15f9383/data)
- [Functional assay SVI documentation](https://cspec.genome.network/cspec/File/id/bf9feb99-0fbf-4793-98aa-2d7789617d62/data)
- [Table for CMMRD diagnosis](https://cspec.genome.network/cspec/File/id/84297b01-9a41-4b27-95ff-b3e310d65ea2/data)
- [Appendix](https://cspec.genome.network/cspec/File/id/b18c8c73-f4f5-4828-bcce-ce7f24a83671/data)
- [MMR functional domains](https://cspec.genome.network/cspec/File/id/d106852b-e2a5-4ce6-a8fc-711f793359b0/data)
- [MMR PVS1 Decision Tree](https://cspec.genome.network/cspec/File/id/60f0a036-9884-4b45-85c6-158f3dde7711/data)
- [VCEP pilot variants - MMR](https://cspec.genome.network/cspec/File/id/89ddc569-619a-4f57-810c-a0d3792c97a0/data)

### 官方链接
- [ClinGen CSpec 文档页面](https://cspec.genome.network/cspec/ui/svi/doc/GN138)

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN095 — Cardiomyopathy Variant Curation Expert Panel

### 致病性证据规则（PS/PM/PP）

#### PVS1
- 默认强度：Pathogenic Very Strong
- ACMG原始定义：Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
 * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
 * Use caution interpreting LOF variants at the extreme 3’ end of a gene.
 * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
 * Use caution in the presence of multiple transcripts.
- **Very Strong** ✅：Currently only applicable to _MYBPC3_ where LOF is an established disease mechanism.

Refer to SVI guidance for the interpretation of this criterion (Abou Tayoun _et al._ 2018[<sup>1</sup>](#pmid_30192042)).

[SpliceAI](https://spliceailookup.broadinstitute.org)[<sup>2</sup>](#pmid_30661751) is recommended for evaluation of predicted splice impacts.

Factors to consider when assessing the consequences of putative LOF variants in the _MYBPC3_ gene:

1.  Codon p.1254 is located 50 nucleotides upstream of the most 3' exon-exon junction (exon 33:34) in _MYBPC3._ As such, nonsense variants introducing a premature termination codon after this point may escape nonsense mediated decay (NMD) and consequently not result in protein haploinsufficiency (Nagy & Maquat 1998[<sup>3</sup>](#pmid_9644970)).
2.  When assessing variants predicted to affect splicing of micro-exons (exons 10, 11 and 14), be aware that _in silico_ splice site predictions may be less reliable in this setting and the consequences of variants affecting splice sites at these exons less predictable (Frank-Hansen _et al._ 2008[<sup>4</sup>](#pmid_18337725)).

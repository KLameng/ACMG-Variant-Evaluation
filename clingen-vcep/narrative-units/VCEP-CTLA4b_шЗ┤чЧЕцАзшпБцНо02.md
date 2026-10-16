> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Strong** ✅：*   For truncating variants located in the isoform-specific exon 3, apply PVS1 if nonsense mediated decay is predicted (truncation at codon 172 or lower) and PVS1\_strong if NMD is not predicted (truncation at codon 173 or higher). While this recommendation already matches the SVI guidance, it is specified here because similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452), despite the fact that exon 3 is omitted from an alternative transcript (NM\_001037631.3) that encodes the soluble isoform (PMID: 40168991).
- **Moderate** ✅：*   Apply PVS1\_Moderate for nonsense or frameshift variants that introduce a premature stop codon between codons 202 and 223 of CTLA4, as these are predicted not to undergo nonsense-mediated decay and to result in C-terminal truncation of less than 10% of the protein product.
- **Supporting** ✅：*   Apply PVS1\_Supporting for initiation codon variants in accordance with Tayoun et al (PMID: 30192042). There are no known alternative start codons and the closest potential in-frame start codon is at codon 38. No disease-causing missense variants have yet been identified in the N-terminal region between codons 1 and 37.


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：*   Use PS1 for missense variants when other variant was classified pathogenic by VCEP standards without using PS1.
*   Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.

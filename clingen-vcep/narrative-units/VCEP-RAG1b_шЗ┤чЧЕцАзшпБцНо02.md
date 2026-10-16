> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, at least one pathogenic variant **must be** present downstream in order to apply PVS1\_Strong.
- **Moderate** ✅：Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:

*   For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, when at least one pathogenic variant is **not** present downstream, downgrade to PVS1\_Moderate.


#### PS1
- 默认强度：Pathogenic Strong
- ACMG原始定义：Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T.

Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for _RAG1._
- **Moderate** ✅：It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T

Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for _RAG1._


#### PS2
- 默认强度：Pathogenic Strong

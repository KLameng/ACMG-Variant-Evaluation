> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.
- **Supporting** ✅：Missense variant with “MAPP/PP2 Prior P” score  \<0.11 from [http://hci-lovd.hci.utah.edu/variants.php?select_db=PMS2_priors&action=search_unique](http://hci-lovd.hci.utah.edu/variants.php?select_db=PMS2_priors&action=search_unique) 

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

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count _in silico_ predictor data) but can be used together with PM1.
*   In-frame insertions or deletions of any size will meet PM4 at the moderate (default) level, due to the greater importance of the location of the variant rather than the size.


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Moderate** ✅：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*   Caveat: Residue must be highly conserved across all 5 human KCNQ paralogues in order to be considered for PM5. To confirm conservation, curators should access paralogue data and regions of alignment and non-alignment between KCNQ1 and KCNQ2, KCNQ3, KCNQ4, and KCNQ5  at the site below: [https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1](https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1).
*   Poor conservation (ineligibility for PM5) is defined whenever 1 or more KCNQ’s show a different amino acid at the position. 
*   Comparison variants must have a Pathogenic or Likely Pathogenic classification reached using these VCEP-specified rules without using PM5.
*   Variants at any codon where a likely benign / benign variant has been classified by the group are not eligible for PM5.
*   SpliceAI must be used to examine both variants for similar predicted effect or lack of effect on splicing (SpliceAI Δ score \<0.2).
*   Not used at the PM5\_Strong level.


#### PM6
- 默认强度：Pathogenic Moderate

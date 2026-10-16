> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

- **Supporting** 📋：**PM2\_Supporting:** Minor allele frequency  ≤ 0.00005 with at least 2000 alleles tested around and 20x coverage at the position.

Caveat: 

\*We recommend evaluating PM2\_supporting using the GrpMax FAF when it is available in gnomAD v4.1.0. If a GrpMax FAF value is not available, we recommend requiring that all subpopulations meet the PM2\_supporting threshold.


#### PM4
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.
- **Strong** 📋：**For in-frame/indel variants:**

**PM4\_strong:** In-frame deletion/insertion impacting at least one of the following AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.

**For stop loss variants:**

**PM4:** Stop-loss variant causing a protein extension.
- **Moderate** 📋：In-frame deletion/insertion impacting at least one of the following amino acid residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.
- **Supporting** 📋：**PM4\_Supporting:**

In-frame deletion/insertion impacting at least one of the other AA residues 89-204 within the RHD.


#### PM5
- 默认强度：Pathogenic Moderate
- ACMG原始定义：Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.
- **Strong** 📋：**PM5\_Strong:** Missense change at an AA residue where ≥ 2 different missense changes which have been determined to be pathogenic before (after accounting for Grantham scores).

Caveats:

\*Of note, the variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.


> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

## 规范 1：GN008 — Myeloid Malignancy Variant Curation Expert Panel

### 覆盖疾病
- **MONDO:0011071**（遗传方式：Autosomal dominant inheritance）

### 通用说明
Release notes:
(1) New gnomAD MAF threshold for PM2_supporting ≤ 0.00005 to account for larger population in gnomAD v4.
(2) Upgraded strength of PM1 to PM1_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added a caveat to not use PM5/PS1 at any level if PM1 was applied.
(3) Upgraded strength of PM4 to PM4_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added an allowance to use PM4 for stop-loss variants.
(4) Established PVS1_variable (RNA) and BP7_variable (RNA) to be used when RNA data is available for splicing variants. PS1 is now able to be used for splicing variants with the same predicted splicing event as a known pathogenic/likely pathogenic splicing variant.
(5) Conservation data is no longer considered when applying BP7. BP7 is limited to intronic variants, and synonymous variants which don’t occur in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site.
(6) Revised PM5 to account for Grantham scores when evaluating missense variants.

### 不适用证据码
PM3、PP2、PP4、PP5、BS2、BP1、BP3、BP5、BP6

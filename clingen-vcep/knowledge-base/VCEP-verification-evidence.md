# VCEP知识库核实证据文件
完成日期：2026-06-14

---

## ACTA1 GN147 (AD规范) 核实证据

### 来源
- 在线官方源：https://cspec.genome.network/cspec/ui/svi/doc/GN147 (Version 2.0.0, Released 8/27/2024)
- 本地文件：./ClinGen-VCEP/knowledge-base/VCEP-ACTA1.md (规范2，从第213行开始)

### 逐条证据码对比

#### PVS1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Loss of function is not a mechanism of disease for autosomal dominant alpha-actinopathy caused by variants in ACTA1."
- 本地：不适用证据码列表包含PVS1 ✅

#### PS1 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### PS2 — 一致
- 在线 Very Strong/Strong/Moderate/Supporting 与本地完全匹配 ✅

#### PS3 — 一致
- 在线 Strong/Moderate/Supporting 三种强度的规则文本与本地完全匹配 ✅

#### PS4 — 核心阈值一致，但缺少VCEP Specifications说明文本
- 在线阈值：Strong=8, Moderate=4, Supporting=2 ✅
- **缺失**：在线版有VCEP Specifications文本："ACTA1 is associated with both autosomal recessive and autosomal dominant disease. If you are curating biallelic observations, please use the AR specifications. Cases should not be counted if there are complex phenotypic features in addition to those listed that are incompatible with ACTA1, such as neurogenic etiology, central nervous system involvement, lysosomal disorders, increased serum CK levels, or extraocular muscle weakness."
- 本地文件未收录此段VCEP Specifications说明

#### PM1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "There are no defined hotspots or critical functional domains in ACTA1 at this time."
- 本地：不适用证据码列表包含PM1 ✅

#### PM2 — 核心规则一致，但缺少VCEP Specifications说明
- 在线 Supporting 规则文本与本地匹配 ✅
- **缺失**：在线版有VCEP Specifications："If the mode of inheritance for the variant is unclear (largely with missense variants as loss of function variants are predicted to cause AR disease), use the more conservative AD cutoff for PM2_Supporting."

#### PM3 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Biallelic cases should not be counted using the ACTA1 autosomal dominant specifications."
- 本地：不适用证据码列表包含PM3 ✅

#### PM4 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### PM5 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### PM6 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### PP1 — 核心规则一致，但缺少VCEP Specifications说明
- 在线 Strong/Moderate/Supporting 规则文本与本地匹配 ✅
- **缺失**：在线版有VCEP Specifications："The segregation chart (adopted from Biesecker et al 2023 PMID:38103548) should be used to determine the strength level of the total number of segregations. The combination of PP1 and PP4 is capped at strong."

#### PP2 — 核心规则一致，但缺少Comments
- 在线 Supporting 规则文本与本地匹配 ✅
- **缺失**：在线版有Comments："NEB is not a gene that is constrained for missense variation. Hence PP2 is not applicable."（注：此条为VCEP面板级通用说明，非ACTA1特异，可酌情处理）

#### PP3 — 一致
- 在线 REVEL≥0.7, SpliceAI≥0.5 与本地匹配 ✅

#### PP4 — 有差异
- **差异1（错误添加）**：本地PP4 Strong中包含"PP1+PP4 combined cannot exceed Bayesian 5 points."，但在线版中只有"The combination of PP1 and PP4 is capped at strong."，**没有**"Bayesian 5 points"相关表述。此为本地文件额外添加的内容，在线源无此说法。
- **缺失1**：在线版有VCEP Specifications："The strength of PP4 should be determined based on the case with the most specific phenotype. It should only be applied once per variant, even if there are multiple cases that meet PP4 criteria. The combination of PP4 and PP1 is capped at strong."
- **缺失2**：在线版有Comments："PP4 is not separately applicable for case counting. However, meeting PP4 increases the weight of a case. See PS4 specifications for more information."
- Moderate和Supporting强度规则文本一致 ✅

#### PP5 — 一致（均为Not Applicable）
- 在线：Not Applicable (retired by ClinGen SVI)
- 本地：不适用证据码列表包含PP5 ✅

#### BA1 — 核心阈值一致，但缺少VCEP Specifications说明
- 在线阈值 ≥0.0000781 for AD variants 与本地匹配 ✅
- **缺失**：在线版有VCEP Specifications："If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BA1."

#### BS1 — 核心阈值一致，但缺少VCEP Specifications说明
- 在线阈值 ≥0.00000781 for AD variants 与本地匹配 ✅
- **缺失**：在线版有VCEP Specifications："If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BS1."

#### BS2 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### BS3 — 一致（均为Not Applicable）
- 在线：Not Applicable. "The VCEP has decided that lack of demonstrated effect in a functional assay should not count against the pathogenicity of an ACTA1 variant..."
- 本地：不适用证据码列表包含BS3 ✅

#### BS4 — 一致
- 在线 Strong/Moderate/Supporting 与本地完全匹配 ✅

#### BP1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Both missense and truncating variants in ACTA1 are disease-causing."
- 本地：不适用证据码列表包含BP1 ✅

#### BP2 — 一致
- 在线 Supporting 与本地匹配 ✅

#### BP3 — 一致（均为Not Applicable）
- 在线：Not Applicable. "There are no regions in ACTA1 where BP3 would apply."
- 本地：不适用证据码列表包含BP3 ✅

#### BP4 — 一致
- 在线 REVEL≤0.15, SpliceAI cutoff 与本地匹配 ✅

#### BP5 — 一致
- 在线 Supporting 与本地匹配 ✅

#### BP6 — 一致（均为Not Applicable）
- 在线：Not Applicable (retired)
- 本地：不适用证据码列表包含BP6 ✅

#### BP7 — 一致
- 在线 SpliceAI cutoff 与本地匹配 ✅

#### 不适用证据码列表 — 一致
- 在线：PVS1, PM1, PM3, PP5, BS3, BP1, BP3, BP6
- 本地：PVS1、PM1、PM3、PP5、BS3、BP1、BP3、BP6 ✅

---

## VWF GN090 (AR规范) 核实证据

### 来源
- 在线官方源：https://cspec.genome.network/cspec/ui/svi/doc/GN090 (Version 1.0.0, Released 7/9/2024)
- 本地文件：./ClinGen-VCEP/knowledge-base/VCEP-VWF.md (规范2，从第145行开始)

### 逐条证据码对比

#### PVS1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "VWD type 2N is caused by qualitative protein defects and not null variants."
- 本地：不适用证据码列表包含PVS1 ✅

#### PS1 — 有差异（PS1_Moderate缺失）
- 在线 Strong 与本地匹配 ✅
- **缺失**：在线版有 Moderate："Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP."
- 本地文件仅收录了Strong，未收录Moderate

#### PS2 — 有差异（PS2_Very Strong和PS2_Supporting缺失，VCEP Specifications缺失）
- 在线 Strong 和 Moderate 与本地匹配 ✅
- **缺失1**：在线版有 Very Strong："Use proposed SVI point recommendations for 'Phenotype consistent with gene but not highly specific' if the proband meets PP4 criteria. Use 'Phenotype highly specific for gene' phenotype consistency if the proband meets PP4_Moderate criteria. See Table 1 attached. Required 4 points."
- **缺失2**：在线版有 Supporting："Use proposed SVI point recommendations for 'Phenotype consistent with gene but not highly specific' if the proband meets PP4 criteria. If the proband meets PP4_Moderate criteria, use a moderate or higher evidence weight (see above). See Table 1 attached. Required 0.5 point."
- **缺失3**：在线版有 VCEP Specifications："Please note that presence of a second VWF variant is required to use this rule code."

#### PS3 — 一致
- 在线 Strong 规则文本与本地匹配 ✅

#### PS4 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Use PM3 for proband counting."
- 本地：不适用证据码列表包含PS4 ✅
- 注意：在线版有额外VCEP Specifications："Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count proband used for PP4 in this code's proband count."

#### PM1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Rule does not apply due to benign variation being present throughout the gene."
- 本地：不适用证据码列表包含PM1 ✅

#### PM2 — 一致
- 在线 Supporting popmax MAF <0.005 与本地匹配 ✅

#### PM3 — 核心规则一致，但缺少VCEP Specifications
- 在线 Very Strong/Strong/Moderate/Supporting (4/2/1/0.5分) 与本地匹配 ✅
- **缺失**：在线版有VCEP Specifications："May be applied when the variants on both alleles have MAFs below the BS1 threshold."

#### PM4 — 一致
- 在线 Moderate "Use with no specification." 与本地匹配 ✅

#### PM5 — 一致
- 在线 Moderate/Supporting 规则文本与本地匹配 ✅

#### PM6 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Use the PS2 code in lieu of using this code for de novo variants."
- 本地：不适用证据码列表包含PM6 ✅

#### PP1 — 一致
- 在线 Strong(3)/Moderate(2)/Supporting(1) affected family members 与本地匹配 ✅

#### PP2 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Not applicable due to presence of benign variation throughout the VWF gene."
- 本地：不适用证据码列表包含PP2 ✅

#### PP3 — 一致
- 在线 REVEL≥0.644, SpliceAI≥0.5 与本地匹配 ✅

#### PP4 — 一致
- 在线 Moderate 规则文本与本地匹配 ✅

#### PP5 — 一致（均为Not Applicable）
- 在线：Not Applicable (retired)
- 本地：不适用证据码列表包含PP5 ✅

#### BA1 — 一致
- 在线 Popmax MAF >0.1 与本地匹配 ✅

#### BS1 — 一致
- 在线 Popmax MAF >0.01 与本地匹配 ✅

#### BS2 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Not applicable due to the incomplete penetrance seen in VWD."
- 本地：不适用证据码列表包含BS2 ✅

#### BS3 — 一致（均为Not Applicable）
- 在线：Not Applicable. "There are no available assays that can clearly and dependably show no damaging protein effects."
- 本地：不适用证据码列表包含BS3 ✅

#### BS4 — 有差异（BS4_Supporting缺失）
- 在线 Strong 与本地匹配 ✅
- **缺失**：在线版有 Supporting："Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family."

#### BP1 — 一致（均为Not Applicable）
- 在线：Not Applicable. "The VWF gene is not constrained for missense variation (gnomAD)."
- 本地：不适用证据码列表包含BP1 ✅

#### BP2 — 一致（均为Not Applicable）
- 在线：Not Applicable. "Do not use due to potential of variant being associated with VWD 2N (recessive disease)."
- 本地：不适用证据码列表包含BP2 ✅

#### BP3 — 一致（均为Not Applicable）
- 在线：Not Applicable. "There are no known repetitive regions in the VWF gene without a known function."
- 本地：不适用证据码列表包含BP3 ✅

#### BP4 — 核心规则一致，但缺少Comments
- 在线 REVEL≤0.290 AND SpliceAI<0.1 与本地匹配 ✅
- **缺失**：在线版有Comments："Not using at this time but will note CADD and SpliceAI scores and consider use during pilot testing."

#### BP5 — 一致
- 在线 Supporting 规则文本与本地匹配 ✅

#### BP6 — 一致（均为Not Applicable）
- 在线：Not Applicable (retired)
- 本地：不适用证据码列表包含BP6 ✅

#### BP7 — 一致
- 在线 SpliceAI cutoff=0 与本地匹配 ✅

#### 不适用证据码列表 — 一致
- 在线：PVS1, PS4, PM1, PM6, PP2, PP5, BS2, BS3, BP1, BP2, BP3, BP6
- 本地：PVS1、PS4、PM1、PM6、PP2、PP5、BS2、BS3、BP1、BP2、BP3、BP6 ✅

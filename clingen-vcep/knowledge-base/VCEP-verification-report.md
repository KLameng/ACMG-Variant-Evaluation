# VCEP知识库补检核实报告
完成日期：2026-06-14
核实员：VCEP知识库核实员

---

## 任务1：ACTA1 GN147（AD规范）核实

### 对比结果：有差异

### 差异详情

#### 差异1（错误添加）— PP4 Strong
- **行号**：约第390-391行
- **本地内容**：`The combination of PP1 and PP4 is capped at strong. PP1+PP4 combined cannot exceed Bayesian 5 points.`
- **在线原文**：`The combination of PP1 and PP4 is capped at strong.`
- **差异说明**：本地文件额外添加了"PP1+PP4 combined cannot exceed Bayesian 5 points."这句话，但GN147在线规范中**并无此表述**。此为本地文件自行添加的内容，应删除。

#### 差异2（VCEP Specifications说明文本缺失）— PS4
- **行号**：约第290行PS4部分
- **缺失内容**：
  > ACTA1 is associated with both autosomal recessive and autosomal dominant disease. If you are curating biallelic observations, please use the AR specifications. Cases should not be counted if there are complex phenotypic features in addition to those listed that are incompatible with ACTA1, such as neurogenic etiology, central nervous system involvement, lysosomal disorders, increased serum CK levels, or extraocular muscle weakness.
- **影响**：此段说明了哪些病例不应纳入PS4计数，对实际判读有重要指导意义。

#### 差异3（VCEP Specifications说明文本缺失）— PM2
- **行号**：约第300行PM2部分
- **缺失内容**：
  > If the mode of inheritance for the variant is unclear (largely with missense variants as loss of function variants are predicted to cause AR disease), use the more conservative AD cutoff for PM2_Supporting.
- **影响**：此段说明了遗传方式不明确时的处理策略。

#### 差异4（VCEP Specifications说明文本缺失）— PP1
- **行号**：约第340行PP1部分
- **缺失内容**：
  > The segregation chart (adopted from Biesecker et al 2023 PMID:38103548) should be used to determine the strength level of the total number of segregations. The combination of PP1 and PP4 is capped at strong.
- **影响**：此段明确了segregation chart的来源和PP1+PP4上限。

#### 差异5（VCEP Specifications说明文本缺失）— BA1
- **行号**：约第410行BA1部分
- **缺失内容**：
  > If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BA1.
- **影响**：此段说明了遗传方式不明确时应使用更保守的AR截断值。

#### 差异6（VCEP Specifications说明文本缺失）— BS1
- **行号**：约第420行BS1部分
- **缺失内容**：
  > If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BS1.
- **影响**：同BA1，遗传方式不明确时的处理策略。

#### 差异7（VCEP Specifications说明文本缺失）— PP4
- **行号**：约第380行PP4部分
- **缺失内容**：
  > The strength of PP4 should be determined based on the case with the most specific phenotype. It should only be applied once per variant, even if there are multiple cases that meet PP4 criteria. The combination of PP4 and PP1 is capped at strong.
- **影响**：此段明确了PP4只能应用一次和取最特异性表型的规则。

#### 差异8（Comments缺失）— PP4
- **行号**：PP4部分
- **缺失内容**：
  > PP4 is not separately applicable for case counting. However, meeting PP4 increases the weight of a case. See PS4 specifications for more information.
- **影响**：此段说明了PP4与PS4的交互关系。

### 已确认一致的关键规则
- PS1 Strong/Moderate/Supporting ✅
- PS2 Very Strong/Strong/Moderate/Supporting ✅
- PS3 Strong/Moderate/Supporting ✅
- PS4 阈值：8/4/2 case observations ✅
- PM2 Supporting: absent (1 allele allowed) for AD ✅
- PM4 Strong/Moderate/Supporting ✅
- PM5 Strong/Moderate/Supporting ✅
- PM6 Strong/Moderate/Supporting ✅
- PP2 Supporting: gnomAD v4.1 z=6.09 ✅
- PP3: REVEL≥0.7, SpliceAI≥0.5 ✅
- PP4 Moderate: 4种肌肉活检特征 ✅
- PP4 Supporting: nemaline rods ✅
- BA1: ≥0.0000781 for AD ✅
- BS1: ≥0.00000781 for AD ✅
- BS2 Strong/Moderate/Supporting ✅
- BS4 Strong/Moderate/Supporting ✅
- BP2 Supporting ✅
- BP4: REVEL≤0.15, SpliceAI ✅
- BP5 Supporting ✅
- BP7: SpliceAI predicts no impact ✅
- 不适用证据码列表完全一致 ✅

### 建议操作
1. **删除**PP4 Strong中的"PP1+PP4 combined cannot exceed Bayesian 5 points."（在线源无此内容）
2. **补充**PS4、PM2、PP1、BA1、BS1、PP4各证据码下的VCEP Specifications说明文本
3. **补充**PP4的Comments文本

---

## 任务2：VWF GN090（AR规范）核实

### 对比结果：有差异

### 差异详情

#### 差异1（强度等级缺失）— PS1 Moderate
- **行号**：约第160行PS1部分
- **本地内容**：仅收录了Strong
- **在线原文**：除Strong外，还有Moderate："Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP."
- **差异说明**：本地文件遗漏了PS1_Moderate强度等级。这是一个重要的降级路径：当对照变异为Likely Pathogenic时，PS1只能用于Moderate。

#### 差异2（强度等级缺失）— PS2 Very Strong
- **行号**：约第168行PS2部分
- **本地内容**：仅收录了Strong和Moderate
- **在线原文**：还有Very Strong（Required 4 points）和Supporting（Required 0.5 point）
- **差异说明**：本地文件遗漏了PS2_Very Strong。在线版PS2在Very Strong强度要求4分，是PS2的最高证据权重。

#### 差异3（强度等级缺失）— PS2 Supporting
- **行号**：同上PS2部分
- **在线原文**：Supporting强度要求0.5分，且包含额外说明"If the proband meets PP4_Moderate criteria, use a moderate or higher evidence weight (see above)."
- **差异说明**：本地文件遗漏了PS2_Supporting及其中的PP4_Moderate升级说明。

#### 差异4（VCEP Specifications缺失）— PS2
- **行号**：PS2部分
- **缺失内容**：
  > Please note that presence of a second VWF variant is required to use this rule code.
- **影响**：此段是PS2使用的先决条件，遗漏会导致使用错误。

#### 差异5（强度等级缺失）— BS4 Supporting
- **行号**：约第253行BS4部分
- **本地内容**：仅收录了Strong
- **在线原文**：还有Supporting："Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family."
- **差异说明**：本地文件遗漏了BS4_Supporting。这区分了2+亲属（Strong）和1名亲属（Supporting）的不同证据权重。

#### 差异6（VCEP Specifications缺失）— PM3
- **行号**：约第195行PM3部分
- **缺失内容**：
  > May be applied when the variants on both alleles have MAFs below the BS1 threshold.
- **影响**：此段是PM3使用的MAF前提条件。

#### 差异7（Comments缺失）— BP4
- **行号**：约第260行BP4部分
- **缺失内容**：
  > Not using at this time but will note CADD and SpliceAI scores and consider use during pilot testing.
- **影响**：此段说明了BP4当前的试用状态，有实际操作指导意义。

#### 差异8（VCEP Specifications缺失）— PS4
- **行号**：PS4标记为Not Applicable，但在线版有附加说明
- **缺失内容**：
  > Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count proband used for PP4 in this code's proband count.
- **影响**：虽然PS4标记为不适用（"Use PM3 for proband counting"），但此附加说明对理解PM3与PS4的关系有帮助。

### 已确认一致的关键规则
- PS1 Strong ✅
- PS2 Strong (2分)/Moderate (1分) ✅
- PS3 Strong ✅
- PM2 Supporting: popmax MAF <0.005 ✅
- PM3 Very Strong(4分)/Strong(2分)/Moderate(1分)/Supporting(0.5分) ✅
- PM4 Moderate ✅
- PM5 Moderate/Supporting ✅
- PP1 Strong(3)/Moderate(2)/Supporting(1) affected family members ✅
- PP3: REVEL≥0.644, SpliceAI≥0.5 ✅
- PP4 Moderate ✅
- BA1: Popmax MAF >0.1 ✅
- BS1: Popmax MAF >0.01 ✅
- BS4 Strong ✅
- BP4: REVEL≤0.290 AND SpliceAI<0.1 ✅
- BP5 Supporting ✅
- BP7: SpliceAI cutoff=0 ✅
- 不适用证据码列表完全一致 ✅

### 建议操作
1. **补充**PS1_Moderate：添加"Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP."
2. **补充**PS2_Very Strong：添加4分要求的完整规则文本
3. **补充**PS2_Supporting：添加0.5分要求的完整规则文本，含PP4_Moderate升级说明
4. **补充**PS2的VCEP Specifications：添加"presence of a second VWF variant is required to use this rule code."
5. **补充**BS4_Supporting：添加1名亲属的规则文本
6. **补充**PM3的VCEP Specifications：添加MAF前提条件说明
7. **补充**BP4的Comments：添加"pilot testing"说明

---

## 总结

| 规范 | 对比结果 | 关键差异数 | 严重程度 |
|------|---------|-----------|---------|
| ACTA1 GN147 (AD) | 有差异 | 1处错误添加 + 7处文本缺失 | 中等（1处需删除，7处需补充） |
| VWF GN090 (AR) | 有差异 | 3处强度等级缺失 + 4处文本缺失 | 较高（3处强度等级缺失直接影响判读） |

**VWF GN090的3处强度等级缺失（PS1_Moderate、PS2_Very Strong/Supporting、BS4_Supporting）为高优先级修复项**，因为这些缺失会导致知识库用户无法使用这些证据强度等级，直接影响变异分类结果。

**ACTA1 GN147的PP4 Strong中"Bayesian 5 points"为高优先级删除项**，因为此内容在线源中不存在，可能误导用户。

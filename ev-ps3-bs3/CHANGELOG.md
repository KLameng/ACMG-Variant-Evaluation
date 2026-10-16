# ev-ps3-bs3 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此

## v1.1.0

- 新增【文献核验+可疑文献上报】强制子步骤（功能实验文献先核验是否针对本特异变异，ClinVar/HGMD挂载一律默认可疑）

## v1.1.1

- 补跨技能引用声明——凡本技能判定依赖文献检索/核验时，须调用 `ev-variant-literature-patient` 完成「可疑文献上报」与按用途差异化提取；本技能 description 显式声明该跨技能依赖，不再隐式引用。

## v1.2.1

- 弃用闸就位——①弃用 PS3 前须输出穷尽检索记录（证明确无针对本特异变异的成熟功能实验）；②单篇定性/生化实验最高 PS3_Supporting；③携带者队列关联测量不得误用 PS3（SMPD1 判例：ClinVar curated 明言 no experimental evidence）。

## v1.3.0

- 新增【功能实验穷尽检索专项】（整改 P0-2，实证 var010 GALC COS-1 酶活 PMID 9272171 / var036 SLC22A5 HEK293T 转运 PMID 16931768 / var037 G6PD 已确立缺乏变异型 功能实验文献未检索到而被漏计）：①判定 PS3/BS3 前**必须**穷尽检索该基因该变异的成熟功能实验（PubMed gene+变异+酶活/转运/荧光等关键词 + ClinVar 功能实验标注 + HGMD），输出"功能实验检索结果表"，不得只凭 ClinVar/HGMD 挂载或单篇；②PS3 与 PP3 同存时的取舍统一以收尾技能互斥矩阵 §1.2 裁决（v1.4.0 起本技能不再内嵌"PS3 优先保留"取舍结论，互斥裁决唯一在收尾）。

## v1.4.0（全局维护收敛整改）

- 可疑文献判定完整标准收敛到唯一权威 `ev-variant-literature-patient`；越权"PS3↔PP3 互斥优先"段删除，互斥裁决唯一移交收尾 `acmg-conflict-summary-output` §1.2。

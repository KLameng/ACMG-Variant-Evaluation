# ev-pm1 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此

## v1.0.1

- 补跨技能引用声明——凡本技能判定依赖文献检索/核验时，须调用 `ev-variant-literature-patient` 完成「可疑文献上报」与按用途差异化提取；本技能 description 显式声明该跨技能依赖，不再隐式引用。

## v1.0.2（全局维护收敛整改）

- 可疑文献判定完整标准（L1/L2/L3 分级 + 挂载默认可疑 + 强制上报）收敛到唯一权威 `ev-variant-literature-patient`，本技能仅保留按用途定制提取要求，不再内嵌重复完整段。

## v1.1.0（约束取数 fallback 分支，2026-10-16 用户复盘"RMC NOT FOUND 被当无约束/漏查 DECIPHER"）

- **根因**：COL7A1 实测——ExAC RMC 仅 2701 基因未覆盖 COL7A1，第一轮误判"该区域无约束证据"并标"争议"；且 DECIPHER 基因级约束分第一轮漏做（没发起查询），却写成"未取到"（把"没查"当"查不到"）。ev-pm1 操作步骤无 NOT FOUND 处理分支，且未引用 ev-gnomad-constraint 的"缺数据≠反对"规则（该技能第56行）。
- **落地**：ev-pm1 操作步骤新增「约束取数 fallback 分支」硬步骤——①识别 NOT FOUND 类型（资源未覆盖 vs 确无约束数据）；②基因不在数据集按"缺数据≠反对"处理（不得据此不支持 PM1，引用 ev-gnomad-constraint）；③区域级取不到**同轮立即**切替代通道（DECIPHER 基因级 missense 约束 + G2P/ClinGen 机制 + 结构域热点文献，走 ev-variant-literature-patient 核验）；④替代通道能定 → 直接定"确信"，不得带"争议"进收尾；⑤实在取不到才"查不到"并标注类型；⑥铁律"漏做≠查不到"（约束取数必须实际发起 RMC+基因级，不得因没查写查不到/标争议）。
- 纯文字规则，无引擎改动；与其他 ev-* 技能正交（缺数据≠反对唯一权威在 ev-gnomad-constraint，本技能仅引用）。

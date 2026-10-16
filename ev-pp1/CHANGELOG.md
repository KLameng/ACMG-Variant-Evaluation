# ev-pp1 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此

## v1.1.0

- 新增遗传方式前置判定硬步骤——判定前必须先调用 `arad-inheritance-judgment` 确认该变异为显性(AD)/隐性(AR)/X连锁，再选用对应 LOD 公式与强度表，禁止默认 AD 或 AR；遗传方式以 ClinVar 患者基因型+PubMed报道+GenCC MOI 三方交叉为准。

## v1.2.0

- 新增【文献核验+可疑文献上报】强制子步骤（引用文献家系做共分离累加时先核验，仅本家系数据不受限）

## v1.2.1

- 补跨技能引用声明——凡本技能判定依赖文献检索/核验时，须调用 `ev-variant-literature-patient` 完成「可疑文献上报」与按用途差异化提取；本技能 description 显式声明该跨技能依赖，不再隐式引用。

## v1.3.0

- 新增【共分离穷尽检索专项】对治"共分离家系漏用"——启用 PP1 前必须完成本家系+PubMed/ClinVar/HGMD 其他家系多通道穷尽检索（segregation/pedigree/family/co-segregation 关键词），逐家系核对受累/非受累成员按 LOD 累加，确认无共分离家系后才弃用，不得凭"查不到"直接漏用；内置 OTOF/GJB2/GALC 应用判例。

## v1.3.0

- 补齐 BS4（无共分离，良性 Strong）——BS4 为 PP1 的良性镜像（变异解读查询路径 5.5.7），在受影响个体中检测不到该变异/与该变异不共分离且样本量足够时使用；判定前同样须调用 `arad-inheritance-judgment` 确认遗传方式。

## v1.3.1（全局维护收敛整改）

- 可疑文献判定完整标准（L1/L2/L3 分级 + 挂载默认可疑 + 强制上报）收敛到唯一权威 `ev-variant-literature-patient`，本技能仅保留按用途定制提取要求，不再内嵌重复完整段。

## v1.6.0（HL VCEP 官方矩阵强制闸，2026-10-16 用户评级实证 USH2A）

- **根因**：USH2A 家系 3 受累分离被经验计数当 2 个，PP1 误给 Moderate（应为 Strong）。
- **第 4 步升级为强制官方矩阵闸**：PP1 第一步先判断该基因有无 ClinGen VCEP cspec；有 → 必须回官方规范原文逐格查表，禁止计数推理。
- **固化 HL VCEP（GN005）AR 口径**：受累分离数 **含先证者**、unaffected 不含携带者父母；LOD=log10(1/(0.25^affected×0.75^unaff))（Strande 2017/Table 4b）；阈值 0.6/1.2/1.5（Table 4a）。有 HL VCEP 基因**禁用通用 pp1_lod_ar**（其 0.25^(affected-1) 排除先证者、阈值 0.9/1.5/2.1，系统性低估档位）。
- **确定性工具**：新增 `acmg_evidence.py::pp1_lod_hl_ar`（官方口径），`pp1_lod_ar` 加 `gene` 参数自动命中 HL VCEP 基因；CLI 注册两入口。阈值集中 `config/thresholds.json → hl_vcep_pp1`。
- **输出强制四要素**：受累分离数（含先证者）+ unaffected 数 + 查表 LOD + 对照阈值，杜绝"≥2 亲属=Moderate"经验表述。
- 纯输出/工具契约，组合引擎与 39 集评测不受影响（golden 无 HL VCEP PP1 变异，回归需实测确认）。
- 版本：ev-pp1 **1.6.0**（收尾、acmg_evidence、thresholds 同步见 sync-manifest §10）。

## v1.5.0（PP1 共分离证据逐家系结构化输出，2026-10-16 用户拍板）

- **PP1 共分离证据结构化输出模板**：第 2 点"数据值"对每个计入 PP1 的家系，**逐家系**列全——家系规模（几人）、携带该变异的人数、携带者是否受累（有表型/无表型/未报告）、表型是什么、参考文献号(PMID)+链接(URL)。有 N 个家系列 N 个；任一字段未给出**直接写"未给出"**，不得空着、不得捏造。
- 当前先证者**本家系数据**（非文献来源）须注明"本家系数据（无独立文献，无 PMID）"，不得伪报文献。衔接收尾『文献呈现强制规则』（PMID+URL 成对）。纯 L1 输出层文本契约，**不改 LOD 计分/判定/引擎**。
- 措辞防照抄修正（同版本 1.5.0，逻辑不变）：模板明确为"字段清单（数据采集项），不是要输出的句子"——输出须逐字段填本次查到的实际值，**禁止照抄模板字段名/示例枚举**（如"几人""有表型"）；整段照抄模板或只输出字段名不填值判违规、不得定级。

## v1.4.0（第三方第三轮深度审计修复，2026-10-15）

- **PP1 共分离 LOD 强度阈值切换为 ClinGen 共识可核验值（0.9/1.5/2.1，来源 Jarvik & Browning 2016, PMID 27495972）**：原 0.6/1.2/1.5 来自内部 slide、不可外部核验，已弃用。判定语义：Supporting LOD≥0.9（3–4 个减数分裂）/ Moderate ≥1.5（5–6 个）/ Strong ≥2.1（7 个以上）。阈值统一读 `config/thresholds.json → pp1_lod`，由 `scripts/acmg_evidence.py` 的 `pp1_lod_adxl` / `pp1_lod_ar` 确定性定档（替代手工查表）。
- 备注：原 CHANGELOG 存在两个重复 v1.3.0 条目（一为共分离穷尽检索、一为 BS4 补齐），保留原文、未合并改动。

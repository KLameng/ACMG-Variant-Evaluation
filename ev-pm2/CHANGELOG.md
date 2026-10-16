# ev-pm2 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此

## v1.1.0

- 新增【阈值选择优先级】——存在基因/疾病特异性阈值时必须优先用特异性阈值，不得一律套用通用阈值；新增【频率数据质量核验】——gnomAD 等低质量/呼叫质量差的位点频率不可靠时须标注并作降权/弃用处理。

## v1.2.0

- 新增遗传方式前置判定硬步骤——判定前必须先调用 `arad-inheritance-judgment` 确认该变异为 AD/XL 或 AR，再选对应 PM2 阈值（通用与特异性阈值均分 AD/AR），禁止默认遗传方式；遗传方式以 ClinVar 患者基因型+PubMed报道+GenCC MOI 三方交叉为准。

## v1.3.0

- 新增【文献核验+可疑文献上报】强制子步骤（特异性阈值出处文献/频率降权引用文献先核验，纯数据库频率判定不触发）

## v1.3.2

- 补跨技能引用声明——凡本技能判定依赖文献检索/核验时，须调用 `ev-variant-literature-patient` 完成「可疑文献上报」与按用途差异化提取；本技能 description 显式声明该跨技能依赖，不再隐式引用。

## v1.3.3（全局维护收敛整改）

- 可疑文献判定完整标准（L1/L2/L3 分级 + 挂载默认可疑 + 强制上报）收敛到唯一权威 `ev-variant-literature-patient`，本技能仅保留按用途定制提取要求，不再内嵌重复完整段。

## v1.4.1（D9′ 落定，2026-10-15）

- **用户拍板确认**：2026-10-15 用户在对话中明确表态「永久固定 PM2_Supporting」——v1.4.0 的领域拍板声明从"待确认"转为**已确认固化**。
- 落地：SKILL.md 补充「永久固定」声明（不得因频率更低/数据更足给 Moderate/Strong）；收尾 `acmg-conflict-summary-output` 分值表 PM2 行同步标注仅 Supporting(+1)。

## v1.4.0（领域拍板，2026-10-15）

- **PM2 强度裁定**：PM2 **永久固定为 `PM2_Supporting`**（除非未来 ACMG/ClinGen 指南更新），现版本一律按 Supporting 强度处理，不降级、不升档争议。
- **两种评级结算方式（经典联合规则 Table5 + Tavtigian 分值）均以证据等级（VeryStrong/Strong/Moderate/Supporting）为统一量纲**：`PM2_Supporting` 即 Supporting，计入 Supporting 桶/SU=1，**不因码属 PM 类而打折、也不升档为 Moderate**；证据码升降级对应"最终使用等级"，与码前缀基线解耦（引擎 `acmg_combine.py` 已按此实现）。

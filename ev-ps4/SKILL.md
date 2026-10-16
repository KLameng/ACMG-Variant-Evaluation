---
name: ev-ps4
version: 1.2.3
description: PS4 强致病证据（变异在患病群体中频率显著高于对照）判定。按 指南解读 slide 39-40 与 变异解读查询路径 5.5.1 执行：AD/XL 按先证者个数升降级，AR 须文献报道 OR>5.0 且置信区间不含1.0。含 ClinGen VCEPs 各基因先证者个数阈值表（MYH7/RASopathy/PTEN/CDH1/HL）。判定前须先调用 `arad-inheritance-judgment` 确认遗传方式（AD/XL 或 AR），禁止默认；文献先证者数/OR 须经 `ev-variant-literature-patient` 核验并上报可疑文献。
---


# PS4：病例-对照 / 先证者个数证据

## 定义（原文）

PS4：变异出现在患病群体中的频率显著高于对照群体。

## ⚠ 遗传方式前置判定（硬步骤，v1.1.0 新增，分流前提）

**判定 PS4 前，必须先调用 `arad-inheritance-judgment` 子技能确认该变异的遗传方式（AD/XL 或 AR），禁止默认。** PS4 的分流规则完全依赖遗传方式：

- **AD / XL** → 按第 1 步第 1 条：数先证者个数升降级（>1 个 Supporting，>2 个 Moderate）；
- **AR** → 按第 1 步第 2 条 + 第 2 步：**不可数先证者个数**，须查文献 OR>5.0 且 CI 不含 1.0；
- **无法推断**：写"无法推断"，按证据不足处理，不得擅自假设遗传方式选错分流规则。

> 遗传方式以 ClinVar 患者基因型 + PubMed 报道 + GenCC MOI 三方交叉为准，ARAD 为辅助检索工具（见 arad-inheritance-judgment 技能）。

## 操作步骤（指南解读 slide 39；变异解读查询路径 5.5.1）

### 第 1 步：按遗传方式分流

- **AD 或 XL 遗传**：可参考文献中的先证者个数按 变异解读查询路径（下表）升降级，并附参考文献 PMID 号。无特殊：>1 个先证者用 Supporting，>2 个用 Moderate。
  > **⚠ 先证者独立性核对（v1.2.3，防"3 提交≠3 无亲缘患者"）**：数先证者个数时，**须核对 ClinVar 各 SCV submission 是否无亲缘/独立**——多个提交可能指向同一患者或同一家系（同一变异 + 同表型 + 同机构或同家系），须按患者/家系去重后再计数，不得"提交数≈患者数"直接推断；无法确认独立时按"疑同源（无法确认），保守合并"并标注。先证者数逐篇核对、不重复计数。
- **AR 遗传**：不可根据先证者个数升降级；需查阅文献是否报道该变异满足 **OR > 5.0 且置信区间(IC)不包括 1.0**，满足才可用 PS4。

### 第 2 步：AR 的 OR/IC 计算（变异解读查询路径 p18-19）

- 如文献包含对照人群，选用文献中该变异在对照人群中的频率；
- 若文献不含对照人群，选 ExAC 中的频率；满足"OR>5.0 且 IC 不包括 1.0"即可使用 PS4。
- 计算 OR 和 IC 网址（两个链接均已实测可访问，2026-10-09 核验）：① **http://www.hutchon.net/ConfidOR.htm**（Hutchon 病例对照 OR+95%CI 计算器，BMJ 2000 出处，主用）；② **https://www.4calculators.com/calculators/odds-ratio-calculator/**（备用，同样返回 OR+95%CI）。原第二链接 `easyca-lculateon.com` 为拼写笔误且不可达，已替换为备用计算器。
- 罕见病例对照研究无统计意义时：若为显性遗传病且变异 AF 符合 PM2，已有多个相同表型患者携带该变异的报道可使用 PS4，强度随患者数量减少而下降。

> **⚠ 文献核验 + 可疑文献上报（引用唯一权威，PS4 全依赖文献先证者数/OR，必须先核验再计）**
> **PS4 的一切数据（先证者个数、OR/IC、患者频率）都来自文献，须调用 `ev-variant-literature-patient` 完成「可疑文献上报」判定（L1/L2/L3 分级 + 挂载默认可疑 + 强制上报的完整判定标准，唯一以该技能为准）；判定输出须含"本次计入文献核验等级(L1/L2/L3)"；命中可疑文献未核验前，PS4 标注"待全文核验"或暂不成立。**
> **⚠ 按用途定制提取（v1.3.0 全局，PS4）：本证据码从文献中必须提取【先证者个数 + 病例数/对照数 + OR 值与置信区间 CI(AR 必需)】；缺对照或未给 OR/CI 的文献不得用于 AR 型 PS4 判定（AR 需 OR>5 且 CI 不含 1）。先证者数须逐篇核对、不重复计数。关键字段提取不到，该数据标"未报告"，不得凭推测填充。**


### 第 3 步：按 ClinGen VCEPs 先证者个数定级（变异解读查询路径 p19 表1）

| 基因/疾病 | PS4_Supporting | PS4_Moderate | PS4 (Strong) | PM2 threshold |
|---|---|---|---|---|
| MYH7 肥厚型心肌病 | ≥2 probands 表型一致 | ≥6 probands 表型一致 | ≥15 probands 表型一致 | <0.004% |
| RASopathy | ≥1 proband 符合 RASopathy 标准 | ≥3 probands 符合 | ≥5 probands 符合 | Strictly absent |
| PTEN 错构瘤肿瘤综合征(PHTS) | >1 proband 符合 Cleveland Clinic 标准(30 score) | >2 probands 符合 | >4 probands 符合 | <0.001% |
| CDH1 遗传性弥漫性胃癌(HDGC) | >1 HDGC family 符合 | >2 HDGC family 符合 | >4 HDGC family 符合 | <0.001% |
| HL（常显耳聋） | ≥2 probands 表型一致 | ≥6 probands 表型一致 | ≥15 probands 表型一致 | <0.002% |

> **🔧 确定性定档（acmg_evidence.py，替代手工查表）**：先证者数→档位统一用 `scripts/acmg_evidence.py` 的 `ps4_band(probands, gene)`（命中 VCEP 表用表内阈值，否则通用 ≥2/≥6/≥15）；AR 的 OR+95%CI 用 `ps4_or_ci(a,b,c,d)`（Haldane 零校正）。用法：`python acmg_evidence.py ps4_band 3 MYH7`。

## 案例（指南解读 slide 40）

46,XY 性反转 AR c.1175C>G p.Pro392Arg：PS4_Moderate（PMID:10571951、29582157，各 1 patient），配合 PM2_Supporting、PP3_Moderate(REVEL=0.841)、PP4_Supporting，评为可能致病。

## 自检清单

- [ ] 已区分 AD/XL（数先证者）与 AR（须 OR>5.0 且 CI 不含 1.0）。
- [ ] 先证者个数已对号 VCEPs 表定级并附 PMID。
- [ ] **已执行「可疑文献上报」核验（v4.1.0 全局，判定标准唯一以 `ev-variant-literature-patient` 为准）：凡依赖文献检索，命中可疑文献判定标准（HGMD/ClinVar 已挂载但全文通道全部无法获取、或标题/摘要检索不到该变异）时，已把 PMID+链接+原因上报用户人工核验，未把无法核验全文的文献静默当作已核实证据计入。**

---

## 输出格式（强制，本 SKILL 判定完成后必须按此输出）

每个证据码判定完成后，**必须**按下述三点完整输出；缺一不可，查不到的数据明确写 **"查不到"**，严禁用本 SKILL 内的举例数据或推测代替。

### 1. 证据码 + 对应等级
`[证据码]_[使用等级]`，如 `PM3_Strong`、`PP3_Moderate`、`PM2_Supporting`。未成立则写"本证据不成立/弃用"。

### 2. 支持该等级使用的规则性数据内容 + 定级规则
- 写明支撑该等级判定的**具体数据值**（如人群频率、REVEL 分数、反式例数、对照数目、OR 值、分离次数等）；
- 对照本 SKILL 的定级规则/阈值表，说明该数据落在哪个区间/档位，从而定为该等级；
- 即：数据值 → 落入的规则档位 → 所得等级，三步闭环。

### 3. 查询路径
列出本次判定**实际查询过**的数据库链接、文献编号(PMID)及对应链接；**每次查询都必须是真实查询**。
- 数据库：名称 + URL（如 ClinVar、gnomAD、Pubvar、OMIM、HGMD、ClinGen 等）；
- 文献：PMID 编号 + 链接；
- 某项查不到：写 **"查不到"**，不得以举例数据填充。

> **铁律**：本 SKILL 内所有"案例/示例/举例"仅供教学演示，**禁止**作为评级数据套用；评级数据一律来自实际查询，否则该证据码不得计入。

---
name: ev-pp3-bp4
version: 1.6.2
description: PP3（支持致病，计算机预测有害）与 BP4（支持良性，计算机预测无害）判定，同技能承载 BP1（错义但该基因仅 LOF 机制）与 BP7（同义/非编码且不影响剪接）。按 指南解读 slide 53 与 变异解读查询路径 5.3.2.3/5.3.2.4 执行：错义主要参考 REVEL 值按强度表落 PP3 Supporting/Moderate/Strong 或 BP4 VeryStrong/Strong/Moderate/Supporting，剪接侧用 SpliceAI2。铁律：REVEL 能取到必须以 REVEL 对照强度表定档，多工具共识不得替代。
---

# PP3 / BP4 / BP1 / BP7：计算机预测与机制类证据

## 定义（原文）

- **PP3**：多种统计方法预测出该变异会对基因或基因产物造成有害的影响，包括保守性预测、进化预测、剪接位点影响等。
- **BP4**：多种统计方法预测出该变异会对基因或基因产物无影响，包括保守性预测、进化预测、剪接位点影响等。

## 操作步骤（指南解读 slide 53；变异解读查询路径 5.3.2.3/5.3.2.4）

针对错义突变，**主要参考 REVEL 值**。REVEL 阈值区间（指南解读 Table 2，对应 BP4/PP3 强度）：

### REVEL 强度对照

> **权威来源 = `config/thresholds.json` → `revel`；改切点必须在 thresholds.json + 本表 + `scripts/acmg_evidence.py::revel_band` 三处同步（sync-manifest §10）**

| REVEL 区间 | 证据强度 |
|---|---|
| ≤ 0.003 | BP4 Very Strong |
| (0.003, 0.016] | BP4 Strong |
| (0.016, 0.183] | BP4 Moderate |
| (0.183, 0.290] | BP4 Supporting |
| [0.644, 0.773] | PP3 Supporting |
| [0.773, 0.932] | PP3 Moderate |
| ≥ 0.932 | PP3 Strong |

> **🔧 确定性定档（acmg_evidence.py，替代手工查表）**：REVEL 值→档位映射统一用 `scripts/acmg_evidence.py` 的 `revel_band(revel)` 确定性输出（含中空档判定），LLM 不再手算区间。用法：`python acmg_evidence.py revel_band <REVEL值>` 或 `import acmg_evidence; acmg_evidence.revel_band(0.972)`；REVEL 取不到仍写"查不到"，不得默认档位。

> **⚠ REVEL 中空档兜底（强制，0.290 < REVEL < 0.644）**：REVEL 值落在此区间时，**PP3 与 BP4 均不成立**（计算机预测呈中性/不确定，无任何一侧证据可计），**不得默认套用 PP3，也不得默认套用 BP4 任一侧强度**。判定输出须写明"REVEL=… 落中空档 (0.290, 0.644)，PP3/BP4 均不适用"。边界值归侧：REVEL=0.290 属 **BP4_Supporting**（(0.183,0.290] 含端点），REVEL=0.644 属 **PP3_Supporting**（[0.644,0.773] 含端点）。

> 区间记号：`(` `)` 表示不含端点，`[` `]` 表示含端点。

**REVEL 取数兜底与阈值复核（强制，v1.4.0 强化：REVEL 主通道强制优先）：**

1. **REVEL 主通道强制优先（v1.4.0，防 var022 类通道遗漏）**：
   - **REVEL 能取到（① Ensembl VEP/dbNSFP `revel_score`；② GeneBe api-public `revel_score`；③ MyVariant.info dbnsfp 块）时，必须以 REVEL 值对照强度表定档 PP3/BP4**，多工具共识**不得**替代 REVEL 定档。
   - **多工具共识（CADD+SIFT+PolyPhen 等 ≥3 个 concordant damaging）仅限"REVEL 三通道全部取不到"时作为兜底**，且只能佐证 PP3 方向、最高给 PP3_Supporting，必须在"查询路径"注明"REVEL 取不到，用替代共识（仅 Supporting 上限）"。
   - **判例（写死，防复发）**：var022 SLC22A5 c.338G>A——REVEL 可取得 0.972 ≥ 0.932 → **必须 PP3_Strong**，不得因取多工具共识给 Supporting。
2. **阈值逐数复核（防误标档位）**：REVEL 值须与下表边界**逐数核对**——尤其 `0.932`（PP3_Strong 下界）、`0.773`（PP3_Moderate 下界）、`0.644`（PP3_Supporting 下界）、`0.290`（BP4_Supporting 上界）。例：REVEL=0.91 落 [0.773,0.932] → **PP3_Moderate**，不是 Strong；REVEL=0.972 落 ≥0.932 → **PP3_Strong**。不得凭整数近似估档。

辅助核对：
1. 参考 REVEL 值（PMID:36413997）。
2. 保守性预测该位点是否保守。
3. 参考 Pubvar 数据库中的预测结果。

> BP4：大多数基因不使用该证据（变异解读查询路径 5.3.2.4）。

### BP4 使用限定条件（功能实验优先，硬闸门，v1.5.0 新增，不符合不得给分）

> 根治"计算机预测良性掩盖功能受损致病变异"（实证 **UGT1A1 c.211G>A（*6, p.Gly71Arg）**：多 in silico 工具预测良性，但功能实验证明酶活降低 PMID 9630669/19830808，曾误给 BP4_Moderate）。BP4（预测无害）**不得与功能实验证据冲突**。

**强制排除闸（功能实验优先，一票否决）**：给 BP4 前**必须**穷尽检索该特异变异的成熟功能实验——PubMed（gene + 变异 + 酶活/转运/荧光/功能关键词）、ClinVar 功能实验标注、HGMD：
1. **检出功能受损证据**：若存在针对该特异变异的功能实验显示**功能受损/酶活降低/功能缺失**（PS3 侧证据，如 UGT1A1*6 酶活降低 PMID 9630669/19830808）→ **BP4 与功能实验冲突，功能实验优先，BP4 强制不成立**，回致病证据链（PS3 侧），不得按 REVEL 预测给 BP4；
2. **未检出功能实验**：才可按上方 REVEL 强度表给 BP4；
3. **无法确认**：功能实验检索结果不明确/取不到 → 写"查不到功能实验证据"，**不得默认无功能受损而给 BP4**。

> **判例（写死，防复发）**：UGT1A1 c.211G>A（*6, p.Gly71Arg）——多 in silico 工具预测良性（BP4 侧），但功能实验证明酶活降低（PMID 9630669/19830808）→ **BP4 强制不成立**，不得判 LB。

## 预测工具官方网址与当前调用方式

| 工具 | 官方网址 | 当前调用方式 |
|---|---|---|
| REVEL | https://revel.genome.edu/ | 通过 Ensembl VEP dbNSFP 插件 |
| AlphaMissense | https://github.com/google-deepmind/alphamissense | 通过 Ensembl VEP 插件 |
| MetaRNN | https://github.com/bcm-lin-lab/MetaRNN | 通过 Ensembl VEP dbNSFP 插件 |
| BayesDel | https://github.com/fenglab/bayesdel | 通过 Ensembl VEP dbNSFP 插件 |
| SpliceAI | https://spliceailookup.broadinstitute.org/ | 直接调用官方 API（可独立调用 ✓） |
| SpliceAI2 | https://github.com/Illumina/SpliceAI2 | **剪接预测主升级通道（v1.6.0）**：`spliceai2_summary_score` 阈值 0.1/0.25/0.5（对应初代 0.2/0.5/0.8）；预计算 40 亿 SNV + 1.5 亿 indel 学术免费（PyPI 需 CUDA GPU）；不可达时回退初代 SpliceAI API 并交叉验证（✓） |
| CADD | https://cadd.gs.washington.edu/ | 直接调用官方 API（可独立调用 ✓） |
| SIFT | https://sift.bii.a-star.edu.sg/ | 未独立调用（仅 Ensembl VEP 内置） |
| PolyPhen-2 | http://genetics.bwh.harvard.edu/pph2/ | 未独立调用（仅 Ensembl VEP 内置） |
| Genebe | https://genebe.net/ | **正式兜底取数通道（推荐）：GeneBe api-public 端点直接取 REVEL/AlphaMissense/BayesDel/SpliceAI/gnomAD/ClinVar/ACMG 全字段（见下）** |

> 参考：
> - SpliceAI 查询：https://spliceailookup.broadinstitute.org/
> - SpliceAI 原文（Jaganathan et al., Bioinformatics 2017）：https://academic.oup.com/bioinformatics/article/33/2/235/2525715
> - 调用约定：错义类预测（REVEL/AlphaMissense/MetaRNN/BayesDel/SIFT/PolyPhen-2）统一走 Ensembl VEP（dbNSFP）批量取数；需要剪接影响时单独调 SpliceAI 官方 API；需要综合打分时单独调 CADD 官方 API。
> - **剪接侧主通道（v1.6.0）：优先 SpliceAI2**（github.com/Illumina/SpliceAI2，`spliceai2_summary_score`，阈值 0.1/0.25/0.5 ↔ 初代 0.2/0.5/0.8；深内含子/隐蔽剪接灵敏度优于初代，SpliceAI2 约半数隐蔽剪接位点位于 >50bp 深内含子，初代易漏）；SpliceAI2 不可达/无 GPU 时回退初代 SpliceAI 官方 API（spliceailookup，0.2 高召回切点）并交叉验证；两者都取不到才写"查不到"。
> - SpliceAI、CADD 以官方 API 口径为准，本 SKILL 不另作封装或阈值改动。

## SpliceAI2 剪接侧接入（v1.6.0，直接接入，来源版本绑定）

> **接入目的**：初代 SpliceAI 对深内含子/隐蔽剪接灵敏度不足（SpliceAI2 约半数隐蔽剪接位点位于 >50bp 深内含子，外显子测序常漏），SpliceAI2（训练数据扩 100 倍，31.5 万 RNA-seq、多物种）在此类场景显著提升。SpliceAI2 仅做实本技能**剪接侧**（PP3 剪接辅助、BP7 剪接影响、BP4 剪接无害侧），**不替代 REVEL 错义主通道**（错义 PP3/BP4 仍以 REVEL 强度表为准）。

**取数通道优先级（写死）**：
1. **SpliceAI2（主升级通道）**：`spliceai2_summary_score`（0-1）。通道：预计算表/本地模型（github.com/Illumina/SpliceAI2，学术免费；PyPI 安装需 CUDA GPU；预计算覆盖 40 亿 SNV + 1.5 亿 indel）。
2. **初代 SpliceAI（回退+交叉）**：spliceailookup.broadinstitute.org 官方 API `spliceai_max_score`。SpliceAI2 不可达/无 GPU 时回退，并对关键结果与 SpliceAI2（若可得）交叉验证。
3. **GeneBe api-public（兜底）**：`spliceai_max_score` 字段。
4. 全部取不到 → 写"查不到"，不得默认无剪接影响。

**阈值映射（来源版本绑定，写死；权威来源=config/thresholds.json → `spliceai.v2_thresholds`，判定统一走 `acmg_evidence.py spliceai_band`，防漂移）**：
| SpliceAI2 summary_score | 对应初代 SpliceAI | 口径 | 用途 |
|---|---|---|---|
| ≥ 0.1 | > 0.2 | 高召回 | 判"有剪接影响"（BP7 不成立 / 剪接侧 PP3） |
| ≥ 0.25 | ≥ 0.5 | 平衡 P/R | 剪接影响较确 |
| ≥ 0.5 | ≥ 0.8 | 高精度 | 剪接破坏高度可信 |

> **版本绑定（铁律）**：SpliceAI2 v2，Illumina BioInsight AI Lab，2026-10-08（technical article + manuscript preprint；正式期刊发表后以正式版为准并触发重审）；初代 SpliceAI 阈值 Jaganathan et al. *Cell*. 2019;176(3):535-548，PMID 30661751。ClinGen 已将初代纳入剪接证据指南。输出须注明所用通道（SpliceAI2 v2 / 初代 API）+ 版本。

**合规边界**：SpliceAI2 仅作基础注释取数（剪接预测分值），其预测为"剪接影响概率/效应"，非致病评级字段；不替代成熟功能实验（PS3/BS3）与 RNA 实证（PVS1_Strength(RNA)）；与 REVEL 错义主通道并列但各司其职。

## 取数兜底路径（正式通道，必读）

> **重要**：REVEL 官方无独立 API（仅交互式网页 revel.genome.edu），错义预测常规走 Ensembl VEP 的 dbNSFP 插件列；**若经该原路径取不到 REVEL/预测值（如 VEP 默认端点不返回 dbNSFP 列、或 genebe 老端点 api-x 被 robots 反爬拦截），一律改用下方 GeneBe api-public 端点取数**，再按上文 REVEL 强度对照表对号定级。两者都取不到才写"查不到"。

### GeneBe api-public 端点（已验证可用，推荐兜底）

- **基础 URL**：`https://api.genebe.net/cloud/api-public/v1`
- **步骤 1（HGVS→坐标）**：
  ```
  curl "https://api.genebe.net/cloud/api-public/v1/convert?id=<URL编码的HGVS如 F7:c.656C>A>&genome=hg38"
  # 返回 [{variants:[{genome,chr,pos,ref,alt}]}]，取 chr/pos/ref/alt
  ```
- **步骤 2（取全字段注释）**：
  ```
  curl "https://api.genebe.net/cloud/api-public/v1/variant?chr=<chr>&pos=<pos>&ref=<ref>&alt=<alt>&useRefseq=true&useEnsembl=false&genome=hg38"
  ```
- **返回中与本证据相关的关键字段**（在 `variants[0]` 中；**仅限以下基础注释字段可用于取数**）：
  | 字段 | 说明 |
  |---|---|
  | `revel_score` / `revel_prediction` | REVEL 分数与预测（对号 REVEL 强度表） |
  | `alphamissense_score` / `alphamissense_prediction` | AlphaMissense（辅助核对） |
  | `bayesdelnoaf_score` / `bayesdelnoaf_prediction` | BayesDel（辅助核对） |
  | `spliceai_max_score` / `spliceai_max_prediction` | SpliceAI（阈值 >0.2 判剪接影响，来源：Jaganathan et al. Cell. 2019;176(3):535-548，PMID 30661751，https://spliceailookup.broadinstitute.org/） |
  | `computational_prediction_selected` / `computational_score_selected` / `computational_source_selected` | 选定主预测工具与分数 |
  | `gnomad_exomes_af` / `gnomad_genomes_af` / `frequency_reference_population` | 人群频率（供 PM2/BS1 参考） |

> **铁律（GeneBe 边界）**：GeneBe 仅限基础注释取数（转录本/核苷酸改变/氨基酸改变/外显子/hg19坐标/软件预测分值）。**其返回的评级判断字段 `acmg_classification` / `acmg_criteria` / `acmg_score` / `clinvar_classification` / `clinvar_submissions_summary` 等，对变异证据的判断一律不可用**，不得作为 PP3/BP4（或其他任何证据码）的判定依据。本 SKILL 判定 PP3/BP4 一律以 `revel_score`（REVEL 强度对照表）为准；GeneBe/ClinVar 的任何评级字段均不引用，只在"查询路径"如实注明实际所用基础注释通道与返回分值。

> 示例（仅说明返回结构，非真实评级数据）：若某变异 `revel_score=0.81`，则落在 [0.773, 0.932] → **PP3_Moderate**；`revel_score=0.955` 落在 ≥0.932 → **PP3_Strong**。

## 辅助支撑要素（非编码/剪接调控深度模型，可选，仅供佐证，不改变判定标准）

以下内容**仅作为 PP3/BP4 判定"剪接/调控影响"的辅助参考**，**不改变 PP3/BP4 证据码的使用标准、阈值、等级或互斥规则**。错义变异仍以 REVEL 强度对照表为准；本小节仅用于**非编码区变异（内含子/启动子/UTR/基因间）或剪接相关变异**的调控影响辅助评估。

- **深度模型辅助（可选）**：当变异位于非编码区或影响剪接/调控时，可用序列深度模型评估该变异对调控信号的影响（辅助 PP3 的"预测有害"或 BP4 的"预测无害"方向）：
  - AlphaGenome / Enformer / Borzoi / ChromBPNet / Evo2 等：预测变异在表达、染色质可及性、TF 结合、剪接等轨道上的 Δ（alt−ref）效应。
  - **读取方式（仅辅助）**：Δ 为效应量非致病概率；跨相关组织轨道的大幅破坏可佐证 PP3 方向，近零破坏可佐证 BP4 方向；须对已知调控变异校准，不作绝对阈值。
- **约束**：深度模型预测**不能替代 REVEL/SpliceAI/CADD 等既定取数通道，也不能单独定级 PP3/BP4**；仅在与既定证据方向一致时作佐证，不得反向推翻。需要商用/非商业授权 Key（如 NVIDIA_API_KEY 等）时，按可用性与授权合规决定是否调用，缺失则写"查不到"。
- **查询入口（仅辅助取数，评级字段不可用）**：AlphaGenome / Enformer / Borzoi / ChromBPNet / Evo2 相关官方入口；SpliceAI https://spliceailookup.broadinstitute.org/ ；CADD https://cadd.gs.washington.edu/ 。

## 互斥裁决（移交收尾技能，本技能不执行）

按全局约束：**互斥原则只在收尾技能 `acmg-conflict-summary-output` 统一裁决**，证据码子技能不做互斥。本技能只做 PP3/BP4 自身预测判定，**不因与 PVS1/PS3/PM4 等码互斥而弃用、降档或拒用 PP3**；是否保留/弃用由收尾技能按证据强度与互斥矩阵统一裁决。

## 案例（指南解读 slide 40/42）

- AR c.1175C>G：REVEL=0.841 → PP3_Moderate。
- GCDH c.416C>G：REVEL=0.98 → PP3_Strong。

## BP1：错义变异，但该基因仅以 LOF 为致病机制（良性 Supporting，v1.3.0 补齐）

### 定义（原文）
BP1：该基因仅通过破坏基因功能的机制（LOF，loss-of-function）导致疾病，而该变异为错义变异。证据强度：良性 Supporting。

### 操作步骤（变异解读查询路径 5.3.2.5）
1. **确认致病机制**：通过 ClinGen 基因-疾病有效性、OMIM、文献，确认该基因致病的**唯一/主要机制为 LOF**（截短变异致病，无显性负效/功能获得证据）；
2. **变异类型核对**：本变异为**错义变异**（missense）；
3. **机制前提成立** → 若该基因疾病仅由 LOF 引起，错义变异通常不致病 → 可用 BP1；
4. **例外排除**：若该基因存在**功能获得(GOF)/显性负效(DN)错义致病**机制、或错义变异已被证实致病，则 BP1 不成立；
5. **与 PP2 的关系**：BP1（仅 LOF 机制下的错义不致病）与 PP2（错义变异为该基因主要致病机制时支持致病）是**同一机制判定的两侧**，互斥——裁决统一以收尾技能互斥矩阵为准。

> **查证通道**：ClinGen Gene-Disease Validity（基因有效性）、OMIM 疾病机制段落、已发表基因功能文献。

### 示例（教学演示，非真实评级数据）
- 某基因明确仅以无义/移码截短变异致病（LOF），某错义变异在该基因中未见致病报道 → 可考虑 BP1。

### 真实判例（已核实真实判例，查询路径可复现；评级时仍须按查询路径实际查询）

> 以下判例仅用于展示 BP1 判定路径，**禁止**作为评级数据直接套用；评级时须重新走 ClinGen 基因-疾病有效性/OMIM/文献查询。

**判例 BP1-成立（错义 + 该基因仅截断/LOF 致病 → BP1 成立）**
- 变异：**APC c.5465T>A（p.Val1822Asp），rs459552**。
- 来源：ClinVar VCV000021030.58（https://www.ncbi.nlm.nih.gov/clinvar/variation/21030/ ），**ClinGen InSiGHT 遗传性结直肠癌/息肉病 VCEP（HCCP VCEP）评审，2023-02 判 Benign（家族性腺瘤性息肉病 FAP）**。
- 权威分类：Benign（VCEP 评审，FDA 认可数据库）。
- 判定路径要点：VCEP 注释原文——"APC is defined by the HCCP VCEP as a gene for which primarily truncating variants are known to cause disease (BP1)"；该变异为错义，APC 致病以截短（LOF）为主，故 BP1 成立。本例同时叠加 BA1（gnomAD v2.1.1 非洲人群 MAF 0.9598 > APC VCEP BA1 阈值 >0.1%），但 **BP1 本身独立成立**（错义 + LOF-only 机制）。

**判例 BP1-不成立（基因存在错义/DN/GOF 致病机制 → BP1 前提不成立）**
- 依据：**FBN1 VCEP 规范原文——"BP1: Missense variant in a gene for which primarily truncating variants are known to cause disease. FBN1 VCEP: not applicable."**（马凡综合征以 FBN1 错义/半剂量不足/显性负效为主要致病机制，并非 LOF-only）。
- 判定路径要点：FBN1 相关 VCEP 明确将 BP1 标注为 **not applicable**，即"该基因仅截断致病"这一前提不成立，任何 FBN1 错义变异都不得套 BP1。同理，凡 OMIM/ClinGen 基因-疾病有效性显示该基因存在 GOF/DN 错义致病例外（如 RASopathy 基因、TP53、RUNX1 等），BP1 一律不成立。
- 出处：ClinGen FBN1 VCEP Specifications（可经 cspec.genome.network 检索 FBN1 VCEP 条目复核）。

### 穷尽检索专项 / 判定完成闸（BP1）
判定 BP1 前**必须**完成：
1. **机制前提检索**：ClinGen 基因-疾病有效性（Gene-Disease Validity）+ OMIM 致病机制段落 + 已发表基因功能文献，三方确认该基因致病**仅/主要为 LOF（截短/无义/移码/剪接 LOF）**，无 GOF/DN 错义致病报道；
2. **例外排除检索**：ClinVar/文献检索该基因是否已有错义致病变异或 DN/GOF 机制报道——若有，则 BP1 **不成立出口**：写"该基因存在错义/GOF/DN 致病机制，BP1 不成立"；
3. **变异类型核对**：本变异确为错义（missense）；
4. **不成立出口**：机制前提检索不到、或检出 GOF/DN/错义致病例外、或基因-疾病有效性未达"明确 LOF-only"时，一律写"BP1 不成立"，不得默认套 BP1。

## BP7：同义/非编码变异，且不影响剪接（良性 Supporting，v1.3.0 补齐）

### 定义（原文）
BP7：同义（沉默）突变或非编码区（内含子/非剪接）变异，且已预测或证实不会影响剪接，也不会改变蛋白。证据强度：良性 Supporting。

### 操作步骤（变异解读查询路径 5.3.2.6）
1. **变异类型核对**：本变异为**同义突变（synonymous）**或**非编码区变异**（内含子深部/5'UTR/3'UTR/基因间，非剪接关键位点）；
2. **剪接影响评估（强制）**：用剪接预测工具（**SpliceAI2 优先**（v1.6.0）、SpliceAI、MaxEntScan、NNSPLICE 等）评估是否影响剪接——**SpliceAI2 `spliceai2_summary_score` ≥0.1（高召回，对应初代 0.2）或初代 SpliceAI 阈值 >0.2（Jaganathan 2019，高召回切点）判有剪接影响 → BP7 不成立（来源版本绑定：SpliceAI2 v2, 2026-10-08 / 初代 PMID 30661751）**；多个工具一致预测无剪接影响才可用；
3. **蛋白影响核对**：同义突变密码子不变（沉默）→ 不影响蛋白；若同义突变可能激活隐蔽剪接位点或改变外显子剪接调控元件（ESE/ESS），须谨慎，BP7 不成立；
4. **杂合性排除**：非编码变异须确认不在剪接供体/受体关键位点（±1,2），否则不走 BP7；
5. 剪接预测无法取得时写"查不到"，不得默认无影响而套 BP7。

> **⚠ 与 BP4 的区分**：BP4 是错义变异"计算机预测无害"（REVEL 阈值），BP7 是同义/非编码变异"不影响剪接/蛋白"——两者适用变异类型不同，不重复计。

### 示例（教学演示，非真实评级数据）
- 某基因 5'UTR 深部同义变异，SpliceAI 各分值均 <0.1，多个预测工具一致无剪接影响 → 可考虑 BP7。

### 真实判例（已核实真实判例，查询路径可复现；评级时仍须按查询路径实际查询）

> 以下判例仅用于展示 BP7 判定路径，**禁止**作为评级数据直接套用；评级时须重新取 SpliceAI 分值并核对剪接证据。

**判例 BP7-成立（同义 + SpliceAI 全低分 + 无剪接证据 → BP7 成立）**
- 变异：**SERPINC1 c.870C>T（p.Phe290=），rs370190321**。
- 来源：ClinVar VCV000293839.17（https://www.ncbi.nlm.nih.gov/clinvar/variation/293839/ ），**ClinGen 血栓性疾病 VCEP（Thrombosis VCEP）评审，2024-08 判 Likely Benign（遗传性抗凝血酶缺乏症）**。
- 权威分类：Likely Benign（VCEP 评审，FDA 认可数据库）。
- 判定路径要点：VCEP 注释——"does not code for a different amino acid (p.Phe290=)… **SpliceAI predicts no splicing impact**… ACMG/AMP criteria applied… for SERPINC1: **BP4, BP7**"。该同义变异 SpliceAI 预测无剪接影响，故 BP7 成立（同时叠加 BS1：gnomAD v2.1.1 欧洲人群 MAF 0.000373 > SERPINC1 BS1 阈值 >0.0002）。

**判例 BP7-不成立（同义但 SpliceAI 高分 + 实测致异常剪接 → BP7 不成立）**
- 变异：**BRCA2 c.516G>A（p.Lys172=，即 p.K172K）**。
- 来源：ClinVar VCV000051795.47（https://www.ncbi.nlm.nih.gov/clinvar/variation/51795/ ），**ENIGMA BRCA1/2 VCEP 评审，判 Likely Pathogenic（BRCA2 相关肿瘤易感）**。
- 权威分类：Likely Pathogenic（VCEP 评审）。
- 判定路径要点：虽为同义（沉默）变异，但 **SpliceAI delta score = 0.84（≥0.2 阈值）预测剪接影响**；患者来源 mRNA RT-PCR 实测显示外显子 6 跳跃、外显子 5+6 跳跃（均框外），minigene 证实变异等位基因无全长转录本（PMID:19267246）。**因同义变异确实破坏剪接，BP7 不成立**（反向落入 PVS1(RNA)/PM2 致病侧）。此例是"同义≠良性"的反面教材。

### 穷尽检索专项 / 判定完成闸（BP7）
判定 BP7 前**必须**完成：
1. **变异类型核对**：确认为同义（synonymous）或非剪接关键位非编码变异（非 ±1,2 供受体位点）；
2. **剪接全低分闸（强制，v1.6.0 升级 SpliceAI2 优先）**：**SpliceAI2 `spliceai2_summary_score` <0.1（高召回，对应初代 0.2）**，且**初代 SpliceAI 四通道（DS_AG/DS_AL/DS_DG/DS_DL）全部 ≤0.2**（阈值出处：SpliceAI2 v2 2026-10-08 / Jaganathan et al. *Cell* 2019;176(3):535-548，PMID 30661751；https://spliceailookup.broadinstitute.org/ ）才满足"无剪接影响"前提；**SpliceAI2 ≥0.1 或初代任一通道 >0.2** → **不成立出口**：写"BP7 不成立（SpliceAI2 ≥0.1 或 SpliceAI 任一通道 >0.2）"；
3. **实测剪接证据检索（强制）**：PubMed/ClinVar 检索该变异是否有 RT-PCR/minigene/RNA-seq 异常剪接报道——若有剪接破坏证据（即便 SpliceAI 低）→ **不成立出口**：写"BP7 不成立（有实测剪接异常证据）"；
4. **取数兜底**：SpliceAI 走官方 API；取不到时写"查不到"，**不得默认无影响而套 BP7**；
5. **与 BP4 区分**：BP7 仅适用同义/非编码，错义"预测无害"走 BP4（REVEL 阈值表），不重复计。

## 自检清单

- [ ] **BP4 使用限定条件（v1.5.0 硬闸门）**：已穷尽检索该特异变异成熟功能实验（PubMed gene+变异+酶活/转运/功能、ClinVar 功能标注、HGMD）；检出功能受损/酶活降低证据（PS3 侧）→ 已走"BP4 强制不成立"出口、回致病证据链；功能实验取不到/不明确时未默认无功能受损而给 BP4（参照 UGT1A1*6 酶活降低 PMID 9630669/19830808 不成立判例）。
- [ ] **REVEL 主通道强制优先（v1.4.0）：REVEL 能取到（VEP/dbNSFP、GeneBe api-public、MyVariant.info）时，已以 REVEL 值对照强度表定档 PP3/BP4，未用多工具共识替代 REVEL 定档；仅 REVEL 三通道全部取不到时用多工具共识兜底且最高 PP3_Supporting 并在查询路径注明（参照 var022 SLC22A5 c.338G>A REVEL=0.972→PP3_Strong 判例）。**
- [ ] 已取 REVEL 值并按表对号强度（BP4 VeryStrong/Strong/Moderate/Supporting 或 PP3 Supporting/Moderate/Strong）。
- [ ] **已按取数优先级确认渠道（v1.6.0）：错义预测走 VEP/dbNSFP（REVEL 主通道）；剪接侧优先 SpliceAI2（spliceai2_summary_score，0.1/0.25/0.5 ↔ 初代 0.2/0.5/0.8），不可达回退初代 SpliceAI 官方 API 并交叉验证；取不到时再用 GeneBe api-public 兜底；SpliceAI/CADD 走官方 API；全部取不到才写"查不到"。**
- [ ] 已从 GeneBe 返回的 `revel_score` 取值，未用 `acmg_classification`/`clinvar_classification` 代替判定（GeneBe 评级字段一律不可用）。
- [ ] 已参考保守性预测与 Pubvar。
- [ ] **BP1：已确认该基因仅 LOF 机制致病、本变异为错义、且无 GOF/DN 错义致病例外（v1.3.0）。**
- [ ] **BP7：已确认同义/非编码且位于非剪接关键位点，SpliceAI2（≥0.1）或 SpliceAI 等预测无剪接影响（>0.2 判有影响则 BP7 不成立），剪接预测取不到时未默认无影响而套 BP7（v1.3.0/v1.6.0）。**
- [ ] **BP1 穷尽闸（v19）：已查 ClinGen 基因-疾病有效性 + OMIM 机制 + 文献确认 LOF-only；检出 GOF/DN/错义致病或机制查不到时，已走"BP1 不成立"出口（参照 APC c.5465T>A 成立 / FBN1 VCEP not applicable 不成立 判例）。**
- [ ] **BP7 穷尽闸（v19/v1.6.0）：SpliceAI2 summary_score 已 <0.1 且 SpliceAI 四通道已全部 ≤0.2（SpliceAI2 v2 2026-10-08 / Jaganathan 2019, PMID 30661751），且已检索无 RT-PCR/minigene 剪接异常报道（参照 SERPINC1 c.870C>T 成立 / BRCA2 c.516G>A SpliceAI 0.84 不成立 判例）；SpliceAI2 ≥0.1 或任一通道 >0.2 或有实测剪接破坏证据即判不成立。**
- [ ] 互斥裁决统一在收尾技能 `acmg-conflict-summary-output` 执行（本技能不据此弃用/降档）。

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

# ev-pp3-bp4 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此

## v1.6.2（D32 权威来源标注补全，2026-10-15）

- **D32（spliceai 阈值权威来源标注补全）**：SpliceAI2 阈值映射段标"权威来源=config/thresholds.json → `spliceai.v2_thresholds`，判定统一走 `acmg_evidence.py spliceai_band`（D31 联动，读 config 不硬编码）"。纯标注增强，不改阈值与判定规则。


## 本版新增（预测工具网址+GeneBe兜底通道）

- 本版新增各预测工具官方网址与当前调用方式，并补充 **GeneBe api-public 端点作为正式兜底取数通道**（REVEL/AlphaMissense/BayesDel/SpliceAI/gnomAD/ClinVar 全字段，替代被 robots 反爬拦截的 genebe api-x 老端点）。

## v1.3.0

- 同技能补齐 BP1 与 BP7（良性 Supporting）判定段——BP1 为错义变异但基因仅 LOF 机制（变异解读查询路径 5.3.2.5，需排除 GOF/DN 错义致病例外）；BP7 为同义/非编码变异且不影响剪接（变异解读查询路径 5.3.2.6，SpliceAI 阈值 >0.2 判有剪接影响则 BP7 不成立，剪接预测取不到不得默认无影响）。

## v1.4.0

- REVEL 主通道强制优先（整改 P1，实证 var022 SLC22A5 c.338G>A——技能群取多工具共识给 PP3_Supporting，金标准 REVEL=0.972≥0.932 → PP3_Strong，通道遗漏致偏低）：REVEL 能取到（VEP/dbNSFP、GeneBe api-public、MyVariant.info 任一通道）时，**必须以 REVEL 值对照强度表定档**，多工具共识（CADD+SIFT+PolyPhen 等）**不得替代 REVEL 定档**，只能作为 REVEL 全部通道取不到时的兜底且仅佐证方向/Supporting 上限。

## v1.5.0（BP4 使用限定条件硬闸门）

- 给 BP4 前必须穷尽检索该特异变异的成熟功能实验——检出功能受损/酶活降低证据（PS3 侧，如 UGT1A1*6 酶活降低 PMID 9630669/19830808）时，BP4（预测无害）与功能实验冲突，功能实验优先，BP4 强制不成立、回致病证据链；功能实验检索取不到/不明确时不得默认无功能受损而给 BP4（实证 UGT1A1 c.211G>A 预测良性但功能受损被误给 BP4）。

## v1.6.1（阈值双写同步标注，2026-10-15）

- REVEL 强度对照表头补「权威来源 = `config/thresholds.json` → `revel`，改切点必须在 thresholds.json + 本表 + `scripts/acmg_evidence.py::revel_band` 三处同步（sync-manifest §10）」——纯文档增强，阈值/规则不变。

## v1.6.0（SpliceAI2 剪接侧升级通道，直接接入）

- 本技能 PP3 的剪接侧（剪接相关/非编码变异预测有害）、BP7 剪接影响判定、BP4 剪接无害侧，新增 SpliceAI2 作为剪接预测主升级通道——`spliceai2_summary_score`（0-1）阈值：0.1=高召回（对应初代 SpliceAI 0.2，Jaganathan 2019）、0.25=平衡（对应 0.5）、0.5=高精度（对应 0.8）；来源版本绑定 SpliceAI2 v2（Illumina BioInsight AI Lab，2026-10-08，technical article + manuscript preprint，GitHub `Illumina/SpliceAI2`，预计算 40 亿 SNV + 1.5 亿 indel，学术免费，PyPI 安装需 CUDA GPU）；SpliceAI2 只做实剪接侧，**不替代 REVEL 错义主通道**；SpliceAI2 不可达/无 GPU 时回退初代 SpliceAI 官方 API（spliceailookup）0.2 高召回切点并交叉验证，标注来源版本。

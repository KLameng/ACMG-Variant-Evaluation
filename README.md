# ACMG 单病变异评级技能群

对孟德尔疾病相关基因序列变异进行 ACMG/AMP 2015 致病性分类的成套技能（23 个技能 = 1 总调度 + 1 收尾 + 1 遗传方式前置 + 19 证据码子技能 + 1 个 VCEP 数据载体 `clingen-vcep`）。

## 技能构成

| 层级 | 技能 | 职责 |
|---|---|---|
| 总调度（唯一入口） | `acmg-total-scheduler` | 变异身份归一化 → 遗传方式前置 → 按变异类型圈定证据码池 |
| 遗传方式前置 | `arad-inheritance-judgment` | AD/AR/多模式/LOF 机制判定（依赖遗传模式的证据码须先调用） |
| 收尾（互斥汇总） | `acmg-conflict-summary-output` | 互斥消解、赋分累加、经典联合规则 + Tavtigian 双套定级 |
| 证据码子技能 | `ev-*`（PVS1/PS1-PM5/PM1-PM4/PP1-PP4/PS2-PM6/PS3-BS3/PS4/BS1-BS2/PP3-BP4/PM4/文献等 19 个） | 逐码判定，输出证据码+等级/数据+规则/查询路径 |
| VCEP 载体 | `clingen-vcep` | 已装载基因按基因特异性规则判定（仅辅助，须联网核实 ClinGen cspec 最新版） |

## 安装与依赖

```bash
pip install -r requirements.txt   # 核心：requests>=2.28
```

涉及 `requests` 的技能：`ev-gene-identity` / `ev-disease-info` / `ev-variant-literature-patient` / `arad-inheritance-judgment`。建议在隔离 venv 中安装。

`ev-gnomad-constraint` / `ev-pp2` 的 `query_constraint.py` 仅依赖 Python 标准库（gnomAD GCS 公共存储桶，无需 API 认证）。

## 环境变量（可选）

| 变量 | 用途 | 默认 |
|---|---|---|
| `NCBI_EMAIL` | NCBI E-utilities 联系邮箱（建议设真实邮箱规避限流） | `variant-rating-skill@example.com` |
| `GNOMAD_INSECURE=1` | 仅证书错位时临时降级 SSL 校验 | 严格校验证书（安全优先） |

## 数据与缓存

- gnomAD 约束数据（v4 ≈82MB / v2 ≈13MB）：首次查询落盘到各脚本同目录 `_cache/`，后续直接读缓存；`python query_constraint.py <gene> --refresh` 强制更新。
- VCEP 载体：`clingen-vcep/gene-gn-file-mapping.csv`（131 基因，132 行含表头）+ `narrative-units/`（1721 单元）。⚠ 该载体仅为快速检阅通道，**非最终依据**；每次用到 VCEP 规则必须联网核实 ClinGen cspec 最新版，以数据库最新更新为准。

## 外部依赖与断链说明

- **HGMD**（`hgmd-variant-query`）：商业数据库，未随包提供；需自行采购授权后接入，未接入时相应证据码走 ClinVar/文献检索通道并标注。
- **火山方舟**（`ARK_API_KEY`）：默认端点 `ep-20260106113130-tj2pt` 为私有付费端点，非通用可用；使用前须替换为自有可用 endpoint，否则按"查不到"出口处理，不得静默用默认值。

## 目录结构

```
acmg-total-scheduler/           总调度
acmg-conflict-summary-output/   收尾
arad-inheritance-judgment/      遗传方式前置
clingen-vcep/                   VCEP 载体（映射表 + narrative-units + knowledge-base）
ev-*/                           证据码子技能（各含 SKILL.md [+ 脚本 + CHANGELOG.md]）
requirements.txt / README.md    依赖与说明（随包分发）
```

## 随包门禁与自检（v5.2.0 起随包交付）

以下回归/评测/契约工具**随包分发**，解压即可在包内自检（相对路径，不依赖构建环境）：

| 文件 | 作用 | 运行 |
|---|---|---|
| `config/golden.json` | 双尺子金标准（39 条，methodA 经典联合 / methodB 分值；暂用版，随金标准更新重建） | 评测输入快照 |
| `scripts/combination_eval.py` | 组合层分口径评测（同尺子对同尺子：engine_a vs methodA / engine_b vs methodB） | `python scripts/combination_eval.py`（默认读 config/golden.json） |
| `scripts/regression_gate.py` | 回归门禁：穷举 328 对照 + 引擎/CLI 冒烟 + 39 集双尺子评测（SKIP>0 视为失败）+ 版本一致性 | `python scripts/regression_gate.py` |
| `scripts/contract_test.py` | L1→L2 输入契约测试（官方裁定形态 / 复合码方向） | `python scripts/contract_test.py` |
| `scripts/golden_builder.py` | golden.json 生成说明（输入 39 变异集仅在构建环境，重建时指明输入路径） | 构建侧工具 |
| `sync-manifest.md` | **变更同步载体清单**：改任何"口径/枚举/识别串/契约"前先读它（confidence 边界 / interval 枚举 / 官方识别串 / BA1 门控 / 版本号 / 可疑文献 / 提交门禁 七组），防"改了数据层漏了文档层"连续复发 | **随包治理资产，改前必读** |

- 一致率声明以随包 `config/golden.json` 为基准，解压后运行 `scripts/combination_eval.py` 即可复现。
- **一致率双分母（口径诚实，v5.3.3）**：39 集暂用金标准实测——**表5一致率 93.8%（15/16，仅 basis=Table5 精选子集）/ 全量不筛 basis 51.3%（20/39）**；**分值一致率 97.1%（34/35，剔除 VCEP 官方 4 条）/ 官方遵循率 100%（4/4）**；两套引擎 agreement 97.4%（38/39）（v5.5.6 补 1VS+1SU→LP 后由 66.7% 26/39 上升）。并列"精选/全量"与"含官方/剔除官方"分母，不写单一高值；官方裁定条目按最高真值层单独统计（只验证"技能群是否优先采官方"），不混入引擎一致率。
- 打包门禁（`build_package` 五闸：README 数字 + 嵌句检测 + py_compile + 契约测试 + 回归门禁）**仅在构建环境**运行，不随包（构建产物不含构建脚本）。

## 整改记录（2026-10-15）

- 各技能 version 变更日志已从 SKILL.md frontmatter 下沉至各技能目录 `CHANGELOG.md`，description 精简为职责+触发（≤300 字符）。
- 可疑文献 L1/L2/L3 判定标准唯一收敛至 `ev-variant-literature-patient`，其余子技能仅单点引用。
- gnomAD 查询恢复 SSL 证书校验 + 落盘缓存；NCBI 联系邮箱改为环境变量。

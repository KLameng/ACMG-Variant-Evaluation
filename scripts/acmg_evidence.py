# -*- coding: utf-8 -*-
"""ACMG 评级技能群 · 确定性证据档位引擎 acmg_evidence.py

把各 ev-* 子 SKILL 中"数据值 → 证据码强度档位"的纯查表 / 累分逻辑脚本化，
替代 LLM 手工查表（防档位标错、累分错误、中空档误判）。阈值统一读 config/thresholds.json；
缺失的强度表以带 source+version 的内联常量给出（与对应子 SKILL 的现行口径一致）。

设计铁律：
- 本引擎只做"数据 → 档位"的确定性映射，不做取数 / 文献核验 / 语义判断；
- 输入"数据值"由各子 SKILL（LLM/库查询）提取；取不到则返回 None 并说明，不得默认档位；
- 每个函数返回 (档位, 依据说明)；档位格式如 "PM2_Supporting"、"PP3_Strong"、"PM3_Moderate"；
  不成立时返回 (None, "不成立原因")，供子 SKILL 写入"查不到/不适用"。

用法：python acmg_evidence.py 函数名 参数...
或：import acmg_evidence; acmg_evidence.revel_band(0.972)
"""
import json
import os
import math

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = os.path.join(BASE, "config", "thresholds.json")


def _load():
    with open(CONF, encoding="utf-8") as f:
        return json.load(f)


T = _load()


# ============ 1. REVEL → PP3/BP4 档位（thresholds.revel；指南解读 slide 53/Table 2） ============
def revel_band(revel):
    """REVEL 值 → PP3_Strong/Moderate/Supporting 或 BP4_VeryStrong/Strong/Moderate/Supporting。
    中空档 (0.290, 0.644) → PP3/BP4 均不适用（必须返回 None，不得默认任一侧）。"""
    r = T["revel"]
    if revel is None:
        return None, "REVEL 取不到"
    # D31（2026-10-15）：依据说明从 config 格式化，禁止硬编码字面量——改 config 后逻辑与打印必须同步
    if revel >= r["pp3_strong_min"]:
        return "PP3_Strong", f"REVEL={revel} ≥{r['pp3_strong_min']} → PP3_Strong"
    if revel >= r["pp3_moderate_min"]:
        return "PP3_Moderate", f"REVEL={revel} ∈[{r['pp3_moderate_min']},{r['pp3_strong_min']}) → PP3_Moderate"
    if revel >= r["pp3_supporting_min"]:
        return "PP3_Supporting", f"REVEL={revel} ∈[{r['pp3_supporting_min']},{r['pp3_moderate_min']}) → PP3_Supporting"
    if revel <= r["bp4_very_strong_max"]:
        return "BP4_VeryStrong", f"REVEL={revel} ≤{r['bp4_very_strong_max']} → BP4_VeryStrong"
    if revel <= r["bp4_strong_max"]:
        return "BP4_Strong", f"REVEL={revel} ∈({r['bp4_very_strong_max']},{r['bp4_strong_max']}] → BP4_Strong"
    if revel <= r["bp4_moderate_max"]:
        return "BP4_Moderate", f"REVEL={revel} ∈({r['bp4_strong_max']},{r['bp4_moderate_max']}] → BP4_Moderate"
    if revel <= r["bp4_supporting_max"]:
        return "BP4_Supporting", f"REVEL={revel} ∈({r['bp4_moderate_max']},{r['bp4_supporting_max']}] → BP4_Supporting"
    return None, f"REVEL={revel} 落中空档 ({r['bp4_supporting_max']},{r['pp3_supporting_min']})，PP3/BP4 均不适用"


# ============ 2. PM2 AF → 档位（ev-pm2 第3.5步：AD/XL 0.0005、AR 0.001；特异性阈值优先） ============
def pm2_band(af, mode="AD", gene_specific=None):
    """PM2：AF vs 阈值 → 档位。mode=AD/XL|AR；gene_specific 为基因/疾病特异性阈值（优先）。
    满足阈值 → PM2_Supporting（ev-pm2 自检口径，SVI 降级）；AF=0 → Supporting。"""
    pm2 = T["pm2"]
    if af is None:
        return None, "AF 取不到"
    if gene_specific is not None:
        th, src = gene_specific, f"基因特异性阈值 {gene_specific}"
    else:
        # 读配置表"本实验室现行通用口径"（af_lab_generic），与子技能 ev-pm2 口径一致
        lab = pm2.get("af_lab_generic", {})
        th = lab.get(mode.upper(), lab.get("AD", 0.0005))
        src = f"{mode} 通用阈值 {th}（af_lab_generic，{lab.get('version','lab-v1')}）"
    if af < th:
        return "PM2_Supporting", f"AF={af} < 阈值{th}（{src}）→ PM2_Supporting"
    return None, f"AF={af} ≥ 阈值{th}（{src}），PM2 不成立（罕见前提不满足）"


# ============ 3. PM3 反式累分 → 档位（ev-pm3 计分表 + 第3步强度表） ============
def pm3_points(examples, phase_A=0, phase_B_P=0, phase_B_LP=0, homozyg=0, vus_trans=0):
    """PM3 累分：examples 为逐例清单[权重]，或直接传各分档例数。
    权重（ev-pm3 计分表 / thresholds.pm3_score）：
      confirmed in trans(A) 1.0；phase-unknown P(B-P) 0.5、LP(B-LP) 0.25；纯合 0.5(封顶1.0)；VUS 0.25。
    强度（第3步表）：<0.5→不计/Supporting? ；0.5→Supporting；1.0–1.9→Moderate；2.0–3.9→Strong；≥4.0→VeryStrong。
    """
    pm3 = T["pm3_score"]
    weights = {
        "A": pm3["confirmed_in_trans"], "B_P": pm3["phase_unknown_P"],
        "B_LP": pm3["phase_unknown_LP"], "hom": pm3["homozygous"], "VUS": pm3["VUS_in_trans"],
    }
    caps = {"hom": pm3.get("homozygous_cap", 1.0), "VUS": pm3.get("VUS_cap", 0.5)}
    # 逐例累分（examples 每项形如 {"type": "A"|"B_P"|"B_LP"|"hom"|"VUS", "n": 例数}）
    total = 0.0
    detail = []
    for ex in examples or []:
        typ = ex.get("type", "A")
        n = ex.get("n", 1)
        w = weights.get(typ)
        if w is None:
            continue
        if typ in caps:
            # 纯合封顶 1.0 / VUS 封顶 0.5（官网核对 Q9：表 'VUS 变异（上限 0.5）'，引擎此前漏实现）
            add = min(caps[typ], w * n)
        else:
            add = w * n
        total += add
        detail.append(f"{typ}×{n}(w={w})=+{add:.2f}")
    if total < 0.5:
        return None, f"PM3 累分={total:.2f} <0.5，不足以定档（若为反式例但相位无佐证→按 C 不计分）"
    if total >= 4.0:
        band = "PM3_VeryStrong"
    elif total >= 2.0:
        band = "PM3_Strong"
    elif total >= 1.0:
        band = "PM3_Moderate"
    else:
        band = "PM3_Supporting"
    return band, f"PM3 累分={total:.2f}（{' + '.join(detail)}）→ {band}"


# ============ 4. PP1 共分离 LOD → 档位（ev-pp1：AD/XL LOD 公式；强度表） ============
def pp1_lod_adxl(segregations):
    """PP1 显性/XL：LOD = log10(1 / 0.5^segregations)。
    强度（phenocopy 不成立，阈值读 config pp1_lod，ClinGen 共识 0.9/1.5/2.1，来源 Jarvik & Browning 2016 PMID 27495972）：Supporting LOD≥0.9；Moderate ≥1.5；Strong ≥2.1。"""
    pp1 = T.get("pp1_lod", {"supporting": 0.9, "moderate": 1.5, "strong": 2.1})
    if segregations is None or segregations < 2:
        return None, "共分离分离次数不足"
    lod = math.log10(1 / (0.5 ** segregations))
    if lod >= pp1["strong"]:
        band = "PP1_Strong"
    elif lod >= pp1["moderate"]:
        band = "PP1_Moderate"
    elif lod >= pp1["supporting"]:
        band = "PP1_Supporting"
    else:
        band = None
    return band, f"分离次数={segregations} → LOD={lod:.2f} → {band if band else '不成立'}（阈值 {pp1['supporting']}/{pp1['moderate']}/{pp1['strong']}）"


def pp1_lod_ar(affected, unaffected, parental_both_carrier=True, gene=None):
    """PP1 隐性：LOD = log10(1 / (0.25^(affected-1) × 0.75^unaffected))（父母均携带者典型模型）；
    若父母一方携带者一方患病，用 0.5/0.5。返回 LOD（强度映射同 AD/XL，读 config pp1_lod：0.9/1.5/2.1）。

    ⚠ HL VCEP 闸（v1.6.0/证据层强制）：传 gene 且命中 HL VCEP 覆盖基因（如 USH2A）时，
    自动改用 HL VCEP 官方口径 pp1_lod_hl_ar（受累个体数含先证者、分离数=个体数−1、阈值 0.6/1.2/1.5）；
    无 gene 或未命中则保持通用口径。注（v1.6.1 归因修正）：通用版 0.25^(affected-1) 与官网 −1 口径一致，
    数值无"排除先证者"问题；通用版档位偏低的真实原因是阈值错配——通用 0.9/1.5/2.1 是 AD(LOD 底数0.5)阈值，
    套在 AR(底数0.25) LOD 上偏低；HL VCEP 基因必须走官方 0.6/1.2/1.5 阈值，禁用通用阈值。"""
    if gene is not None and _in_hl_vcep(gene):
        return pp1_lod_hl_ar(affected, unaffected)
    pp1 = T.get("pp1_lod", {"supporting": 0.9, "moderate": 1.5, "strong": 2.1})
    if affected is None or affected < 2:
        return None, "患者分离次数不足（AR 需 ≥2 患者）"
    p_aff, p_un = (0.25, 0.75) if parental_both_carrier else (0.5, 0.5)
    lod = math.log10(1 / (p_aff ** (affected - 1) * p_un ** max(unaffected or 0, 0)))
    if lod >= pp1["strong"]:
        band = "PP1_Strong"
    elif lod >= pp1["moderate"]:
        band = "PP1_Moderate"
    elif lod >= pp1["supporting"]:
        band = "PP1_Supporting"
    else:
        band = None
    return band, f"AR 患者={affected} 非患者={unaffected or 0} → LOD={lod:.2f} → {band if band else '不成立'}（通用口径，阈值 {pp1['supporting']}/{pp1['moderate']}/{pp1['strong']}）"


def _in_hl_vcep(gene):
    """HL VCEP（GN005）覆盖基因锚点（非穷举）：命中即 PP1 须走官方口径。来源：ClinGen Hearing Loss EP。
    锚点集以常用遗传性耳聋基因为主，HL 相关基因遇不确定回官方核对，不得因锚点漏列而误用通用口径。"""
    hl = {"USH2A", "GJB2", "MYO15A", "OTOF", "SLC26A4", "CDH23", "MYO7A", "TMPRSS3", "TMC1", "STRC", "LOXHD1", "TRIOBP", "PCDH15", "GJB6", "KCNQ4"}
    return gene.strip().upper() in hl


def pp1_lod_hl_ar(affected, unaffected):
    """HL VCEP（GN005）PP1 AR 官方口径（v1.6.1 修正 off-by-one）：LOD = log10(1/(0.25^(affected-1) × 0.75^unaffected))，
    affected = 受累个体数（含先证者），受累分离数 = affected − 1（官网 v2 明文："do not count probands as a
    segregation；Affected segregations = # affected individuals − 1"）；unaffected 不含携带者父母；
    阈值 0.6/1.2/1.5（4:1/16:1/32:1，HL VCEP v2 Table 2 / General Recommendations）。来源：ClinGen HL EP v2 PMID 30311386。"""
    hlv = T.get("hl_vcep_pp1", {"supporting": 0.6, "moderate": 1.2, "strong": 1.5})
    if affected is None or affected < 2:
        return None, "HL VCEP AR 受累分离数不足（受累个体数含先证者需 ≥2，分离数=个体数−1；仅先证者分离数=0）"
    lod = math.log10(1 / (0.25 ** (affected - 1) * (0.75 ** max(unaffected or 0, 0))))
    if lod >= hlv["strong"]:
        band = "PP1_Strong"
    elif lod >= hlv["moderate"]:
        band = "PP1_Moderate"
    elif lod >= hlv["supporting"]:
        band = "PP1_Supporting"
    else:
        band = None
    return band, f"受累个体数(含先证者)={affected} 受累分离数=个体数−1={affected-1} 非患者={unaffected or 0} → LOD={lod:.2f} → {band if band else '不成立'}（HL VCEP v2 官方口径，阈值 {hlv['supporting']}/{hlv['moderate']}/{hlv['strong']}）"


# ============ 5. PS4 先证者数 / OR → 档位（ev-ps4 VCEP 表 + 通用） ============
PS4_VCEP = {
    # gene/disease -> (Supporting, Moderate, Strong) 先证者阈值
    # 注意判据统一为 `>=`：MYH7/HL/RASopathy 表用 ≥ 直接存；PTEN/CDH1 表用 >1/>2/>4
    # （严格大于），等价于 ≥2/≥3/≥5，故存 (2,3,5)，避免引擎比表低 1 档（官网核对 Q4）。
    "MYH7": (2, 6, 15), "HL": (2, 6, 15),
    "RASopathy": (1, 3, 5),
    "PTEN": (2, 3, 5), "CDH1": (2, 3, 5),  # 表语义 >1/>2/>4 = ≥2/≥3/≥5
}


def ps4_band(probands, gene=None, ar=False):
    """PS4：先证者数 → 档位。gene 命中 VCEP 表用表内阈值；否则按通用：
      AD/XL 罕见病例对照无统计意义但 AF 符合 PM2 且有多个相同表型患者 → 随患者数下降：≥2→Supporting，≥6→Moderate，≥15→Strong。
    AR 需 OR>5 且 CI 不含 1（见 ps4_or_ci）。"""
    if probands is None:
        return None, "先证者数取不到"
    if gene and gene in PS4_VCEP:
        sup, mod, st = PS4_VCEP[gene]
        if probands >= st:
            return "PS4_Strong", f"{gene} VCEP：先证者 {probands} ≥{st} → PS4_Strong"
        if probands >= mod:
            return "PS4_Moderate", f"{gene} VCEP：先证者 {probands} ≥{mod} → PS4_Moderate"
        if probands >= sup:
            return "PS4_Supporting", f"{gene} VCEP：先证者 {probands} ≥{sup} → PS4_Supporting"
        return None, f"{gene} VCEP：先证者 {probands} <{sup}，PS4 不成立"
    # 通用
    if probands >= 15:
        return "PS4_Strong", f"通用：先证者 {probands} ≥15 → PS4_Strong"
    if probands >= 6:
        return "PS4_Moderate", f"通用：先证者 {probands} ≥6 → PS4_Moderate"
    if probands >= 2:
        return "PS4_Supporting", f"通用：先证者 {probands} ≥2（AF 符合 PM2 时）→ PS4_Supporting"
    return None, f"通用：先证者 {probands} <2，PS4 不成立"


def ps4_or_ci(cases_exposed, cases_control, ctr_exposed, ctr_control):
    """PS4 OR 与 95%CI（AR 必需：OR>5 且 CI 不含 1）。
    输入 2×2：cases_exposed=cases 携带者数，cases_control=cases 未携带；ctr_exposed=对照携带者，ctr_control=对照未携带。
    返回 (OR, CI_low, CI_high)；用 Haldane 校正处理零单元格。"""
    a, b, c, d = cases_exposed, cases_control, ctr_exposed, ctr_control
    # Haldane 零校正
    a2, b2, c2, d2 = a + 0.5, b + 0.5, c + 0.5, d + 0.5
    or_ = (a2 * d2) / (b2 * c2)
    ln_or = math.log(or_)
    se = math.sqrt(1 / a2 + 1 / b2 + 1 / c2 + 1 / d2)
    ci_low = math.exp(ln_or - 1.96 * se)
    ci_high = math.exp(ln_or + 1.96 * se)
    return or_, ci_low, ci_high


# ============ 6. SpliceAI 剪接影响 → 档位（thresholds.spliceai） ============
def spliceai_band(score, version="v2"):
    """SpliceAI 分数 → 剪接影响判定。
    v2（SpliceAI2）：0.1=Supporting(高召回)、0.25=Moderate、0.5=Strong；
    v1：>0.2 判有剪接影响（高召回档）。返回 (影响, 说明)。
    ⚠ 版本绑定（官网核对 Q10）：调用方必须按取数通道显式传 version——取数来自 SpliceAI2 预计算/引擎默认 → v2；
    取数来自初代 SpliceAI（如部分 VCEP 原文刻度 ≤0.1/≤0.2）→ v1。禁止默认 v2 却喂初代分数（[0.1,0.2) 区间方向会误判）。"""
    sa = T["spliceai"]
    if score is None:
        return None, "SpliceAI 分数取不到"
    # D31（2026-10-15）：依据说明从 config 格式化，禁止硬编码字面量（改 config 后逻辑与打印同步）
    if version == "v2":
        v2 = sa["v2_thresholds"]
        if score >= v2["strong"]:
            return "影响(Strong)", f"SpliceAI2 score={score} ≥{v2['strong']} → 强剪接影响"
        if score >= v2["moderate"]:
            return "影响(Moderate)", f"SpliceAI2 score={score} ≥{v2['moderate']} → 中度剪接影响"
        if score >= v2["supporting"]:
            return "影响(Supporting)", f"SpliceAI2 score={score} ≥{v2['supporting']} → 支持剪接影响"
        return "无影响", f"SpliceAI2 score={score} <{v2['supporting']} → 无剪接影响"
    else:  # v1
        if score > sa["v1_threshold"]:
            return "影响", f"SpliceAI v1 score={score} >{sa['v1_threshold']}（高召回档）→ 判有剪接影响"
        return "无影响", f"SpliceAI v1 score={score} ≤{sa['v1_threshold']} → 无剪接影响"


# ============ 7. PS1 / PM5 映射（ev-ps1-pm5：同氨基酸→PS1，异氨基酸→PM5） ============
def ps1_pm5_band(same_aa, known_class, other_p_count=0):
    """PS1/PM5 档位：
      same_aa=True（同密码子同氨基酸，不同核苷酸）→ PS1：known_class=P→PS1(强)；known_class=LP→PS1_Moderate；
      same_aa=False（同一位置不同氨基酸，且该等位已确立 P/LP）→ PM5：
          known_class=LP（1 个其他氨基酸 LP）→PM5_Supporting；known_class=P（1 个其他氨基酸 P）→PM5_Moderate；
          2 个其他氨基酸 P → PM5_Strong。
    已知变异分类必须不依赖本证据。"""
    if same_aa:
        if known_class == "P":
            return "PS1", "同氨基酸已知 P → PS1（Strong）"
        if known_class == "LP":
            return "PS1_Moderate", "同氨基酸已知 LP → PS1_Moderate（降级）"
        return None, f"同氨基酸但已知分类={known_class}（非 P/LP），PS1 不成立"
    else:
        if other_p_count >= 2:
            return "PM5_Strong", f"{other_p_count} 个其他氨基酸为 P → PM5_Strong"
        if known_class == "P":
            return "PM5_Moderate", "1 个其他氨基酸为 P → PM5_Moderate"
        if known_class == "LP":
            return "PM5_Supporting", "1 个其他氨基酸为 LP → PM5_Supporting"
        return None, f"异氨基酸但已知分类={known_class}、其他 P 数={other_p_count}，PM5 不成立"


# ============ 8. BS1 AF → 判定（ev-bs1-bs2：AF 大于疾病发病率） ============
def bs1_band(af, prevalence, high_penetrance_early=True):
    """BS1：等位基因频率 > 疾病发病率（且疾病高外显、早发前提，由 LLM/疾病检索判断）。
    返回 (是否成立, 说明)。"""
    if af is None or prevalence is None:
        return None, "AF 或发病率取不到"
    if af > prevalence:
        return "BS1成立", f"AF={af} > 发病率={prevalence}（高外显早发前提={high_penetrance_early}）→ BS1 可考虑"
    return None, f"AF={af} ≤ 发病率={prevalence}，BS1 不成立"


def pm2_by_gene(af, gene, mode="AD"):
    """PM2 便捷入口：按基因查特异性阈值（config af_genetic，若无则回退通用 af_lab_generic）。
    消除"特异性阈值永远到不了引擎"的问题（N11）：基因特异性阈值以配置表 af_genetic 为准。"""
    pm2 = T.get("pm2", {})
    spec = (pm2.get("af_genetic") or {}).get(gene.upper()) if gene else None
    if spec is not None:
        return pm2_band(af, mode=mode, gene_specific=spec)
    return pm2_band(af, mode=mode, gene_specific=None)


# ============ CLI 入口（可选，供手动单测） ============
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        args = sys.argv[2:]
        funcs = {
            "revel_band": (revel_band, [float]),
            "pm2_band": (pm2_band, [float, str, float]),
            "pm2_by_gene": (pm2_by_gene, [float, str, str]),
            "ps4_band": (ps4_band, [int, str]),
            "pp1_lod_adxl": (pp1_lod_adxl, [int]),
            "pp1_lod_ar": (pp1_lod_ar, [int, int, str, str]),
            "pp1_lod_hl_ar": (pp1_lod_hl_ar, [int, int]),
            "spliceai_band": (spliceai_band, [float, str]),
            "bs1_band": (bs1_band, [float, float]),
        }
        if fn in funcs:
            f, conv = funcs[fn]
            # 可选参数（gene_specific/mode）不足时以 None 填充
            vals = [c(a) if i < len(args) and a != "-" else None
                    for i, (c, a) in enumerate(zip(conv, args))]
            print(f(*vals))
        else:
            print("用法: python acmg_evidence.py 函数名 参数...")
    else:
        # 自检样例
        for r in [0.972, 0.841, 0.955, 0.91, 0.05, 0.5]:
            print(revel_band(r))
        print(pm2_band(0.00005, "AD"))
        print(pm2_band(0.0008, "AR"))
        print(pm3_points([{"type": "A", "n": 1}]))
        print(pm3_points([{"type": "hom", "n": 2}]))
        print(pm3_points([{"type": "B_P", "n": 4}]))
        print(pp1_lod_adxl(4))
        print(pp1_lod_ar(3, 0))
        print(pp1_lod_hl_ar(3, 0))
        print(pp1_lod_ar(3, 0, True, "USH2A"))
        print(ps4_band(2, "MYH7"))
        print(ps4_band(16, None))
        print(spliceai_band(0.15, "v2"))
        print(spliceai_band(0.5, "v1"))
        print(ps1_pm5_band(True, "P"))
        print(ps1_pm5_band(False, "P", 2))
        print(bs1_band(0.02, 0.002))

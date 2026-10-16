#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contract_test.py — L1→L2 输入契约测试（收敛计划 P3，纳入打包门禁）
验证组合层输入契约（input-schema.md）四条硬性：
  1. 官方裁定带 class → 短路，不按通用规则
  2. 官方裁定无 class（level 不含分类）→ official_pending，不得按 VUS 处置
  3. 官方裁定可从 status 描述文字提取分类（var005/006/030/038 形态）→ 短路官方
  4. 复合码方向限定：PS2/PM6 同向只计一次；PP3/BP4、PM2/BA1 对向 skip（不双计/不抵消/不推良性）
任一 FAIL → 退出码 1。
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(HERE, "acmg_combine.py")  # 相对路径：引擎同目录（随包可移植）

fails = 0
passed = 0


def ok(name, cond, detail=""):
    global fails, passed
    if cond:
        passed += 1
        print(f"  [PASS] {name}  {detail}")
    else:
        fails += 1
        print(f"  [FAIL] {name}  {detail}")


def cli_ev(ev):
    r = subprocess.run([sys.executable, SC, "-e", json.dumps(ev, ensure_ascii=False)],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout, r.stderr


def has(out, *kws):
    return all(k in out for k in kws)


# 1. 官方带 class 短路
rc, out, err = cli_ev([{"code": "VCEP官方裁定", "level": "官方", "class": "Pathogenic"}])
ok("官方带 class → 短路 Pathogenic", rc == 0 and has(out, "官方", "Pathogenic"), f"rc={rc}")

# 2. 官方无 class → official_pending，不得按 VUS
rc, out, err = cli_ev([{"code": "VCEP官方裁定", "level": "官方"}])
ok("官方无 class → official_pending（不按 VUS）",
   rc == 0 and "official_pending" in out and "待上游补官方分类" in out and "不得按通用 VUS" in out, f"rc={rc}")

# 3. 官方可从 status 描述提取分类（var005/006/030/038 形态）
for status, expect in [
    ("Hearing Loss VCEP GN023：PP3+PM3_VS+PP4+PP1_S→致病", "Pathogenic"),
    ("ClinGen Hearing Loss 专家组共识：AR NSHL 致病、可变外显", "Pathogenic"),
    ("ClinGen Hemoglobinopathy VCEP GN170：VCV15458=Pathogenic（15 confirmed trans）", "Pathogenic"),
]:
    rc, out, err = cli_ev([{"code": "VCEP官方裁定", "level": "官方", "status": status}])
    ok(f"官方 status 补分类 → {expect}", rc == 0 and expect in out, f"rc={rc}")

# 4a. 复合码同向只计一次（PS2/PM6）
rc, out, err = cli_ev({"PS2/PM6": "Moderate"})
ok("复合码同向只计一次（PS2/PM6→1条 Moderate）", rc == 0 and "PM6" not in out and "Moderate" in out, f"rc={rc}")

# 4b. 复合码对向 skip（PP3/BP4 不双计不抵消）
rc, out, err = cli_ev({"PP3/BP4": "Supporting"})
ok("复合码对向 skip（PP3/BP4 不双计不抵消）", rc == 0, f"rc={rc}")

# 4c. 复合码对向 skip（PM2/BA1 不推良性）
rc, out, err = cli_ev({"PM2/BA1": "Supporting"})
ok("复合码对向 skip（PM2/BA1 不推良性）", rc == 0, f"rc={rc}")

# 4d. BA1 不带 level → fallback VeryStrong → Benign（D15/D16：堵"成立的 BA1"断言盲区）
rc, out, err = cli_ev({"BA1": ""})
ok("BA1 不带 level → Benign", rc == 0 and "Benign" in out, f"rc={rc} out={out[:80]}")

# 4e. BA1 Standalone（原始等级名，白名单已收录）→ Benign（不再静默 skip 成 VUS）
rc, out, err = cli_ev({"BA1": "Standalone"})
ok("BA1 Standalone → Benign（白名单收录，不再 skip 成 VUS）", rc == 0 and "Benign" in out, f"rc={rc} out={out[:80]}")

# 4f. BA1 Stand-alone（连字符写法）→ Benign
rc, out, err = cli_ev({"BA1": "Stand-alone"})
ok("BA1 Stand-alone → Benign", rc == 0 and "Benign" in out, f"rc={rc} out={out[:80]}")

# 4g. BA1 降档等级（D26/F2 钉住）：BA1 只看 code、成立即判良性；降档等级不 skip、按该等级计良性侧
rc, out, err = cli_ev({"BA1": "Supporting"})
ok("BA1=Supporting → 引擎A Benign、引擎B Likely Benign（不 skip 不升格）",
   rc == 0 and "Benign" in out and "Likely Benign" in out, f"rc={rc} out={out[:100]}")

# 4h. BA1 带括号写法（D27/v5.5.2）：ClinGen VCEP 官方原文 "1 Stand Alone (BA1)" 剥括号对 → Benign；
# 括号前缀变体 "(BA1) Stand Alone" 同样归一；知识库原文不改、只改引擎 standalone 识别
rc, out, err = cli_ev({"BA1": "Stand Alone (BA1)"})
ok("BA1 'Stand Alone (BA1)' → Benign（D27 剥括号对）", rc == 0 and "Benign" in out, f"rc={rc} out={out[:80]}")
rc, out, err = cli_ev({"BA1": "(BA1) Stand Alone"})
ok("BA1 '(BA1) Stand Alone' → Benign（D27 剥括号对，前缀变体）", rc == 0 and "Benign" in out, f"rc={rc} out={out[:80]}")

# 5a. 负向断言（D19/D21）：非 BA1 码写 standalone → 整条 skip，不升格（PM1+PM2_M+PP3_S 不得成 Pathogenic）
rc, out, err = cli_ev({"PM1": "Standalone", "PM2": "Moderate", "PP3": "Supporting"})
ok("非BA1+Standalone 不升格（PM1 用例仍 VUS）", rc == 0 and "VUS" in out and "Pathogenic" not in out, f"rc={rc} out={out[:80]}")

# 5b. 负向断言：PP3+SA 单码 → PP3 skip，不参与计分（结果 VUS 非致病）
rc, out, err = cli_ev({"PP3": "SA"})
ok("PP3+SA 单码不参与计分（VUS）", rc == 0 and "VUS" in out and "Pathogenic" not in out, f"rc={rc} out={out[:80]}")

# 5c. 负向断言（D28 修复，有牙齿）：BS1+SA 不得升格。BS1 因 standalone 被 skip，
# 结论必须与"只喂背景"（去掉 BS1）一致；若 BS1 被错误升格 VeryStrong → 会推成 Benign。
# 牙齿检验：v10 把 BS1:SA 升 VeryStrong → Benign（断言 FAIL）；v11 起 skip → VUS（断言 PASS）。
rc_a, out_a, _ = cli_ev({"BS1": "SA"})
rc_b, out_b, _ = cli_ev({})
ok("BS1+SA 不升格：BS1 被 skip，结论与空背景一致（VUS，不含 Benign/Pathogenic）",
   rc_a == 0 and "VUS" in out_a and "Benign" not in out_a and "Pathogenic" not in out_a
   and "VUS" in out_b and "Benign" not in out_b, f"rc_a={rc_a} out_a={out_a[:60]}")

# 5d. 负向断言（D29 修复）：list 形态的 stand-alone 维度（D19 门控在 list 分支同样生效）
rc, out, err = cli_ev([{"code": "PM1", "level": "Standalone"}])
ok("list：非 BA1+Standalone 不升格（PM1 skip，仍 VUS）",
   rc == 0 and "VUS" in out and "Pathogenic" not in out, f"rc={rc} out={out[:80]}")

# 5e. D24 负向断言（dict 形态，F1 cap）：PM2=Strong → 封顶到 Supporting 计入（cap），绝不按传入等级判 Pathogenic
rc, out, err = cli_ev({"PM2": "Strong", "PP3": "Supporting", "PS3": "Strong"})
ok("dict：PM2=Strong → 封顶 Supporting（不判 Pathogenic，结果为 LP）",
   rc == 0 and "Likely Pathogenic" in out and "Pathogenic" not in out.replace("Likely Pathogenic", ""), f"rc={rc} out={out[:100]}")
# F4（去子串）：items 层断言 PM2 已封顶 Supporting、note 含 cap、capped 标记置位（F6）
import acmg_combine as _ac
_its, _of = _ac.parse_evidence_items({"PM2": "Strong", "PP3": "Supporting", "PS3": "Strong"})
_pm2 = [i for i in _its if i["code"] == "PM2"]
ok("dict：PM2 items 层已 cap（level=Supporting, skip=False, note 含 cap, capped=True）",
   bool(_pm2) and _pm2[0]["level"] == "Supporting" and not _pm2[0]["skip"] and "cap" in (_pm2[0].get("note") or "") and _pm2[0].get("capped"),
   f"pm2={[(i['level'],i['skip'],i.get('note'),i.get('capped')) for i in _pm2]}")
# F6（v5.5.1）：cap 留痕透传到 CLI 输出，可审计可见
rc, out, err = cli_ev({"PM2": "Strong", "PP3": "Supporting", "PS3": "Strong"})
ok("dict：CLI 输出含被封顶标记（F6 可审计）", rc == 0 and "封顶" in out, f"rc={rc} out={out[:100]}")

# 5f. D24 负向断言（list 形态）：PM2 非 Supporting 同样封顶 Supporting（cap）
rc, out, err = cli_ev([{"code": "PM2", "level": "Strong"}, {"code": "PP3", "level": "Supporting"}])
ok("list：PM2=Strong → 封顶 Supporting（list 分支同 dict 生效）",
   rc == 0 and "Pathogenic" not in out, f"rc={rc} out={out[:100]}")

print(f"\n契约测试: {passed} 通过 / {fails} 失败")
sys.exit(1 if fails else 0)

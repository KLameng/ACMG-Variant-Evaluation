# -*- coding: utf-8 -*-
"""
acmg_cache.py — ACMG 评级技能群跨变异查询缓存（慢优化核心，v1.2.0）

慢的根因之一：同一基因的疾病信息 / VCEP 规则 / 变异基础注释，评 10 个变异就重复查 10 遍外部 API。
本模块提供跨变异共享的落盘查询缓存：首查外部 API 后回写，后续命中直接读本地，跳过网络。

- 命名空间隔离：gene_disease（基因疾病）/ vcep（VCEP 规则）/ genebe（变异基础注释）/ freq（频率）/ revel（预测分值）/ result（已确认评级结果，永久归档）
- TTL 分级：静态数据（基因疾病/VCEP 规则）30 天；变异级检索 24h；**result 永久归档（TTL=0，无过期）**
- 原子写（临时文件 + rename），多变异并行写安全
- 命中在输出标注（缓存命中 + 存储时间），未命中才发外部请求并回写

⚠ 永久归档边界（v1.1.0）：只有「已确认的评级结果」（result 命名空间）永久存储——它是评级结论快照，
含 rated_at / skills_version / data_snapshot，命中时显式输出结论所基于的数据时点，不静默当作最新。
原始查询命名空间（gene_disease/vcep/genebe/freq/revel）一律按 TTL 过期，防止用过期的外部数据定级
（外部库升版会改变 gnomAD AF / ClinVar 分类 / VCEP 官方裁定 / REVEL/SpliceAI 分值）。

⚠ 时效守卫（v1.2.0，check 动作）：命中 result 归档后，复用前须跑 `check` 把三道闸脚本化——
  闸1 rated_at 距今 > fresh_days（默认 90 天）→ 需重评；
  闸2 data_snapshot 缺失 / 任一数据源取数时点距今 > fresh_days / 传入当前数据版本且归档版本更低 → 需重评；
  闸3 skills_version 落后当前技能群版本（自动读收尾 SKILL frontmatter，可用 --current-version 覆盖）→ 需重评。
  任一触发 → 强制走完整重评；全过才可复用。把"依赖 LLM 读字段判断"固化为确定性脚本。
"""
import argparse
import hashlib
import json
import os
import sys
import time

# 缓存根：技能群根目录 / _cache（跨变异共享；随包 _cache 为空，运行时生成）
CACHE_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_cache")

# TTL 分级（小时）
TTL_STATIC = 30 * 24      # 基因疾病信息、VCEP 规则：30 天
TTL_VARIANT = 24          # 变异级检索（GeneBe/ClinVar 单变异）：24h

# 时效守卫默认新鲜度阈值（天）
FRESH_DAYS_DEFAULT = 90

NAMESPACES = {"gene_disease", "vcep", "genebe", "freq", "revel", "result"}

# result 命名空间 = 永久归档（无过期）；其余按 TTL 分级
PERMANENT_NS = {"result"}


def _path(namespace, key):
    h = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE_ROOT, namespace, h + ".json")


def cache_key(*parts):
    return "|".join(str(x) for x in parts)


def cache_get(namespace, key):
    """命中且未过期 → value；未命中/过期/损坏 → None。永久条目（expire=None）不过期。"""
    p = _path(namespace, key)
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
        if d.get("expire") is not None and time.time() > d["expire"]:
            return None
        return d["value"]
    except Exception:  # 损坏缓存按未命中处理，不阻断
        return None


def cache_set(namespace, key, value, ttl_hours):
    """写入。ttl_hours=0 → 永久归档（expire=None，result 命名空间默认永久）。"""
    os.makedirs(os.path.dirname(_path(namespace, key)), exist_ok=True)
    p = _path(namespace, key)
    expire = None if ttl_hours == 0 else time.time() + ttl_hours * 3600
    d = {"value": value, "expire": expire, "stored": time.time()}
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False)
    os.replace(tmp, p)  # 原子写，防并发冲突
    return p


def _fmt(ts):
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(ts))


# ---------- 时效守卫（v1.2.0）----------

def _parse_ts(v):
    """宽容解析时间：秒(float/int)/ISO/日期字符串 → 秒；失败返回 None。"""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("T", " ").replace("Z", "").split(".")[0]
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return time.mktime(time.strptime(s, fmt))
        except ValueError:
            pass
    return None


def _version_tuple(v):
    if not v:
        return None
    out = []
    for p in str(v).strip().lstrip("v").split("."):
        try:
            out.append(int(p))
        except ValueError:
            out.append(0)
    return tuple(out)


def _ver_ge(a, b):
    """版本 a >= b？无法比较返回 None（不判升版）。"""
    ta, tb = _version_tuple(a), _version_tuple(b)
    if ta is None or tb is None:
        return None
    return ta >= tb


def _collect_snapshot_times(data_snapshot):
    """从 data_snapshot（dict/str/数值）收集所有"取数时点"，供 90 天新鲜度判断。"""
    times = []
    if isinstance(data_snapshot, dict):
        for _k, v in data_snapshot.items():
            if isinstance(v, dict):
                hit = False
                for f in ("at", "stored", "time", "date"):
                    if f in v:
                        t = _parse_ts(v[f])
                        if t:
                            times.append(t)
                            hit = True
                            break
                if not hit and "version" in v:
                    # 仅版本号无可比时点，不当作"取数很久"
                    pass
            else:
                t = _parse_ts(v)
                if t:
                    times.append(t)
    elif isinstance(data_snapshot, (str, int, float)):
        t = _parse_ts(data_snapshot)
        if t:
            times.append(t)
    return times


def check_rated_result(value, current_version=None, fresh_days=FRESH_DAYS_DEFAULT, current_data_version=None):
    """时效守卫三道闸（确定性脚本）。返回 {status, reason, fields}。

    闸1 rated_at 距今 > fresh_days → 需重评
    闸2 data_snapshot 缺失 / 任一数据源取数时点距今 > fresh_days / 归档数据版本 < 当前 → 需重评
    闸3 skills_version 落后当前技能群版本 → 需重评
    """
    if not isinstance(value, dict):
        return {"status": "RERATE", "reason": "归档条目非 dict，无法校验时效，视为需重评", "fields": {}}
    now = time.time()
    reasons = []
    rated_at = _parse_ts(value.get("rated_at"))
    skills_version = value.get("skills_version")
    data_snapshot = value.get("data_snapshot")

    if rated_at is None:
        reasons.append("闸1 rated_at 缺失，无法确认时效")
    elif now - rated_at > fresh_days * 86400:
        reasons.append(f"闸1 rated_at 距今 {int((now - rated_at) / 86400)} 天 > {fresh_days} 天")

    if data_snapshot is None:
        reasons.append("闸2 data_snapshot 缺失（归档缺数据快照，命中不得复用）")
    else:
        for t in _collect_snapshot_times(data_snapshot):
            if now - t > fresh_days * 86400:
                reasons.append(f"闸2 有数据源取数距今 > {fresh_days} 天（旧快照，需取最新数据重评）")
                break
        if current_data_version and isinstance(data_snapshot, dict):
            for k, v in data_snapshot.items():
                if isinstance(v, dict) and "version" in v:
                    cur = current_data_version.get(k)
                    if cur and _ver_ge(v["version"], cur) is False:
                        reasons.append(f"闸2 数据源 {k} 已升版（归档 {v['version']} < 当前 {cur}）")

    if current_version and skills_version:
        if _ver_ge(skills_version, current_version) is False:
            reasons.append(f"闸3 skills_version {skills_version} < 当前 {current_version}（规则已升级，需重评）")

    status = "REUSE" if not reasons else "RERATE"
    return {
        "status": status,
        "reason": "；".join(reasons) if reasons else f"时效守卫三道闸全部通过（fresh_days={fresh_days}）",
        "fields": {"rated_at": rated_at, "skills_version": skills_version, "data_snapshot": data_snapshot},
    }


def _current_skill_version():
    """从收尾 SKILL frontmatter 读取当前技能群版本；失败返回 None。"""
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "acmg-conflict-summary-output", "SKILL.md")
    try:
        for line in open(p, encoding="utf-8"):
            if line.startswith("version:"):
                return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return None


def main():
    ap = argparse.ArgumentParser(description="ACMG 跨变异查询缓存")
    ap.add_argument("action", choices=["get", "set", "hit", "miss", "clear", "check"])
    ap.add_argument("--ns", choices=sorted(NAMESPACES), required=True, help="命名空间")
    ap.add_argument("--key", help="缓存键（'|' 分隔的多段原始值，内部按段 hash）")
    ap.add_argument("--ttl", type=int, default=None, help="TTL 小时（默认按命名空间：gene_disease/vcep=720，其余=24）")
    ap.add_argument("--value", help="set 时写入的 JSON 值")
    ap.add_argument("--fresh-days", type=int, default=None, help="时效守卫新鲜度阈值（天，默认 90）")
    ap.add_argument("--current-version", help="时效守卫当前技能群版本（默认自动读收尾 SKILL frontmatter）")
    ap.add_argument("--current-data-version", help="时效守卫当前数据源版本 JSON（如 '{\"gnomAD\":\"v4.0\"}'），可选")
    args = ap.parse_args()

    if args.action == "get":
        if not args.key:
            ap.error("get 需 --key")
        v = cache_get(args.ns, args.key)
        if v is None:
            print("MISS")
            sys.exit(0)
        # 附命中时间（读文件 metadata）
        p = _path(args.ns, args.key)
        stored = None
        permanent = False
        try:
            md = json.load(open(p, encoding="utf-8"))
            stored = md.get("stored")
            permanent = md.get("expire") is None
        except Exception:
            pass
        print("HIT")
        if permanent:
            print("PERMANENT")
        if stored:
            print(f"stored_at={_fmt(stored)}")
        print(json.dumps(v, ensure_ascii=False))
        sys.exit(0)
    if args.action == "set":
        if not args.key or not args.value:
            ap.error("set 需 --key 与 --value")
        ttl = args.ttl if args.ttl is not None else (0 if args.ns == "result" else (TTL_STATIC if args.ns in ("gene_disease", "vcep") else TTL_VARIANT))
        val = json.loads(args.value)
        p = cache_set(args.ns, key=args.key, value=val, ttl_hours=ttl)
        print(f"SET {p}" + (" (PERMANENT)" if ttl == 0 else ""))
        sys.exit(0)
    if args.action == "hit":
        # 报告命名空间命中率（供优化评估）：扫描缓存文件数
        ns_dir = os.path.join(CACHE_ROOT, args.ns)
        n = sum(1 for f in os.listdir(ns_dir)) if os.path.isdir(ns_dir) else 0
        print(f"namespace={args.ns} cached_entries={n}")
        sys.exit(0)
    if args.action == "miss":
        sys.exit(0)
    if args.action == "clear":
        ns_dir = os.path.join(CACHE_ROOT, args.ns)
        if os.path.isdir(ns_dir):
            for f in os.listdir(ns_dir):
                os.remove(os.path.join(ns_dir, f))
            print(f"CLEAR {args.ns}")
        sys.exit(0)
    if args.action == "check":
        # 时效守卫（v1.2.0）：命中 result 归档后，复用前脚本化跑三道闸
        if not args.key:
            ap.error("check 需 --key")
        v = cache_get(args.ns, args.key)
        if v is None:
            print("STATUS: NOT_FOUND")
            sys.exit(0)
        cur = args.current_version or _current_skill_version()
        cdata = None
        if args.current_data_version:
            try:
                cdata = json.loads(args.current_data_version)
            except Exception:
                ap.error("--current-data-version 必须是合法 JSON")
        res = check_rated_result(v, current_version=cur, fresh_days=args.fresh_days or FRESH_DAYS_DEFAULT, current_data_version=cdata)
        print(f"STATUS: {res['status']}")
        print(f"REASON: {res['reason']}")
        print(f"current_skills_version: {cur}")
        print(f"archived_skills_version: {res['fields'].get('skills_version')}")
        print(f"rated_at: {res['fields'].get('rated_at')}")
        sys.exit(0)


if __name__ == "__main__":
    main()

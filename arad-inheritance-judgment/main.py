#!/usr/bin/env python3
"""
AR/AD遗传模式判断 - 查询ClinVar和PubMed获取患者基因型（zygosity）信息
用法:
  python main.py clinvar <gene> "<variant>"
  python main.py pubmed <gene> "<variant>"
  python main.py same_type <gene> "<variant_type>"
"""

import sys
import os
import json
import re
import xml.etree.ElementTree as ET
try:
    import requests  # 第三方库（非 Python 标准库），使用前需安装：python -m pip install requests
except ImportError:
    print("错误：缺少第三方依赖 requests。请先安装：python -m pip install requests，再重新运行本脚本。",
          file=sys.stderr)
    sys.exit(2)

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL_PARAM = {"tool": "arad-inheritance-judgment-jb", "email": os.environ.get("NCBI_EMAIL", "variant-rating-skill@example.com")}


def esearch(db, term, retmax=50):
    """NCBI E-utilities esearch, return list of IDs"""
    params = {"db": db, "term": term, "retmax": retmax, "retmode": "json"}
    params.update(TOOL_PARAM)
    try:
        resp = requests.get(f"{BASE_URL}/esearch.fcgi", params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        result = data.get("esearchresult", {})
        ids = result.get("idlist", [])
        count = result.get("count", "0")
        return ids, int(count)
    except Exception as e:
        print(json.dumps({"error": f"esearch failed: {str(e)}"}, ensure_ascii=False))
        return [], 0


def efetch_xml(db, ids):
    """NCBI E-utilities efetch in XML mode, return ElementTree root"""
    params = {"db": db, "id": ",".join(ids), "retmode": "xml"}
    params.update(TOOL_PARAM)
    resp = requests.get(f"{BASE_URL}/efetch.fcgi", params=params, timeout=60)
    resp.raise_for_status()
    return ET.fromstring(resp.text)


def extract_zygosity_from_text(text):
    """Extract zygosity keywords from free text, return deduplicated list"""
    if not text:
        return []
    text_lower = text.lower()
    found = []
    # Check compound heterozygous before heterozygous
    if "compound heterozygous" in text_lower or "compound heterozygote" in text_lower:
        found.append("compound_heterozygous")
    if "homozygous" in text_lower or "homozygote" in text_lower:
        found.append("homozygous")
    # Only add heterozygous if not already captured as compound
    if ("heterozygous" in text_lower or "heterozygote" in text_lower) and "compound heterozygous" not in text_lower:
        found.append("heterozygous")
    elif "heterozygous" in text_lower and "compound heterozygous" in text_lower:
        # Both present - add heterozygous too
        if "heterozygous" not in found:
            found.append("heterozygous")
    if "hemizygous" in text_lower or "hemizygote" in text_lower:
        found.append("hemizygous")
    return list(dict.fromkeys(found))  # deduplicate preserving order


def search_clinvar(gene, variant):
    """Query ClinVar for variant, extract patient zygosity info"""
    evidence = []

    # Build search query
    search_term = f'{gene}[gene] AND "{variant}"'
    ids, count = esearch("clinvar", search_term, retmax=30)

    if not ids:
        # Try broader search without quotes
        search_term = f"{gene}[gene] AND {variant}"
        ids, count = esearch("clinvar", search_term, retmax=30)

    if not ids:
        return {
            "source": "ClinVar",
            "found": False,
            "total_hits": count,
            "evidence": [],
            "search_url": f"https://www.ncbi.nlm.nih.gov/clinvar/?term={gene}+{variant}"
        }

    try:
        root = efetch_xml("clinvar", ids)
    except Exception as e:
        return {"source": "ClinVar", "found": False, "error": f"efetch failed: {str(e)}", "evidence": []}

    seen_zygosities = set()

    for clinvar_set in root.findall(".//ClinVarSet"):
        record_id = clinvar_set.findtext("ID", "")

        # Extract variant name
        variant_name = ""
        for measure in clinvar_set.findall(".//Measure"):
            for name_elem in measure.findall(".//Name"):
                if name_elem.get("Type") == "Preferred":
                    ev = name_elem.find("ElementValue")
                    if ev is not None and ev.text:
                        variant_name = ev.text
                        break

        # Extract disease/trait
        traits = []
        for trait in clinvar_set.findall(".//Trait"):
            for name_elem in trait.findall(".//Name"):
                ev = name_elem.find("ElementValue")
                if ev is not None and ev.text:
                    traits.append(ev.text)

        # Extract zygosity - search in multiple locations
        zygosities = []

        # Method 1: Look for explicit Zygosity elements
        for zyg in clinvar_set.findall(".//Zygosity"):
            ev = zyg.find("ElementValue")
            if ev is not None and ev.text:
                zygosities.extend(extract_zygosity_from_text(ev.text))

        # Method 2: Look in ObservedIn > Sample for genotype descriptions
        for observed_in in clinvar_set.findall(".//ObservedIn"):
            sample = observed_in.find("Sample")
            if sample is not None:
                for feature in sample.findall(".//Feature"):
                    name_elem = feature.find("Name")
                    if name_elem is not None and name_elem.text:
                        zygosities.extend(extract_zygosity_from_text(name_elem.text))
                    for desc in feature.findall(".//Attribute"):
                        if desc.text:
                            zygosities.extend(extract_zygosity_from_text(desc.text))

        # Method 3: Look in GenotypeSet
        for genotype in clinvar_set.findall(".//GenotypeSet//Genotype"):
            for ev in genotype.findall(".//ElementValue"):
                if ev.text and ev.get("Type") in ("Zygosity", "ConstitutionalZygosity"):
                    zygosities.extend(extract_zygosity_from_text(ev.text))

        # Method 4: Look in ObservedData descriptions
        for obs_data in clinvar_set.findall(".//ObservedData"):
            for desc in obs_data.findall(".//Description"):
                if desc.text:
                    zygosities.extend(extract_zygosity_from_text(desc.text))

        # Deduplicate
        zygosities = list(dict.fromkeys(zygosities))

        if zygosities:
            ev_key = tuple(sorted(zygosities))
            if ev_key not in seen_zygosities:
                seen_zygosities.add(ev_key)
                evidence.append({
                    "clinvar_id": record_id,
                    "variant": variant_name,
                    "zygosity": zygosities,
                    "traits": list(dict.fromkeys(traits))[:5],
                    "clinvar_url": f"https://www.ncbi.nlm.nih.gov/clinvar/{record_id}/"
                })

    return {
        "source": "ClinVar",
        "found": len(evidence) > 0,
        "total_hits": count,
        "evidence": evidence,
        "search_url": f"https://www.ncbi.nlm.nih.gov/clinvar/?term={gene}+{variant}"
    }


def search_pubmed(gene, variant):
    """Query PubMed for variant in literature, extract zygosity from abstracts"""
    evidence = []

    # Build search query - use variant notation for precision
    search_term = f"{gene}[Title/Abstract] AND {variant}"
    ids, count = esearch("pubmed", search_term, retmax=30)

    if not ids:
        # Broader search
        search_term = f"{gene} AND {variant}"
        ids, count = esearch("pubmed", search_term, retmax=30)

    if not ids:
        return {
            "source": "PubMed",
            "found": False,
            "total_hits": count,
            "evidence": [],
            "search_url": f"https://pubmed.ncbi.nlm.nih.gov/?term={gene}+{variant}"
        }

    try:
        root = efetch_xml("pubmed", ids)
    except Exception as e:
        return {"source": "PubMed", "found": False, "error": f"efetch failed: {str(e)}", "evidence": []}

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID", "")
        title = article.findtext(".//ArticleTitle", "")

        # Get full abstract text
        abstract_parts = []
        for abs_text in article.findall(".//AbstractText"):
            parts = []
            if abs_text.text:
                parts.append(abs_text.text)
            # Handle mixed content (text + sub-elements)
            for child in abs_text:
                if child.text:
                    parts.append(child.text)
                if child.tail:
                    parts.append(child.tail)
            if parts:
                abstract_parts.append("".join(parts))
        abstract = " ".join(abstract_parts)

        if not abstract:
            continue

        # Extract zygosity from abstract
        zygosities = extract_zygosity_from_text(abstract)

        if zygosities:
            evidence.append({
                "pmid": pmid,
                "title": title[:200],
                "zygosity": zygosities,
                "abstract_snippet": abstract[:500],
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            })

    return {
        "source": "PubMed",
        "found": len(evidence) > 0,
        "total_hits": count,
        "evidence": evidence,
        "search_url": f"https://pubmed.ncbi.nlm.nih.gov/?term={gene}+{variant}"
    }


def search_same_gene_same_type(gene, variant_type):
    """Search PubMed for other variants of same gene and same variant type"""
    evidence = []

    # Map common variant types to search terms
    type_map = {
        "missense": "missense",
        "nonsense": "nonsense",
        "frameshift": "frameshift",
        "splice_site": "splice",
        "splice": "splice",
        "inframe_deletion": "inframe deletion",
        "inframe_insertion": "inframe insertion",
        "indel": "indel",
        "deletion": "deletion",
        "insertion": "insertion",
        "truncating": "truncating",
        "loss_of_function": "loss of function",
        "lof": "loss of function"
    }
    search_type = type_map.get(variant_type.lower().replace(" ", "_"), variant_type)

    search_term = f"{gene}[Title/Abstract] AND {search_type}[Title/Abstract]"
    ids, count = esearch("pubmed", search_term, retmax=30)

    if not ids:
        return {
            "source": "PubMed_SameType",
            "found": False,
            "total_hits": count,
            "evidence": [],
            "variant_type_searched": variant_type,
            "search_url": f"https://pubmed.ncbi.nlm.nih.gov/?term={gene}+{search_type}"
        }

    try:
        root = efetch_xml("pubmed", ids)
    except Exception as e:
        return {"source": "PubMed_SameType", "found": False, "error": str(e), "evidence": []}

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID", "")
        title = article.findtext(".//ArticleTitle", "")

        abstract_parts = []
        for abs_text in article.findall(".//AbstractText"):
            parts = []
            if abs_text.text:
                parts.append(abs_text.text)
            for child in abs_text:
                if child.text:
                    parts.append(child.text)
                if child.tail:
                    parts.append(child.tail)
            if parts:
                abstract_parts.append("".join(parts))
        abstract = " ".join(abstract_parts)

        if not abstract:
            continue

        zygosities = extract_zygosity_from_text(abstract)

        if zygosities:
            # Try to extract specific variant descriptions from abstract
            variant_mentions = re.findall(
                r'(?:c\.\d+[ACGT]>[ACGT]|c\.\d+_[A-Za-z]+\d+del|p\.[A-Z][a-z]{2}\d+[A-Z][a-z]{0,3}|[A-Z][a-z]{2}\d+[A-Z][a-z]{0,3}[^a-z])',
                abstract
            )

            evidence.append({
                "pmid": pmid,
                "title": title[:200],
                "zygosity": zygosities,
                "variant_mentions": list(dict.fromkeys(variant_mentions))[:5] if variant_mentions else [],
                "abstract_snippet": abstract[:500],
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            })

    return {
        "source": "PubMed_SameType",
        "found": len(evidence) > 0,
        "total_hits": count,
        "evidence": evidence,
        "variant_type_searched": variant_type,
        "search_url": f"https://pubmed.ncbi.nlm.nih.gov/?term={gene}+{search_type}"
    }


def main():
    if len(sys.argv) < 4:
        print(json.dumps({
            "error": "Usage: python main.py <mode> <gene> <variant_or_type>",
            "modes": "clinvar, pubmed, same_type"
        }, ensure_ascii=False))
        sys.exit(1)

    mode = sys.argv[1].lower()
    gene = sys.argv[2]
    variant = sys.argv[3]

    if mode == "clinvar":
        result = search_clinvar(gene, variant)
    elif mode == "pubmed":
        result = search_pubmed(gene, variant)
    elif mode == "same_type":
        result = search_same_gene_same_type(gene, variant)
    else:
        result = {"error": f"Unknown mode: {mode}. Use: clinvar, pubmed, same_type"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

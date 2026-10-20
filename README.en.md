# ACMG-Variant-Evaluation · Monogenic Point-Mutation ACMG Classification Skill Suite

A reusable skill suite for **ACMG/AMP pathogenicity classification of sequence variants in Mendelian disease genes**. Built on the ACMG/AMP 2015 framework, covering the full evidence-code workflow for point-mutation classification.

## Overview

- **23 skills**, including `acmg-total-scheduler` (master scheduler / single entry) and `ev-*` evidence-code sub-skills (PVS1/PS1-PS4/PM1-PM6/PP1-PP4/BS1-BS4/BP1-BP7 etc.).
- Variant-identity normalization → inheritance-mode pre-check → per-evidence-code classification → conflict-summary layer for evidence-direction consistency and score-chain validation.
- Judging criteria are externalized: rules are centrally managed; changing criteria does not touch the workflow, adding cases does not touch the code.
- The mutual-exclusion matrix lives only in the concluding skill `acmg-conflict-summary-output`; `ev-*` sub-skills carry no evidence-exclusion content.

## Software Architecture

```
acmg-total-scheduler/          # Master scheduler (single entry)
  ├── SKILL.md                 # Mandatory flow: normalize → inheritance pre-check → per-code → conclude
  └── references/              # criteria & rule data
ev-*/                          # Evidence-code sub-skills (PVS1 / PS1-PS4 / PM1-PM6 / PP1-PP4 / BS* / BP*)
acmg-conflict-summary-output/  # Concluding skill: mutual-exclusion matrix + evidence-direction consistency
config/                        # golden / thresholds
scripts/                       # helper scripts
```

## Quick Start

1. Enter via `acmg-total-scheduler/SKILL.md` (single entry).
2. Follow the mandatory flow: normalize → inheritance pre-check → per-evidence-code → concluding score-chain validation.
3. For single-variant classification, start from the `acmg-total-scheduler` suite.

## Contribution

Welcome de-identified variant cases and review feedback to help ratify evidence-code criteria. See `CONTRIBUTING.md` in each skill directory.

## License

- License: **Apache License 2.0**, copyright **KLameng**. See `LICENSE`.
- Maintainer: **KLameng** · Contact: **911712412@qq.com**

---

*Copyright (c) 2026 KLameng <911712412@qq.com> · Released under Apache-2.0.*

> **来源**：ClinGen SVI Criteria Specification Repository
> 数据日期：2026-06-13
> 原文提取方式：逐字保留

*   Use only for Single Nucleotide Polymorphism inside the gene (do not use for promoter sequence)
    *   Parameters utilized:
        *   Input sequence: FASTA (Ensembl NR\_\_003051.3)
        *   Insert SNP details
        *   Mode: 1
        *   Folding window: 100 nt
        *   Measure: “Distance” option
        *   Minimum length of the sequence interval: 50 
        *   Cut-off the base pair probabilities: 0.01

The p-value threshold significance should be considered 0.1 according to Sabarinathan et al., 2013. PMID: 23315997. If the value is less than 0.1, apply PP3 as a supporting level of evidence.


#### PP4
- 默认强度：Pathogenic Supporting
- ACMG原始定义：Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.
- **Moderate** ✅：A patient score of ≥2 points (see instructions below).
- **Supporting** ✅：A patient score of 1-\<2 points (see instructions below).

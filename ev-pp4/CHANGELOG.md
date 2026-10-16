# ev-pp4 CHANGELOG

2026-10-15 description 瘦身整改：version 变更日志从 SKILL.md frontmatter 下沉至此；同日修复版本序列非单调（原 1.3.0 在 1.1.0/1.2.1 之前，现已按版本号单调升序重排）。

## v1.1.0

- 新增遗传方式前置判定硬步骤——判定前必须先调用 `arad-inheritance-judgment` 确认该变异遗传方式，作为"家族史与疾病遗传方式一致"及表型特异性的判定前提，禁止默认遗传方式；遗传方式以 ClinVar 患者基因型+PubMed报道+GenCC MOI 三方交叉为准。

## v1.2.1

- 表型四要素闸就位——①临床表现询问（无表型→PP4 不成立）；②特异性反证检查（多基因异质→不用，判例 HPS3/CNGA3/ETFDH/GRHPR/PKHD1/ERCC4/SLC25A13/G6PD）；③强制搜文献（OMIM/ClinGen/文献 + 按用途提取 + 可疑上报）；④不以 PP4 弱码顶替可取得的 PM3/PP3/PS3（以弱代强违规，HEXB/SLC22A5-51 教训）。

## v1.3.0

- 新增跨技能调用声明——判定表型特异性/外显率/发病率须调用 `ev-disease-info`（NCBI Books GeneReviews 通道，books/medgen/clingen 子命令）获取结构化疾病信息，输出写明子命令与标准疾病名。

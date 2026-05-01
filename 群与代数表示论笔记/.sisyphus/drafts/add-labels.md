# Draft: Add Labels to 群表示.tex

## Requirements (confirmed)
- 为所有定理类环境添加引用标签（除 instance 外）
- 范围：definition, theorem, lemma, corollary, property
- 标签风格：优先使用中文语义名，无法表达时用编号
- Lemma/Corollary 编号规则：章号.序号（如 lem:1.1, cor:1.1）
- 标签语法：`\begin{<env>}[<title>][<label>]`（rainbow.sty 规范）

## Scope Boundaries
- INCLUDE: 群表示.tex 中所有 definition/theorem/lemma/corollary/property
- EXCLUDE: instance, proof 环境，其他 .tex 文件

## Technical Decisions
- 语法：第二个可选参数即标签，无标题时第一参数留空 `[]`
- 章节号：群表示.tex 是第一章（见主文档 line 169）
- 标签前缀：def:, thm:, lem:, cor:, prop:

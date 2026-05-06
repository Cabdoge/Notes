# 对称群的表示与特征标理论 — 项目指南

## 项目概况
- **用途**：群与代数表示论 期中大作业（上海交大）
- **文档类**：`sjtureport`
- **编译**：`xelatex`（三遍，imakeidx 自动调用 makeindex）
- **输出**：`群与代数表示论期中大作业.pdf`（37 页）

## 文件清单
| 文件 | 说明 |
|------|------|
| `群与代数表示论期中大作业.tex` | 主文件（符号说明、Ch2–4、索引、参考文献） |
| `Young表.tex` | 第一章 Young表（`\input` 引入） |
| `pinyin.ist` | makeindex 索引样式（拼音首字母段标题） |

## 编译流程
```bash
cd "/Users/1tianpang/Desktop/笔记/群与代数表示论期中大作业"
xelatex "群与代数表示论期中大作业.tex"     # 第1遍：生成 .idx
xelatex "群与代数表示论期中大作业.tex"     # 第2遍：imakeidx 自动调 makeindex 生成 .ind，嵌入索引
xelatex "群与代数表示论期中大作业.tex"     # 第3遍：固定交叉引用页码
```
> 每次新增 `\index` 条目或修改标签后，需完整三轮编译。

## 包依赖
`amsmath, amsthm, bm, physics, ytableau, imakeidx, longtable, hyperref, geometry, setspace`

- `imakeidx` + `makeindex`：索引生成（`pinyin.ist` 样式）
- `hyperref`（`hidelinks`）：索引页码超链接
- `longtable`：符号说明表跨页

## 章节结构

### 符号说明（`\chapter*`）
- 44 项符号，按「组合基础 / 群与代数 / 表示与模 / 对称多项式 / 边界带」五类分栏
- 使用 `longtable` 可跨页（`p{3.2cm}` + 剩余宽度），次页自动显示"（续）"表头
- 新增条目时在对应分类下加 `\\` 行即可

### 第一章 Young表（`\input{Young表.tex}`，189 行）
- **§1.1 分拆**：`λ ⊢ n` 定义、`ρ(n)`、定理 1.1（S_n 共轭类与分拆一一对应）
- **§1.2 Young表**：Young图/Young表定义、标准Young表、钩长公式首次预告（`f^λ`）
- **§1.3 Young子群**：行群 `R_t`、列群 `C_t` 定义
- **§1.4 Young对称化子**：`a_t`, `b_t`, `c_t = a_t b_t`、von Neumann 引理、`c_t` 本质幂等元定理

### 第二章 对称群的不可约表示（主文件，行 ~140–570）
- **§2.1 置换模**：行等价报 `{t}`、置换模 `M^λ` ≅ `Ind_{R_t}^{S_n}(1)`、维数 `n!/λ!`
- **§2.2 内积与伴随**：`M^λ` 上的 `S_n`-不变内积、`b_t` 自伴引理
- **§2.3 Specht模**：多项表 `e_t = b_t{t}`、`S^λ = span{e_t}`、等价定理 `S^λ ≅ ℂ[S_n]c_t`
- **§2.4 极值性与子模定理**：⭐ 多项表极值性（二同行元素→`b_t{t'}=0`）、推论 `b_t{t}=±e_t`、⭐ 子模定理（正交补二分法）
- **§2.5 不可约性**：⭐ `S^λ` 不可约（子模定理直接推论）
- **§2.6 分类**：支配序 `λ ⊵ μ`、同态蕴含支配（`λ≠μ → Hom(S^λ,M^μ)=0`）→ ⭐ 不同分拆不同表示
- **§2.7 基与维数**：字典序、Garnir 元 `G_{A,B}`、多项表分解定理（非标准→标准线性表出）、⭐ 维数定理 `dim S^λ = f^λ`

### 第三章 对称群的特征标（主文件，行 ~575–1135）
- **§3.1 Frobenius公式**：幂和对称多项式 `p_k`, `p_μ`、中心化子阶 `z_μ`、交错和 `a_α`/Vandermonde `Δ(x)`、Schur 多项式 `s_λ`（行列式+组合双定义）、⭐ Frobenius 特征标公式 `s_λ = Σ (χ^λ_μ/z_μ)p_μ`、逆关系（推论）、证明骨架（Frobenius 映射 `F` + Hall 内积等距性）、例 3.1：S₃ 完整特征标表（三个分拆的行列式展开 + Newton 恒等式转换）
- **§3.2 边界带表**：边界（rim）定义（`(i+1,j+1)∉λ`）、⭐ 边界带三条件（连通/无 2×2/移除后合法分拆）、高度 `ht(ξ)` 与符号 `ε(ξ)`、例 3.2（`λ=(3,1)` 边界带枚举）、例 3.3（`2×2` 禁令 `λ=(2,2)`）、⭐ 边界带表定义（分拆递减链形式+填数等价描述）、表高度与符号、例 3.4（`λ=(3,1), μ=(2,2)` 边界带表构造）
- **§3.3 Murnaghan-Nakayama 公式**：⭐ 递推形式 `χ^λ_μ = Σ_{|ξ|=μ₁} (-1)^{ht(ξ)} χ^{λ\ξ}_{(μ₂,…)}`、封闭形式 `χ^λ_μ = Σ_T (-1)^{ht(T)}`、分量顺序无关性注记、引理 `p_r·s_ν = Σ_ξ (-1)^{ht(ξ)} s_{ν∪ξ}`（思路简述）、完整证明（反复应用引理→叠加 Frobenius 逆关系→比较 `s_λ` 系数）、例 3.5：S₄ 五个特征标值 MN 手算（覆盖平凡/符号/null/递推）、衔接注记 `μ=(1^n)` 退化至钩长公式
- **§3.4 钩长公式**：钩长 `h_{i,j}` 与钩长积 `H(λ)`、⭐ Frame-Robinson-Thrall 公式 `dim S^λ = n!/∏h_{i,j}`、证明三步走——(i) MN `μ=(1^n)` 导出分支递推 `f^λ = Σ_c f^{λ\c}`，(ii) 钩长恒等式引理 `n/H(λ) = Σ_c 1/H(λ\c)`（Hook-content 有理函数 `Φ_λ(x)` + 留数+部分分式证明），(iii) 归纳完成、钩游走概率注记（GNW 1979）、例：`λ=(3,1)` 验证

### 第四章 总结（行 ~1140–1190）
- 全文三阶段回顾（表示构造→代数翻译→组合计算）
- 定理关系表（D1→T10 依存链，★标记核心定理）
- 四个未涉及方向简注（限制/诱导、Frobenius 同构、Littlewood-Richardson、模表示论）
- 收尾：群论·组合学·对称函数三领域融合

### 参考文献
- Fulton-Harris (GTM 129)：`\cite{FultonHarris}`
- Sagan (GTM 203)：`\cite{Sagan}`

### 关键词索引（`\printindex`）
- `imakeidx` + `makeindex -s pinyin.ist` 自动生成
- 双栏排版、拼音首字母段标题（数字/B/D/F/G/H/L/M/N/S/V/W/Y/Z）
- 55 条目、带 `hyperref` 超链接页码
- `\index` 命令散布全文约 55 处（Young表.tex 11 + 第二章 16 + 第三章 28）

## 索引系统
- **后端**：`makeindex` + `pinyin.ist`
- **样式特性**：拼音首字母段标题（B/D/F/G/H/L/M/N/S/V/W/Y/Z + 数字）
- **条目格式**：`\index{首字母@中文词}`，全文约 55 处
- **分布**：Young表.tex 11 处 + 第二章 16 处 + 3.1~3.4 约 28 处
- **超链接**：`hyperref` 使页码可点击（`hidelinks` 无框）

### 新增 `\index` 条目步骤
1. 在环境 `\begin{xxx}[...]` 后插入 `\index{首字母@中文词}`
2. 首字母按拼音：b/d/f/g/h/j/l/m/n/s/v/w/y/z 或 2/数字
3. 完整三轮编译

## 翻译约定
| 中文 | 英文 |
|------|------|
| 边界带 | border strip / rim hook |
| 高度 | leg length → ht(ξ) |
| 边界带表 | border strip tableau |
| 多项表 | polytabloid |
| 行等价报 | tabloid |
| 可移角格 | removable corner |

## 定理/定义标签体系
- 定理：`thm:MN`, `thm:frobenius`, `thm:hook`, `thm:conjugacy_classes_of_Sn`
- 定义：`def:borderstrip`（边界带）, `def:bst`（边界带表）
- 引理：`lem:ps-Schur`, `lem:hook-identity`, `lem:extremality`
- 推论：`cor:inv`, `cor:MN-closed`
- 例子：`ex:S3`, `ex:bs-31`, `ex:bs-22`, `ex:bst-31-22`, `ex:MN-S4`
- 用 `\ref`, `\eqref` 交叉引用

## 当前状态
| 项目 | 状态 |
|------|------|
| 全文四章 + 总结 | ✅ 完成 |
| 符号说明表（44项） | ✅ longtable 跨页，加宽列 |
| 索引（55项，带段标题+超链接） | ✅ 完成 |
| 段内精确拼音排序 | ⬜ 部分条目用单字母排序键（如 `b@`），改为全拼（如 `ban@`）可细化 |
| zhmakeindex | ⬜ 未安装（需 Go 编译或 TL2026+），当前 makeindex + 拼音键等效 |

## 注意事项
- 文件名含中文 → **必须用 xelatex**（pdflatex 会乱码）
- `Young表.tex` 是 `\input` 引入，标签在主文件中正常引用
- 新建 `\index` 后需三轮编译，修改 `pinyin.ist` 后同样
- `longtable` 跨页时次页自动显示"（续）"表头
- 修改索引样式 → 编辑 `pinyin.ist`（如 `headings_flag`、`heading_prefix` 等）

# Typst 波浪符（Tilde）使用指南

本文档介绍如何在 Typst 中为字母添加波浪符（tilde）。

## 基本用法

### 1. 数学模式中的波浪符

在 Typst 的数学模式中，可以使用以下方法为字母添加波浪符：

#### 方法一：使用 `tilde` 函数
```typst
$tilde(x)$
$tilde(A)$
$tilde(omega)$
```
效果：x̃, Ã, ω̃

#### 方法二：使用 `accent` 函数
```typst
$accent(x, tilde)$
$accent(A, tilde)$
```
效果：x̃, Ã

#### 方法三：使用 Unicode 组合字符
```typst
$x ̃$
```
注意：波浪符直接跟在字母后面（使用 Unicode 组合波浪符 U+0303）

### 2. 文本模式中的波浪符

#### 独立的波浪符号
```typst
~
```
效果：~（独立的波浪号）

#### 组合波浪符
使用 Unicode 组合字符在文本中添加波浪符：
```typst
añ
õ
ñ
```

## 常见数学符号示例

### 向量和变量标记
```typst
$tilde(x)$ 表示变量 x 的另一个版本
$tilde(bold(v))$ 表示向量 v 的变形
$tilde(f)(x)$ 表示函数 f 的近似或变形
```

### 等价关系
```typst
$x sim y$ 表示 x 与 y 等价/相似
$a approx b$ 表示 a 约等于 b
$x equiv y$ 表示 x 与 y 全等
```

### 多个波浪符
```typst
$tilde(tilde(x))$ 双波浪符
$tilde(x)_1, tilde(x)_2, ..., tilde(x)_n$ 带下标的波浪符变量
```

## 与 LaTeX 的对比

| LaTeX | Typst | 说明 |
|-------|-------|------|
| `\tilde{x}` | `$tilde(x)$` | 单个字符上的波浪符 |
| `\widetilde{ABC}` | `$tilde(A B C)$` | 宽波浪符（覆盖多个字符） |
| `\sim` | `$sim$` | 相似符号 |
| `\approx` | `$approx$` | 约等于符号 |
| `\~{}` | `~` | 文本模式的波浪号 |

## 宽波浪符（Wide Tilde）

当需要在多个字符上方添加波浪符时：

```typst
$tilde(A B C)$
$tilde(x y z)$
```

Typst 会自动根据内容调整波浪符的宽度。

## 其他相关符号

```typst
$sim$ 相似符号 ∼
$approx$ 约等于 ≈
$equiv$ 全等 ≡
$cong$ 同余 ≅
```

## 实际应用示例

### 傅里叶变换
```typst
$tilde(f)(omega) = integral_(-infinity)^infinity f(t) e^(-i omega t) dif t$
```

### 估计量
```typst
设 $tilde(theta)$ 为参数 $theta$ 的估计量
```

### 拓扑空间
```typst
令 $tilde(X)$ 为空间 $X$ 的万有覆叠空间
```

### 变换后的变量
```typst
$tilde(x) = (x - mu) / sigma$ 标准化后的变量
```

## 注意事项

1. **自动间距**：Typst 会自动处理波浪符与字符之间的间距
2. **字体支持**：确保使用的字体支持波浪符显示
3. **可读性**：在复杂表达式中，波浪符可能影响可读性，考虑使用下标或上标替代方案
4. **数学模式**：波浪符主要用于数学模式 `$...$` 中

## 进阶技巧

### 自定义波浪符命令
```typst
#let td(x) = $tilde(#x)$

// 使用
$td(x) + td(y) = td(z)$
```

### 多种装饰组合
```typst
$tilde(hat(x))$ 先加帽子再加波浪符
$hat(tilde(x))$ 先加波浪符再加帽子
$tilde(bold(x))$ 粗体加波浪符
```

## 参考资源

- [Typst 官方文档 - Math](https://typst.app/docs/reference/math/)
- [Typst 官方文档 - Symbols](https://typst.app/docs/reference/symbols/)
- [Unicode 组合字符](https://unicode.org/charts/PDF/U0300.pdf)

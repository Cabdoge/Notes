# Typst Tilde Usage Guide

This document explains how to add tilde accents above letters in Typst.

## Basic Usage

### 1. Tilde in Math Mode

In Typst's math mode, you can add tilde accents using the following methods:

#### Method 1: Using the `tilde` function
```typst
$tilde(x)$
$tilde(A)$
$tilde(omega)$
```
Result: x̃, Ã, ω̃

#### Method 2: Using the `accent` function
```typst
$accent(x, tilde)$
$accent(A, tilde)$
```
Result: x̃, Ã

#### Method 3: Using Unicode combining characters
```typst
$x̃$
```
Note: The tilde follows directly after the letter (using Unicode combining tilde U+0303)

### 2. Tilde in Text Mode

#### Standalone tilde symbol
```typst
~
```
Result: ~ (standalone tilde)

#### Combining tilde in text
Use Unicode combining characters to add tilde in text:
```typst
añ
õ
ñ
```

## Common Mathematical Symbol Examples

### Vectors and Variable Notation
```typst
$tilde(x)$ represents another version of variable x
$tilde(bold(v))$ represents a transformed vector v
$tilde(f)(x)$ represents an approximation or variant of function f
```

### Equivalence Relations
```typst
$x sim y$ means x is equivalent to or similar to y
$a approx b$ means a is approximately equal to b
$x equiv y$ means x is congruent to y
```

### Multiple Tildes
```typst
$tilde(tilde(x))$ double tilde
$tilde(x)_1, tilde(x)_2, ..., tilde(x)_n$ tilde variables with subscripts
```

## Comparison with LaTeX

| LaTeX | Typst | Description |
|-------|-------|-------------|
| `\tilde{x}` | `$tilde(x)$` | Tilde over a single character |
| `\widetilde{ABC}` | `$tilde(A B C)$` | Wide tilde (covering multiple characters) |
| `\sim` | `$sim$` | Similarity symbol |
| `\approx` | `$approx$` | Approximately equal symbol |
| `\~{}` | `~` | Tilde in text mode |

## Wide Tilde

When you need to add a tilde over multiple characters:

```typst
$tilde(A B C)$
$tilde(x y z)$
```

Typst automatically adjusts the tilde width based on the content.

## Related Symbols

```typst
$sim$ similarity symbol ∼
$approx$ approximately equal ≈
$equiv$ equivalence ≡
$cong$ congruence ≅
```

## Practical Examples

### Fourier Transform
```typst
$tilde(f)(omega) = integral_(-infinity)^infinity f(t) e^(-i omega t) dif t$
```

### Estimators
```typst
Let $tilde(theta)$ be an estimator of parameter $theta$
```

### Topological Spaces
```typst
Let $tilde(X)$ be the universal covering space of space $X$
```

### Transformed Variables
```typst
$tilde(x) = (x - mu) / sigma$ standardized variable
```

## Important Notes

1. **Automatic Spacing**: Typst automatically handles spacing between tilde and characters
2. **Font Support**: Ensure your font supports tilde display
3. **Readability**: In complex expressions, tildes may affect readability; consider using subscripts or superscripts as alternatives
4. **Math Mode**: Tildes are primarily used in math mode `$...$`

## Advanced Tips

### Custom Tilde Command
```typst
#let td(x) = $tilde(#x)$

// Usage
$td(x) + td(y) = td(z)$
```

### Combining Multiple Decorations
```typst
$tilde(hat(x))$ hat first, then tilde
$hat(tilde(x))$ tilde first, then hat
$tilde(bold(x))$ bold with tilde
```

## References

- [Typst Official Documentation - Math](https://typst.app/docs/reference/math/)
- [Typst Official Documentation - Symbols](https://typst.app/docs/reference/symbols/)
- [Unicode Combining Characters](https://unicode.org/charts/PDF/U0300.pdf)

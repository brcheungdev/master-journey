[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 04 Notes 
# 计算机编程（Python）——第 04 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [String Basics / 字符串基础](#string-basics--字符串基础)
- [Escapes & Raw Strings / 转义与原始字符串](#escapes--raw-strings--转义与原始字符串)
- [Concatenation & Repetition / 连接与重复](#concatenation--repetition--连接与重复)
- [Indexing & Slicing / 索引与切片](#indexing--slicing--索引与切片)
- [Search & Selection / 搜索与判定](#search--selection--搜索与判定)
- [Count & Alnum Checks / 计数与字母数字检查](#count--alnum-checks--计数与字母数字检查)
- [Formatting Strings / 字符串格式化](#formatting-strings--字符串格式化)
- [Exercise 4‑1: find & rfind / 练习 4‑1：find 与 rfind](#exercise-4‑1-find--rfind--练习-4‑1find-与-rfind)
- [Exercise 4‑2: join  / 练习 4‑2：join](#exercise-4‑2-join-no-built-in--练习-4‑2join不得用内置)
- [Exercise 4‑3: split  / 练习 4‑3：split](#exercise-4‑3-split-no-built-in--练习-4‑3split不得用内置)

---

## Today’s Agenda / 今日教学安排

- Strings — creation, escapes, raw strings, concatenation, repetition, indexing & slicing, search & selection, basic formatting.  
字符串——创建、转义、原始字符串、连接、重复、索引与切片、搜索与判定、基础格式化。

- **Exercises:** 4‑1 **find & rfind**, 4‑2 **join**, 4‑3 **split**.  
**演习：**4‑1 **find 与 rfind**，4‑2 **join**，4‑3 **split**。

---

## Learning Objectives / 学习目标

- Create strings via **literals** and **`str()`**, and know **empty string** semantics.  
**掌握**通过**字面量**与 **`str()`** 创建字符串，并理解**空字符串**语义。

- Use **escapes** (`\n`, `\t`, `\'`, `\"`, `\\`) and **raw strings** `r"..."`.  
**会用**转义（`\n`、`\t`、`\'`、`\"`、`\\`）与**原始字符串** `r"..."`。

- Combine strings via **`+`** and multi‑line **literal adjacency / parentheses**; use **`*`** for repetition.  
**用**`+`** 与多行**字面量相邻/括号**连接；用 **`*`** 进行重复。

- Access substrings by **index** and **slice**; understand **immutability**.  
**通过**索引**与**切片**访问子串；理解**不可变性**。

- Search with **`find/rfind`** vs **`index/rindex`**; test prefixes/suffixes with **`startswith/endswith`**.  
**用**`find/rfind` 与 **`index/rindex`** 搜索；用 **`startswith/endswith`** 判断前后缀。

- Format strings with **f‑strings** and **`str.format` / format‑spec**.  
**用**f 字符串**与**`str.format`/格式说明符**格式化。

---

## String Basics / 字符串基础

- Literals: single `'...'`, double `"..."`, triple `'''...'''` / `"""..."""`.  
**字面量：**单引号 `'...'`、双引号 `"..."`、三引号 `'''...'''` / `"""..."""`。

- Empty string `""` is **Falsey** in boolean context.  
**空字符串 `""`** 在布尔上下文中为**假值**。

- `str(x)` makes a textual form of `x`.  
**`str(x)`** 生成对象 `x` 的字符串表示。

---

## Escapes & Raw Strings / 转义与原始字符串

- Common escapes: `\n` newline, `\t` tab, `\'` / `\"` quotes, `\\` backslash.  
**常用转义：**`\n` 换行、`\t` 制表、`\'`/`\"` 引号、`\\` 反斜杠。

- Raw strings: prefix **`r`** disables escape processing (useful for regex, paths).  
**原始字符串：**前缀 **`r`** 关闭转义处理（常用于正则、路径）。

> **Note / 注意：** Raw strings cannot end with a single trailing backslash.  
> **注意：**原始字符串**不能**以单个反斜杠结尾。

---

## Concatenation & Repetition / 连接与重复

- `"Hello, " + name` and literal adjacency `"Hello, " "world"`.  
**连接：**`"Hello, " + name` 与**字面量相邻** `"Hello, " "world"`。

- `"ha" * 3 -> "hahaha"`.  
**重复：**`"ha" * 3 -> "hahaha"`。

- Multi‑line concatenation via parentheses:  
**多行连接（括号）示例：**
```
s = (
    "It "
    "rains "
    "cats and dogs."
)
```

---

## Indexing & Slicing / 索引与切片

- `s[i]` (0‑based), negative indices from the **end**; slices `s[start:stop:step]`.  
**`s[i]`**（从 0 开始），负索引从**末尾**计；切片 `s[start:stop:step]`。

- Strings are **immutable**: `s[0] = 'X'` is invalid; use rebuild via slices or `.replace()`.  
**字符串不可变**：`s[0] = 'X'` 非法；可用切片或 `.replace()` 生成新串。

---

## Search & Selection / 搜索与判定

- `s.find(sub)` → lowest offset or **`-1`** if not found; `s.rfind(sub)` → highest offset or **`-1`**.  
**`s.find(sub)`** → 最小下标，未找到返回 **`-1`**；**`s.rfind(sub)`** → 最大下标，未找到返回 **`-1`**。

- `s.index(sub)` / `s.rindex(sub)` → like find/rfind but **raise `ValueError`** if not found.  
**`s.index(sub)` / `s.rindex(sub)`** → 类似 find/rfind，但未找到时**抛异常**。

- `s.startswith(prefix)` / `s.endswith(suffix)` test beginnings/endings.  
**`s.startswith(prefix)` / `s.endswith(suffix)`** 判断前/后缀。

---

## Count & Alnum Checks / 计数与字母数字检查

- `s.count(sub)` counts non‑overlapping occurrences.  
**`s.count(sub)`** 统计**不重叠**的出现次数。

- `s.isalpha()` / `s.isdigit()` / `s.isalnum()` for character classes.  
**`s.isalpha()` / `s.isdigit()` / `s.isalnum()`** 检查字符类别。

---

## Formatting Strings / 字符串格式化

- **f‑strings:** `f"{name} scored {score:.1f}"`.  
**f 字符串：**`f"{name} scored {score:.1f}"`。

- **`str.format`:** `"{0:^10s}{1:+08.2f}".format(name, value)`.  
**`str.format`：**`"{0:^10s}{1:+08.2f}".format(name, value)`。

- **Format‑spec highlights:** alignment `<^>`, sign `+ - space`, width, precision `.2f`, type `s d f` …  
**格式说明要点：**对齐 `<^>`、符号 `+ - 空格`、宽度、精度 `.2f`、类型 `s d f` 等。

---

## Exercise 4‑1: find & rfind / 练习 4‑1：find 与 rfind

> **Goal:** Implement `find(string, word)` and `rfind(string, word)` that mirror `str.find`/`str.rfind` behaviors.  
> **目标：**实现 `find(string, word)` 与 `rfind(string, word)`，行为与 `str.find`/`str.rfind` 一致。

- **Key rules:** return **`-1`** if not found; for **empty** `word`, `find` returns **`0`**, `rfind` returns **`len(string)`**.  
**要点：**未找到返回 **`-1`**；**空子串**时，`find → 0`，`rfind → len(string)`。

- **Left vs Right search**: scan offsets from **left to right** or **right to left**.  
**左右搜索：**从**左至右**或**右至左**扫描候选起点。

```python
def rfind(string: str, word: str) -> int:
    m, n = len(word), len(string)
    if m == 0:
        return n
    for i in range(n - m, -1, -1):
        if string[i:i+m] == word:
            return i
    return -1
```

> [rfind.py — Code / rfind.py — 代码](./src/rfind.py)

---

## Exercise 4‑2: join  / 练习 4‑2：join

> **Goal:** Implement `join(iterable, sep)` equivalent to `sep.join(iterable)` without calling `.join()`.  
> **目标：**实现 `join(iterable, sep)`，与 `sep.join(iterable)` 等价，但**不得调用** `.join()`。

- **Edge cases:** empty iterable → `""`; single item → `str(item)`; always **stringify** each item.  
**边界：**空序列 → `""`；单元素 → `str(item)`；元素需**统一转为字符串**。

```python
def join(iterable, sep: str) -> str:
    out, first = "", True
    for item in iterable:
        if not first:
            out += sep
        out += str(item)
        first = False
    return out
```

> [join.py — Code / join.py — 代码](./src/join.py)

---

## Exercise 4‑3: split  / 练习 4‑3：split

> **Goal:** Implement `split(string, sep)` using `.find()`; **do not** call `.split()`.  
> **目标：**用 `.find()` 实现 `split(string, sep)`；**不得**调用 `.split()`。

- **Edge cases:** `sep == ""` should **raise** `ValueError("empty separator")` (match Python).  
**边界：**`sep == ""` 应 **抛出** `ValueError("empty separator")`（与 Python 一致）。

```python
def split(string: str, sep: str):
    if sep == "":
        raise ValueError("empty separator")
    parts, i, k = [], 0, len(sep)
    while True:
        j = string.find(sep, i)
        if j == -1:
            parts.append(string[i:])
            break
        parts.append(string[i:j])
        i = j + k
    return parts
```

> [split.py — Code / split.py — 代码](./src/split.py)

<h2></h2>

[← Previous Lecture / 上一讲](./lecture03.md) · [Next Lecture / 下一讲 →](./lecture05.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

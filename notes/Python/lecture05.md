[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 04 Notes  
# 计算机编程（Python）——第 04 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Creating Strings / 创建字符串](#creating-strings--创建字符串)
- [Comments / 注释](#comments--注释)
- [Escapes with Backslash / 反斜杠转义](#escapes-with-backslash--反斜杠转义)
- [Raw Strings / 原始字符串](#raw-strings--原始字符串)
- [Concatenation / 字符串连接](#concatenation--字符串连接)
- [Repetition / 字符串重复](#repetition--字符串重复)
- [Indexing & Slicing / 索引与切片](#indexing--slicing--索引与切片)
- [Search: find vs rfind vs index / 搜索：find、rfind 与 index](#search-find-vs-rfind-vs-index--搜索findrfind-与-index)
- [Prefix/Suffix: startswith & endswith / 前后缀判断](#prefixsuffix-startswith--endswith--前后缀判断)
- [Counting & Character Tests / 计数与字符类别判断](#counting--character-tests--计数与字符类别判断)
- [Formatting Basics / 字符串格式化基础](#formatting-basics--字符串格式化基础)
- [Exercises Overview / 演习总览（find/rfind、join、split）](#exercises-overview--演习总览findrfindjoinsplit)
- [Appendix: Common Pitfalls / 附录：常见陷阱](#appendix-common-pitfalls--附录常见陷阱)

---

## Today’s Agenda / 今日教学安排

- Strings — creation, comments, escapes, raw strings, concatenation, repetition, indexing, slicing, search.  
字符串——创建、注释、转义、原始字符串、连接、重复、索引、切片、搜索。

- **Exercises:** 4‑1 **find & rfind**, 4‑2 **join**, 4‑3 **split**.  
**演习：**4‑1 **find 与 rfind**，4‑2 **join**，4‑3 **split**。

---

## Learning Objectives / 学习目标

- Understand how to **create and represent** strings with different quotation styles and `str()`.  
**理解**如何使用不同引号风格与 `str()` **创建与表示**字符串。

- Use **escapes** and **raw strings** correctly; know when escapes are processed.  
**正确使用**转义**与**原始字符串**；理解何时会解析转义。

- Manipulate strings via **concatenation**, **repetition**, **indexing**, **slicing**.  
**掌握**通过**连接**、**重复**、**索引**、**切片**操作字符串。

- Search and test substrings; distinguish `find/rfind` vs `index/rindex`.  
**学会**搜索与判定子串；区分 `find/rfind` 与 `index/rindex`。

- Implement `find/rfind`, `join`, and `split` manually (per exercises).  
**能手写**`find/rfind`、`join`、`split`（按照演习要求）。

---

## Creating Strings / 创建字符串

- Single `'...'`, double `"..."`, triple `'''...'''` or `"""..."""` (multi‑line).  
**单引号 `'...'`、双引号 `"..."`、三引号 `'''...'''` 或 `"""..."""`（可多行）。**

- Triple quotes preserve newlines and quotes without escaping.  
**三引号可直接包含换行与引号而无需转义。**

- `str(x)` converts an object to its textual form.  
**`str(x)`** 将任意对象转换为文本表示。

---

## Comments / 注释

- Line comments start with `#`, everything to the line end is ignored.  
**行注释以 `#` 开头**，直到行尾的内容都会被忽略。

- Keep comments **brief and precise**; prefer explaining **why** instead of **what**.  
**注释应**简明且准确**；优先解释**为什么**而非**做了什么**。

---

## Escapes with Backslash / 反斜杠转义

- Common escapes: `\n` newline, `\t` tab, `\'` / `\"` quotes, `\\` backslash.  
**常见转义：**`\n` 换行、`\t` 制表、`\'`/`\"` 引号、`\\` 反斜杠。

- Use escapes when the same quote is used inside a quoted string.  
**当内外使用相同引号时可用转义**来包含引号本身。

- In triple‑quoted strings, fewer escapes are needed; indentation may be captured.  
**三引号字符串**通常需要更少转义；注意会**包含缩进与换行**。

---

## Raw Strings / 原始字符串

- Prefix `r"..."` disables escape processing: `r"\n"` has **two characters** `\` and `n`.  
**前缀 `r"..."` 关闭转义处理：**`r"\n"` 实际是两个字符 `\` 与 `n`。

- Useful for regex and Windows paths.  
**常用于**正则表达式**与 Windows 路径。**

- **Limitation:** cannot end with a single trailing backslash.  
**限制：****不能**以**单个反斜杠**结尾。

---

## Concatenation / 字符串连接

- With `+`: `"Hello, " + name`.  
**使用 `+`：**`"Hello, " + name`。

- Adjacent literals: `"Hello, " "world"` (combined at compile time).  
**字面量相邻：**`"Hello, " "world"`（编译期合并）。

- Multi‑line via parentheses for readability:  
**使用括号多行连接，提高可读性：**
```python
s = (
    "It "
    "rains "
    "cats and dogs."
)
```

---

## Repetition / 字符串重复

- `"ha" * 3 -> "hahaha"`.  
**`"ha" * 3 -> "hahaha"`。**

- Useful for **padding**, simple **ASCII art**, or quick **test strings**.  
**常用于**填充**、简单 **ASCII 图案**、快速**测试字符串**。

---

## Indexing & Slicing / 索引与切片

- Indexing starts at **0**; negative indices from the **end** (`s[-1]` last).  
**索引从 **0** 开始；负索引自**末尾**计（`s[-1]` 为最后一个）。**

- Slicing: `s[start:stop:step]`; out‑of‑range slices **don’t raise**.  
**切片：**`s[start:stop:step]`；越界切片**不会报错**。

- Strings are **immutable** — operations return **new** strings.  
**字符串是**不可变**的——相关操作返回**新**字符串。

---

## Search: find vs rfind vs index / 搜索：find、rfind 与 index

- `s.find(sub)` → lowest index or `-1`; `s.rfind(sub)` → highest index or `-1`.  
**`s.find(sub)`** → 最小下标或 `-1`；**`s.rfind(sub)`** → 最大下标或 `-1`。

- `s.index(sub)` / `s.rindex(sub)` → like find/rfind but **raise `ValueError`** if not found.  
**`s.index(sub)` / `s.rindex(sub)`** → 类似 find/rfind，但未找到时**抛出 `ValueError`**。

- Empty substring: `find("") == 0`, `rfind("") == len(s)`.  
**空子串：**`find("") == 0`，`rfind("") == len(s)`。

---

## Prefix/Suffix: startswith & endswith / 前后缀判断

- `s.startswith(prefix)` / `s.endswith(suffix)` test the beginning and ending.  
**`s.startswith(prefix)` / `s.endswith(suffix)`** 用于判断前缀与后缀。

- Accept **tuples** of prefixes/suffixes: `s.startswith(("http://","https://"))`.  
**可接受**元组**：`s.startswith(("http://","https://"))`。

---

## Counting & Character Tests / 计数与字符类别判断

- `s.count(sub)` counts **non‑overlapping** occurrences.  
**`s.count(sub)`** 统计**不重叠**出现次数。

- Character classes: `s.isalpha()`, `s.isdigit()`, `s.isalnum()`, `s.isspace()`, etc.  
**字符类别：**`s.isalpha()`、`s.isdigit()`、`s.isalnum()`、`s.isspace()` 等。

---

## Formatting Basics / 字符串格式化基础

- **f‑strings:** `f"{name} scored {score:.1f}"`.  
**f 字符串：**`f"{name} scored {score:.1f}"`。

- **`str.format`:** `"{0:^10s}{1:+08.2f}".format(name, value)`.  
**`str.format`：**`"{0:^10s}{1:+08.2f}".format(name, value)`。

- **Format‑spec quick view:** alignment `<^>`, sign `+ - space`, width, precision `.2f`, type `s d f` …  
**格式说明速览：**对齐 `<^>`、符号 `+ - 空格`、宽度、精度 `.2f`、类型 `s d f` 等。

---

## Exercises Overview / 演习总览（find/rfind、join、split）

- **find/rfind:** implement lowest/highest index search; return `-1` when absent; handle empty `word`.  
**find/rfind：**实现最小/最大起点搜索；未找到返回 `-1`；处理空子串。

- **join:** implement `join(iterable, sep)` without calling `.join()`.  
**join：**手写 `join(iterable, sep)`，**不得调用**`.join()`。

- **split:** implement `split(string, sep)` using `.find()` and preserve empty fields; raise on empty `sep`.  
**split：**使用 `.find()` 实现 `split(string, sep)`，保留空字段；空分隔符需抛异常。

> For reference implementations and testbenches, see `Python/src/rfind.py`, `join.py`, `split.py` we prepared earlier.  
> 参考实现与测试脚本见我们先前提供的 `Python/src/rfind.py`、`join.py`、`split.py`。

---

## Appendix: Common Pitfalls / 附录：常见陷阱

- **Immutability surprises:** `s[0] = 'X'` is illegal; use slicing + concatenation or `.replace()`.  
**不可变性误区：**`s[0] = 'X'` 非法；需用切片+连接或 `.replace()`。

- **Raw strings cannot end with single `\`.**  
**原始字符串不能以单个 `\` 结尾。**

- **`index/rindex` raise on missing** — prefer `find/rfind` if absence is common.  
**`index/rindex` 未找到会抛错**——若经常找不到，优先 `find/rfind`。

- **`split` with explicit `sep` preserves empty fields** (different from whitespace split behavior).  
**显式 `sep` 的 `split` 会保留空字段**（与空白分隔的 `split()` 不同）。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture03.md) · [Next Lecture / 下一讲 →](./lecture05.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

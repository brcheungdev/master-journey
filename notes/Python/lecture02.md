[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md) 

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 02 Notes / 计算机编程（Python）——第 02 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Data — Types, Values, Variables & Names / 数据——类型、值、变量与名字](#data--types-values-variables--names--数据类型值变量与名字)
- [Numbers — Booleans, Integers, Floats & Type Conversion / 数值——布尔、整数、浮点与类型转换](#numbers--booleans-integers-floats--type-conversion--数值布尔整数浮点与类型转换)
- [Exercises / 演习](#exercises--演习)
- [Appendix — Quick Reference Tables / 附录——速查表](#appendix--quick-reference-tables--附录速查表)

---

## Today’s Agenda / 今日教学安排

- Data: types, values, variables and names; Numbers: booleans, integers, floating‑point, conversion.  
数据：类型、值、变量与名字；数值：布尔、整数、浮点与类型转换

- **Exercises:** Example problems and two small programming tasks (BMI; Heron’s formula).  
**演习：**例题与两个小程序任务（BMI；海伦公式）。


---

## Learning Objectives / 学习目标

- Understand **Python’s built‑in data types**, **mutability**, and the **object model** (type, id, value, reference counting).  
**理解 **Python 内建数据类型**、**可变性（mutability）**与**对象模型**（类型、ID、值、引用计数）。

- Apply **variable naming rules**, **assignment semantics**, and **multiple assignment** correctly.  
**掌握**变量命名规则**、**赋值语义**与**多重赋值**的正确使用。

- Master **numeric literals and operators**, **precedence**, **bases (bin/oct/hex)**, **in‑place ops**, and **conversion functions**.  
**掌握**数值字面量与运算符**、**优先级**、**进制（bin/oct/hex）**、**就地运算**与**类型转换函数**。

- Implement small functions with **tests**: `bmi(weight, height)` and `heron(a, b, c)`.  
**实现**小函数并通过**测试**：`bmi(weight, height)` 与 `heron(a, b, c)`。

---

## Data — Types, Values, Variables & Names / 数据——类型、值、变量与名字

- **Core built‑in types (intro):** `bool`, `int`, `float`, `complex`, `str`, `list`, `tuple`, `bytes`, `bytearray`, `set`, `frozenset`, `dict`.  
**内建核心类型（入门）：**`bool`、`int`、`float`、`complex`、`str`、`list`、`tuple`、`bytes`、`bytearray`、`set`、`frozenset`、`dict`。

- **Mutability:** lists/sets/dicts/bytearray are **mutable**; numbers, strings, tuples, bytes, frozenset are **immutable**.  
**可变性：**列表/集合/字典/字节数组为**可变**；数值、字符串、元组、字节序列、不可变集合为**不可变**。

- **Variables are names, not boxes:** a variable **binds** to an object; **rebinding** points the name to a new object (old object’s **refcount** decrements).  
**变量是名字而非盒子：**变量**绑定**到对象；**重新绑定**会让名字指向新对象（旧对象**引用计数**递减）。

- **Naming rules:** letters (a–z, A–Z), digits (0–9), underscore `_`; **case‑sensitive**; must **not** start with a digit; avoid leading `_` unless intended; **not** a **reserved word**.  
**命名规则：**字母（a–z，A–Z）、数字（0–9）、下划线 `_`；**区分大小写**；不得以数字开头；避免以 `_` 起始（有特殊含义）；且**不得**为**保留字**。

- **Assignment patterns:** literals to variables; variable‑to‑variable; **multiple assignment** (`a = b = 5`); tuple unpacking (`x, y = 1, 2`).  
**赋值方式：**字面量赋值；变量间赋值；**多重赋值**（`a = b = 5`）；元组拆包（`x, y = 1, 2`）。

> **Tip：** Mutability affects behavior on shared references—mutating a list via one name is visible via all names bound to it.  
> **提示：**可变性影响共享引用的行为——通过某个名字修改列表，会在所有绑定到它的名字上可见。

---

## Numbers — Booleans, Integers, Floats & Type Conversion / 数值——布尔、整数、浮点与类型转换

- **Booleans:** `True` / `False`; `bool(x)` returns `False` for `False`, `0`, `0.0`, empty containers/strings; otherwise `True`.  
**布尔：**`True` / `False`；`bool(x)` 对 `False`、`0`、`0.0`、空容器/空串返回 `False`，否则 `True`。

- **Integer literals & ops:** `+ - * / // % **`; **precedence**: `**` > `* / // %` > `+ -`; use **parentheses** for clarity.  
**整数字面量与运算：**`+ - * / // % **`；**优先级**：`**` > `* / // %` > `+ -`；用**括号**澄清意图。

- **Readable digits:** underscores as separators: `1_000_000`; **no commas**.  
**可读数字：**用下划线分隔：`1_000_000`；**不要用逗号**。

- **Division by zero raises an exception**, including `//` and `%`.  
**除以零会抛异常**，`//` 与 `%` 亦然。

- **In‑place ops:** `+= -= *= /= //= %= **=` as concise forms of `x = x <op> y`.  
**就地运算：**`+= -= *= /= //= %= **=` 是 `x = x <op> y` 的简写。

- **Bases:** binary `0b`/`0B`, octal `0o`/`0O`, hex `0x`/`0X`; conversion helpers: `bin()`, `oct()`, `hex()`.  
**进制：**二进制 `0b`/`0B`，八进制 `0o`/`0O`，十六进制 `0x`/`0X`；转换函数：`bin()`、`oct()`、`hex()`。

- **Int size:** Python `int` has **arbitrary precision** (no fixed 32/64‑bit overflow).  
**整数大小：**Python `int` 为**任意精度**（无固定 32/64 位溢出）。

- **Floats:** decimal or scientific notation; be mindful of **binary floating‑point rounding**.  
**浮点：**十进制或科学计数法；注意**二进制浮点舍入**。

- **Conversions:** `int()`, `float()`, `bool()`, character/ordinal `chr()`, `ord()`. Implicit casts occur in mixed numeric ops.  
**类型转换：**`int()`、`float()`、`bool()`，字符/码点：`chr()`、`ord()`。数值混合运算中可发生隐式转换。

---

## Exercises / 演习

### Example: Triangle Area / 例题：三角形面积

- Compute area from base and height; practice input, arithmetic, formatted output.  
**通过底与高计算面积；练习输入、算术与格式化输出。**

```python
# Example (with f-strings) / 示例（使用 f 字符串）
base = float(input("base: "))
height = float(input("height: "))
area = 0.5 * base * height
print(f"Area = {area}")
```

> **FYI / 说明：** Without f‑strings you can build strings via concatenation and `str()` conversion, but readability suffers.  
> **提示：**若不使用 f 字符串，可用拼接与 `str()` 转换，但**可读性变差**。

### Exercise 2‑1: BMI

- **Definition:** `BMI = weight / (height ** 2)` where `weight` in **kg**, `height` in **meters**; **truncate fractional part** and return an **integer**.  
**定义：**`BMI = weight / (height ** 2)`，`weight` 单位 **kg**，`height` 单位 **米**；**截断小数部分**并返回**整数**。

- **Starter testbench:** `bmi.py` calls `bmi(w, h)` on multiple vectors and checks equality to an expected **int**.  
**测试脚本：**`bmi.py` 会对多组参数调用 `bmi(w, h)`，并与期望的**整数**结果比对。

```python
# Complete this function / 补全该函数
def bmi(weight, height):
    # truncate to int / 截断为整数
    return int(weight / (height * height))
```

- [bmi.py — Code / bmi.py — 代码](./src/bmi.py)


### Exercise 2‑2: Heron’s Formula / 练习 2‑2：海伦公式

- **Formula:** Given triangle sides `a, b, c`, semiperimeter `s = (a + b + c) / 2`, area `A = sqrt(s * (s-a) * (s-b) * (s-c))`.  
**公式：**三边 `a, b, c`，半周长 `s = (a + b + c) / 2`，面积 `A = sqrt(s * (s-a) * (s-b) * (s-c))`。

- **Task:** Implement `heron(a, b, c)` returning a **float**; use `math.sqrt`.  
**任务：**实现 `heron(a, b, c)` 返回**浮点**；使用 `math.sqrt`。

```python
import math

def heron(a, b, c):
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
```

- [heron.py — Code / heron.py — 代码](./src/heron.py)

> **Note / 注意：** Inputs must satisfy triangle inequality; otherwise the radicand becomes negative.  
> **注意：**输入需满足三角不等式，否则被开方数为负。

---

## Appendix — Quick Reference Tables / 附录——速查表

**Core Types & Mutability / 核心类型与可变性**

| Type / 类型 | Mutable? / 可变？ | Examples / 示例 |
|---|---|---|
| `bool` | No / 否 | `True`, `False` |
| `int` | No / 否 | `0`, `-3`, `47`, `25_000` |
| `float` | No / 否 | `3.14`, `2.7e5` |
| `complex` | No / 否 | `3j`, `5 + 9j` |
| `str` | No / 否 | `'alas'`, "a verse" |
| `list` | Yes / 是 | `[1, 2, 3]` |
| `tuple` | No / 否 | `(2, 4, 8)` |
| `bytes` | No / 否 | `b'ab\xff'` |
| `bytearray` | Yes / 是 | `bytearray(b'abc')` |
| `set` | Yes / 是 | `{3, 5, 7}` |
| `frozenset` | No / 否 | `frozenset([1, 2])` |
| `dict` | Yes / 是 | `{'a': 1}` |

**Integer Operators & Precedence / 整数运算与优先级**

| Op / 运算 | Meaning / 含义 | Example / 例 | Result / 结果 |
|---|---|---|---|
| `+` | addition / 加法 | `5 + 8` | `13` |
| `-` | subtraction / 减法 | `90 - 10` | `80` |
| `*` | multiplication / 乘法 | `4 * 7` | `28` |
| `/` | float division / 浮点除法 | `7 / 2` | `3.5` |
| `//` | floor division / 整除 | `7 // 2` | `3` |
| `%` | modulo / 取余 | `7 % 3` | `1` |
| `**` | power / 幂 | `3 ** 4` | `81` |

**Bases & Conversions / 进制与转换**

- `0b1010 == 10`, `0o12 == 10`, `0xA == 10`  
**示例：**`0b1010 == 10`，`0o12 == 10`，`0xA == 10`。

- `bin(10) -> '0b1010'`, `oct(10) -> '0o12'`, `hex(10) -> '0xa'`  
**转换：**`bin(10) -> '0b1010'`，`oct(10) -> '0o12'`，`hex(10) -> '0xa'`。

---

[← Previous Lecture / 上一讲](./lecture01.md) · [Next Lecture / 下一讲 →](./lecture03.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

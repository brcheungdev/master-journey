[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 01 Notes 
# 计算机编程（Python）——第 01 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](./lecture01.md#todays-agenda--今日教学安排)
- [Recommended Python Books / 推荐的python书目](./lecture01.md#recommended-python-books--推荐的python书目)
- [What is Python? / 什么是 Python？](./lecture01.md#what-is-python--什么是-python)
- [Python in the Real World / Python 在现实世界中的应用](./lecture01.md#python-in-the-real-world--python-在现实世界中的应用)
- [Why Python / When Not to Use / 为什么选择 Python / 何时不该用](./lecture01.md#why-python--when-not-to-use--为什么选择-python--何时不该用)
- [The Zen of Python (PEP 20) / Python 之禅（PEP 20）](./lecture01.md#the-zen-of-python-pep-20--python-之禅pep-20)
- [Jupyter Notebook Basics / Jupyter Notebook 基础](./lecture01.md#jupyter-notebook-basics--jupyter-notebook-基础)
- [I/O, Data Types & Operators / 输入输出、数据类型与运算符](./lecture01.md#io-data-types--operators--输入输出数据类型与运算符)
- [Numeric Computation / 数值计算](./lecture01.md#numeric-computation--数值计算)
- [Conditionals / 条件分支](./lecture01.md#conditionals--条件分支)
- [Loops / 循环](./lecture01.md#loops--循环)
- [Functions / 函数](./lecture01.md#functions--函数)
- [Exercises & Prep Tasks / 课后练习与预习任务](./lecture01.md#exercises--prep-tasks--15-课后练习与预习任务)

---

## Today’s Agenda / 今日教学安排

- **Lecture:** Lesson 1-0 (Course Overview), Lesson 1-1 (Python Overview), Lesson 1-2 (Python Super Intro).  
**讲授：**Lesson 1-0（课程概览）、Lesson 1-1（Python 概述）、Lesson 1-2（Python 超入门）。

- **Exercises:** Exercise 1-0 (Setup), Exercise 1-1 (Super Intro practice).  
**演习：**Exercise 1-0（环境准备）、Exercise 1-1（超入门练习）。

- **Preview task briefing.**  
**预习任务说明。**


---

## Recommended Python Books / 推荐的python书目

- **[O’Reilly] Introducing Python, 2nd Ed.** (Bill Lubanovic) — ISBN 978-1492051367.  
**【O’Reilly】《Introducing Python》第2版**（Bill Lubanovic）— ISBN 978-1492051367。

- **Chinese Translation:** *Python 语言及其应用（第2版）*, 人民邮电出版社，**ISBN 978-7-115-58622-3**, 纸质 RMB **129.8**，电子版 RMB **64.9**。  
**中文版：**《Python 语言及其应用（第2版）》，人民邮电出版社，**ISBN 978-7-115-58622-3**，纸书 **129.8 元**，电子版 **64.9 元**。

- **独習 Python**（山田祥寛，翔泳社，2020）— ISBN 978-4798163642。  
**《独習 Python》**（山田祥寛，翔泳社，2020）— ISBN 978-4798163642。

- **Fluent Python, 2nd Ed.**（Luciano Ramalho, O’Reilly Japan）— ISBN 978-4-87311-817-8。  
**《Fluent Python（第2版）》**（Luciano Ramalho，O’Reilly Japan）— ISBN 978-4-87311-817-8。

- **Python3 入門**（中村勝則）。  
**《Python3 入门》**（中村胜则）。

---

## What is Python? / 什么是 Python？

- **Open‑source** programming language started in **1989** by **Guido van Rossum**; named after **Monty Python**.  
**开源**语言，**Guido van Rossum** 于 **1989 年**启动；名称源于喜剧团体 **Monty Python**。

- Backed by **Python Software Foundation (PSF)** — **https://www.python.org/**.  
由 **Python Software Foundation (PSF)** 支持 —— **https://www.python.org/**。

- **Core traits:** **ease of use**, **readability**, **clarity**, strong **ecosystem** (dev tools & libraries).  
**核心特性：****易用**、**可读**、**清晰**，以及强大的**生态（开发环境与库）**。

- **Application areas:** scripting, GUI/web, servers, cloud, mobile, **IoT/embedded**, scientific computing, **data science**, **ML**...      
**应用领域：**脚本、GUI/网页、服务器、云端、移动端、**物联网/嵌入式**、科学计算、**数据科学**、**机器学习** 等。

---

## Python in the Real World / Python 在现实世界中的应用

- In use **since 1991**; consistently in **Top 5** most popular languages (e.g., **TIOBE** index).  
自 **1991** 年起使用至今；常年位居**最流行语言前五**（如 **TIOBE** 指数）。

- Powers backends at **Google, YouTube, Dropbox, Instagram, Netflix, Hulu**, etc.  
驱动 **Google、YouTube、Dropbox、Instagram、Netflix、Hulu** 等的后端。

- Key benefit: **high developer productivity**.  
关键优势：**开发效率高**。

---

## Why Python / When Not to Use / 为什么选择 Python / 何时不该用

- **Why popular:** **general‑purpose**, designed for **readability**, **concise code**, **“batteries‑included”** libraries, **open source**.  
**受欢迎原因：****通用**、**可读性导向**、**代码简洁**、**“电池齐全”**的标准库、**开源**。

- **Limits:** Might not be **preinstalled**; for **CPU‑bound** ultra‑high‑performance tasks, languages like **C/C++/C#/Java** may be faster.  
**限制：**可能不是**预装**；对**强 CPU 绑定**且极度**性能敏感**的任务，**C/C++/C#/Java** 往往更快。

- **Mitigations:** Write hot paths in **C extensions**; CPython keeps getting **faster**; focus on **better algorithms** first.  
**缓解方式：**将热点路径用 **C 扩展**实现；**CPython** 不断**优化**；优先寻求**更佳算法**。

---

## The Zen of Python (PEP 20) / Python 之禅（PEP 20）

> **Guiding principles for Python’s design.**  
> **Python 设计的指导原则。**

```
Beautiful is better than ugly.
醜いより美しいほうがよい。/ 醜陋不如美观。

Explicit is better than implicit.
暗黙より明示のほうがよい。/ 隐式不如显式。

Simple is better than complex.
複雑より単純のほうがよい。/ 复杂不如简单。

Complex is better than complicated.
極端な複雑よりただの複雑のほうがよい。/ 过度繁复不如适度复杂。

Flat is better than nested.
入れ子よりもフラットのほうがよい。/ 扁平优于嵌套。

Sparse is better than dense.
密よりも疎のほうがよい。/ 稀疏优于密集。

Readability counts.
読みやすさは大切だ。/ 可读性至关重要。

Special cases aren't special enough to break the rules.
特殊条件だからといって原則を破ってよいわけではない。/ 特例不足以破坏规则。

Although practicality beats purity.
実用性は純粋性に勝る。/ 但实用优先于纯粹。

Errors should never pass silently.
無言でエラーを次に渡してはならない。/ 错误不应悄然溜过。

Unless explicitly silenced.
わざと黙らされている場合を除き。/ 除非被明确消音。

In the face of ambiguity, refuse the temptation to guess.
曖昧なものが出てきたときに推測に頼るな。/ 面对歧义，拒绝臆猜。

There should be one— and preferably only one —obvious way to do it.
当然の方法は１つ、むしろ１つだけ。/ 应该有且最好只有一种显而易见的做法。

Although that way may not be obvious at first unless you're Dutch.
ただしオランダ人でなければ最初は当然と思わないかも。/ 但除非你是荷兰人，这种方法起初未必显而易见。

Now is better than never.
今するのはしないままよりもよい。/ 现在做胜过永不做。

Although never is often better than right now.
もっとも、しないままのほうが慌てて今すぐするよりよいことも多い。/ 但仓促立刻做不如谨慎不做。

If the implementation is hard to explain, it's a bad idea.
実装を説明するのが難しいなら、それは悪いアイデア。/ 难以解释的实现往往是坏主意。

If the implementation is easy to explain, it may be a good idea.
実装を説明するのが簡単なら、良いアイデアかもしれない。/ 易于解释的实现可能是好主意。

Namespaces are one honking great idea — let's do more of those!
名前空間はすばらしいアイデアの1つだ。もっとやろう！/ 命名空间是极好的主意——多用！
```

> <details><summary>Extra tip / 补充说明</summary>
> You can print the Zen anytime in Python with `import this`.  
> 在 Python 中可用 `import this` 随时打印《Python 之禅》。
> </details>

---

## Jupyter Notebook Basics / Jupyter Notebook 基础

- Write and run code in **cells**; toggle **line numbers** via *View → Toggle Line Numbers*.  
在**单元格**中编写并执行代码；通过 *View → Toggle Line Numbers* 切换**行号**。

- Change **cell type** to **Markdown** for narrative text and math; support **LaTeX math** in Markdown.  
将单元格类型切换为 **Markdown** 以撰写说明与数学公式；Markdown 支持 **LaTeX 数学**。

- Typical workflow: mix **code cells** and **Markdown cells** for **literate programming**.  
常见做法：**代码单元**与**Markdown 单元**混合，实现**可读性编程**。

---

## I/O, Data Types & Operators / 输入输出、数据类型与运算符

- **Output:** `print()` displays text and variable values.  
**输出：**使用 `print()` 输出文本与变量值。

- **Input:** `input()` returns **string**; convert types as needed.  
**输入：**`input()` 返回**字符串**；必要时进行类型转换。

**Common Built‑in Types / 常见内建类型**

| Name | 名称 | Type | Examples |
|---|---|---|---|
| Boolean | 布尔值 | `bool` | `True`, `False` |
| Integer | 整数 | `int` | `47`, `25000`, `-36` |
| Float | 浮点数 | `float` | `3.14`, `2.7e5` |
| String | 字符串 | `str` | `'hello'`, `"world"`, `"""cat and dog"""` |
| List | 列表 | `list` | `[2022, 4, 1, "Friday"]` |
| Tuple | 元组 | `tuple` | `(3, 2, 1, "Go")` |
| Dict | 字典 | `dict` | `{"apple": "red", "lemon": "yellow"}` |
| Set | 集合 | `set` | `{"apple", "orange", "lemon"}` |

**Comparison Operators / 比较运算符**

| Op | Meaning / 含义 | Example / 例 | Bool / 结果 |
|---|---|---|---|
| `==` | equal / 等于 | `5 == 3` | `False` |
| `!=` | not equal / 不等于 | `5 != 3` | `True` |
| `>` | greater / 大于 | `5 > 3` | `True` |
| `>=` | ≥ / 大于等于 | `5 >= 3` | `True` |
| `<` | less / 小于 | `5 < 3` | `False` |
| `<=` | ≤ / 小于等于 | `5 <= 3` | `False` |

**Numeric Operators / 数值运算符**

| Op | Meaning / 含义 | Example / 例 | Result / 结果 |
|---|---|---|---|
| `+` | addition / 加法 | `5 + 8` | `13` |
| `-` | subtraction / 减法 | `90 - 10` | `80` |
| `*` | multiplication / 乘法 | `4 * 7` | `28` |
| `/` | float division / 浮点除法 | `7 / 2` | `3.5` |
| `//` | floor div / 整除（向下取整） | `7 // 2` | `3` |
| `%` | modulo / 取余 | `7 % 3` | `1` |
| `**` | power / 幂 | `3 ** 4` | `81` |

---

## Numeric Computation / 数值计算

- Example topics include **triangle area** and **circle area** computations.  
示例涵盖**三角形面积**与**圆面积**的计算。

```python
# Triangle area / 三角形面积
base = float(input("Base: "))   # 底
height = float(input("Height: "))  # 高
area = 0.5 * base * height
print("Area:", area)

# Circle area / 圆面积
import math
r = float(input("Radius: "))
print("Area:", math.pi * r * r)
```

---

## Conditionals / 条件分支

- Use `if`, `elif`, `else` to branch on **boolean** expressions.  
使用 `if`、`elif`、`else` 根据**布尔表达式**进行分支。

```
# if example / if 示例
if 2 > 3:
    print("won't run")  # 不会执行
print("done")           # 会执行
```

```
# if-else with a flag / 带标志位的 if-else
disaster = True
if disaster:
    print("woe!")   # 灾难：输出 woe!
else:
    print("whee!")  # 安全：输出 whee!
```

```
# if-elif-else on color / 基于颜色的多分支
color = input("color? ")
if color == "red":
    print("It's a tomato.")
elif color == "yellow":
    print("It's a banana.")
else:
    print("It's not what I know!")
```

**Flowcharts (ASCII) / 流程图（ASCII）**

```
# if-else (disaster=True)
start
  |
  v
disaster? --True--> print("woe!") --> end
    |
    '--False--> print("whee!") --> end
```

```
# if-else (disaster=False)
start
  |
  v
disaster? --False--> print("whee!") --> end
    |
    '--True--> print("woe!") --> end
```

---

## Loops / 循环

- **for + range(n):** iterate `0..n-1`, great for **regular** iteration.  
**for + range(n)：**遍历 `0..n-1`，适合**规则**重复。

```python
for i in range(5):  # 0,1,2,3,4
    print(i)
```

- **while:** repeat while a **condition** holds; initialize and update **control variables**.  
**while：**在条件满足时反复执行；注意**控制变量**的初始化与更新。

```python
i = 0               # init / 初始化
while i < 5:        # condition / 条件
    print(i)        # body / 循环体
    i += 1          # update / 更新
```

---

## Functions / 函数

- Define with `def name(params): ...`; call by `name(args)`; distinguish **parameters** vs **arguments**.
使用 `def 名称(形参): ...` 定义；用 `名称(实参)` 调用；区分**形参**与**实参**。

```python
import math

def circle_area(r):           # function name & parameter / 函数名与形参
    return math.pi * r * r

for r in [1, 2, 3]:           # repeated calls / 多次调用
    print(r, circle_area(r))
```

---

## Exercises & Prep Tasks / 课后练习与预习任务

- Set up **Python runtime** & **Jupyter** environment.  
**准备 **Python 运行环境** 与 **Jupyter**。

- Practice: input/output, types, operators, conditionals, loops, functions.
练习：输入/输出、类型、运算符、条件、循环、函数。


---

[Next Lecture / 下一讲 →](./lecture02.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

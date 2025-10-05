[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 03 Notes 
# 计算机编程（Python）——第 03 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [If — Selection Patterns / If —— 选择结构](#if--selection-patterns--if--选择结构)
- [Blocks, Indentation, Clause-Header-Suite / 代码块与缩进、子句-头部-语句块](#blocks-indentation-clause-header-suite--代码块与缩进子句-头部-语句块)
- [Comparisons & Logical Operators / 比较与逻辑运算](#comparisons--logical-operators--比较与逻辑运算)
- [Ternary Operator / 三元表达式](#ternary-operator--三元表达式)
- [Truthiness in Python / Python 的真值规则](#truthiness-in-python--python-的真值规则)
- [Membership with `in` / 使用 `in` 进行包含判断](#membership-with-in--使用-in-进行包含判断)
- [Walrus Operator `:=` / 海象运算符 `:=`](#walrus-operator--海象运算符-)
- [For & While Loops / for 与 while 循环](#for--while-loops--for-与-while-循环)
- [range() — Numeric Iterators / range()——数值迭代器](#range--numeric-iterators--range——数值迭代器)
- [break, continue, and loop else / break、continue 与循环的 else](#break-continue-and-loop-else--breakcontinue-与循环的-else)
- [Exercise 3‑1: to_grade(score) / 练习 3‑1：成绩分级](#exercise-3‑1-to_gradescore--练习-3‑1成绩分级)
- [Exercise 3‑2: fizz_buzz(n) / 练习 3‑2：FizzBuzz](#exercise-3‑2-fizz_buzzn--练习-3‑2fizzbuzz)

---

## Today’s Agenda / 今日教学安排

- **if** selection, **for/while** loops.  
**if** 选择结构、**for/while** 循环。

- **Exercises:** 3‑1 **to_grade**, 3‑2 **FizzBuzz**.  
**演习：**3‑1 **to_grade**，3‑2 **FizzBuzz**。

---

## Learning Objectives / 学习目标

- Write correct **if / elif / else** decision logic and understand **nested** vs **sequential** comparisons.  
**掌握**if/elif/else** 的编写方法，理解 **嵌套** 与 **顺序** 比较。

- Understand Python **blocks**, **indentation (4 spaces)**, and the anatomy **clause = header + suite**.  
**理解**Python 的**代码块**、**四空格缩进**与**子句=头部+语句块**结构。

- Use **comparison** and **logical** operators; know **truthiness** rules.  
**会用**比较**与**逻辑**运算符；熟悉**真值**规则。

- Apply **membership tests** (`in`) on strings, sets, lists, tuples, dicts.  
**掌握**`in`** 在 字符串/集合/列表/元组/字典 上的判断。

- Write loops with **for/in, range(), while**, and control flow via **break/continue/else**.  
**能用**for/in、range()、while** 编写循环，并用 **break/continue/else** 控制流程。

---

## If — Selection Patterns / If —— 选择结构

- **Basic if:** run suite only when condition is **True**.  
**基本 if：**条件为 **True** 时执行语句块。

```python
if n < 0:
    n = -n
```

- **if-else:** choose exactly one of two branches.  
**if-else：**在两个分支中二选一。

```python
disaster = True
if disaster:
    print("woe!")
else:
    print("whee!")
```

- **if-elif-else:** multi-way selection (sequential checks).  
**if-elif-else：**多路选择（顺序判断）。

```python
color = input("color? ")
if color == "red":
    print("It's a tomato.")
elif color == "green":
    print("It's a green pepper.")
else:
    print("I don't know.")
```

---

## Blocks, Indentation, Clause-Header-Suite / 代码块与缩进、子句-头部-语句块

- Python uses **indentation** to denote blocks; **recommended: 4 spaces**.  
**Python 用**缩进**表示代码块；**推荐：4 空格**。

- **Clause = Header + Suite**, header ends with `:`, suite is indented.  
**子句 = 头部 + 语句块**；头部以 `:` 结尾，语句块需要缩进。

---

## Comparisons & Logical Operators / 比较与逻辑运算

- Comparison operators: `== != < <= > >=` → result is **True/False**.  
**比较运算：**`== != < <= > >=` → 结果为 **True/False**。

- Boolean operators: `and` / `or` / `not` (**short-circuiting**).  
**逻辑运算：**`and`/`or`/`not`（**短路求值**）。

```python
x = 10
ok = (0 <= x <= 100) and (x % 2 == 0)
```

---

## Ternary Operator / 三元表达式

- Syntax: `A if cond else B`.  
**语法：**`A if cond else B`。

```python
parity = "even" if (x % 2 == 0) else "odd"
```

---

## Truthiness in Python / Python 的真值规则

- **Falsey:** `False`, `0`, `0.0`, empty string/containers (`""`, `[]`, `{}`, `set()`, `dict()`), `None`.  
**假值：**`False`、`0`、`0.0`、空串/空容器（`""`、`[]`、`{}`、`set()`、`dict()`）、`None`。

- Everything else is **truthy**.  
除此之外均为**真值**。

---

## Membership with `in` / 使用 `in` 进行包含判断

- Strings: `"cat" in "concatenate" → True`.  
**字符串：**`"cat" in "concatenate" → True`。

- Containers: support in **set/list/tuple/dict** (dict tests **keys**).  
**容器：**适用于 **集合/列表/元组/字典**（字典测试**键**）。

```python
if "x" in {"x": 1, "y": 2}:  # True — checks keys
    ...
```

---

## Walrus Operator `:=` / 海象运算符 `:=`

- Assign and test in one expression (Python **3.8+**).  
**在表达式中赋值并测试**（Python **3.8+**）。

```python
while (line := input()) != "":
    print(line)
```

---

## For & While Loops / for 与 while 循环

- **for + in** iterates items of an **iterator/iterable**.  
**for + in** 遍历 **迭代器/可迭代对象** 的元素。

```python
for i in range(5):  # 0..4
    print(i)
```

- **while** repeats while condition is **True**.  
**while** 在条件 **True** 时重复执行。

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## range() — Numeric Iterators / range()——数值迭代器

- Form: `range(start, stop, step)`; default `start=0`, `step=1`.  
**格式：**`range(start, stop, step)`；默认 `start=0`、`step=1`。

- `range(10)`, `range(1, 10)`, `range(10, 0, -1)` (descending).  
**示例：**`range(10)`、`range(1, 10)`、`range(10, 0, -1)`（降序）。

---

## break, continue, and loop else / break、continue 与循环的 else

- `break` exits loop early; `continue` skips to next iteration.  
**`break`** 提前退出循环；**`continue`** 跳到下一轮。

- `for`/`while ... else:` runs `else` only if loop **did not** break.  
**循环**的 `else`：仅在循环**没有**通过 `break` 退出时执行。

```python
for x in [2, 4, 6, 9, 10]:
    if x % 2:    # found odd
        print("odd found")
        break
else:
    print("no odd found")  # runs only if no break
```

---

## Exercise 3‑1: to_grade(score) / 练习 3‑1：成绩分级

**Spec / 规范**  
- Input: integer `score` in **[0, 100]** → map to `"A"|"B"|"C"|"F"`.  
**输入：**整数 `score` 在 **[0,100]** → 映射到 `"A"|"B"|"C"|"F"`。  
- **Revised:** out-of-range: `score < 0 → "L"`, `score > 100 → "H"`.  
**修订：**越界时：`score < 0 → "L"`，`score > 100 → "H"`。

**Reference solution (top-down check) / 参考解（自上而下）**

```python
def to_grade(score: int) -> str:
    if score > 100:
        return "H"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 0:
        return "F"
    return "L"
```

**Testbench name / 测试脚本名**：`to_grade.py`。将其与此函数放到同一工程后运行 `pytest -q`。

> [to_grade.py — Code / to_grade.py — 代码](./src/to_grade.py)

---

## Exercise 3‑2: fizz_buzz(n) / 练习 3‑2：FizzBuzz

**Spec / 规范**  
- `n % 15 == 0 → "FizzBuzz"`; `n % 3 == 0 → "Fizz"`; `n % 5 == 0 → "Buzz"`; otherwise return **n**.  
**规则：**`n % 15 == 0 → "FizzBuzz"`；`n % 3 == 0 → "Fizz"`；`n % 5 == 0 → "Buzz"`；否则返回 **n** 本身。

**Reference solution / 参考解**

```python
def fizz_buzz(n: int):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n
```

**Testbench name / 测试脚本名**：`FizzBuzz.py`。运行 `pytest -q` 以检查通过所有 1..30 的期望值。

> [FizzBuzz.py — Code / FizzBuzz.py — 代码](./src/FizzBuzz.py)

<h2></h2>

[← Previous Lecture / 上一讲](./lecture02.md) · [Next Lecture / 下一讲 →](./lecture04.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

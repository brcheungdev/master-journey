[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 07 Notes 
# 计算机编程（Python）——第 07 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Defining and Calling Functions / 函数的定义与调用](#defining-and-calling-functions--函数的定义与调用)
- [Arguments and Return Values / 实参与返回值](#arguments-and-return-values--实参与返回值)
- [Default Arguments — Pitfalls / 缺省参数与常见陷阱](#default-arguments--pitfalls--缺省参数与常见陷阱)
- [Mutable vs Immutable Arguments / 可变与不可变实参](#mutable-vs-immutable-arguments--可变与不可变实参)
- [Inner Functions / 函数内函数](#inner-functions--函数内函数)
- [Generators and `yield` / 生成器与 `yield`](#generators-and-yield--生成器与-yield)
- [Generator Comprehensions / 生成器内包表记](#generator-comprehensions--生成器内包表记)
- [Namespaces and Scope / 命名空间与作用域](#namespaces-and-scope--命名空间与作用域)
- [Exceptions and Error Handling / 异常与错误处理](#exceptions-and-error-handling--异常与错误处理)
- [Recursion Basics / 递归基础](#recursion-basics--递归基础)
- [Exercises 7‑1/7‑2/7‑3 — Polygonal Numbers by Recursion / 演习 7‑1/7‑2/7‑3——用递归求多角数](#exercises-7‑17‑27‑3--polygonal-numbers-by-recursion--演习-7‑17‑27‑3——用递归求多角数)
- [Appendix — Quick Reference / 附录——速查](#appendix--quick-reference--附录速查)

---

## Today’s Agenda / 今日教学安排

- Functions → arguments/return → inner functions → generators → namespaces/scope → recursion → exceptions.  
函数 → 实参与返回值 → 函数内函数 → 生成器 → 命名空间与作用域 → 递归 → 异常。

- **Exercises:** Triangular/Square/Pentagonal/General polygonal numbers via **recursion**.  
**演习：**使用**递归**实现三角数/四角数/五角数/一般多角数。

---

## Learning Objectives / 学习目标

- Define functions with `def`, write docstrings, and call them correctly.  
**掌握**用 `def` 定义函数、编写文档字符串并正确调用。

- Use **positional/keyword arguments**, defaults, and return values safely.  
**正确使用****位置/关键字参数**、默认值与返回值。

- Build **generators** with `yield` and understand lazy iteration.  
**能用 `yield`** 构建**生成器**，理解惰性迭代。

- Reason about **namespaces/scope** (`locals()`, `globals()`, `global`) and immutability.  
**理解****命名空间/作用域**（`locals()`、`globals()`、`global`）与不可变性。

- Implement and test **recursive** solutions; handle **exceptions** with `try/except/else/finally`.  
**实现并测试****递归**解法；使用 `try/except/else/finally` 处理**异常**。

---

## Defining and Calling Functions / 函数的定义与调用

- The simplest function uses `def name(): ...` and may `pass`.  
**最简单的函数**使用 `def 名称(): ...`，可用 `pass` 作为占位。

```python
def do_nothing():
    """Example minimal function."""
    pass
do_nothing()  # call requires parentheses even with no args
```
**注：**即使无参数，调用时也需加 `()`。

- Return values are provided by **`return`**; if omitted, the function returns **`None`**.  
**返回值**由 **`return`** 指定；若省略，函数返回 **`None`**。

- Functions can have **docstrings**; use `help(func)` or `func.__doc__` to view them.  
函数可带**文档字符串**；用 `help(func)` 或 `func.__doc__` 查看。

---

## Arguments and Return Values / 实参与返回值

- **Argument vs Parameter:** values passed in are **arguments**; function’s named receivers are **parameters**.  
**实参与形参：**传入的值为**实参**；函数定义中的命名接收者为**形参**。

- **Positional arguments** map by order; **keyword arguments** map by name.  
**位置实参**按顺序匹配；**关键字实参**按名称匹配。

- **Return** ends execution immediately and hands a value back to caller.  
**`return`** 立即结束执行并把值返回给调用者。

---

## Default Arguments — Pitfalls / 缺省参数与常见陷阱

- Default values are **evaluated once at function definition time**.  
**默认值**在**定义时**求值一次。

```python
def append_item(x, result=[]):   # DANGEROUS
    result.append(x)             # keeps growing across calls
    return result
```
**问题：**可变默认值会**跨调用共享**。

- Prefer `None` sentinel and create a new object inside.  
**建议：**用 `None` 作为哨兵，在函数体内新建对象。

```python
def append_item(x, result=None):
    if result is None:
        result = []
    result.append(x)
    return result
```

---

## Mutable vs Immutable Arguments / 可变与不可变实参

- **Immutable types** (`int`, `str`, `tuple`) create **new objects** on “change”.  
**不可变类型**（`int`、`str`、`tuple`）在“修改”时**创建新对象**。

- **Mutable types** (`list`, `dict`, `set`) can be modified **in place**.  
**可变类型**（`list`、`dict`、`set`）可**原地修改**。

- Always be clear whether your function **mutates** arguments or returns **new** data.  
务必明确函数是**就地修改**参数还是**返回新对象**。

---

## Inner Functions / 函数内函数

- Functions can be defined **inside** other functions to encapsulate logic.  
函数可在**另一个函数内部**定义以封装逻辑。

```python
def outer(x):
    def square(y): return y*y
    return square(x) + square(x+1)
```

---

## Generators and `yield` / 生成器与 `yield`

- A **generator** produces a sequence lazily; use **`yield`** to emit next values.  
**生成器**以惰性方式产生序列；使用 **`yield`** 逐个产出值。

```python
def ranger(start, stop, step=1):
    cur = start
    while cur < stop:
        yield cur
        cur += step
```
**要点：**生成器**记住进度**；第二次遍历已**耗尽**的生成器将不会产生任何输出。

---

## Generator Comprehensions / 生成器内包表记

- Syntax: `(expr for x in iterable if cond)`.  
**语法：**`(expr for x in iterable if cond)`。

- Use when you only **iterate once** and want to save memory vs list comprehension.  
当只**迭代一次**且希望节省内存时优先于列表推导。

---

## Namespaces and Scope / 命名空间与作用域

- Each function has its **local namespace**; the main program has a **global namespace**.  
每个函数都有**局部命名空间**；主程序有**全局命名空间**。

- Use `global name` to **assign** to a global variable within a function.  
在函数内对全局变量**赋值**需 `global 名称`。

- Inspect with `locals()` and `globals()`; reserved names often have `__double_underscores__`.  
用 `locals()` 与 `globals()` 检查；保留名常采用 `__双下划线__`。

---

## Exceptions and Error Handling / 异常与错误处理

- Wrap risky code with `try/except`; optionally add `else` (runs if no exception) and `finally` (always runs).  
把可能出错的代码置于 `try/except` 中；可选 `else`（无异常时运行）与 `finally`（总会运行）。

```python
try:
    x = int(s)
except ValueError:
    x = 0
else:
    print("parsed ok")
finally:
    print("cleanup")
```

---

## Recursion Basics / 递归基础

- A **recursive function** has a **base case** and a **recursive step**.  
**递归函数**包含**基例**与**递归步**。

- Examples: **factorial**, **Fibonacci**, **triangular numbers**.  
示例：**阶乘**、**斐波那契**、**三角数**。

- Design tips: ensure progress toward base case; beware of stack depth; consider memoization if overlapping subproblems.  
设计提示：确保朝基例推进；注意栈深限制；若存在重叠子问题可考虑**记忆化**。

---

## Exercises 7‑1/7‑2/7‑3 — Polygonal Numbers by Recursion / 演习 7‑1/7‑2/7‑3——用递归求多角数

> **Goal:** Implement **triangular** `P3(n)`, **square** `P4(n)`, **pentagonal** `P5(n)`, and **general polygonal** `P(p, n)` using **recursion**; verify with provided testbenches.  
> **目标：**用**递归**实现 **三角数** `P3(n)`、**四角数** `P4(n)`、**五角数** `P5(n)` 以及**一般多角数** `P(p, n)`；并用测试脚本验证。

**Triangular numbers / 三角数**  
- Closed form: `P3(n) = n(n+1)/2`; recursive idea: `P3(0)=0`, `P3(n)=P3(n-1)+n`.  
**闭式：**`P3(n) = n(n+1)/2`；**递归：**`P3(0)=0`，`P3(n)=P3(n-1)+n`。

```python
def P3(n: int) -> int:
    return 0 if n == 0 else P3(n-1) + n
```

**Square numbers / 四角数**  
- Closed form: `P4(n) = n^2`; recursive idea: `P4(0)=0`, `P4(n)=P4(n-1)+2n-1`.  
**闭式：**`P4(n) = n^2`；**递归：**`P4(0)=0`，`P4(n)=P4(n-1)+2n-1`。

```python
def P4(n: int) -> int:
    return 0 if n == 0 else P4(n-1) + 2*n - 1
```

**Pentagonal numbers / 五角数**  
- Closed form: `P5(n) = n(3n−1)/2`; recursive idea: `P5(0)=0`, `P5(n)=P5(n-1)+3n-2`.  
**闭式：**`P5(n) = n(3n−1)/2`；**递归：**`P5(0)=0`，`P5(n)=P5(n-1)+3n-2`。

```python
def P5(n: int) -> int:
    return 0 if n == 0 else P5(n-1) + 3*n - 2
```

**General polygonal numbers / 一般多角数**  
- General formula: `P(p,n) = ((p−2)n^2 − (p−4)n)/2`.  
**一般公式：**`P(p,n) = ((p−2)n^2 − (p−4)n)/2`。

- Recursive relation (one valid form): `P(p,0)=0`, `P(p,n)=P(p,n−1) + (p−2)n − (p−4)` .  
**一种可用的递推：**`P(p,0)=0`，`P(p,n)=P(p,n−1) + (p−2)n − (p−4)`。

```python
def P(p: int, n: int) -> int:
    if n == 0:
        return 0
    return P(p, n-1) + (p-2)*n - (p-4)
```

**Testing / 测试**  
- Use provided testbenches `P3.py`, `P4.py`, `P5.py`, `PP.py`.  
**使用提供的测试脚本**`P3.py`、`P4.py`、`P5.py`、`PP.py`。

> [P3.py — Code / P3.py — 代码](./src/P3.py)
> 
> [P4.py — Code / P4.py — 代码](./src/P4.py)
> 
> [P5.py — Code / P5.py — 代码](./src/P5.py)
> 
> [PP.py — Code / PP.py — 代码](./src/PP.py)

---

## Appendix — Quick Reference / 附录——速查

- **Function**: `def`, docstring, `return`, positional/keyword args, defaults, `*args`, `**kwargs`.  
**函数：**`def`、文档字符串、`return`、位置/关键字参数、默认值、`*args`、`**kwargs`。

- **Generator**: `yield`, one‑shot iteration, generator comprehension.  
**生成器：**`yield`、一次性迭代、生成器内包。

- **Namespace**: `locals()`, `globals()`, `global` keyword, `__name__`, `__doc__`.  
**命名空间：**`locals()`、`globals()`、`global`、`__name__`、`__doc__`。

- **Exceptions**: `try/except/else/finally`, specific exceptions (`ValueError`, etc.).  
**异常：**`try/except/else/finally`，特定异常（如 `ValueError`）。

- **Recursion**: base case + recursive step, ensure progress.  
**递归：**基例 + 递归步，确保推进到基例。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture06.md) · [Next Lecture / 下一讲 →](./lecture08.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

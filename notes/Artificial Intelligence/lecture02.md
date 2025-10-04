[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 02 / 人工知能ソフトウェア活用Ⅰ — 第2讲
**Topic:** Python Basics (Variables → Operators → Data Structures → Control Flow → Functions → Modules & Libraries)  
**主题：** Python 基础（变量 → 运算符 → 数据结构 → 控制流 → 函数 → 模块与库）

---

## Table of Contents / 目录
- [Today’s Content / 今日内容](#todays-content--今日内容)
- [Variables / 变量](#variables--变量)
- [Variable Types / 变量的类型](#variable-types--变量的类型)
- [Variable Names / 变量命名](#variable-names--变量命名)
- [Reserved Words / 保留关键字](#reserved-words--保留关键字)
- [Operators / 运算符](#operators--运算符)
- [Data Structures / 数据结构](#data-structures--数据结构)
- [Control Flow / 控制流](#control-flow--控制流)
- [Functions / 函数](#functions--函数)
- [Modules & Libraries / 模块与库](#modules--libraries--模块与库)
- [Practice Set / 练习题](#practice-set--练习题)

---

## Today’s Content / 今日内容
- **Python basics** (for those who already studied Python, treat it as a review).  
**Python 基础**（已学过者可作为复习）。
- **Variables, Operators, Data Structures, Control Flow, Functions, Modules/Libraries.**  
**变量、运算符、数据结构、控制流、函数、模块/库。**

---

## Variables / 变量
- **A variable is a container (a “box”) that stores a value.**  
**变量是装载数值的“容器/盒子”。**
- **Defining a variable means “putting a value into the box”.**  
**定义变量即“把值放进盒子”。**
- **Use `print()` to inspect the value of a variable.**  
**使用 `print()` 查看变量当前的值。**

```python
x = 5
print(x)       # 5
```
**示例：** 将 `5` 赋给 `x` 并打印。

---

## Variable Types / 变量的类型
- **Integers, floats, strings, booleans, etc.**  
**整数、浮点数、字符串、布尔等。**
- **Use `type()` to check the type of a value.**  
**使用 `type()` 检查值的类型。**

```python
n = 42
type(n)        # <class 'int'>
```
**示例：** `n` 的类型是整数。

<details><summary>Common literals / 常见字面量</summary>

- **Integers:** `0`, `-3`, `7`  
**整数：** `0`、`-3`、`7`
- **Floats:** `3.14`, `1e-3`  
**浮点：** `3.14`、`1e-3`
- **Strings:** `'abc'`, `"abc"`  
**字符串：** `'abc'`、`"abc"`
- **Booleans:** `True`, `False`  
**布尔：** `True`、`False`

</details>

---

## Variable Names / 变量命名
- **Almost anything is allowed, but follow rules & exceptions.**  
**几乎任意命名，但需遵循规则与例外。**
- **Allowed characters:** `a–z`, `A–Z`, `0–9`, underscore `_`.  
**可用字符：** 字母、数字、下划线。**
- **First character cannot be a digit.**  
**首字符不能为数字。**
- **Leading underscore has special conventions—avoid for general use.**  
**前导下划线常用于特殊约定—一般不建议使用。**
- **Case sensitive (`score` ≠ `Score`).**  
**大小写敏感（`score` 与 `Score` 不同）。**
- **Do not use reserved words.**  
**不要使用保留关键字。**

```python
valid_name = 1     # OK
# 1st = 2         # ❌ 不能以数字开头
# class = 3       # ❌ 关键字，禁止
```
**示例：** 合法与非法命名对比。

<details><summary>Style tips (PEP 8) / 风格建议（PEP 8）</summary>

- **Variables & functions:** `snake_case` (e.g., `user_count`).  
**变量/函数：** 下划线风格（如 `user_count`）。
- **Constants:** `UPPER_SNAKE_CASE`.  
**常量：** 全大写下划线（如 `MAX_LEN`）。
- **Classes:** `CapWords` (e.g., `LinearModel`).  
**类名：** 首字母大写驼峰（如 `LinearModel`）。

</details>

---

## Reserved Words / 保留关键字
- **Examples:** `False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`.  
**示例：** `False, None, True, and, as, assert, async, await, break, class, ...` 等。

```python
import keyword
keyword.iskeyword("class")  # True
```
**示例：** 检查某字符串是否为关键字。

---

## Operators / 运算符
- **Used for arithmetic, assignment, comparison, logic, bitwise ops, and strings.**  
**用于代数、赋值、比较、逻辑、位运算与字符串操作。**

### Arithmetic / 代数运算子
- `+`, `-`, `*`, `/` (true division), `**` (power), `//` (floor division), `%` (modulo).  
**`+`、`-`、`*`、`/`（实除）、`**`（幂）、`//`（地板除）、`%`（取余）。**

```python
7 // 2   # 3
7 % 2    # 1
2 ** 10  # 1024
```
**示例：** 地板除、取余与幂。

### Assignment / 赋值运算子
- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` 等。  
**`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` 等。**

```python
x = 5
x += 5   # x = 10
```

### Comparison / 比较运算子
- `==`, `!=`, `>`, `<`, `>=`, `<=`.  
**`==`、`!=`、`>`、`<`、`>=`、`<=`。**

```python
y = 6
y == 5   # False
y > 5    # True
```

### Logical / 逻辑运算子
- `and`, `or`, `not` (short-circuit evaluation).  
**`and`、`or`、`not`（短路求值）。**

```python
def f(): print("called"); return True
False and f()   # 不会调用 f()
True  or  f()   # 不会调用 f()
```

### Bitwise / 位运算（补充）
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<`, `>>`.  
**`&` 与、`|` 或、`^` 异或、`~` 取反、`<<` 左移、`>>` 右移。**

### String ops / 字符串运算
- `+` (concatenate), `*` (repeat).  
**`+`（拼接）、`*`（重复）。**

```python
"AI" + "Pro"   # "AIPro"
"na" * 3       # "nanana"
```

<details><summary>Identity vs Equality / 身份与相等（补充）</summary>

- `==` compares **values**; `is` compares **object identity**.  
**`==` 比值；`is` 比对象身份。**
```python
a = [1,2]; b = [1,2]
a == b   # True
a is b   # False
```
</details>

---

## Data Structures / 数据结构
- **Manage multiple items in one variable: retrieve, add, delete, modify.**  
**用一个变量管理多条数据：取出、添加、删除、修改。**
- **List, Tuple, Dict, Set.**  
**列表、元组、字典、集合。**

### List / 列表
- **Ordered, mutable;** square brackets `[]`; zero-based index.  
**有序且可变；用方括号 `[]`；从 0 开始计数。**

```python
nums = [10, 20, 30]
nums.append(40)     # 增
nums[1] = 21        # 改
del nums[0]         # 删
len(nums)           # 查
```
**示例：** 增改删查。

- **Slicing:** `a[start:stop:step]` (stop **excluded**).  
**切片：** `a[起:止:步]`（**止位不包含**）。
```python
a = [0,1,2,3,4,5]
a[0:3]    # [0,1,2]
a[::2]    # [0,2,4]
```

<details><summary>Copy vs Reference / 复制与引用（补充）</summary>

```python
a = [1,2]; b = a
b[0] = 9
print(a)  # [9,2]  指向同一对象

c = a[:]          # 浅拷贝
import copy; d = copy.deepcopy(a)  # 深拷贝
```
**列表是可变对象；赋值会共享引用。**

</details>

### Tuple / 元组
- **Ordered, immutable;** parentheses `()`.  
**有序且不可变；用圆括号 `()`。**
```python
pt = (12.5, 7.3)
pt[0]      # 12.5
# pt[0]=1  # ❌ 不可修改
```
- **Common use:** group strongly related values; safe as dict keys.  
**常用：打包强相关数据；可作字典键。**

### Dict / 字典
- **Key–Value mapping;** braces `{}`, colon `:` between key & value.  
**键值映射；花括号 `{}`，键值用冒号连接。**
```python
user = {"id": 1, "name": "Roi"}
user["name"] = "Boru"      # 改
user["email"] = "x@y.com"  # 增
"user" in locals()         # 查是否存在变量名
```
- **Iteration:** `for k, v in dict.items()`.  
**遍历：** `for k, v in dict.items()`。

### Set / 集合
- **Unordered, unique elements;** braces `{}`.  
**无序且元素唯一；用花括号 `{}`。**
```python
s = {1,2,2,3}   # {1,2,3}
s.add(4); s.remove(1)
s2 = {3,4,5}
s & s2   # 交集 {3,4}
s | s2   # 并集 {1,2,3,4,5}
s - s2   # 差集 {2}
```
**集合不保留重复项；常用于去重与集合代数。**

<details><summary>Mutability table / 可变性速查</summary>

```
List: mutable / 可变
Tuple: immutable / 不可变
Dict: mutable / 可变
Set: mutable / 可变（元素需可哈希）
```
</details>

---

## Control Flow / 控制流
- **Controls execution order: sequential, conditional, loops.**  
**控制执行顺序：顺序、分支、循环。**

### if / elif / else
- **End condition with `:`; block indented by 4 spaces (PEP 8).**  
**条件末尾加 `:`；代码块缩进 4 空格（PEP 8）。**
```python
score = 78
if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
```

### for loop / for 循环
- **Iterate over an iterable (list/tuple/dict/set/range/string, etc.).**  
**遍历可迭代对象（列表/元组/字典/集合/range/字符串等）。**
```python
names = ["Sato","Suzuki","Takahashi"]
for n in names:
    print(f"{n}さん、3番窓口へお越しください")
```

- **`range(start, stop, step)` generates an arithmetic progression.**  
**`range(起,止,步)` 生成等差数列（止位不含）。**
```python
for i in range(0, 10, 2):  # 0,2,4,6,8
    pass
```

<details><summary>Enumerate & Zip / 枚举与打包（补充）</summary>

```python
for i, n in enumerate(names, start=1):
    print(i, n)

xs, ys = [1,2,3], [10,20,30]
for x, y in zip(xs, ys):
    print(x, y)
```
**`enumerate` 提供索引；`zip` 同步遍历多序列。**
</details>

### while loop / while 循环
- **Loop without preset count; stop by condition.**  
**不预设次数；用条件停止。**
```python
i = 0
while i < 3:
    print(i)
    i += 1
```
- **Always ensure a stopping condition to avoid infinite loops.**  
**务必设置终止条件以避免死循环。**

<details><summary>`for`/`while` … `else` / 循环后的 `else`（补充）</summary>

```python
for x in [1,2,3]:
    if x == 2:
        break
else:
    print("no break happened")   # 仅当未触发 break 才执行
```
**循环的 `else` 子句仅在循环**正常结束**时执行（未 `break`）。**
</details>

---

## Functions / 函数
- **A “machine” that takes inputs, performs operations, returns outputs.**  
**函数像“机器”：接收输入，执行操作，返回输出。**

### Built‑ins / 内置函数
- **Examples:** `print()`, `int()`, `len()`, `sum()`, `sorted()`.  
**示例：** `print()`、`int()`、`len()`、`sum()`、`sorted()`。

```python
vals = [3,1,2]
sorted(vals)        # [1,2,3]
```

### Return values / 返回值
- **Capture outputs to variables to verify results.**  
**将返回值赋给变量以便验证。**
```python
s = int("42")       # 返回整数 42
```

### User‑defined / 自定义函数
- **Use `def` to define; parameters → body → `return`.**  
**用 `def` 定义；形参 → 函数体 → `return`。**
```python
def add5(x):
    """Return x + 5 / 返回 x+5"""
    return x + 5
```

<details><summary>Parameters & scopes / 形参与作用域（补充）</summary>

- **Default args:** `def f(x, k=3): ...`  
**默认参数：** `def f(x, k=3): ...`
- **Keyword args:** `f(x=10, k=2)`  
**关键字参数：** `f(x=10, k=2)`
- **\*args / \*\*kwargs:** variable parameters.  
**可变参数：** `*args` / `**kwargs`
- **Scope:** LEGB (Local → Enclosing → Global → Builtins).  
**作用域链：** LEGB（局部→嵌套→全局→内建）。

</details>

---

## Modules & Libraries / 模块与库
- **Module:** a reusable piece of code (functions, classes…).  
**模块：可复用的代码单元（函数、类等）。**
- **Library / Package:** a collection of modules (often many files).  
**库/包：多个模块的集合（通常为多文件）。**
- **Motivation:** when code grows to hundreds of lines and is reused.  
**动机：当代码增至数百行并多处复用时应模块化。**

```python
# mymath.py
def add(a,b): return a+b

# main.py
import mymath
print(mymath.add(1,2))
```
**示例：** 自建模块并导入使用。

<details><summary>Import patterns / 导入范式（补充）</summary>

```python
import numpy as np               # 别名导入
from math import sqrt, pi        # 选择性导入
from collections import defaultdict as DD  # 改名导入
```
**根据上下文选择合适的导入方式，注意命名冲突与可读性。**
</details>

---

## Practice Set / 练习题
1. **Variables & Types:** create 3 variables (`int`, `float`, `str`) and print their `type`.  
**变量与类型：** 创建 3 个不同类型变量并打印 `type`。
2. **Operators:** compute `((7 // 2) ** 3) % 5` and explain each step.  
**运算符：** 计算 `((7 // 2) ** 3) % 5` 并逐步解释。
3. **List & Slice:** build a list `[0..9]`, get evens by slicing.  
**列表与切片：** 构造 `[0..9]`，用切片取偶数。
4. **Dict:** make a dict for a student (`id`, `name`, `score`) and update `score`.  
**字典：** 建一个学生字典并更新分数。
5. **Set:** deduplicate `[1,2,2,3,3,3]` and take intersection with `{2,4}`.  
**集合：** 去重并与 `{2,4}` 求交集。
6. **Control flow:** write a grader function → return `A/B/C/F`.  
**控制流：** 写评分函数返回 `A/B/C/F`。
7. **Function:** write `pow_plus(x, n)` returning `x**n + x`.  
**函数：** 写 `pow_plus(x, n)` 返回 `x**n + x`。
8. **Module:** split your grader into `grader.py`, import & test.  
**模块：** 将评分逻辑拆到 `grader.py` 中导入测试。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture01.md) · [Next Lecture / 下一讲 →](./lecture03.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

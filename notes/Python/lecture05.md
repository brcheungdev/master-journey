[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 05 Notes 
# / 计算机编程（Python）——第 05 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Containers Overview / 容器概览](#containers-overview--容器概览)
- [Lists — Part 1 / 列表（第一部分）](#lists--part-1--列表第一部分)
- [Tuples / 元组](#tuples--元组)
- [Lists vs Tuples / 列表与元组对比](#lists-vs-tuples--列表与元组对比)
- [Lists — Part 2 / 列表（第二部分）](#lists--part-2--列表第二部分)
- [List Comprehensions / 列表内包表记](#list-comprehensions--列表内包表记)
- [Exercises / 演习](#exercises--演习)
- [Appendix — Quick Reference / 附录——速查](#appendix--quick-reference--附录速查)

---

## Today’s Agenda / 今日教学安排

- Lists & Tuples — creation, access, mutation, slicing, search, comparison; assignment & copies; iteration; `zip()`; list-of-lists; comprehensions.  
列表与元组——创建、访问、修改、切片、搜索、比较；赋值与拷贝；迭代；`zip()`；列表的列表；列表内包。

- **Exercises:** Square numbers, pentagonal numbers, generalized polygonal numbers.  
**演习：**四角数、五角数、多角数一般化。

---

## Learning Objectives / 学习目标

- Understand Python **containers** and the differences between **mutable** and **immutable** ones.  
**理解 Python 的**容器**及其**可变/不可变**差异。

- Create and manipulate **lists**: build, index, slice, append/insert/extend, replace, delete, search, compare.  
**掌握对**列表**的操作：构建、索引、切片、追加/插入/扩展、替换、删除、搜索、比较。

- Create and use **tuples**: literal forms, singleton tuple, unpacking, swapping, iteration, comparison.  
**掌握**元组**：字面量、单元素元组、拆包、交换、迭代、比较。

- Know **assignment vs copy**, shallow vs deep copy, and their effects on nested containers.  
**理解**赋值与拷贝**、浅拷贝与深拷贝**，及其对嵌套容器的影响。

- Use **`zip()`** for parallel iteration and building lists/dicts; master **list comprehensions**.  
**会用**`zip()`**进行并行迭代与构建列表/字典；掌握**列表内包**。

---

## Containers Overview / 容器概览

- **Definition:** container holds **collections of objects**; umbrella for ADTs/classes like list, tuple, dict, set.  
**定义：**容器存放**对象的集合**；是列表、元组、字典、集合等抽象数据类型/类的总称。

- **Kinds in Python:** **list**, **tuple**, **dict**, **set**.  
**Python 中的类型：** **list（列表）**、**tuple（元组）**、**dict（字典）**、**set（集合）**。

- **Access modes:** list by **offset**; dict by **key**; set tests **membership** only.  
**访问方式：**列表按**偏移量**；字典按**键**；集合只支持**成员性**测试。

- **Mutability:** list/dict/set are **mutable**; tuple is **immutable**.  
**可变性：**列表/字典/集合为**可变**；元组为**不可变**。

---

## Lists — Part 1 / 列表（第一部分）

**Creation / 创建**  
- `[]` or `list()`; heterogeneous elements allowed; duplicates allowed.  
**`[]` 或 `list()`；元素可异构；允许重复。

- Single-element list: brackets with **no trailing comma**.  
**单元素列表：**方括号内单个元素，**无需**末尾逗号。

- Convert via `list("abc") -> ['a','b','c']`, `list((1,2)) -> [1,2]`; `"a b c".split() -> ['a','b','c']`.  
**转换：**`list("abc") -> ['a','b','c']`，`list((1,2)) -> [1,2]`；`"a b c".split() -> ['a','b','c']`。

**Access / 访问**  
- Indexing: `lst[i]`, negative from end; slicing: `lst[a:b:c]`.  
**索引：**`lst[i]`，负索引从尾部；**切片：**`lst[a:b:c]`。

- Slices outside range **don’t raise**; they **clip** or return `[]`.  
**越界切片**不会报错；会**裁剪**或返回 `[]`。

**Append & Insert / 追加与插入**  
- `append(x)` adds at end; `insert(i,x)` adds at offset (no exception on large i).  
**`append(x)`** 末尾追加；**`insert(i,x)`** 指定位置插入（过大索引也不报错）。

**Extend & Concatenate / 扩展与连接**  
- `extend(iterable)`; `+= iterable`.  
**扩展：**`extend(iterable)`；或用 `+= iterable`。

**Replace & Delete / 替换与删除**  
- Offset: `lst[i] = x`; Slice: `lst[a:b] = iterable` (iterable **unpacks**).  
**按位替换：**`lst[i] = x`；**切片替换：**`lst[a:b] = iterable`（会**拆成元素**）。

- `del lst[i]`, `remove(x)`, `pop([i])`.  
**删除相关：**`del lst[i]`、`remove(x)`、`pop([i])`。

**Search, Count, Compare / 搜索、计数、比较**  
- `x in lst`, `lst.index(x)`, `lst.count(x)`; lists compare **lexicographically**.  
**成员/索引/计数/比较：**`x in lst`、`lst.index(x)`、`lst.count(x)`；列表按**字典序**比较。

---

## Tuples / 元组

**Creation / 创建**  
- `()` or `tuple()`; single-element tuple requires **trailing comma** `(x,)`.  
**`()` 或 `tuple()`；单元素元组需在元素后加**逗号** `(x,)`。

- Parentheses help readability and disambiguation in expressions & arguments.  
**加括号**有助于在表达式/实参中避免歧义并提升可读性。

**Unpacking & Swap / 拆包与交换**  
- `a, b = (1, 2)`; `x, y = y, x`.  
**`a, b = (1, 2)`；`x, y = y, x`。

**Concatenate, Repeat, Iterate, Compare / 连接、重复、迭代、比较**  
- `t1 + t2`, `t * k`, `for x in t`, lexicographic comparison.  
**`t1 + t2`、`t * k`、`for x in t`、按字典序比较。

**Immutability & Hashability / 不可变与可哈希**  
- Elements fixed; tuples (if elements hashable) can be **dict keys**.  
**元素不可改；**若元素可哈希，元组可作**字典键**。

---

## Lists vs Tuples / 列表与元组对比

- List **mutable**; Tuple **immutable**.  
**列表**可变；**元组**不可变。

- Tuple often uses **less memory**; safer from accidental edits.  
**元组**更省内存；更不易被误改。

- Tuple usable as **dict key**; consider `collections.namedtuple` for record-like data.  
**元组**可作**字典键**；记录型数据可用 `collections.namedtuple`。

---

## Lists — Part 2 / 列表（第二部分）

**Assignment vs Copy / 赋值与拷贝**  
- Alias via `b = a`; shallow copy via `a.copy()`, `list(a)`, `a[:]`; deep copy via `copy.deepcopy(a)`.  
**赋值为别名** `b = a`；**浅拷贝** `a.copy()`、`list(a)`、`a[:]`；**深拷贝** `copy.deepcopy(a)`。

**Sorting / 排序**  
- `sorted(a)` returns a new list; `a.sort()` sorts in place; use `reverse=True` for descending.  
**`sorted(a)`** 返回新列表；**`a.sort()`** 原地排序；降序用 `reverse=True`。

**Length & Iteration / 长度与迭代**  
- `len(a)`; `for x in a:`; parallel iteration with `zip()`.  
**`len(a)`；`for x in a:`；并行迭代用 `zip()`。

**List of Lists / 列表的列表**  
- Beware `[[0]*n]*m` aliasing; prefer `[ [0]*n for _ in range(m) ]`.  
**注意**`[[0]*n]*m` 的别名问题；推荐 `[ [0]*n for _ in range(m) ]`。

---

## List Comprehensions / 列表内包表记

- Basic: `[expr for x in xs]`; Conditional: `[expr for x in xs if cond(x)]`; Nested: `[f(i,j) for i in I for j in J]`.  
**基础：**`[expr for x in xs]`；**条件：**`[expr for x in xs if cond(x)]`；**嵌套：**`[f(i,j) for i in I for j in J]`。

- Example — squares & pentagonals:  
**示例——平方数与五角数：**
```python
squares = [n*n for n in range(1, 11)]
pentagonals = [n*(3*n-1)//2 for n in range(1, 11)]
```

---

## Exercises / 演习

- **EX 5‑1** Square numbers — generate first N squares.  
**EX 5‑1** 四角数——生成前 N 个平方数。

- **EX 5‑2** Pentagonal numbers — `P(n) = n(3n-1)/2`.  
**EX 5‑2** 五角数——`P(n) = n(3n-1)/2`。

- **EX 5‑3** General polygonal numbers — `P_k(n) = ((k-2)n^2 - (k-4)n)/2`.  
**EX 5‑3** 一般多角数——`P_k(n) = ((k-2)n^2 - (k-4)n)/2`。

---

## Appendix — Quick Reference / 附录——速查

- **Common list methods:** `append, insert, extend, pop, remove, clear, index, count, sort, reverse, copy`.  
**常见列表方法：**`append、insert、extend、pop、remove、clear、index、count、sort、reverse、copy`。

- **Built-ins:** `len, sorted, zip, list, tuple, dict, set`.  
**常用内置：**`len、sorted、zip、list、tuple、dict、set`。

- **Copy semantics:** assignment → alias; `copy()/list()/[:]` → shallow; `deepcopy()` → deep.  
**拷贝语义：**赋值→别名；`copy()/list()/[:]`→浅拷贝；`deepcopy()`→深拷贝。

<h2> </h2>

[← Previous Lecture / 上一讲](./lecture04.md) · [Next Lecture / 下一讲 →](./lecture06.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

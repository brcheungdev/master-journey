[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 06 Notes 
# 计算机编程（Python）——第 06 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Dictionaries — Concepts & Basics / 字典——概念与基础](#dictionaries--concepts--basics--字典概念与基础)
- [Build & Convert Dictionaries / 字典的创建与转换](#build--convert-dictionaries--字典的创建与转换)
- [Add, Update, Retrieve / 添加、更新与取值](#add-update-retrieve--添加更新与取值)
- [Membership, Views, Length / 成员测试、视图与长度](#membership-views-length--成员测试视图与长度)
- [Merge & Combine / 合并与组合](#merge--combine--合并与组合)
- [Delete & Pop & Clear / 删除、弹出与清空](#delete--pop--clear--删除弹出与清空)
- [Assignment vs Copy / 赋值与拷贝（浅/深）](#assignment-vs-copy--赋值与拷贝浅深)
- [Iterating over Dictionaries / 遍历字典](#iterating-over-dictionaries--遍历字典)
- [Sets — Concepts & Basics / 集合——概念与基础](#sets--concepts--basics--集合概念与基础)
- [Build & Convert Sets / 集合的创建与转换](#build--convert-sets--集合的创建与转换)
- [Modify & Query Sets / 集合的修改与查询](#modify--query-sets--集合的修改与查询)
- [Set Algebra / 集合代数运算](#set-algebra--集合代数运算)
- [Set Relations & Tests / 集合关系与判定](#set-relations--tests--集合关系与判定)
- [Set Comprehensions & frozenset / 集合内包与不可变集合](#set-comprehensions--frozenset--集合内包与不可变集合)
- [Larger Data Structures / 更大的数据结构组合](#larger-data-structures--更大的数据结构组合)
- [Exercises 6‑1/6‑2/6‑3: 2‑D Array Display / 演习 6‑1/6‑2/6‑3：二维数组显示](#exercises-6‑16‑26‑3-2‑d-array-display--演习-6‑16‑26‑3二维数组显示)

---

## Today’s Agenda / 今日教学安排

- **Lecture:** **Dictionaries** and **Sets**; then review solutions from last time; finally the **2‑D array display** exercises.  
**讲授：**学习 **字典**与**集合**；回顾上次演习的参考解；最后进行**二维数组显示**系列演习。

- **Exercises:** **Exercise 6‑1**, **6‑2**, **6‑3** (progressive 2‑D printing).  
**演习：****演习 6‑1**、**6‑2**、**6‑3**（逐步加强的二维打印）。

---

## Learning Objectives / 学习目标

- Understand **key–value** storage, mutability, and access patterns in **dict**.  
**理解**字典的**键–值**存储、可变性与访问方式。

- Create, convert, update, merge, and safely retrieve items in a dict.  
**掌握**字典的创建、转换、更新、合并与安全取值方法。

- Master **set** basics, membership tests, **set algebra** (∩ ∪ − ⊕), and relations (⊆ ⊂ ⊇ ⊃).  
**掌握**集合基础、成员测试、**集合代数**（交并差对称差）与集合关系（子集/真子集/上位集/真上位集）。

- Design readable printers for **2‑D arrays** (lists of lists), including **framed** and **inner‑frame** layouts.  
**能设计**二维数组**（列表的列表）**的打印器，包括**带外框**与**仅内框**布局。

---

## Dictionaries — Concepts & Basics / 字典——概念与基础

- A **dictionary** stores elements as **(key, value)** pairs; lookups use **keys**.  
**字典**以**（键，值）**对存储；访问基于**键**。

- **Unordered**: insertion order is preserved in modern Python, but conceptually order **doesn’t matter** for lookups.  
**无序：**现代 Python 保留插入顺序，但从概念上讲顺序与查找**无关**。

- **Keys must be immutable** (hashable), but the **dict itself is mutable**.  
**键必须不可变**（可哈希），但**字典本身可变**。

- Type name: **`dict`**.  
类型名：**`dict`**。

---

## Build & Convert Dictionaries / 字典的创建与转换

- **Empty dict:** `{}` or `dict()`.  
**空字典：**`{}` 或 `dict()`。

- **Literal build:** `{"a": 1, "b": 2}`; duplicate keys keep the **last value**.  
**字面量创建：**`{"a": 1, "b": 2}`；**重复键**将保留**最后一次**赋的值。

- **`dict()` conversions:** from  
**`dict()` 转换：**可由以下创建：
  - list of 2‑item lists: `dict([["a",1],["b",2]])`  
  - **2‑item tuples** list: `dict([("a",1),("b",2)])`  
  - tuple of 2‑item lists/tuples;  
  - sequence of **2‑char strings**: `dict(["ab","cd"])  # "a"->"b", "c"->"d"`  
  中文：  
  - **二维列表**（每项 2 元素）；**二维元组**列表；  
  - **列表/元组的元组**；  
  - **由 2 字符串组成的序列**（如 `"ab"` 变为 key=`"a"`, value=`"b"`）。

- **Keyword args:** `dict(one=1, two=2)` (names must be valid identifiers).  
**关键字参数：**`dict(one=1, two=2)`（参数名必须是**合法标识符**）。

---

## Add, Update, Retrieve / 添加、更新与取值

- **Add/Update by key:** `d[key] = value`. Duplicate key → value **overwritten** by latest.  
**通过键添加/更新：**`d[key] = value`。重复键 → 以**最后**赋值为准。

- **Retrieve by key:** `d[key]` returns value if key exists; **`KeyError`** otherwise.  
**取值：**`d[key]` 若存在返回值；否则抛出 **`KeyError`**。

- **Safe retrieval:**  
**安全取值：**
  - `key in d` → boolean membership test;  
  - `d.get(key, default=None)` → returns value or **default** (no exception).  
  - `key in d` → 判断是否存在；  
  - `d.get(key, default=None)` → 返回值或**默认值**（不抛异常）。

---

## Membership, Views, Length / 成员测试、视图与长度

- **Views:** `d.keys()`, `d.values()`, `d.items()` return dynamic views.  
**视图：**`d.keys()`、`d.values()`、`d.items()` 返回**动态视图**。

- **Length:** `len(d)` gives number of items.  
**长度：**`len(d)` 返回元素个数。

---

## Merge & Combine / 合并与组合

- **In‑place merge:** `d.update(other)`; if keys collide, later **overwrites**.  
**原地合并：**`d.update(other)`；键冲突时**以后者覆盖**。

- **Expression merge (3.9+):** `d1 | d2` returns a **new dict**; `d1 |= d2` updates in place.  
**表达式合并（3.9+）：**`d1 | d2` 生成**新字典**；`d1 |= d2` 为**原地更新**。

- **Unpack merge:** `{**a, **b}` creates a new dict; rightmost wins on conflicts.  
**解包合并：**`{**a, **b}` 生成新字典；右侧冲突**优先生效**。

---

## Delete & Pop & Clear / 删除、弹出与清空

- **`del d[key]`** removes an item; missing key raises **`KeyError`**.  
**`del d[key]`** 删除元素；缺失键将抛 **`KeyError`**。

- **`d.pop(key)`** returns and removes; missing key raises **`KeyError`** unless default is given: `d.pop(k, default)`.  
**`d.pop(key)`** 返回并删除；若缺失则抛 **`KeyError`**，除非提供默认值：`d.pop(k, default)`。

- **`d.clear()`** empties dict; assigning `{}` also yields an empty dict.  
**`d.clear()`** 清空；也可赋值 `{}` 达到空字典效果。

---

## Assignment vs Copy / 赋值与拷贝（浅/深）

- **Assignment:** `b = a` creates an **alias**; edits to one affect the other.  
**赋值：**`b = a` 创建**别名**；修改一方会影响另一方。

- **Shallow copy:** `a.copy()`, `dict(a)` copy **top‑level only**.  
**浅拷贝：**`a.copy()`、`dict(a)` 只复制**最外层**。

- **Deep copy:** `copy.deepcopy(a)` recursively copies nested objects; safe when values are **mutable**.  
**深拷贝：**`copy.deepcopy(a)` 递归复制**嵌套可变对象**，更安全。

---

## Iterating over Dictionaries / 遍历字典

- Iterate **keys**: `for k in d:` or `for k in d.keys():`  
**遍历键：**`for k in d:` 或 `for k in d.keys():`。

- Iterate **values**: `for v in d.values():`  
**遍历值：**`for v in d.values():`。

- Iterate **items**: `for k, v in d.items():` (tuple unpacking).  
**遍历键值对：**`for k, v in d.items():`（元组解包）。

---

## Sets — Concepts & Basics / 集合——概念与基础

- A **set** is an **unordered** collection of **unique** hashable elements.  
**集合**是**无序**的、由**唯一**可哈希元素构成的容器。

- Types: **`set`** (mutable) and **`frozenset`** (immutable).  
类型：**`set`**（可变）与 **`frozenset`**（不可变）。

---

## Build & Convert Sets / 集合的创建与转换

- **Empty set:** `set()` (note: `{}` is an empty **dict**).  
**空集合：**`set()`（注意：`{}` 是空**字典**）。

- **From iterables:** `set("abc")`, `set([1,2,3])`, `set((1,2,3))`, `set({"k":1})` → keys only.  
**从可迭代对象：**`set("abc")`、`set([1,2,3])`、`set((1,2,3))`、`set({"k":1})`（只取键）。

---

## Modify & Query Sets / 集合的修改与查询

- **Add:** `s.add(x)`; **Remove:** `s.remove(x)` raises **`KeyError`** if absent; `s.discard(x)` is safe.  
**添加/删除：**`s.add(x)`；`s.remove(x)` 若不存在抛 **`KeyError`**；`s.discard(x)` 不报错。

- **Length:** `len(s)`; **Membership:** `x in s`.  
**长度：**`len(s)`；**成员测试：**`x in s`。

- **Iteration:** `for x in s:`.  
**迭代：**`for x in s:`。

---

## Set Algebra / 集合代数运算

- **Intersection (∩):** `s & t` or `s.intersection(t)`.  
**交集（∩）：**`s & t` 或 `s.intersection(t)`。

- **Union (∪):** `s | t` or `s.union(t)`.  
**并集（∪）：**`s | t` 或 `s.union(t)`。

- **Difference (−):** `s - t` or `s.difference(t)`.  
**差集（−）：**`s - t` 或 `s.difference(t)`。

- **Symmetric difference (⊕):** `s ^ t` or `s.symmetric_difference(t)`.  
**对称差（⊕）：**`s ^ t` 或 `s.symmetric_difference(t)`。

---

## Set Relations & Tests / 集合关系与判定

- **Subset:** `s <= t` or `s.issubset(t)`; **Proper subset:** `s < t`.  
**子集：**`s <= t` 或 `s.issubset(t)`；**真子集：**`s < t`。

- **Superset:** `s >= t` or `s.issuperset(t)`; **Proper superset:** `s > t`.  
**上位集：**`s >= t` 或 `s.issuperset(t)`；**真上位集：**`s > t`。

---

## Set Comprehensions & frozenset / 集合内包与不可变集合

- **Set comprehension:** `{expr for x in iterable}`; can combine **if** and multiple **for**.  
**集合内包：**`{expr for x in iterable}`；可结合 **if** 与多个 **for**。

- **`frozenset(iterable)`** builds an immutable set (hashable, can be a dict key).  
**`frozenset(iterable)`** 生成不可变集合（可哈希，可作字典键）。

---

## Larger Data Structures / 更大的数据结构组合

- **Tuple of lists**, **list of lists**, **dict of lists**, **dict with tuple keys** (keys must be immutable).  
**列表元组**、**列表的列表**、**值为列表的字典**、**以元组为键的字典**（键必须不可变）。

- Choose structures based on **access pattern** (offset vs key) and **mutability** needs.  
**按访问方式**（偏移 vs 键）和**可变性需求**选择合适结构。

---

## Exercises 6‑1/6‑2/6‑3: 2‑D Array Display / 演习 6‑1/6‑2/6‑3：二维数组显示

> **Goal:** Print **2‑D arrays** (lists of lists) in progressively richer layouts.  
> **目标：**以逐步增强的样式打印**二维数组**（列表的列表）。

**Common inputs / 通用输入**  
- Testbenches iterate over arrays like `[[0,1,2]]`, `[[0,1,2],[2,0,1]]`, `[[0,1,2],[2,0,1],[1,2,0]]`, etc.  
**测试脚本会遍历**如 `[[0,1,2]]`、`[[0,1,2],[2,0,1]]`、`[[0,1,2],[2,0,1],[1,2,0]]` 等多种数组。

**Exercise 6‑1 — `show_1(a)`**  
- **Generalize** a 3×3 printing demo to **any `m × n`** 2‑D list.  
**将 3×3 打印示例**一般化，支持**任意 `m × n`**。  
- **Hints:** rows = `len(a)`, cols = `len(a[0])`; loop rows, then columns; `print()` end‑control.  
**提示：**行数 `len(a)`，列数 `len(a[0])`；外层行、内层列循环；掌握 `print()` 的 `end` 控制。  
- **Robustness:** if rows are **ragged** (different lengths), consider raising or handling gracefully (e.g., per‑row length).  
**健壮性：**若**不规则**（行长不同），可选择抛错或按行长度处理。

**Exercise 6‑2 — `show_2(a)`**  
- Print array with an **outer frame** (top/bottom borders and side bars).  
**为数组加**外框**显示（上下边框与左右边界）**。  
- **Pattern idea:** compute column width per column to align; build `border = "+" + "+".join("-"*w for w in widths) + "+"`; print rows with `|` separators.  
**样式思路：**可为每列计算宽度对齐；构建 `border` 作为上下边界；行内用 `|` 分隔。  
- **Edge cases:** empty array or empty rows → define a sensible empty frame or skip.  
**边界：**空数组/空行时给出合理的空框或跳过。

**Exercise 6‑3 — `show_3(a)`**  
- Print only the **inner grid lines** (no outer frame), i.e., draw separators **between** cells.  
**仅打印**内部网格线**（不画外边框），只在**单元格之间**画分隔。**  
- **Idea:** reuse width computation; build a row separator (e.g., `"---+----+--"`) printed **between** data rows.  
**思路：**复用列宽计算；构造行间分隔线，只在各数据行**之间**打印。

> **Testing:** Use provided scripts `show_1.py`, `show_2.py`, `show_3.py`; each loops over several arrays and calls `show_1/2/3`. Adjust formatting to match your instructor’s expected output.  
> **测试：**使用提供的 `show_1.py`、`show_2.py`、`show_3.py`；它们会遍历多组数组并调用 `show_1/2/3`。**调整打印格式以匹配授课老师的期望输出。**

**ASCII sketch / ASCII 示意**  
```
# show_1 (no frame / 无外框)
0 1 2
2 0 1
1 2 0

# show_2 (outer frame / 外框)
+-------+-------+-------+
|   0   |   1   |   2   |
+-------+-------+-------+
|   2   |   0   |   1   |
+-------+-------+-------+
|   1   |   2   |   0   |
+-------+-------+-------+

# show_3 (inner grid only / 仅内部网格)
  0   |   1   |   2
------+------+------
  2   |   0   |   1
------+------+------
  1   |   2   |   0
```

### Implementation Notes & Minimal Sanity Tests / 实现思路与最小对拍用例

**show_1(a) — no frame / 无外框**  
- Convert each row to strings and join with a single space.  
**逐行转为字符串并用单空格连接。**

```python
from Python.src.show_1 import show_1
show_1([[0,1,2]])
show_1([[0,1,2],[2,0,1],[1,2,0]])
```

**show_2(a) — outer frame / 外框**  
- Compute per‑column widths; draw top/bottom borders like `+-----+---+...+`; pad cells with 1 space on both sides.  
**计算每列宽度；绘制上/下边框；单元格两侧各留 1 空格。**

```python
from Python.src.show_2 import show_2
show_2([[0,1,2]])
show_2([[0,1,2],[2,0,1],[1,2,0]])
```

**show_3(a) — inner grid only / 仅内部网格**  
- No outer frame; separate cells with ` | `; print row separators **between** data rows using dashes.  
**不画外框；单元格用 ` | ` 分隔；行与行之间用虚线分隔。**

```python
from Python.src.show_3 import show_3
show_3([[0,1,2]])
show_3([[0,1,2],[2,0,1]])
show_3([[0,1,2],[2,0,1],[1,2,0]])
```


> [show_1.py — Code / show_1.py — 代码](./src/show_1.py)

> [show_2.py — Code / show_2.py — 代码](./src/show_2.py)

> [show_3.py — Code / show_3.py — 代码](./src/show_3.py)

> Tip: If your `show_*.py` script has strict requirements for the output format, please make minor adjustments to the padding and delimiter details (such as the number of spaces on both sides and the number of dashes).

> 注意：若你的 `show_*.py` 对输出格式有严格要求，请对填充与分隔符细节做微调（例如左右空格数、横线数量）。



<h2></h2>

[← Previous Lecture / 上一讲](./lecture05.md) · [Next Lecture / 下一讲 →](./lecture07.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

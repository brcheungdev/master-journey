[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 09 Notes 
# 计算机编程（Python）——第 09 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Modules, Packages, Standard Library / 模块、包与标准库](#modules-packages-standard-library--模块包与标准库)
- [Import Patterns / import 常见模式](#import-patterns--import-常见模式)
- [Managing Packages / 管理包与模块搜索路径](#managing-packages--管理包与模块搜索路径)
- [Stdlib Highlights / 标准库亮点：pprint、random、collections、itertools](#stdlib-highlights--标准库亮点pprintrandomcollectionsitertools)
- [Exercises 9‑A/9‑B — Primes (3) & (4) / 演习 9‑A/9‑B——素数（3）与（4）](#exercises-9a9b--primes-3--4--演习-9a9b——素数3与4)
- [Timing & Plotting / 计时与绘图](#timing--plotting--计时与绘图)
- [Implementation Notes & Minimal Tests / 实现思路与最小对拍](#implementation-notes--minimal-tests--实现思路与最小对拍)
- [Source Files / 源码文件](#source-files--源码文件)

---

## Today’s Agenda / 今日教学安排

- Modules → Packages → Standard Library tour; then Primes (3) & (4).  
模块 → 包 → 标准库导览；随后是素数（3）与（4）。 

---

## Learning Objectives / 学习目标

- Understand **modules** (files), **packages** (directories) and how **import** works.  
**理解**模块（文件）、包（目录）与 **import** 的工作方式。 

- Use **stdlib** tools (`pprint`, `random`, `collections`, `itertools`) in small tasks.  
**掌握**常用标准库（`pprint`、`random`、`collections`、`itertools`）的基本用法。

- Implement **optimized sieves** for primes and compare performance.  
**能实现**优化的素数筛，并比较性能。

---

## Modules, Packages, Standard Library / 模块、包与标准库

- **Module:** a single **.py file**; **Package:** a directory containing modules (can be nested).  
**模块：**一个 **.py 文件**；**包：**包含模块的目录（可层级化）。 

- Examples show `choices/` package with `fast.py`, `advice.py`, and usage from `questions.py`.  
示例展示 `choices/` 包（`fast.py`、`advice.py`）及 `questions.py` 的调用。 

- **Standard library** provides many helpers; docs: `docs.python.org` (JP/EN).  
**标准库**提供大量模块；官方文档 JP/EN 版本并列。 

---

## Import Patterns / import 常见模式

- **Module alias:** `import numpy as np` reduces typos/verbosity.  
**模块别名：**通过 `import numpy as np` 降低输入量并提升可读性。
  
- **Selective import:** `from math import pi, sqrt as rt`.  
**选择性导入：**`from math import pi, sqrt as rt`。

- **From package:** `from choices import fast`; then `fast.pick(seq)`.  
**从包导入：**`from choices import fast`；随后调用 `fast.pick(seq)`。

---

## Managing Packages / 管理包与模块搜索路径

- Python searches modules along **sys.path** (starts at current dir).  
Python 通过 **sys.path**（从当前目录开始）搜索模块。

- Organize **directory hierarchies** to manage many modules.  
通过**目录层次**管理多模块工程。 

- Acquire third‑party code via **PyPI** and **GitHub**.  
通过 **PyPI** 与 **GitHub** 获取第三方代码。 

---

## Stdlib Highlights / 标准库亮点：pprint、random、collections、itertools

- **`pprint`** pretty‑prints nested structures; control **width**.  
**`pprint`** 漂亮打印嵌套结构；可控制**宽度**。 

- **`random`**: `choice`, `sample`, `randint`, `randrange`, `random`, seeds/state.  
**`random`**：`choice`、`sample`、`randint`、`randrange`、`random`、种子/状态。

- **`collections`**: `defaultdict`, `Counter`, `deque`.  
**`collections`**：`defaultdict`、`Counter`、`deque`。

- **`itertools`**: `chain`, `cycle`, `accumulate`.  
**`itertools`**：`chain`、`cycle`、`accumulate`。 

---

## Exercises 9‑A/9‑B — Primes (3) & (4) / 演习 9‑A/9‑B——素数（3）与（4）

- **Task 9‑A (prime_list_3)**: Implement **Eratosthenes**; verify via `prime_list_3.py`; measure **n=1000..10000** step 1000; plot vs **prime_list_2** using `plot_graph_2-3.py`.  
**任务 9‑A（prime_list_3）：**实现**埃氏筛**；用 `prime_list_3.py` 验证；在 **n=1000..10000**、步长 **1000** 测时；并用 `plot_graph_2-3.py` 与 **prime_list_2** 作图对比。

- **Task 9‑B (prime_list_4)**: Improve speed by using **odd‑only** array; verify via `prime_list_4.py`; measure and plot vs **prime_list_3** using `plot_graph_3-4.py`.  
**任务 9‑B（prime_list_4）：**基于**仅奇数数组**优化；用 `prime_list_4.py` 验证；计时并用 `plot_graph_3-4.py` 与 **prime_list_3** 作图对比。

---

## Timing & Plotting / 计时与绘图

- `%timeit` in loops for **n=1000..10000** (step 1000).  
在循环中用 `%timeit` 对 **1000..10000**（步长 **1000**）计时。 

- Fill arrays `y_2`, `y_3`, `y_4` with measured **milliseconds**; then run plotting scripts.  
将测得的**毫秒**填入 `y_2`、`y_3`、`y_4`，再运行对应绘图脚本。 

---

## Implementation Notes & Minimal Tests / 实现思路与最小对拍

**`prime_list_3(n)` — standard sieve / 标准埃氏筛**  
- Full array of size `n+1`; mark multiples from **`p*p`**; complexity **O(n log log n)**.  
**使用 `n+1` 大小数组，从 **`p*p`** 起标记倍数；复杂度 **O(n log log n)**。

```python
from Python.src.prime_list_3 import prime_list_3
print(prime_list_3(50))
```

**`prime_list_4(n)` — odd‑only sieve / 仅奇数筛**  
- Map index `i` to number **`2*i+3`** (3,5,7,...); halve memory & ~halve time.  
**索引 `i` 映射到 **`2*i+3`**（3,5,7, ...）；内存减半，时间近半。**

```python
from Python.src.prime_list_4 import prime_list_4
print(prime_list_4(50))
```

> Testing / 测试：使用提供的 `prime_list_3.py` 与 `prime_list_4.py`。 

---

## Source Files / 源码文件

- [`Python/src/prime_list_3.py`](./src/prime_list_3.py) 
**说明：**标准埃氏筛。

- [`Python/src/prime_list_4.py`](./src/prime_list_4.py) 
**说明：**仅奇数的埃氏筛。

- [`Python/src/Timeit-3.py`](./src/Timeit-3.py) 
**说明：**对 `prime_list_3` 的 `%timeit`。

- [`Python/src/Timeit-4.py`](./src/Timeit-4.py) 
**说明：**对 `prime_list_4` 的 `%timeit`。

- [`Python/src/plot_graph_2-3.py`](./src/plot_graph_2-3.py) 
**说明：**`prime_list_2` vs `prime_list_3` 绘图模板。

- [`Python/src/plot_graph_3-4.py`](./src/plot_graph_3-4.py) 
**说明：**`prime_list_3` vs `prime_list_4` 绘图模板。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture08.md) · [Next Lecture / 下一讲 →](./lecture10.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

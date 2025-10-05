[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.
  
# Computer Programming (Python) — Lecture 10 Notes 
# 计算机编程（Python）——第 10 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Objects & Classes — Basics / 对象与类：基础](#objects--classes--basics--对象与类基础)
- [Attributes & Initialization / 属性与初始化](#attributes--initialization--属性与初始化)
- [Inheritance & super() / 继承与 super()](#inheritance--super--继承与-super)
- [Multiple Inheritance & MRO / 多重继承与 MRO](#multiple-inheritance--mro--多重继承与-mro)
- [Encapsulation: Property & Name Mangling / 封装：property 与名称改写](#encapsulation-property--name-mangling--封装property-与名称改写)
- [Class/Instance Attributes & Method Types / 类属性/实例属性与方法类型](#classinstance-attributes--method-types--类属性实例属性与方法类型)
- [Duck Typing / 鸭子类型](#duck-typing--鸭子类型)
- [Special Methods / 特殊方法](#special-methods--特殊方法)
- [NamedTuple & Dataclass / NamedTuple 与 Dataclass](#namedtuple--dataclass--namedtuple-与-dataclass)
- [Composition vs Inheritance / 组合 vs 继承](#composition-vs-inheritance--组合-vs-继承)
- [Exercises C‑03‑0/1/2 — Tic‑Tac‑Toe / 演习 C‑03‑0/1/2——井字棋](#exercises-c03-012--tictactoe--演习-c03-012——井字棋)
- [Implementation Notes & Minimal Tests / 实现思路与最小对拍](#implementation-notes--minimal-tests--实现思路与最小对拍)
- [Source Files / 源码文件](#source-files--源码文件)

---

## Today’s Agenda / 今日教学安排

- Objects & Classes → Inheritance → Properties → Method Types → Duck Typing → Special Methods → NamedTuple/Dataclass → Composition.  
对象与类 → 继承 → 属性/属性访问器 → 方法类型 → 鸭子类型 → 特殊方法 → NamedTuple/Dataclass → 组合。

- **Exercises:** C‑03‑0 rules; C‑03‑1 show the **board**; C‑03‑2 **is_win** judgement.  
**演习：**C‑03‑0 规则；C‑03‑1 显示**棋盘**；C‑03‑2 **胜负判定**。 

---

## Learning Objectives / 学习目标

- Define classes, construct objects, add/read/write attributes, and implement methods.  
**掌握**类定义、对象构造、属性读写与方法实现。

- Use inheritance/override and `super()`; explain MRO in multiple inheritance.  
**会用**继承/重写与 `super()`；理解多重继承的 **MRO**。

- Use properties, getters/setters, and name‑mangling for encapsulation.  
**理解**`property`、getter/setter 与名称改写以实现封装。 

- Apply duck typing and special methods (`__eq__`, `__repr__`, etc.).  
**应用**鸭子类型与特殊方法（`__eq__`、`__repr__` 等）。

---

## Objects & Classes — Basics / 对象与类：基础

- **Object:** a custom data structure containing **data (attributes)** and **code (methods)**.  
**对象：**包含**数据（属性）**与**代码（方法）**的自定义数据结构。

- Define classes with `class Name:`; instantiate with `obj = Name(...)`.  
使用 `class 名称:` 定义；用 `obj = 名称(...)` 实例化。

---

## Attributes & Initialization / 属性与初始化

- Add attributes on the instance; access via dot notation.  
在实例上添加属性；使用点号访问。

- Initialize with **`__init__(self, ...)`**; first parameter must be **`self`**.  
使用 **`__init__(self, ...)`** 初始化；第一个参数必须是 **`self`**。 

---

## Inheritance & super() / 继承与 super()

- Child class reuses parent code; override to change behavior.  
子类复用父类代码；通过**重写**修改行为。

- Call parent implementations with **`super()`**.  
用 **`super()`** 调用父类实现。 

---

## Multiple Inheritance & MRO / 多重继承与 MRO

- Multiple inheritance forms a method resolution order (**MRO**); inspect with `.mro()`.  
多重继承决定方法解析顺序（**MRO**）；可用 `.mro()` 查看。 

- Mixins provide reusable method groups without deep hierarchies.  
**Mixin** 提供可复用方法群，避免深层继承。 

---

## Encapsulation: Property & Name Mangling / 封装：property 与名称改写

- Access control via `@property` / `@x.setter`; computed properties are common.  
通过 `@property` / `@x.setter` 访问；常用于计算属性。 

- Name‑mangling with double underscores helps **hide** implementation details.  
**双下划线**名称改写可**隐藏**实现细节（内部用）。

---

## Class/Instance Attributes & Method Types / 类属性/实例属性与方法类型

- Distinguish **class attributes** vs **instance attributes**; updates affect different scopes.  
区分**类属性**与**实例属性**；修改影响范围不同。 

- Method types: **instance methods** (default), **`@classmethod`** (first arg `cls`), **`@staticmethod`** (no implicit first arg).  
方法类型：**实例方法**、**`@classmethod`**（首参 `cls`）、**`@staticmethod`**（无隐式首参）。

---

## Duck Typing / 鸭子类型

- Focus on **capabilities** (methods/attributes) rather than exact types.  
关注对象**能做什么**，而非其确切类型。

---

## Special Methods / 特殊方法

- Implement `__eq__` for equality; `__repr__` for printable representation; many others for comparison/arithmetic.  
实现 `__eq__` 用于相等比较；`__repr__` 用于可读表示；以及其他比较/算术等特殊方法。

---

## NamedTuple & Dataclass / NamedTuple 与 Dataclass

- **namedtuple**: tuple‑like, immutable, access by attribute name, memory‑/speed‑efficient.  
**namedtuple：**类元组、不可变、可用属性名访问，内存/速度更优。 

- **dataclass** (3.7+): class boilerplate reduction with type annotations.  
**dataclass（3.7+）：**借助类型注解减少样板代码。

---

## Composition vs Inheritance / 组合 vs 继承

- Prefer **composition** when modeling “has‑a” or “uses” relations; use inheritance for clear “is‑a”.  
“**has‑a / uses**” 关系优先**组合**；明确“**is‑a**”时用**继承**。 

---

## Exercises C‑03‑0/1/2 — Tic‑Tac‑Toe / 演习 C‑03‑0/1/2——井字棋

- **C‑03‑0 (Rules)**: 3×3 grid; players place **O** or **X** alternately; line of 3 wins; full board without line is a draw.  
**C‑03‑0（规则）：**3×3 网格；两名玩家轮流下 **O/X**；任一方向三连即胜；满盘无三连则**平局**。

- **C‑03‑1 (show_board)**: input a length‑9 list of ints (0/1/2); output 3×3 characters by mapping **0→“-”**, **1→“O”**, **2→“X”**.  
**C‑03‑1（显示棋盘）：**输入 9 元整数列表（0/1/2）；输出 3×3 字符阵，映射 **0→“-”**、**1→“O”**、**2→“X”**。 

- **C‑03‑2 (is_win)**: implement `is_win(board, player)`; check rows, columns, and two diagonals for **all 1s** (player 1) or **all 2s** (player 2).  
**C‑03‑2（胜负判定）：**实现 `is_win(board, player)`；在行、列、两条对角线上检查**全为 1**（先手）或**全为 2**（后手）。

> 注意：某些无效棋面可能出现双方“同时胜出”。实际对局中一方胜出时立刻结束，因此不会出现同时胜出的情况。  
> **Note:** invalid positions may appear to have both sides winning, but real games stop at first win. 

---

## Implementation Notes & Minimal Tests / 实现思路与最小对拍

**`show_board(board)`**  
- Validate **length==9**; map via `("-", "O", "X")`; print three rows with spaces.  
**校验长度 9**；用 `("-", "O", "X")` 映射；三行打印、元素间空格分隔。

```python
from Python.src.show_board import show_board
board = [0, 1, 2, 1, 2, 0, 2, 0, 1]
show_board(board)
# Expect (match testbench style):
# - O X
# O X -
# X - O
```

**`is_win(board, player)`**  
- Predefine winning triples: rows `(0,1,2) ...`, cols `(0,3,6) ...`, diagonals `(0,4,8)`, `(2,4,6)`; return True if any triple equals `player`.  
**预置连线三元组：**行、列、对角线；任一三元组全等于 `player` 则 True。

```python
from Python.src.is_win import is_win
print(is_win([1,1,1, 0,2,2, 2,0,1], 1))  # True
```

> **Testbenches:** `show_board.py`, `is_win.py`. 
> 对拍脚本：`show_board.py` 与 `is_win.py`。  


---

## Source Files / 源码文件

- [`Python/src/show_board.py`](./src/show_board.py) 
**说明：**将 9 元列表呈现为 3×3 棋盘（`- / O / X`）。

- [`Python/src/is_win.py`](./src/is_win.py)
**说明：**判定给定玩家是否三连（行/列/斜线）。


---

## Implementation add‑on — Minimal sanity tests & CLI / 实现补充——最小对拍与命令行工具

**Minimal sanity tests / 最小对拍**

```python
from Python.src.show_board import show_board
from Python.src.is_win import is_win

# A sample board / 示例棋面
board = [0, 1, 2,
         1, 2, 0,
         2, 0, 1]

show_board(board)
print("win O? ", is_win(board, 1))  # player=1 -> O
print("win X? ", is_win(board, 2))  # player=2 -> X
```

**Command‑line mini tool / 命令行小工具**

- [`Python/src/ttt_cli.py`](./src/ttt_cli.py) 
**说明：**一行命令传入棋盘与玩家，打印棋盘并判定胜负。

```bash
# In project root / 在项目根目录
python Python/src/ttt_cli.py "[1,1,1,0,2,2,2,0,1]" 1
# or / 或
python -m Python.src.ttt_cli "[0,1,2,1,2,0,2,0,1]" 2
```

<h2></h2>

[← Previous Lecture / 上一讲](./lecture09.md) · [Next Lecture / 下一讲 →](./lecture11.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 13 Notes 
# 计算机编程（Python）——第 13 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Assignment C‑3‑9: Improve next-move function / 作业 C‑3‑9：改进“下一手”函数](#assignment-c3-9-improve-next-move-function--作业-c3-9改进下一手函数)
- [Game examples / 游戏示例](#game-examples--游戏示例)
- [Game tree & Minimax/Negamax/Alpha-Beta / 游戏树与 Minimax/Negamax/Alpha-Beta](#game-tree--minimaxnegamaxalpha-beta--游戏树与-minimaxnegamaxalpha-beta)
- [Design hints / 设计提示](#design-hints--设计提示)
- [Implementation plan / 实现方案](#implementation-plan--实现方案)
- [Minimal tests / 最小对拍](#minimal-tests--最小对拍)
- [Source Files / 源码文件](#source-files--源码文件)

---

## Today’s Agenda / 今日教学安排

- **Review previous work; finalize next-move function; set evaluation.**  
**复习前序内容；完善“下一手”函数；说明评估办法。** 

---

## Learning Objectives / 学习目标

- Turn heuristics and search into a **deterministic next-move function**.  
**将启发式与搜索**落地为**确定性的下一手函数**。 

- Understand **game tree search** and **alpha‑beta pruning** benefits.  
**理解**游戏树搜索与 **α‑β 剪枝** 的优势。 

---

## Assignment C‑3‑9: Improve next-move function / 作业 C‑3‑9：改进“下一手”函数

- **Goal:** write a function that chooses the **most promising next move**.  
**目标：**编写函数，选择**最有希望**的下一手。

- **Using `Tic_Tac_Toe` module:** you **may import** required functions from it.  
**允许**从 `Tic_Tac_Toe` 模块 **import** 必要函数辅助开发。

- **Local objects rule:** aside from those imports, **all other helpers** (functions/data) must be **defined locally inside your function**.  
**本地对象约束：**除必要的导入外，**其它对象**（函数/数据）必须在**你的函数内部**定义。

- **Name:** function name e.g., `M00W0000(board, player)`.  
**命名：**函数名例如 `M00W0000(board, player)`。


---

## Game tree & Minimax/Negamax/Alpha-Beta / 游戏树与 Minimax/Negamax/Alpha-Beta

- Build a **game tree** from the current state; terminal nodes are **win/loss/draw**.  
**从当前局面扩展**游戏树；终端节点为**胜/负/和**。 

- **Minimax:** MAX tries to **maximize** utility, MIN tries to **minimize**; back up values.  
**Minimax：**MAX **最大化**收益，MIN **最小化**；自底向上回溯数值。 

- **Negamax:** symmetric form of minimax: `max(val) == -min(-val)` simplifies code.  
**Negamax：**minimax 的对称写法：`max(val) == -min(-val)`，代码更简洁。

- **Alpha‑Beta:** same result as minimax but **prunes** branches, hence faster.  
**Alpha‑Beta：**与 minimax 等价，但可**剪枝**，因此更快。 

---

## Design hints / 设计提示

- Prefer **search‑based** decision for correctness; add **heuristics** to break ties and guide move ordering.  
**优先**基于**搜索**的正确性；用**启发式**打破平局并进行着法排序。

- Read **Wikipedia (JP)** pages for **ミニマックス法 / アルファ・ベータ法** as background.  
可参考维基（JP）条目 **Minimax/Alpha‑Beta** 作为背景阅读。

---

## Implementation plan / 实现方案

- **Core function:** implement your `M00W0000(board, player)` .  
**核心函数：**实现 `M00W0000(board, player)`。

- **Search:** use **Negamax + Alpha‑Beta**; evaluation at terminals: **+10 win / −10 loss / 0 draw**, with **depth tie‑break**.  
**搜索：**使用 **Negamax + αβ 剪枝**；在终局：**胜 +10 / 负 −10 / 和 0**，并用**深度**打破平局。

- **Move ordering:** use **center → corners → edges** to prune early.  
**着法排序：**启发式 **中→角→边**，利于早剪枝。

- **Local helpers:** move legality / win check / evaluation **defined inside** your function (per rule).  
**本地辅助：**合法着法/胜负判断/评估逻辑**定义在函数内部**（作业要求）。

- **Optional upgrades:** **transposition table**, **symmetry reduction**, randomized tie‑break to avoid mirrors.  
**可选增强：****置换表**、**对称性裁剪**、随机化平局打破避免镜像。

---

## Minimal tests / 最小对拍

```python
from Python.src.template_next_move import M00W0000

# Must win now / 立即取胜
print(M00W0000([1,1,0, 0,2,0, 0,0,2], 1))  # expect 2

# Must block / 必须堵住
print(M00W0000([2,2,0, 1,0,0, 0,1,0], 1))  # expect 2
```

---

## Source Files / 源码文件

- [`Python/src/template_next_move.py`](./src/template_next_move.py)
**说明：**Negamax + αβ 的**下一手函数模板**。

- [`Python/src/Testbench_C-03-9.py`](./src/Testbench_C-03-9.py)
**说明：**对拍脚本：你的函数 vs `Random`/`L0`。
  

<h2></h2>


[← Previous Lecture / 上一讲](./lecture12.md) · [Next Lecture / 下一讲 →](./lecture14.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

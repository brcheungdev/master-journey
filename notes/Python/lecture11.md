[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 11 Notes 
# 计算机编程（Python）——第 11 讲笔记
---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [Find legal moves: `candidate(board)` / 计算可落子位置：`candidate(board)`](#find-legal-moves-candidateboard--计算可落子位置candidateboard)
- [Random policy: `player_Random(board, player)` / 随机策略：`player_Random(board-player)`](#random-policy-player_randomboard-player--随机策略player_randomboard-player)
- [Tic_Tac_Toe module overview / `Tic_Tac_Toe` 模块总览](#tictactoe-module-overview--tictactoe-模块总览)
- [Play against human / 与人对战程序](#play-against-human--与人对战程序)
- [Experiment: first move 0 vs 1 vs 4 / 实验：首手 0、1、4 的胜率](#experiment-first-move-0-vs-1-vs-4--实验首手-014-的胜率)
- [Implementation Notes & Minimal Tests / 实现思路与最小对拍](#implementation-notes--minimal-tests--实现思路与最小对拍)
- [Source Files / 源码文件](#source-files--源码文件)

---

## Today’s Agenda / 今日教学安排

- Legal moves → Random player → `Tic_Tac_Toe` module → Play_with_human → Experiments.  
可落子 → 随机玩家 → `Tic_Tac_Toe` 模块 → 人机对战 → 实验。 

- **Exercises:** C‑03‑3 `candidate()`; C‑03‑4 `player_Random()`; C‑03‑5 run 10,000 games to analyze first move.  
**演习：**C‑03‑3 `candidate()`；C‑03‑4 `player_Random()`；C‑03‑5 运行 1 万局分析首手差异。 

---

## Learning Objectives / 学习目标

- Implement **legal move search** and a **random policy** using `random.choice`.  
**掌握**可落子搜索与 **`random.choice`** 的随机策略。

- Compose a small **game engine** (init/place/show/is_win/bots/play loop).  
**能组合**小型**博弈引擎**（初始化/落子/显示/胜判/AI/对局循环）。

- Design **experiments** and reason about **symmetry** (corner/edge/center group).  
**会设计实验**并基于**对称性**分析（角/边/中）位置的有利性。

---

## Find legal moves: `candidate(board)` / 计算可落子位置：`candidate(board)`

- Input a **length‑9** list with values **0/1/2**; return indices with value **0**.  
**输入**长度 **9** 的列表（值 **0/1/2**）；返回值为 **0** 的索引。 

- Use list comprehension `[(i) for i,v in enumerate(board) if v==0]`.  
**用列表推导** `[(i) for i,v in enumerate(board) if v==0]`。

> Testbench pages in slides verify the expected outputs.  
> 讲义中提供了测试基准与期望输出。 

---

## Random policy: `player_Random(board, player)` / 随机策略：`player_Random(board, player)`

- If cannot judge which move is better, **pick randomly** from candidates.  
**无法判断优劣时**，在候选中**随机选择**。

- Implementation: `random.choice(candidate(board))`; note `player` is **unused for choice**.  
**实现：**`random.choice(candidate(board))`；注意 `player` 在选择过程**不参与**。 

---

## Tic_Tac_Toe module overview / `Tic_Tac_Toe` 模块总览

- Functions: `init_board()`, `place(board,pos,player)`, `show_board(board)`, `is_win(board,player)`, **`player_L0`** (random), `play_game(...)`, `game_control(...)`, `document_it`.  
**函数集合：**`init_board()`、`place(board,pos,player)`、`show_board(board)`、`is_win(board,player)`、**`player_L0`**（随机）、`play_game(...)`、`game_control(...)`、`document_it`。

- `play_game` plays **one** game from the initial board; `game_control` runs **multiple** games and **aggregates** win/draw rates.  
`play_game` 负责**单局对战**；`game_control` 执行**多局统计**胜率/和棋率。 

---

## Play against human / 与人对战程序

- Choose to be **first or second**; default opponent is `player_L0`.  
可选择**先手/后手**；默认对手为 `player_L0`。

- Replace opponent policy to play stronger bots later.  
替换对手策略即可与**更强 AI** 对战。

---

## Experiment: first move 0 vs 1 vs 4 / 实验：首手 0、1、4 的胜率

- Symmetry groups: **corners** `[0,2,6,8]`, **edges** `[1,3,5,7]`, **center** `[4]`.  
**对称分组：**角 `[0,2,6,8]`、边 `[1,3,5,7]`、中 `[4]`。

- Analyze only **representatives** 0, 1, 4. Run **10,000** games each and compare first‑player win rates.  
仅分析代表位置 **0/1/4**；各跑 **10,000 局**对比先手胜率。 

---

## Implementation Notes & Minimal Tests / 实现思路与最小对拍

**`candidate(board)`**  
- Validate length/values; return indices where cell==0.  
**先校验长度/取值；再返回等于 0 的索引列表。**

```python
from Python.src.candidate import candidate
print(candidate([0,2,0, 1,2,1, 0,1,2]))  # -> [0,2,6]
```

**`player_Random(board, player)`**  
- Forward to `candidate()`; random‑choose one index.  
**调用 `candidate()` 获取候选，再随机选一个。**

```python
from Python.src.player_random import player_Random
print(player_Random([0,1,0, 2,1,2, 0,2,1], 2))
```

**`tictac_toe` engine / 引擎**  
- `play_game(board, p1, p2, Debug)` returns winner **1/2/0** and final board.  
**返回胜者 1/2/0 与终局棋盘。**

```python
from Python.src.tictac_toe import play_game, game_control, player_L0
w, b, m = play_game(player_1=player_L0, player_2=player_L0, Debug=0)
print("winner=", w, "moves=", m)
print(game_control(count=1000, init_pos=0))  # (wins_1, wins_2, draws)
```

---

## Source Files / 源码文件

- [`Python/src/candidate.py`](./src/candidate.py) 
**说明：**返回所有可落子索引。

- [`Python/src/player_random.py`](./src/player_random.py) 
**说明：**在候选中随机选一个落子位置。

- [`Python/src/tictac_toe.py`](./src/tictac_toe.py) 
**说明：**完整模块（初始化/落子/显示/胜判/随机 AI/单局/多局/装饰器）。

- [`Python/src/play_with_human.py`](./src/play_with_human.py))  
**说明：**命令行人机对战（可选先后手）。

---

## Experiment Template / 实验模板

> **Run this cell/script to reproduce the “first move 0/1/4” experiment.**  
> **运行下面代码以复现实验：比较首手 0/1/4 的胜率。**

```python
# Experiment: first-move advantage (0 vs 1 vs 4) / 实验：首手 0/1/4 的胜率
# English above; Chinese below each key line.

from pathlib import Path
import csv, random, time
from Python.src.tictac_toe import game_control, player_L0

# Fix random seed for reproducibility / 固定随机种子，便于复现实验
random.seed(20251111)

N = 10_000                      # games per position / 每个位置的对局数
positions = [0, 1, 4]           # symmetry representatives / 对称代表（角/边/中）
out_dir = Path("outputs/experiments")
out_dir.mkdir(parents=True, exist_ok=True)
csv_path = out_dir / "ttt_first_move.csv"

# CSV header / CSV 表头
with csv_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["init_pos", "games", "wins_p1", "wins_p2", "draws", "p1_win_rate"])

    # Loop over positions / 遍历三个首手位置
    for pos in positions:
        t0 = time.perf_counter()
        w1, w2, d = game_control(count=N, init_pos=pos)   # run N games / 跑 N 局
        dt = time.perf_counter() - t0
        rate = w1 / (w1 + w2 + d) if (w1 + w2 + d) else 0.0

        # Write a row and print a summary / 写入一行并打印摘要
        w.writerow([pos, N, w1, w2, d, f"{rate:.6f}"])
        print(f"pos={pos}  P1 win-rate={rate:.3%}  (w1={w1}, w2={w2}, d={d})  time={dt:.2f}s")

print("Saved CSV ->", csv_path)
```

> **Output files:** `outputs/experiments/ttt_first_move.csv` (results).  
> **输出文件：**`outputs/experiments/ttt_first_move.csv`（结果数据）。


<h2></h2>

[← Previous Lecture / 上一讲](./lecture10.md) · [Next Lecture / 下一讲 →](./lecture12.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

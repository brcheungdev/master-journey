[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 12 Notes 
# 计算机编程（Python）——第 12 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [C‑03‑6 — `player_L0`: group‑aware move selection / 分组优先的 `player_L0`](#c03-6--player_l0-groupaware-move-selection--分组优先的-player_l0)
- [C‑03‑7 — `player_L1`: immediate win first / `player_L1` 的“一步取胜”优先](#c03-7--player_l1-immediate-win-first--player_l1-的一步取胜优先)
- [C‑03‑8 — `player_L2`: win → block → fallback / `player_L2` 的“取胜→阻挡→兜底”](#c03-8--player_l2-win--block--fallback--player_l2-的取胜→阻挡→兜底)
- [Testbenches & Experiments / 测试基准与实验建议](#testbenches--experiments--测试基准与实验建议)
- [Implementation Notes & Minimal Tests / 实现思路与最小对拍](#implementation-notes--minimal-tests--实现思路与最小对拍)
- [Source Files / 源码文件](#source-files--源码文件)

---

## Today’s Agenda / 今日教学安排

- From random to **player_L0/L1/L2**; evaluate win‑rates with testbenches.  
从随机策略到 **player_L0/L1/L2**；用测试基准评估胜率提升。

---

## Learning Objectives / 学习目标

- Translate qualitative heuristics (center/corner/edge) into **codeable priorities**.  
**将启发式（中心/角/边）**转化为可编码的**优先级**。

- Detect **immediate win** and **opponent threats** by **hypothetical moves**.  
通过**假设落子**检测**一步取胜**与**对手威胁**。

- Run **controlled experiments** and present results (CSV + narrative).  
组织**可复现实验**并呈现结果（CSV + 文本分析）。

---

## C‑03‑6 — `player_L0`: group‑aware move selection / 分组优先的 `player_L0`

- Based on Lecture 11 analysis, prioritize **center → corners → edges**.  
基于第 11 讲分析，优先 **中心→角→边**。

- Among candidates, choose randomly **within** the best available group.  
在候选的**最佳分组**内进行**随机**选择。

- Interface: `player_L0(board, player) -> int` (player unused for choice).  
接口：`player_L0(board, player) -> int`（选择中不使用 `player`）。

---

## C‑03‑7 — `player_L1`: immediate win first / `player_L1` 的“一步取胜”优先

- For each candidate, **simulate placing** `player`; if `is_win(tmp, player)` then **take it**.  
对每个候选**模拟落子**，若 `is_win(tmp, player)` 为真则**立刻选取**。

- Else, **fallback** to `player_L0` (group‑aware choice).  
否则**退回** `player_L0` 的分组优先策略。

---

## C‑03‑8 — `player_L2`: win → block → fallback / `player_L2` 的“取胜→阻挡→兜底”

- Step 1: if **winning move** exists for `player`, choose it.  
第一步：若存在**取胜点**，直接选择。

- Step 2: else, if opponent has an **immediate winning move**, **block** it.  
第二步：否则，若对手存在**一步取胜**点，则**进行阻挡**。

- Step 3: else, **fallback** to `player_L0`.  
第三步：否则**退回** `player_L0`。

---

## Testbenches & Experiments / 测试基准与实验建议

- Use provided patterns from slides `Test_player_xyz.py` / `Test_player_L0.py` / `Test_players_L1.py` / `Test_player_L2.py`.  
参考讲义中的 `Test_player_xyz.py`/`Test_player_L0.py`/`Test_players_L1.py`/`Test_player_L2.py` 思路。

- Our repository also includes runnable scripts:  
本仓库也提供可运行脚本：  
  - `Python/src/Test_player_L0.py` — L0 vs Random。  
  - `Python/src/Test_player_L1.py` — L1 vs L0。  
  - `Python/src/Test_player_L2.py` — L2 vs L1 / L0。

- Recommendation: run **5k–10k** games per matchup and record **win/draw rates** to CSV for report.  
建议每组对战运行 **5k–10k 局**，记录**胜/和率**并用于报告。

---

## Implementation Notes & Minimal Tests / 实现思路与最小对拍

**`player_L0(board, player)`**  
- Choose center if free; else any corner; else any edge (random within group).  
若中心可下则选中心；否则选任一角；再否则选任一边（组内随机）。

```python
from Python.src.player_L0 import player_L0
from Python.src.tictac_toe import game_control
print(game_control(count=1000, player_1=player_L0, player_2=player_L0))
```

**`player_L1(board, player)`**  
- Scan candidates, simulate own move, return if winning; else L0.  
扫描候选，若自己一步可胜则立即选择；否则退回 L0。

```python
from Python.src.player_L1 import player_L1
from Python.src.tictac_toe import game_control
print(game_control(count=1000, player_1=player_L1, player_2=player_L1))
```

**`player_L2(board, player)`**  
- Try win; else block opponent win; else L0.  
先取胜；否则堵对手；再否则 L0。

```python
from Python.src.player_L2 import player_L2
from Python.src.tictac_toe import game_control
print(game_control(count=1000, player_1=player_L2, player_2=player_L2))
```

> Sanity tip / 小贴士：在 `tictac_toe.play_game(Debug=3)` 下观察一步步落子与棋盘演变，便于调试策略。

---

## Source Files / 源码文件

- [`Python/src/player_L0.py`](./src/player_L0.py) 
**说明：**分组优先（中>角>边），组内随机。

- [`Python/src/player_L1.py`](./src/player_L1.py) 
**说明：**一步取胜优先，否则退回 L0。

- [`Python/src/player_L2.py`](./src/player_L2.py)  
**说明：**取胜→阻挡→退回 L0。

- [`Python/src/Test_player_L0.py`](./src/Test_player_L0.py) 
**说明：**L0 对 Random 的胜率测试。

- [`Python/src/Test_player_L1.py`](./src/Test_player_L1.py) 
**说明：**L1 对 L0 的胜率测试。

- [`Python/src/Test_player_L2.py`](./src/Test_player_L2.py) 
**说明：**L2 对 L1/L0 的胜率测试。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture11.md) · [Next Lecture / 下一讲 →](./lecture13.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

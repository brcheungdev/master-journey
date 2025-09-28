[← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor: Prof. Shinji Tomita (富田眞治)  

---
# Lecture 13: Control-Unit Speedup (2) — Hazards, OoO, Speculation, Superscalar, Deep Pipelines  
# 第13回：制御装置の高速化（その2）— 乱実行・投機実行・スーパスカラ・ディープパイプライン

---

## ⚪ Lecture Overview / 课程概览
- **Pipeline hazards**: data / control / resource (数据/控制/资源相关)  
  **流水线风险**：数据相关 / 控制相关 / 资源相关  
- **Resource conflicts**: cache misses, long-latency FP units → bubbles/stalls (缓存未命中/浮点长延迟导致停顿)  
  **资源冲突**：缓存未命中、长延迟浮点单元 → 产生气泡/停顿  
- **Mitigations**: multi-level caches, bypassing, FP pipelines (多级缓存/旁路/浮点流水线)  
  **缓解手段**：多级缓存、转发/旁路、浮点流水线  
- **Out-of-Order (OoO)** execution & **Speculation** with rollback (乱実行与投機回滚)  
  **乱序执行（OoO）**与**投机执行**（带回滚）  
- **Reorder Buffer (ROB)** & **Register Renaming** (重排序缓冲与寄存器改名)  
  **重排序缓冲（ROB）**与**寄存器重命名**  
- **Superscalar** multi-issue & **Deep pipelines** (多发射与深流水)  
  **超标量**多发射与**深流水**  
- ILP limits → **multithreading/multicore** (从指令级并行转向线程/多核)  
  **ILP 的极限** → 迈向**多线程/多核**

---

### 1) Hazards & Dependencies / 乱れ要因与依存关系
- **Data dependence** blocks followers; without forwarding, multiple bubbles appear.  
  **数据相关**会阻塞后继指令；无转发时往往插入多个气泡。  
- **Control dependence** arises from branches/exceptions with unknown next PC.  
  **控制相关**源自分支/异常导致的下一条指令不确定。  
- **Resource conflict** when only one FP unit exists or on cache misses.  
  **资源冲突**如仅一台浮点单元或发生缓存未命中。  

```
Example timeline (long FP op blocks follower)
先行  IF  D  EX  EX  EX  MA  S
后继  IF  -  -  EX  EX  EX  MA  S     ← 无独立资源 → 插入2个bubble
```
### 2) Resource Conflicts → Speedups / 资源冲突与加速手段
(a) Multi-level caches  
  （a）多级缓存
- Typical (e.g., Intel i7-6700): L1=64KB, L2=256KB, L3=8MB  
  典型配置（如 Intel i7-6700）：L1=64KB，L2=256KB，L3=8MB  
- Relative costs (vs L1 hit time `T_H`): `T_L1≈12·T_H`, `T_L2≈44·T_H`, `T_L3≈70·T_H`  
  相对代价（相对于 L1 命中时间 `T_H`）：`T_L1≈12·T_H`、`T_L2≈44·T_H`、`T_L3≈70·T_H`  
- Example miss rates: `β=0.0271`, `βγ=0.0089` (cumulative)  
  命中/失配率示例：`β=0.0271`，`βγ=0.0089`（逐级失配）  
  - Effective time (2/3-level): `T_C = T_H + β·T_L1 + βγ·T_L2 (+ βγδ·T_L3)`  
    有效访问时间（两/三级）：`T_C = T_H + β·T_L1 + βγ·T_L2 (+ βγδ·T_L3)`  

(b) FP unit conflicts  
  （b）浮点单元冲突
- FP add/mul often 3-stage pipelines (one-per-cycle issue); FP div is long/rarely pipelined.  
  浮点加/乘常为 3 段流水（每拍一条）；浮点除延迟长，通常不深度流水。  
- **Bypass** cuts dependency waits; combine with cache/branch bypass to reduce bubbles.  
  **旁路**可降低依赖等待；与缓存/分支旁路结合进一步降泡。  

```
FP pipeline (3 stages), issue every cycle
IF  D  EX1 EX2 EX3 MA  S
    IF  D  EX1 EX2 EX3 MA  S
        IF  D  EX1 EX2 EX3 MA  S
```

### 3) Out-of-Order (OoO) Execution / 乱実行
- Idea: later independent ops may start/finish before earlier ones → higher throughput.  
  思想：无依赖的后继指令可先于先行启动/完成 → 提升吞吐。  
- Early issue: imprecise exceptions (earlier fault but later already committed).  
  早期问题：**非精确异常**（先行已出错但后继已提交）。  
- Fix: **ROB + renaming** so retirement is in-order to guarantee precise exceptions.  
  解决：使用**ROB + 寄存器改名**，按取指顺序提交，保证**精确异常**。  

```
In-Order（顺序执行）
队列: [1][2][3][4][5] → ①②③④⑤ 依次完成

OoO（乱実行）
队列: [1][2][3][4][5] → 同时发射；可能③④⑤①②次序完成
提交（ROB尾部提交）仍按 1,2,3,4,5 顺序写回，错则回滚
```

---

### 4) Speculative Execution & Rollback / 投机执行与回滚
- Predict branch and execute along the likely path; keep results in ROB until validated.  
  预测分支并沿可能路径执行；在验证前结果暂存于 ROB。  
- Mispredict/exception → rollback to the branch/fault point; discard younger results.  
  误判/异常 → 回滚至分支/故障点；丢弃更“年轻”的结果。  
- Mechanisms: ROB checkpoints, rename-map snapshots to restore architectural state.  
  机制：ROB 检查点、改名映射快照以恢复体系结构状态。  
- 
### 5) Superscalar & Deep Pipelines / 多发射与深流水
(a) Superscalar (2–4 issue common)  
  （a）超标量（常见 2–4 发射）
- Fetch/decode multiple instructions per cycle; multiple ALUs/LSUs run in parallel.  
  每拍取/译多条；多套 ALU/LSU 并行执行。  

(b) Deep pipelines  
  （b）深流水
- Split 5 stages into ~10 to raise frequency; commercial deepest ~31; modern ~14–15.  
  将 5 段细分至 ~10 段以抬频；最深商用约 31 段；现代常 ~14–15 段。  
- Cost: larger branch penalties; more complex bypass/timing.  
  代价：更大的分支惩罚；旁路与时序更复杂。
  
```
5-stage (shallow)           10-stage (deep, ~2x freq)
IF  D  EX  MA  S            IF1 IF2 D1 D2 EX1 EX2 MA1 MA2 S1 S2
```

### 6) Worked Example: E = (A+B)×(C+D) / 例题：流水化收益
- **No pipeline** (IF/ID/EX/MA/S each 1 cycle; memory 2 cycles) → ≈37 cycles  
  **无流水**（取/译/算/存各 1 拍；访存 2 拍）→ 约 37 周期  
- **Basic pipeline** (no bypass) → ≈20 cycles  
  **基本流水**（无旁路）→ 约 20 周期  
- **Compiler reordering** (increase distance) → ≈18 cycles  
  **编译器重排**（拉开依赖距离）→ 约 18 周期  
- **With bypass** (load/ALU/store) → ≈14 cycles  
  **开启旁路**（load/ALU/store）→ 约 14 周期  
- **Superscalar 2-way** → ≈11 cycles  
  **双发射超标量** → 约 11 周期
  
```
No-bypass schedule (excerpt)
LOAD A     IF D EX MA S
LOAD B        IF D EX MA S
ADD R1,R1,R2     IF - - EX MA S     ← 依赖等待 → 泡
...
With bypass: values can be forwarded earlier; fewer bubbles; 2-issue adds parallelism
有旁路后：依赖值可提前转发，气泡更少；双发射进一步并行
```

### 7) From ILP to Thread/Core / 从指令级并行到线程/多核
- ILP ceilings: limited independent ops; cache/wire delays; diminishing returns for deep pipelines.  
  ILP 瓶颈：可独立指令有限；缓存/连线延迟显性化；深流水边际收益递减。  
- Power: dynamic power ∝ `f·V²`; voltage scaling stalls while leakage rises.  
  功耗：动态功耗 ∝ `f·V²`；电压难再降同时漏电上升。  
- Roadmap: multithreading/multicore, smarter memory hierarchy, stronger prediction/rollback, wider vectors/accelerators.  
  路线：多线程/多核、更聪明的存储层次、更强的预测/回滚、更宽的向量与加速器。  

---
### Key Points
- OoO + speculation + bypass + multi-level caches together mitigate data/control/resource hazards.  
  乱序 + 投机 + 旁路 + 多级缓存共同缓解数据/控制/资源三类风险。  
- **ROB + renaming** ensures precise exceptions/rollback; deep pipelines & superscalar increase freq/parallelism but magnify branch/memory penalties.  
  **ROB + 改名**提供精确异常与回滚；深流水/超标量提升频率与并行，但放大分支与访存惩罚。  
- Real performance depends on: hit rates, branch accuracy, dependency distance, structural bandwidth, and scheduling quality.  
  实际性能取决于：命中率、分支准确率、依赖距离、结构带宽与调度质量。  

<h2></h2>

[← Previous Lecture / 上一章](./Lecture12.md) · [← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 12: Speeding Up the Control Unit — Pipelines & Branch Prediction  
# 第12回：制御装置の高速化 — 命令パイプライン与分岐预测  
Improving a 5-stage DLX pipeline (IF/ID/EX/MEM/WB), CPI/IPC, hazards (data/control/resource), bypassing/forwarding, load/store/branch bypass, branch prediction (local/global/hybrid; 1-bit/2-bit; two-level; gshare/GAs/PAs; perceptron/TAGE)
  覆盖 DLX 五段流水线（IF/ID/EX/MEM/WB）、CPI/IPC、数据/控制/资源相关、旁路/转发、加载/存储/分支旁路，以及分支预测（局部/全局/混合；1 位/2 位；两级；gshare/GAs/PAs；感知器/TAGE）。

---

## ⚪ Lecture Overview
- **Pipeline = assembly line**; overlap stages to approach **CPI≈1** / **IPC≈1**.
  **流水线**好比“装配线”，让各阶段重叠运行，理想情况下 **CPI≈1** / **IPC≈1**。
- **DLX 5-stage**: IF (fetch), ID (decode), EX (execute/EA calc), MEM (access), WB (writeback).
  **DLX 五段**：IF 取指、ID 译码、EX 执行/有效地址计算、MEM 访存、WB 回写。
- **Hazards / 乱れ要因**: data dependency, control dependency, resource conflict → bubbles/stalls.
  **数据相关/控制相关/资源冲突**会引入“气泡/停顿”，降低吞吐。
- **Acceleration / 高速化**: operand/load/store/branch **bypass**; **branch prediction** (local/global/hybrid; one-/two-level).
  **加速手段**：操作数/加载/存储/分支**旁路（转发）**；以及**分支预测**（局部/全局/混合；一级/二级）【通过**旁路/转发**与**分岐预测**减少停顿与分支惩罚。】。
  
---

## 1) Pipeline Principle / 流水线原理
- **Clocked synchronous** execution; e.g., **1 GHz → 1 ns/cycle**; one instruction takes ~5 cycles but overlaps.  
  **时钟同步**：如 **1 GHz=1 ns/周期**；单条指令历经约5个阶段，但多条可**重叠**执行。
**5-stage timeline / 五段时间线（示意）**
```
Inst1: IF ID EX MEM WB
Inst2: IF ID EX MEM WB
Inst3: IF ID EX MEM WB
Inst4: IF ID EX MEM WB
```
> Ideal CPI≈1; **No Operation (NOP)** fills bubbles when hazards stall.  
> 理想 CPI≈1；发生停顿时用 **NOP** 填充气泡。 
---

## 2) Model ISA & Stage Work / 模型指令集与阶段职责
- **ALU**: `Rd ← Rs1 op Rs2`
  **算术逻辑**：`Rd ← Rs1 op Rs2`
- **Load/Store**: absolute `M(D)` or indexed `M(R15+D)`
  **加载/存储**：绝对寻址 `M(D)` 或索引寻址 `M(R15+D)`
- **Branch**: `BRU/BRCC` with condition codes **Z/N/V/C**; `BAL/RTN` for calls/returns.
  **分支**：带条件码 **Z/N/V/C** 的 `BRU/BRCC`；调用/返回使用 `BAL/RTN`。
- **Stage roles / 阶段职责**
  **阶段职责**
  - **IF**: fetch instruction
    **IF**：取指
  - **ID**: decode & read CC/regs
    **ID**：译码并读取条件码/寄存器
  - **EX**: ALU or effective-address calc
    **EX**：ALU 运算或有效地址计算
  - **MEM (MA)**: cache/memory access (ALU/BR idle here)
    **MEM（MA）**：缓存/内存访问（算术/分支在此阶段空转）
  - **WB (S)**: writeback & finish
    **WB（S）**：回写并结束
---

## 3) Hazards / 乱れ与停顿
### (a) Data dependence / 数据相关
- **ALU-use** wait → typically **2-cycle bubble** without forwarding.  
  算术结果未就绪会导致**约2周期气泡**。【**ALU→下条使用**在无转发时通常要**等 2 个周期**。】
- **Load-use** wait → load result available after MEM → **2-cycle bubble**常见。  
  加载后使用通常也会**插入2周期**。【**加载→使用**结果在 MEM 阶段后才可用，常见**约 2 周期气泡**。】

### (b) Control dependence / 控制相关
- Conditional branch resolves later → naive causes **~4-cycle bubble**.
  条件分支较晚决策；朴素实现可能插入**≈4 个周期**的停顿。

### (c) Resource conflict / 资源冲突
- **Cache miss**: cache≈1 cycle vs main memory≈**~100 cycles** → long bubble.
  **缓存未命中**：缓存≈1 周期而主存≈**~100 周期**，导致长气泡。
- **Long-latency unit** (e.g., FP) with single unit stalls followers.
  **长延迟功能单元**（如浮点）若仅一台，会阻塞后续指令。

---

## 4) Bypassing / 转发与旁路
- **ALU bypass**: forward EX result to next ID/EX → ALU-use bubble ↓ from 2 → **1 or 0**.
  **ALU 旁路**：把 EX 结果直接送到下一条的 ID/EX，等待从 2 个周期降到 **1 或 0**。
- **Load bypass**: forward MEM-read data earlier → shrink load-use bubble.
  **加载旁路**：更早转发 MEM 读到的数据，缩短加载-使用停顿。
- **Store bypass**: overlap EA (address) & ED (data) paths; avoid serial EA→ED stalls.
  **存储旁路**：并行地址计算（EA）与写数据（ED）通路，避免串行等待。
- **Branch bypass**: notify IF earlier once branch resolves → penalty ~4 → **~2 cycles**.
  **分支旁路**：分支一旦判定，尽早通知 IF，惩罚由 ~4 周期降至 **~2 周期**。

> Combined ALU/Load/Store/Branch bypass further compresses bubbles.
  多种旁路组合能进一步压缩气泡。

---

## 5) Branch Prediction / 分岐预测
**Why / 为什么**  
- Deep pipelines & high clocks amplify branch penalty; prediction feeds likely path into IF.
  深流水与高频率放大分支惩罚；预测使 IF 预取“更可能正确”的路径。
**Simple / 简单策略**  
- **Predict Not-Taken** (historically common; loops often Taken → poor).
  **预测不跳转**（早期常见；循环多为跳转 → 效果差）。 
- Bias-aware programming or opcodes (`BRCC T Z` vs `BRCC F Z`) seen in old ISAs.  
  旧机型甚至提供显式“预测真/假”的变体。【  某些 ISA 提供偏置提示或用法约定。】

**1-level predictors / 一级预测（状态机FSM）**  
- **1-bit counter**: last outcome = next prediction; flips on TFTF… patterns.
  **1 位计数器**：以上次结果预测下次；在 **TFTF…** 模式易抖动。
- **2-bit saturating counter**: four states; tolerates one misdirection.
  **2 位饱和计数器**：四状态机；可容忍一次反向。
  > Example classroom figures: **1-bit≈10% → 2-bit≈4% → advanced≈2%** mispredict (illustrative).
    课堂示意：**1 位≈10% → 2 位≈4% → 更高级≈2%** 误判率（近似级别，仅作说明）。

**2-level adaptive / 二级自适应**
- **Local**: index by that branch’s own history bits.
  **局部**：按**该分支自身**的历史比特选择预测器。
- **Global**: index by global history register (GHR).
  **全局**：按**全局分支历史**寄存器（GHR）索引预测表。
- **Hybrid**: local+global with a chooser (e.g., Alpha 21264).
  **混合**：局部+全局，由选择器仲裁（如 Alpha 21264）。
- Representatives: **gshare / GAs / PAs**; newer: **Perceptron / TAGE**.
  代表：**gshare（全局）/ GAs（全局）/ PAs（局部）**；新方法：**Perceptron / TAGE**。

> Outcome: fewer flushes & stalls; cost is area/energy/complexity.
  效果：减少回滚与停顿；代价是面积/能耗/复杂性上升。【降低**控制相关**的停顿，提升吞吐；代价是结构与能耗复杂度上升。】 

---

## 6) Putting It Together / 端到端优化
- **Caches + TLB** cut memory time; **bypass** narrows producer→consumer latency; **prediction** hides control stalls.
  **缓存 + TLB** 降低访存时间；**旁路**缓解生成-使用时距；**预测**隐藏控制停顿。
- **Superscalar / OoO / Speculation** collaborate with pipelines to extract more ILP.
  **超标量/乱序/投机**在更高阶处理器中发射多指令、乱序执行、投机提交与流水线协同进一步榨取并行性。

---

##  Mini Walk-through / 小例：分支惩罚如何缩短
```
; naive (no bypass, no prediction)
IF D EX MA S

IF D EX MA S

IF D EX MA S

IF D EX MA S ; BR resolves late → ~4 bubbles

; with branch bypass + predict-not-taken
IF D EX MA S

IF D EX MA S

IF D EX MA S ; notify IF earlier → ~2 bubbles
```
> Actual numbers vary with depth/resolve point; BTB and I$ streaming also help.
  实际效果依流水深度/判定点而异；实机还会结合 I$ 线性批量取指与目标缓冲（BTB）。 

---

##  Key Points
- **5-stage pipeline** improves throughput; ideal **CPI≈1** depends on removing stalls.
  **五段流水线**提升吞吐；**CPI≈1** 取决于消除停顿。
- **Hazards**: data/control/resource; cache and unit latency set bubble length.
  **三类乱源**：数据/控制/资源；缓存与功能单元延迟决定气泡长度。
- **Bypassing** cuts ALU/Load/Store waits; **branch bypass** shortens branch penalty.
  **旁路**减少 ALU/加载/存储等待；**分支旁路**缩短分支惩罚。
- **Branch prediction**: from simple to two-level/hybrid (gshare/GAs/PAs/Perceptron/TAGE) lowers mispredicts.
  **分支预测**从简单到二级/混合（gshare/GAs/PAs/Perceptron/TAGE）显著降低误判。

---
## ※※ Supplementary Notes (Lecture 12)  
- [1-bit vs 2-bit Saturating Counter FSM](./figs/lecture12_branch_counter_fsm.md)
  [1 位 vs 2 位饱和计数器状态机](./figs/lecture12_branch_counter_fsm.md)
- [Two-level Branch Predictors](./figs/lecture12_two_level_predictors.md)
  [二级分支预测器](./figs/lecture12_two_level_predictors.md)

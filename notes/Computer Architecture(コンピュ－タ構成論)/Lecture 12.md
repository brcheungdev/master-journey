#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 12: Speeding Up the Control Unit — Pipelines & Branch Prediction  
# 第12回：制御装置の高速化 — 命令パイプライン与分岐预测  
5-stage DLX pipeline (IF/ID/EX/MEM/WB), CPI/IPC, hazards (data/control/resource), bypassing/forwarding, load/store/branch bypass, branch prediction (local/global/hybrid; 1-bit/2-bit; two-level; gshare/GAs/PAs; perceptron/TAGE)

---

## ⚪ Lecture Overview
- **Pipeline = assembly line**; overlap stages to approach **CPI≈1** / **IPC≈1**.  
  **流水线**像“流动生产线”，将取指/译码/执行/存取/回写重叠，理想达到 **CPI≈1** / **IPC≈1**。 
- **DLX 5-stage**: IF (fetch), ID (decode), EX (execute/EA calc), MEM (access), WB (writeback).  
  **DLX 五段**：取指IF、译码ID、执行/地址计算EX、访存MEM、回写WB。  
- **Hazards / 乱れ要因**: data dependency, control dependency, resource conflict → bubbles/stalls.  
  **数据/控制/资源**相关会插入“气泡/停顿”，降低吞吐。
- **Acceleration / 高速化**: operand/load/store/branch **bypass**; **branch prediction** (local/global/hybrid; one-/two-level).  
  通过**旁路/转发**与**分岐预测**减少停顿与分支惩罚。
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

## 2) Model ISA & Stage Work / 模型指令集与阶段工作
- **ALU**: `Rd ← Rs1 op Rs2`  
- **Load/Store**: absolute `M(D)` or indexed `M(R15+D)`  
- **Branch**: `BRU/BRCC` with condition codes **Z/N/V/C**; `BAL/RTN` for calls/returns.  
- **Stage roles / 阶段职责**  
  - **IF**: fetch instruction / 取指  
  - **ID**: decode & read CC/regs / 译码与读寄存器/条件码  
  - **EX**: ALU or effective-address calc / 执行或地址计算  
  - **MEM (MA)**: cache/memory access (ALU/BR → NOP) / 访存（算术/分支此阶段空转）  
  - **WB (S)**: writeback & finish / 回写与结束 
---

## 3) Hazards / 乱れ与停顿
### (a) Data dependence / 数据相关
- **ALU-use** wait → typically **2-cycle bubble** without forwarding.  
  算术结果未就绪会导致**约2周期气泡**。  
- **Load-use** wait → load result available after MEM → **2-cycle bubble**常见。  
  加载后使用通常也会**插入2周期**。

### (b) Control dependence / 控制相关
- Conditional branch resolves later → naive causes **~4-cycle bubble**.  
  条件分支晚决策，天真实现可致**约4周期**停顿。

### (c) Resource conflict / 资源争用
- **Cache miss**: cache≈1 cycle vs main memory≈**~100 cycles** → long bubble.  
  **缓存未命中**可能带来**约100周期**级别停顿。  
- **Long-latency unit** (e.g., FP) with single functional unit stalls followers.  
  **长延时运算器**（如浮点）且仅一台，会阻塞后续。

---

## 4) Bypassing / 转发与旁路
- **ALU bypass / 演算器旁路**: forward EX result to next ID/EX → ALU-use bubble ↓ from 2 → **1 or 0**.  
  将EX结果直接转发到后续使用，减少/消除等待。  
- **Load bypass / 读旁路**: forward MEM data earlier → load-use bubble ↓。  
  尽早转发MEM读取值，降低加载-使用停顿。  
- **Store bypass / 写旁路**: overlap EA (address) & ED (data) paths; avoid sequential EA→ED stalls。  
  将**地址计算EA**与**写数据访问ED**合理并行/旁路，减少顺序依赖。  
- **Branch bypass / 分岐旁路**: notify IF earlier once branch resolves → branch penalty 4 → **~2 cycles**。  
  分支一旦判定，尽早通知IF，缩短分支惩罚。 
> Combined schemes (**load/store/ALU bypass**) further cut bubbles.  
> 旁路组合可进一步压缩气泡。

---

## 5) Branch Prediction / 分岐预测
**Why / 为什么**  
- Deep pipelines & high clocks amplify branch penalty; prediction feeds likely path into IF.  
  深流水与高频使分支惩罚更显著，预测让IF提前取“可能正确”的路径。
**Simple / 简单策略**  
- **Predict Not-Taken / 预测不跳转**（历史机器常用；循环多“Taken”会差）。  
- Bias-aware programming or opcodes (`BRCC T Z` vs `BRCC F Z`) seen in old ISAs.  
  旧机型甚至提供显式“预测真/假”的变体。

**1-level predictors / 一级预测（状态机）**  
- **1-bit counter**：上次行为即下次预测；易在“TFTF…”模式中抖动。  
- **2-bit saturating counter**：四状态机，容错一次反向。  
  > 常见误判率示意：**1-bit≈10% → 2-bit≈4% → 更高级≈2%**（教材示例级别）。 

**2-level adaptive / 二级自适应**  
- **Local / 局部**：按**该分支自身**的历史比特串选择预测器。  
- **Global / 大域**：按**全局分支历史**（GHR）索引预测表。  
- **Hybrid / 混合**：本地+全局由选择器仲裁（如 Alpha 21264）。  
- 代表：**gshare（全局）/ GAs（全局）/ PAs（局部）**；新方法：**Perceptron / TAGE**。 

> Outcome / 结果：降低**控制相关**的停顿，提升吞吐；代价是结构与能耗复杂度上升。  
> 通过更精确预测减少冲刷/回退。 

---

## 6) Putting It Together / 端到端优化
- **Caches + TLB** reduce average MEM time; **bypass** handles producer→consumer latency; **prediction** hides control stalls.  
  缓存/地址翻译降低访存延迟；旁路缓解生成-使用时距；预测隐藏控制停顿。  
- **Superscalar / OoO / Speculation**（提要）：发射多指令、乱序执行、投机提交，进一步榨取并行性。  
  **超标量/乱序/投机**在更高阶处理器中与流水线协同。 

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
> 实际效果依流水深度/判定点而异。  
> 实机还会结合 I$ 线性批量取指与目标缓冲（BTB）。 

---

##  Key Points 
- **5-stage pipeline** improves throughput; ideal **CPI≈1** depends on removing stalls.  
  五段流水提升吞吐，理想 CPI 取决于停顿控制。
- **Hazards**：数据/控制/资源三类；缓存与功能部件延迟决定气泡长短。  
  三大乱源需要结构/策略配合缓解。
- **Bypassing** cuts ALU/Load/Store waits; **branch bypass**缩短分支惩罚。  
  旁路/转发是应对近距离依赖的关键。 
- **Branch prediction**：从简单到二级自适应/混合（gshare/GAs/PAs/Perceptron/TAGE），误判率显著下降。  
  分岐预测是现代高性能流水线不可或缺的组成。

---
## ※※ Supplementary Notes (Lecture 12)  
- [1-bit vs 2-bit Saturating Counter FSM](./figs/lecture12_branch_counter_fsm.md)  
- [CSMA/CD Operation Flow & Timing](./figs/lecture05_csma_cd_flow.md)


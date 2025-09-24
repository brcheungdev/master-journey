#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 13: Control-Unit Speedup (2) — Hazards, OoO, Speculation, Superscalar, Deep Pipelines  
# 第13回：制御装置の高速化（その2）— 乱実行・投機実行・スーパスカラ・ディープパイプライン

---

## ⚪ Lecture Overview / 课程概览
- **Pipeline hazards**: data / control / resource（数据/控制/资源相关）  
- **Resource conflicts**: cache misses, long-latency FP units → bubbles/stalls（缓存未命中/浮点长延迟导致停顿）  
- **Mitigations**: multi-level caches, bypassing, FP pipelines（多级缓存/旁路/浮点流水线）  
- **Out-of-Order (OoO)** execution & **Speculation** with rollback（乱実行与投机回滚）  
- **Reorder Buffer (ROB)** & **Register Renaming**（重排序缓冲与寄存器改名）  
- **Superscalar** multi-issue & **Deep pipelines**（多发射与深流水）  
- ILP limits → **multithreading/multicore**（从指令级并行转向线程/多核）

---

### 1) Hazards & Dependencies / 乱れ要因与依存关系
- **Data dependence**（数据相关）会阻塞后继指令；无旁路时易插入多个气泡。  
- **Control dependence**（控制相关）来自分支/异常的下一步不确定。  
- **Resource conflict**（资源竞争）如只有1台浮点单元或 cache miss。  

```
Example timeline (long FP op blocks follower)
先行  IF  D  EX  EX  EX  MA  S
后继  IF  -  -  EX  EX  EX  MA  S     ← 无独立资源 → 插入2个bubble
```
### 2) Resource Conflicts → Speedups / 资源冲突与加速手段
(a) Multi-level caches（多级缓存分层）
- 典型配置（Intel i7-6700）示意：L1=64KB, L2=256KB, L3=8MB
- 访问代价（相对 L1 命中延迟 T_H）：T_L1≈12·T_H, T_L2≈44·T_H, T_L3≈70·T_H
- 命中/失配率示例：β=0.0271, βγ=0.0089（逐级失配）
  - 有效访存时间（两/三级）可按 T_C = T_H + β·T_L1 + βγ·T_L2 (+ βγδ·T_L3) 粗略估计
(b) FP unit conflicts（浮点运算资源冲突
- FP add/mul 常做 3段流水，可“每拍进一条”；FP div 低频，常不做深流水。
- Bypass（转发）可减少依赖等待；与 cache/分支旁路配合进一步降泡。

```
FP pipeline (3 stages), issue every cycle
IF  D  EX1 EX2 EX3 MA  S
    IF  D  EX1 EX2 EX3 MA  S
        IF  D  EX1 EX2 EX3 MA  S
```

### 3) Out-of-Order (OoO) Execution / 乱実行
- 思想：无依赖的后继指令可先于先行指令启动/完成，提高吞吐。
- 早期问题：不精确中断（先行抛错而后继已提交）
- 解决：重排序缓冲(ROB) + 寄存器改名，以取指顺序提交，保证精确异常。

```
In-Order（顺序执行）
队列: [1][2][3][4][5] → ①②③④⑤ 依次完成

OoO（乱実行）
队列: [1][2][3][4][5] → 同时发射；可能③④⑤①②次序完成
提交（ROB尾部提交）仍按 1,2,3,4,5 顺序写回，错则回滚
```
### 4) Speculative Execution & Rollback / 投机执行与回滚
- 分支命中：沿预测路径执行并在 ROB 中暂存结果；命中即正常提交。
- 分支失误/异常：从 分支点/出错点 回滚，丢弃之后的未提交结果。
- 回滚机制示例：ROB法、Register Renaming法（保存快照/映射以恢复状态）。
- 
### 5) Superscalar & Deep Pipelines / 多发射与深流水
(a) Superscalar（2~4发射常见）
- 同时取/译多条指令；多套 ALU / LSU 并行执行。
(b) Deep pipelines（深流水）
- 将5段细分为10段以提高频率：最深商用达 31 段；现代常 14~15 段。
- 代价：分支惩罚、旁路/时序复杂度更高。
```
5-stage (shallow)           10-stage (deep, ~2x freq)
IF  D  EX  MA  S            IF1 IF2 D1 D2 EX1 EX2 MA1 MA2 S1 S2
```

### 6) Worked Example: E = (A+B)×(C+D) / 例题：流水化收益
**无流水**（取/译/算/存各1拍，访存2拍） → ≈37 cycles
**基本流水**（无旁路） → ≈20 cycles
**编译器重排**（拉开依赖） → ≈18 cycles
**有旁路**（load/ALU/store bypass） → ≈14 cycles
**双发射** Superscalar（2-way） → ≈11 cycles
```
No-bypass schedule (excerpt)
LOAD A     IF D EX MA S
LOAD B        IF D EX MA S
ADD R1,R1,R2     IF - - EX MA S     ← 依赖等待 → 泡
...
With bypass: 依赖值可提前转发，少插泡；2-issue 再并行
```

### 7) From ILP to Thread/Core / 从指令级并行到线程/多核
- ILP瓶颈：可并行指令不多、cache/布线延迟显性化、深流水边际收益低。
- 功耗限制：动态功耗 ∝ f·V²，电压难降（漏电上升）。
- 路线：多线程/多核、更聪明的存储层次、更强预测/回滚、更大向量化/加速器。

---
### Key Points
- 乱実行 + 投機 + 旁路 + 多级缓存：共同缓解 数据/控制/资源 三类乱れ
- **ROB+改名** 提供精确异常与回滚；深流水/多发射带来频率与并行，但也放大分支/访存惩罚
- 实际性能取决于：命中率、分支准确率、依赖距离、结构带宽与调度质量

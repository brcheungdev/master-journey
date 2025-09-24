#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 10: History of Computers & Instruction Set Styles
Stored-program concept, ENIAC/EDSAC, microprocessor evolution, memory & endianness, instruction formats, stack machines, CISC vs RISC, system hierarchy, analog vs digital, non-von-Neumann
<br/>
存储程序概念、ENIAC/EDSAC、微处理器的发展、内存与字节序、指令格式、栈式机器、CISC 与 RISC、系统层次结构、模拟与数字、非冯·诺依曼结构
---

## ⚪ Lecture Overview 
- **Stored-program** model & its characteristics vs. **wired programming**  
  存储程序模型及其特点与有线编程模型的对比  
- Historical machines: **ENIAC** (1946), **EDSAC** (1949)  
  历史上的计算机：ENIAC（1946 年），EDSAC（1949 年）  
- **Memory addressing**, **linear vs associative**, **little/big endian**  
  内存寻址、线性寻址与关联寻址、小端序与大端序  
- **Clocked synchronous** execution & (intro to) **pipelining**  
  时钟同步执行及流水线技术入门  
- Instruction formats: **3-addr / 2-addr / 1-addr / 0-addr (stack)**  
  指令格式：三址指令 / 二址指令 / 一址指令 / 无址指令（栈式）  
- **CISC vs RISC** ideas & examples  
  CISC 与 RISC 的理念及示例  
- Evolution: **Intel 4004 → 8086 → 80386 → Pentium 4 → Core i7 → Apple M1**  
  发展历程：英特尔 4004 → 8086 → 80386 → 奔腾 4 → 酷睿 i7 → 苹果 M1  
- Performance & parallelism trends; **Fugaku** supercomputer  
  性能与并行性趋势；富岳超级计算机  
- **System hierarchy**; **analog vs digital**; **non-von-Neumann**  
  系统层次结构；模拟与数字；非冯·诺依曼结构  

---

## ⚪ Lecture Content 讲座内容

### 1) Stored-Program Computers  程序内置方式
- **Definition**: program (instructions + data) is stored in main memory; CPU executes **one instruction at a time** referenced by **PC**.  
- **Key characteristics**  
  1) **Sequential control** by PC（与“数据驱动”对比）  
  2) **Clock-synchronous** execution（按节拍推进）  
  3) **Low-level, fast** instructions with wide applicability  
  4) **Linear memory** suits sequential control  
  5) **Binary** representation  
- **Why it persisted**: backward **compatibility** (IBM/360 1964, Intel 8086 1978, IA-32/80386 1985), **semiconductor advances**, and **architectural simplicity**. 
---

### 2) Wired Programming vs Stored-Program  接线式 vs 程序内置
- **Wired (Plug-board)**: 手动布线数据与控制脉冲（例：计算  E=(A+B)×(C+D)  要通过开关与线缆连接加/乘单元及显示），更改“程序”=重新布线。  
- **Stored**: 以**电子速度**装/改程序与数据，易于复用与扩展。 
---

### 3) ENIAC (1946)  概览
- ~**17,468 真空管**, 7,200 二极管, 1,500 继电器, 70,000 电阻, 10,000 电容；约 **30 m × 2.4 m × 0.9 m**, **27 吨**, **150 kW**。  
- **十进制** 10 位环形计数器；**10 的补数**表示（符号位 0 正 / 9 负）；I/O 采用打孔卡与打印。  
- 约 **5,000 次/s** 加/减，**385 次/s** 乘，**40 次/s** 除；时钟 **100 kHz**（加法 ~20 周期≈200 μs）。  
- 以**程序盘/线路**组织：可实现**循环、分支、子程序**，但**非存储程序机**。

---

### 4) EDSAC (1949, Cambridge)  
- **Mercury delay-line memory**；**17-bit word**, **1,024 words**；同步 500 kHz；加/减 ~1.5 ms；乘 ~6 ms。  
- 指令 **17 位**：**5-bit opcode + 10-bit address + 1-bit operand-length + 1 保留**；初期**无无条件分支/子程序调用**。  
- **71-bit accumulator**, 35-bit multiplier register；最初**无索引寄存器**（后由 D. Wheeler 加入）；**二补数**表示。  
- I/O：纸带 / 电传打字机。常见指令：**A/S/H/V/N/T/U/C/R/L/E/G/I/O/F/Y/Z**（加/减/乘寄存器搬运/乘加/乘减/存储/与/移位/条件跳转/IO/停止等）。

---

### 5) Memory, Addressing & Endianness  存储与寻址
- **Byte addressing**；例：**1 MB** 需 **20-bit** 地址，十六进制 5 位 `00000–FFFFF`。  
- **R/W** 术语：**Load**（读）/**Store**（写）。  
- **Endianness**：**Little-endian** vs **Big-endian**（多字节整数在内存的高/低位顺序）。  
- **Linear vs Associative** memory：按地址访问 vs 按**内容匹配**返回地址。{index=5}

---

### 6) Clocked Execution & Pipelining  同步与流水线
- 典型阶段：**取指 → 译码 → 访存/执行 → 回写/结束**。  
- 示例：**1 GHz** 时钟，**1 ns**/周期；指令执行可为 **4–5 阶段**。流水化后同一时刻多条指令**分布在不同阶段**。 

---

### 7) Instruction Formats  指令格式总览
- **3-address**：`Md ← Ms1 op Ms2`  
- **2-address**：`Md ← Md op Ms`  
- **1-address**：  
  - **Accumulator**：`ACC ← ACC op Ms`  
  - **Register-Memory**：`Rd ← Rd op Ms` / `Md ← Rs`  
  - **Load-Store**：`Rd ← Rs1 op Rs2`；`Rd ← Ms` / `Md ← Rs`  
- **0-address (Stack)**：`PUSH Ms`, `OP`（对栈顶/次顶），`POP Md`。  
- 真实系统案例：**VAX-11/780 (3-addr)**、**IBM 360/Intel 80386 (1-addr, reg-mem)**、**MIPS/ SPARC (load-store)**、**Burroughs 5000 / Java VM (0-addr)**。

---

### 8) Stack Machines & Polish Notation  栈机与波兰/逆波兰
- **LIFO 栈**：表达式求值常用。  
- **中缀 → 逆波兰**：`(2+3)*(4+5)` → `23+45+*`。  
- 计算流程：读到数则 **PUSH**；读到运算符则对 **栈顶两数**运算并 **PUSH 结果**。 

---

### 9) CISC vs RISC  复杂/精简指令集
- **CISC**：可变长，多寻址方式，复杂指令（例：**VAX**）。  
- **RISC**：**固定长、少寻址、硬布线控制、Load-Store、寄存器多**；强调编译器优化与芯片资源（寄存器/Cache）。  
- RISC 系谱：**IBM 801 (John Cocke)**、**Berkeley RISC (Patterson)**、**MIPS (Hennessy)**、**SPARC**；现代 x86 亦大量采用 RISC-like 内核+译码前端。 

---

### 10) Microprocessor Evolution  微处理器演进
- **Intel 4004 (1971)**：**2,300** 晶体管，**750 kHz**，**4-bit**，16 寄存器，程序存储 4 KB，约 **0.07 MIPS**。  
- **8086 (1978)**：约 **29k** 晶体管，**8 MHz**，**16-bit**，20-bit 地址（1 MB）。  
- **80386 (1985)**：**32-bit**，分页支持，4 阶段流水。  
- **Pentium 4 (2000)**：**42M** 晶体管，**1.4 GHz**，NetBurst，超线程/多媒体 SIMD。  
- **Core i7 (2008)**：**731M** 晶体管，**3.2 GHz**，Nehalem，L1/L2/L3 多级缓存，4 核 8 线程。  
- **Apple M1 (2020)**：**5 nm**，**160 亿**晶体管，**8 CPU 核（4P+4E）**，大容量 L1/L2，**8-core GPU (~2.6 TFLOPS)**，**16-core Neural Engine**。

---

### 11) Performance & Parallelism  性能与并行
- **Instruction-level**：流水线、乱序、**推测执行**、**超标量**。  
- **Memory hierarchy**：多级 Cache + 主存；**局部性**驱动。  
- **Local parallel**：单芯片多核、SIMD/向量（**CRAY-1、GPU**）。  
- **Global parallel**：大规模并行（**Fugaku**），约 **0.4 EFLOPS**，内存 **32 GB × 153,600** 节点，功耗 **30–40 MW**。  
- 趋势：算力提升受制于**功耗**与**存储墙**，架构/软件协同优化更关键。 
---

### 12) System Hierarchy & Design Levels  系统层级
1) 应用层　2) 高级语言层　3) 机器指令层/OS　4) **寄存器传输**层  
5) **门电路逻辑**层　6) **器件（MOS/CMOS）**层  
- RT 层示例：`ADD R3,R1,R2` 的控制/数据通路；门级：与/或/非、**XOR**、触发器（亚稳态注意）；器件级：**MOS/CMOS** 反相/与非/或非实现。

---

### 13) Analog vs Digital；Non-von-Neumann  模式与新范式
- **Analog vs Digital**：采样定理（`Δt = 1/(2ν_M)`），A/D、D/A；模拟计算（运放/接线） vs 数字算法。  
- **Non-von-Neumann**：数据流、**神经网络**、**光/量子**计算（国内外研究机构、D-Wave 等）。 

---

## Key Points 
- **Stored-program + PC + clock** form the core abstraction of modern computers; linear memory and compatibility drive its persistence  
  **存储程序 + 程序计数器 + 时钟** 构成现代计算机的核心抽象；线性内存与兼容性推动其延续  
- **ENIAC/EDSAC** demonstrate the transition from wired programming to stored-program, from decimal to binary, from paper tape to electronic delay lines  
  **ENIAC/EDSAC** 展示了从接线式到存储程序、从十进制到二进制、从纸带到电子延时线的关键过渡  
- Understanding **addressing / endianness**, **synchronous / pipelining**, and the **instruction format** spectrum (3/2/1/0-addr)  
  理解 **寻址 / 端序**、**同步 / 流水线** 与 **指令格式** 光谱（3/2/1/0-addr）  
- **RISC vs CISC** is a design trade-off: simplified decoding / compiler optimization vs complex instructions / multiple addressing modes  
  **RISC vs CISC** 是设计取舍：简化译码 / 靠编译优化 vs 强指令 / 多寻址模式  
- Performance scaling: from **ILP** to **multicore / GPU / supercomputers**, power and memory hierarchy become bottlenecks  
  性能提升：从 **指令级并行 (ILP)** 到 **多核 / GPU / 超算**，功耗与存储层次成为瓶颈  
- Architecture & implementation layers: a unified top-down/bottom-up view from **RT → Gate → Device**  
  体系结构与实现层级：**寄存器传输级 → 门级 → 器件级** 的自上而下 / 自下而上的统一视角  



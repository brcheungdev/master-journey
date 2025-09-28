#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor: Prof. Shinji Tomita (富田眞治)  

---
# Lecture 10: History of Computers & Instruction Set Styles
Stored-program concept, ENIAC/EDSAC, microprocessor evolution, memory & endianness, instruction formats, stack machines, CISC vs RISC, system hierarchy, analog vs digital, non-von-Neumann
<br/>
存储程序概念、ENIAC/EDSAC、微处理器的发展、内存与字节序、指令格式、栈式机器、CISC 与 RISC、系统层次结构、模拟与数字、非冯·诺依曼结构
---

## ⚪ Lecture Overview 
- **Stored-program** model & its characteristics vs. **wired programming**  
  存储程序模型及其特点与**接线式编程**的对比  
- Historical machines: **ENIAC** (1946), **EDSAC** (1949)  
  历史机器：**ENIAC**（1946）、**EDSAC**（1949）  
- **Memory addressing**, **linear vs associative**, **little/big endian**  
  **内存寻址**、**线性 vs 关联寻址**、**小端/大端**  
- **Clocked synchronous** execution & (intro to) **pipelining**  
  **时钟同步**执行与（入门）**流水线**  
- Instruction formats: **3-addr / 2-addr / 1-addr / 0-addr (stack)**  
  指令格式：**三址 / 二址 / 一址 / 零址（栈式）**  
- **CISC vs RISC** ideas & examples  
  **CISC vs RISC** 的理念与示例  
- Evolution: **Intel 4004 → 8086 → 80386 → Pentium 4 → Core i7 → Apple M1**  
  处理器演进：**Intel 4004 → 8086 → 80386 → Pentium 4 → Core i7 → Apple M1**  
- Performance & parallelism trends; **Fugaku** supercomputer  
  性能与并行趋势；**富岳（Fugaku）**超级计算机  
- **System hierarchy**; **analog vs digital**; **non-von-Neumann**  
  **系统层次**；**模拟 vs 数字**；**非冯·诺依曼**  

---

## ⚪ Lecture Content 讲座内容

### 1) Stored-Program Computers  程序内置方式
- **Definition**: program (instructions + data) is stored in main memory; CPU executes **one instruction at a time** referenced by **PC**.  
  **定义**：程序（指令 + 数据）保存在主存中；CPU 依据**程序计数器（PC）**一次取出并执行**一条指令**。  
- **Key characteristics**  
  **关键特征**  
  1) **Sequential control** by PC (vs dataflow).  
     1）由 PC 实现**顺序控制**（对比数据驱动）。  
  2) **Clock-synchronous** execution (tick-by-tick).  
     2）**时钟同步**执行（按时钟节拍推进）。  
  3) **Low-level, fast** instructions with wide applicability.  
     3）**底层且快速**的指令，适用范围广。  
  4) **Linear memory** fits sequential control.  
     4）**线性内存**匹配顺序控制。  
  5) **Binary** representation.  
     5）**二进制**表示。  
- **Why it persisted**: backward **compatibility** (IBM/360 1964, Intel 8086 1978, IA-32/80386 1985), **semiconductor advances**, and **architectural simplicity**.  
  **为何长期占主导**：向后**兼容性**（IBM/360 1964、Intel 8086 1978、IA-32/80386 1985），**半导体进步**与**架构简洁性**。  
---

### 2) Wired Programming vs Stored-Program  接线式 vs 程序内置
- **Wired (Plug-board)**: manually route data and control pulses (e.g., computing `E=(A+B)*(C+D)` by wiring add/mul units and display); changing the “program” means rewiring.  
  **接线式（插线板）**：手动布线数据与控制脉冲（例：计算  E=(A+B)×(C+D)  要通过开关与线缆连接加/乘单元及显示），更改“程序”=重新布线。
- **Stored**: load/modify programs and data at **electronic speed**, easy reuse and expansion.  
  **程序内置**：以**电子速度**装载/修改程序与数据，易于复用且可扩展。  
---

### 3) ENIAC (1946)  概览
- ~**17,468 vacuum tubes**, 7,200 diodes, 1,500 relays, 70,000 resistors, 10,000 capacitors; about **30 m × 2.4 m × 0.9 m**, **27 tons**, **150 kW**.  
  约 **17,468 只真空管**、7,200 只二极管、1,500 个继电器、70,000 个电阻、10,000 个电容；体积约 **30 m × 2.4 m × 0.9 m**，**27 吨**，**150 kW**。  
- **Decimal** 10-digit ring counters; **10’s complement** (sign 0 positive / 9 negative); I/O via punched cards & printer.  
  **十进制** 10 位环形计数器；**十的补数**表示（符号位 0 正/9 负）；I/O 为打孔卡和打印机。  
- ~**5,000/s** add/sub, **385/s** mul, **40/s** div; clock **100 kHz** (add ~20 cycles ≈ 200 μs).  
  加/减约 **5,000 次/秒**，乘 **385 次/秒**，除 **40 次/秒**；时钟 **100 kHz**（加法约 20 周期≈200 μs）。  
- Organized by **program panels/wiring**: loops/branches/subroutines possible, but **not stored-program**.  
  通过**程序盘/连线**组织：可实现循环、分支、子程序，但**并非存储程序机**。  

---

### 4) EDSAC (1949, Cambridge)  
- **Mercury delay-line memory**; **17-bit word**, **1,024 words**; sync 500 kHz; add/sub ~1.5 ms; mul ~6 ms.  
  **水银延迟线存储**；**17 位字长**、**1,024 字**；同步 500 kHz；加/减约 1.5 ms；乘约 6 ms。  
- **17-bit instruction**: **5-bit opcode + 10-bit address + 1-bit operand-length + 1 reserved**; initially **no unconditional branch/call**.  
  **17 位指令**：**5 位操作码 + 10 位地址 + 1 位操作数长度 + 1 位保留**；最初期**无无条件分支/子程序调用**。  
- **71-bit accumulator**, 35-bit multiplier register; originally **no index register** (added by D. Wheeler); **two’s complement** arithmetic.  
  **71 位累加器**、35 位乘法寄存器；最初**无索引寄存器**（后由 D. Wheeler 加入）；**二补数**计算。  
- I/O: paper tape & teleprinter. Common mnemonics: **A/S/H/V/N/T/U/C/R/L/E/G/I/O/F/Y/Z**.  
  I/O：纸带/电传打字机。常见指令：**A/S/H/V/N/T/U/C/R/L/E/G/I/O/F/Y/Z**（加/减/乘寄存器搬运/乘加/乘减/存储/与/移位/条件跳转/IO/停止等）。 

---

### 5) Memory, Addressing & Endianness  存储与寻址
- **Byte addressing**; e.g., **1 MB** needs **20-bit** addresses (`00000–FFFFF` in hex).  
  **字节寻址**；例如 **1 MB** 需要 **20 位**地址（十六进制 `00000–FFFFF`）。  
- **R/W terms**: **Load** (read) / **Store** (write).  
  **读写术语**：**Load**（读）/ **Store**（写）。  
- **Endianness**: **Little-endian** vs **Big-endian** for multi-byte integers.  
  **端序**：多字节整数的**小端**与**大端**（多字节整数在内存的高/低位顺序）。  
- **Linear vs Associative** memory: by address vs by **content match**.  
  **线性 vs 关联**存储：按地址访问 vs 按**内容匹配**返回地址。

---

### 6) Clocked Execution & Pipelining  同步与流水线
- Typical stages: **Fetch → Decode → Mem/Execute → Writeback/End**.  
  典型阶段：**取指 → 译码 → 访存/执行 → 回写/结束**。  
- Example: **1 GHz** clock → **1 ns**/cycle; a 4–5 stage pipeline overlapps multiple instructions.  
  例：**1 GHz** 时钟 → **1 ns/周期**；**4–5 级**流水将多条指令**并行分布**在不同阶段。  

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

### 8) Stack Machines & Polish Notation  栈机与（逆）波兰式
- **LIFO stack** suits expression evaluation.  
  **后进先出（LIFO）栈**适合表达式求值。 
- **Infix → RPN**: `(2+3)*(4+5)` → `23+45+*`.  
  **中缀 → 逆波兰**：`(2+3)*(4+5)` → `23+45+*`。 
- Procedure: read numbers → **PUSH**; read operator → compute on top-2 → **PUSH result**.  
  计算流程：读到数字就 **PUSH**；读到运算符就对**栈顶两数**运算并 **PUSH 结果**。  

---

### 9) CISC vs RISC  复杂/精简指令集
- **CISC**: variable-length, many addressing modes, complex instructions (e.g., **VAX**).  
  **CISC**：可变长、寻址方式多、指令复杂（如 **VAX**）。  
- **RISC**: fixed-length, few modes, hardwired control, load-store, many registers; compiler-centric.  
  **RISC**：固定长、寻址少、硬布线控制、负载-存储、寄存器多；依赖编译器优化。  
- Lineage: **IBM 801 (Cocke)**, **Berkeley RISC (Patterson)**, **MIPS (Hennessy)**, **SPARC**; modern x86 uses RISC-like cores with a decode front-end.  
  系谱：**IBM 801（Cocke）**、**Berkeley RISC（Patterson）**、**MIPS（Hennessy）**、**SPARC**；现代 x86 采用 RISC-like 内核 + 译码前端。 

---

### 10) Microprocessor Evolution  微处理器演进
- **Intel 4004 (1971)**: **2,300** transistors, **750 kHz**, **4-bit**, 16 regs, 4 KB program store, ~**0.07 MIPS**.  
  **Intel 4004（1971）**：**2,300** 晶体管，**750 kHz**，**4 位**，16 个寄存器，4 KB 程序存储，约 **0.07 MIPS**。  
- **8086 (1978)**: ~**29k** transistors, **8 MHz**, **16-bit**, 20-bit addr (1 MB).  
  **8086（1978）**：约 **2.9 万**晶体管，**8 MHz**，**16 位**，20 位地址（1 MB）。  
- **80386 (1985)**: **32-bit**, paging, 4-stage pipeline.  
  **80386（1985）**：**32 位**，支持分页，4 级流水。  
- **Pentium 4 (2000)**: **42M** transistors, **1.4 GHz**, NetBurst, HT/SIMD.  
  **Pentium 4（2000）**：**4,200 万**晶体管，**1.4 GHz**，NetBurst，超线程/SIMD。  
- **Core i7 (2008)**: **731M** transistors, **3.2 GHz**, Nehalem, L1/L2/L3 caches, 4C/8T.  
  **Core i7（2008）**：**7.31 亿**晶体管，**3.2 GHz**，Nehalem，L1/L2/L3 多级缓存，4 核 8 线程。  
- **Apple M1 (2020)**: **5 nm**, **16B** transistors, **8 CPU cores (4P+4E)**, large L1/L2, **8-core GPU (~2.6 TFLOPS)**, **16-core Neural Engine**.  
  **Apple M1（2020）**：**5 nm**，**160 亿**晶体管，**8 核 CPU（4P+4E）**，大容量 L1/L2，**8 核 GPU（~2.6 TFLOPS）**，**16 核神经引擎**。  

---

### 11) Performance & Parallelism  性能与并行
- **Instruction-level**: pipelining, out-of-order, **speculation**, **superscalar**.  
  **指令级并行**：流水线、乱序、**推测执行**、**超标量**。  
- **Memory hierarchy**: multi-level caches + DRAM; **locality** matters.  
  **存储层次**：多级缓存 + 主存；**局部性**驱动至关重要。  
- **Local parallel**: multicore on-chip, SIMD/vector (**CRAY-1, GPU**).  
  **局部并行**：单芯片多核、SIMD/向量（**CRAY-1、GPU**）。  
- **Global parallel**: large-scale (e.g., **Fugaku**), ~**0.4 EFLOPS**, memory **32 GB × 153,600 nodes**, power **30–40 MW**.  
  **全局并行**：大规模并行（如 **富岳**），约 **0.4 EFLOPS**，内存 **32 GB × 153,600** 节点，功耗 **30–40 MW**。  
- Trend: compute limited by **power** & **memory wall**; co-design increasingly vital.  
  趋势：算力受制于**功耗**与**存储墙**，架构/软件协同优化愈发重要。
   
---

### 12) System Hierarchy & Design Levels  系统层级
1) Application  2) High-level Language  3) Machine/OS  4) **Register-Transfer (RT)**  
   1）应用层  2）高级语言层  3）机器指令层/操作系统  4）**寄存器传输层（RT）**  
5) **Gate/Logic**  6) **Device (MOS/CMOS)**  
   5）**门/逻辑层**  6）**器件层（MOS/CMOS）**  
- RT example: control/data path of `ADD R3,R1,R2`; gate level: AND/OR/NOT/**XOR**, flip-flops (metastability); device level: **MOS/CMOS** inverters/NAND/NOR.  
  RT 层示例：`ADD R3,R1,R2` 的控制/数据通路；门级：与/或/非/**异或**、触发器（注意亚稳态）；器件级：**MOS/CMOS** 反相器/NAND/NOR 实现。  

---

### 13) Analog vs Digital；Non-von-Neumann  模拟 vs 数字；非冯·诺依曼
- **Analog vs Digital**: sampling theorem (`Δt = 1/(2ν_M)`), A/D & D/A; analog computing (op-amps/wiring) vs digital algorithms.  
  **模拟 vs 数字**：采样定理（`Δt = 1/(2ν_M)`）、模数/数模；模拟计算（运放/接线）vs 数字算法。  
- **Non-von-Neumann**: dataflow, **neural**, **photonic/quantum** computing.  
  **非冯·诺依曼**：数据流、**神经网络**、**光/量子**计算（国内外研究机构、D-Wave 等）。。  

---

## Key Points 
- **Stored-program + PC + clock** form the core abstraction of modern computers; linear memory and compatibility drive its persistence  
  **存储程序 + PC + 时钟** 构成现代计算机的核心抽象；线性内存与兼容性促成其延续。
- **ENIAC/EDSAC** demonstrate the transition from wired programming to stored-program, from decimal to binary, from paper tape to electronic delay lines  
  **ENIAC/EDSAC** 展示了从接线式到存储程序、从十进制到二进制、从纸带到电子延时线的关键转变。 
- Understanding **addressing / endianness**, **synchronous / pipelining**, and the **instruction format** spectrum (3/2/1/0-addr)  
  掌握**寻址/端序**、**同步/流水线**以及 **3/2/1/0-址** 指令格式光谱。 
- **RISC vs CISC** is a design trade-off: simplified decoding / compiler optimization vs complex instructions / multiple addressing modes  
  **RISC vs CISC** 是译码简化与编译优化 vs 强指令与多寻址模式的权衡。  
- Performance scaling: from **ILP** to **multicore / GPU / supercomputers**, power and memory hierarchy become bottlenecks  
  性能提升：从 **指令级并行 (ILP)** 到 **多核 / GPU / 超算**，功耗与存储层次成为瓶颈  
- Architecture & implementation layers: a unified top-down/bottom-up view from **RT → Gate → Device**  
  体系结构与实现层级：**寄存器传输级 → 门级 → 器件级** 的自上而下 / 自下而上的统一视角  



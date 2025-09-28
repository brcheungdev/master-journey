[← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor :Prof. Shinji Tomita (富田眞治)  

---

# Lecture 8: CPU Operation Principles & A Tiny Machine Language
CPU/Memory/I-O, fetch–decode–execute, byte addressing & endianness, condition codes, a toy 2-byte ISA, assembly ↔ machine code, branches  
中央处理器/内存/输入/输出、取数-解码-执行流程、字节寻址与字节序、条件代码、一个简单的 2 字节指令集、汇编语言与机器代码之间的转换、分支操作

---

## ⚪ Lecture Overview
- Computer components & data paths: **Control / ALU / Main Memory / I-O**  
  计算机组件及数据路径：**控制 / 算术逻辑单元 / 主存储器 / 输入输出**  
- **Main memory & addressing**: byte addressing, **little/big endian**, program/data layout  
  **主存储器及寻址方式**：字节寻址，**小端 / 大端格式**，程序 / 数据布局  
- **Control Unit** cycle: **Fetch → Decode → Execute**, PC update  
  **控制单元**周期：**取指 → 解码 → 执行**，程序计数器更新  
- **ALU ops** & condition codes (**Z / N / V / C**); shifts, logic, compare  
  **算术逻辑单元操作**及条件代码（**零 / 非零 / 溢出 / 进位**）；移位、逻辑运算、比较  
- A **tiny 2-byte fixed-length ISA**: LOAD / STORE, ADD / SUB / MUL / DIV, BRU / BRCC  
  一个**小型的 2 字节固定长度指令集**：加载 / 存储、加法 / 减法 / 乘法 / 除法、无条件 / 条件跳转  
- **Write & read** short machine programs; mapping to C  
  **编写与读取**简短的机器程序；与 C 语言的映射关系  

---

## ⚪ Lecture Content 讲座内容

### 1) Computer Components 计算机的构成要素
- **Control Unit (CU)**: fetch/decode/control execution, maintains **PC**  
  **控制单元 (CU)**：取指/译码/控制执行，维护 **PC**  
- **Arithmetic Unit (ALU)**: integer/float arithmetic, logic, shifts, compares, sets **Z/N/V/C** flags  
  **算术逻辑单元 (ALU)**：整数/浮点运算、逻辑、移位、比较，设置 **Z/N/V/C** 状态  
- **Main Memory**: byte addressing, stores machine programs & data  
  **主存**：字节寻址，存放机器程序与数据  
- **I/O Unit**: disks, network, display, keyboard, mouse, audio/video devices  
  **输入输出单元**：磁盘、网卡、显示器、键盘、鼠标、音视频设备  
- **Data paths & control**: buses/interfaces; DMA, memory-mapped I/O, interrupts/polling  
  **数据路径与控制**：总线/接口；DMA、存储映射 I/O、中断/轮询  

---

### 2) Main Memory, Addressing & Endianness 主存/寻址/端序
- **Byte addressing**: e.g., 1MB requires 20-bit address (hex 5-digit: 00000–FFFFF)  
  **字节寻址**：例如 1MB 内存需 20 位地址（16 进制 5 位：00000–FFFFF）  
- **R/W terminology**: Load = read, Store = write  
  **读写术语**：Load = 读，Store = 写  
- **Endianness**: little-endian vs big-endian for multi-byte integers  
  **字节序**：多字节整数的大小端序表示  
- Example layout: Code @0x00 (2B/instr), Data @0x30 (4B signed int)  
  示例内存布局：代码自 0x00 起（2 字节/条），数据自 0x30 起（4 字节补码整数）  

---

### 3) Control Unit Cycle 控制器工作流程
1. **Fetch**: use PC to fetch instruction from memory  
   **取指**：用 PC 从内存取指令  
2. **Decode**: determine type (Load/Store, ALU, Branch, I/O)  
   **解码**：判断指令类型（Load/Store、ALU、Branch、I/O）  
3. **Execute**: drive ALU or memory/I-O; update PC (sequential/branch)  
   **执行**：驱动 ALU 或内存/I-O；更新 PC（顺序或分支跳转）  

---

### 4) Tiny ISA Spec 课堂模型指令集
- Instruction length: 2 bytes (fixed)  
  指令长度：2 字节（固定）  
- Memory: 256 bytes (2-hex-digit address)  
  内存：示例256 字节（2 位十六进制地址空间）  
- Registers: 16, R0..R15  
  寄存器：16 个，R0..R15  
- Data: 4B signed int (two’s complement)  
  数据（抽象）：4 字节补码整数  
- Format: [opcode | operands], Rd/Rs1/Rs2 fields  
  格式：[操作码 | 操作数]，操作数字段指明Rd/Rs1/Rs2 字段  
- Condition codes: Z(Zero), N(Negative), V(Overflow), C(Carry) set by arithmetic ops  
  条件码：Z/N/V/C 由算术指令设置  

Instruction classes 指令类别：  
- LOAD Rd, Addr → Rd ← M[Addr]  
- STORE Rs, Addr → M[Addr] ← Rs  
- ADD/SUB/MUL/DIV Rd, Rs1, Rs2 → Rd ← Rs1 op Rs2 (DIV: quotient→Rd, remainder→Rd+1)  
- BRU target → PC ← target  
- BRCC cond, target → PC ← target if cond true, else PC+2

> **符号/十六进制记法**在讲义中一一对应；DIV 的“商/余数寄存器”与 **溢出/进位**示例也在课堂展示。

---

### 5) LOAD/STORE & ALU Encoding 示例
**LOAD/STORE（示例）**
```
Mnemonic  Hex  Note
LOAD R0,A  00 30  A@0x30
STORE R1,B 21 34  B@0x34
```
**ALU（示例）**
```
ADD R0,R1,R10  40 1A  Rd=R0, Rs1=R1, Rs2=R10
```
> 结果会更新 **Z/N/V/C**，以供 **BRCC** 使用；溢出可由 V 标志体现。
> 
---

### 6) Addressing Ambiguity 寻址歧义的消解
`LOAD R1, A` may mean:  
 LOAD R1, A 在记号层面可能指：
①`R1 ← M[A]` (value at A/把 **地址 A 处的值** 读入 R1) 
②`R1 ← &A` (address A itself/把 **地址 A 本身** 读入 R1).  
课堂统一采用**①**，必要时写作 **LOAD R1, M(A)** 与 **LOAD R1, &A** 区分。

---

### 7) Example 1: E = (A+B)*(C+D)
**Data layout（4-byte int）**: A@0x30=16, B@0x34=3, C@0x38=10, D@0x3C=17, E@0x40=?
**Program（2-byte/inst, code @0x00）**:  
```
Addr Mnemonic      Hex
00   LOAD R1,A     01 30
02   LOAD R2,B     02 34
04   ADD R3,R2,R1  43 21
06   LOAD R4,C     04 38
08   LOAD R5,D     05 3C
0A   ADD R6,R5,R4  46 54
0C   MUL R7,R6,R3  67 63
0E   STORE R7,E    27 40
10   STOP          B4 --
```
Equivalent C     等价 C 代码：  
```c
int a=16,b=3,c=10,d=17,e;
e=(a+b)*(c+d);
```

---

### 8) Example 2: Conditional Branch 条件分支
Goal: If A>B then E=A+B+C else E=A*B*C  
```
Addr Mnemonic          Hex
00   LOAD R1,A         01 30
02   LOAD R2,B         02 34
04   LOAD R3,C         03 38
06   SUB  R4,R2,R1     54 21  ; sets Z/N/V/C
08   BRCC N,L1         B1 10  ; if N==1 goto L1
0A   MUL  R5,R1,R2     65 12
0C   MUL  R5,R3,R5     65 35
0E   BRU  L2           8- 14
10 L1:ADD R5,R1,R2     45 12
12   ADD R5,R5,R3      45 53
14 L2:STORE R5,E       25 3C
16   STOP              B4 --
```
**C equivalent**:  
```c
if(a>b) e=a+b+c; else e=a*b*c;
```

---

### 9) Notes on I/O & Buses I/O与总线
- Storage & peripherals: HDD/SSD/DVD/BD/tape, printers, Ethernet/Wi-Fi, cameras, displays  
  存储与外设：HDD/SSD/DVD/BD/磁带、打印机、以太网/Wi-Fi、摄像头、显示器  等
- Buses: PCIe x16, SATA, USB  
  典型通道总线：PCIe x16（超高速）, SATA（高速）, USB  （低速）
- Control: DMA, memory-mapped I/O, interrupt/polling  
  控制方式：DMA、存储映射 I/O、中断/轮询  

---

### Key Points
- **Fetch–Decode–Execute**:sequential 2B instructions; branches rewrite PC  
  **取指 – 解码 – 执行**：PC 所指的 2 字节指令按顺序执行，分支跳转会修改 PC
- **Byte addressing & endianness**: understanding multi-byte integer layout is essential
  **字节寻址与端序**：理解多字节整数的内存布局至关重要
- **Z / N / V / C** status flags feed into **BRCC** for conditional branching; **DIV** yields quotient & remainder 
  **Z / N / V / C** 状态标志用于 **BRCC** 条件分支；**DIV** 指令产生商与余数
- Translate formulas/branch logic into a sequence of **LOAD / STORE + ALU + BR** 
  将公式 / 分支逻辑翻译成 **LOAD / STORE + ALU + BR** 的指令序列 
- Verify correctness by mapping symbols to hexadecimal in the machine program
  通过“符号 → 十六进制”的一一对应，验证机器程序装载是否正确

<h2></h2>

[← Previous Lecture / 上一章](./Lecture07.md) · [→ Next Lecture / 下一章](./Lecture09.md) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

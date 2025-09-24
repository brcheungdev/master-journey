#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 8: CPU Operation Principles & A Tiny Machine Language
CPU/Memory/I-O, fetch–decode–execute, byte addressing & endianness, condition codes, a toy 2-byte ISA, assembly ↔ machine code, branches<br/>
中央处理器/内存/输入/输出、取数-解码-执行流程、字节寻址与字节序、条件代码、一个简单的 2 字节指令集、汇编语言与机器代码之间的转换、分支操作
---

## ⚪ Lecture Overview
- Computer components & data paths: **Control/ALU/Main Memory/I-O**  计算机组件及数据路径：**控制/算术逻辑单元/主存储器/输入输出**
- **Main memory & addressing**: byte addressing, **little/big endian**, program/data layout  **主存储器及寻址方式**：字节寻址，**小端/大端格式**，程序/数据布局
- **Control Unit** cycle: **Fetch → Decode → Execute**, PC update  **控制单元**周期：**取指 → 解码 → 执行**，程序计数器更新
- **ALU ops** & condition codes (**Z/N/V/C**); shifts, logic, compare   **算术逻辑单元操作**及条件代码（**零/非/溢出/条件**）；移位、逻辑运算、比较
- A **tiny 2-byte fixed-length ISA**: LOAD/STORE, ADD/SUB/MUL/DIV, BRU/BRCC  一个**小型的 2 字节固定长度指令集**：加载/存储、加法/减法/乘法/除法、跳转/条件跳转
- **Write & read** short machine programs; mapping to C  **写入与读取**简短的机器程序；转换为 C 语言

---

## ⚪ Lecture Content 讲座内容

### 1) Computer Components 计算机的构成要素
- **Control Unit (CU)**：取指/译码/控制执行，维护 **PC**  
- **Arithmetic Unit (ALU)**：整数/浮点四则、逻辑、移位、比较，设置 **Z/N/V/C** 状态  
- **Main Memory (主存)**：字节寻址，存放 **机器语言程序** 与数据  
- **I/O Unit**：磁盘、网卡、显示、键鼠、音视频设备  
- **Data paths & control**：总线/接口；**DMA、Memory-Mapped I/O、Interrupt/Polling**

---

### 2) Main Memory, Addressing & Endianness 主存/寻址/端序
- **Byte addressing**；例如 **1 MB** 可用 **20-bit** 地址（16 进制 5 位：`00000`–`FFFFF`）  
- **R/W** 术语：**Load**(读) / **Store**(写)  
- **Endianness**：**Little-endian / Big-endian**（多字节数在内存的字节序）  
- 课堂模型常用内存布局（示例）：  
  - **Code** 从 `0x00` 起按 **2 字节/条** 顺序存放  
  - **Data**（4 字节补码整数）从 `0x30` 等地址开始

---

### 3) Control Unit Cycle 控制器工作流程
1. **Fetch**：用 **PC** 从主存取指  
2. **Decode**：判断类型（Load/Store、ALU、Branch、I/O）  
3. **Execute**：驱动 ALU 或主存/I-O；更新 **PC**（加上本条指令字节数或分支跳转）

---

### 4) Tiny ISA Spec（课堂模型指令集）
- **Instruction length**：**2 bytes（fixed）**  
- **Memory**：示例 **256 bytes**（2 位十六进制地址空间）  
- **Registers**：**16 个**，`R0..R15`  
- **Data**：**4-byte signed int（two’s complement）**  
- **Format**（抽象）：`[ opcode | operands ]`，操作数字段指明 `Rd / Rs / Rs1 / Rs2`  
- **Condition Codes**：`Z`(Zero), `N`(Negative), `V`(Overflow), `C`(Carry) 由算术指令设置

**Instruction classes**
- **LOAD Rd, Addr**：`Rd ← M[Addr]`  
- **STORE Rs, Addr**：`M[Addr] ← Rs`  
- **ADD/SUB/MUL/DIV Rd, Rs1, Rs2**：`Rd ← Rs1 (op) Rs2`（`DIV`：商→`Rd`，余数→`Rd+1`）  
- **BRU target**：无条件分支，`PC ← target`  
- **BRCC cond, target**：按 **Z/N/V/C** 条件分支，真：`PC ← target`；假：`PC ← PC+2`

> **符号/十六进制记法**在讲义中一一对应；DIV 的“商/余数寄存器”与 **溢出/进位**示例也在课堂展示。

---

### 5) LOAD/STORE & ALU Encoding 示例
**LOAD/STORE（示例）**

```
Mnemonic Hex encoding Note
LOAD R0, A 0 0 30 A at address 0x30
STORE R1, B 2 1 34 B at address 0x34
```

**ALU（示例）**
```
ADD R0, R1, R10 4 0 1 A Rd=R0, Rs1=R1, Rs2=R10
```
> 结果会更新 **Z/N/V/C**，以供 **BRCC** 使用；溢出可由 `V` 标志体现。

---

### 6) Addressing Ambiguity 寻址歧义的消解
- `LOAD R1, A` 在记号层面可能指：  
  ① `R1 ← M[A]`（把 **地址 A 处的值** 读入 `R1`）  
  ② `R1 ← &A`（把 **地址 A 本身** 读入 `R1`）  
- 课堂统一采用 **①**，必要时写作 **`LOAD R1, M(A)`** 与 **`LOAD R1, &A`** 区分。

---

### 7) Example 1 — `E = (A+B) * (C+D)`
**Data layout（4-byte int）**：`A@0x30=16, B@0x34=3, C@0x38=10, D@0x3C=17, E@0x40=?`

**Program（2-byte/inst, code @0x00）**
```
Addr Mnemonic Hex
00 LOAD R1, A 01 30
02 LOAD R2, B 02 34
04 ADD R3, R2, R1 43 21
06 LOAD R4, C 04 38
08 LOAD R5, D 05 3C
0A ADD R6, R5, R4 46 54
0C MUL R7, R6, R3 67 63
0E STORE R7, E 27 40
10 STOP B4 --
```

**Equivalent C**
```c
int a=16, b=3, c=10, d=17, e;
e = (a+b) * (c+d);
```

### 8) Example 2 — Conditional Branch 条件分支
Goal：If A > B then E = A + B + C else E = A * B * C
```
Addr  Mnemonic                        Hex
00    LOAD  R1, A                     01 30
02    LOAD  R2, B                     02 34
04    LOAD  R3, C                     03 38
06    SUB   R4, R2, R1                54 21         ; sets Z/N/V/C
08    BRCC  N,  L1                    B1 10         ; if (N==1) goto L1
0A    MUL   R5, R1, R2                65 12
0C    MUL   R5, R3, R5                65 35
0E    BRU      L2                     8- 14
10 L1:ADD   R5, R1, R2                45 12
12    ADD   R5, R5, R3                45 53
14 L2:STORE R5, E                      25 3C
16    STOP                             B4 --
```
Equivalent C
```c
int a=16, b=3, c=10, e;
if (a > b) e = a + b + c;
else       e = a * b * c;
```

### 9) Notes on I/O & Buses I/O与总线
- 存储与外设：HDD/SSD、DVD/BD/磁带（归档）、打印机、以太网/Wi-Fi、摄像头/麦克/显示器等
- 典型通道：PCIe x16（超高速）、SATA（高速）、USB（低速）
- 控制方式：DMA、Memory-Mapped I/O、Interrupt/Poling

---
### Key Points
- Fetch–Decode–Execute：PC 指向的 2-byte 指令按序执行，分支改写 PC
- 字节寻址 & 端序：理解多字节整数的内存布局很关键
- Z/N/V/C 状态承接到 BRCC 的条件判定；DIV 产 商/余数
- 将公式/分支逻辑翻译成LOAD/STORE + ALU + BR 的序列
- 通过“符号→十六进制”的一一对应，验证机器程序装载是否正确

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 9: From C to Machine Code on a Tiny ISA  
Translating C to machine code, register allocation, loops/arrays, index addressing, BAL/RTN function calls, parameter passing (value/reference)<br/>
将 C 语言翻译成机器代码、寄存器分配、循环/数组、索引寻址、BAL/RTN 函数调用、参数传递（值/引用）
---

## ⚪ Lecture Overview 
- How a C program is **lowered** into the toy 2-byte instruction set  
  如何将 C 程序**转换**为简化的 2 字节指令集  
- **Register allocation** strategy and label design  
  **寄存器分配**策略与标签设计  
- Classic tasks in both C and assembly:  
  C 和汇编中的典型练习：  
  1) `E = (A+B) * (C+D)`  
     计算表达式 `E = (A+B) * (C+D)`  
  2) `if (A>B) E=A+B+C; else E=A*B*C;`  
     分支结构：若 A>B，E=A+B+C，否则 E=A*B*C  
  3) **Sum 1..10** with a loop  
     使用循环求 1..10 的和  
  4) **Sum of A[0..9]** in three styles: naïve / dangerous self-modifying / index addressing  
     三种风格求 A[0..9] 的和：普通 / 危险自修改 / 索引寻址  
  5) **Repeat** a sum many times: naïve vs **function call** with `BAL/RTN`  
     多次重复求和：普通方式 vs 使用 `BAL/RTN` 的函数调用  
- **Parameter passing**: call-by-value vs call-by-reference on the model ISA  
  **参数传递**：在模型 ISA 上的值传递 vs 引用传递  

---

## ⚪ Lecture Content 讲座内容

### 1) From C to Assembly: Registers, Labels, Data  
从 C 到汇编：寄存器、标签与数据布局  
**Data layout (example)**  
数据布局（示例）  
- `ZERO@0x30 = 0`, `ONE@0x34 = 1`  
- `A@0x30`, `B@0x34`, `C@0x38`, `D@0x3C`, `E@0x40` (4-byte 2’s-complement ints)  
  `A@0x30`、`B@0x34`、`C@0x38`、`D@0x3C`、`E@0x40`（4 字节补码整数）  

**Register conventions (typical for this lecture)**  
寄存器约定（本课示例）  
- `R1`: accumulator / partial sum `s`  
  `R1`：累加器 / 临时和 `s`  
- `R3`: loop index `i`  
  `R3`：循环变量 `i`  
- `R0`: loop bound `imax` or constants  
  `R0`：循环上界 `imax` 或常量寄存器  
- `R15`: **index register** (when using indexed addressing)  
  `R15`：**索引寄存器**（用于索引寻址）  

---

### 2) Example: `E = (A+B) * (C+D)`  
示例：`E = (A+B) * (C+D)`  
**C (for reference)**  
**C 代码（仅作参考）**  
```c
int a=16, b=3, c=10, d=17, e;
e = (a+b) * (c+d);
```

**Assembly (2-byte/inst; code @0x00)**  
**汇编（2 字节/条；代码从 0x00 开始）**  
```
00  LOAD  R1, A
02  LOAD  R2, B
04  ADD   R3, R2, R1          ; R3 = A+B
06  LOAD  R4, C
08  LOAD  R5, D
0A  ADD   R6, R5, R4          ; R6 = C+D
0C  MUL   R7, R6, R3          ; R7 = (A+B)*(C+D)
0E  STORE R7, E
10  STOP
```

---

### 3) Example: Conditional (`if A>B ... else ...`)  
示例：条件分支（`if A>B ... else ...`）  
**C**
```c
if (a > b) e = a + b + c;
else       e = a * b * c;
```

**Assembly (idea)**  
**汇编思路**  
```
LOAD R1, A
LOAD R2, B
LOAD R3, C
SUB  R4, R2, R1        ; sets N/Z/V/C using B-A
BRCC N, L_then         ; if (A>B) → N==1 → then-branch
MUL  R5, R1, R2
MUL  R5, R5, R3
BRU  L_end
L_then:
ADD  R5, R1, R2
ADD  R5, R5, R3
L_end:
STORE R5, E
STOP
```

---

### 4) Loop: Sum of integers 1..10  
循环：计算 1..10 的和  
**C**
```c
int s=0;
for (int i=1; i<=10; i++) s += i;
printf("%d\n", s);
```

**Assembly (branch on condition codes)**  
**汇编（基于条件码分支）**  
```
LOAD R1, ZERO      ; s=0
LOAD R3, ONE       ; i=1
LOAD R2, ONE       ; increment = 1
LOAD R0, IMAX      ; imax=10

L1:
SUB  R4, R0, R3    ; imax - i
BRCC N, L2         ; if (imax-i) < 0 → done
ADD  R1, R1, R3    ; s += i
ADD  R3, R3, R2    ; i++
BRU  L1
L2:
STORE R1, SUM
STOP
```

---

### 5) Array Sum A[0..9] — three approaches  
数组求和 A[0..9] —— 三种方法  

#### (a) Naïve (賢くない方法)  
#### (a) 朴素法（不聪明的办法）  
> Load and add each element explicitly; verbose and not scalable.  
> 逐条 `LOAD A[k]` 然后 `ADD`，写 10 次，非常冗长，不可扩展。  
```
LOAD R1, ZERO
LOAD R3, A[0];  ADD R1, R1, R3
LOAD R3, A[1];  ADD R1, R1, R3
...
LOAD R3, A[9];  ADD R1, R1, R3
STORE R1, SUM
STOP
```

#### (b) Dangerous: **self-modifying** by patching the data address  
#### (b) 危险方法：**自修改代码**（修改数据地址字段）  
> Each iteration increments the encoded data address (e.g., +4 for next int).  
> 每轮将指令中的“数据地址字段”加 4 以访问下一个元素。  
> **Risk**: corrupts instruction fields; poor portability; not recommended.  
> **风险**：可能破坏其他指令字段；可移植性差；不建议。  

#### (c) Proper: **index addressing** with `R15`  
#### (c) 正确方法：使用 `R15` 的**索引寻址**  
> `LOADX Rd, A` ≈ read from `M(Addr(A)+R15)`; bump `R15 += 4` per element.  
> `LOADX Rd, A` 近似表示从 `M(Addr(A)+R15)` 读取；每次元素后 `R15 += 4`。  

**Assembly**  
**汇编**  
```
LOAD  R0, REPEAT    ; 10
LOAD  R1, ZERO      ; s=0
LOAD  R2, ONE       ; +1
LOAD  R4, FOUR      ; +4 (element size)
LOAD  R15, ZERO     ; index base = 0
LOADX R3, A[0]      ; R3 = A[0] with index

L1:
ADD   R1, R1, R3    ; s += A[i]
SUB   R0, R0, R2    ; repeat--
BRCC  Z, L2         ; if zero → done
ADD   R15, R15, R4  ; index += 4
LOADX R3, A         ; next A[i+1]
BRU   L1
L2:
STORE R1, SUM
STOP
```

---

### 6) Repeating a Sum Many Times: **Function call vs naïve**  
多次重复求和：**函数调用** vs 朴素复制  
- **Naïve**: copy-paste the sum loop everywhere → big and hard to maintain  
  **朴素**：把“求和 1..N”的指令序列到处复制 → 体积大、难维护  
- **Function**: use `BAL` (Branch-and-Link) / `RTN` (Return)  
  **函数化**：使用 `BAL`（带返回地址跳转）与 `RTN`（返回）  
  - Call site: `BAL Rrtn, SUM`; function end: `RTN Rrtn`  
    调用点：`BAL Rrtn, SUM`；函数尾：`RTN Rrtn`  
  - Save/restore registers; pass/return via registers  
    需要保存/恢复寄存器；通过寄存器传参与返回  

**C (reference)**  
**C 代码（参考）**  
```c
int sum(int n){ int s=0; for(int i=1;i<=n;i++) s+=i; return s; }

int a=10, b=5;
int sum1 = sum(a+b);   // 120
int sum2 = sum(a-b);   // 15
```

**Assembly sketch (call-by-value)**  
**汇编草图（值传递）**  
```
; caller
LOAD R1, A
LOAD R2, B
ADD  R5, R1, R2      ; R5 = a+b
; R5 as argument copy
BAL  R4, SUM         ; call
STORE R6, SUM1       ; R6 holds return value

SUB  R5, R1, R2      ; R5 = a-b
BAL  R4, SUM
STORE R6, SUM2
...

; callee: SUM
STORE R1, SAVER1     ; save clobbered regs
STORE R2, SAVER2
STORE R3, SAVER3
LOAD  R1, ZERO       ; s=0
LOAD  R2, ONE        ; +1
LOAD  R3, ONE        ; i=1
L1:  ADD  R1, R1, R3 ; s+=i
     SUB  R5, R5, R2 ; n--
     BRCC Z, L2
     ADD  R3, R3, R2 ; i++
     BRU  L1
L2:  LOAD R6, ZERO
     ADD  R6, R1, R6 ; return s in R6
     LOAD R1, SAVER1 ; restore
     LOAD R2, SAVER2
     LOAD R3, SAVER3
     RTN  R4
```

---

### 7) Parameter Passing: **by value** vs **by reference**  
参数传递：**值传递** vs **引用传递**  
- **Call-by-Value**: pass a copy of `n`; callee cannot modify the original  
  **值传递（Call-by-Value）**：把 `n` 的**拷贝**传给函数，函数内部改不回原变量

- **Call-by-Reference**: pass an address and access via LOADX/STOREX  
  **引用传递（Call-by-Reference）**：把**地址**传给函数，在函数内通过地址读写原变量  
  - 讲义给出两种把地址传给函数的方法：  
    1) 新增 `LOADA`（Load-Address）把 `&C` 装入寄存器（如 `R15`），函数中用 `LOADX/STOREX` 访问  
    2) 在数据区**预先存放**指针变量 `PNTC= &C`，调用前把 `PNTC` 装入 `R15` 作为索引基址  

**C (reference form)**  
**C 代码（参考形式）**  
```c
int sum_ref(int *n){
  int s=0; for(int i=1;i<=*n;i++) s+=i; return s;
}
sum_ref(&c); sum_ref(&d);
```

**Assembly (reference idea)**  
**汇编（引用思路）**  
```
; caller sets argument as an ADDRESS
LOADA R15, C        ; R15 = &C      (or LOAD R15, PNTC)
BAL   R4, SUM       ; call
STORE R6, SUM1

; callee reads *n via indexed access
LOADX R5, 0         ; R5 = *(&C) = C
...                 ; loop uses R5 as bound
```

---

### 8) Notes: Disassembly in Visual Studio  
注：在 Visual Studio 中查看反汇编  
- Debug → Windows → **Disassembly** shows compiler-generated code paths.  
  Debug → Windows → **Disassembly** 可以观察编译器生成的机器码/指令序列，帮助理解 C 到机器语言的映射与优化路径。  

---

### Key Points
- Learn to decompose C programs into: **data area**, **register allocation**, **control flow (labels/branches)**, **arithmetic/memory instructions**  
  学会将 C 程序拆分成：**数据区**、**寄存器分配**、**控制流（标签/分支）**、**算术/访存指令**  
- **Indexed addressing (`LOADX/STOREX`)** is the scalable array traversal method; **self-modifying code** has portability and security risks  
  **索引寻址 (`LOADX/STOREX`)** 才是可扩展的数组遍历方式；**自修改代码**存在可移植性与安全隐患  
- Using `BAL/RTN` for **function calls** significantly reduces repeated code; remember **register save/restore**  
  使用 `BAL/RTN` 进行**函数化**可显著减少重复代码；注意**寄存器保存与恢复**  
- **Call-by-value** passes copies, **call-by-reference** passes addresses; on the model ISA, can be done via `LOADA` or pointer variables + `R15`/`LOADX`  
  **值传递**传递的是值的副本，**引用传递**传递的是地址；在模型 ISA 中可用 `LOADA` 或指针变量 + `R15`/`LOADX` 实现  

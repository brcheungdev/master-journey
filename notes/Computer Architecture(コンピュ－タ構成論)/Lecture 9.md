#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 9: From C to Machine Code on a Tiny ISA  
Translating C to machine code, register allocation, loops/arrays, index addressing, BAL/RTN function calls, parameter passing (value/reference)(br/)
将 C 语言翻译成机器代码、寄存器分配、循环/数组、索引寻址、BAL/RTN 函数调用、参数传递（值/引用）
---

## ⚪ Lecture Overview
- How a C program is **lowered** into the toy 2-byte instruction set  
- **Register allocation** strategy and label design  
- Classic tasks in both C and assembly:  
  1) `E = (A+B) * (C+D)`  
  2) `if (A>B) E=A+B+C; else E=A*B*C;`  
  3) **Sum 1..10** with a loop  
  4) **Sum of A[0..9]** in three styles: naïve / dangerous self-modifying / index addressing  
  5) **Repeat** a sum many times: naïve vs **function call** with `BAL/RTN`  
- **Parameter passing**: call-by-value vs call-by-reference on the model ISA

- 如何将 C 程序“降级”为简易的 2 字节指令集
- 寄存器分配策略和标签设计
- C 语言和汇编语言中的经典任务：
1）`E = (A+B) * (C+D)`
2）`如果 (A>B) 则 E = A+B+C；否则 E = A*B*C;``
3) 使用循环进行 1 到 10 的求和
4) 以三种方式计算 A[0 到 9] 的总和：原始方法/危险的自修改方法/索引寻址方法
5) 多次重复求和：原始方法与使用“BAL/RTN”进行函数调用的对比 - 参数传递：按值传递与按引用传递在模型指令集中的情况对比
---

## ⚪ Lecture Content 讲座内容

### 1) From C to Assembly: Registers, Labels, Data
**Data layout (example)**  
- `ZERO@0x30 = 0`, `ONE@0x34 = 1`  
- `A@0x30`, `B@0x34`, `C@0x38`, `D@0x3C`, `E@0x40` (4-byte 2’s-complement ints)

**Register conventions (typical for this lecture)**
- `R1`: accumulator / partial sum `s`  
- `R3`: loop index `i`  
- `R0`: loop bound `imax` or constants  
- `R15`: **index register** (when using indexed addressing)

---

### 2) Example: `E = (A+B) * (C+D)`
**C (for reference)**
```c
int a=16, b=3, c=10, d=17, e;
e = (a+b) * (c+d);
```

**Assembly (2-byte/inst; code @0x00)**  
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
**C**
```c
if (a > b) e = a + b + c;
else       e = a * b * c;
```

**Assembly (idea)**  
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
**C**
```c
int s=0;
for (int i=1; i<=10; i++) s += i;
printf("%d\n", s);
```

**Assembly (branch on condition codes)**
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

#### (a) Naïve (賢くない方法)
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
> 通过给一个 `LOAD` 指令的“数据地址字段”每轮 `+4` 来访问 `A[k+1]`。  
> **风险**：溢出会覆盖指令中的寄存器字段；复制到别处不可移植；软件工程上**不推荐**修改指令流。

#### (c) Proper: **index addressing** with `R15`
> 讲义引入 **indexed load/store**：`LOADX Rd, A` 等价于从 `M(Addr(A)+R15)` 读。  
> 每次把 `R15 += 4`（4 字节元素）即可扫描数组。

**Assembly**
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
- **Naïve**：把“求和 1..N”的指令序列复制粘贴多处 → 代码大、维护难  
- **函数化**：使用 `BAL` (Branch-and-Link) / `RTN` (Return)  
  - 调用点：`BAL Rrtn, SUM`；函数末尾：`RTN Rrtn`  
  - 调用时保存/恢复必要寄存器（callee saves），并以寄存器传参/返回

**C (reference)**
```c
int sum(int n){ int s=0; for(int i=1;i<=n;i++) s+=i; return s; }

int a=10, b=5;
int sum1 = sum(a+b);   // 120
int sum2 = sum(a-b);   // 15
```

**Assembly sketch (call-by-value)**  
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
- **值传递（Call-by-Value）**：把 `n` 的**拷贝**传给函数，函数内部改不回原变量  
- **引用传递（Call-by-Reference）**：把**地址**传给函数，在函数内通过地址读写原变量  
  - 讲义给出两种把地址传给函数的方法：  
    1) 新增 `LOADA`（Load-Address）把 `&C` 装入寄存器（如 `R15`），函数中用 `LOADX/STOREX` 访问  
    2) 在数据区**预先存放**指针变量 `PNTC= &C`，调用前把 `PNTC` 装入 `R15` 作为索引基址

**C (reference form)**
```c
int sum_ref(int *n){
  int s=0; for(int i=1;i<=*n;i++) s+=i; return s;
}
sum_ref(&c); sum_ref(&d);
```

**Assembly (reference idea)**
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
- Debug → Windows → **Disassembly**：可观察编译器生成的真实机器码/指令序列，帮助理解 **C→机器语言** 的降级路径与优化。

---

## Key Points 
- 学会把 C 程序拆成：**数据区**、**寄存器分配**、**控制流（标签/分支）**、**算术/访存指令**  
- **索引寻址 (`LOADX/STOREX`)** 才是可扩展的数组遍历方式；**自修改代码**有可移植性与安全风险  
- 使用 `BAL/RTN` 做**函数化**可显著减少重复代码；注意**寄存器保存/恢复**  
- **值传递**传拷贝，**引用传递**传地址；在模型 ISA 上可通过 `LOADA` 或 **指针变量** + `R15`/`LOADX` 实现

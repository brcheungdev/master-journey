[← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---

# Lecture 7: Bits, Number Systems & Numeric Data Representation  
Bits & bytes, positional notation, base conversion, exponent/log rules, data encodings, two’s complement, integer add/sub & overflow, IEEE-754 floating point, C literals  
位与字节、位置表示法、基数转换、指数/对数规则、数据编码、二进制补码、整数加/减及溢出处理、IEEE-754 浮点数、C 语言常量

---

## ⚪ Lecture Overview
- Bit/Byte, MSB/LSB, positional notation  
  比特/字节、最高有效位/最低有效位、位置表示法  
- Base conversion: binary ↔ octal/hex/decimal; integers & fractions  
  基数转换：二进制 ↔ 八进制 / 十六进制 / 十进制；整数与小数  
- Exponent & logarithm laws (review)  
  指数与对数定律（复习）  
- What bits can represent: numbers, text codes (ASCII/Unicode), booleans, patterns, RGB images  
  位所能表示的内容：数字、文本编码（ASCII/Unicode）、布尔值、模式、RGB 图像  
- SI prefixes (decimal/binary) & typical HW/OS scale  
  国际单位制前缀（十进制 / 二进制）及典型硬件 / 操作系统规模  
- Numeric data representation: fixed-point vs floating-point  
  数值数据表示：定点与浮点  
- Negative numbers: sign-magnitude, 1’s complement, 2’s complement  
  负数：符号位表示法、1 的补码、2 的补码  
- Integer add/sub algorithms & **overflow** detection  
  整数加 / 减算法及 **溢出** 检测  
- IEEE-754: single/double (NaN/∞/denorm), half/quad (overview)  
  IEEE-754：单精度 / 双精度（非数 / 无穷大 / 非正规数），半精度 / 四分之一精度（概述）  
- C numeric literals in multiple bases  
  多种进制下的 C 语言数值常量  

---

## ⚪ Lecture Content 讲座内容

### 1) Bits, Bytes & Positional Notation  比特/字节与位权制
- **Bit** = binary digit: `0/1`; **Byte** = 8 bits.  
  **位**：二进制数字，取值 0 或 1；**字节**：8 位组成。  
- MSB = Most Significant Bit (最高位)；LSB = Least Significant Bit (最低位)。  
  MSB = 最高有效位；LSB = 最低有效位。  
- **Positional notation** (base `r`):  
  **位权表示法** (基数 `r`)：
  `(a_{n-1} ... a_0)_r = a_{n-1}·r^{n-1} + ... + a_1·r^1 + a_0·r^0`

Examples  
示例：  
- `(253)_{10} = 2·10^2 + 5·10^1 + 3·10^0`  
- `(01011010)_2 = 2^6 + 2^4 + 2^3 + 2^1 = (90)_{10}`

---

### 2) Base Conversion  进制转换（整/小数）
**Binary ↔ Octal / Hex (grouping method)**  
二进制 ↔ 八/十六进制（分组法）：  
- 每 3 位二进制对应 1 位八进制；每 4 位二进制对应 1 位十六进制。  
- `(90)_{10} = (01011010)_2 = (132)_8 = (5A)_{16}`  
  - `1010→A, 1011→B, 1100→C, 1101→D, 1110→E, 1111→F`

**Decimal → Binary (integer, divide-by-2)**  
十进制整数转二进制：反复除以 2 取余数，从最后一位余数倒序写出。  

**Decimal Fraction → Binary (fraction, multiply-by-2)**  
十进制小数转二进制：反复乘以 2 取整数部分，依次构成小数位。  
Example: `0.625_{10} = 0.101_2`；`0.1_{10}` = 循环小数 `0.0001100110011..._2`  

---

### 3) Exponents & Logarithms  指数与对数速记
- Laws: commutative, associative, distributive  
  规律：交换律、结合律、分配律  
- Exponent laws:  
  指数律：`a^n · a^m = a^{n+m}`, `(a^n)^m = a^{nm}`, `(ab)^n = a^n b^n`, `a^{-n} = 1/a^n`  
- Logarithm laws:  
  对数律：`log_a(xy)=log_a x + log_a y`, `log_a(x/y)=log_a x - log_a y`, `log_a x^n = n log_a x`  
- Common bases: `e`, `10`, `2`  
  常用底数：`e`（自然对数）、`10`（常用对数）、`2`（信息论）

---

### 4) What Bits Can Represent  比特可表示的对象
- Numbers: integers, fractions  
  数字：整数、小数  
- Text codes: ASCII/EBCDIC, Unicode (UTF-8/UTF-16)  
  文本编码：ASCII/EBCDIC，Unicode (UTF-8/UTF-16)  
- Booleans: `True=1 / False=0` (logic AND/OR/NOT)  
  布尔值：`True=1 / False=0`（逻辑与/或/非）  
- Patterns & Images: bitmaps, RGB images  
  模式和图像：位图、RGB 图像

---

### 5) SI Prefixes & Scales  前缀与数量级
- Decimal: k, M, G, T, P, E, Z, Y, R, Q (10^3, 10^6, …)  
  十进制前缀：k, M, G, T, P, E, Z, Y, R, Q (10^3, 10^6, …)  
- Binary: Ki, Mi, Gi, Ti, Pi, Ei (2^10, 2^20, …)  
  二进制前缀：Ki, Mi, Gi, Ti, Pi, Ei (2^10, 2^20, …)  
- Typical HW/OS scales: Cache=MB, Memory=GB, CPU=GHz, Disk=GB–TB  
  典型硬件/系统规模：缓存=MB，内存=GB，CPU=GHz，磁盘=GB–TB  

---

### 6) Numeric Data Representation  数值数据表示
- Fixed-point（整数/定点）: decimal point fixed position  
  定点数：小数点位置固定 （像算盘） 
- Floating-point（浮点）: sign × base^exponent × significand  
  浮点数：表示为符号×基数^指数×尾数  
- C types: int/long long → fixed; float/double → floating  
  C 语言类型：整数（int/long long 等）=int/long long（定点整数）；浮点=float/double（float 单精度 / double 双精度）

---

### 7) Negative Numbers 负数表示法
- Sign-magnitude（原码）: sign bit + magnitude  
  符号位+数值  
- 1’s complement（反码）: bitwise NOT  
  1 的补码：按位取反（存在两个 0）  
- 2’s complement（补码）: NOT + 1  
  2 的补码：按位取反再加 1 （现代整数运算通用表示）  
- Range (L-bit): [-2^L, 2^L−1]  
  L 位补码范围：[-2^L, 2^L−1]

---

### 8) Integer Add/Sub & Overflow  加减运算与溢出
- Use (L+1)-bit adder  
  用无符号加法器在 **(L+1) 位**（含符号位）上做加减。 
- Overflow detection: XOR of carry-in/out or sign rules  
  溢出检测（补码加法）：
  - 可用**符号位“进位入”和“进位出”的 XOR** 判断；
  - 或用**符号规则**：
    - X>0,Y>0 且结果为负 → 溢出；
    - X<0,Y<0 且结果为正 → 溢出。
- 补码减法可转为加法（被减数 + 负数的补码）。

- 10/9 的补数法（十进制）也在讲义中回顾，用于手算减法的等价实现思路。

---

### 9) IEEE-754 Floating Point 浮点数（单/双精度） 
- **Single (32-bit)**：sign(1) | exponent(8, bias=127) | fraction(23)
  - 数值（正规化区间）：(-1)^s × 2^{e-127} × (1.f)
  - 特殊：e=255, f≠0 → NaN；e=255, f=0 → ±∞；e=0, f≠0 → 非正规数；e=f=0 → ±0
  - 精度：二进制约 24 位（十进制约 8 位） - **Double (64-bit)**：sign(1) | exponent(11, bias=1023) | fraction(52)
  - 数值：(-1)^s × 2^{e-1023} × (1.f)；精度二进制约 53 位（十进制约 16 位）
  - **Half/Quad**：课程概览提及（CG/高精度计算等场景）
  - 例：0.1_{10} 在二进制是循环小数 → 浮点表示存在舍入误差；IEEE-754 默认**四舍六入五留双（Nearest-even）**。

---

### 10) C Numeric Literals  C 语言数值常量
```c
int d  = 10;        // decimal
int hx = 0xA;       // hexadecimal
int oc = 012;       // octal
int bn = 0b1011;    // binary (if supported)
```
Mixed computation & formatting  
混合运算与格式化：
```c
#include <stdio.h>
int main(void) {
    double a = 1.4, b = 2.3, c;
    int    d;
    c = a + b;      // 3.7 (double)
    d = a + b;      // truncated to 3
    printf("c (double) = %lf
", c);
    printf("d (int)    = %d
",  d);
    return 0;
}
```

---

### Key Points 
- Master Positional notation & base conversion between binary, octal, decimal, and hexadecimal
  掌握位权制与二 / 八 / 十六进制之间的分组转换  
- Remember basic exponent/logarithm identities (useful in complexity estimation and numeric scaling)
  牢记指数 / 对数的基本恒等式（在程序复杂度与数值尺度估算中常用） 
- Use two’s complement for unified add/sub of negative numbers; detect overflow via carry XOR or sign rules
  负数用补码统一加减（硬件实现高效），溢出用进位 XOR 或符号规则判别  
- IEEE-754 formats, special values, and rounding affect numeric computation results  
  IEEE-754 的规格 / 特殊值 / 舍入会影响数值计算结果
- Correctly write and print numeric literals of various types in C  
  在 C 中正确书写与打印不同类型的数值

<h2></h2>

[← Previous Lecture / 上一章](./Lecture06.md) · [→ Next Lecture / 下一章](./Lecture08.md) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
## Lecture 3
- Data Types, Binary & Hexadecimal, Control Statements, Arrays, Quadratic Equation Solver
 
---
## ⚪ Lecture Overview 
1. Bits, Bytes, and Number Systems
2. C Language Program Structure and Data Types  
3. Arithmetic, Logical, and Conditional Statements 
4. Repetition Structures: For & While
5. Arrays and Applications (Sum, Min, Max)  
6. Quadratic Equation Solver Program

## ⚪ Lecture Content 讲座内容
### 1) Bits, Bytes, and Number Systems    位、字节与数制系统
- Bit: binary digit, one binary digit (0 or 1)
- Byte: 8 bits = 1 byte
- Common units:
  - K (kilo) = 2^10, M (mega) = 2^20, G (giga) = 2^30
  - T (tera) = 2^40, P (peta) = 2^50, E (exa) = 2^60
Number Systems:
- Decimal (10): (253)₁₀ = 2×10² + 5×10¹ + 3×10⁰
- Binary (2): (01011010)₂ = 90₁₀
- Octal (8): (132)₈ = 90₁₀
- Hex (16): (5A)₁₆ = 90₁₀
Binary to Hex Mapping:
- 1010 = A, 1011 = B, 1100 = C, 1101 = D, 1110 = E, 1111 = F

### 2) C Program Structure & Data Types    C 语言程序结构与数据类型
Program Structure:                         程序结构
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a, b, c;
    a = 1; b = 2;
    c = a + b;
    printf("Sum = %d\n", c);
    return 0;
}
```
Data Types:
- int: integer
- float: single precision floating-point
- double: double precision floating-point
- char: character, ASCII code
Format Specifiers:
- %d → int, %f → float, %lf → double, %c → char, %s → string

### 3) Arithmetic & Logical Operations    算术与逻辑运算
- Arithmetic: +, -, *, /, %
- Increment/Decrement: i++, i--
- Logical Operators: && (AND), || (OR), ! (NOT)
- Relational Operators: <, >, <=, >=, ==, !=
Example:
```c
#include <stdio.h>
int main() {
    int a = 5, b = 2;
    printf("Quotient = %d, Remainder = %d\n", a/b, a%b);
    return 0;
}
```
### 4) Conditional Statements (if-else)    条件语句（if-else）
```c
#include <stdio.h>
int main() {
    int a=10, b=20;
    if (a >= b)
        printf("a >= b\n");
    else
        printf("a < b\n");
    return 0;
}
```
### 5) Repetition Statements (for, while)    重复语句（for 循环、while 循环）
For loop:
```c
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}
```
While loop:
```c
int i = 0;
while (i < 10) {
    printf("%d ", i);
    i++;
}
```
### 6) Arrays and Applications    数组与应用
- Array Declaration: int A[10];
- Sum of Elements:
```c
int A[10] = {1,2,3,4,5,6,7,8,9,10};
int sum = 0;
for (int i=0; i<10; i++) sum += A[i];
printf("Sum = %d\n", sum);
```
- Find Max & Min:
```c
int max = A[0], min = A[0];
for (int i=1; i<10; i++) {
    if (A[i] > max) max = A[i];
    if (A[i] < min) min = A[i];
}
printf("Max = %d, Min = %d\n", max, min);
```
### 7) Quadratic Equation Solver    二次方程求解器
Equation: ax² + bx + c = 0
```c
#include <stdio.h>
#include <math.h>
int main() {
    double a=1.0,b=4.0,c=3.0,d,ans1,ans2;
    d = b*b - 4*a*c;
    if (d >= 0) {
        ans1 = (-b + sqrt(d)) / (2*a);
        ans2 = (-b - sqrt(d)) / (2*a);
        printf("Real roots: %lf, %lf\n", ans1, ans2);
    } else {
        ans1 = -b / (2*a);
        ans2 = sqrt(-d)/(2*a);
        printf("Complex roots: %lf ± %lfi\n", ans1, ans2);
    }
    return 0;
}
```

---
### Key Points
- Bits, bytes, binary, and hexadecimal systems
- C program structure: #include, declarations, main body
- Data types and operators
- Conditional and loop constructs
- Arrays, sum, min, max programs
- Quadratic equation solver using math.h

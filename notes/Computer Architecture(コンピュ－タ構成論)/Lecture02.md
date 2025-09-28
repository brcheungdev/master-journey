#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor: Prof. Shinji Tomita (富田眞治)  

---
## Lecture 2
C Programming Structure, Integer Arithmetic, Debugging in Visual Studio  <br/>
C 程序结构、整数运算、Visual Studio 调试 
---
## ⚪ Lecture Content  
- C Program Structure  
  C 程序结构  
- Integer Addition and Division Examples  
  整数加法与除法示例  
- Visual Studio Environment and Key Terms  
  Visual Studio 环境与关键术语  
- Debugging Methods: Breakpoints, Step Execution  
  调试方法：断点、单步执行  
- Keyboard Input and Error Handling  
  键盘输入与错误处理  
- Assignment with Mathematical Functions  
  数学函数作业练习  

---

### 1) C Program Structure  
C 程序基本结构  

- Specified part (header files): `#include <...>`  
  指定部（头文件）：`#include <...>`  
- Declaration section: variables / function declarations  
  声明部：变量 / 函数声明  
- Main body (`main` function)  
  程序本体（`main` 函数）  

```c
#include <stdio.h>
#include <stdlib.h>

/* Integer addition */
int main(void) {
    int a, b, c;   // declaration
    a = 1;         // assignment
    b = 2;
    c = a + b;     // computation
    printf("Sum = %d\n", c);  // output
    return 0;
}
```
※/* ... */ for block comments; \n means newline; use standard ASCII quotes ", not curly quotes.
※ /* ... */ 为块注释；\n 是换行符；双引号必须是标准 ASCII "（不要用 Word 的弯引号）

### 2) Integer Arithmetic
整数运算：加法 / 除法 / 取余

```c
#include <stdio.h>
int main(void){
    int a=5, b=2, q, r;
    q = a / b;     // quotient
    r = a % b;     // remainder
    printf("Quotient = %d, Remainder = %d\n", q, r); // 2, 1
    return 0;
}
```
※Formula: dividend = quotient × divisor + remainder (e.g., 5 = 2×2 + 1). Division by zero (b=0) causes a runtime exception.

※公式：被除数 = 商 × 除数 + 余数（例如 5 = 2×2 + 1） 错误示例：b=0 会触发“除以 0”异常（runtime exception）。

### 3) Visual Studio Terms   VS术语速记
- Solution: container for large apps, can have multiple Projects
Solution：大型应用的容器，可含多个 Project
- Project: source code, libraries, resources container
Project：源代码、库、资源的容器
- Build: compile + link → machine code
Build：编译 + 链接 → 生成机器码
- Debug: run with debugging (breakpoints, step, variables)
Debug：带调试运行（断点、单步、变量观察）
- Common ops: Build Solution → Start Debugging
常用操作：Build Solution → Start Debugging
- Shortcuts: F10 Step Over, F11 Step Into
快捷键：F10 Step Over，F11 Step Into

### 4) Debugging Techniques 调试方法
- Compile-time errors: syntax/spelling errors, caught by the compiler
编译期错误：语法/拼写错误，编译器直接报错
- Runtime errors: divide by zero, type mismatch (int/float)
运行期错误：如除以 0、类型不当（int/float混用）
- Breakpoints: stop at a line to inspect the state
断点（Breakpoint）：在目标行停住，观察状态
- Variable windows:
变量窗口：
    - Auto: variables related to breakpoints
Auto（自动变量）：与断点相关的变量
    - Local: local variables in the current function
Local（局部）：当前函数内的局部变量

### 5) Keyboard Input 键盘输入示例（scanf_s）
```c
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int a, b, c;
    printf("Enter a: ");
    scanf_s("%d", &a);
    printf("Enter b: ");
    scanf_s("%d", &b);

    c = a + b;
    printf("Sum = %d\n", c);
    return 0;
}
```
Input two values at once:
一次输入两个值：
```c
scanf_s("%d%d", &a, &b);
printf("a=%d, b=%d\n", a, b);
```
### 6) Report Task   作业
- Input a=2, b=3 from keyboard
  从键盘输入 a=2, b=3
- Compute c = a^3 + b^4 (use pow(), need #include <math.h>)
  计算 c = a^3 + b^4（使用 pow() 需要 #include <math.h>）
- Output quotient and remainder of c / 8
  输出 c / 8 的商和余数
  
```c
#include <stdio.h>
#include <math.h>

int main(void){
    int a, b;
    long long c;        // 结果可能较大
    printf("Enter a and b: ");
    scanf_s("%d%d", &a, &b);

    c = (long long)pow(a,3) + (long long)pow(b,4);
    printf("c = %lld\n", c);

    int q = (int)(c / 8);
    int r = (int)(c % 8);
    printf("c/8 => quotient=%d, remainder=%d\n", q, r);
    return 0;
}
```
---
### Key Points
- Master C program's three-section structure: include → declarations → main  
  掌握 C 程序的三段式结构：include → 声明 → main  
- Use Visual Studio breakpoints + step execution to locate logic errors and observe variables  
  在 Visual Studio 中使用断点 + 单步执行定位逻辑问题，观察变量变化  
- Pay attention to integer vs floating types, standard quotes, and `\n` newline syntax  
  注意整数 / 浮点类型、标准双引号以及 `\n` 换行符的用法  

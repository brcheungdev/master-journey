#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
## Lecture 2

---
## ⚪ Lecture Content   讲座内容
C Programming Structure, Integer Arithmetic, Debugging in Visual Studio
- C Program Structure
- Integer Addition and Division Examples
- Visual Studio Environment and Key Terms
- Debugging Methods: Breakpoints, Step Execution
- Keyboard Input and Error Handling
- Assignment with Mathematical Functions

### 1) C Program Structure  C程序基本结构
- 指定部（头文件）：`#include <...>`
- 声明部：变量 / 函数声明
- 程序本体（`main` 函数）

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
※ /* ... */ 为块注释；\n 是下排的反斜杠换行；双引号必须是标准 ASCII "（不要用 Word 的弯引号）

### 2) Integer Arithmetic   整数运算：加法 / 除法 / 取余
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
※公式：被除数 = 商 × 除数 + 余数（例如 5 = 2×2 + 1） 错误示例：b=0 会触发“除以 0”异常（runtime exception）。

### 3) Visual Studio Terms   VS术语速记
- Solution：大型应用的容器，可含多个 Project
- Project：源代码、库、资源的容器
- Build：编译 + 链接 → 生成机器码
- Debug：带调试运行（断点、单步、变量观察）
- 常用操作：Build Solution → Start Debugging
- 快捷键：F10 Step Over，F11 Step Into

### 4) Debugging Techniques 调试方法
- 编译期错误：语法/拼写错误，编译器直接报错
- 运行期错误：如除以 0、类型不当（int/float混用）
- 断点（Breakpoint）：在目标行停住，观察状态
- 变量窗口：
    - Auto（自动变量）：与断点相关的变量
    - Local（局部）：当前函数内的局部变量

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
一次输入两个值：
```c
scanf_s("%d%d", &a, &b);
printf("a=%d, b=%d\n", a, b);
```
### 6) Report Task   作业
- 从键盘输入 a=2, b=3
- 计算 c = a^3 + b^4（使用 pow() 需要 #include <math.h>）
- 输出 c / 8 的商和余数
  
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
- 掌握 C 程序三段式：include → 声明 → main
- 用 VS 的 断点 + 单步 定位逻辑问题，观察变量
- 注意 整数/浮点 类型、标准双引号、\n 的反斜杠位置

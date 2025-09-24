#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 5: Functions, Parameter Passing & Pointers in C  
Functions, parameter passing (by value / by reference), pointers, globals, arrays & strings  函数、参数传递（按值传递/按引用传递）、指针、全局变量、数组和字符串

---

## ⚪ Lecture Overview
- What is a **function** and why we use it  
- Function **declaration** & **return values**; structure of `main`  
- **Parameter passing**: Call by Value vs Call by Reference  
- **Pointers**: address, dereference, pointer arithmetic  
- **Arrays** as function parameters (implicit by reference)  
- `scanf_s` input: numeric vs string arguments  
- **Global variables**: usage, pros & cons  
- Multiple ways to **return results** from functions

---

## ⚪ Lecture Content 讲座内容

### 1) What is a Function?  什么是函数
- 将“对不同数据执行相同处理”的逻辑抽成**函数**，主程序通过**实引数**传给函数的**形参**，函数计算后以**返回值**`return`结果给主程序使用。  
- **优点**：  
  - 代码体积更小、结构清晰（分而治之）  
  - 易于测试与复用（小规模单元易验证）  
  - 便于维护与修改  
- **缺点**：参数传递/调用会有开销，可能 **略微降低速度**。

---

### 2) Function Declaration & `main`  函数与主函数结构
**一般函数形式：**
```c
return_type func_name(type arg1, type arg2 /* ... */) {
    /* local declarations */
    /* statements ... */
    return value;   /* if return_type is not void */
}
```
主函数形式（返回 int）：
```c
int main(void) {
    /* local declarations */
    /* statements ... */
    return 0;   /* 可省略，但建议保留 */
}

```
※ 不能在函数内部再声明另一个函数（C 无函数嵌套）。void 用于“无返回值函数”或“无形参声明”（int main(void)）。

### 3) Simple Function Example 简单函数例
计算 1～n 的总和并返回：
```c
#include <stdio.h>
#include <stdlib.h>

int sum(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) s += i;
    return s;
}

int main(void) {
    int a = 10, b = 5;
    int sum1 = sum(a + b);   // 实参可为表达式
    int sum2 = sum(a - b);
    printf("sum(a+b) = %d\n", sum1); // 120
    printf("sum(a-b) = %d\n", sum2); // 15
    return 0;
}
```
### 4) Parameter Passing 参数传递：值传递 vs 引用传递
Call by Value（值传递）：把值的拷贝传入函数，函数内修改形参不影响实参。
```c
#include <stdio.h>

int add_then_change_i(int i, int j) {
    int s = i + j;
    i = 100;                 // 仅改变局部副本
    return s;
}

int main(void) {
    int a = 10, b = 5;
    int s = add_then_change_i(a, b);
    printf("a+b = %d\n", s);         // 15
    printf("a (unchanged) = %d\n", a); // 10
    return 0;
}
```
Call by Reference（引用传递）：传入地址，在函数内通过*解引用直接修改外部变量。
```c
#include <stdio.h>

int add_and_set_i100(int *i, int *j) {
    int s = *i + *j;
    *i = 100;               // 改变外部变量
    return s;
}

int main(void) {
    int a = 10, b = 5;
    int s = add_and_set_i100(&a, &b);
    printf("a+b = %d\n", s);     // 15
    printf("a (changed) = %d\n", a); // 100
    return 0;
}
```
※ &x 取地址，*p 取指针指向内容。传数组实参时无需 &（见第 6 节）。

### 5) scanf_s Input 输入：数值 vs 字符串
数值输入必须传地址：
```c
int a;  scanf_s("%d", &a);
double x; scanf_s("%lf", &x);
```
字符串输入（数组名即地址），并需传缓冲区大小**：
```c
char name[16];
scanf_s("%s", name, 16);  // VS 安全扩展：必须写入缓冲区大小
printf("name = %s\n", name);
```
※ 若对数值忘记写 &，将无法把输入写回变量。字符串（char[]）为数组名，隐式按引用传递；未提供大小将报错（VS 的 _s 系列）。

### 6) Arrays as Parameters 数组作形参（隐式按引用）
推荐：携带长度参数的通用写法
```c
#include <stdio.h>

int sum_array(int A[], int m) {
    int s = 0;
    for (int i = 0; i < m; i++) s += A[i];
    return s;
}

int main(void) {
    int B[] = {3,5,1,4,9,2,6,10,8,7};
    int C[] = {3,5,1,4,9,2,6,10,8,7,11};
    printf("sum(B) = %d\n", sum_array(B, 10));
    printf("sum(C) = %d\n", sum_array(C, 11));
    return 0;
}
```
等价的指针形参写法（指针走位）：
```c
int sum_array_ptr(int *pB, int m) {
    int s = 0;
    for (int i = 0; i < m; i++) { s += *pB; pB++; }
    return s;
}
```
※ sum_array(&B, n) ❌（类型不匹配）；应传 B 或 &B[0]。把形参写成固定长度 int A[10] 会限制适用性；携带 m 更通用。

### 7) Pointer Basics & Pointer Arithmetic 指针基础
变量与指针的最小示例：
```c
int a = 123;
int *p = &a;      // p 保存 a 的地址
int c = *p + 1;   // 读出 a 的值做计算（等同 c = a + 1）
```
指针与数组（以 int 为例）：
- int A[10]; int *p = &A[0];
- p+1 实际向前移动 sizeof(int) 个字节（通常为 4）。
- *p 读取当前元素内容；*(p+1) 读取下一个元素。
字符与字符串：
- char *s = "ABC"; printf("%s\n", s);
- 字符串以**'\0' 结尾**；二维字符数组可存放多行短字符串。
- 注意 %p 用于打印地址，%s 打印以 '\0' 结尾的字符串。

### 8) Global Variables 大域变量
特性：所有函数可共享同一份数据，读写方便但降低封装性、可能让程序更难理解与维护。
示例：函数调用次数计数
```c
#include <stdio.h>

int g_count = 0;              // global

int sum2(int i, int j) {
    g_count++;                // 记录调用
    return i + j;
}

int main(void) {
    int a = 10, b = 5;
    printf("%d\n", sum2(a, b));   // 15
    g_count += 2;                  // 主程序也可修改
    printf("g_count = %d\n", g_count);
    return 0;
}
```
用全局变量“返回”结果的方式（不推荐作为常规做法）：
```c
#include <stdio.h>

int gs, gc;            // gs: result, gc: loop count

void sum_to_gc(void) { // 无形参、无显式返回值
    gs = 0;
    for (int i = 1; i <= gc; i++) gs += i;
}

int main(void) {
    int a = 10, b = 5;
    gc = a + b; sum_to_gc(); printf("sum(a+b) = %d\n", gs);
    gc = a - b; sum_to_gc(); printf("sum(a-b) = %d\n", gs);
    return 0;
}
```
※ 优先使用 返回值 或 引用传递 返回结果；全局变量留作必要时使用。

### 9) Ways to Return Results 返回结果的三种方式
- return 单一返回值（简单清晰；不能直接返回数组）
- 引用传递（通过指针“输出多个值”或“返回数组内容”）
- 全局变量（共享快速，但不利封装与测试）

---
### Key Points 
- 掌握函数的声明/调用/返回与 main 的规范写法
- 理解 值传递 与 引用传递 的本质（拷贝 vs 地址）
- 熟悉 指针 与 数组 的关系及指针算术
- 记住 scanf_s 在 数字与字符串参数上的不同写法
- 使用 数组作形参 时默认按引用传递；携带长度参数更通用
- 谨慎使用 全局变量；优先考虑返回值/引用返回

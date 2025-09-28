#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor: Prof. Shinji Tomita (富田眞治)  

---

# Lecture 6: Recursion, Performance, I/O, Structs & Dynamic Memory
Recursive functions & iteration, time measurement, `printf/scanf_s`, structs, dynamic memory, lists, paradigms (procedural/declarative, Lisp), compiler vs interpreter  
递归函数与迭代、时间测量、`printf/scanf_s` 函数、结构体、动态内存、列表、范式（过程式/声明式、Lisp）、编译器与解释器

---

## ⚪ Lecture Overview
- What recursion is; factorial & divide-and-conquer sum  
  递归的概念；阶乘与分治求和  
- Recursion vs iteration: **performance measurement**  
  递归与迭代：**性能比较**  
- `printf` format specifiers & `scanf_s` (safe input in VS)  
  `printf` 格式控制符与 `scanf_s`（Visual Studio 中的安全输入）  
- **Structs** (`typedef`, dot/arrow), struct-in-struct, array of structs  
  **结构体**（`typedef`，点 / 箭头操作符）、结构体嵌套、结构体数组  
- **Dynamic memory**: `malloc/calloc/free` and pointer basics  
  **动态内存**：`malloc/calloc/free` 及指针基础  
- **Linked lists** (self-referential structs) & node insertion  
  **链表**（自引用结构体）与节点插入  
- Programming paradigms: procedural vs declarative (SQL/Prolog), functional (Lisp)  
  编程范式：命令式 vs 声明式（SQL / Prolog），函数式（Lisp）  
- High-level language processing: compiler vs interpreter, macros, split compilation  
  高级语言处理：编译器 vs 解释器，宏，分离编译  

---

## ⚪ Lecture Content 讲座内容

### 1) Recursion Basics & Factorial 递归与阶乘
**Recursion**: a function that calls itself until a base case.  
**递归**：一个函数不断调用自身，直到满足基例条件。

```c
#include <stdio.h>

int FACT(int i) {
    if (i == 1) return 1;         /* base case */
    else        return i * FACT(i - 1);
}

int main(void) {
    int s = FACT(10);
    printf("Recursive factorial 10! = %d
", s);  /* 3628800 */
    return 0;
}
```
Call flow (3! example): FACT(3) → FACT(2) → FACT(1) → return chain.  
调用流程 (3! 示例)：FACT(3) → FACT(2) → FACT(1) → 返回链。

---

### 2) Divide & Conquer Sum 递归分治求和 vs 迭代求和
```c
/* Recursively compute sum from i..j */
int SUM(int i, int j) {
    if (i == j) return i;
    int mid = (i + j) / 2;           /* integer division */
    return SUM(i, mid) + SUM(mid + 1, j);
}
```
Iterative sum (for comparison):  
迭代求和（对比用）：
```c
int iter_sum_1_to_1000(void){
    int s = 0;
    for (int i = 1; i <= 1000; i++) s += i;
    return s;                         /* 500500 */
}
```

---

### 3) Measuring Time 递归与迭代性能对比
Compare recursion vs iteration for summing 1..1000 repeated 1,000,000 times.  
对同一任务（1..1000 求和）循环 1,000,000 次，比较递归与迭代的耗时。  
Demonstrates both time_t/difftime and clock() usage.  
演示了 time_t/difftime 与 clock() 的两种计时方式。

```c
#include <stdio.h>
#include <time.h>

int SUM(int i, int j){
    if (i == j) return i;
    int m = (i + j) / 2;
    return SUM(i, m) + SUM(m + 1, j);
}

int main(void){
    const int LOOP = 1000000;
    int s; clock_t t0, t1; double sec;

    /* Recursive */
    t0 = clock();
    for (int k = 0; k < LOOP; k++) s = SUM(1, 1000);
    t1 = clock();
    sec = (t1 - t0) / (double)CLOCKS_PER_SEC;
    printf("Recursive sum=%d, time=%.6f sec
", s, sec);

    /* Iterative */
    t0 = clock();
    for (int k = 0; k < LOOP; k++){
        s = 0; for (int i = 1; i <= 1000; i++) s += i;
    }
    t1 = clock();
    sec = (t1 - t0) / (double)CLOCKS_PER_SEC;
    printf("Iterative sum=%d, time=%.6f sec
", s, sec);
    return 0;
}
```
Note: recursion adds call overhead; iteration is usually faster.  
注意：递归函数有调用开销，迭代通常更快。

---

### 4) printf & scanf_s I/O   printf 常用说明
printf common specifiers: %d, %f, %lf, %c, %s, %p; precision like %.2lf.  
printf 常用控制符：%d, %f, %lf, %c, %s, %p；精度控制示例：%.2lf → 小数点后两位。

scanf_s in VS: numbers need `&`, strings need buffer length.  
在 VS 中，scanf_s 数值参数需 `&`，字符串需指定缓冲区长度：

数值一定要传地址：scanf_s("%d", &a);、scanf_s("%lf", &x);
字符串传数组名（即地址）且必须提供缓冲区大小：
```c
char name[16];
scanf_s("%s", name, (unsigned)_countof(name));
```
Missing & (numbers) or buffer length (strings) causes errors.  
忘记写 &（数值）或忘记写缓冲区大小（字符串，在 VS 的 _s 系列）会出错。

---

### 5) Structs & Member Access 结构体与成员访问
```c
typedef struct student {
    char  name[32];
    int   flan, math, sci, soc, lang;
    float average;
} Student;

/* Using dot/arrow and functions to update members */
float Average(Student *p){
    p->average = (p->flan + p->math + p->sci + p->soc + p->lang) / 5.0f;
    return p->average;
}

int main(void){
    Student yamada = {"yamada_taro",90,80,75,60,80,0};
    printf("After update avg = %.2f
", Average(&yamada));
    return 0;
}
```
Struct in Struct (nested):  
结构体嵌套示例：
```c
typedef struct node {
    Student a;
    int     b;
} Node;
```
Member access: node.a.average; pointer: p->a.name  
成员访问：node.a.average；指针访问：p->a.name  
Array of Structs: Student A[] = {yamada, aoki}; average = (A[0].flan + A[1].flan)/2  
结构体数组：Student A[] = {yamada, aoki}; 平均分 = (A[0].flan + A[1].flan)/2  

---

### 6) Dynamic Memory & Self-referential Structs 动态内存与自引用
```c
/* Minimal calloc demo (check NULL, free after use) */
int *a = (int*)calloc(1, sizeof(int));
if (!a) { /* error */ } else { *a = 123; /* use */ }
free(a);
```
Singly Linked List: insert at head  
单向链表：插入到表头  
```c
typedef struct node {
    Student a;
    struct node *next;
} Node;

typedef struct list {
    Node *head;
} List;

void init(List *lst){ lst->head = NULL; }

Node* alloc_node(void){
    return (Node*)calloc(1, sizeof(Node));
}

void set_node(Node *n, const Student *x){
    n->a = *x; n->next = NULL;
}

void insert_front(List *lst, const Student *x){
    Node *p = alloc_node();
    set_node(p, x);
    p->next = lst->head;
    lst->head = p;
}
```

---

### 7) Programming Paradigms & Preprocessing 编程范式与预处理
- Procedural/Imperative → sequence/branch/loop; structured programming (Dijkstra)  
  命令式 → 顺序/分支/循环；结构化程序设计（Dijkstra）
- Declarative → SQL/Prolog describe "what" not "how"  
  声明式 → SQL/Prolog 描述“是什么”而非“如何做”
- Functional (Lisp) → functions, no side effects, recursion; car/cdr/cons/append  
  函数式 (Lisp) → 函数、无副作用与递归；car/cdr/cons/append 等
- Macros & Preprocessor: #define, #include, split compilation & linking  
  宏与预处理：#define、#include、分离编译与链接
- Compiler vs Interpreter: speed vs interactivity/debug; JIT compromise  
  编译器 vs 解释器：速度 vs 交互性/易调试；JIT 折中方案  

---

### 8) Extra: Inner Product & Loop Unrolling 额外示例：向量内积与循环展开
```c
int A[10], B[10], s1=0, s2=0;
for (int i=0;i<10;i++){ A[i]=i+1; B[i]=10-i; }
for (int i=0;i<=8;i+=2){ s1 += A[i]*B[i]; s2 += A[i+1]*B[i+1]; }
printf("Inner product = %d
", s1+s2);
```

---

### Key Points 
- Recursion = base case + smaller subproblems; iteration usually faster  
  递归 = 基例 + 缩小问题规模；迭代通常更高效  
- Use clock()/difftime for timing code execution  
  用 clock()/difftime 进行代码计时  
- scanf_s: numbers need &var; strings need buffer length  
  scanf_s：数值需 &var；字符串需指定缓冲区长度  
- Struct access: dot for variables, arrow for pointers; nested structs, struct arrays  
  结构体访问：变量用点，指针用箭头；支持嵌套结构体和结构体数组  
- Dynamic memory and singly linked list basics  
  动态内存与单链表基础操作  
- Programming paradigms, compilation vs interpretation differences  
  编程范式、编译与解释的差异  

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
## Lecture 4
Repetition Statements, Arrays, String Operations, Sorting Algorithms <br/>
 重复语句、数组、字符串操作、排序算法

---
## ⚪ Lecture Overview 
- Repetition Statements: for, while, do-while  
  重复语句：for、while、do-while  
- One-dimensional and Two-dimensional Arrays  
  一维和二维数组  
- String Handling with string.h  
  使用 string.h 进行字符串处理  
- Array Applications: Sum, Product, Max/Min  
  数组应用：求和、乘积、最大值/最小值  
- Sorting Algorithms: Bubble Sort  
  排序算法：冒泡排序  
- Report Assignment: Max/Min with Multiple Indices  
  报告作业：带多个索引的最大/最小值问题  

---
## ⚪ Lecture Content 讲座内容
### 1) Repetition Statements – Loops      重复语句 - 循环
For loop (known iteration count):         “for”循环（已知迭代次数）：
```c
/* Sum from 1 to 10 using for loop */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i, s = 0;
    for (i = 1; i <= 10; i++)
        s = s + i;
    printf("Sum(1-10) = %d\n", s);
    return 0;
}
```
While loop (unknown iteration count):    “while”循环（未知循环次数）：
```c
/* Product of odd numbers until product >= 5000 */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int max = 5000;
    int s = 1, i = 1;
    while (s < max) {
        s = s * i;
        i = i + 2;
    }
    printf("Last odd = %d\n", i - 2);
    printf("Product = %d\n", s);
    return 0;
}
```
Do-While loop (executes at least once):  “do-while”循环（至少会执行一次）：
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int max = 5000;
    int s = 1, i = 1;
    do {
        s = s * i;
        i = i + 2;
    } while (s < max);
    printf("Last odd = %d\n", i - 2);
    printf("Product = %d\n", s);
    return 0;
}
```

### 2) One-dimensional & Two-dimensional Arrays    一维数组与二维数组
- Declaration:
```c
int A[10];          // 1D array
int B[5][5];        // 2D array (5x5)
char name[20];      // char array (string)
```
- Index starts at 0
- Initialization:
```c
int A[] = {1,2,3};         // size inferred
char str[] = "Hello";      // includes '\0'
```

### 3) String Operations – <string.h>          字符串操作 - <string.h>
String length & copy:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char str1[20] = "Hello";
    char str2[20] = "World";

    printf("Length = %d\n", (int)strlen(str1));
    strcpy_s(str1, 20, str2);       // copy str2 → str1
    strcat_s(str1, 20, "!!!");      // concatenate
    printf("After copy+concat: %s\n", str1);
    return 0;
}
```
String input:
```c
char name[10];
scanf_s("%s", name, 10);
printf("You entered: %s\n", name);
```

### 4) Array Applications        数组应用
Sum of array elements:
```c
int A[10], s = 0;
for (int i = 0; i < 10; i++) A[i] = i+1;
for (int i = 0; i < 10; i++) s += A[i];
printf("Sum = %d\n", s);
```
Product of two arrays:
```c
int A[10], B[10], s = 0;
for (int i = 0; i < 10; i++) { A[i] = i+1; B[i] = 10-i; }
for (int i = 0; i < 10; i++) s += A[i]*B[i];
printf("Sum of products = %d\n", s);
```
Max & Min values:
```c
int A[] = {3,5,1,4,9,2,6,10,8,7};
int max=A[0], min=A[0], max_i=0, min_i=0;
for (int i=1;i<10;i++){
    if(A[i]>max){ max=A[i]; max_i=i; }
    if(A[i]<min){ min=A[i]; min_i=i; }
}
printf("max=%d idx=%d  min=%d idx=%d\n", max,max_i,min,min_i);
```

### 5) Sorting Algorithm – Bubble Sort      排序算法 - 冒泡排序
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int A[] = {3,5,1,4,9,2,6,10,8,7};
    int n=10,temp;
    for (int i=0;i<n-1;i++){
        for (int j=n-1;j>i;j--){
            if(A[j-1]>A[j]){
                temp=A[j-1]; A[j-1]=A[j]; A[j]=temp;
            }
        }
    }
    for (int i=0;i<n;i++) printf("%d ",A[i]);
    printf("\n");
    return 0;
}
```

---
### Key Points
- for, while, do-while repetition statements  
  for、while、do-while 三种循环语句  
- One & two-dimensional arrays, string operations  
  一维和二维数组，字符串操作  
- Array applications: sum, product, max, min, sorting  
  数组应用：求和、乘积、最大值、最小值、排序  
- Handling duplicates in arrays & bubble sort basics  
  处理数组中的重复元素与冒泡排序基础  

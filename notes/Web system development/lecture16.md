[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 16: JavaScript Functions — Definition, Arguments, Return, Scope, and Built-ins  
# 第16讲：JavaScript 函数 —— 定义、参数、返回值、作用域与内置函数

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Is a Function & Why](#what-is-a-function--why)  
- 什么是函数与为什么要用
- [Define a Function](#define-a-function)  
- 定义函数
- [Call/Invoke a Function](#callinvoke-a-function)  
- 调用/执行函数
- [Arguments & Parameters (Single/Multiple)](#arguments--parameters-singlemultiple)  
- 参数与形参与实参（单参/多参）
- [Return Values (`return`)](#return-values-return)  
- 返回值（`return`）
- [Scope: Parameters & `let` (Block Scope)](#scope-parameters--let-block-scope)  
- 作用域：形参与 `let`（块级作用域）
- [Event-driven Calls: Button `onClick`](#event-driven-calls-button-onclick)  
- 事件驱动调用：按钮 `onClick`
- [Built-in Functions & Methods (String/Number)](#builtin-functions--methods-stringnumber)  
- 内置函数与方法（字符串/数值）
- [`substring()` Details (Indexing from 0)](#substring-details-indexing-from-0)  
- `substring()` 细节（从 0 开始的索引）
- [Method Call vs Function Call](#method-call-vs-function-call)  
- 方法调用 vs 函数调用
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## What Is a Function & Why  
## 什么是函数与为什么要用

- A **function** groups **multiple statements** under a **name** so you can call them **anytime, repeatedly**.  
- **函数**将**多条语句**按一个**名称**封装，便于**随时、重复**调用。  
- Benefits: **reuse** (no need to re‑write similar code), **readability**, and **black‑box** usage (know inputs/outputs only).  
- 好处：**复用**（无需重复写相似代码）、**可读性**更高，以及**黑箱**使用（只需了解输入/输出）。  
- Learn to use **built-ins** like **`parseInt()`**, **`Number()`** effectively; and to **write your own** functions.  
- 要熟练使用 **`parseInt()`**、**`Number()`** 等**内置函数**，并学会**自定义**函数。  

---

## Define a Function  
## 定义函数

```js
function greet() {
  // process goes here
  // 在此编写处理逻辑
}
```
- Syntax: `function` + **name** + `()` + **block `{}`**.  
- 语法：`function` + **函数名** + `()` + **代码块 `{}`**。  
- **Only defining** doesn’t execute; you must **call** it.  
- **仅定义**不会执行；必须**调用**才会运行。  

---

## Call/Invoke a Function  
## 调用/执行函数

```js
greet(); // call it
// 调用函数
```
- Write the **name followed by `()`** to **run** the function body.  
- 书写**函数名加 `()`** 即可**执行**函数体。  

---

## Arguments & Parameters (Single/Multiple)  
## 参数与形参与实参（单参/多参）

```js
// definition with a parameter / 含形参的定义
function greeting(msg) {
  console.log(msg);
}
// call with a literal / 字面量作为实参
greeting("おはよう！");
// call with a variable / 变量作为实参
let word = "こんにちは";
greeting(word);

// multiple parameters / 多个参数
function add(x, y) {
  const nx = parseInt(x, 10);
  const ny = parseInt(y, 10);
  return nx + ny;
}
const z = add("12", "34"); // 46
```
- **Arguments** (actual values) are passed in the **call**; **parameters** (placeholders) are **declared in the definition**.  
- **实参**在**调用**时传入；**形参**在**定义**时声明。  
- With **multiple** params, separate by **commas**; actuals are **positionally** assigned.  
- **多参数**用**逗号**分隔；实参按**位置对应**赋给形参。  

---

## Return Values (`return`)  
## 返回值（`return`）

```js
function add(x, y) {
  return Number(x) + Number(y);
}
const total = add(3, 5); // total = 8
```
- Use **`return <value>`** to send a result **back to the caller**.  
- 使用 **`return <值>`** 将结果**返回给调用处**。  
- Functions can be of **two types**: **with return** (capture into a variable) and **no return** (just perform an action).  
- 函数可分为**有返回值**（用变量接收）与**无返回值**（仅执行动作）两类。  

---

## Scope: Parameters & `let` (Block Scope)  
## 作用域：形参与 `let`（块级作用域）

```js
function add(x, y) {
  const z = Number(x) + Number(y);
  return z;
}
console.log(typeof z); // ReferenceError: z is not defined
// 作用域示例：z 只在函数块内有效
{
  let i = 10;
}
// console.log(i); // ReferenceError
```
- **Parameters** and variables declared with **`let`** inside a function/block are **local** to that **block**.  
- **形参**与在函数/块中用 **`let`** 声明的变量**仅在该块内有效**。  
- Outside the block, they are **not visible**.  
- 离开该块，变量**不可见**。  

---

## Event-driven Calls: Button `onClick`  
## 事件驱动调用：按钮 `onClick`

```html
<button onClick="show('OK')">押してね</button>
<script>
  function show(message) {
    window.alert(message);
  }
</script>
```
- Putting a function call in **`onClick`** runs it when the **button is clicked**.  
- 在 **`onClick`** 属性里写函数调用可在**按钮被点击**时执行。  
- Mind the quotes: **HTML attribute uses double quotes**, inner **string uses single quotes** (or escape accordingly).  
- 注意引号：**HTML 属性用双引号**，内部**字符串用单引号**（或适当转义）。  

---

## Built-in Functions & Methods (String/Number)  
## 内置函数与方法（字符串/数值）

```js
let str1 = "ABCDE";
str1 = str1.toLowerCase();   // "abcde"
str1 = str1.substring(1, 3); // "bc"

let num = 123;
let s = num.toString();      // "123"
```
- JavaScript provides **built‑ins** for common tasks per **type** (String/Number/…); see **MDN Reference** for the catalog.  
- JavaScript 针对各**数据类型**提供了**内置方法/函数**（字符串/数值/…）；目录详见 **MDN 参考**。  

---

## `substring()` Details (Indexing from 0)  
## `substring()` 细节（从 0 开始的索引）

- Syntax: **`substring(indexStart [, indexEnd])`**; returns chars from **`indexStart` up to but not including `indexEnd`**.  
- 语法：**`substring(indexStart [, indexEnd])`**；返回从 **`indexStart` 到（但不含）`indexEnd`** 的子串。  
- If **`indexEnd` omitted**, it returns **to the end** of the string.  
- 若**省略 `indexEnd`**，则从起始位置一直取到**字符串末尾**。  
- **Index starts at `0`** (not 1).  
- **索引从 `0` 开始**（不是 1）。  

---

## Method Call vs Function Call  
## 方法调用 vs 函数调用

```js
let str = "ABC";
// Not: toLowerCase(str)   // 不是这样
str = str.toLowerCase();    // 调用“方法”：点号写法
```
- Many string/number operations are **methods** called via **dot notation on a value/variable**.  
- 许多字符串/数值操作是**方法**，通过**在值/变量上使用点号**调用。  
- Why not pass the variable as an argument? This **method binding** model will be explained in the **next lecture**.  
- 为什么不写成“把变量作为参数传入”？这种**方法绑定**模型会在**下一讲**解释。  

---

## Practice Tasks  
## 练习任务

1) **Refactor greeting**: extract repeated greeting prints into a **`greeting(msg)`** function; call it with **three messages**.  
1) **重构问候**：将重复的问候打印提炼为 **`greeting(msg)`** 函数；用**三种消息**调用它。  
2) **Adder with return**: write **`add(x, y)`** converting inputs to numbers and **`return`** the sum; show the result.  
2) **带返回的加法器**：编写 **`add(x, y)`** 将入参转数值并 **`return`** 求和；输出结果。  
3) **Button click**: create a **button** with `onClick="show('OK')"` and implement **`show(message)`** to `alert` it.  
3) **按钮触发**：创建带 `onClick="show('OK')"` 的**按钮**并实现 **`show(message)`** 弹窗显示。  
4) **Substring drill**: prompt a word and print **`toLowerCase()`**, **`substring(1, 3)`**, and **`toString()` for numbers**.  
4) **子串练习**：输入一段文本并打印 **`toLowerCase()`**、**`substring(1, 3)`**，以及**数值的 `toString()`**。  

---

## Quick Checklist  
## 快速清单

- **Define** with `function name(){…}`; **call** with `name()`.  
- **定义**用 `function name(){…}`；**调用**用 `name()`。  
- Distinguish **parameters** (in definition) vs **arguments** (in call); multiple arguments map by **position**.  
- 区分**形参**（定义处）与**实参**（调用处）；多参数按**位置**对应。  
- Use **`return`** to send results back; capture in a **variable**.  
- 用 **`return`** 返回结果；在**变量**中接收。  
- **`let` is block‑scoped**; variables/parameters inside a function/block are **not visible outside**.  
- **`let` 为块级作用域**；函数/块内部的变量/形参**在外部不可见**。  
- Prefer **built‑ins** (`toLowerCase`, `substring`, `toString`, `parseInt`, `Number`) for common tasks.  
- 常见操作优先使用**内置方法/函数**（`toLowerCase`、`substring`、`toString`、`parseInt`、`Number`）。  
- For quick demos, **`onClick`** can call a function; mind **quote nesting** in attributes.  
- 快速演示可用 **`onClick`** 调函数；注意属性里的**引号嵌套**。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture15.md) · [Next Lecture / 下一讲 →](./lecture17.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

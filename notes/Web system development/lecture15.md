[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 15: JavaScript Conditionals — `if/else`, `else if`, Nested, and `switch`  
# 第15讲：JavaScript 条件分支 —— `if/else`、`else if`、嵌套与 `switch`

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Why We Need Branching](#why-we-need-branching)  
- 为什么需要分支
- [Boolean (True/False) Basics](#boolean-truefalse-basics)  
- 真偽值（布尔）的基础
- [Comparison Operators & Results](#comparison-operators--results)  
- 比较运算符与返回结果
- [Console Output & Trying Examples](#console-output--trying-examples)  
- 控制台输出与动手实验
- [`if` (Single Branch)](#if-single-branch)  
- `if`（单分支）
- [`if … else` (Two-Way Branch)](#if--else-twoway-branch)  
- `if … else`（二分支）
- [`if … else if … else` (Multi-Way)](#if--else-if--else-multiway)  
- `if … else if … else`（多分支）
- [Logical Operators `&&` `||` `!`](#logical-operators---)  
- 逻辑运算符 `&&` `||` `!`
- [Nested Conditions (Indentation)](#nested-conditions-indentation)  
- 条件嵌套（缩进与可读性）
- [`switch` with `case` and `break`](#switch-with-case-and-break)  
- `switch` 与 `case`、`break`
- [Random Numbers & Fortune Example](#random-numbers--fortune-example)  
- 随机数与运势示例
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Notes & Tips (Optional)](#notes--tips-optional)  
- 注释与小贴士（可选）

---

## Why We Need Branching  
## 为什么需要分支

- A program runs **top-to-bottom** by default; branching **chooses different actions** based on **conditions**.  
- 程序默认**自上而下**执行；条件分支用于根据**条件**选择**不同的处理**。  

```
Button pressed? → Yes → proceed
               → No  → wait
按钮被按下？ → 是 → 继续
           → 否 → 等待
```

---

## Boolean (True/False) Basics  
## 真偽值（布尔）的基础

- JavaScript core types include **Number**, **String**, **Boolean**, plus **`null`** and **`undefined`**.  
- JavaScript 的核心类型包含 **Number**、**String**、**Boolean**，以及 **`null`** 与 **`undefined`**。  
- **Booleans** are either **`true`** or **`false`** and drive **yes/no** decisions.  
- **布尔值**只有 **`true`** 或 **`false`**，用于表示**是/否**判断。  

---

## Comparison Operators & Results  
## 比较运算符与返回结果

- Comparing two values yields a **Boolean** (`true`/`false`).  
- 比较两个值会得到一个**布尔值**（`true`/`false`）。  
- Operators: **`==`**, **`===`**, **`!=`**, **`!==`**, **`>`**, **`>=`**, **`<`**, **`<=`**.  
- 常用运算符：**`==`**、**`===`**、**`!=`**、**`!==`**、**`>`**、**`>=`**、**`<`**、**`<=`**。  

```js
5 == 5        // true (loose equality / 宽松相等)
5 === 5       // true (strict equality / 严格相等：值与类型都相等)
5 != 5        // false
5 !== 5       // false
5 == "5"      // true (string coerces to number / 字符串被数值化)
5 === "5"     // false (types differ / 类型不同)
5 > 5         // false
5 >= 5        // true
5 < 5         // false
5 <= 5        // true
```

---

## Console Output & Trying Examples  
## 控制台输出与动手实验

- Open **Chrome DevTools → Console** to see `console.log(...)` outputs.  
- 打开 **Chrome 开发者工具 → Console** 查看 `console.log(...)` 的输出。  
- Create a test page (e.g., **`wp02-1.html`**) and try comparisons directly in the console.  
- 建立测试页（如 **`wp02-1.html`**），在控制台中直接尝试各类比较表达式。  

---

## `if` (Single Branch)  
## `if`（单分支）

- Syntax: run the **block** only when the **condition is `true`**.  
- 语法：仅当**条件为 `true`** 时执行**代码块**。  

```html
<script>
  const h = 12;
  if (h < 12) {
    console.log("おはよう"); // Good morning / 早上好
  }
</script>
```

---

## `if … else` (Two-Way Branch)  
## `if … else`（二分支）

- Choose **one of two** blocks based on the condition.  
- 根据条件在**两个分支**之间做出选择。  

```html
<script>
  const h = 15;
  if (h < 12) {
    console.log("おはよう");
  } else {
    console.log("こんにちは");
  }
</script>
```

---

## `if … else if … else` (Multi-Way)  
## `if … else if … else`（多分支）

- Chain multiple conditions with **`else if`**; the **first matching** branch runs.  
- 用 **`else if`** 链接多个条件；**第一个满足**的分支会被执行。  

```html
<script>
  const h = 20;
  if (h < 12) {
    console.log("おはよう");
  } else if (h < 17) {
    console.log("こんにちは");
  } else {
    console.log("こんばんは");
  }
</script>
```

---

## Logical Operators `&&` `||` `!`  
## 逻辑运算符 `&&` `||` `!`

- Combine conditions: **`&&` (and)**, **`||` (or)**, **`!` (not)**.  
- 组合条件：**`&&`（且）**、**`||`（或）**、**`!`（非）**。  
- Example: “`a` is in **[1, 5)**” → `1 <= a && a < 5` (don’t write `1 <= a < 5`).  
- 例：判断 “`a` 在 **[1, 5)**” → `1 <= a && a < 5`（不要写成 `1 <= a < 5`）。  

```js
const a = 3;
if (1 <= a && a < 5) { console.log("in range"); }
if (a < 0 || a >= 100) { console.log("out of range"); }
```

---

## Nested Conditions (Indentation)  
## 条件嵌套（缩进与可读性）

- You can **nest** `if` statements to express **hierarchies** of checks; use **indentation** to keep code readable.  
- 可**嵌套** `if` 语句表达**层级判断**；使用**缩进**保持代码可读。  

```js
const computer = 40;
const database = 50;

if (computer >= 60) {
  console.log("Computer: OK");
} else {
  if (database >= 60) {
    console.log("DB: OK");
  } else {
    console.log("Both under 60");
  }
}
```

---

## `switch` with `case` and `break`  
## `switch` 与 `case`、`break`

- `switch (target) { case value: …; break; default: …; }` handles **discrete values** more cleanly than many `else if`s.  
- 当比较**离散值**时，使用 `switch (表达式) { case 值: …; break; default: …; }` 比大量 `else if` 更清晰。  
- Always put **`break`** at the end of each **`case`** to **prevent fall‑through** (unless intentionally used).  
- 在每个 **`case`** 末尾写上 **`break`**，以**防止落空穿透**（除非有意为之）。  

```html
<script>
  const lang = "ja";
  switch (lang) {
    case "en":
      console.log("Hello");
      break;
    case "ja":
      console.log("こんにちは");
      break;
    default:
      console.log("Hi");
      break;
  }
</script>
```

---

## Random Numbers & Fortune Example  
## 随机数与运势示例

- **`Math.random()`** returns a **float in [0, 1)**; multiply and **`parseInt`** to get an **integer range**.  
- **`Math.random()`** 返回 **[0,1)** 的浮点数；乘以范围并用 **`parseInt`** 取得**整数**。  

```html
<!-- 0, 1, or 2 -->
<script>
  const n = parseInt(Math.random() * 3, 10);
  switch (n) {
    case 0:
      window.alert("あなたの運勢は最高です！");
      break;
    case 1:
      window.alert("あなたの運勢は最悪です");
      break;
    default:
      window.alert("あなたの運勢は普通です");
      break;
  }
</script>
```

---

## Quick Checklist  
## 快速清单

- **`===`** for **strict comparison**; **avoid** relying on **type coercion** with `==`.  
- 使用 **`===`** 进行**严格比较**；**避免**依赖 `==` 的**类型转换**。  
- Combine ranges with **`&&`/`||`**; don’t chain comparisons like `1 <= a < 5`.  
- 区间判断用 **`&&`/`||`**；不要写成 `1 <= a < 5`。  
- Keep **indentation** consistent for nested logic.  
- 嵌套逻辑请保持**缩进一致**。  
- In `switch`, **remember `break`** and include a **`default`** branch.  
- 在 `switch` 中**别忘了 `break`**，并写上 **`default`**。  
- Use **DevTools Console** to verify conditions and outputs.  
- 使用 **开发者工具控制台**验证条件与输出。  

---

## Practice Tasks  
## 练习任务

1) **Greeting by hour**: Prompt for an **hour (0–23)** and print **「おはよう/こんにちは/こんばんは」** with multi-way `if`.  
1) **按小时问候**：提示输入**小时（0–23）**，用多分支 `if` 输出 **「おはよう/こんにちは/こんばんは」**。  
2) **Range check**: Input a number and print whether it’s in **[1, 5)** using `&&`.  
2) **区间判断**：输入一个数字，用 `&&` 判断是否在 **[1, 5)**。  
3) **Score → rank**: With `switch` on a **letter grade** (`"A"`, `"B"`, …), output a message; include `default`.  
3) **分数→等级**：对**等级字母**（`"A"`、`"B"` …）使用 `switch` 输出信息；包含 `default`。  
4) **Fortune**: Generate **0/1/2** with `Math.random()` and show the fortune messages via `switch`.  
4) **运势**：用 `Math.random()` 生成 **0/1/2** 并用 `switch` 输出运势提示。  

---

## Notes & Tips 
## 注释与小贴士

<details><summary>Equality, coercion, and numeric input / 相等性、类型转换与数字输入</summary>

- `==` performs **type coercion**; prefer **`===`** to avoid surprises (`"5" == 5` is `true`).  
- `==` 会进行**类型转换**；建议使用 **`===`** 避免意外（`"5" == 5` 为 `true`）。  
- Values from **`prompt`** are **strings**; convert with **`parseInt(str, 10)`**, **`parseFloat`**, or **`Number`**.  
- **`prompt`** 返回的是**字符串**；请用 **`parseInt(str, 10)`**、**`parseFloat`** 或 **`Number`** 转为数字。  
- In JS, `Number(true) → 1`, `Number(false) → 0`; don’t rely on this implicitly.  
- 在 JS 中，`Number(true) → 1`、`Number(false) → 0`；不要隐式依赖此行为。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture14.md) · [Next Lecture / 下一讲 →](./lecture16.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

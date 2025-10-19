[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 21: Control Structures II — Loops (`while`, `do…while`, `for`, `for…in`, `for…of`)  
# 第21讲：控制结构Ⅱ —— 循环（`while`、`do…while`、`for`、`for…in`、`for…of`）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Why Loops?](#why-loops)  
- 为什么需要循环？
- [`while`: Pre‑condition Loop](#while-precondition-loop)  
- `while`：前置条件循环
- [`do…while`: Post‑condition Loop](#dowhile-postcondition-loop)  
- `do…while`：后置条件循环（至少执行一次）
- [`for`: Count‑controlled Loop](#for-countcontrolled-loop)  
- `for`：计数控制循环
- [Iterating Arrays: `for` + index / `for…of`](#iterating-arrays-for--index--forof)  
- 遍历数组：`for` + 下标 / `for…of`
- [Iterating Objects: `for…in` over keys](#iterating-objects-forin-over-keys)  
- 遍历对象：`for…in` 遍历键名
- [Flowcharts & Loop Updates](#flowcharts--loop-updates)  
- 流程图与循环变量更新
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Why Loops?  
## 为什么需要循环？

- Repeating the **same statement** many times by **copy-paste** is **error‑prone** and **hard to maintain**.  
- 通过**复制粘贴**重复多次相同语句既**易错**又**难维护**。  

```js
// Example / 例子：若当前时间≥7点，提醒5次
if (hour >= 7) {
  console.log("起きてください！"); // Wake up!
  console.log("起きてください！");
  console.log("起きてください！");
  console.log("起きてください！");
  console.log("起きてください！");
}
```

- Use **loops** to repeat a block **as many times as needed** with a **single definition**.  
- 使用**循环**可以用**一次定义**完成**多次重复**的执行。  

---

## `while`: Pre‑condition Loop  
## `while`：前置条件循环

- Syntax: **test the condition first**; if `true`, run the **block**; **may run zero times**.  
- 语法：先**判断条件**，为 `true` 时执行**代码块**；**可能一次也不执行**。  

```js
let i = 0;
while (i < 5) {
  console.log("起きてください！");
  i = i + 1;   // or i += 1, i++
}
console.log("while 終了");
```

- Always ensure the **loop variable updates**, otherwise you get an **infinite loop**.  
- 请确保**循环变量被更新**，否则会发生**死循环**。  

---

## `do…while`: Post‑condition Loop  
## `do…while`：后置条件循环（至少执行一次）

- **Run the block first**, then **check the condition**; the body is executed **at least once**.  
- **先执行代码块**，再**检查条件**；循环体**至少执行一次**。  

```js
let i = 0;
do {
  console.log("一次必执行 / runs at least once");
  i++;
} while (i < 1);
```

---

## `for`: Count‑controlled Loop  
## `for`：计数控制循环

- Form: `for (init; condition; update) { body }` for **fixed or counted** repetitions.  
- 形式：`for (初始化; 条件; 每轮更新) { 循环体 }`，用于**固定或可计数**的重复执行。  

```js
for (let k = 0; k < 5; k++) {
  console.log(k);
}
```

- Execution order: **init → test → body → update → test → …** until the **test is false**.  
- 执行顺序：**初始化 → 判断 → 体 → 更新 → 判断 → …**，直到**条件为假**。  

---

## Iterating Arrays: `for` + index / `for…of`  
## 遍历数组：`for` + 下标 / `for…of`

- With **index**: increase from `0` to `array.length - 1` and access `arr[i]`.  
- 使用**下标**：`i` 从 `0` 增至 `array.length - 1`，通过 `arr[i]` 取值。  

```js
const lists = ["京都","東京","札幌","名古屋","大阪","福岡"];
for (let i = 0; i < lists.length; i++) {
  console.log(i, lists[i]);
}
```

- With **`for…of`**: iterate **values directly**, convenient but **no index** provided.  
- 使用 **`for…of`**：直接遍历**值**，简洁但**无下标**。  

```js
for (const p of lists) {
  console.log(p);
}
```

> Note: **`for…of`** was added in **ES2015**; very old browsers may not support it.  
> 说明：**`for…of`** 自 **ES2015** 引入；非常老的浏览器可能不支持。  

---

## Iterating Objects: `for…in` over keys  
## 遍历对象：`for…in` 遍历键名

- **`for…in`** enumerates an object’s **property names (keys)**; get values via **`obj[key]`**.  
- **`for…in`** 用于枚举对象的**属性名（键）**；通过 **`obj[key]`** 取值。  

```js
const obj = { id: "M23W9999", name: "Yamada", year: 2023 };
for (const key in obj) {
  console.log(key, obj[key]);
}
```

---

## Flowcharts & Loop Updates  
## 流程图与循环变量更新

- Loop logic can be expressed in a **flowchart**: **initialize → test → body → update**.  
- 循环逻辑可画成**流程图**：**初始化 → 判断 → 循环体 → 更新**。  

```
i = 0
        ┌───────────────┐
        │   i < 5 ?     │
        └──────┬────────┘
               │Yes
               v
       console.log(...)
           i = i + 1
               │
               └─────→ (back to test)
               No
               ↓
        console.log("終了")
```

- Remember to **update** the loop variable inside the body (e.g., `i++`).  
- 别忘了在循环体中**更新**循环变量（例如 `i++`）。  

---

## Practice Tasks  
## 练习任务

1) **Wake‑up messages**: Print “起きてください！” **5 times** using `while`, then rewrite with `for`.  
1) **起床提醒**：用 `while` 打印“起きてください！”**5 次**，再改写为 `for`。  
2) **Array iteration**: Given an array of cities, print **index + value** with indexed `for`, then print **values** with `for…of`.  
2) **数组遍历**：给定城市数组，先用下标 `for` 打印**序号+名称**，再用 `for…of` 打印**名称**。  
3) **Object enumeration**: Use `for…in` to print **all keys and values** of a student object.  
3) **对象枚举**：用 `for…in` 打印学生对象的**所有键与值**。  
4) **`do…while` demo**: Show that `do…while` runs the body **at least once** even if the condition is false initially.  
4) **`do…while` 示例**：验证即使初始条件为假，循环体也会**至少执行一次**。  

---

## Quick Checklist  
## 快速清单

- Pick the **right loop**: `while`/`do…while` for **condition‑driven** repetition; `for` for **counted** loops.  
- **按需选择**：条件驱动用 `while`/`do…while`；**计数**循环用 `for`。  
- For arrays, use **indexed `for`** when you need the **index**; use **`for…of`** to loop **values** concisely.  
- 对数组，需**下标**时用 **下标 `for`**；只需**值**时用 **`for…of`**。  
- For objects, **`for…in`** gets **keys**, then read **values** via `obj[key]`.  
- 对对象，用 **`for…in`** 遍历**键**，用 `obj[key]` 取**值**。  
- **Always update** loop counters to avoid **infinite loops**.  
- **务必更新**循环计数器，避免**死循环**。  

---

## Notes
## 注释

<details><summary>Unowned/inherited keys in `for…in` / `for…in` 与继承属性</summary>

- In modern JS, `for…in` can enumerate **inherited enumerable** keys; for **own keys only**, prefer `Object.keys(obj)`.  
- 现代 JS 中，`for…in` 可能枚举**继承的可枚举键**；若只要**自有键**，可用 `Object.keys(obj)`。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture20.md) · [Next Lecture / 下一讲 →](./lecture22.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

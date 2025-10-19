[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 22: Function Definitions & Event Listeners (addEventListener)  
# 第22讲：函数的多种定义方式与事件监听（addEventListener）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Function Definitions Overview](#function-definitions-overview)  
- 函数定义方式总览
- [Function Declaration](#function-declaration)  
- 函数声明式
- [Function Expression (Anonymous)](#function-expression-anonymous)  
- 函数表达式（无名函数）
- [Arrow Functions](#arrow-functions)  
- 箭头函数（Arrow）
- [What Is an Event & Event Handler](#what-is-an-event--event-handler)  
- 什么是事件与事件处理器
- [Two Ways to Attach Handlers](#two-ways-to-attach-handlers)  
- 指定事件处理器的两种方式
- [Example: Convert `onclick` Attribute → `addEventListener`](#example-convert-onclick-attribute--addeventlistener)  
- 示例：从 `onclick` 属性改为 `addEventListener`
- [Practice 1: Slider Value on Button Click](#practice-1-slider-value-on-button-click)  
- 练习1：点击按钮读取滑块数值
- [Practice 2: Non-Click Events (`input`/`change` on `<input type="range">`)](#practice-2-non-click-events-inputchange-on-input-typerange)  
- 练习2：非点击事件（`<input type="range">` 的 `input`/`change`）
- [Task 09 Exercises (Circle Perimeter/Area, Radius Input)](#task-09-exercises-circle-perimeterarea-radius-input)  
- 第09回练习（圆的周长/面积，半径输入）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Function Definitions Overview  
## 函数定义方式总览

- In JavaScript, you can define functions via **declaration**, **function expression (anonymous)**, and **arrow function**.  
- 在 JavaScript 中，可通过**声明式**、**函数表达式（无名）**与**箭头函数**三种主要方式定义函数。  

---

## Function Declaration  
## 函数声明式

```js
function greet(name) {
  // statements...
  return "Hello, " + name;
}

// call
greet("KCGI");
```
- Use the `function` keyword with a **name** and **parameters**; you can call it by its name.  
- 使用 `function` 关键字、**函数名**与**参数**；通过函数名即可调用。  
- Typically placed at **top-level**; **hoisted** by the engine.  
- 通常置于**顶层**；引擎会对其进行**提升（hoist）**。  

---

## Function Expression (Anonymous)  
## 函数表达式（无名函数）

```js
const area = function (r) {
  return Math.PI * r * r;
}; // ← semicolon is required
// call
area(10);
```
- Define an **unnamed function** and **assign** it to a variable/constant.  
- 定义**没有名字**的函数并**赋值**给变量/常量。  
- Since it’s an **assignment**, the statement ends with a **semicolon**.  
- 因为是**赋值语句**，所以行末需加**分号**。  

---

## Arrow Functions  
## 箭头函数（Arrow）

```js
const circumference = (r) => {
  return 2 * Math.PI * r;
};
// concise body when single expression
// 当函数体只有一个表达式时可省略 return 与花括号
const circumference2 = (r) => 2 * Math.PI * r;
```
- Remove the `function` keyword and put **`=>`** between **parameter list** and **body**.  
- 去掉 `function` 关键字，在**参数列表**与**函数体**之间写 **`=>`**。  
- Still an **assignment**, so **semicolon** is required at the end.  
- 仍然是**赋值语句**，行末需要**分号**。  

---

## What Is an Event & Event Handler  
## 什么是事件与事件处理器

- An **event** is an **interaction or occurrence** on the page (clicks, key presses, slider moves, menu changes, etc.).  
- **事件**指网页中的**交互或发生的动作**（点击、键盘输入、滑块移动、菜单变更等）。  
- A function that runs **in response to an event** is an **event handler**.  
- **事件发生时被调用**的函数称为**事件处理器（handler）**。  

---

## Two Ways to Attach Handlers  
## 指定事件处理器的两种方式

**Way 1 — HTML attribute**  
**方式一——HTML 属性**

```html
<button onclick="getText()">输入值を表示</button>
```
- Quick but **mixes HTML & JS**; used in earlier lectures.  
- 快速但会**混杂 HTML 与 JS**；前几讲曾使用。  

**Way 2 — `addEventListener` (recommended)**  
**方式二——`addEventListener`（推荐）**

```html
<button id="btn1">输入值を表示</button>
<script>
  const btn = document.querySelector("#btn1");
  // (a) named function / 具名函数
  btn.addEventListener("click", getText);
  function getText(){ /* ... */ }

  // (b) anonymous or arrow / 无名或箭头
  btn.addEventListener("click", function(){ /* ... */ });
  btn.addEventListener("click", () => { /* ... */ });
</script>
```
- **Separates** HTML & JS, easier to **maintain**; pass the **function reference** (not `getText()` with parentheses).  
- **分离**结构与脚本、更易**维护**；传入**函数引用**（而不是带括号的 `getText()`）。  

---

## Example: Convert `onclick` Attribute → `addEventListener`  
## 示例：从 `onclick` 属性改为 `addEventListener`

```html
<!-- Before / 改造前 -->
<button onclick="getText()">输入値を表示</button>
<script>
  function getText(){ /* ... */ }
</script>

<!-- After / 改造后 -->
<button id="btn1">输入値を表示</button>
<script>
  const el = document.querySelector("#btn1");
  el.addEventListener("click", getText);
  function getText(){ /* ... */ }
</script>
```

---

## Practice 1: Slider Value on Button Click  
## 练习1：点击按钮读取滑块数值

```html
<input id="slider" type="range" min="0" max="100">
<span id="out">-</span>
<button id="btn">显示</button>

<script>
  const btn = document.querySelector("#btn");
  btn.addEventListener("click", () => {
    const v = document.querySelector("#slider").value; // string
    document.querySelector("#out").textContent = v;
  });
</script>
```
- Use **`addEventListener` + arrow function**; read **`.value`** and write to **`textContent`**.  
- 使用 **`addEventListener` + 箭头函数**；读取 **`.value`** 并写入 **`textContent`**。  

---

## Practice 2: Non-Click Events (`input`/`change` on `<input type="range">`)  
## 练习2：非点击事件（`<input type="range">` 的 `input`/`change`）

```html
<input id="slider2" type="range" min="0" max="100">
<span id="out2">-</span>

<script>
  const s = document.querySelector("#slider2");
  // fires for every thumb move / 拖动过程持续触发
  s.addEventListener("input",  () => { out2.textContent = s.value; });
  // fires when value is committed / 变更确定后触发
  s.addEventListener("change", () => { console.log("changed"); });
</script>
```
- **`input`**: fires **as the user drags**; **`change`**: when **commit** happens.  
- **`input`**：**拖动过程中**持续触发；**`change`**：**变更被确认**时触发。  

---

## Task 09 Exercises (Circle Perimeter/Area, Radius Input)  
## 第09回练习（圆的周长/面积，半径输入）

**Exercise 9‑1 — Buttons + Function Expressions**  
**练习 9‑1 —— 用按钮与函数表达式**

- Input **radius** (`type="text"`) and show **circumference**/**area** on button clicks.  
- 输入**半径**（`type="text"`），点击按钮分别显示**圆周**与**面积**。  
- Use **`addEventListener` + function expressions (anonymous)**; **`Math.PI`** for π.  
- 使用 **`addEventListener` + 无名函数**；π 使用 **`Math.PI`**。  

```html
<input id="r1" type="text" placeholder="半径">
<button id="btnC">円周計算</button>
<button id="btnA">面積計算</button>
<p id="ans1"></p>
<script>
  const r1 = document.querySelector("#r1");
  const out = document.querySelector("#ans1");
  document.querySelector("#btnC").addEventListener("click", function(){
    const r = Number(r1.value);
    out.textContent = "円周: " + (2 * Math.PI * r);
  });
  document.querySelector("#btnA").addEventListener("click", function(){
    const r = Number(r1.value);
    out.textContent = "面積: " + (Math.PI * r * r);
  });
</script>
```

**Exercise 9‑2 — `input` Listener + Arrow Functions**  
**练习 9‑2 —— `input` 监听 + 箭头函数**

- Radius input **`type="number"`**, no buttons; update **circumference/area** on **`input`**.  
- 半径输入用 **`type="number"`**，不使用按钮；在 **`input`** 事件中更新**圆周/面积**。  

```html
<input id="r2" type="number" min="0">
<p id="ans2"></p>
<script>
  const r2 = document.querySelector("#r2");
  const a2 = document.querySelector("#ans2");
  const show = () => {
    const r = Number(r2.value || 0);
    a2.innerHTML = `円周: ${2*Math.PI*r}<br>面積: ${Math.PI*r*r}`;
  };
  r2.addEventListener("input", show);
</script>
```

**Exercise 9‑3 — Slider (`type="range"`)**  
**练习 9‑3 —— 滑块（`type="range"`）**

- Change the radius input to **`type="range"`** with **`min="0"`** and **`max="10000"`**; update on **`input`**.  
- 将半径输入改为 **`type="range"`**，**`min="0"`**、**`max="10000"`**；在 **`input`** 时更新结果。  

```html
<input id="r3" type="range" min="0" max="10000" step="1">
<p id="ans3"></p>
<script>
  const r3 = document.querySelector("#r3");
  const a3 = document.querySelector("#ans3");
  r3.addEventListener("input", () => {
    const r = Number(r3.value);
    a3.textContent = `半径=${r} → 円周=${2*Math.PI*r} 面積=${Math.PI*r*r}`;
  });
</script>
```


---

## Quick Checklist  
## 快速清单

- Choose **function declaration / expression / arrow** appropriately.  
- 按需选择**函数声明/表达式/箭头函数**。  
- Prefer **`addEventListener`** to keep HTML/JS **separated**; pass a **function reference**.  
- 优先使用 **`addEventListener`** 以保持 HTML/JS **分离**；传入**函数引用**。  
- For sliders, use **`input`** for live updates; **`change`** for committed updates.  
- 对滑块：**`input`** 用于实时更新；**`change`** 用于确认后的更新。  
- Convert **`prompt/alert`** workflows to **DOM I/O** (`.value` + `textContent/innerHTML`).  
- 将 **`prompt/alert`** 工作流改为 **DOM 入出力**（`.value` + `textContent/innerHTML`）。  

---

## Notes 
## 注释

<details><summary>Why “pass the function name” to `addEventListener`? / 为什么给 `addEventListener` 传“函数名”</summary>

- `addEventListener("click", getText)` stores a **reference** to be called **later** on click, while `getText()` would **call it immediately**.  
- `addEventListener("click", getText)` 传入的是**引用**，将在点击时**再调用**；而 `getText()` 会**立刻执行**。  
</details>

---

[← Previous Lecture / 上一讲](./lecture21.md) · [Next Lecture / 下一讲 →](./lecture23.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

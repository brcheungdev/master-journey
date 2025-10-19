[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 18: DOM Input/Output — `querySelector`, `value`, `textContent`, `innerHTML`, and `style`  
# 第18讲：DOM 页面输入输出 —— `querySelector`、`value`、`textContent`、`innerHTML` 与 `style`

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [DOM & Tree Structure](#dom--tree-structure)  
- DOM 与树形结构
- [Get DOM Objects: `document.querySelector` (CSS Selectors)](#get-dom-objects-documentqueryselector-css-selectors)  
- 获取 DOM 对象：`document.querySelector`（CSS 选择器）
- [Read Input Values: `<input type="text">` / `<input type="range">`](#read-input-values-input-typetext--input-typerange)  
- 读取输入值：`<input type="text">` / `<input type="range">`
- [Practice 1: Get Text Value and `alert`](#practice-1-get-text-value-and-alert)  
- 练习1：获取文本框并 `alert`
- [Practice 2: Get Range Value and `alert` (min/max)](#practice-2-get-range-value-and-alert-minmax)  
- 练习2：获取滑块值并 `alert`（最小/最大）
- [Output to Page: `textContent` vs `innerHTML` (`document.write` discouraged)](#output-to-page-textcontent-vs-innerhtml-documentwrite-discouraged)  
- 输出到页面：`textContent` vs `innerHTML`（不推荐 `document.write`）
- [Overwrite/Append Examples (`innerHTML +=`)](#overwriteappend-examples-innerhtml-)  
- 覆盖/追加示例（`innerHTML +=`）
- [Change Element Text from JS](#change-element-text-from-js)  
- 用 JS 实时改变元素文本
- [Change Styles via `element.style` (camelCase props)](#change-styles-via-elementstyle-camelcase-props)  
- 通过 `element.style` 修改样式（小驼峰属性名）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes (Optional)](#notes-optional)  
- 注释（可选）

---

## DOM & Tree Structure  
## DOM 与树形结构

- In browsers, each HTML tag on the page is represented as a **DOM (Document Object Model) object**.  
- 浏览器中，页面上的每个 HTML 标签都会被表示为一个 **DOM（文档对象模型）对象**。  
- The whole document forms a **tree** (rooted at **`<body>`**) of DOM objects.  
- 整个文档形成以 **`<body>`** 为根的 **DOM 对象树**。  

```
<body>
  <ol type="a">
    <li>京都</li>
    <li>東京</li>
    <li>札幌</li>
  </ol>
</body>

DOM tree / DOM 树
body
└─ ol (type="a")
   ├─ li "京都"
   ├─ li "東京"
   └─ li "札幌"
```

---

## Get DOM Objects: `document.querySelector` (CSS Selectors)  
## 获取 DOM 对象：`document.querySelector`（CSS 选择器）

- To **read/update** a tag, first **get its DOM object**.  
- 要**读取/更新**标签，首先需要**获取其 DOM 对象**。  
- Use **`document.querySelector("selector")`** to get the **first match** for a **CSS selector**.  
- 使用 **`document.querySelector("选择器")`**，按 **CSS 选择器**规则获取**第一个**匹配的元素。  
- Selector examples: **element** (`h1`, `a`, `ul`), **class** (`.container1`), **id** (`#div1`, must be **unique**).  
- 选择器示例：**元素**（`h1`、`a`、`ul`）、**类**（`.container1`）、**id**（`#div1`，必须**唯一**）。  

```js
const el1 = document.querySelector("ul");     // element / 元素选择器
const el2 = document.querySelector(".box");   // class / 类选择器
const el3 = document.querySelector("#input1");// id / id 选择器
```

---

## Read Input Values: `<input type="text">` / `<input type="range">`  
## 读取输入值：`<input type="text">` / `<input type="range">`

- **`<input type="text">`**: single-line **string** input.  
- **`<input type="text">`**：**单行字符串**输入。  
- **`<input type="range">`**: **numeric slider**; set range by **`min`/`max`**.  
- **`<input type="range">`**：**数值滑块**；用 **`min`/`max`** 指定范围。  
- To get the current value: **(1)** `querySelector` the element → **(2)** read its **`.value`**.  
- 获取当前值的步骤：**（1）** 用 `querySelector` 定位元素 → **（2）** 读取其 **`.value`**。  
- **Note**: `value` is a **string** (convert to number if needed).  
- **注意**：`value` 是**字符串**（需要数值时请自行转换）。  

```html
<input type="text" id="text1">
<input type="range" id="slider1" min="0" max="100">

<script>
  const t = document.querySelector("#text1");
  const s = document.querySelector("#slider1");
  const vText = t.value;           // string / 字符串
  const vNum  = Number(s.value);   // number / 转为数值
</script>
```

---

## Practice 1: Get Text Value and `alert`  
## 练习1：获取文本框并 `alert`

- Add an **`<input id="input01" type="text">`** and a **button** calling **`showValues()`** on **`onclick`**.  
- 添加 **`<input id="input01" type="text">`** 与一个 **button**，点击 **`onclick`** 调用 **`showValues()`**。  

```html
<input id="input01" type="text">
<button onclick="showValues()">押してね</button>

<script>
  function showValues() {
    const el = document.querySelector("#input01"); // (3)
    const v  = el.value;                            // (4)
    window.alert(v);
  }
</script>
```

---

## Practice 2: Get Range Value and `alert` (min/max)  
## 练习2：获取滑块值并 `alert`（最小/最大）

- Add an **`<input type="range" id="slider01" min="0" max="100">`** and show its **value**.  
- 添加 **`<input type="range" id="slider01" min="0" max="100">`** 并显示其 **value**。  

```html
<h3>Volume</h3>
<input type="range" id="slider01" min="0" max="100">
<button onclick="alert(document.querySelector('#slider01').value)">show</button>
```

---

## Output to Page: `textContent` vs `innerHTML` (`document.write` discouraged)  
## 输出到页面：`textContent` vs `innerHTML`（不推荐 `document.write`）

- **`textContent`** reads the **rendered text** inside an element.  
- **`textContent`** 用于读取元素内部的**纯文本**。  
- **`innerHTML`** reads the **HTML string** of the element’s **children**.  
- **`innerHTML`** 用于读取元素**子内容**的 **HTML 字符串**。  
- **Do not** use **`document.write()`** for normal dynamic updates.  
- 动态更新时**不要**使用 **`document.write()`**。  

```html
<ul id="list">
  <li>京都</li>
  <li>東京</li>
  <li>札幌</li>
</ul>

<script>
  const list = document.querySelector("#list");
  console.log(list.textContent); // "京都東京札幌"
  console.log(list.innerHTML);   // "<li>京都</li><li>東京</li><li>札幌</li>"
</script>
```

---

## Overwrite/Append Examples (`innerHTML +=`)  
## 覆盖/追加示例（`innerHTML +=`）

- You can **append** HTML snippets by `element.innerHTML += "...";`.  
- 通过 `element.innerHTML += "..."` 可以**追加**一段 HTML 片段。  

```js
const list = document.querySelector("#list");
list.innerHTML += "<li>ニューヨーク</li>"; // append one more item / 追加一项
```

---

## Change Element Text from JS  
## 用 JS 实时改变元素文本

- Modify the **display text** of a **button** by **assigning** to its **`textContent`**.  
- 通过给 **`textContent`** **赋值**可以修改**按钮**的**显示文本**。  

```html
<button id="btn">押してね</button>

<script>
  function show(message) {
    const btn = document.querySelector("#btn");
    btn.textContent = message; // overwrite text / 覆盖显示文字
  }
</script>

<button onclick="show('どかーん')">Change text</button>
```

---

## Change Styles via `element.style` (camelCase props)  
## 通过 `element.style` 修改样式（小驼峰属性名）

- The **`style`** property is an object containing **CSS properties**; **assign** to change the element’s **appearance**.  
- **`style`** 属性是一个包含**CSS 属性**的对象；对其**赋值**即可改变元素**外观**。  
- In JS, property names **cannot contain `-`**, so use **camelCase** (e.g., `backgroundColor`, not `background-color`).  
- 在 JS 中属性名**不能包含 `-`**，因此需使用 **小驼峰**（如 `backgroundColor`，而不是 `background-color`）。  

```js
const item = document.querySelector("#item");
item.style.backgroundColor = "pink";
item.style.fontSize = "20px";
```

---

## Quick Checklist  
## 快速清单

- Get elements with **`document.querySelector`** (element/class/**unique id**).  
- 使用 **`document.querySelector`** 获取元素（元素/类/**唯一 id**）。  
- For inputs, read **`.value`** (string); **convert** if numeric needed.  
- 表单输入取 **`.value`**（字符串）；需要数值请**转换**。  
- Use **`textContent`** for text; **`innerHTML`** for HTML fragments; **avoid** `document.write`.  
- 文本用 **`textContent`**；HTML 片段用 **`innerHTML`**；**避免** `document.write`。  
- To append, `innerHTML += "..."`; to overwrite, assign **`textContent`**/**`innerHTML`**.  
- 追加可用 `innerHTML += "..."`；覆盖则赋值 **`textContent`**/**`innerHTML`**。  
- Modify styles via **`element.style`** with **camelCase** property names.  
- 通过 **`element.style`** 修改样式，属性名使用 **小驼峰**。  

---

## Notes
## 注释

<details><summary>Value conversions / 值的转换</summary>

- `Number("42") → 42`, `parseInt("42px", 10) → 42`, `parseFloat("3.14") → 3.14`.  
- `Number("42") → 42`、`parseInt("42px", 10) → 42`、`parseFloat("3.14") → 3.14`。  
- For sliders (`type="range"`), **`value`** is still a **string**; convert before math.  
- 对滑块（`type="range"`），**`value`** 仍是**字符串**；在参与运算前请转换。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture17.md) · [Next Lecture / 下一讲 →](./lecture19.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 14: Orientation + JavaScript Basics   
# 第14讲：导学 + JavaScript 基础

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Course Orientation (WP2)](#course-orientation-wp2)  
- 课程导学（WP2）
- [What Is JavaScript? Role in the Web Stack](#what-is-javascript-role-in-the-web-stack)  
- 什么是 JavaScript？在 Web 技术栈中的角色
- [Two Ways to Include JavaScript](#two-ways-to-include-javascript)  
- 在页面中编写/引入 JavaScript 的两种方式
- [Run & Test in the Browser](#run--test-in-the-browser)  
- 在浏览器中运行与测试
- [Output APIs: `alert` and `console.log`](#output-apis-alert-and-consolelog)  
- 输出接口：`alert` 与 `console.log`
- [Comments: Single-line & Multi-line](#comments-single-line--multi-line)  
- 注释：单行与多行
- [Values & Variables: `let` and Types](#values--variables-let-and-types)  
- 值与变量：`let` 与常见类型
- [Naming Rules & Styles](#naming-rules--styles)  
- 命名规则与风格
- [Expressions & Assignment](#expressions--assignment)  
- 表达式与赋值
- [Basic Arithmetic & Operators](#basic-arithmetic--operators)  
- 基本算术与运算符
- [Input via `window.prompt`](#input-via-windowprompt)  
- 通过 `window.prompt` 获取输入
- [Using DevTools Console & Reading Errors](#using-devtools-console--reading-errors)  
- 使用开发者工具控制台与阅读错误
- [Constants with `const` (Tax Example)](#constants-with-const-tax-example)  
- 常量 `const`（消费税示例）
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [References](#references)  
- 参考资料
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## Course Orientation  
## 课程导学

- **Goal**: Design and implement **interactive web applications** that update page design/content **in the browser** based on user actions (using **JavaScript**).  
- **目标**：能使用 **JavaScript** 设计并实现**交互式 Web 应用**，根据用户操作在**浏览器端**更新页面设计与内容。  
- **Audience**: Students **without prior JavaScript** knowledge; prerequisites are **Web Programming I (HTML5+CSS3)** or equivalent.  
- **适用对象**：**没有 JavaScript 背景**的同学；先修为 **Web Programming I（HTML5+CSS3）**或同等水平。  
- **Evaluation**: **13 weekly exercises** (each due **the day before the next lecture, 23:59**) + **final project** in weeks **14–15**; **exercises 50% + final 50%**; **plagiarism penalized/failed**.  
- **考核方式**：前 **13 次**课每次布置**编程练习**（**下次课前一日 23:59** 截止）；第 **14–15** 次为**期末大作业**；**平时 50% + 期末 50%**；**抄袭严惩/判零**。  
- **Instructor**: **H. An**; profile and contacts provided.  
- **任课教师**：**安 平勲**；提供个人简介与联系方式。  

---

## What Is JavaScript? Role in the Web Stack  
## 什么是 JavaScript？在 Web 技术栈中的角色

- **JavaScript** is a **programming language** that runs **in the browser** (also runs in other environments).  
- **JavaScript** 是在**浏览器中运行**的**编程语言**（也可运行于其他环境）。  
- Web page composition: **HTML = structure**, **CSS = presentation**, **JavaScript = interaction/behavior** (manipulates HTML & CSS).  
- 网页由 **HTML（结构）**、**CSS（表现）**与 **JavaScript（交互/行为）**构成（JS 用于操作 HTML 与 CSS）。  
- Use JS to make pages **interactive/dynamic**: menus on click, calculations, **asynchronous** communication, etc.  
- 使用 JS 令页面**交互/动态**：点击展开菜单、计算输入、**异步**通信等。  
- Note: **Java** and **JavaScript** are **completely different** languages.  
- 注意：**Java** 与 **JavaScript** 是**完全不同**的语言。  

---

## Two Ways to Include JavaScript  
## 在页面中编写/引入 JavaScript 的两种方式

1) **Inline** inside HTML using **`<script>…</script>`** (no HTML tags allowed inside).  
1) 在 HTML 内直接使用 **`<script>…</script>`**（内部**不能**写 HTML 标签）。  
2) **External** file **`*.js`** referenced with **`<script src="file.js"></script>`**; JS loads and runs when the page loads.  
2) 以 **外部文件 `*.js`** 形式通过 **`<script src="file.js"></script>`** 引入；页面加载时同时加载并执行 JS。  

```html
<!-- Inline / 内联 -->
<script>
// JS code here / 此处编写 JavaScript
</script>

<!-- External / 外部文件 -->
<script src="first.js"></script>
```

---

## Run & Test in the Browser  
## 在浏览器中运行与测试

- Use **VS Code**; if installed, the **Open in Browser** extension lets you open the current HTML via **Shift+Alt+B** or context menu.  
- 使用 **VS Code**；若安装 **Open in Browser** 扩展，可通过 **Shift+Alt+B** 或右键菜单在浏览器打开当前 HTML。  
- Save **`wp01-1.html`**, then open in **Chrome** to run your JS.  
- 保存 **`wp01-1.html`**，在 **Chrome** 中打开即可运行 JS。  

---

## Output APIs: `alert` and `console.log`  
## 输出接口：`alert` 与 `console.log`

- Show a **modal dialog** with **`window.alert(value)`**.  
- 通过 **`window.alert(value)`** 显示**模式对话框**。  
- Log to the **DevTools Console** with **`console.log(value)`**.  
- 使用 **`console.log(value)`** 将信息输出到**开发者工具控制台**。  

```html
<script>
  // Outputs / 输出
  window.alert("Hello, KCGI!"); // dialog / 对话框
  console.log("Logged to console"); // DevTools console / 控制台
</script>
```

---

## Comments: Single-line & Multi-line  
## 注释：单行与多行

- **Single-line**: `// comment`.  
- **单行**：`// 注释`。  
- **Multi-line**: `/* comment … */`.  
- **多行**：`/* 注释 … */`。  
- Comments are **ignored** by the engine; use to explain logic or **comment‑out** code.  
- 注释在执行时会被**忽略**；用于解释逻辑或**临时屏蔽**代码。  

```js
// single-line / 单行
/*
 multi-line / 多行
*/
```

---

## Values & Variables: `let` and Types  
## 值与变量：`let` 与常见类型

- **Variables** are **containers** for values; declare with **`let`** (ES2015+).  
- **变量**是值的**容器**；使用 **`let`**（ES2015+）声明。  
- Common **types**: **Number** (`123`, `-3`, `3.14`), **String** (`"京都"`, `"123"`), **Boolean** (`true/false`), plus **`null`** and **`undefined`**.  
- 常见**类型**：**数字**（`123`、`-3`、`3.14`）、**字符串**（`"京都"`、`"123"`）、**布尔**（`true/false`），以及 **`null`** 与 **`undefined`**。  
- Declare and assign; variables can be **reassigned**.  
- 声明与赋值；变量可**反复赋值**。  

```js
let x;          // declare / 声明
x = 2;          // assign / 赋值
x = 100;        // reassign / 再赋值
let y = 90;     // declare + assign / 声明并赋值
let msg = "おはよう"; // string / 字符串
```

---

## Naming Rules & Styles  
## 命名规则与风格

- Use **letters/digits/`_`/`$`**; **first character cannot be a digit**; avoid **reserved words**; **case‑sensitive**.  
- 变量名由**字母/数字/`_`/`$`**组成；**首字符不能是数字**；避免**保留字**；**大小写敏感**。  
- Prefer **lower camelCase** in JavaScript (e.g., `firstName`), not `first_name`.  
- JavaScript 中推荐使用 **小驼峰**（如 `firstName`），不使用 `first_name`。  
- Avoid **full‑width** characters in identifiers.  
- **标识符**中避免使用**全角字符**。  

---

## Expressions & Assignment  
## 表达式与赋值

- Compute on the **right-hand side** and assign to the **left-hand side** variable.  
- 先在**右侧**计算，再将结果赋给**左侧**变量。  
- `+` adds numbers; for strings, `+` **concatenates**.  
- `+` 对数字表示**加法**；对字符串表示**拼接**。  

```js
let z = 90;         // 90
let u = "今日は";    // "今日は"
z = z + 200;        // 290
u = u + "晴です";   // "今日は晴です"
```

---

## Basic Arithmetic & Operators  
## 基本算术与运算符

- Examples: `x + 3`, `1 - y`, `p * q`, `p / q`, remainder **`%`**.  
- 示例：`x + 3`、`1 - y`、`p * q`、`p / q`、取余 **`%`**。  
- Execution is **top→bottom**; store results in variables for later use.  
- 计算按**自上而下**顺序执行；结果保存在变量中以便后续使用。  

```js
let x = 15;
let y = x % 2; // remainder / 余数
y = y + 1;     // y becomes ? / 结果是多少？
```

---

## Input via `window.prompt`  
## 通过 `window.prompt` 获取输入

- Use **`window.prompt("message")`** to get a **string** from the user.  
- 通过 **`window.prompt("提示语")`** 获取用户输入（**字符串**）。  
- Combine with `console.log` to **echo** the value.  
- 可与 `console.log` 结合**回显**该值。  

```html
<script>
  let value = window.prompt("入力してください。"); // get input / 获取输入
  console.log(value); // show in DevTools / 显示在控制台
</script>
```

---

## Using DevTools Console & Reading Errors  
## 使用开发者工具控制台与阅读错误

- Open **Chrome DevTools**: **Ctrl+Shift+I** (Windows) / **Option+Command+I** (macOS), then click the **Console** tab.  
- 打开 **Chrome 开发者工具**：**Ctrl+Shift+I**（Windows）/ **Option+Command+I**（macOS），然后切换到 **Console** 选项卡。  
- **Error messages** show **file/line** details; read them to fix typos like using **`val`** instead of **`value`**.  
- **错误信息**会给出**文件/行号**；阅读提示即可修复如将 **`value`** 误写为 **`val`** 等问题。  

---

## Constants with `const` (Tax Example)  
## 常量 `const`（消费税示例）

- Use **`const`** for **named constants** (cannot be reassigned); use **UPPER_CASE** by convention to distinguish from variables.  
- 使用 **`const`** 声明**命名常量**（不可再赋值）；通常用 **全大写** 与变量区分。  
- Constants make code **readable** and **reduce typos** when the **same value** is used in many places.  
- 当同一数值在多处使用时，常量让代码更**易读**且**降低误输**。  

```js
const TAX = 1.1;        // 10% tax / 10% 税
let price = 130;
let withTax = price * TAX; // 143
// TAX = 1.08; // ✗ Error: cannot reassign / 不能重新赋值
```

---

## Practice Tasks  
## 练习任务

1) **External script**: Duplicate `wp01-1.html` → `wp01-1a.html`; create **`first.js`**; move the inline JS into it and reference with `<script src="first.js"></script>`.  
1) **外部脚本**：复制 `wp01-1.html` → `wp01-1a.html`；创建 **`first.js`**；将内联 JS 移入该文件并用 `<script src="first.js"></script>` 引用。  
2) **Expression practice**: Duplicate to `wp01-1b.html`; add examples of **addition/concatenation** and **`%` remainder**; log results.  
2) **表达式练习**：复制得到 `wp01-1b.html`；添加**加法/拼接**与 **`%` 取余**示例，并输出结果。  
3) **I/O practice**: Create `wp01-2.html`; prompt for input with **`window.prompt`**, then **`console.log`** it.  
3) **输入/输出练习**：创建 `wp01-2.html`；使用 **`window.prompt`** 获取输入，并用 **`console.log`** 输出。  
4) **Tax practice**: Refactor repeated numeric literals into a **`const TAX`** and compute **tax‑inclusive price**.  
4) **税率练习**：将重复的数值提取为 **`const TAX`**，计算**含税价格**。  

---

## References  
## 参考资料

- **Beginner book**: *いちばんやさしいJavaScriptの教本 第2版* (Impress, 2019).  
- **入门书籍**：*いちばんやさしいJavaScriptの教本 第2版*（インプレス，2019）。  
- **Deeper reference**: *改訂新版 JavaScript本格入門* (技術評論社, 2016).  
- **进阶参考**：*改訂新版 JavaScript本格入門*（技術評論社，2016）。  
- **Free guide**: **MDN Web Docs – JavaScript Guide** (Japanese/Chinese editions available).  
- **免费指南**：**MDN Web Docs – JavaScript Guide**（提供日/中文版本）。  

---

## Quick Checklist  
## 快速清单

- Choose **inline vs external** scripts appropriately; remember that **HTML tags are invalid inside `<script>`**.  
- 合理选择**内联或外链**脚本；牢记 **`<script>` 内不能写 HTML 标签**。  
- Use **`alert`** and **`console.log`** to verify outputs; keep **DevTools Console** open.  
- 用 **`alert`** 与 **`console.log`** 验证输出；保持**控制台**打开。  
- Prefer **lower camelCase** names; avoid reserved words and full‑width characters.  
- 使用**小驼峰**命名；避免保留字与全角字符。  
- Understand **numbers vs strings** and the dual role of **`+`**.  
- 理解**数字与字符串**的差异及 **`+`** 的双重含义。  
- Extract magic numbers into **`const`**; constants **cannot** be reassigned.  
- 将“魔法数字”提取为 **`const`**；常量**不可**再赋值。  

---

[← Previous Lecture / 上一讲](./lecture13.md) · [Next Lecture / 下一讲 →](./lecture15.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

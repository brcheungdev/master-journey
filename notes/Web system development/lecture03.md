[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 03: CSS Basics and Styling Methods  
# 第03讲：CSS 基础与样式指定方法

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What is CSS (Cascading Style Sheets)](#what-is-css-cascading-style-sheets)  
- 什么是 CSS（层叠样式表）
- [Why use CSS (Benefits)](#why-use-css-benefits)  
- 为什么使用 CSS（优势）
- [CSS Syntax: Selector, Property, Value](#css-syntax-selector-property-value)  
- CSS 基本语法：选择器、属性、值
- [Selectors by Example](#selectors-by-example)  
- 通过示例理解选择器
- [Classes and IDs: Definition and Use](#classes-and-ids-definition-and-use)  
- class 与 id：定义与用法
- [Class vs ID: When to Use Which](#class-vs-id-when-to-use-which)  
- 何时使用 class、何时使用 id
- [Specificity & Source Order](#specificity--source-order)  
- 优先级与后定义覆盖
- [Link Pseudo‑classes and Order (LVHA)](#link-pseudo-classes-and-order-lvha)  
- 链接伪类与推荐顺序（LVHA）
- [Three Ways to Add CSS in HTML](#three-ways-to-add-css-in-html)  
- 在 HTML 中引入 CSS 的三种方式
- [Color Specifications](#color-specifications)  
- 颜色指定方法
- [Comments in HTML and CSS](#comments-in-html-and-css)  
- HTML 与 CSS 中的注释
- [Practice: Internal → External CSS Refactor](#practice-internal--external-css-refactor)  
- 实操练习：内联样式到外部样式重构
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## What is CSS (Cascading Style Sheets)  
## 什么是 CSS（层叠样式表）

- **CSS** is the language for describing **presentation (design/appearance)** of web pages (e.g., text size, color, background, layout).  
- **CSS** 是用于指定网页**表现（设计/外观）**的语言（如文字大小、颜色、背景与布局）。  
- Recommended practice: **HTML defines document structure**, while **CSS defines design**.  
- 推荐实践：**HTML 负责文档结构**，**CSS 负责设计与外观**。  

---

## Why use CSS (Benefits)  
## 为什么使用 CSS（优势）

- **Clearer HTML structure**; content and presentation are **separated**.  
- **HTML 结构更清晰**；实现**内容与表现分离**。  
- **Avoid repeating design data** in every page.  
- **避免**在每个页面重复书写大量样式数据。  
- **Consistent design** across pages with **one shared stylesheet**.  
- 通过**共享样式表**实现**全站设计统一**。  
- **Easy global changes**: edit the stylesheet to update **multiple pages at once**.  
- **全局修改更容易**：仅修改样式表即可**批量生效**。  

---

## CSS Syntax: Selector, Property, Value  
## CSS 基本语法：选择器、属性、值

```
selector { property: value; }
选择器    { 属性:     值;   }
```

- **Selector**: the target(s) to style (e.g., `body`, `h1`, `p`, **classes**, **IDs**, combinations).  
- **选择器**：指定要应用样式的目标（如 `body`、`h1`、`p`，以及**类**、**ID**与其组合）。  
- **Property**: which aspect to style (e.g., `color`, `font-size`).  
- **属性**：表示要设置的样式维度（如 `color`、`font-size`）。  
- **Value**: the concrete value (e.g., `blue`, `12pt`).  
- **值**：具体取值（如 `blue`、`12pt`）。  

**Examples / 示例**  
**Example 1** / **示例1**  
```css
body { color: blue; }
```
- Set **text color** of `body` to **blue**.  
- 将 `body` 的**文字颜色**设为 **blue**。  

**Example 2** / **示例2**  
```css
body { color: blue; font-size: 12pt; }
```
- Set **color** and **font size** together.  
- 同时设置**颜色**与**字体大小**。  

**Example 3 — group selector** / **示例3——分组合并**  
```css
h1, h2, h3 { color: yellow; }
```
- Apply same style to **multiple elements** at once.  
- 一次性给**多个元素**应用相同样式。  

**Example 4 — descendant selector** / **示例4——后代选择器**  
```css
p strong { color: red; }
```
- Style any `strong` **inside** a `p` (child, grandchild, etc.).  
- 选中 `p` **内部**的所有 `strong`（子、孙等所有后代）。  

---

## Classes and IDs: Definition and Use  
## class 与 id：定义与用法

- **Class (`class="..."`)** — assign a **category**; can be **reused** on **multiple elements**.  
- **Class（`class="..."`）**——赋予**类别名**；可在**多个元素**上**重复使用**。  
- **ID (`id="..."`)** — assign a **unique name**; should be **used once per page**.  
- **ID（`id="..."`）**——赋予**唯一名称**；**每页仅使用一次**为宜。  

**Class selector** / **class 选择器**  
```html
<h2 class="aka">Class example</h2>
```
```css
/* Element + class */
h2.aka { color: red; }
/* Class alone (any element) */
.aka   { color: red; }
```
- Use a leading **dot `.`** before class names in CSS.  
- CSS 中以**点号 `.`**开头表示 class 名。  

**ID selector** / **ID 选择器**  
```html
<h2 id="grn">ID example</h2>
```
```css
/* Element + id */
h2#grn { color: green; }
/* ID alone */
#grn   { color: green; }
```
- Use a leading **hash `#`** before ID names in CSS.  
- CSS 中以**井号 `#`**开头表示 ID 名。  

---

## Class vs ID: When to Use Which  
## 何时使用 class、何时使用 id

- **Default to class** for styling; it’s **reusable** and flexible.  
- **默认使用 class** 来定义样式；其**可复用**且灵活。  
- Use **id** when a **single, uniquely identifiable** element needs special styling or anchor linking.  
- 当需要对**单一且唯一**的元素进行特殊样式或锚点链接时使用 **id**。  
- Avoid over‑mixing complex id/class rules; it can **complicate priority reasoning**.  
- 避免在大项目中**过度混用**复杂的 id/class 规则，以免**难以判断优先级**。  

---

## Specificity & Source Order  
## 优先级与后定义覆盖

- If styles **conflict**, the rule **defined later wins** (same specificity).  
- 当样式**冲突**时，在**同等优先级**下，**后写的规则**会覆盖前面的规则。  
- Between **class** and **id**, the **ID selector** is **more specific** and therefore **wins**.  
- **class 与 id 冲突**时，**ID 选择器**的**优先级更高**，因此会**覆盖**。  

---

## Link Pseudo‑classes and Order (LVHA)  
## 链接伪类与推荐顺序（LVHA）

- For `<a>` links, pseudo‑classes: `:link` (unvisited), `:visited` (visited), `:hover` (pointer over), `:active` (during click).  
- `<a>` 链接的伪类：`:link`（未访问）、`:visited`（已访问）、`:hover`（悬停）、`:active`（按下时）。  
- Recommended declaration order: **`:link` → `:visited` → `:hover` → `:active`**.  
- 建议按 **`:link` → `:visited` → `:hover` → `:active`** 的顺序书写。  

```css
a:link    { color: #06c; }
a:visited { color: #639; }
a:hover   { text-decoration: underline; }
a:active  { color: #c00; }
```

---

## Three Ways to Add CSS in HTML  
## 在 HTML 中引入 CSS 的三种方式

1. **Internal stylesheet** — `<style>` inside `<head>`.  
1. **内部样式表**——在 `<head>` 内写 `<style>`。  
   ```html
   <head>
     <meta charset="UTF-8">
     <style>
       body { color: blue; }
       h1, h2, h3 { color: yellow; }
     </style>
   </head>
   ```
   - Effective **for this page only**.  
   - **仅对当前页面**生效。  

2. **External stylesheet** — `<link rel="stylesheet" href="...">` + a `.css` file.  
2. **外部样式表**——使用 `<link rel="stylesheet" href="...">` 引入 `.css` 文件。  
   ```css
   /* wp1-03_style.css */
   @charset "UTF-8";
   body { color: green; font-size: 12pt; }
   h1, h2 { color: blue; }
   ```
   ```html
   <head>
     <meta charset="UTF-8">
     <title>Title</title>
     <link rel="stylesheet" href="wp1-03_style.css">
   </head>
   ```
   - **Share one CSS** across **multiple pages**; best for **site‑wide consistency**.  
   - **多个页面共享**同一个 CSS，利于**全站一致**。  

3. **Inline style** — the `style="..."` attribute on an element.  
3. **行内样式**——在元素上使用 `style="..."` 属性。  
   ```html
   <p style="color: purple;">Inline style example</p>
   ```
   - Makes HTML **harder to maintain**; **avoid** except for **small, local tweaks**.  
   - 会让 HTML **难以维护**；除**局部微调**外应**尽量避免**。  

**Choosing which** / **选择建议**  
- **Many pages share styles** → use **external CSS**.  
- **多页面共享样式** → 使用**外部样式表**。  
- **Page‑only styles** → use **internal CSS**.  
- **仅此页使用的样式** → 使用**内部样式表**。  
- **Tiny one‑off override** → consider **inline**, but keep minimal.  
- **少量一次性覆盖** → 可用**行内样式**，但尽量少。  

---

## Color Specifications  
## 颜色指定方法

- **Named colors** (basic 16 names are widely supported).  
- **颜色名称**（基础 16 色广泛支持）。  
- **Hexadecimal RGB** — `#RRGGBB` (0x00–0xFF per channel) or shorthand `#RGB`.  
- **十六进制 RGB**——`#RRGGBB`（每通道 0x00–0xFF）或简写 `#RGB`。  

**RGB channels** / **RGB 三通道**  
```
R: 00–FF, G: 00–FF, B: 00–FF
示例 Examples:
#000000 → black / 黑
#FFFFFF → white / 白
#00FF00 → green / 绿
#0F0    → shorthand for #00FF00 / 简写
```

---

## Comments in HTML and CSS  
## HTML 与 CSS 中的注释

- **HTML comments**: `<!-- ... -->`.  
- **HTML 注释**：`<!-- ... -->`。  
- **CSS comments**:  `/* ... */`.  
- **CSS 注释**：`/* ... */`。  
- Comments are **ignored by browsers**, useful for **leaving notes, reasons, or old code**.  
- 注释会被浏览器**忽略**，适合**保留说明、修改原因或旧代码**。  

---

## Practice: Internal → External CSS Refactor  
## 实操练习：内联样式到外部样式重构

1. Create **`wp1-03-1.html`** with an **internal** stylesheet, then test in the browser.  
1. 新建 **`wp1-03-1.html`**，先写**内部样式表**，在浏览器测试。  
2. Create **`wp1-03_style.css`** in the **same folder**, move rules from `<style>` into it.  
2. 在**同一文件夹**创建 **`wp1-03_style.css`**，把 `<style>` 中的规则迁移进去。  
3. In HTML, **remove** the old `<style>` rules and **link** the CSS via `<link>`.  
3. 在 HTML 中**删除**旧的 `<style>` 规则，并用 `<link>` **引入** CSS。  
4. Confirm styles still apply; now **multiple pages** can share this stylesheet.  
4. 确认样式仍然生效；此后**多个页面**可共享该样式表。  

**Mini checklist / 小清单**  
```
- Keep class names meaningful (e.g., .btn-primary, .note).
- Prefer classes over IDs for styling hooks.
- Declare link pseudo-classes in LVHA order.
- Use external CSS for shared site-wide design.
- Colors: prefer hex or modern CSS color functions when needed.
- 注：同等优先级时，后写的规则会覆盖先写的规则；ID > class。
```

---

## Quick Checklist  
## 快速清单

- Separate **structure (HTML)** from **presentation (CSS)**.  
- **结构（HTML）**与**表现（CSS）**相分离。  
- Choose **external** vs **internal** vs **inline** appropriately.  
- 结合场景选择 **外部/内部/行内** 样式。  
- Use **classes** for reusable styles; reserve **IDs** for unique elements.  
- **可复用样式用 class**；**唯一元素用 ID**。  
- Declare **link pseudo‑classes** in **LVHA** order.  
- 链接伪类按 **LVHA** 顺序声明。  
- Prefer **hex RGB** or **named colors**; ensure **contrast & accessibility**.  
- 颜色优先用 **十六进制**或**名称**；注意**对比度与可访问性**。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture02.md) · [Next Lecture / 下一讲 →](./lecture04.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

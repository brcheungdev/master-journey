[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 10: Flexbox and Responsive Web Design (RWD)  
# 第10讲：Flexbox 弹性布局与响应式网页设计（RWD）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Flexbox Overview](#flexbox-overview)  
- Flexbox 概述
- [Core Terms: Container / Items / Axes](#core-terms-container--items--axes)  
- 核心术语：容器 / 项目 / 轴线
- [Getting Started: `flex1.html` Structure](#getting-started-flex1html-structure)  
- 入门示例：`flex1.html` 结构
- [`display:flex` + First Result](#displayflex--first-result)  
- `display:flex` 初体验
- [`flex-direction` (row/row-reverse/column/column-reverse)](#flex-direction-rowrow-reversecolumncolumn-reverse)  
- `flex-direction`（主轴方向）
- [`flex-wrap` (nowrap/wrap/wrap-reverse)](#flex-wrap-nowrapwrapwrap-reverse)  
- `flex-wrap`（是否换行）
- [`flex-flow` Shorthand](#flex-flow-shorthand)  
- `flex-flow` 速记写法
- [`justify-content` (main-axis alignment)](#justify-content-main-axis-alignment)  
- `justify-content`（主轴对齐）
- [What Is RWD & Why](#what-is-rwd--why)  
- RWD 是什么与动机
- [RWD Pros & Cons](#rwd-pros--cons)  
- RWD 的优缺点
- [RWD Step 1: `meta viewport`](#rwd-step-1-meta-viewport)  
- RWD 步骤1：`meta viewport`
- [Viewport: CSS Pixels & DPR](#viewport-css-pixels--dpr)  
- 视口：CSS 像素与 DPR
- [RWD Step 2: Relative Sizing (%/vw/vh)](#rwd-step-2-relative-sizing-vwvh)  
- RWD 步骤2：相对尺寸（%/vw/vh）
- [RWD Step 3: Media Queries](#rwd-step-3-media-queries)  
- RWD 步骤3：媒体查询
- [Where to Write Media Queries (`@media`, `link[media]`, `@import`)](#where-to-write-media-queries-media-linkmedia-import)  
- 媒体查询写在哪里（`@media`、`link[media]`、`@import`）
- [Mobile-first vs Desktop-first](#mobile-first-vs-desktop-first)  
- 移动优先 vs 桌面优先
- [What to Switch at Breakpoints](#what-to-switch-at-breakpoints)  
- 断点切换哪些东西
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## Flexbox Overview  
## Flexbox 概述

- **CSS Flexible Box Layout** (**Flexbox**) simplifies **horizontal/vertical arrangements** compared with legacy **`float`**-based layouts.  
- **CSS 弹性盒布局（Flexbox）**相较传统依赖 **`float`** 的方式，可更**简洁**且**灵活**地实现水平/垂直排列。  
- Useful foundation for **responsive** layouts; supported in **modern browsers (IE11+)**.  
- 是实现**响应式**布局的基础；**现代浏览器（IE11+）**均提供支持。  

---

## Core Terms: Container / Items / Axes  
## 核心术语：容器 / 项目 / 轴线

- **Flex container**: parent that holds flex items.  
- **Flex 容器**：承载 flex 项目的**父元素**。  
- **Flex items**: direct children of the container.  
- **Flex 项目**：容器的**直接子元素**。  
- **Main axis**: axis along **`flex-direction`**; **Cross axis**: perpendicular axis.  
- **主轴**：与 **`flex-direction`** 一致的轴；**副轴**：与主轴**垂直**的轴。  

```
[flex container]
main axis →   item1   item2   item3
cross axis
  ↓
```
- The **`flex-direction`** default is **`row`** (left→right).  
- **`flex-direction`** 默认是 **`row`**（从左到右）。  

---

## Getting Started: `flex1.html` Structure  
## 入门示例：`flex1.html` 结构

```html
<div class="flex-container">
  <div class="item">box1</div>
  <div class="item">box2</div>
  <div class="item">box3</div>
  <div class="item">box4</div>
</div>
```
- Parent uses class **`flex-container`**; children use class **`item`**.  
- 父元素使用类 **`flex-container`**；子元素使用类 **`item`**。  

---

## `display:flex` + First Result  
## `display:flex` 初体验

```css
.flex-container { display: flex; }
.item { width: 90px; height: 90px; }
```
- Items arrange **inline on the main axis** and **try to fit** within the container’s width.  
- 子项会**沿主轴横排**，并**尽量适配**容器宽度。  

---

## `flex-direction` (row/row-reverse/column/column-reverse)  
## `flex-direction`（主轴方向）

- `row`: items **left→right** (default).  
- `row`：**从左到右**（默认）。  
- `row-reverse`: items **right→left**.  
- `row-reverse`：**从右到左**。  
- `column`: items **top→bottom** (main axis is **vertical**).  
- `column`：**从上到下**（主轴变为**纵向**）。  
- `column-reverse`: items **bottom→top**.  
- `column-reverse`：**从下到上**。  

---

## `flex-wrap` (nowrap/wrap/wrap-reverse)  
## `flex-wrap`（是否换行）

- `nowrap` (default): items **don’t wrap**; widths may **shrink** to fit one line.  
- `nowrap`（默认）：**不换行**；项宽可能被**压缩**以适配单行。  
- `wrap`: items **wrap to the next line** (top→bottom).  
- `wrap`：**允许换行**（从上到下）。  
- `wrap-reverse`: items wrap **bottom→top**.  
- `wrap-reverse`：**反向**换行（从下到上）。  

```css
.flex-container { display: flex; flex-wrap: wrap; }
```
- Example: 4 items of **90px** width within a **300px** container → the 4th item **wraps**.  
- 例如：4 个 **90px** 宽度的项目在 **300px** 容器内 → 第 4 个会**换行**。  

---

## `flex-flow` Shorthand  
## `flex-flow` 速记写法

- Combine **`flex-direction`** and **`flex-wrap`**: `flex-flow: row wrap;` (default `row nowrap`).  
- 将 **`flex-direction`** 与 **`flex-wrap`** 合并：`flex-flow: row wrap;`（默认 `row nowrap`）。  

---

## `justify-content` (main-axis alignment)  
## `justify-content`（主轴对齐）

- `flex-start` (default) — align to **start**; `flex-end` — align to **end**; `center` — **centered**.  
- `flex-start`（默认）——**起始**对齐；`flex-end`——**末尾**对齐；`center`——**居中**。  
- `space-between` — first item at start, last at end, others **split remaining space**.  
- `space-between`——首项贴起点、末项贴终点，其他**均分剩余空间**。  
- `space-around` — items have **equal outer spaces** around them.  
- `space-around`——项目两侧留有**均等外间距**。  

```css
.flex-container { justify-content: space-between; }
```

---

## What Is RWD & Why  
## RWD 是什么与动机

- **Responsive Web Design (RWD)**: one **HTML + CSS**, styles **switch** by environment to produce **appropriate layouts** across devices.  
- **响应式网页设计（RWD）**：用一份 **HTML + CSS**，根据环境**切换样式**，在不同设备上形成**合适布局**。  
- Screens vary by **size** and **resolution**; RWD avoids maintaining **separate sites** for PC/phone/tablet.  
- 屏幕的**尺寸**与**分辨率**多样；RWD 可避免为 PC/手机/平板分别维护**不同站点**。  

---

## RWD Pros & Cons  
## RWD 的优缺点

- **Pros**: single source to maintain; **SEO-friendly**; **one URL** simplifies **sharing**.  
- **优点**：单一源码便于维护；对 **SEO** 友好；**统一 URL** 便于**分享**。  
- **Cons**: mobile may download **heavy** PC assets; some **design freedom** limitations; **build complexity** increases.  
- **缺点**：移动端可能下载**较重**资源；**设计自由度**受限；**构建复杂度**上升。  

---

## RWD Step 1: `meta viewport`  
## RWD 步骤1：`meta viewport`

- Add the **viewport meta** inside `<head>` to define **layout viewport** size and initial scale.  
- 在 `<head>` 中加入 **viewport meta**，定义**布局视口**宽度与初始缩放。  

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

- Without it, phones often simulate a **~980px** wide viewport, forcing users to **pinch-zoom**.  
- 若不设置，手机通常模拟 **~980px** 视口，用户需**手动缩放**才能阅读。  

---

## Viewport: CSS Pixels & DPR  
## 视口：CSS 像素与 DPR

- With viewport set, page CSS pixels are based on **device pixel ratio (DPR)**, not the physical resolution.  
- 设置 viewport 后，页面的 CSS 像素以**设备像素比（DPR）**为基准，而非物理分辨率。  
- Examples (CSS px after viewport):  
- 示例（设置 viewport 后的 CSS 像素）：  

```
iPhone XR/11: 828×1792, DPR=2 → 414×896 (CSS px)
iPhone X/XS/11 Pro: 1125×2436, DPR=3 → 375×812 (CSS px)
iPad mini: 1536×2048, DPR=2 → 768×1024 (CSS px)
```

---

## RWD Step 2: Relative Sizing (%/vw/vh)  
## RWD 步骤2：相对尺寸（%/vw/vh）

- Prefer **relative units** for widths/heights: `%`, `vw`, `vh`, or font-relative `em`/`rem`.  
- 尽量使用**相对单位**：`%`、`vw`、`vh`，或与字体相关的 `em`/`rem`。  
- Avoid rigid **absolute** units (`px`, `mm`, `in`) except when necessary.  
- 除非必要，避免使用**绝对单位**（`px`、`mm`、`in` 等）。  

---

## RWD Step 3: Media Queries  
## RWD 步骤3：媒体查询

- Use **media queries** to branch CSS by **viewport width**, **orientation**, or **media type**.  
- 用 **媒体查询**按**视口宽度**、**方向**或**媒体类型****分支** CSS。  

```css
/* Base (mobile-first) */
.card { font-size: 14px; }

/* ≥480px */
@media (min-width: 480px) {
  .grid { display: flex; }
}

/* ≥768px */
@media (min-width: 768px) {
  .card { font-size: 16px; }
}

/* ≥1024px */
@media (min-width: 1024px) {
  .sidebar { display: block; }
}
```
- **Breakpoints** are the **widths** where the layout **changes**; write **narrow → wide** to let later rules **override** earlier ones.  
- **断点**是布局**发生变化**的宽度；按 **窄 → 宽** 顺序编写，便于**后写覆盖**前写。  

---

## Where to Write Media Queries (`@media`, `link[media]`, `@import`)  
## 媒体查询写在哪里（`@media`、`link[media]`、`@import`）

- **Inside CSS** with `@media { ... }` for **partial branching**.  
- 在 **CSS 内**用 `@media { ... }` 做**局部切换**。  
- In **HTML** via `<link rel="stylesheet" media="screen and (min-width: 600px)">`.  
- 在 **HTML** 中通过 `<link rel="stylesheet" media="screen and (min-width: 600px)">`。  
- With **`@import`** at the **top** of a stylesheet (after `@charset`).  
- 在样式表**顶部**（`@charset` 之后）用 **`@import`** 引入外部样式。  

---

## Mobile-first vs Desktop-first  
## 移动优先 vs 桌面优先

- **Mobile-first**: start from **small** screens and scale up with **`min-width`** queries (**recommended**).  
- **移动优先**：从**小屏**出发，用 **`min-width`** 逐步增强（**推荐**）。  
- **Desktop-first**: start from **large** screens and scale down with **`max-width`** queries.  
- **桌面优先**：从**大屏**出发，用 **`max-width`** 逐步收敛。  
- Browsers apply rules **top→bottom**; ensure **order** so later rules override as intended.  
- 浏览器自上而下应用规则；注意**书写顺序**以保证覆盖关系。  

---

## What to Switch at Breakpoints  
## 断点切换哪些东西

- **Layout**: **two-column ↔ one-column**, reorder or wrap flex items.  
- **布局**：**双栏↔单栏**、调整或换行 flex 项目。  
- **Visibility**: **show all ↔ hide some** details.  
- **可见性**：**全部显示↔隐藏部分**内容。  
- **Assets**: **higher-res ↔ lower-res** backgrounds for performance.  
- **资源**：**高分辨率↔低分辨率**背景以优化性能。  
- Note: media queries only **switch CSS**; they **don’t change HTML content**.  
- 注意：媒体查询仅**切换 CSS**，**不能改变** HTML 标签与正文。  

---

## Quick Checklist  
## 快速清单

- Use **flexbox** for robust alignment; pick `flex-direction`, `flex-wrap`, `justify-content` per design.  
- 使用 **flexbox** 实现稳健对齐；按需选择 `flex-direction`、`flex-wrap`、`justify-content`。  
- Add **`<meta name="viewport">`** for correct mobile scaling.  
- 添加 **`<meta name="viewport">`** 以获得正确的移动端缩放。  
- Prefer **relative units**; keep **breakpoints** clear and consistent.  
- 优先使用**相对单位**；设定**清晰一致**的断点。  
- Write **mobile-first** queries and let later rules **override**.  
- 采用**移动优先**的写法，并让后续规则**覆盖**之前的规则。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture09.md) · [Next Lecture / 下一讲 →](./lecture11.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

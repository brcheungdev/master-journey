[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 09: HTML5 Semantic Structure (Header/Nav/Article/Section/Aside/Footer) and CSS Layout Effects  
# 第09讲：HTML5 语义结构（Header/Nav/Article/Section/Aside/Footer）与 CSS 布局与效果

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [HTML Outline & Sections: Why It Matters](#html-outline--sections-why-it-matters)  
- HTML 的“文档大纲”与“分节”：为什么重要
- [From HTML4 to HTML5: What Changed](#from-html4-to-html5-what-changed)  
- 从 HTML4 到 HTML5：发生了什么变化
- [Semantic Sectioning Tags Overview](#semantic-sectioning-tags-overview)  
- 语义化分节元素概览
- [`<header>` and `<footer>`](#header-and-footer)  
- `<header>` 与 `<footer>`
- [`<nav>`: Site/Page Navigation](#nav-sitepage-navigation)  
- `<nav>`：站点/页面导航
- [`<article>`: Self-contained Content](#article-self-contained-content)  
- `<article>`：可独立分发的内容
- [`<section>` vs `<div>`](#section-vs-div)  
- `<section>` 与 `<div>` 的差别
- [`<aside>`: Tangential/Supporting Info](#aside-tangentialsupporting-info)  
- `<aside>`：旁注/补充信息
- [Hands-on: Semantic Markup for a Kyoto Page](#handson-semantic-markup-for-a-kyoto-page)  
- 实操：为 kyoto.html 进行语义标注
- [CSS Layout: Max-Width, Display, and Descendant Selectors](#css-layout-max-width-display-and-descendant-selectors)  
- CSS 布局：max-width、display 与后代选择器
- [Hide vs Invisible: `display:none` vs `visibility:hidden`](#hide-vs-invisible-displaynone-vs-visibilityhidden)  
- 隐藏与“不可见”：`display:none` vs `visibility:hidden`
- [Floats & Clear: Two-Column Layout with Footer](#floats--clear-twocolumn-layout-with-footer)  
- 浮动与清除：双栏布局与页脚
- [List Styles in Aside, Link Colors & Hover](#list-styles-in-aside-link-colors--hover)  
- 侧栏列表样式、链接颜色与悬停
- [Image & Quote Tweaks: `.photo` float and `.quotation` clear](#image--quote-tweaks-photo-float-and-quotation-clear)  
- 图像与引用微调：`.photo` 浮动与 `.quotation` 清除环绕
- [Rounded Corners: `border-radius` (complex radii)](#rounded-corners-borderradius-complex-radii)  
- 圆角：`border-radius`（复杂角半径）
- [Shadows: `box-shadow` Parameters & `inset`](#shadows-boxshadow-parameters--inset)  
- 阴影：`box-shadow` 参数与 `inset`
- [Gradients: `linear-gradient` and `radial-gradient`](#gradients-lineargradient-and-radialgradient)  
- 渐变：`linear-gradient` 与 `radial-gradient`
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## HTML Outline & Sections: Why It Matters  
## HTML 的“文档大纲”与“分节”：为什么重要

- The **outline** describes a page’s **textual structure** (what’s **main content**, **header**, **navigation**, etc.).  
- **文档大纲**描述页面的**文章结构**（哪些是**主内容**、**页眉**、**导航**等）。  
- Proper sectioning helps **crawlers** (e.g., Google) understand your page and index it accurately.  
- 正确分节可以帮助**搜索引擎爬虫**更准确地理解与收录页面。  
- Use semantic tags like **`<header>`**, **`<footer>`**, **`<nav>`**, **`<aside>`**, **`<article>`**, **`<section>`** to mark structure; this is **about document structure, not layout**.  
- 用 **`<header>`**、**`<footer>`**、**`<nav>`**、**`<aside>`**、**`<article>`**、**`<section>`** 等语义元素标注结构；它们描述**文章结构**而非**视觉布局**。  

---

## From HTML4 to HTML5: What Changed  
## 从 HTML4 到 HTML5：发生了什么变化

- **HTML4.01 and earlier** relied on **headings** (`<h1>`–`<h6>`) and **`<div id="...">`** to imply sections.  
- **HTML4.01 及更早版本**主要依靠**标题**（`<h1>`–`<h6>`）与 **`<div id="...">`** 隐式划分区域。  
- **HTML5** introduced **explicit sectioning elements**: `<header>`, `<footer>`, `<nav>`, `<section>`, `<aside>`, `<article>`.  
- **HTML5** 新增**显式分节元素**：`<header>`、`<footer>`、`<nav>`、`<section>`、`<aside>`、`<article>`。  

---

## Semantic Sectioning Tags Overview  
## 语义化分节元素概览

- Typical two-column page: **Header**, **Navigation**, **Main**, **Sidebar**, **Footer** → use matching semantic elements.  
- 典型双栏页面：**页眉**、**导航**、**主块**、**侧栏**、**页脚** → 选用对应的语义元素。  

```
<header>   — Page intro / site branding
<nav>      — Site/page navigation
<article>  — Self-contained main content
<section>  — Thematic subsections inside article or page
<aside>    — Tangential sidebar info
<footer>   — Footer for the nearest section
```

- Headings (`<h1>`–`<h6>`) still outline content **within sections**.  
- 标题元素（`<h1>`–`<h6>`）仍用于**分节内部**的层级结构。  

---

## `<header>` and `<footer>`  
## `<header>` 与 `<footer>`

- Use `<header>` for **introduction** or a **group of navigational aids**.  
- `<header>` 用于**页面/章节引言**或**导航组**。  
- Use `<footer>` for the **footer of the nearest section** (page/article/section).  
- `<footer>` 用于**最近一级分节**（页面/文章/小节）的**页脚**。  
- `<small>` is for **small print** (disclaimers, legal notes), **not** “make text smaller” per se.  
- `<small>` 用于**细目/免责声明/版权等**，**并非**单纯“字体更小”。  

---

## `<nav>`: Site/Page Navigation  
## `<nav>`：站点/页面导航

- Enclose the **major navigation section(s)**; not every link group requires `<nav>`.  
- 只需把**主要导航区域**包在 `<nav>` 中；并非所有链接群都必须 `<nav>`。  
- Footer **legal links** etc. often belong under **`<footer>`**, not `<nav>`.  
- 底部**条款/版权**等链接通常放在 **`<footer>`** 而非 `<nav>`。  

---

## `<article>`: Self-contained Content  
## `<article>`：可独立分发的内容

- Represents a **self-contained** composition: forum post, news/blog entry, comment, magazine article.  
- 表示可**独立成篇**的内容：论坛帖、新闻/博客文章、评论、杂志条目等。  
- **Nested `article`** is allowed; inner articles are **related** to the outer article.  
- **嵌套 `article`** 是允许的；内层与外层**语义相关**。  

---

## `<section>` vs `<div>`  
## `<section>` 与 `<div>` 的差别

- `<section>` groups **thematically related** content (think “**section** of a document”).  
- `<section>` 用于归纳**主题相关**的内容（可类比“**章节**”）。  
- `<div>` is **non-semantic**; use it for **styling hooks** or when no better semantic element fits.  
- `<div>` **无语义**，用于**样式分组**或确无更合适语义元素时。  
- A section **may have a heading**, but it’s **not required**; if present, put it **inside** the section.  
- `<section>` **可有标题**但**非必需**；若有，应写在**内部**。  

---

## `<aside>`: Tangential/Supporting Info  
## `<aside>`：旁注/补充信息

- Use for **side content** related to but distinct from the main flow — like **callouts, tips, or sidebars**.  
- 适用于与主体**相关但独立**的边栏信息——如**提示、边注、侧栏**。  

---

## Hands-on: Semantic Markup for a Kyoto Page  
## 实操：为 kyoto.html 进行语义标注

- Mark **“おいでやす京都”** as `<header>`; move **legal small print** to `<footer>`.  
- 将“おいでやす京都”作为 `<header>`；把**版权/细目**移入 `<footer>`。  
- Wrap the **main navigation** with `<nav>`.  
- 用 `<nav>` 包裹**主导航**。  
- Put **Kinkaku-ji** and **Kiyomizu-dera** as **`<section>`** blocks; wrap them together as an **`<article>`**.  
- 将**金阁寺**与**清水寺**各作一个 **`<section>`**；对其整体包裹为 **`<article>`**。  
- Use `<aside>` for **tangential notes**.  
- 用 `<aside>` 表示**余谈/补充**内容。  

---

## CSS Layout: Max-Width, Display, and Descendant Selectors  
## CSS 布局：max-width、display 与后代选择器

- Use **`max-width`** to limit overall width responsively; `width` may **overflow** on narrow viewports.  
- 用 **`max-width`** 限制页面最大宽度；`width` 在窄屏上可能**溢出**。  
- Ensure HTML5 sectioning elements are **`display:block`** (legacy browser quirk).  
- 确保 HTML5 分节元素为 **`display:block`**（照顾旧环境/UA）。  
- Center header/nav text with `text-align: center;`.  
- 用 `text-align: center;` 居中 header/nav 文本。  
- **Descendant selector** example: `nav li { ... }` targets **only `li` inside `nav`**; set `display: inline` to line up links; remove bullets via `list-style-type: none`.  
- **后代选择器**示例：`nav li { ... }` 仅选中 **`nav` 内的 `li`**；设 `display: inline` 横向排列；`list-style-type: none` 去除项目符号。  

---

## Hide vs Invisible: `display:none` vs `visibility:hidden`  
## 隐藏与“不可见”：`display:none` vs `visibility:hidden`

- **`display:none`** removes the element **from layout**; no space is reserved.  
- **`display:none`** 让元素**不参与布局**，不占空间。  
- **`visibility:hidden`** hides the element but **keeps its layout space**.  
- **`visibility:hidden`** 隐藏但**保留空间**。  

---

## Floats & Clear: Two-Column Layout with Footer  
## 浮动与清除：双栏布局与页脚

- Float **`article` left**, **`aside` right** for a two-column layout.  
- 让 **`article` 向左浮动**、**`aside` 向右浮动** 实现双栏。  
- Use `clear: both` on **`footer`** to **stop wrapping** and ensure it appears **below**.  
- 在 **`footer`** 上用 `clear: both` **解除环绕**，避免页脚被包围。  

---

## List Styles in Aside, Link Colors & Hover  
## 侧栏列表样式、链接颜色与悬停

- Customize **`aside ul, aside li`** list styles.  
- 自定义 **`aside ul, aside li`** 的列表样式。  
- Style links: change **link color**, **remove underline**, and add **`:hover`** color change.  
- 链接样式：修改**颜色**、**去下划线**，并在 **`:hover`** 时改变颜色。  

---

## Image & Quote Tweaks: `.photo` float and `.quotation` clear  
## 图像与引用微调：`.photo` 浮动与 `.quotation` 清除环绕

- Add **class `photo`** to images and float **left** for text wrap.  
- 让图片加上 **`photo` 类**并**左浮动**以实现文字环绕。  
- Add **class `quotation`** to a paragraph to **clear floats** and start below images.  
- 段落加上 **`quotation` 类**以**清除环绕**，从图片下方开始。  

---

## Rounded Corners: `border-radius` (complex radii)  
## 圆角：`border-radius`（复杂角半径）

- You can set **different radii** per corner; syntax supports **horizontal/vertical** radii with a **slash**.  
- 可为四角设置**不同半径**；语法支持用 **斜杠**分别指定**水平/垂直**半径。  

```css
/* TL TR BR BL / TL TR BR BL  (clockwise) */
border-radius: 100px 25px 50px 50px / 50px 25px 50px 25px;
```

---

## Shadows: `box-shadow` Parameters & `inset`  
## 阴影：`box-shadow` 参数与 `inset`

- Syntax: `box-shadow: offset-x offset-y blur spread color [inset];`.  
- 语法：`box-shadow: 水平偏移 垂直偏移 模糊半径 扩散半径 颜色 [inset]`。  
- Positive **x** → right, negative → left; positive **y** → down, negative → up.  
- **x** 正值→向右，负值→向左；**y** 正值→向下，负值→向上。  
- **Blur** controls feathering; **spread** grows/shrinks the shadow; **`inset`** changes to an **inner shadow**.  
- **模糊**控制柔化；**扩散**控制扩大/收缩；**`inset`** 将**外阴影**改为**内阴影**。  

---

## Gradients: `linear-gradient` and `radial-gradient`  
## 渐变：`linear-gradient` 与 `radial-gradient`

- `linear-gradient(angle|to side, color-stops...)` — angle in **deg** or **to top/right/bottom/left** keywords.  
- `linear-gradient(角度|to 方向, 颜色序列...)`——角度可用 **deg**，或 `to top/right/bottom/left`。  
- Provide **start/mid/end colors** and optional **stop positions**.  
- 指定**起始/中间/结束**颜色，可选**位置**。  
- **Radial gradients** use `radial-gradient(position, shape/size, colors...)`.  
- **径向渐变**使用 `radial-gradient(位置, 形状/大小, 颜色...)`。  

---

## Quick Checklist  
## 快速清单

- Use **semantic sectioning** for structure; **don’t** confuse it with layout.  
- 用**语义分节**表达结构；**不要**把结构与布局混为一谈。  
- Prefer `<section>` for **thematic groups**; `<div>` for **pure styling hooks**.  
- **主题分组**优先用 `<section>`；**纯样式**用 `<div>`。  
- Keep `<nav>` for **major navigation**; legal/utility links usually belong to `<footer>`.  
- `<nav>` 仅用于**主要导航**；条款/版权类链接通常放 `<footer>`。  
- Use **max-width**, **floats/clear** (or modern layout methods) to achieve **two-column** layouts.  
- 用 **max-width**、**浮动/清除**（或现代布局方案）实现**双栏**。  
- Enhance UI with **`border-radius`**, **`box-shadow`**, **gradients** judiciously.  
- 合理使用 **圆角**、**阴影**、**渐变**增强界面表现。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture08.md) · [Next Lecture / 下一讲 →](./lecture10.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

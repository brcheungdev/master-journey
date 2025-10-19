[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 11: Full‑Screen Page Layout (Part 1) with Flexbox  
# 第11讲：使用 Flexbox 实现全屏页面布局（上）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Goal & Setup](#goal--setup)  
- 目标与准备
- [Reset CSS: Why and What](#reset-css-why-and-what)  
- Reset CSS：目的与要点
- [HTML Skeleton: Title & CSS Order](#html-skeleton-title--css-order)  
- HTML 框架：标题与样式表顺序
- [Header: Logo as H1 and Home Link](#header-logo-as-h1-and-home-link)  
- 头部：用 H1 放置 Logo 并链接首页
- [Navigation: `<nav>` + `<ul class="main-navi">`](#navigation-nav--ul-classmain-navi)  
- 导航：`<nav>` + `<ul class="main-navi">`
- [Global Styles: Typography & Links & Images](#global-styles-typography--links--images)  
- 全局样式：排版、链接与图片
- [Nav Adjustment 1: Horizontal Menu](#nav-adjustment-1-horizontal-menu)  
- 导航调整一：横向菜单
- [Nav Adjustment 2: Header Flex & Spacing](#nav-adjustment-2-header-flex--spacing)  
- 导航调整二：Header Flex 与两端对齐
- [Wrapper Width: `.wrap` (max-width + center)](#wrapper-width-wrap-max-width--center)  
- 容器宽度：`.wrap`（最大宽度与居中）
- [Content Block: Centered Text & Headings](#content-block-centered-text--headings)  
- 内容块：文本居中与标题样式
- [Full‑Screen Background: `#home.bg` + `100vh`](#fullscreen-background-homebg--100vh)  
- 全屏背景：`#home.bg` + `100vh`
- [Responsive: Viewport & Media Query (≤600px)](#responsive-viewport--media-query-600px)  
- 响应式：视口与媒体查询（≤600px）
- [Recap: `box-sizing`, Line Height, Font Families, Relative Units](#recap-box-sizing-line-height-font-families-relative-units)  
- 复习：`box-sizing`、行高、字体族、相对单位
- [Upload & Test on KCG Server](#upload--test-on-kcg-server)  
- 上传与在 KCG 服务器测试
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## Goal & Setup  
## 目标与准备

- Build a **full‑screen landing page** with a **header (logo + global nav)**, **centered hero text**, and **cover background**, then add **responsive tweaks**.  
- 目标：制作包含**页眉（Logo + 全局导航）**、**居中主文案**与**覆盖式背景图**的**全屏落地页**，并加入**响应式适配**。  
- Open the **`11HTML`** folder in **VS Code** (materials provided on KING‑LMS).  
- 在 **VS Code** 中打开 **`11HTML`** 资料文件夹（来自 KING‑LMS）。  

---

## Reset CSS: Why and What  
## Reset CSS：目的与要点

- Use a **reset stylesheet** to neutralize **UA defaults** across browsers.  
- 使用 **Reset CSS** 以消除不同浏览器的**默认样式差异**。  
- Typical rules include: `box-sizing: border-box;` reset `margin/padding`; set `button { cursor: pointer; }`; remove default button styles.  
- 常见规则：`box-sizing: border-box;`、重置 `margin/padding`、为 `button` 设定 `cursor: pointer;`、移除按钮默认样式。  

```css
/* reset.css (excerpt / 摘录) */
*, *::before, *::after { box-sizing: border-box; }
html, body, h1, h2, h3, p, ul, li { margin: 0; padding: 0; }
button { cursor: pointer; background: none; border: none; }
```

---

## HTML Skeleton: Title & CSS Order  
## HTML 框架：标题与样式表顺序

- In **`index.html`**, set a **descriptive `<title>`**, then include **`reset.css`** **before** `styles.css` (**later CSS wins**).  
- 在 **`index.html`** 中设置**语义化 `<title>`**，并按 **先 `reset.css` 后 `styles.css`** 的顺序引入（**后引入者优先**）。  

```html
<head>
  <meta charset="UTF-8">
  <title>Kyoto — Temples & Seasons</title>
  <link rel="stylesheet" href="reset.css">
  <link rel="stylesheet" href="styles.css">
</head>
```

---

## Header: Logo as H1 and Home Link  
## 头部：用 H1 放置 Logo 并链接首页

- Add `<header class="page-header">`; place the **logo image inside `<h1>`**; wrap it with a link to **`index.html`**.  
- 新增 `<header class="page-header">`；将**Logo 图片放在 `<h1>`** 内；并用链接指向 **`index.html`**。  

```html
<header class="page-header">
  <h1><a href="index.html"><img class="logo" src="img/logo.png" alt="Kyoto"></a></h1>
  ...
</header>
```

---

## Navigation: `<nav>` + `<ul class="main-navi">`  
## 导航：`<nav>` + `<ul class="main-navi">`

- Create a `<nav>` containing `<ul class="main-navi">` with **three links**: temples, cherry blossoms, autumn foliage.  
- 在 `<nav>` 中放置 `<ul class="main-navi">`，包含**三个链接**：京のお寺、桜の名所、紅葉の名所。  

```html
<nav>
  <ul class="main-navi">
    <li><a href="kyoto.html">京のお寺</a></li>
    <li><a href="kyoto2.html">桜の名所</a></li>
    <li><a href="kyoto3.html">紅葉の名所</a></li>
  </ul>
</nav>
```

---

## Global Styles: Typography & Links & Images  
## 全局样式：排版、链接与图片

- Set **line height** and **text color**; remove link **underlines**; constrain **images** with `max-width: 100%`.  
- 指定**行高**与**文字颜色**；去除链接**下划线**；为图片添加 `max-width: 100%` 以适配容器。  

```css
body { line-height: 1.6; color: #333; }
a { text-decoration: none; color: inherit; }
img { max-width: 100%; height: auto; }
```

---

## Nav Adjustment 1: Horizontal Menu  
## 导航调整一：横向菜单

- Make the menu **horizontal** by applying `display: flex` to **`.main-navi`**; add **left margins** to `li`; remove list markers.  
- 在 **`.main-navi`** 上设 `display: flex` 让菜单**横排**；为 `li` 添加**左外边距**；移除默认**项目符号**。  

```css
.main-navi { display: flex; list-style-type: none; }
.main-navi li + li { margin-left: 24px; }
.main-navi a:hover { color: #c00; } /* hover color 悬停变色 */
```

---

## Nav Adjustment 2: Header Flex & Spacing  
## 导航调整二：Header Flex 与两端对齐

- Make the **header a flex container** and **split** logo and nav with `justify-content: space-between`.  
- 将 **`header` 设为 flex 容器**，用 `justify-content: space-between` **两端对齐** Logo 与导航。  

```css
.page-header { display: flex; justify-content: space-between; align-items: center; }
.logo { width: 180px; margin: 8px 0; } /* adjust size & margin 调整尺寸与边距 */
```

- Add a **top margin** on `.main-navi` if needed to vertically **align** with the logo.  
- 视情况给 `.main-navi` 加 **上外边距** 以与 Logo **纵向对齐**。  

---

## Wrapper Width: `.wrap` (max-width + center)  
## 容器宽度：`.wrap`（最大宽度与居中）

- Add a **`.wrap`** utility to cap width and center blocks; apply to **`header`** and **content**.  
- 定义 **`.wrap`** 工具类用于限制最大宽度并**水平居中**；应用在 **`header`** 与**内容区**。  

```html
<header class="page-header wrap">...</header>
<div class="home-content wrap">...</div>
```
```css
.wrap { max-width: 1000px; margin: 0 auto; padding: 0 16px; }
```

---

## Content Block: Centered Text & Headings  
## 内容块：文本居中与标题样式

- Center the **hero text** with `text-align: center;` add **top margin** to separate from header; increase **font sizes**.  
- 用 `text-align: center;` 让主文案**居中**，并增加**上外边距**与**字号**。  

```css
.home-content { text-align: center; margin-top: 48px; font-size: 1.125rem; }
.home-content h2 { font-size: 2rem; font-family: "MS P明朝", "Times New Roman", serif; }
```

---

## Full‑Screen Background: `#home.bg` + `100vh`  
## 全屏背景：`#home.bg` + `100vh`

- Wrap **`header`** and **`.home-content`** in `<div id="home" class="bg">` and set **full viewport height**.  
- 用 `<div id="home" class="bg">` 将 **`header`** 与 **`.home-content`** 包裹，并设置**占满视口高度**。  

```html
<body>
  <div id="home" class="bg">
    <header class="page-header wrap">...</header>
    <div class="home-content wrap">...</div>
  </div>
</body>
```

```css
#home { min-height: 100vh; }
.bg {
  background-image: url("img/kyoto-hero.jpg");
  background-size: cover;           /* keep aspect & cover 保持纵横比并铺满 */
  background-position: center;      /* center the focal point 焦点居中 */
  background-repeat: no-repeat;
}
```

- **Note**: `.bg` is **reusable** across pages (hence **class**); `#home` is page‑specific (thus **id**).  
- **说明**：`.bg` 可在多页**复用**（用 **class**），`#home` 仅用于本页（用 **id**）。  

---

## Responsive: Viewport & Media Query (≤600px)  
## 响应式：视口与媒体查询（≤600px）

- Add **viewport** meta for correct **CSS pixel** scaling; then use **media queries** to adjust layout on **narrow screens**.  
- 先添加 **viewport** 元信息以获得正确的 **CSS 像素**缩放；再用 **媒体查询**适配**窄屏**布局。  

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

```css
@media (max-width: 600px) {
  .page-header { flex-direction: column; align-items: flex-start; }
  .main-navi { margin-top: 8px; }
  .home-content { margin-top: 32px; font-size: 1rem; }
  .home-content h2 { font-size: 1.5rem; }
}
```

---

## Recap: `box-sizing`, Line Height, Font Families, Relative Units  
## 复习：`box-sizing`、行高、字体族、相对单位

- **`box-sizing: content-box`** (default) measures **content only**; **`border-box`** measures **content + padding + border**.  
- **`box-sizing: content-box`**（默认）表示仅量度**内容区**；**`border-box`** 表示**内容+内边距+边框**总和。  
- **Line height**: e.g., `1.5`, `150%`, or `1.5em` all mean **1.5×** the font size.  
- **行高**：`1.5`、`150%`、`1.5em` 都表示字号的 **1.5 倍**。  
- **Font families**: generic `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, or specific names (e.g., **MS P明朝**, **Arial**).  
- **字体族**：通用族 `serif`、`sans-serif`、`monospace`、`cursive`、`fantasy`，或具体字体（如 **MS P明朝**、**Arial**）。  
- **Relative units**: `%`, `em`, `rem`, `vh`, `vw` help **adapt** to container, root, or viewport.  
- **相对单位**：`%`、`em`、`rem`、`vh`、`vw` 便于随容器、根元素或视口**自适应**。  

---

## Upload & Test on KCG Server  
## 上传与在 KCG 服务器测试

- Upload the **`kyoto`** folder to **`/public_html/web1/task11`** on `web1.kcg.edu`, then test on **PC and smartphone**.  
- 将 **`kyoto`** 目录上传到 `web1.kcg.edu` 的 **`/public_html/web1/task11`**，分别在 **PC 与智能手机**上验证。  

---

## Quick Checklist  
## 快速清单

- **Reset first**, then **site CSS**; make **header** a **flex container**.  
- **先重置**再加载**站点 CSS**；把 **header** 设置为 **flex 容器**。  
- **Flex menu**: `.main-navi { display:flex }` + remove bullets + spacing + `:hover` color.  
- **弹性菜单**：`.main-navi { display:flex }` + 去项目符号 + 间距 + `:hover` 变色。  
- Use **`.wrap`** to cap width and **center** layout.  
- 用 **`.wrap`** 限制宽度并**居中**。  
- **Full‑screen background**: `#home { min-height:100vh }` + `.bg { background-size:cover }`.  
- **全屏背景**：`#home { min-height:100vh }` 与 `.bg { background-size:cover }`。  
- **Viewport + media queries** for **≤600px**: stack header vertically, tweak sizes/margins.  
- 对 **≤600px** 使用 **视口 + 媒体查询**：头部垂直堆叠并调整字号/间距。  

---

[← Previous Lecture / 上一讲](./lecture10.md) · [Next Lecture / 下一讲 →](./lecture12.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

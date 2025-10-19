[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 12: Web Fonts & Two-Column Layout (Continuation)  
# 第12讲：Web 字体与双栏页面布局（续）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Are Web Fonts](#what-are-web-fonts)  
- 什么是 Web 字体
- [Sources: Google Fonts & Adobe Fonts](#sources-google-fonts--adobe-fonts)  
- 字体来源：Google Fonts 与 Adobe Fonts
- [How to Use Google Fonts (Step-by-step)](#how-to-use-google-fonts-step-by-step)  
- 使用 Google Fonts（分步）
- [Apply to `.page-title` + Font Size Tuning](#apply-to-pagetitle--font-size-tuning)  
- 应用到 `.page-title` 与字号微调
- [Caveats of Web Fonts](#caveats-of-web-fonts)  
- Web 字体的注意事项
- [Build a Two-Column Page (`kyoto.html`)](#build-a-two-column-page-kyotohtml)  
- 创建双栏页面（`kyoto.html`）
- [Header & Page Heading Block](#header--page-heading-block)  
- 头部与页面大标题区
- [Footer](#footer)  
- 页脚
- [Layout Skeleton with Flexbox](#layout-skeleton-with-flexbox)  
- 用 Flexbox 的布局骨架
- [Main Content: Sections & Media Rows](#main-content-sections--media-rows)  
- 主内容：分节与图文行
- [Sidebar: Lists & Hover Effects](#sidebar-lists--hover-effects)  
- 侧栏：列表与悬停效果
- [Responsive Adjustments (Mobile)](#responsive-adjustments-mobile)  
- 响应式适配（移动端）
- [Quick Checklist](#quick-checklist)  
- 快速清单


---

## What Are Web Fonts  
## 什么是 Web 字体

- Normally, browsers render text using **fonts installed on the device**; if the specified font is missing, **fallback fonts** appear.  
- 通常浏览器使用**设备已安装的字体**渲染文本；若指定字体缺失，会显示**回退字体**。  
- **Web Fonts** download font files **over the network during page load**, ensuring a **consistent look** on all devices.  
- **Web 字体**在页面加载时**通过网络下载字体文件**，从而在各设备上实现**一致的外观**。  

---

## Sources: Google Fonts & Adobe Fonts  
## 字体来源：Google Fonts 与 Adobe Fonts

- **Google Fonts**: https://fonts.google.com/ (free, easy to embed).  
- **Google Fonts**：https://fonts.google.com/（免费，嵌入简单）。  
- **Adobe Fonts**: https://fonts.adobe.com (requires **Adobe Creative Cloud ID**).  
- **Adobe Fonts**：https://fonts.adobe.com（需要 **Adobe Creative Cloud ID**）。  

---

## How to Use Google Fonts (Step-by-step)  
## 使用 Google Fonts（分步）

1) Pick a font and click **“+ Select this style”**.  
1) 选择字体并点击 **“+ Select this style”**。  
2) On the **Embed** panel, copy the provided **`<link href="…">`** snippet.  
2) 在 **Embed** 面板复制提供的 **`<link href="…">`** 代码片段。  
3) Paste it inside your page’s **`<head>`** (e.g., `index.html`).  
3) 将其粘贴到页面的 **`<head>`** 中（如 `index.html`）。  
4) Add the font name to your **CSS `font-family`** declarations.  
4) 在 **CSS 的 `font-family`** 中添加该字体名。  

```html
<!-- index.html (head) / 头部引入 -->
<link href="https://fonts.googleapis.com/css2?family=Italianno&display=swap" rel="stylesheet">
```

```css
/* styles.css */
.page-title { 
  font-family: "Italianno", "Times New Roman", serif; 
}
```

---

## Apply to `.page-title` + Font Size Tuning  
## 应用到 `.page-title` 与字号微调

- Increase **desktop** font sizes where appropriate, and also adjust sizes in the **mobile** media query.  
- 在 **桌面端**适当增大字号，并在**移动端媒体查询**中同步微调。  

```css
/* Desktop / 桌面 */
.page-title { font-size: 3rem; }

/* Mobile / 移动端 */
@media (max-width: 600px) {
  .page-title { font-size: 2.2rem; }
}
```

---

## Caveats of Web Fonts  
## Web 字体的注意事项

- **Large font files** can **slow down** loading — **CJK fonts** are particularly **heavy**.  
- **大型字体文件**会**拖慢**加载，**中日韩字体**尤其**体积大**。  
- Some fonts are **paid** or **license-limited**.  
- 部分字体**需付费**或**有授权限制**。  

---

## Build a Two-Column Page (`kyoto.html`)  
## 创建双栏页面（`kyoto.html`）

- **Copy** `index.html` to create **`kyoto.html`**; then **rename** appropriately.  
- **复制** `index.html` 生成 **`kyoto.html`**，并**重命名**。  
- Change the `<title>` to **“おいでやすKyoto - 京のお寺”**.  
- 将 `<title>` 修改为 **“おいでやすKyoto - 京のお寺”**。  
- Remove the **home-only content block** that followed `</header>`.  
- 删除 `</header>` 后用于首页的**特定内容块**。  
- Change container **`id="home"` → `id="temple"`**, and annotate its closing tag.  
- 将容器 **`id="home"` 改为 `id="temple"`**，并给结束标签**加注释**。  

---

## Header & Page Heading Block  
## 头部与页面大标题区

- Below `</header>`, insert a **page heading block** (`<div class="page-heading">…</div>`) with **centered text** and **background image**.  
- 在 `</header>` 下方加入**页面大标题区**（`<div class="page-heading">…</div>`），**文字居中**并设置**背景图**。  

```css
/* styles.css */
.page-heading {
  padding: 48px 0;
  text-align: center;
  background: url("img/temple-hero.jpg") center / cover no-repeat;
}
.page-heading h2 { font-size: 2rem; margin: 0; }
```

---

## Footer  
## 页脚

- Add `<footer>…</footer>` right before `</body>`; use `<small>` for **legal/notice** text.  
- 在 `</body>` 前添加 `<footer>…</footer>`；**细目/版权**使用 `<small>`。  

```html
<footer>
  <small>© Kyoto Sample. All rights reserved.</small>
</footer>
```

```css
footer { background: #222; color: #ddd; padding: 16px; text-align: center; }
footer small { font-size: 0.875rem; }
```

---

## Layout Skeleton with Flexbox  
## 用 Flexbox 的布局骨架

- Immediately **before** the footer, add a container wrapping **`<article>` (main)** and **`<aside>` (sidebar)**.  
- 在页脚**之前**新增一个容器，内部包含 **`<article>`（主内容）**与 **`<aside>`（侧栏）**。  

```html
<div class="columns wrap">
  <article>…</article>
  <aside>…</aside>
</div>
```

```css
.columns { 
  display: flex; 
  justify-content: space-between; 
  gap: 24px;                 /* space between columns / 双栏间距 */
}
.columns article { flex: 1 1 66%; }
.columns aside   { flex: 1 1 32%; }
```

- Use **percentage/flex-basis** so widths adapt as the viewport changes.  
- 使用**百分比/基础宽度**以便随视口变化自适应。  

---

## Main Content: Sections & Media Rows  
## 主内容：分节与图文行

- In `<article>`, add **two `<section>` blocks** (e.g., **Kinkaku-ji** and **Kiyomizu-dera**).  
- 在 `<article>` 内加入**两个 `<section>`**（例如**金阁寺**与**清水寺**）。  
- For image-with-text rows, wrap **`<img>` and `<p>`** in a parent `<div>` and set it to **`display:flex`**.  
- 图文行请将 **`<img>` 与 `<p>`** 包在父 `<div>` 中，并设为 **`display:flex`**。  

```css
.media-row { display: flex; align-items: flex-start; gap: 12px; }
.media-row img { width: 200px; height: auto; flex: 0 0 auto; }
.media-row p { margin: 0; }
section + section { margin-top: 24px; }  /* space between sections / 分节间距 */
```

---

## Sidebar: Lists & Hover Effects  
## 侧栏：列表与悬停效果

- Add classes to **`<h3>`** and **`<ul>`** (e.g., `.side-title`, `.side-links`); remove bullets; **full-width clickable** items with `display:block`; add **dividers** and **hover** color.  
- 为 **`<h3>`** 与 **`<ul>`** 添加类（如 `.side-title`、`.side-links`）；去除项目符号；用 `display:block` 让项**可全宽点击**；加入**分隔线**与**悬停**变色。  

```css
.side-title { margin: 8px 0; padding-bottom: 4px; border-bottom: 2px solid #ccc; }
.side-links { list-style: none; padding: 0; margin: 0; }
.side-links li + li { border-top: 1px solid #eee; }
.side-links a { display: block; padding: 8px; color: #333; text-decoration: none; }
.side-links a:hover { color: #c00; background: #f9f9f9; }
```

---

## Responsive Adjustments (Mobile)  
## 响应式适配（移动端）

- In a **media query**, **stack** `article` and `aside` vertically: `flex-direction: column;`.  
- 在**媒体查询**中将 `article` 与 `aside` **纵向堆叠**：`flex-direction: column;`。  
- Set both to **`width: 100%`** (or `flex: auto`) for full width.  
- 二者设置为 **`width: 100%`**（或 `flex: auto`）以占满宽度。  
- For media rows, **stack** `img` and `p` vertically.  
- 图文行在移动端将 **`img` 与 `p`** **纵向排列**。  

```css
@media (max-width: 600px) {
  .columns { flex-direction: column; }
  .columns article, .columns aside { flex: 1 1 auto; }
  .media-row { flex-direction: column; }
  .media-row img { width: 100%; }
}
```

---

## Quick Checklist  
## 快速清单

- **Embed** Google Fonts with `<link>`; add to **`font-family`**; tune **desktop + mobile** font sizes.  
- 用 `<link>` **嵌入** Google Fonts；加入 **`font-family`**；同步微调**桌面与移动**字号。  
- Beware of **file size** and **licensing**; CJK fonts are **heavy**.  
- 注意**文件体积**与**授权**问题；CJK 字体**较大**。  
- Build **two columns** using **Flexbox** (`display:flex`, `justify-content`, `gap`, flexible widths).  
- 使用 **Flexbox** 构建**双栏**（`display:flex`、`justify-content`、`gap`、弹性宽度）。  
- **Media queries**: stack columns and media rows on **≤600px** screens.  
- **媒体查询**：在 **≤600px** 屏幕上将各列与图文行**纵向堆叠**。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture11.md) · [Next Lecture / 下一讲 →](./lecture13.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

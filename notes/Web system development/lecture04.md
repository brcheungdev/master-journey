[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 04: Block vs Inline, Fonts, and Images in CSS/HTML  
# 第04讲：块级与内联、字体与图像（CSS/HTML）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Block-level vs Inline Elements: Concepts](#block-level-vs-inline-elements-concepts)  
- 块级元素与内联元素：概念
- [Placement Rules and Nesting](#placement-rules-and-nesting)  
- 布局与嵌套规则
- [`<div>` and `<span>`: Non-semantic Hooks](#div-and-span-non-semantic-hooks)  
- `<div>` 与 `<span>`：非语义挂钩
- [Font Units: Absolute vs Relative](#font-units-absolute-vs-relative)  
- 字体长度单位：绝对与相对
- [Font Size: `font-size` (px, em, rem, %)](#font-size-font-size-px-em-rem-)  
- 字号：`font-size`（px、em、rem、%）
- [Font Keywords and Weight](#font-keywords-and-weight)  
- 字号关键字与字重
- [Italic and Text Decoration](#italic-and-text-decoration)  
- 斜体与文本装饰
- [Font Families and Fallbacks](#font-families-and-fallbacks)  
- 字体族与回退链
- [Line Height and Readability](#line-height-and-readability)  
- 行高与可读性
- [Shorthand `font` Property](#shorthand-font-property)  
- `font` 速写属性
- [Web Image Formats (JPEG/GIF/PNG)](#web-image-formats-jpeggifpng)  
- Web 常用图像格式（JPEG/GIF/PNG）
- [`<img>` Tag: `src`, `alt`, and Paths](#img-tag-src-alt-and-paths)  
- `<img>` 标签：`src`、`alt` 与路径
- [Sizing Images with CSS: `width`/`height`](#sizing-images-with-css-widthheight)  
- 用 CSS 控制图像尺寸：`width`/`height`
- [Borders on Images](#borders-on-images)  
- 图像边框
- [Vertical Alignment with Text](#vertical-alignment-with-text)  
- 与文本的垂直对齐
- [Text Wrapping with `float` and `clear`](#text-wrapping-with-float-and-clear)  
- 使用 `float` 与 `clear` 的文字环绕
- [Background Images: Repeat and Attachment](#background-images-repeat-and-attachment)  
- 背景图像：平铺与固定

---

## Block-level vs Inline Elements: Concepts  
## 块级元素与内联元素：概念

- **Block-level elements** form a **rectangular block**, typically starting on a **new line** and expanding to fill the **available width**.  
- **块级元素**表示一个**矩形块**，通常**独占一行**并横向**尽可能占满**。  
- Common block elements: headings **`<h1>…<h6>`**, **`<p>`**, lists **`<ul>/<ol>`**, tables **`<table>`**.  
- 常见块级元素：标题 **`<h1>…<h6>`**、**`<p>`**、列表 **`<ul>/<ol>`**、表格 **`<table>`**。  
- **Inline elements** flow **within a line** and **do not** cause line breaks before/after by default.  
- **内联元素**在**行内流动**，默认**不会**在前后产生换行。  
- Common inline elements: links **`<a>`**, emphasis **`<strong>` / `<em>`**.  
- 常见内联元素：链接 **`<a>`**、强调 **`<strong>` / `<em>`**。  
- **Note (HTML5)**: the traditional block/inline dichotomy is **less strict**, but still useful for **authoring rules**.  
- **提示（HTML5）**：现代规范对块/内联的界定**不再刚性**，但依旧有助于**理解书写规则**。  

---

## Placement Rules and Nesting  
## 布局与嵌套规则

- A **block-level** element may **contain** other **block** or **inline** elements.  
- **块级元素**内部可以**包含**其他**块级**或**内联**元素。  
- An **inline** element may contain **text** and **other inline elements**, **not** block elements.  
- **内联元素**内部可以包含**文本**与**其它内联元素**，但**不能**包含块级元素。  

**Correct / 正确**  
```html
<p>在段落中嵌入 <strong>内联元素</strong> 是可以的。</p>
```

**Incorrect / 错误**  
```html
<strong>在内联元素里放入<p>块级元素</p>是不允许的。</strong>
```

---

## `<div>` and `<span>`: Non-semantic Hooks  
## `<div>` 与 `<span>`：非语义挂钩

- **`<div>`** is a **block-level** generic container; **`<span>`** is an **inline** generic container.  
- **`<div>`** 是**块级**通用容器；**`<span>`** 是**内联**通用容器。  
- They have **no intrinsic semantic meaning**; use them to attach **CSS selectors** to specific ranges.  
- 二者**无语义含义**，常用于为特定范围**挂接 CSS 选择器**。  

**Example / 示例**  
```html
<div>
  <h1>国内旅行</h1>
  <h2>京都</h2>
  <span>世界遗产</span>がたくさんあります。
  <h2>沖縄</h2>
  沖縄といえばやはり<span>青い海</span>ですね。
  <h2>北海道</h2>
  <span>海鮮丼</span>がおいしいです。
</div>
```

```css
div  { color: #124; }   /* 深蓝 / dark blue */
span { color: #c00; }   /* 红色 / red */
```

---

## Font Units: Absolute vs Relative  
## 字体长度单位：绝对与相对

- **Absolute units**: `in`, `cm`, `mm`, `pt`, `pc`, `px` (≈ device pixels; hi‑DPI may abstract).  
- **绝对单位**：`in`、`cm`、`mm`、`pt`、`pc`、`px`（≈ 设备像素；高分屏会抽象化）。  
- **Relative units**: `%`, `em`, `ex`, `rem`, `vh`, `vw`.  
- **相对单位**：`%`、`em`、`ex`、`rem`、`vh`、`vw`。  
- Prefer **relative units** for responsive text; reserve **px** for **precise tweaks**.  
- **响应式文本**优先用**相对单位**；**px**仅用于**必要的精细控制**。  

---

## Font Size: `font-size` (px, em, rem, %)  
## 字号：`font-size`（px、em、rem、%）

- Browser default text size is commonly **16px**; omitted `font-size` falls back to default.  
- 浏览器默认字号通常为 **16px**；未指定时回退到默认值。  
- `em`: relative to the **current element’s** font size; `rem`: relative to **`html` root** font size.  
- `em`：相对**当前元素**字号；`rem`：相对 **`html` 根**字号。  
- `%`: percentage of the **parent** size.  
- `%`：相对**父元素**字号的百分比。  

**Example / 示例**  
```css
html { font-size: 16px; }
body { font-size: 1.25rem; }     /* 20px */
p    { font-size: 1.2em; }       /* 相对 body：24px */
.small { font-size: 90%; }       /* 相对父元素：0.9× */
```

---

## Font Keywords and Weight  
## 字号关键字与字重

- Size **keywords**: `xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`; relative: `smaller`, `larger`.  
- 字号**关键字**：`xx-small`、`x-small`、`small`、`medium`、`large`、`x-large`、`xx-large`；相对关键字：`smaller`、`larger`。  
- **Weight** with `font-weight`: numeric **100–900** (400=normal, 700=bold) or keywords `normal`, `bold`, `lighter`, `bolder`.  
- **字重**用 `font-weight`：数值 **100–900**（400=常规，700=加粗）或关键字 `normal`、`bold`、`lighter`、`bolder`。  
- Some fonts **do not provide** all weights; the browser may **simulate**.  
- 某些字体**不含**所有字重，浏览器可能**模拟**粗细。  

---

## Italic and Text Decoration  
## 斜体与文本装饰

- `font-style`: `normal`, `italic`, `oblique`.  
- `font-style`：`normal`、`italic`、`oblique`。  
- `text-decoration`: `none`, `underline`, `overline`, `line-through`, etc.  
- `text-decoration`：`none`、`underline`、`overline`、`line-through` 等。  

---

## Font Families and Fallbacks  
## 字体族与回退链

- Choose with `font-family`: **generic families** `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, or **specific fonts**.  
- 用 `font-family` 选择字体：**通用族** `serif`、`sans-serif`、`monospace`、`cursive`、`fantasy`，或**具体字体**。  
- Provide a **comma‑separated fallback list**; **quote** names with spaces.  
- 提供**逗号分隔**的**回退链**；字体名含空格需**加引号**。  

**Example / 示例**  
```css
body { font-family: "MS Pゴシック", Arial, Helvetica, sans-serif; }
```

---

## Line Height and Readability  
## 行高与可读性

- Set with `line-height`: numbers **multiply** current size (e.g., `1.5` ≈ **150%**), or explicit units (`em`, `%`, `px`).  
- 使用 `line-height`：纯数字表示**倍数**（如 `1.5`≈**150%**），也可用带单位的值（`em`、`%`、`px`）。  
- Typical reading lines: **1.4–1.8**; adjust per font and size.  
- 常见可读行高：**1.4–1.8**；按字体与字号微调。  

**Example / 示例**  
```css
h1 { font-size: 50px; line-height: 1.6em; }  /* 1 行高约 80px */
```

---

## Shorthand `font` Property  
## `font` 速写属性

- Syntax: `font: <style> <weight> <size>/<line-height> <family>;` (`size` and `family` are **required**).  
- 语法：`font: <style> <weight> <size>/<line-height> <family>;`（必须提供 **size** 与 **family**）。  
- Order of `style` and `weight` is **interchangeable**.  
- `style` 与 `weight` 的顺序可**互换**。  

**Example / 示例**  
```css
p { font: bold italic 1.1em/1.5 serif; }
```

---

## Web Image Formats (JPEG/GIF/PNG)  
## Web 常用图像格式（JPEG/GIF/PNG）

- **JPEG**: up to **24‑bit color**, **lossy compression**; good for **photos**.  
- **JPEG**：支持 **24 位色**，**有损压缩**；适合**照片**。  
- **GIF**: up to **256 colors**, supports **transparency** and simple **animation**; good for **logos/icons**.  
- **GIF**：最多 **256 色**，支持**透明**与简单**动画**；适合**标志/图标**。  
- **PNG**: web‑oriented, **lossless compression**, high color depth; usually **smaller than GIF** for same content.  
- **PNG**：面向 Web，**无损压缩**、高色深；同内容通常比 **GIF** **更小**。  

---

## `<img>` Tag: `src`, `alt`, and Paths  
## `<img>` 标签：`src`、`alt` 与路径

- Use **`src`** for the **relative path** to the image; provide **`alt`** for accessibility and fallback text.  
- 通过 **`src`** 指定图像的**相对路径**；提供 **`alt`** 以便无障碍与回退显示。  

```html
<h2>京都</h2>
<img src="img/kinkakuji.jpg" alt="金閣寺">
<span>世界遗产</span>がたくさんあります。
```

- If an image **does not show**, re‑check **filename** and **path**; avoid **full‑width characters**; don’t hardcode **absolute paths**.  
- 若图像**未显示**，请检查**文件名**与**路径**；避免**全角字符**；不要硬编码**绝对路径**。  

---

## Sizing Images with CSS: `width`/`height`  
## 用 CSS 控制图像尺寸：`width`/`height`

- Set size via **CSS**: in **pixels** or **percentages**.  
- 使用 **CSS** 指定尺寸：单位可为**像素**或**百分比**。  
- If you set **only one** of `width`/`height`, the **other dimension auto‑scales** to keep **aspect ratio**.  
- 当仅设置 `width` 或 `height` 之一时，**另一边会自适应**，以保持**纵横比**。  
- Setting **both** to fixed values may **distort**.  
- 同时固定两者可能导致**拉伸变形**。  

---

## Borders on Images  
## 图像边框

- Use `border` to style a **frame** around images: e.g., `border: 3px solid gold;`.  
- 使用 `border` 为图像添加**边框**：如 `border: 3px solid gold;`。  
- When an image is a **link**, some browsers historically **showed a border**; ensure `border: none;` if undesired.  
- 当图像被设置为**链接**时，历史上部分浏览器会**显示边框**；不需要时可设 `border: none;`。  

---

## Vertical Alignment with Text  
## 与文本的垂直对齐

- Inline images align with text **baseline** by default; adjust with `vertical-align`: `top`, `middle`, `bottom` (default), etc.  
- 行内图片默认与文本的**基线**对齐；可用 `vertical-align` 调整为 `top`、`middle`、`bottom`（默认）等。  

---

## Text Wrapping with `float` and `clear`  
## 使用 `float` 与 `clear` 的文字环绕

- `float: left|right` lets text **wrap around** the image; subsequent elements flow beside it.  
- 使用 `float: left|right` 可让文本**环绕**图像，后续元素会并排流动。  
- Cancel wrapping with `clear: left|right|both` on a **following block**.  
- 在**后续块级元素**上用 `clear: left|right|both` 以**解除环绕**。  

**Example / 示例**  
```html
<img src="img/photo.jpg" class="float-left" alt="…">
<h2 class="float-clear">沖縄</h2>
```
```css
.float-left  { float: left;  margin: 0 12px 8px 0; }
.float-clear { clear: both; }
```

---

## Background Images: Repeat and Attachment  
## 背景图像：平铺与固定

- Set with `background-image: url("path")`; control tiling via `background-repeat`: `no-repeat`, `repeat`, `repeat-x`, `repeat-y`.  
- 使用 `background-image: url("路径")`；通过 `background-repeat` 控制平铺：`no-repeat`、`repeat`、`repeat-x`、`repeat-y`。  
- Keep backgrounds fixed during scroll with `background-attachment: fixed`.  
- 用 `background-attachment: fixed` 让背景在滚动时**固定不动**。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture03.md) · [Next Lecture / 下一讲 →](./lecture05.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

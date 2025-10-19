[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 08: CSS Box Model, Display (Block/Inline), and Positioning  
# 第08讲：CSS 盒模型、显示类型（块/内联）与定位

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Box Model: Concept & Parts](#box-model-concept--parts)  
- 盒模型：概念与组成
- [Padding: Syntax & Shorthands](#padding-syntax--shorthands)  
- 内边距：语法与速记
- [Border: Styles & Usage](#border-styles--usage)  
- 边框：样式与使用
- [Margin: Syntax/Auto/Centers](#margin-syntaxautocenters)  
- 外边距：语法/auto/居中
- [Box Size (`width`/`height`) & Overflow](#box-size-widthheight--overflow)  
- 盒子尺寸（`width`/`height`）与溢出处理
- [Display: Block vs Inline vs Inline-block](#display-block-vs-inline-vs-inline-block)  
- 显示类型：块、内联与内联块
- [Block vs Inline Behavior Recap](#block-vs-inline-behavior-recap)  
- 块与内联行为回顾
- [Positioning: static / relative / absolute / fixed](#positioning-static--relative--absolute--fixed)  
- 定位：static / relative / absolute / fixed
- [Z-index: Stacking Order](#z-index-stacking-order)  
- 层叠顺序（z-index）
- [Quick Practice](#quick-practice)  
- 快速练习

---

## Box Model: Concept & Parts  
## 盒模型：概念与组成

- A **box** is the **rectangular area** each element occupies.  
- **盒子（box）**是每个元素所占据的**矩形区域**。  
- It consists of **Content**, **Padding**, **Border**, and **Margin**.  
- 它由 **内容（Content）**、**内边距（Padding）**、**边框（Border）**与**外边距（Margin）**构成。  

```
+------------------------------+
|          Margin              |  （外边距，不着色）
|  +------------------------+  |
|  |        Border          |  |  （边框）
|  |  +------------------+  |  |
|  |  |     Padding      |  |  |  （内边距）
|  |  |  +------------+  |  |  |
|  |  |  |  Content   |  |  |  |  （内容区，受 width/height 影响）
|  |  |  +------------+  |  |  |
|  |  +------------------+  |  |
|  +------------------------+  |
+------------------------------+
```

- **`width`/`height`** set the size of the **content box** (unless you use `box-sizing: border-box`).  
- **`width`/`height`** 默认设置的是**内容区**大小（除非使用 `box-sizing: border-box`）。  

---

## Padding: Syntax & Shorthands  
## 内边距：语法与速记

- Set with `padding` (unit or `%`); can target sides individually.  
- 使用 `padding`（可用单位或 `%`）；也可单独指定四边。  
- Longhand: `padding-top/right/bottom/left`.  
- 长写：`padding-top/right/bottom/left`。  
- Shorthand patterns:  
- 速记模式：  

```
padding: A;               /* 上右下左 全部为 A */
padding: A B;             /* 上下=A，左右=B */
padding: A B C;           /* 上=A，左右=B，下=C */
padding: A B C D;         /* 上=A，右=B，下=C，左=D（顺时针）*/
```

**Example / 示例**  
```css
.box { padding: 1em 2em 3em; }  /* 上1em, 左右2em, 下3em */
```

---

## Border: Styles & Usage  
## 边框：样式与使用

- Use `border: <width> <style> <color>;` on elements to draw borders.  
- 使用 `border: <宽度> <样式> <颜色>;` 绘制边框。  
- Common styles: `solid`, `double`, `dotted`, `dashed`, `groove`, `ridge`, `inset`, `outset`.  
- 常见样式：`solid`、`double`、`dotted`、`dashed`、`groove`、`ridge`、`inset`、`outset`。  

```css
h1, p { border: 1px solid #333; }
```

---

## Margin: Syntax/Auto/Centers  
## 外边距：语法/auto/居中

- Longhand & shorthands mirror **padding** (including **clockwise order**).  
- 长写与速记与 **padding** 相同（含**顺时针**规则）。  
- `margin: 0;` removes element margins (unit omitted for **zero**).  
- `margin: 0;` 可去除元素外边距（**0** 可省略单位）。  
- **Horizontal centering** of a fixed-width block: `margin-left: auto; margin-right: auto;`.  
- **固定宽度块**的**水平居中**：左右 `margin` 设为 **`auto`**。  
- To remove the default gap to the viewport, also set `body { margin: 0; }`.  
- 若要移除页面与视口的默认空白，还应设置 `body { margin: 0; }`。  

```css
.box1 { margin: 60px 0 60px auto; }   /* 示例，仅演示写法 */
.centered { width: 600px; margin: 60px auto; }
body { margin: 0; }
```

---

## Box Size (`width`/`height`) & Overflow  
## 盒子尺寸（`width`/`height`）与溢出处理

- Set box size via `width`/`height`.  
- 使用 `width`/`height` 指定盒子尺寸。  
- When content **doesn’t fit**, different UAs may expand or **overflow**. Control with `overflow`.  
- 当内容**放不下**时，不同浏览器可能扩展或**溢出**；用 `overflow` 控制：  

```css
.box { width: 320px; height: 120px; overflow: auto; /* or scroll/hidden */ }
```

- Multiple classes can be applied by **space-separated names** in `class`.  
- 一个元素可通过在 `class` 中**空格分隔**来应用多个类。  

---

## Display: Block vs Inline vs Inline-block  
## 显示类型：块、内联与内联块

- **Block** elements stack **vertically**, can set **`width`/`height`** and all margins/paddings.  
- **块级**元素**纵向**排列，可设置 **`width`/`height`** 及上下左右 `margin/padding`。  
- **Inline** elements flow **horizontally**, **cannot** set `width/height` (generally) nor vertical margins.  
- **内联**元素**横向**排布，通常**不能**设置 `width/height`，也**不能**设置上下外边距。  
- **Inline-block** keeps **inline flow** but allows **`width/height`** and vertical margins.  
- **内联块（inline-block）**保持**行内**排列，同时可设置 **`width/height`** 与上下外边距。  

```css
.disp { background: #124; color: #fff; }
p.disp { width: 100%; height: 80px; }      /* 块：尺寸生效 */
a.disp { display: inline-block; width: 160px; height: 40px; } /* 内联块：尺寸生效 */
```

---

## Block vs Inline Behavior Recap  
## 块与内联行为回顾

- **Blocks** take full **available width** by default; **inlines** take **content width** and wrap at the edge.  
- **块级**默认占满**可用宽度**；**内联**仅占**内容宽度**，到行末**换行**。  

---

## Positioning: static / relative / absolute / fixed  
## 定位：static / relative / absolute / fixed

- `position: static` — default flow; **`top/right/bottom/left` don’t apply**, **no `z-index`**.  
- `position: static`——默认文档流；**四向偏移无效**，**不能用 `z-index`**。  
- `position: relative` — offset **relative to its normal position**; supports `top/right/bottom/left` and `z-index`.  
- `position: relative`——相对**自身常规位置**偏移；可用四向偏移与 `z-index`。  
- `position: absolute` — positioned **relative to the nearest non-static ancestor**, otherwise the **viewport**.  
- `position: absolute`——**相对最近的非 static 祖先**定位；若无，则相对**视口**。  
- `position: fixed` — like absolute but **fixed on screen during scroll**.  
- `position: fixed`——类似 absolute，但在滚动时**位置固定**。  

```css
.static   { position: static; }
.rel1     { position: relative; top: 20px; left: 80px; }
.abs1     { position: absolute; top: 120px; right: 0; }
.fixedBR  { position: fixed; right: 12px; bottom: 12px; }
```

**Absolute ancestor rule / 绝对定位参考系规则**  
- Move an absolutely positioned element **inside a `position: relative` parent** to use that parent’s **top-left** as origin.  
- 将绝对定位元素**移入 `position: relative` 的父元素**，其参考原点就会变为父元素的**左上角**。  

---

## Z-index: Stacking Order  
## 层叠顺序（z-index）

- Larger **`z-index`** is painted **on top** (among positioned elements).  
- **`z-index`** 越大，元素越**靠上**（就定位元素之间）。  
- Without `z-index`, later elements **paint over earlier ones**.  
- 未指定 `z-index` 时，**后出现**的元素会覆盖**先出现**的元素。  

```css
.relative1 { position: relative; z-index: 10; }
.relative2 { position: relative; z-index: 5;  }  /* relative1 将在 relative2 之上 */
```

---

## Quick Practice  
## 快速练习

1) **Padding practice** — apply `padding: 1em 2em 3em;` and observe content offset.  
1) **内边距练习**——应用 `padding: 1em 2em 3em;` 观察内容位移。  
2) **Centering** — give a fixed width and set `margin: 60px auto;`.  
2) **居中**——设定固定宽度后设置 `margin: 60px auto;`。  
3) **Inline to block** — switch `a` from `inline` to `block`/`inline-block` and test `width/height`.  
3) **内联转块**——将 `a` 从 `inline` 改为 `block`/`inline-block` 测试 `width/height`。  
4) **Absolute vs fixed** — create a badge in the bottom-right with `position: fixed;`.  
4) **绝对 vs 固定**——用 `position: fixed;` 在右下角放置徽章。  

---

[← Previous Lecture / 上一讲](./lecture07.md) · [Next Lecture / 下一讲 →](./lecture09.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

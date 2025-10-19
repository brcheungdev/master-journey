[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 06: HTML Tables, Cell Merging, and Calendar/Timetable Tasks  
# 第06讲：HTML 表格、单元格合并与日历/时间表练习

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Table Elements Overview](#table-elements-overview)  
- 表格元素总览
- [Minimal Structure: `table` / `tr` / `td` / `th`](#minimal-structure-table--tr--td--th)  
- 基本结构：`table` / `tr` / `td` / `th`
- [Borders with CSS: `border` and Types](#borders-with-css-border-and-types)  
- CSS 边框：`border` 与类型
- [Merging Adjacent Borders: `border-collapse`](#merging-adjacent-borders-border-collapse)  
- 合并相邻边框：`border-collapse`
- [Add Columns and Rows](#add-columns-and-rows)  
- 新增列与行
- [Table Size: `width` / `height` and `table-layout`](#table-size-width--height-and-table-layout)  
- 表格尺寸：`width` / `height` 与 `table-layout`
- [Per-row/column Sizing via Classes](#per-rowcolumn-sizing-via-classes)  
- 通过类选择器设置行/列尺寸
- [Text Alignment in Cells](#text-alignment-in-cells)  
- 单元格文字对齐
- [Font Size within Tables](#font-size-within-tables)  
- 表格内字体大小
- [Horizontal/Vertical Merging: `colspan` / `rowspan`](#horizontalvertical-merging-colspan--rowspan)  
- 横向/纵向合并：`colspan` / `rowspan`
- [Backgrounds: Color and Images](#backgrounds-color-and-images)  
- 背景：颜色与图片
- [Table Caption and Position](#table-caption-and-position)  
- 表格标题与位置
- [Exercise 6‑1: Build a Monthly Calendar](#exercise-6-1-build-a-monthly-calendar)  
- 练习 6‑1：制作当月日历
- [Exercise 6‑2: Build Your Timetable](#exercise-6-2-build-your-timetable)  
- 练习 6‑2：制作本学期时间表
- [Common Rules](#common-rules)  
- 共通规则

---

## Table Elements Overview  
## 表格元素总览

- A table is built by combining **`<table>`**, **`<tr>`**, **`<td>`**, and **`<th>`**.  
- 表格由 **`<table>`**、**`<tr>`**、**`<td>`** 与 **`<th>`** 组合构成。  
- **`<table>`** wraps the whole grid; **`<tr>`** makes a **row**; **`<td>`** makes a **cell**; **`<th>`** is a **header cell**.  
- **`<table>`** 包裹整个网格；**`<tr>`** 定义**行**；**`<td>`** 定义**单元格**；**`<th>`** 为**表头单元格**。  

---

## Minimal Structure: `table` / `tr` / `td` / `th`  
## 基本结构：`table` / `tr` / `td` / `th`

```html
<table>
  <tr> <!-- row 行 -->
    <th>A</th><th>B</th><th>C</th> <!-- header cells 表头 -->
  </tr>
  <tr>
    <td>a1</td><td>a2</td><td>a3</td> <!-- data cells 数据单元格 -->
  </tr>
</table>
```

- Keep **the same number of cells** in each row.  
- 各行中**单元格数量需一致**。  

---

## Borders with CSS: `border` and Types  
## CSS 边框：`border` 与类型

- Apply borders on **`td, th`** (and optionally `table`).  
- 在 **`td, th`**（必要时包括 `table`）上添加边框。  
- Shorthand: `border: <width> <style> <color>;`.  
- 速记：`border: <宽度> <样式> <颜色>;`。  

```css
td, th { border: 1px solid blue; }   /* width, style, color */
```

- Common styles: `solid`, `double`, `groove`, `ridge`, `inset`, `outset`, `dotted`, `dashed`.  
- 常见样式：`solid`、`double`、`groove`、`ridge`、`inset`、`outset`、`dotted`、`dashed`。  

---

## Merging Adjacent Borders: `border-collapse`  
## 合并相邻边框：`border-collapse`

- On **`table`**, set `border-collapse: collapse;` to **merge** adjacent cell borders (default is `separate`).  
- 在 **`table`** 上设置 `border-collapse: collapse;` 可**合并相邻边框**（默认 `separate`）。  

```css
table { border-collapse: collapse; }
```

---

## Add Columns and Rows  
## 新增列与行

- To add a **column**, add **`<th>` / `<td>`** in **each row**.  
- 新增**列**：在**每一行**中都添加 **`<th>` / `<td>`**。  
- To add a **row**, add another **`<tr>`** with matching number of cells.  
- 新增**行**：增加一个 **`<tr>`**，并保持单元格数一致。  

---

## Table Size: `width` / `height` and `table-layout`  
## 表格尺寸：`width` / `height` 与 `table-layout`

- By default, columns **auto-size** to their content (`table-layout: auto`).  
- 默认列宽随内容**自动调整**（`table-layout: auto`）。  
- Use `table-layout: fixed;` to **equalize column widths**.  
- 设置 `table-layout: fixed;` 可**均匀分配列宽**。  
- You can set table size with **`width`**/`height` on `table`.  
- 可在 `table` 上设置 **`width`**/`height` 指定整体尺寸。  

```css
table { width: 600px; table-layout: fixed; }
```

---

## Per-row/column Sizing via Classes  
## 通过类选择器设置行/列尺寸

- Assign **class names** to `tr`/`td` and style them.  
- 给 `tr`/`td` 添加**类名**并设置样式。  

```html
<tr class="h50">...</tr>
```
```css
.h50 { height: 50px; } /* set row height 行高50px */
```

---

## Text Alignment in Cells  
## 单元格文字对齐

- **Horizontal** with `text-align`: `left` (default), `center`, `right`.  
- **水平对齐**用 `text-align`：`left`（默认）、`center`、`right`。  
- **Vertical** with `vertical-align`: `top`, `middle` (default), `bottom`.  
- **垂直对齐**用 `vertical-align`：`top`、`middle`（默认）、`bottom`。  
- These apply to **`tr` / `td` / `th`**.  
- 以上属性可用于 **`tr` / `td` / `th`**。  

---

## Font Size within Tables  
## 表格内字体大小

- Set base size on `table` via `font-size`; override per row/column/cell with classes.  
- 在 `table` 上用 `font-size` 设定基准；需个别调整时用类在行/列/单元格上覆盖。  

---

## Horizontal/Vertical Merging: `colspan` / `rowspan`  
## 横向/纵向合并：`colspan` / `rowspan`

- **Horizontal** merge with **`colspan="N"`** on `td/th`.  
- **横向合并**：在 `td/th` 上设置 **`colspan="N"`**。  
- **Vertical** merge with **`rowspan="N"`** on `td/th`.  
- **纵向合并**：在 `td/th` 上设置 **`rowspan="N"`**。  

```html
<tr>
  <td colspan="3">Merged across 3 cols / 横向合并3列</td>
</tr>
<tr>
  <td rowspan="2">Merged 2 rows / 纵向合并2行</td>
  <td>R1C2</td><td>R1C3</td>
</tr>
<tr>
  <td>R2C2</td><td>R2C3</td> <!-- cell under rowspan omitted 被合并处省略 -->
</tr>
```

- When using `rowspan`, **omit** the covered cells in subsequent rows.  
- 使用 `rowspan` 时，后续行中被覆盖的单元格**应省略**。  

---

## Backgrounds: Color and Images  
## 背景：颜色与图片

- You can set **`background-color`** or **`background-image`** on `table`, `tr`, `td`, `th`.  
- 可在 `table`、`tr`、`td`、`th` 上设置 **`background-color`** 或 **`background-image`**。  
- For specific cells, assign a **class or id** and style it.  
- 若仅针对特定单元格，使用 **class/id** 单独指定样式。  

---

## Table Caption and Position  
## 表格标题与位置

- Use **`<caption>`** to add a table title.  
- 使用 **`<caption>`** 添加表格标题。  
- Control placement via **`caption-side`**: `top`, `bottom`; `left/right` exist but are **unsupported in Chrome/IE**.  
- 通过 **`caption-side`** 控制位置：`top`、`bottom`；`left/right` 存在但 **Chrome/IE 不支持**。  

---

## Exercise 6‑1: Build a Monthly Calendar  
## 练习 6‑1：制作当月日历

- Create a **calendar** for the **month mapped by your student ID’s last digit** (see table below).  
- 根据**学籍号末尾数字**制作对应**月份**的日历（见下表）。  
- **Include Japanese public holidays** (参考 **`https://uic.jp/calendar/`**).  
- **标注日本法定节假日**（参考 **`https://uic.jp/calendar/`**）。  
- **Filename**: `task06a.html`.  
- **文件名**：`task06a.html`。  
- **CSS** must be written **inside `<style>` within `<head>`**.  
- **CSS** 必须写在 **`<head>` 内 `<style>`** 中。  
- Required styles (**must-have**):  
- 必选样式（**必须设置**）：  
  1) **Caption** (e.g., “2023年10月”)  
  1) **标题 caption**（如“2023年10月”）  
  2) **Saturdays in blue**, **Sundays & holidays in red**  
  2) **周六蓝色**，**周日/节假日红色**  
  3) **Merge empty cells** (no-date cells) and give them a **background color**  
  3) **合并无日期单元格**并设置**背景色**  
  4) Put the **month name in the first cell**  
  4) 在**首个单元格**写入**月份**  
- Example month mapping / 示例映射：  

```
ID last digit → Calendar month / 学籍号末尾 → 月份
1 → 2023-02
2 → 2023-03
3 → 2023-04
4 → 2023-05
5 → 2023-06
6 → 2023-07
7 → 2022-10
8 → 2022-11
9 → 2022-12
0 → 2023-01
```

**Starter skeleton / 起步骨架**  
```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Calendar</title>
<style>
  table { border-collapse: collapse; table-layout: fixed; width: 700px; }
  td, th { border: 1px solid #333; width: 100px; height: 60px; text-align: right; padding: 4px; }
  caption { caption-side: top; font-weight: bold; margin-bottom: 8px; }
  .sat { color: blue; }  /* Saturday 周六 */
  .sun, .holiday { color: red; } /* Sunday & holidays 周日与节假日 */
  .empty { background: #f5f5f5; } /* merged empty cells 合并空白 */
</style>
</head>
<body>
  <table>
    <caption>2023年10月</caption>
    <tr><th>日</th><th>月</th><th>火</th><th>水</th><th>木</th><th>金</th><th>土</th></tr>
    <!-- rows & cells go here 此处填写日期与样式 -->
  </table>
</body>
</html>
```

---

## Exercise 6‑2: Build Your Timetable  
## 练习 6‑2：制作本学期时间表

- Build your **weekly timetable** with **period & time horizontally**, **weekdays vertically**.  
- 制作**每周时间表**：**横向显示时限与时间**，**纵向显示星期**。  
- **Merge cells** for **two-period continuous classes** (`rowspan` or `colspan` as appropriate).  
- 对**连续两节**的课程**合并单元格**（`rowspan`/`colspan` 视布局决定）。  
- If you have **no continuous 2‑period classes**, treat **“Web Programming I”** as a **2‑period** block.  
- 若**没有连续两节**课程，则将**“Web Programming I”**按**两节连上**处理。  
- **Color‑code** practicals vs lecture‑only classes.  
- 对**含实习**与**纯讲授**的课程**使用不同颜色**标注。  
- **CSS** must be in `<head><style>…</style></head>`.  
- **CSS** 必须写在 `<head><style>…</style></head>` 中。  
- **Filename**: `task06b.html`.  
- **文件名**：`task06b.html`。  

**Starter skeleton / 起步骨架**  
```html
<table class="timetable">
  <tr>
    <th>曜日\時限</th><th>1</th><th>2</th><th>3</th><th>4</th>
  </tr>
  <tr>
    <th>月</th>
    <td class="lecture">科目A</td>
    <td class="practical" colspan="2">科目B（演習）</td>
    <td class="lecture">科目C</td>
  </tr>
  <!-- more rows 此处补充其它星期 -->
</table>
<style>
  .timetable { border-collapse: collapse; table-layout: fixed; width: 100%; }
  .timetable th, .timetable td { border: 1px solid #999; text-align: center; padding: 6px; }
  .lecture   { background: #eef7ff; }
  .practical { background: #fff7e6; }
</style>
```

---


## Common Rules  
## 共通规则

- **Use ASCII file names**: **no full‑width characters** and **no spaces**.  
- **文件命名用 ASCII**：**不得使用全角字符**、**不得含空格**。  
- `<title>` must **reflect the page content**.  
- `<title>` 必须**准确反映页面内容**。  
- Submit **only the files you actually use**; keep **folder structure intact** to avoid broken links.  
- **只提交使用中的文件**；保持**目录结构**以避免链接失效。  
- **Remove unused CSS** from submission.  
- **删除未使用的 CSS**。  
- Use **HTML5 + CSS only** (no CSS frameworks, no JavaScript).  
- 仅使用 **HTML5 + CSS**（禁止 CSS 框架与 JavaScript）。  
- Must **work in Google Chrome**.  
- 必须确保在 **Google Chrome** 中运行正常。  


---

[← Previous Lecture / 上一讲](./lecture05.md) · [Next Lecture / 下一讲 →](./lecture07.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 05: Lists (ul/ol), Description Lists (dl/dt/dd), and Blockquote  
# 第05讲：列表（ul/ol）、说明列表（dl/dt/dd）与引用（blockquote）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Overview: Why Lists?](#overview-why-lists)  
- 概览：为什么使用列表？
- [Unordered Lists (`ul` + `li`)](#unordered-lists-ul--li)  
- 无序列表（`ul` + `li`）
- [Marker Styles with CSS (`list-style-type` for `ul`)](#marker-styles-with-css-list-style-type-for-ul)  
- CSS 指定无序列表标记（`list-style-type`）
- [Ordered Lists (`ol` + `li`)](#ordered-lists-ol--li)  
- 有序列表（`ol` + `li`）
- [`start` Attribute: Custom Start Number](#start-attribute-custom-start-number)  
- `start` 属性：自定义起始编号
- [Number Styles with CSS (`list-style-type` for `ol`)](#number-styles-with-css-list-style-type-for-ol)  
- CSS 指定有序列表编号（`list-style-type`）
- [Using Images as Markers (`list-style-image`)](#using-images-as-markers-list-style-image)  
- 使用图像作为标记（`list-style-image`）
- [Nested Lists: Correct Structure](#nested-lists-correct-structure)  
- 列表嵌套：正确结构
- [Common Pitfall: Invalid Nesting](#common-pitfall-invalid-nesting)  
- 常见误区：错误的嵌套
- [Only `li` as Children of `ul/ol`](#only-li-as-children-of-ulol)  
- 仅 `li` 可作为 `ul/ol` 的子元素
- [Description Lists (`dl`/`dt`/`dd`)](#description-lists-dldtdd)  
- 说明列表（`dl`/`dt`/`dd`）
- [Blockquote and Cite](#blockquote-and-cite)  
- 引用与引用源

---

## Overview: Why Lists?  
## 概览：为什么使用列表？

- Lists **organize related items** into a clear, scannable structure.  
- 列表能够将**相关条目**组织为**清晰、易扫读**的结构。  
- Choose **unordered** lists when **order doesn’t matter**, and **ordered** lists when **sequence matters**.  
- 当**顺序无关紧要**用**无序列表**；当**先后有意义**用**有序列表**。  

---

## Unordered Lists (`ul` + `li`)  
## 无序列表（`ul` + `li`）

- Use `<ul> ... </ul>` to wrap the list, with each item in `<li> ... </li>`.  
- 使用 `<ul> ... </ul>` 包裹列表；每个条目写在 `<li> ... </li>` 中。  

```html
<h2>Ingredients</h2>
<ul>
  <li>Onion</li>
  <li>Potato</li>
  <li>Carrot</li>
</ul>
```

- Browsers automatically render a **marker (bullet)** before each item.  
- 浏览器会在每个条目前自动渲染一个**标记（圆点）**。  

---

## Marker Styles with CSS (`list-style-type` for `ul`)  
## CSS 指定无序列表标记（`list-style-type`）

- Control bullet style with **`list-style-type`** on `ul` or `li`.  
- 在 `ul` 或 `li` 上通过 **`list-style-type`** 控制圆点样式。  

```
disc (default) / 默认 ●
circle / 圈 ○
square / 方 ■
none / 无标记
```

```css
ul { list-style-type: square; }   /* ■ */
```

---

## Ordered Lists (`ol` + `li`)  
## 有序列表（`ol` + `li`）

- Use `<ol> ... </ol>` with `<li>` items to indicate **meaningful order**.  
- 使用 `<ol> ... </ol>` 与 `<li>` 条目，表示**顺序有意义**。  

```html
<h2>Steps</h2>
<ol>
  <li>Prep ingredients</li>
  <li>Heat oil</li>
  <li>Stir-fry</li>
</ol>
```

---

## `start` Attribute: Custom Start Number  
## `start` 属性：自定义起始编号

- On `ol`, use **`start="x"`** to begin numbering at **any integer** (even **0** or **negative**).  
- 在 `ol` 上使用 **`start="x"`** 将编号从**任意整数**开始（包括 **0** 或**负数**）。  

```html
<ol start="-2">
  <li>First shown as -2</li>
  <li>-1</li>
  <li>0</li>
</ol>
```

---

## Number Styles with CSS (`list-style-type` for `ol`)  
## CSS 指定有序列表编号（`list-style-type`）

- For `ol`, `list-style-type` controls **numbering style**.  
- 对于 `ol`，`list-style-type` 控制**编号样式**。  

```
decimal        → 1, 2, 3, …
lower-alpha    → a, b, c, …
upper-alpha    → A, B, C, …
lower-roman    → i, ii, iii, …
upper-roman    → I, II, III, …
hiragana       → あ, い, う, …
katakana       → ア, イ, ウ, …
```

```css
ol { list-style-type: upper-roman; }  /* I, II, III, … */
```

---

## Using Images as Markers (`list-style-image`)  
## 使用图像作为标记（`list-style-image`）

- Replace the default marker with an **image** using `list-style-image`.  
- 使用 `list-style-image` 将默认标记替换为**图像**。  

```css
ul { list-style-image: url("img/bullet.png"); }
```

- The value is a **`url()`** path to the image file.  
- 该属性值使用 **`url()`** 指向图像文件路径。  

---

## Nested Lists: Correct Structure  
## 列表嵌套：正确结构

- Nest a list **inside an `li`**, not as a sibling.  
- **嵌套列表**必须写在**上层 `li` 的内部**，而不是作为其同级元素。  

```html
<ul>
  <li>Level 1
    <ul>
      <li>Level 2</li>
      <li>Level 2</li>
    </ul>
  </li>
  <li>Level 1</li>
</ul>
```

- Default browser markers by depth: typically **● → ○ → ■** for the first three levels; **3rd level and deeper** may all be **■**.  
- 浏览器默认的深度标记通常为前三级 **● → ○ → ■**；**第三级及更深**可能都显示为 **■**。  

---

## Common Pitfall: Invalid Nesting  
## 常见误区：错误的嵌套

- **Incorrect**: placing a second-level `ul` **as a sibling** of `li`.  
- **错误示例**：把二级 `ul` 放在 `li` 的**同级**。  

```html
<!-- ✗ Incorrect -->
<ul>
  <li>Level 1</li>
</ul>
<ul>  <!-- Wrong: sibling list instead of child of li -->
  <li>Level 2</li>
</ul>
```

- Always keep deeper lists **inside** their parent `li`.  
- 正确写法是将更深层级的列表**置于父级 `li` 内部**。  

---

## Only `li` as Children of `ul/ol`  
## 仅 `li` 可作为 `ul/ol` 的子元素

- The **only valid child** of `ul`/`ol` is **`li`**.  
- `ul`/`ol` 的**唯一合法子元素**是 **`li`**。  
- If you need images, paragraphs, or links, **put them inside `li`**.  
- 如需图像、段落或链接，请**放入 `li` 内部**。  

```html
<ul>
  <li><img src="img/curry.jpg" alt="Curry"> Photo of curry</li>
  <li><a href="recipe.html">Recipe</a></li>
</ul>
```

---

## Description Lists (`dl`/`dt`/`dd`)  
## 说明列表（`dl`/`dt`/`dd`）

- Use **`<dl>`** for a **set of terms and descriptions** (glossaries, dictionaries).  
- 使用 **`<dl>`** 表示一组**术语与说明**（如词汇表、字典）。  
- **`<dt>`** marks the **term**; **`<dd>`** provides its **definition/description**.  
- **`<dt>`** 表示**术语**；**`<dd>`** 表示其**定义/说明**。  

```html
<dl>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets. Controls presentation.</dd>
  <dt>HTML</dt>
  <dd>HyperText Markup Language. Defines structure.</dd>
</dl>
```

---

## Blockquote and Cite  
## 引用与引用源

- Use **`<blockquote>`** to quote **extracts from works** (books, web pages, etc.).  
- 使用 **`<blockquote>`** 引用**作品内容**（书籍、网页等）。  
- Add **`cite="URL"`** on `<blockquote>` to indicate the **source**.  
- 在 `<blockquote>` 上通过 **`cite="URL"`** 指明**引用来源**。  

```html
<blockquote cite="https://www.example.com/article">
  “Programs must be written for people to read, and only incidentally for machines to execute.”
</blockquote>
```

- **Note**: The **`<cite>`** tag is used for **titles of works** (book, song, movie, painting, play, opera), **not** for quoting long passages.  
- **注意**：**`<cite>`** 用于**作品标题**（书、歌、电影、绘画、戏剧、歌剧等），**不是**用于长段文本引用。  

---

[← Previous Lecture / 上一讲](./lecture04.md) · [Next Lecture / 下一讲 →](./lecture06.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

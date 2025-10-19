[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 07: HTML Forms — Inputs, Labels, Select, Buttons, and HTML5 Types  
# 第07讲：HTML 表单——输入框、标签、选择菜单、按钮与 HTML5 新类型

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What is a Form](#what-is-a-form)  
- 表单是什么
- [`<form>`: Action, Method, Enctype](#form-action-method-enctype)  
- `<form>`：action、method、enctype
- [Single‑line Text Input (`type="text"`)](#singleline-text-input-type-text)  
- 单行文本输入（`type="text"`）
- [Password Input (`type="password"`)](#password-input-type-password)  
- 密码输入（`type="password"`）
- [Radio Buttons (Single Choice)](#radio-buttons-single-choice)  
- 单选按钮（单项选择）
- [Labels for Controls (`<label>`)](#labels-for-controls-label)  
- 控件标签（`<label>`）
- [Select Menu & Options](#select-menu--options)  
- 下拉选择菜单与选项
- [Submit & Reset Buttons (`input`)](#submit--reset-buttons-input)  
- 提交与重置按钮（`input`）
- [Multiple Selection (`multiple`, `size`)](#multiple-selection-multiple-size)  
- 多项选择（`multiple`、`size`）
- [Checkboxes (Multi‑select)](#checkboxes-multiselect)  
- 复选框（多选）
- [Textarea (Multi‑line Input)](#textarea-multiline-input)  
- 多行文本输入（`textarea`）
- [Buttons via `<button>` + CSS States](#buttons-via-button--css-states)  
- 使用 `<button>` 与 CSS 状态
- [Buttons with Images](#buttons-with-images)  
- 使用图片按钮
- [Link Pseudo‑classes Recap (LVHA)](#link-pseudoclasses-recap-lvha)  
- 链接伪类回顾（LVHA 顺序）
- [HTML5 Input Types (Catalog)](#html5-input-types-catalog)  
- HTML5 新增输入类型（目录）
- [Date Input (`type="date"`)](#date-input-type-date)  
- 日期输入（`type="date"`）
- [Quick Checklist](#quick-checklist)  
- 快速清单



---

## What is a Form  
## 表单是什么

- A **form** lets users **enter data** and **send** it to a **server**. Typical controls: text boxes, checkboxes, etc.  
- **表单**用于让用户**输入数据**并**发送**到**服务器**。常见控件：文本框、复选框等。  
- Used for **contact forms**, **search boxes**, and more.  
- 常用于**联系表单**、**搜索框**等场景。  

---

## `<form>`: Action, Method, Enctype  
## `<form>`：action、method、enctype

- Wrap controls with **`<form> ... </form>`** to make the section **submittable**.  
- 使用 **`<form> ... </form>`** 包裹控件以形成**可提交**的区域。  
- **`action`** — URL or **mailto:** where data is sent (server‑side script like **PHP/CGI**).  
- **`action`**——数据发送到的 **URL** 或 **mailto:**（如 **PHP/CGI** 等服务端脚本）。  
- **`method`** — `post` (large payload, body only) or `get` (default; appends data to URL after `?`).  
- **`method`**——`post`（可传较大数据、放请求体）或 `get`（默认；数据附在 URL `?` 之后）。  
- **`enctype`** — for `post`: `application/x-www-form-urlencoded` (default), `multipart/form-data` (file upload), `text/plain` (mail).  
- **`enctype`**——配合 `post` 使用：`application/x-www-form-urlencoded`（默认）、`multipart/form-data`（文件上传）、`text/plain`（邮件）。  

**Example / 示例**  
```html
<form action="/submit" method="post" enctype="application/x-www-form-urlencoded">
  ...
</form>
```

---

## Single‑line Text Input (`type="text"`)  
## 单行文本输入（`type="text"`）

- Use `<input type="text">`; key attributes: **`name`**, `size`, `maxlength`, `value`, `placeholder`.  
- 使用 `<input type="text">`；关键属性：**`name`**、`size`、`maxlength`、`value`、`placeholder`。  

```html
<input type="text" name="username" size="20" maxlength="30" placeholder="Your name">
```

---

## Password Input (`type="password"`)  
## 密码输入（`type="password"`）

- Use `<input type="password">`; similar attributes as text; characters display as **●/**\***.  
- 使用 `<input type="password">`；与文本相似；输入会显示为 **●/**\***。  

```html
<input type="password" name="pwd" maxlength="20">
```

---

## Radio Buttons (Single Choice)  
## 单选按钮（单项选择）

- Use `<input type="radio">`; **group by the same `name`** so only **one** can be selected per group.  
- 使用 `<input type="radio">`；通过**相同的 `name`** 形成**互斥组**。  
- Use `value` to submit the selected option; `checked` sets default.  
- 用 `value` 提交选择项；`checked` 指定默认选中。  

```html
<label><input type="radio" name="gender" value="m" checked> Male</label>
<label><input type="radio" name="gender" value="f"> Female</label>
```

---

## Labels for Controls (`<label>`)  
## 控件标签（`<label>`）

- Wrap input with `<label> ... </label>` or link via `for="id"` to make **text clickable**.  
- 使用 `<label> ... </label>` 包裹或通过 `for="id"` 关联，使**文字可点击**。  

```html
<label for="agree">I agree</label>
<input id="agree" type="checkbox" name="agree">
```

---

## Select Menu & Options  
## 下拉选择菜单与选项

- Use `<select name="...">` with nested `<option value="...">` items; `selected` marks default.  
- 使用 `<select name="...">` 并在其中写 `<option value="...">`；`selected` 指定默认项。  

```html
<select name="pref">
  <option value="kyoto">Kyoto</option>
  <option value="osaka" selected>Osaka</option>
</select>
```

---

## Submit & Reset Buttons (`input`)  
## 提交与重置按钮（`input`）

- Submit: `<input type="submit" name="send" value="Send">`  
- 提交：`<input type="submit" name="send" value="Send">`  
- Reset: `<input type="reset" value="Reset">`  
- 重置：`<input type="reset" value="Reset">`  

---

## Multiple Selection (`multiple`, `size`)  
## 多项选择（`multiple`、`size`）

- On `<select>`, add **`multiple`** to allow **multi‑select**; users hold **Shift/Ctrl** to select multiple; `size` sets visible rows.  
- 在 `<select>` 上加 **`multiple`** 以启用**多选**；用户可用 **Shift/Ctrl** 多选；`size` 设置可见行数。  

```html
<select name="fruits" multiple size="4">
  <option>Apple</option><option>Banana</option>
  <option>Cherry</option><option>Date</option>
</select>
```

---

## Checkboxes (Multi‑select)  
## 复选框（多选）

- Use `<input type="checkbox">`; use the **same `name`** for a group; each option needs a `value`; `checked` sets default.  
- 使用 `<input type="checkbox">`；同组使用**相同 `name`**；每项有 `value`；`checked` 为默认。  

```html
<label><input type="checkbox" name="hobby" value="music" checked> Music</label>
<label><input type="checkbox" name="hobby" value="sports"> Sports</label>
```

---

## Textarea (Multi‑line Input)  
## 多行文本输入（`textarea`）

- Use `<textarea name="..." rows="..." cols="...">`; **`rows` is required**; `placeholder` for hint text.  
- 使用 `<textarea name="..." rows="..." cols="...">`；**`rows` 必填**；`placeholder` 用于提示。  

```html
<textarea name="message" rows="5" cols="30" placeholder="Your message"></textarea>
```

---

## Buttons via `<button>` + CSS States  
## 使用 `<button>` 与 CSS 状态

- You can use `<button type="submit">` / `<button type="reset">` with **custom CSS** for hover/active effects.  
- 可用 `<button type="submit">` / `<button type="reset">`，并通过 **CSS** 定制悬停/激活效果。  

```html
<button type="submit" class="btn1">Send</button>
<button type="reset"  class="btn1">Reset</button>
```
```css
.btn1 { padding: 8px 14px; border: 1px solid #444; background: #eee; color: #222; }
.btn1:hover { background: #444; color: #fff; cursor: pointer; }
```

---

## Buttons with Images  
## 使用图片按钮

- You can style `<button>` with **background images**, or use `<input type="image">`; remove unwanted borders via CSS.  
- 可给 `<button>` 使用**背景图**，或使用 `<input type="image">`；如出现不需要的边框，用 CSS 去除。  

```html
<input type="image" src="img/send.png" alt="Send">
```
```css
input[type="image"] { border: none; }
```

---

## Link Pseudo‑classes Recap (LVHA)  
## 链接伪类回顾（LVHA 顺序）

- `:link` (unvisited) → `:visited` (visited) → `:hover` (hover) → `:active` (active).  
- `:link`（未访问）→ `:visited`（已访问）→ `:hover`（悬停）→ `:active`（按下）。  

```css
a:link{...} a:visited{...} a:hover{...} a:active{...}
```

---

## HTML5 Input Types (Catalog)  
## HTML5 新增输入类型（目录）

- `search`, `tel`, `url`, `email`, `datetime`, `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range`, `color`.  
- `search`、`tel`、`url`、`email`、`datetime`、`date`、`month`、`week`、`time`、`datetime-local`、`number`、`range`、`color`。  

---

## Date Input (`type="date"`)  
## 日期输入（`type="date"`）

- Use `<input type="date" name="..." value="YYYY-MM-DD">`; the format is **`yyyy-mm-dd`**.  
- 使用 `<input type="date" name="..." value="YYYY-MM-DD">`；取值格式为 **`yyyy-mm-dd`**。  

---

## Quick Checklist  
## 快速清单

- Wrap inputs in a **`<form>`** and set **`action`**, **`method`**, **(for POST) `enctype`**.  
- **所有输入控件**置于 **`<form>`** 内，并设置 **`action`**、**`method`**，以及（POST 时）**`enctype`**。  
- Group radios/checkboxes with the **same `name`**; always provide **`value`**.  
- **单选/复选**使用**相同 `name`** 分组；务必提供 **`value`**。  
- Use **`label`** for clickable text; use **`selected`/`checked`** for defaults.  
- 使用 **`label`** 提升可用性；用 **`selected`/`checked`** 设置默认项。  
- For multi‑select `<select>`, add **`multiple`** and set **`size`**.  
- 多选 `<select>` 需添加 **`multiple`** 并设置 **`size`**。  
- Prefer `<button>` when you need **richer styling and states**.  
- 需要**更丰富样式/状态**时优先使用 `<button>`。  
- Review **HTML5 input types** for semantic and mobile‑friendly inputs.  
- 善用 **HTML5 输入类型**，提升语义性与移动端体验。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture06.md) · [Next Lecture / 下一讲 →](./lecture08.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

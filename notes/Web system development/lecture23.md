[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 23: DOM Form Controls — Radio, Checkbox, Select (Single/Multiple) & Common Events  
# 第23讲：DOM 表单控件 —— 单选、复选、选择列表（单/多选）与常用事件

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [In‑Page I/O (Part 2) Overview](#inpage-io-part-2-overview)  
- 页面内输入输出（第二部分）概览
- [Radio Buttons: Single Selection](#radio-buttons-single-selection)  
- 单选按钮：单项选择
- [`querySelector` vs `querySelectorAll`](#queryselector-vs-queryselectorall)  
- `querySelector` 与 `querySelectorAll`
- [Checkboxes: Multiple Selection](#checkboxes-multiple-selection)  
- 复选框：多项选择
- [Select Box: Single Selection](#select-box-single-selection)  
- 选择框：单选
- [Select Box: Multiple Selection](#select-box-multiple-selection)  
- 选择框：多选
- [Events: `input`, `change`, `click`, `mouseover`, `mouseout`](#events-input-change-click-mouseover-mouseout)  
- 事件：`input`、`change`、`click`、`mouseover`、`mouseout`
- [Practice: hover area (mouseover/mouseout)](#practice-hover-area-mouseovermouseout)  
- 练习：悬停区域（mouseover/mouseout）
- [Task 10 (Exercises & Submission)](#task-10-exercises--submission)  
- 第10回练习与提交
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## In‑Page I/O (Part 2) Overview  
## 页面内输入输出（第二部分）概览

- This lecture continues **DOM I/O** with more **form controls** and **events**: radio, checkbox, select (single/multiple), and typical events.  
- 本讲继续学习 **DOM 输入输出**，覆盖更多**表单控件**与**事件**：单选、复选、选择列表（单/多选）以及常见事件。  

---

## Radio Buttons: Single Selection  
## 单选按钮：单项选择

- **Group by `name`** so that **only one** is selectable within the group; the chosen value is the **`value` attribute**.  
- 通过 **`name` 分组**，组内**仅能单选**；被选中项的值来自其 **`value` 属性**。  
- To read the selection, iterate the **NodeList** and check **`.checked`**.  
- 读取选择时，遍历 **NodeList** 并判断 **`.checked`**。  

```html
<div id="radio">
  <label><input type="radio" name="city" value="KYOTO">Kyoto</label>
  <label><input type="radio" name="city" value="TOKYO">Tokyo</label>
  <label><input type="radio" name="city" value="SAPPORO">Sapporo</label>
</div>
<p id="r-out">-</p>
<button id="r-btn">Show</button>

<script>
  document.querySelector("#r-btn").addEventListener("click", () => {
    const ops = document.querySelectorAll("#radio input[type='radio']");
    let result = "";
    for (let i = 0; i < ops.length; i++) {
      if (ops[i].checked) { result = ops[i].value; break; }
    }
    document.querySelector("#r-out").textContent = result || "(none)";
  });
</script>
```

---

## `querySelector` vs `querySelectorAll`  
## `querySelector` 与 `querySelectorAll`

- **`querySelector(sel)`** gets the **first match**; **`querySelectorAll(sel)`** gets **all matches** as a **NodeList**.  
- **`querySelector(sel)`** 取得**首个匹配**；**`querySelectorAll(sel)`** 取得**全部匹配**并返回 **NodeList**。  
- A **NodeList** can be **indexed** (`list[i]`) and has **`.length`** similar to arrays.  
- **NodeList** 可按**下标访问**（`list[i]`）并具有 **`.length`**，使用方式与数组相似。  

---

## Checkboxes: Multiple Selection  
## 复选框：多项选择

- **Multiple choices** allowed within the same **`name`** group; read selected items via **`.checked`** and **push** values into an **array**.  
- 同一 **`name`** 分组内允许**多选**；通过 **`.checked`** 判断并将选中的 **`value`** **push** 到**数组**。  

```html
<div id="checkbox">
  <label><input type="checkbox" name="DB" value="MySQL">MySQL</label>
  <label><input type="checkbox" name="DB" value="PostgreSQL">PostgreSQL</label>
  <label><input type="checkbox" name="DB" value="SQLite">SQLite</label>
</div>
<pre id="c-out">-</pre>
<button id="c-btn">Show</button>

<script>
  document.querySelector("#c-btn").addEventListener("click", () => {
    const ops = document.querySelectorAll("#checkbox input[type='checkbox']");
    const result = [];
    for (let i = 0; i < ops.length; i++) {
      if (ops[i].checked) result.push(ops[i].value);
    }
    document.querySelector("#c-out").textContent = result.join(", ");
  });
</script>
```

---

## Select Box: Single Selection  
## 选择框：单选

- The **selected option’s `value`** is exposed via the **`select.value`** property.  
- 选中项的 **`value`** 可直接通过 **`select.value`** 获取。  

```html
<select id="sel1">
  <option value="A">A</option>
  <option value="B">B</option>
  <option value="C">C</option>
</select>
<span id="s1-out">-</span>
<button id="s1-btn">Show</button>
<script>
  s1-btn.addEventListener("click", () => {  // or query by id
    document.querySelector("#s1-out").textContent =
      document.querySelector("#sel1").value;
  });
</script>
```

---

## Select Box: Multiple Selection  
## 选择框：多选

- Add the **`multiple`** attribute; enumerate **`select.options`** and collect those with **`option.selected === true`**.  
- 给 `select` 添加 **`multiple`** 属性；遍历 **`select.options`** 并收集 **`option.selected === true`** 的条目。  

```html
<select id="sel2" multiple size="3">
  <option value="r">Red</option>
  <option value="g">Green</option>
  <option value="b">Blue</option>
</select>
<pre id="s2-out">-</pre>
<button id="s2-btn">Show</button>
<script>
  document.querySelector("#s2-btn").addEventListener("click", () => {
    const sel = document.querySelector("#sel2");
    const result = [];
    const ops = sel.options;
    for (let i = 0; i < ops.length; i++) {
      if (ops[i].selected) result.push(ops[i].value);
    }
    document.querySelector("#s2-out").textContent = result.join(", ");
  });
</script>
```

> Tip: The **single‑select** case can also be handled by the **same `options`/`selected` loop**, which will have exactly one selected option.  
> 提示：**单选**场景也可以用同样的 **`options`/`selected`** 循环处理，因为会有且仅有一个被选中。  

---

## Events: `input`, `change`, `click`, `mouseover`, `mouseout`  
## 事件：`input`、`change`、`click`、`mouseover`、`mouseout`

- **`input`**: fires when the **value changes live** (e.g., typing, dragging a range slider).  
- **`input`**：当值**实时变化**时触发（如输入文本、拖动滑块）。  
- **`change`**: fires when the **change is committed** (e.g., leaving a field, selecting a radio/checkbox/select).  
- **`change`**：当**变更被确认**时触发（如离开输入框、选择单/复选/下拉）。  
- **`click`**: mouse click; **`mouseover`/`mouseout`**: pointer **enter/leave** an element.  
- **`click`**：鼠标点击；**`mouseover`/`mouseout`**：指针**进入/离开**元素时触发。  

```html
<select id="sel3">
  <option value="A">A</option><option value="B">B</option>
</select>
<span id="s3-out">-</span>
<script>
  const s3 = document.querySelector("#sel3");
  s3.addEventListener("change", () => { document.querySelector("#s3-out").textContent = s3.value; });
</script>
```

---

## Practice: hover area (mouseover/mouseout)  
## 练习：悬停区域（mouseover/mouseout）

```html
<style>
  #area { width:240px; height:120px; background:#eee; border:1px solid #aaa; }
</style>
<div id="area"></div>
<script>
  const area = document.querySelector("#area");
  area.addEventListener("mouseover", () => { area.style.backgroundColor = "orange"; });
  area.addEventListener("mouseout",  () => { area.style.backgroundColor = "#eee"; });
</script>
```

---

## Task 10 (Exercises & Submission)  
## 第10回练习与提交

- **10‑1**: Place **7 input controls** (text, textarea, range, radio, checkbox, select‑single, select‑multiple). Add **7 buttons**; each button shows the **currently entered/selected value** next to it.  
- **10‑1**：摆放**7 种输入部件**（文本、文本域、滑块、单选、复选、选择单选、选择多选）。为每个添加**按钮**，点击后在旁边显示**当前值**。  
- **10‑2**: **Remove buttons**; use **events** for **immediate updates** — `input` for **text/textarea/range**, `change` for **radio/checkbox/select**.  
- **10‑2**：**删除按钮**；改为使用**事件**实现**即显**——**文本/文本域/滑块**用 `input`，**单/复选与选择**用 `change`。  
- **10‑3**: **Factor** the 7 handlers into **3 reusable functions**: (1) `value`‑based controls, (2) radio/checkbox groups, (3) select single/multiple.  
- **10‑3**：将 7 个处理整合为 **3 个可复用函数**：（1）基于 `value` 的控件，（2）单选/复选分组，（3）选择框单/多选。 

---

## Quick Checklist  
## 快速清单

- Radio/checkbox: loop **NodeList** and inspect **`.checked`**; push selected values.  
- 单/复选：遍历 **NodeList** 检查 **`.checked`**；将被选值 push 到数组。  
- Select single: read **`select.value`**; select multiple: loop **`select.options`** and test **`.selected`**.  
- 选择单选：读 **`select.value`**；选择多选：遍历 **`select.options`** 并检测 **`.selected`**。  
- Choose events: **`input`** for live changes, **`change`** for committed changes; `mouseover`/`mouseout` for hover UI.  
- 事件选择：**`input`** 用于实时变更，**`change`** 用于确认后变更；悬停 UI 用 `mouseover`/`mouseout`。  
- Prefer **`addEventListener`** and keep **HTML/JS separated**.  
- 推荐使用 **`addEventListener`**，保持 **HTML/JS 分离**。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture22.md) · [Next Lecture / 下一讲 →](./lecture24.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

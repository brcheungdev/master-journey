[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 24: CSS Transitions, Transforms, `classList`, and the Event Object  
# 第24讲：CSS 过渡（transition）、变形（transform）、`classList` 与事件对象

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Why Animations on Web Pages](#why-animations-on-web-pages)  
- 为什么在网页中使用动画
- [CSS `transition` Property: Syntax & Defaults](#css-transition-property-syntax--defaults)  
- CSS `transition` 属性：语法与默认值
- [Transition Demo: Pure CSS vs Triggered by JavaScript](#transition-demo-pure-css-vs-triggered-by-javascript)  
- 过渡演示：纯 CSS 与由 JavaScript 触发
- [Separate Style from JS: Using `classList` (`add/remove/toggle/contains`)](#separate-style-from-js-using-classlist-addremovetogglecontains)  
- 样式与脚本分离：使用 `classList`（`add/remove/toggle/contains`）
- [CSS3 `transform`: translate/scale/rotate/skew & `transform-origin`](#css3-transform-translatescalerotateskew--transform-origin)  
- CSS3 `transform`：移动/缩放/旋转/斜切 与 `transform-origin`
- [Transform + Transition Example](#transform--transition-example)  
- 变形结合过渡示例
- [Event Object: `event.target` and Friends](#event-object-eventtarget-and-friends)  
- 事件对象：`event.target` 及相关属性
- [Task 11 Exercises](#task-11-exercises)  
- 第11回练习
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Why Animations on Web Pages  
## 为什么在网页中使用动画

- Static pages can benefit from **subtle motion** to draw attention and communicate state changes.  
- 网页通常是**静态**的，恰当的**动态效果**能吸引注意并表达状态变化。  

---

## CSS `transition` Property: Syntax & Defaults  
## CSS `transition` 属性：语法与默认值

```
transition: <property> <duration> <timing-function> <delay>;
```
- Example: `transition: width 2.5s linear 1s;` (can list **multiple properties** separated by commas).  
- 示例：`transition: width 2.5s linear 1s;`（可用**逗号**指定**多个属性**）。  
- Parts: **property** to animate (e.g., `width`), **duration** (e.g., `2.5s`), **timing-function** (`linear/ease/ease-in/ease-out/...`), **delay** (`1s`).  
- 构成：要变化的**属性**（如 `width`）、**持续时间**（如 `2.5s`）、**时间函数**（`linear/ease/ease-in/ease-out/...`）、**延迟**（`1s`）。  
- **Defaults** when omitted: **`all 0s ease 0s`**.  
- 省略时的**默认值**是 **`all 0s ease 0s`**。  

---

## Transition Demo: Pure CSS vs Triggered by JavaScript  
## 过渡演示：纯 CSS 与由 JavaScript 触发

- **Pure CSS**: hover a box to smoothly change background color over **3s**.  
- **纯 CSS**：悬停方块，背景色在 **3s** 内平滑变化。  

```html
<style>
.box { width:120px; height:80px; border:2px solid #09f; transition: background-color 3s; }
.box:hover { background-color:#000; }
</style>
<div class="box"></div>
```

- **JS‑triggered**: without `transition`, the change is **instant**; adding `transition` makes it **animate** when the **event** changes the target value.  
- **JS 触发**：没有 `transition` 时变化是**瞬时**的；加上 `transition` 后，当**事件**改变目标值时会**动画过渡**。  

```html
<style>
#div2 { width:120px; height:80px; background:#eee; /* try with/without transition */ }
/* add to see animation: transition: background-color 3s; */
</style>
<div id="div2"></div>
<script>
  document.querySelector("#div2").addEventListener("click", () => {
    document.querySelector("#div2").style.backgroundColor = "#000";
  });
</script>
```

---

## Separate Style from JS: Using `classList` (`add/remove/toggle/contains`)  
## 样式与脚本分离：使用 `classList`（`add/remove/toggle/contains`）

- Prefer defining **target styles in CSS classes** and **only toggle class names** from JavaScript.  
- 推荐把**目标样式写在 CSS 类**中，JavaScript **只负责切换类名**。  

```html
<style>
.box2 { width:120px; height:80px; background:#eee; transition: background-color 3s, width 3s; }
.box2.animation1 { background:#000; width:200px; }
</style>
<div id="div3" class="box2"></div>
<script>
  const el = document.querySelector("#div3");
  // add/remove/toggle/contains
  el.addEventListener("click", () => el.classList.toggle("animation1"));
</script>
```

- Methods: `element.classList.**add**("a")`, `**remove**("a")`, `**toggle**("a")`, `**contains**("a")`.  
- 常用方法：`element.classList.**add**("a")`、`**remove**("a")`、`**toggle**("a")`、`**contains**("a")`。  

---

## CSS3 `transform`: translate/scale/rotate/skew & `transform-origin`  
## CSS3 `transform`：移动/缩放/旋转/斜切 与 `transform-origin`

- Instead of separately changing `left/top/width/height`, use **`transform`**:  
- 与其分别改 `left/top/width/height`，可使用 **`transform`**：  

```
transform:
  translate(X, Y);    /* move / 移动 */
  translateX(X); translateY(Y);
  scale(sx, sy);      /* scale / 缩放 */
  rotate(deg);        /* rotation / 旋转（单位 deg）*/
  skew(kx, ky);       /* skew / 斜切 */
```

- The **default origin** is the **element center**; set via **`transform-origin`** if needed.  
- **变形原点**默认在**元素中心**；可用 **`transform-origin`** 调整。  

---

## Transform + Transition Example  
## 变形结合过渡示例

```html
<style>
.demo { width:120px; height:120px; background:#69c; transition: transform .5s; }
.demo.on { transform: scale(.6, .6) rotate(360deg); }
</style>
<div id="anim" class="demo"></div>
<script>
  document.querySelector("#anim").addEventListener("click", (e) => {
    e.currentTarget.classList.toggle("on");
  });
</script>
```

---

## Event Object: `event.target` and Friends  
## 事件对象：`event.target` 及相关属性

- Event listeners receive an **event object** parameter (often named **`e`/`ev`/`event`**).  
- 事件监听器会收到一个**事件对象**参数（常命名为 **`e`/`ev`/`event`**）。  
- Inspect properties like **`event.target.id`**, **`event.target.className`**, **`event.target.tagName`**; you can also operate on **`event.target.classList`**.  
- 可查看 **`event.target.id`**、**`event.target.className`**、**`event.target.tagName`** 等；亦可操作 **`event.target.classList`**。  

```html
<ul id="list">
  <li>Kyoto</li><li>Tokyo</li><li>Sapporo</li><li>Nagoya</li>
</ul>
<script>
  document.querySelector("#list").addEventListener("click", (event) => {
    const t = event.target;
    console.log(t.id, t.className, t.tagName);
    t.classList.toggle("on");
  });
</script>
```

---

## Task 11 Exercises  
## 第11回练习

**11‑1 (Click on one `<li>`)**  
**11‑1（点击一个 `<li>`）**

- Clicking a single `<li>` **moves it 40px right** and **changes color** over **1s**; click again to **toggle back**. Use **`transform: translateX(40px)`** and **`classList.toggle`**.  
- 点击一个 `<li>`，在 **1s** 内**右移 40px** 并**变色**；再点恢复。使用 **`transform: translateX(40px)`** 与 **`classList.toggle`**。  

**11‑2 (Click on `<ul><li>×4</li></ul>`)**  
**11‑2（点击 `<ul>` 中的 4 个 `<li>`）**

- Use **`querySelectorAll`** + **`for`** to attach listeners to **each `<li>`**; same **1s** move/color toggle.  
- 通过 **`querySelectorAll`** + **`for`** 给**每个 `<li>`** 绑定监听；实现同样的 **1s** 右移与变色切换。  

**11‑3 (Hover on `<ul><li>×4</li></ul>`)**  
**11‑3（悬停 `<ul>` 的 4 个 `<li>`）**

- On **hover in/out**, animate each `<li>` in **1s** to **right 40px + color change**, and **revert** when mouse leaves.  
- 鼠标**进入/离开**时，分别在 **1s** 内**右移 40px + 变色**，离开时**复原**。  

**11‑4 (Accordion with `<dl><dt><dd>…`)**  
**11‑4（`<dl><dt><dd>` 折叠面板）**

- Initially **only `<dt>` visible**. Clicking a `<dt>` reveals the **immediately following `<dd>`** in **1s** (set **`max-height: 0 → 400px`** and **`opacity: 0 → 1`**), and **hides** on re‑click; set a **delay of 0.5s**.  
- 初始**只显示 `<dt>`**。点击某个 `<dt>`，其**紧随的 `<dd>`** 在 **1s** 内显示（设置 **`max-height: 0 → 400px`** 与 **`opacity: 0 → 1`**），再次点击则**隐藏**；使用 **0.5s 延迟**。  


---

## Quick Checklist  
## 快速清单

- For **smooth changes**, set **`transition`** on the element **before** changing its target properties.  
- 若要平滑变化，应**先**在元素上设置 **`transition`** 再改变目标属性。  
- Prefer **CSS classes + `classList.toggle`** to separate **style** from **behavior**.  
- 推荐用 **CSS 类 + `classList.toggle`** 实现**样式**与**行为**分离。  
- Use **`transform`** for moving/scaling/rotating/skewing; **degrees** use `deg`.  
- 元素的**移动/缩放/旋转/斜切**优先用 **`transform`**；**角度**单位为 `deg`。  
- **Event object** gives you **`target`** info; you can manipulate **`event.target.classList`** directly.  
- **事件对象**提供 **`target`** 信息；可直接操作 **`event.target.classList`**。  

---

## Notes
## 注释

<details><summary>Multiple transitions / 多个过渡的书写</summary>

- Separate multiple transition items with **commas**: `transition: width 2s, height 2s;`.  
- 多个过渡用**逗号**分隔：`transition: width 2s, height 2s;`。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture23.md) · [Next Lecture / 下一讲 →](./lecture25.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

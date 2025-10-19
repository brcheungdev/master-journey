[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 25: Canvas Drawing & Animation — `<canvas>`, 2D Context, Rectangles/Paths/Arcs, and Timers  
# 第25讲：Canvas 绘制与动画 —— `<canvas>`、2D 上下文、矩形/路径/圆弧与定时器

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Is Canvas API](#what-is-canvas-api)  
- 什么是 Canvas API
- [Setup: `<canvas>` Element (HTML/CSS)](#setup-canvas-element-htmlcss)  
- 初始化：`<canvas>` 元素（HTML/CSS）
- [Get 2D Context (`getContext('2d')`)](#get-2d-context-getcontext2d)  
- 获取 2D 上下文（`getContext('2d')`）
- [Draw Rectangles: `strokeRect` / `fillRect`](#draw-rectangles-strokerect--fillrect)  
- 绘制矩形：`strokeRect` / `fillRect`
- [Paths & Lines: `beginPath` → `moveTo`/`lineTo` → `stroke`/`fill` → `closePath`](#paths--lines-beginpath--movetolinetoc-strokefill--closepath)  
- 路径与线段：`beginPath` → `moveTo`/`lineTo` → `stroke`/`fill` → `closePath`
- [Styles & Attributes (`strokeStyle`, `fillStyle`, `lineWidth`, etc.)](#styles--attributes-strokestyle-fillstyle-linewidth-etc)  
- 样式与属性（`strokeStyle`、`fillStyle`、`lineWidth` 等）
- [Draw Circles/Arcs: `arc(x, y, r, start, end)` (radians)](#draw-circlesarcs-arcx-y-r-start-end-radians)  
- 绘制圆/弧：`arc(x, y, r, start, end)`（弧度）
- [Clear Region: `clearRect`](#clear-region-clearrect)  
- 清除区域：`clearRect`
- [Animation Loop: Clear → Update → Draw → Repeat](#animation-loop-clear--update--draw--repeat)  
- 动画循环：清除 → 更新 → 绘制 → 重复
- [Timers: `setInterval` / `clearInterval` vs `setTimeout`](#timers-setinterval--clearinterval-vs-settimeout)  
- 定时器：`setInterval` / `clearInterval` 与 `setTimeout`
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## What Is Canvas API  
## 什么是 Canvas API

- **Canvas API** combines the HTML **`<canvas>`** element with **JavaScript** to draw **2D graphics**.  
- **Canvas API** 将 HTML **`<canvas>`** 元素与 **JavaScript** 结合，用于绘制 **2D 图形**。  fileciteturn24file0 fileciteturn24file1
- It was introduced with **HTML5**, requires **no plugins** (unlike Flash), and enables more complex motion than simple **CSS transitions**.  
- 自 **HTML5** 引入，**无需插件**（不同于 Flash），并能实现比 **CSS 过渡**更复杂的运动。  fileciteturn24file0

---

## Setup: `<canvas>` Element (HTML/CSS)  
## 初始化：`<canvas>` 元素（HTML/CSS）

```html
<style>
  canvas { border: 1px solid #999; } /* just to see the boundary / 边框便于观察 */
</style>
<canvas id="cv" width="640" height="480"></canvas>
```
- The `<canvas>` itself is a **rectangular drawing area**; set **`width`/`height`** and optionally a **border** for clarity.  
- `<canvas>` 本身是一个**矩形绘图区域**；请设定 **`width`/`height`**，并可用 **边框**便于观察。  fileciteturn24file1

---

## Get 2D Context (`getContext('2d')`)  
## 获取 2D 上下文（`getContext('2d')`）

```html
<script>
  const cv = document.querySelector("#cv");    // or: document.getElementById("cv")
  const gc = cv.getContext("2d");              // graphic context / 图形上下文
</script>
```
- First **query the DOM** for the canvas element, then call **`getContext('2d')`** to obtain the **graphics context**.  
- 先**获取 DOM** 的 canvas 元素，再调用 **`getContext('2d')`** 取得**图形上下文**。  fileciteturn24file1

---

## Draw Rectangles: `strokeRect` / `fillRect`  
## 绘制矩形：`strokeRect` / `fillRect`

```js
gc.lineWidth = 5;           // stroke width / 线宽
gc.strokeStyle = "blue";    // stroke color / 线色
gc.strokeRect(50, 50, 100, 100); // x,y,width,height

gc.fillStyle = "rgba(255,0,0,.5)";
gc.fillRect(200, 50, 120, 80);
```
- **`strokeRect(x, y, width, height)`** draws an **outlined** rectangle; **`fillRect(...)`** draws a **filled** rectangle.  
- **`strokeRect(x, y, width, height)`** 绘制**描边矩形**；**`fillRect(...)`** 绘制**填充矩形**。  fileciteturn24file1
- Adjust **`lineWidth`** and **`strokeStyle`** for border style; use **`fillStyle`** for fill color.  
- 用 **`lineWidth`** 与 **`strokeStyle`** 控制边线样式；用 **`fillStyle`** 控制填充颜色。  fileciteturn24file1

---

## Paths & Lines: `beginPath` → `moveTo`/`lineTo` → `stroke`/`fill` → `closePath`  
## 路径与线段：`beginPath` → `moveTo`/`lineTo` → `stroke`/`fill` → `closePath`

```js
gc.beginPath();          // reset path / 重置路径
gc.moveTo(40, 200);      // start / 起点
gc.lineTo(140, 260);     // polyline / 折线
gc.lineTo(240, 220);
gc.stroke();             // draw lines / 描边
gc.closePath();          // connect end to start / 闭合路径

gc.beginPath();
gc.moveTo(300, 200);
gc.lineTo(360, 260);
gc.lineTo(420, 200);
gc.fillStyle = "#0c8";
gc.fill();               // fill interior / 填充
```
- Use **`beginPath()`** then **`moveTo/lineTo`** to build a path; finalize with **`stroke()`** or **`fill()`**; **`closePath()`** joins end to start.  
- 先 **`beginPath()`**，再用 **`moveTo/lineTo`** 构建路径；以 **`stroke()`** 或 **`fill()`** 收尾；**`closePath()`** 可将终点与起点相连。  fileciteturn24file1

---

## Styles & Attributes (`strokeStyle`, `fillStyle`, `lineWidth`, etc.)  
## 样式与属性（`strokeStyle`、`fillStyle`、`lineWidth` 等）

- Common attributes: **`strokeStyle`**, **`fillStyle`**, **`globalAlpha`**, **`lineWidth`**, **`lineCap`**, **`lineJoin`**, **`shadowColor`**, **`font`**.  
- 常见属性：**`strokeStyle`**、**`fillStyle`**、**`globalAlpha`**、**`lineWidth`**、**`lineCap`**、**`lineJoin`**、**`shadowColor`**、**`font`**。  fileciteturn24file1
- Key methods: **`beginPath`**, **`moveTo`**, **`lineTo`**, **`stroke`**, **`fill`**, **`closePath`**, **`strokeRect`**, **`clearRect`**, **`arc`**.  
- 关键方法：**`beginPath`**、**`moveTo`**、**`lineTo`**、**`stroke`**、**`fill`**、**`closePath`**、**`strokeRect`**、**`clearRect`**、**`arc`**。  fileciteturn24file1

---

## Draw Circles/Arcs: `arc(x, y, r, start, end)` (radians)  
## 绘制圆/弧：`arc(x, y, r, start, end)`（弧度）

```js
gc.beginPath();
gc.lineWidth = 5;
gc.strokeStyle = "red";
gc.arc(340, 250, 40, 0, 2*Math.PI); // center (340,250), r=40, full circle
gc.stroke();
```
- **`arc(x, y, r, start, end)`** draws a circle/arc with center **`(x,y)`**, radius **`r`**, angles in **radians**.  
- **`arc(x, y, r, start, end)`** 以 **`(x,y)`** 为圆心，**`r`** 为半径，用**弧度**指明起止角绘制圆/弧。  fileciteturn24file0

---

## Clear Region: `clearRect`  
## 清除区域：`clearRect`

```js
// clear the whole canvas / 清空整个画布
gc.clearRect(0, 0, cv.width, cv.height);
```
- **`clearRect(x, y, w, h)`** clears a rectangular region (often **full canvas**) before redrawing.  
- **`clearRect(x, y, w, h)`** 清除矩形区域（常用于每帧**重绘前**清空整个画布）。  fileciteturn24file1

---

## Animation Loop: Clear → Update → Draw → Repeat  
## 动画循环：清除 → 更新 → 绘制 → 重复

```html
<button id="btn">開始/停止</button>
<canvas id="cv" width="640" height="480" style="border:1px solid #999"></canvas>
<script>
  const cv = document.querySelector("#cv");
  const gc = cv.getContext("2d");

  // (1) model / 数据对象
  const c = { x: 0, y: 0, r: 40 };   // 初始在左上角

  // (2) draw one frame / 绘制一帧
  function drawFrame(){
    gc.clearRect(0, 0, cv.width, cv.height); // 清空
    c.x += 1; c.y += 1;                      // 更新：右下移动
    gc.beginPath();                          // 绘制：圆
    gc.arc(c.x, c.y, c.r, 0, 2*Math.PI);
    gc.stroke();
  }

  // (3) timer loop toggle / 定时循环开关
  let timerId = null;
  document.querySelector("#btn").addEventListener("click", () => {
    if (timerId === null) {                  // start only once / 仅首次启动
      timerId = setInterval(drawFrame, 10);  // 注意：传函数名，不要写 drawFrame()
      btn.textContent = "停止";
    } else {
      clearInterval(timerId);
      timerId = null;
      btn.textContent = "開始";
    }
  });
</script>
```
- For animation: **(A)** clear with **`clearRect`** → **(B)** update object **state** → **(C)** draw new frame → **repeat** via a **timer**.  
- 动画要点：**(A)** 用 **`clearRect`** 清空 → **(B)** 更新对象**状态** → **(C)** 绘制新帧 → 通过**定时器**重复执行。  fileciteturn24file0 fileciteturn24file1
- Use a **model object** like `{x, y, r}` to store shape data; update positions each tick.  
- 用 `{x, y, r}` 这类**数据对象**存储图形；每次计时更新其位置。  fileciteturn24file0

---

## Timers: `setInterval` / `clearInterval` vs `setTimeout`  
## 定时器：`setInterval` / `clearInterval` 与 `setTimeout`

```js
const id = setInterval(drawFrame, 10); // repeat every 10ms / 每10ms重复
clearInterval(id);                     // stop / 终止

// Alternative: setTimeout recursion / 另一种方案：递归 setTimeout
function loop(){
  drawFrame();
  setTimeout(loop, 10);
}
```
- **`setInterval(fn, ms)`** calls **`fn` repeatedly** at approximately **`ms`** intervals; **store the id** to stop with **`clearInterval(id)`**.  
- **`setInterval(fn, ms)`** 以约 **`ms`** 的间隔**反复调用** `fn`；**保存返回的 id**，用 **`clearInterval(id)`** 停止。  fileciteturn24file0 fileciteturn24file1
- Passing **`drawFrame`** (not **`drawFrame()`**) avoids **immediate execution**.  
- 传入 **`drawFrame`**（而非 **`drawFrame()`**）可避免**立刻执行**。  fileciteturn24file0
- Slides note timing **drift** if a frame takes **longer than the interval**; **`setTimeout`** can be chained to avoid piling up.  
- 讲义指出：若**绘制耗时超过间隔**会产生**节奏漂移**；可以用**递归 `setTimeout`** 的方式来避免堆积。  fileciteturn24file0

---

## Practice Tasks  
## 练习任务

1) **Rectangles & Styles**: Draw two **`strokeRect`** with different **`lineWidth`/`strokeStyle`**, then a **`fillRect`** with **`fillStyle`**.  
1) **矩形与样式**：使用不同 **`lineWidth`/`strokeStyle`** 画两个 **`strokeRect`**，再配合 **`fillStyle`** 画一个 **`fillRect`**。  
2) **Path drawing**: `beginPath → moveTo/lineTo → stroke`; then replace `stroke` with `fill` and compare.  
2) **路径绘制**：`beginPath → moveTo/lineTo → stroke`；再改为 `fill` 比较差异。  
3) **Arc**: Draw a circle using **`arc(x, y, r, 0, 2*Math.PI)`** with **`lineWidth=5`** and **red stroke**.  
3) **圆弧**：用 **`arc(x, y, r, 0, 2*Math.PI)`** 绘制圆，**线宽 5**、**红色描边**。  
4) **Moving circle**: Implement the **clear→update→draw** loop; add a **Start/Stop** button that toggles a **single** timer.  
4) **移动的圆**：实现**清空→更新→绘制**循环；添加一个 **开始/停止** 按钮切换**单一**定时器。  
5) **(Optional)** Modify to move **right‑down then bounce**, or try **diagonal speed change**.  
5) **（可选）** 改为**右下移动并反弹**，或尝试**斜向速度变化**。  

---

## Quick Checklist  
## 快速清单

- Always **get context** via **`getContext('2d')`** before drawing.  
- 绘制前务必通过 **`getContext('2d')`** 获取上下文。  fileciteturn24file1
- Rectangles: **`strokeRect`** for border, **`fillRect`** for fill.  
- 矩形：边线用 **`strokeRect`**，填充用 **`fillRect`**。  fileciteturn24file1
- Paths: **`beginPath` → `moveTo/lineTo` → `stroke/fill` → `closePath`**.  
- 路径：**`beginPath` → `moveTo/lineTo` → `stroke/fill` → `closePath`**。  fileciteturn24file1
- Animation: **clear → update → draw → repeat**; manage **timer id** to **start once/stop cleanly**.  
- 动画：**清空 → 更新 → 绘制 → 重复**；管理**定时器 id**，**只启动一次/可干净停止**。  fileciteturn24file0
- Timers: choose between **`setInterval`** and **`setTimeout`**; beware of **drift** if frames are slow.  
- 定时器：选择 **`setInterval`** 或 **`setTimeout`**；若帧耗时过长会**产生漂移**。  fileciteturn24file0

---

## Notes 
## 注释

<details><summary>Coordinate system & angle units / 坐标系与角度单位</summary>

- Canvas coordinates start at the **top‑left** corner; **x increases right**, **y increases down**.  
- Canvas 坐标原点在**左上角**；**x 向右增**、**y 向下增**。  
- `arc` angles use **radians**; **full circle = `2π`**, **90° = `π/2`**.  
- `arc` 的角度使用**弧度**；**整圆 = `2π`**，**90° = `π/2`**。  
</details>

---

[← Previous Lecture / 上一讲](./lecture24.md) · [Next Lecture / 下一讲 →](./lecture26.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

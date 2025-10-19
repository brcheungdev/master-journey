[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 13: CSS Animations (Transitions/Keyframes), Transforms, and HTML5 Audio/Video  
# 第13讲：CSS 动画（过渡/关键帧）、变形与 HTML5 音频/视频

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [CSS Animations: When to Use](#css-animations-when-to-use)  
- CSS 动画：何时使用
- [Transitions: Concept & First Demo](#transitions-concept--first-demo)  
- 过渡（transition）：概念与首次演示
- [Transition Shorthand & Longhands](#transition-shorthand--longhands)  
- 过渡速记与长写属性
- [Timing Functions (ease/linear/ease-in/...)](#timing-functions-easelinearease-in)  
- 时间曲线（ease/linear/ease-in/…）
- [Transition Examples (`all` vs `width` only)](#transition-examples-all-vs-width-only)  
- 过渡示例（`all` 与仅 `width`）
- [Practice 1: Circle → Square on Hover](#practice-1-circle--square-on-hover)  
- 练习1：悬停时圆形变方形
- [Keyframe Animations: `@keyframes` & `animation` Props](#keyframe-animations-keyframes--animation-props)  
- 关键帧动画：`@keyframes` 与 `animation` 属性
- [Keyframe Examples: Color & Size Changes](#keyframe-examples-color--size-changes)  
- 关键帧示例：颜色与尺寸变化
- [Transforms: rotate/skew and with Animation](#transforms-rotateskew-and-with-animation)  
- 变形：旋转/倾斜与结合动画
- [HTML5 Audio: `autoplay` vs `controls`](#html5-audio-autoplay-vs-controls)  
- HTML5 音频：`autoplay` 与 `controls`
- [HTML5 Video & Fallback](#html5-video--fallback)  
- HTML5 视频与回退
- [Common Media Formats & Browser Support](#common-media-formats--browser-support)  
- 常见媒体格式与浏览器支持
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## CSS Animations: When to Use  
## CSS 动画：何时使用

- CSS can animate UI as a **decorative/presentational** feature via **Transitions** and **Animations**.  
- CSS 可通过 **Transitions（过渡）**与 **Animations（动画）**实现**装饰/呈现**层面的动效。  
- **Use CSS** for simple **one-shot** state changes (hover/focus/enter/leave).  
- **简单的一次性**状态切换（悬停/聚焦/进入/离开）优先使用 **CSS**。  
- **Use JS** when you need **start after click**, **pause/resume**, **reverse**, **complex physics-like effects**, etc.  
- 需要**点击后开始**、**暂停/恢复**、**反向播放**、**复杂物理效果**等时应采用 **JavaScript 动画**。  

---

## Transitions: Concept & First Demo  
## 过渡（transition）：概念与首次演示

- A **transition** animates **from current style to new style** over a **duration** when a property **changes**.  
- **过渡**在属性**发生变化**时，在指定**时长**内从**当前样式过渡到新样式**。  

```html
<!-- wp13-1.html (baseline) -->
<style>
div {
  width:200px; height:100px; text-align:center;
  background:#333; color:#fff; margin:10px;
}
div:hover { background:#6ba; width:400px; }
</style>
<div>(1) no transition – instant change</div>
<div>(2) will add transition with delay</div>
<div>(3) width transitions; color changes instantly</div>
```

---

## Transition Shorthand & Longhands  
## 过渡速记与长写属性

- Shorthand **`transition: <property> <duration> <timing> <delay>`**; `all` targets **all animatable properties**.  
- 速记 **`transition: <属性> <时长> <时间曲线> <延迟>`**；`all` 表示**所有可动画属性**。  
- Longhands: **`transition-property`**, **`transition-duration`**, **`transition-timing-function`**, **`transition-delay`**.  
- 长写：**`transition-property`**、**`transition-duration`**、**`transition-timing-function`**、**`transition-delay`**。  

```css
.p1 { transition: all 400ms ease 0.8s; }
```

---

## Timing Functions (ease/linear/ease-in/...)  
## 时间曲线（ease/linear/ease-in/…）

- Common values: **`ease`** (default), **`linear`**, **`ease-in`**, **`ease-out`**, **`ease-in-out`**, or **`cubic-bezier(x1,y1,x2,y2)`**.  
- 常见取值：**`ease`**（默认）、**`linear`**、**`ease-in`**、**`ease-out`**、**`ease-in-out`**，或 **`cubic-bezier(x1,y1,x2,y2)`** 自定义曲线。  

---

## Transition Examples (`all` vs `width` only)  
## 过渡示例（`all` 与仅 `width`）

```html
<!-- wp13-1.html variations -->
<style>
div { width:200px; height:100px; text-align:center; background:#333; color:#fff; margin:10px; }
div:hover { background:#6ba; width:400px; }

/* (2) both width and background color transition */
.p1 { transition: all 400ms ease 0.8s; }

/* (3) only width transitions; color switches instantly */
.p2 { transition: width 400ms ease 0.8s; }
</style>

<div>(1) no transition – instant change</div>
<div class="p1">(2) transition both, 0.8s delay</div>
<div class="p2">(3) transition width only, 0.8s delay</div>
```

---

## Practice 1: Circle → Square on Hover  
## 练习1：悬停时圆形变方形

1) Add a **`<p>`** styled as a **100×100** circle: `width/height:100px; border-radius:50%`.  
1) 新增一个 **`<p>`** 元素并设为 **100×100** 的**圆形**：`width/height:100px; border-radius:50%`。  
2) On **`:hover`**, make it **3× bigger**, turn into a **square**, **double** the **font-size**, **change background**.  
2) **`:hover`** 时放大至**3 倍**并变为**正方形**，**字体 2 倍**，同时**更改背景色**。  
3) Add a **`transition`** so the change happens **smoothly** in **0.8s**.  
3) 添加 **`transition`** 让变化在 **0.8s** 内**平滑**发生。  

---

## Keyframe Animations: `@keyframes` & `animation` Props  
## 关键帧动画：`@keyframes` 与 `animation` 属性

- Use **`@keyframes <name>`** to define **intermediate frames** (0%→100%); apply with **`animation`**.  
- 用 **`@keyframes <名称>`** 定义 **中间帧**（0%→100%）；再用 **`animation`** 应用。  
- Shorthand **`animation`** combines: **name**, **duration**, **timing**, **delay**, **iteration-count** (`infinite`), **direction** (`reverse`/`alternate`), **fill-mode** (`forwards`), etc.  
- 速记 **`animation`** 可合并：**名称**、**时长**、**曲线**、**延迟**、**循环次数**（`infinite`）、**方向**（`reverse`/`alternate`）、**填充模式**（`forwards`）等。  

```html
<!-- wp13-2.html -->
<style>
.an1 { animation: bg 10s infinite; }
@keyframes bg {
  20% { background:#acc; }
  80% { background:#800; }
}
</style>
<div class="an1">Background color changes in a loop</div>
```

---

## Keyframe Examples: Color & Size Changes  
## 关键帧示例：颜色与尺寸变化

```html
<style>
.an1 { animation: bg-color 10s infinite; }
@keyframes bg-color {
  20% { background:#acc; }
  50% { width:150px; }
  80% { background:#800; }
}
</style>
<div class="an1">Changing color and width over time</div>
```

---

## Transforms: rotate/skew and with Animation  
## 变形：旋转/倾斜与结合动画

- **`transform`** supports **2D/3D** transforms: **translate/scale/rotate/skew/perspective/matrix**.  
- **`transform`** 可进行 **2D/3D** 变形：**位移/缩放/旋转/倾斜/透视/矩阵**。  

```html
<!-- wp13-3.html -->
<style>
.t1 { transform: rotate(40deg); }  /* static rotate 静态旋转 */
.t2 { animation: kf2 3s linear 0.5s 2 forwards; } /* keep final state 最终状态保持 */
@keyframes kf2 {
  50%  { transform: rotate(80deg); }
  100% { transform: rotate(40deg); }
}
.t3 { transform: skew(10deg, 10deg); } /* skew (x,y) 倾斜 */
</style>

<div class="t1">rotate(40deg)</div>
<div class="t2">animated to 40deg in 3s</div>
<div class="t3">skew(10deg,10deg)</div>
```

---

## HTML5 Audio: `autoplay` vs `controls`  
## HTML5 音频：`autoplay` 与 `controls`

- **`<audio>`** can **autoplay** or show **controls**; modern browsers **limit autoplay** without user interaction.  
- **`<audio>`** 可设置 **自动播放**或显示**控制条**；现代浏览器通常**限制无交互的自动播放**。  

```html
<!-- wp13-4.html -->
<audio src="audio/loop2_g.mp3" autoplay></audio>
<audio src="audio/loop2_g.mp3" controls></audio>
```

---

## HTML5 Video & Fallback  
## HTML5 视频与回退

- Use **`<video src="..." controls width="...">`**; put **fallback text** between the tags for unsupported browsers.  
- 使用 **`<video src="..." controls width="...">`**；在标签内加入**回退文本**以兼容不支持的浏览器。  

```html
<!-- wp13-5.html -->
<video src="video/sample_NHK.mp4" controls width="400">
  <p>Your browser cannot play this video.</p>
</video>
```

---

## Common Media Formats & Browser Support  
## 常见媒体格式与浏览器支持

- **Audio**: **AAC (`.aac`)**, **MP3 (`.mp3`)**, **Vorbis (`.ogg`)**, **WAVE (`.wav`)**.  
- **音频**：**AAC（`.aac`）**、**MP3（`.mp3`）**、**Vorbis（`.ogg`）**、**WAVE（`.wav`）**。  
- **Video**: **AVI**, **QuickTime**, **MPEG‑1/2**, **WMV**, **FLV**, **MPEG‑4**, **WebM**.  
- **视频**：**AVI**、**QuickTime**、**MPEG‑1/2**、**WMV**、**FLV**、**MPEG‑4**、**WebM**。  
- See **MDN: Supported media formats** for up‑to‑date details:  
- 详见 **MDN：Supported media formats** 了解最新兼容性：  
  - https://developer.mozilla.org/ja/docs/Web/HTML/Supported_media_formats  

---

## Quick Checklist  
## 快速清单

- Use **`transition`** for simple state changes; pick **properties**, **duration**, **timing**, **delay** intentionally.  
- **简单动效**用 **`transition`**；明确选择**属性/时长/时间曲线/延迟**。  
- Use **`@keyframes` + `animation`** for **multi-step** or **looped** effects; consider **`iteration-count`**, **`direction`**, **`fill-mode`**.  
- **多步骤/循环**效果用 **`@keyframes` + `animation`**；注意 **`iteration-count`**、**`direction`**、**`fill-mode`**。  
- Combine **`transform`** with animations for **rotate/scale/skew** etc.  
- 将 **`transform`** 与动画结合实现 **旋转/缩放/倾斜** 等。  
- **Audio/Video**: prefer **`controls`** for usability; provide **fallback** text; mind **format support**.  
- **音视频**：为可用性提供 **`controls`**；加入**回退**文本；关注**格式支持**。  

---

[← Previous Lecture / 上一讲](./lecture12.md) · [Next Lecture / 下一讲 →](./lecture14.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

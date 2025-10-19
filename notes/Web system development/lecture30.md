[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 30: PHP Page Transfer (`include` vs `header('Location')`) and jQuery — Attributes & DOM Manipulation  
# 第30讲：PHP 页面间“嵌入/转送”（`include` 与 `header('Location')`）与 jQuery —— 属性与 DOM 操作

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Recap: PHP Conditions & Array Iteration](#recap-php-conditions--array-iteration)  
- 复习：PHP 条件与数组遍历
- [Login Result Pages: `include()` (embed) vs `header('Location: ...')` (redirect)](#login-result-pages-include-embed-vs-headerlocation-redirect)  
- 登录结果页面：`include()`（嵌入）与 `header('Location: ...')`（转送）
- [jQuery Overview & Versions (1.x/2.x/3.x) + Migrate](#jquery-overview--versions-1x2x3x--migrate)  
- jQuery 概览与版本（1.x/2.x/3.x）+ Migrate
- [Use jQuery via CDN (3.7.1) with Integrity](#use-jquery-via-cdn-371-with-integrity)  
- 通过 CDN 使用 jQuery（3.7.1）并启用完整性校验
- [jQuery Object & Method Chaining](#jquery-object--method-chaining)  
- jQuery 对象与方法链
- [Attribute APIs: `.attr()` / `.removeAttr()` / `.val()`](#attribute-apis-attr--removeattr--val)  
- 属性相关 API：`.attr()` / `.removeAttr()` / `.val()`
- [Class Helpers: `.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()`](#class-helpers-addclass--removeclass--toggleclass--hasclass)  
- class 辅助方法：`.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()`
- [Style APIs & Shortcuts: `.css()` / `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`](#style-apis--shortcuts-css--show--hide--offset--width--height)  
- 样式 API 与便捷方法：`.css()` / `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`
- [DOM Structure Changes: `.append()` / `.prepend()` / `.before()` / `.after()`](#dom-structure-changes-append--prepend--before--after)  
- DOM 结构变更：`.append()` / `.prepend()` / `.before()` / `.after()`
- [Practice A: `attribute.html` — Change Styles/Classes/Visibility](#practice-a-attributehtml--change-stylesclassesvisibility)  
- 练习 A：`attribute.html` —— 变更样式/类/可见性
- [Practice B: `movelist.html` — Move `<li>`s Between Two `<ol>`](#practice-b-movelisthtml--move-lis-between-two-ol)  
- 练习 B：`movelist.html` —— 在两个 `<ol>` 间移动 `<li>`
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Recap: PHP Conditions & Array Iteration  
## 复习：PHP 条件与数组遍历

```php
<?php
// conditions / 条件分支
if ($v == 10) { /*...*/ }
elseif ($v > 10) { /*...*/ }
else { /*...*/ }

// for + count() / for 加 count()
for ($i = 0; $i < count($arr); $i++) { echo $arr[$i]; }

// foreach (indexed) / foreach（索引）
foreach ($arr as $x) { echo $x; }

// foreach (associative) / foreach（关联）
foreach ($map as $k => $v) { echo "$k => $v"; }
?>
```
- Use **`if / elseif / else`** for branching; iterate arrays with **`for(count())`** or **`foreach`** (values / `key => value`).  
- 使用 **`if / elseif / else`** 进行分支；通过 **`for(count())`** 或 **`foreach`** 遍历数组（遍历值 / `key => value`）。  

---

## Login Result Pages: `include()` (embed) vs `header('Location: ...')` (redirect)  
## 登录结果页面：`include()`（嵌入）与 `header('Location: ...')`（转送）

```php
<?php // include: embed a page here / 嵌入到当前输出
if ($ok) include("success.html"); else include("failure.html");
```

```php
<?php // redirect: transfer to another URL / 转送到其他 URL
if ($ok) header("Location: success.html"); else header("Location: failure.html");
exit; // good practice after redirect / 转送后宜 exit
```
- **`include()`** inserts the target page’s output **into current response**; embedded page can **see variables** from the calling script.  
- **`include()`** 将目标页面输出**嵌入当前响应**；被嵌入页面可以**访问调用方变量**。  
- **`header('Location: ...')`** tells the browser to **navigate**; the **address bar changes**; target page **does not inherit** `$_POST/$_GET`.  
- **`header('Location: ...')`** 指示浏览器**跳转**；**地址栏会改变**；目标页**不会继承**原页面的 `$_POST/$_GET`。  
- Call **`header()` before any output**, otherwise you may get **“headers already sent”** errors.  
- 必须在**任何输出之前**调用 **`header()`**，否则可能报 **“headers already sent”** 错误。  

---

## jQuery Overview & Versions (1.x/2.x/3.x) + Migrate  
## jQuery 概览与版本（1.x/2.x/3.x）+ Migrate

- **jQuery** provides cross‑browser **DOM**/**effects**/**AJAX** helpers, improving productivity.  
- **jQuery** 提供跨浏览器的 **DOM/效果/AJAX** 辅助，提升开发效率。  
- Version lines: **1.x (IE8‑)**, **2.x (IE9+)**, **3.x** (re‑architected; current **3.7.1**); use **Migrate** for legacy code.  
- 版本线：**1.x（支持 IE8‑）**、**2.x（支持 IE9+）**、**3.x**（重构；当前 **3.7.1**）；旧代码可配 **Migrate** 过渡。  

---

## Use jQuery via CDN (3.7.1) with Integrity  
## 通过 CDN 使用 jQuery（3.7.1）并启用完整性校验

```html
<script
  src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
```
- **CDN** serves minified libraries fast; **`min`** is compressed; **`slim`** removes some modules.  
- **CDN** 可快速分发压缩库；**`min`** 为压缩版；**`slim`** 删除部分模块。  
- You can also **download** and host locally.  
- 亦可**下载**后本地托管。  

---

## jQuery Object & Method Chaining  
## jQuery 对象与方法链

```js
$("h1").addClass("highlight").hide().fadeIn();
```
- `$(selector)` returns a **jQuery object** that wraps **all matched elements**; most methods return **the same object** for **chaining**.  
- `$(selector)` 返回封装**全部匹配元素**的 **jQuery 对象**；多数方法返回**自身**以支持**链式调用**。  

---

## Attribute APIs: `.attr()` / `.removeAttr()` / `.val()`  
## 属性相关 API：`.attr()` / `.removeAttr()` / `.val()`

```js
// set single or multiple attributes / 设置单个或多个属性
$("a").attr("href", "http://bar.xxx/");
$("img").attr({ alt: "photo", title: "cover" });

// read the attribute (first element) / 读属性（仅第一个匹配元素）
const href = $("a").attr("href");

// remove attribute / 删除属性键值对（而非仅值）
$("input[type=radio]").removeAttr("checked");

// value shortcut for form controls / 表单值便捷方法
$("#account").val("k12345");      // set / 设
const v = $("#account").val();    // get / 取（仅第一个）
```
- `.attr(name, value)` sets attribute(s) on **all** elements; `.attr(name)` **reads from the first** matched element.  
- `.attr(name, value)` 对**所有**元素设属性；`.attr(name)` **仅从第一个**匹配元素读取。  
- `.removeAttr(name)` **deletes** the `name="value"` pair; use `.val()` to get/set **form values**.  
- `.removeAttr(name)` **删除**成对属性；用 `.val()` 获取/设置**表单值**。  

---

## Class Helpers: `.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()`  
## class 辅助方法：`.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()`

```js
$("div").addClass("blue");      // add (non-overwriting) / 追加（不覆盖）
$("div").removeClass("blue");   // remove that token / 删除该类名
$("div").toggleClass("blue");   // add if missing, else remove / 无则加，有则删
const has = $("div").hasClass("blue"); // boolean / 布尔
```
- Unlike `.attr("class", ...)`, these **don’t overwrite** the entire class list.  
- 与 `.attr("class", ...)` 不同，这些方法**不会覆盖**整段类名。  

---

## Style APIs & Shortcuts: `.css()` / `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`  
## 样式 API 与便捷方法：`.css()` / `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`

```js
// css get/set / 读取或设置单个 CSS 属性
$("#target").css("border", "5px solid blue");
const b = $("#target").css("border");

// show/hide (display) / 显示/隐藏（display）
$("#target").hide();
$("#target").show();

// position via page offsets / 页面坐标
$("#target").offset({ top: 120, left: 60 });
const pos = $("#target").offset();

// size / 尺寸
$("#target").width(320).height(240);
```
- `.css(prop, value)` adds/overwrites **just that CSS property**; `.show()`/`.hide()` map to `display`.  
- `.css(prop, value)` **只影响该 CSS 属性**；`.show()`/`.hide()` 改变 `display`。  
- `.offset()` **reads/sets** absolute position; `.width()`/`.height()` read or set size.  
- `.offset()` 可**读/设**绝对位置；`.width()`/`.height()` 读取或设置尺寸。  

---

## DOM Structure Changes: `.append()` / `.prepend()` / `.before()` / `.after()`  
## DOM 结构变更：`.append()` / `.prepend()` / `.before()` / `.after()`

```html
<div id="box"><p>abc</p><p>123</p></div>
<script>
  $("#box").append($("<p>XYZ</p>"));   // as last child / 作为最后一个子元素
  $("#box").prepend($("<p>XYZ</p>"));  // as first child / 作为第一个子元素
  $("#p").after($("<p>XYZ</p>"));      // after sibling / 作为兄弟在后
  $("#p").before($("<p>XYZ</p>"));     // before sibling / 作为兄弟在前
</script>
```
- **Append/Prepend** insert into **children** (end/start); **Before/After** insert as **siblings** (before/after).  
- **Append/Prepend** 插入到**子节点**（末尾/开头）；**Before/After** 插入为**兄弟节点**（前/后）。  

---

## Practice A: `attribute.html` — Change Styles/Classes/Visibility  
## 练习 A：`attribute.html` —— 变更样式/类/可见性

- For `#target`, call methods to: **blue 5px border**, **swap width/height (320↔240)**, **hide**, **add/remove class `"blue"`**, and **read back** current values.  
- 针对 `#target`，调用方法以实现：**蓝色 5px 边框**、**交换宽高（320↔240）**、**隐藏**、**添加/删除 `"blue"` 类**，并**读取**当前值。  

```js
$("#target").css("border","5px solid blue");
const w = $("#target").width(), h = $("#target").height();
$("#target").width(h).height(w);
$("#target").hide();
$("#target").addClass("blue").removeClass("blue");
console.log($("#target").css("border"), $("#target").width(), $("#target").height());
```

---

## Practice B: `movelist.html` — Move `<li>`s Between Two `<ol>`  
## 练习 B：`movelist.html` —— 在两个 `<ol>` 间移动 `<li>`

- Two lists **A/B**; clicking **A→B** moves **the first `<li>` of A** to **the end of B**; **A←B** moves conversely.  
- 两个列表 **A/B**；点击 **A→B** 将 **A 的第一个 `<li>`** 移到 **B 的末尾**；**A←B** 反向操作。  

```html
<ol id="listA"><li>はまち</li><li>たい</li><li>ひらめ</li><li>うに</li></ol>
<ol id="listB"><li>はまち</li></ol>
<button id="ab">A→B</button><button id="ba">A←B</button>
<script>
  $("#ab").on("click", () => { $("#listB").append($("#listA > li:first")); });
  $("#ba").on("click", () => { $("#listA").append($("#listB > li:first")); });
</script>
```
- Key selector: **`#listA > li:first`** picks the **first** `<li>` under `#listA`.  
- 关键选择器：**`#listA > li:first`** 选中 `#listA` 下的**第一个** `<li>`。  

---

## Quick Checklist  
## 快速清单

- Decide **embed vs redirect**: `include()` keeps context; `header('Location')` **navigates** and **drops** POST/GET.  
- 选择**嵌入或转送**：`include()` 保留上下文；`header('Location')` **跳转**且**不继承** POST/GET。  
- Load **jQuery 3.7.1** via **CDN** (with **integrity**) or host locally.  
- 通过 **CDN**（含 **integrity**）加载 **jQuery 3.7.1** 或本地托管。  
- Use **`.attr()`/`.removeAttr()`/`.val()`** for attributes; **class helpers** to manage class tokens.  
- 属性使用 **`.attr()`/`.removeAttr()`/`.val()`**；用 **class 辅助方法**管理类名。  
- For styles, use **`.css()`**, **`.show()`/`.hide()`**; for position/size, use **`.offset()` / `.width()` / `.height()`**.  
- 样式用 **`.css()`**、**`.show()`/`.hide()`**；位置/尺寸用 **`.offset()` / `.width()` / `.height()`**。  
- Change DOM structure via **`.append()`/`.prepend()`/`.before()`/`.after()`**.  
- 用 **`.append()`/`.prepend()`/`.before()`/`.after()`** 改变 DOM 结构。  

---

## Notes
## 注释

<details><summary>CDN choices & docs / CDN 选择与文档</summary>

- Official jQuery CDN: **releases.jquery.com**; also **Google/Microsoft/cdnjs/jsDelivr**.  
- 官方 jQuery CDN：**releases.jquery.com**；亦有 **Google/Microsoft/cdnjs/jsDelivr**。  
- API docs: **api.jquery.com** (EN), **jquerystudy.info / s3pw.com/qrefy** (JA), **hemin.cn/jq/** (ZH).  
- API 文档：**api.jquery.com**（英）、**jquerystudy.info / s3pw.com/qrefy**（日）、**hemin.cn/jq/**（中）。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture29.md) · [Next Lecture / 下一讲 →](./lecture31.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

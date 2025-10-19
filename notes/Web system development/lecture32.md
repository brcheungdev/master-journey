[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 32: jQuery — DOM Replacement (`replaceWith`, `.text()`, `.html()`), Ajax `.load()`, and Calculator Practice  
# 第32讲：jQuery —— DOM 替换（`replaceWith`、`.text()`、`.html()`）、Ajax `.load()` 与计算器练习

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Recap: DOM Insertion (append/prepend/before/after)](#recap-dom-insertion-appendprependbeforeafter)  
- 复习：DOM 插入（append/prepend/before/after）
- [Create Elements from HTML Strings](#create-elements-from-html-strings)  
- 通过 HTML 字符串创建元素
- [Replace Elements & Inner Content](#replace-elements--inner-content)  
- 替换元素与内部内容
- [Practice: `translate.html` — Replace a `<div>` by Textarea Input](#practice-translatehtml--replace-a-div-by-textarea-input)  
- 练习：`translate.html` —— 用文本框内容替换 `<div>` 内部
- [Ajax Basics & jQuery `.load()`](#ajax-basics--jquery-load)  
- Ajax 基本概念与 jQuery `.load()`
- [Frame‑like Content Swap with `.load()`](#frame-like-content-swap-with-load)  
- 用 `.load()` 实现“类 frame”的内容切换
- [POST Data with `.load(url, data)`](#post-data-with-loadurl-data)  
- 使用 `.load(url, data)` 发送 POST 数据
- [Practice: `calc.html` + `calc.php` (Add/Sub/Mul/Div Table)](#practice-calchtml--calcphp-addsubmuldiv-table)  
- 练习：`calc.html` + `calc.php`（加减乘除表格）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Recap: DOM Insertion (append/prepend/before/after)  
## 复习：DOM 插入（append/prepend/before/after）

```html
<div id="box"><p>abc</p><p id="p">123</p></div>
<script>
  $("#box").append($("<p>XYZ</p>"));   // last child / 末尾子元素
  $("#box").prepend($("<p>XYZ</p>"));  // first child / 首个子元素
  $("#p").after($("<p>XYZ</p>"));      // after sibling / 插入为后置兄弟
  $("#p").before($("<p>XYZ</p>"));     // before sibling / 插入为前置兄弟
</script>
```
- **Append/Prepend** change **parent–child** order; **Before/After** change **sibling** order.  
- **Append/Prepend** 改变**父子**顺序；**Before/After** 改变**兄弟**顺序。  fileciteturn31file0

---

## Create Elements from HTML Strings  
## 通过 HTML 字符串创建元素

```js
const span = $("<span>所属</span>");
const empty = $("<div/>");      // empty div
// not in DOM until inserted / 插入前不在页面 DOM 中
$("#box").append(span);
```
- `$("<tag>…</tag>")` or `$("<tag/>")` **creates** elements; insert with `.append()`/`.prepend()`/etc.  
- 使用 `$("<tag>…</tag>")` 或 `$("<tag/>")` **创建**元素；再用 `.append()`/`.prepend()` 等插入。  fileciteturn31file0

---

## Replace Elements & Inner Content  
## 替换元素与内部内容

```html
<h1>Heading 1</h1>
<script>
  $("h1").replaceWith($("<h3>Heading 3</h3>")); // replace the whole node / 替换整个节点
  $("h1").text("お知らせ");                      // replace inner text / 替换纯文本
  $("h1").html("お知らせ <h3>10 月 30 日</h3>"); // replace inner HTML / 替换 HTML
</script>
```
- **`replaceWith(node)`** swaps the **entire element**.  
- **`replaceWith(node)`** **替换整个元素**。  
- **`.text(str)`** sets **plain text** (HTML **not interpreted**).  
- **`.text(str)`** 设置**纯文本**（HTML **不被解析**）。  
- **`.html(str)`** sets **HTML** (tags **are parsed**).  
- **`.html(str)`** 设置 **HTML**（标签会被**浏览器解析**）。  fileciteturn31file0

---

## Practice: `translate.html` — Replace a `<div>` by Textarea Input  
## 练习：`translate.html` —— 用文本框内容替换 `<div>` 内部

```html
<textarea id="src" rows="6" cols="40"><h2>Kyoto</h2></textarea>
<div id="target"></div>
<button id="apply">Apply / 应用</button>
<button id="extract">Extract / 取出</button>

<script>
  $("#apply").on("click", () => { $("#target").html( $("#src").val() ); });
  $("#extract").on("click", () => { $("#src").val( $("#target").html() ); });
</script>
```
- Click **Apply** to **render** the textarea’s HTML inside `#target` using **`.html()`**.  
- 点击 **Apply** 使用 **`.html()`** 将文本框内的 HTML **渲染**到 `#target`。  
- Click **Extract** to **read back** via **`.html()`** into the textarea.  
- 点击 **Extract** 以 **`.html()`** **读回**到文本框。  fileciteturn31file0

---

## Ajax Basics & jQuery `.load()`  
## Ajax 基本概念与 jQuery `.load()`

- **Ajax** lets JavaScript **fetch a URL** and **update part of the DOM** without a full page reload.  
- **Ajax** 允许 JavaScript **获取某个 URL** 并**局部更新 DOM**，无需整页刷新。  
- With jQuery, the simplest form is: **`$(T).load(url)`** to **replace** element **T’s inner HTML** with the fetched content.  
- 使用 jQuery 的最简形式：**`$(T).load(url)`**，用响应内容**替换**元素 **T 的内部**。  fileciteturn31file0

---

## Frame‑like Content Swap with `.load()`  
## 用 `.load()` 实现“类 frame”的内容切换

```html
<ul>
  <li><a href="page01.html">page01</a></li>
  <li><a href="page02.html">page02</a></li>
</ul>
<div id="target"></div>

<script>
$(function(){
  $("ul a").on("click", function(){
    var url = $(this).attr("href");
    $("#target").load(url);       // put the page content into #target / 将页面内容放入 #target
    return false;                 // cancel navigation / 取消默认跳转
  });
});
</script>
```
- Intercept link clicks, **prevent default**, and **inject** the fetched HTML into a container.  
- 拦截链接点击，**阻止默认**跳转，并将获取的 HTML **注入**到容器中。  fileciteturn31file0

---

## POST Data with `.load(url, data)`  
## 使用 `.load(url, data)` 发送 POST 数据

```js
$("#result").load("calc.php", { "x": 25, "y": 40 }); // send POST body / 以 POST 发送
```
- The **second argument** is an **object** that becomes **POST data** (`x=25&y=40`).  
- **第二个参数**是**对象**，会被编码为 **POST 数据**（`x=25&y=40`）。  
- **Same‑origin policy**: the URL must be **on the same domain** as the calling page; behavior on **local files** varies by browser (slides: IE/Opera/Chrome ×; Safari/Firefox ✓).  
- **同源策略**：URL 必须与当前页面**同域**；**本地文件**行为因浏览器而异（课件示例：IE/Opera/Chrome ×；Safari/Firefox ✓）。  fileciteturn31file0

---

## Practice: `calc.html` + `calc.php` (Add/Sub/Mul/Div Table)  
## 练习：`calc.html` + `calc.php`（加减乘除表格）

```html
<!-- calc.html -->
<input id="x" type="number"><input id="y" type="number">
<button id="btn">計算 / Calc</button>
<div id="result"></div>

<script>
$("#btn").on("click", function(){
  $("#result").load("calc.php", { "x": $("#x").val(), "y": $("#y").val() });
  return false; // cancel <form> submit & navigation / 取消表单提交与跳转
});
</script>
```
- Click **Calc** to send **POST** with `x`/`y` to `calc.php`, then **render** the returned table in `#result`.  
- 点击 **Calc** 将 `x`/`y` 以 **POST** 发送给 `calc.php`，再把返回的表格**渲染**到 `#result`。  

```php
<?php // calc.php
$x = $_POST['x']; $y = $_POST['y'];
echo "<table><tbody>";
echo "<tr><td>加算</td><td>".($x+$y)."</td></tr>";
echo "<tr><td>減算</td><td>".($x-$y)."</td></tr>";
echo "<tr><td>乗算</td><td>".($x*$y)."</td></tr>";
echo "<tr><td>除算</td><td>".($y==0 ? 'NaN' : ($x/$y))."</td></tr>";
echo "</tbody></table>";
```
- In the PHP script, **read POST** and **echo** an HTML table with the results.  
- 在 PHP 端**读取 POST** 并 **echo** 出结果表格。  fileciteturn31file0

---

## Quick Checklist  
## 快速清单

- Choose **replace level**: `replaceWith` (whole element) vs `.html()` (HTML) vs `.text()` (plain text).  
- 明确**替换层级**：`replaceWith`（整节点） vs `.html()`（HTML） vs `.text()`（纯文本）。  
- Use **`.load(url)`** to swap content; add **`return false`** to stop navigation/submission.  
- 用 **`.load(url)`** 切换内容；配合 **`return false`** 阻止跳转/提交。  
- Use **`.load(url, data)`** to **POST** an object as form data.  
- 用 **`.load(url, data)`** 将对象作为表单数据 **POST**。  
- **Same‑origin** applies to `.load()`; keep resources **under the same domain/path**.  
- `.load()` 受**同源策略**限制；资源需在**同一域名**下。  fileciteturn31file0

---

## Notes
## 注释

<details><summary>About cross‑origin and modern alternatives / 关于跨域与现代替代</summary>

- For cross‑origin requests, use **CORS** or a **server proxy**; `.load()` won’t bypass same‑origin.  
- 跨域时需要 **CORS** 或**服务器代理**；`.load()` 无法绕过同源限制。  
- Modern apps often prefer **`fetch()`**/`XMLHttpRequest` for **fine‑grained control** over requests and errors.  
- 现代应用常用 **`fetch()`**/`XMLHttpRequest` 以获得对请求与错误的**精细控制**。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture31.md) · [Next Lecture / 下一讲 →](./lecture33.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

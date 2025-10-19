[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 29: PHP Recap and jQuery Introduction  
# 第29讲：PHP 回顾与 jQuery 入门

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [PHP Recap: Run via Apache, Variables & Arrays, GET/POST](#php-recap-run-via-apache-variables--arrays-getpost)  
- PHP 回顾：通过 Apache 运行、变量与数组、GET/POST
- [Conditional Branching in PHP (if / else / elseif)](#conditional-branching-in-php-if--else--elseif)  
- PHP 条件分支（if / else / elseif）
- [Login Result Pages: `include()` vs `header('Location: ...')`](#login-result-pages-include-vs-headerlocation-)  
- 登录结果页面：`include()` 与 `header('Location: ...')`
- [What Is jQuery and Why Use It](#what-is-jquery-and-why-use-it)  
- 什么是 jQuery 以及为什么使用
- [jQuery Versions (1.x / 2.x / 3.x) & Migrate](#jquery-versions-1x--2x--3x--migrate)  
- jQuery 版本（1.x / 2.x / 3.x）与 Migrate
- [Using jQuery via CDN (3.7.1) and Integrity](#using-jquery-via-cdn-371-and-integrity)  
- 通过 CDN 使用 jQuery（3.7.1）与完整性校验
- [jQuery Object: `$(selector)` and Method Chaining](#jquery-object-selector-and-method-chaining)  
- jQuery 对象：`$(selector)` 与方法链
- [Without jQuery vs With jQuery: Highlight Example](#without-jquery-vs-with-jquery-highlight-example)  
- 不用 jQuery 与使用 jQuery：高亮示例
- [Common APIs: `.length`, `.val()`, `.hasClass()`](#common-apis-length-val-hasclass)  
- 常用 API：`.length`、`.val()`、`.hasClass()`
- [Practice: Mastering Selectors](#practice-mastering-selectors)  
- 练习：熟练使用选择器
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## PHP Recap: Run via Apache, Variables & Arrays, GET/POST  
## PHP 回顾：通过 Apache 运行、变量与数组、GET/POST

- Run PHP **through Apache** at `http://localhost/<id>/<date>/<file>.php` (files under `C:\xampp\htdocs\...`).  
- 通过 **Apache** 访问 `http://localhost/<学籍番号>/<日期>/<文件>.php`（文件放在 `C:\xampp\htdocs\...`）。  
- Variables start with **`$`**; arrays can be **indexed** or **associative**.  
- 变量以 **`$`** 开头；数组分为**索引数组**与**关联数组**。  

```php
<?php
  $message = "どうも，PHP！";
  echo "<h1>{$message}</h1>";

  $a = array("百万遍","京都駅前","東京","札幌");    // indexed / 索引
  $m = array("h"=>"百万遍","k"=>"京都駅前");       // associative / 关联
  echo $a[0] . " / " . $m["k"];
?>
```

- Submit data via **GET** (URL query) or **POST** (request body); receive with **`$_GET` / `$_POST`**.  
- 通过 **GET**（URL 查询串）或 **POST**（请求体）提交；用 **`$_GET` / `$_POST`** 接收。  

---

## Conditional Branching in PHP (if / else / elseif)  
## PHP 条件分支（if / else / elseif）

```php
<?php
  $val = 10;
  if ($val == 10) { echo "val は 10 と等しい。<br>"; }

  if ($val == 10) { echo "等しい"; }
  else            { echo "等しくない"; }

  if     ($val < 0)  { echo "負"; }
  elseif ($val == 0) { echo "零"; }
  else               { echo "正"; }
?>
```

- Combine conditions with **`&&`**, **`||`**, and **`!`**; `!($val==10)` equals **`$val != 10`**.  
- 使用 **`&&`**、**`||`** 与 **`!`** 组合条件；`!($val==10)` 等价于 **`$val != 10`**。  

---

## Login Result Pages: `include()` vs `header('Location: ...')`  
## 登录结果页面：`include()` 与 `header('Location: ...')`

- After login check in `check.php`, either **embed** a page with **`include("success.html")`**/**`include("failure.html")`**, or **redirect** with **`header("Location: success.html")`**.  
- 在 `check.php` 中完成校验后，可用 **`include("success.html")`**/**`include("failure.html")`** 进行**页面嵌入**，或用 **`header("Location: success.html")`** 进行**跳转**。  
- **Note**: call `header()` **before any output**; redirected pages **don’t receive** `$_POST/$_GET` automatically.  
- **注意**：`header()` 必须在**任何输出之前**调用；跳转页面**不会继承**`$_POST/$_GET`。  

```
login.html → check.php (judge) → include(...)  ⟶ 当前页嵌入结果
login.html → check.php (judge) → header(...)   ⟶ 浏览器重定向到结果页
```
```
login.html → check.php（判定）→ include(...)  ⟶ 当前页嵌入结果
login.html → check.php（判定）→ header(...)   ⟶ 浏览器重定向到结果页
```

---

## What Is jQuery and Why Use It  
## 什么是 jQuery 以及为什么使用

- **jQuery** is a **popular JavaScript library** for **DOM manipulation**, **effects/animation**, and **AJAX**, smoothing **cross‑browser differences**.  
- **jQuery** 是用于 **DOM 操作**、**效果/动画**与 **AJAX** 的**流行 JavaScript 库**，可平滑处理**跨浏览器差异**。  
- It wraps matched elements into a single **jQuery object** and applies methods to **all** matched nodes at once.  
- 它将匹配到的元素封装为**一个 jQuery 对象**，对其调用方法会作用于**所有**匹配节点。  

---

## jQuery Versions (1.x / 2.x / 3.x) & Migrate  
## jQuery 版本（1.x / 2.x / 3.x）与 Migrate

- **1.x** supports **IE8‑**; **2.x** supports **IE9+**; **3.x** is **re‑architected** (current **3.7.1**).  
- **1.x** 支持 **IE8 及更早**；**2.x** 支持 **IE9+**；**3.x** **重构**（当前 **3.7.1**）。  
- Some older APIs were **removed** (e.g., `.load/.unload/.error` handlers — use **`.on()`**); **ready** listener behavior changed.  
- 部分旧 API 被**移除**（如 `.load/.unload/.error` 事件处理——改用 **`.on()`**）；`ready` 的行为也有调整。  
- Use **jQuery Migrate** to run legacy code on newer jQuery.  
- 可使用 **jQuery Migrate** 在新版 jQuery 上兼容旧代码。  

---

## Using jQuery via CDN (3.7.1) and Integrity  
## 通过 CDN 使用 jQuery（3.7.1）与完整性校验

```html
<script
  src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
```
- **CDN** (Content Delivery Network) hosts popular libraries for **fast, cached** delivery; `min` is minified; `slim` removes some modules.  
- **CDN**（内容分发网络）为常用库提供**快速且可缓存**的分发；`min` 为压缩版；`slim` 去掉了部分模块。  
- Alternatively, **download** from the official site and host it yourself.  
- 或从 **官方站点**下载并自行托管。  

---

## jQuery Object: `$(selector)` and Method Chaining  
## jQuery 对象：`$(selector)` 与方法链

- Select elements with **CSS selectors**: `$("h1")`, `$("table>tbody>tr")`.  
- 用 **CSS 选择器**选择元素：`$("h1")`、`$("table>tbody>tr")`。  
- Methods often return **the same jQuery object**, enabling **chaining**.  
- 方法通常返回**同一 jQuery 对象**，可进行**链式调用**。  

```js
$("h1").addClass("highlight").hide().fadeIn();
```

---

## Without jQuery vs With jQuery: Highlight Example  
## 不用 jQuery 与使用 jQuery：高亮示例

**Without jQuery**  
**不使用 jQuery**

```html
<script>
function highlight(){
  var h1All = document.getElementsByTagName("h1");
  for (var i=0; i<h1All.length; i++){
    var h1 = h1All.item(i);
    h1.setAttribute("class","highlight");
  }
}
</script>
```

**With jQuery**  
**使用 jQuery**

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script>
function highlight(){
  $("h1").addClass("highlight");
}
</script>
```

---

## Common APIs: `.length`, `.val()`, `.hasClass()`  
## 常用 API：`.length`、`.val()`、`.hasClass()`

```js
var n = $("table>tbody>tr").length;           // number of matched elements / 匹配元素个数
var v = $("input[name=account]").val();       // form value / 表单值
if ($("h1").hasClass("highlight")) { /*...*/ } // check class / 判断是否含类
```

---

## Practice: Mastering Selectors  
## 练习：熟练使用选择器

- Highlight **even rows** in a table.  
- 高亮表格的**偶数行**。  
- Highlight the **last row**.  
- 高亮**最后一行**。  
- Highlight the **rightmost cell** of each row.  
- 高亮每行的**最右侧单元格**。  
- Highlight all cells that **contain “4”**.  
- 高亮**包含“4”** 的单元格。  
- Highlight all rows **containing the cell “DWH”**.  
- 高亮**包含“DWH” 单元格**的整行。  
- (Tip: Avoid hard‑coding “the 3rd row”. Use **structural selectors**.)  
- （提示：避免硬编码“第 3 行”，请使用**结构性选择器**。）  

---

## Quick Checklist  
## 快速清单

- Place `.php` under **`htdocs`** and run via **Apache** (`http://localhost/...`).  
- 将 `.php` 放在 **`htdocs`** 下并通过 **Apache** 访问（`http://localhost/...`）。  
- For login result display, choose **`include()`** (embed) or **`header('Location:')`** (redirect).  
- 登录结果显示可选择 **`include()`**（嵌入）或 **`header('Location:')`**（跳转）。  
- Load **jQuery 3.7.1** from **CDN** with **integrity**; or host it yourself.  
- 使用 **CDN** 加载 **jQuery 3.7.1** 并附 **integrity**；或自行托管。  
- Select with **CSS selectors**; prefer **method chaining** for concise code.  
- 用 **CSS 选择器**选取元素；偏好**链式调用**使代码简洁。  
- Know **`.length` / `.val()` / `.hasClass()`** and try selector exercises.  
- 熟悉 **`.length` / `.val()` / `.hasClass()`**，动手完成选择器练习。  

---

## Notes 
## 注释

<details><summary>Removed/changed APIs & the <code>.on()</code> pattern</summary>

- In jQuery 3.x, old event helpers like **`.load`/`.unload`/`.error`** were removed; prefer **`$(...).on('event', handler)`**.  
- 在 jQuery 3.x 中，旧的事件便捷方法 **`.load`/`.unload`/`.error`** 被移除；应使用 **`$(...).on('event', handler)`**。  
</details>

---

[← Previous Lecture / 上一讲](./lecture28.md) · [Next Lecture / 下一讲 →](./lecture30.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 31: jQuery — Attributes, DOM Tree Operations, and Event Handling  
# 第31讲：jQuery —— 属性操作、DOM 树操作与事件处理

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Using jQuery via CDN (3.7.1) or Download](#using-jquery-via-cdn-371-or-download)  
- 通过 CDN（3.7.1）或下载方式使用 jQuery
- [Recap: jQuery Object & CSS Selectors](#recap-jquery-object--css-selectors)  
- 复习：jQuery 对象与 CSS 选择器
- [Attribute Operations: `.attr()` / `.removeAttr()` / `.val()`](#attribute-operations-attr--removeattr--val)  
- 属性操作：`.attr()` / `.removeAttr()` / `.val()`
- [Class & Style Shortcuts: `.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()` / `.css()`](#class--style-shortcuts-addclass--removeclass--toggleclass--hasclass--css)  
- 类名与样式便捷方法：`.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()` / `.css()`
- [Display/Position/Size Helpers: `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`](#displaypositionsize-helpers-show--hide--offset--width--height)  
- 显示/位置/尺寸便捷方法：`.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`
- [DOM Tree Changes: `.append()` / `.prepend()` / `.before()` / `.after()`](#dom-tree-changes-append--prepend--before--after)  
- DOM 树结构变更：`.append()` / `.prepend()` / `.before()` / `.after()`
- [Create New Elements from HTML Strings](#create-new-elements-from-html-strings)  
- 通过 HTML 字符串创建新元素
- [Event Handling: `.on()` / `.off()` — Direct vs Delegated](#event-handling-on--off--direct-vs-delegated)  
- 事件处理：`.on()` / `.off()` —— 直接绑定与事件委托
- [`this` in Callbacks and Anonymous Functions](#this-in-callbacks-and-anonymous-functions)  
- 回调中的 `this` 与无名函数
- [Practice 1: `selector.html` — Master the Selectors](#practice-1-selectorhtml--master-the-selectors)  
- 练习1：`selector.html` —— 熟练使用选择器
- [Practice 2: `chooser.html` — Radio + Invert Highlight](#practice-2-chooserhtml--radio--invert-highlight)  
- 练习2：`chooser.html` —— 单选 + 反选高亮
- [Practice 3: `movelist.html` — Move Items Between Lists](#practice-3-movelisthtml--move-items-between-lists)  
- 练习3：`movelist.html` —— 在列表间移动条目
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Using jQuery via CDN (3.7.1) or Download  
## 通过 CDN（3.7.1）或下载方式使用 jQuery

```html
<script
  src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
```
- You can also **download** from the official site; variants include **minified**, **uncompressed**, and **slim**.  
- 亦可从**官方站点**下载；可选版本包括**压缩版**、**未压缩版**与**瘦身版（slim）**。  

---

## Recap: jQuery Object & CSS Selectors  
## 复习：jQuery 对象与 CSS 选择器

- `$(selector)` wraps **all matched elements** into **one jQuery object**; calling a method **applies to all matches**.  
- `$(selector)` 将**所有匹配元素**封装为**单一 jQuery 对象**；调用方法会**作用于全部匹配项**。  

```js
$("h1").addClass("highlight"); // no for-loop needed / 不需要 for 循环
```

---

## Attribute Operations: `.attr()` / `.removeAttr()` / `.val()`  
## 属性操作：`.attr()` / `.removeAttr()` / `.val()`

```js
// set attributes (one or many) / 设定（单个或多个）
$("img").attr("alt", "photo");
$("img").attr({ alt: "photo", title: "cover" });

// read (first element) / 读取（仅第一个匹配）
const href = $("a").attr("href");

// remove attribute pair / 删除属性键值对
$("input[type=radio]").removeAttr("checked");

// value shortcut for form elements / 表单 value 便捷方法
$("#account").val("k12345");  // set / 设
const v = $("#account").val(); // get / 取（首个）
```

- `.attr(name, value)` sets on **all** elements; `.attr(name)` reads **from the first** match.  
- `.attr(name, value)` 作用于**所有元素**；`.attr(name)` 仅从**首个匹配**读取。  

---

## Class & Style Shortcuts: `.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()` / `.css()`  
## 类名与样式便捷方法：`.addClass()` / `.removeClass()` / `.toggleClass()` / `.hasClass()` / `.css()`

```js
$("div").addClass("blue").removeClass("blue").toggleClass("blue");
const has = $("div").hasClass("blue");

$("#target").css("border","5px solid blue"); // only affects the 'border' prop
```
- Class helpers **don’t overwrite** the entire class list (unlike `attr('class', ...)`).  
- 类名方法**不会覆盖**整段类名（不同于 `attr('class', ...)`）。  

---

## Display/Position/Size Helpers: `.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`  
## 显示/位置/尺寸便捷方法：`.show()` / `.hide()` / `.offset()` / `.width()` / `.height()`

```js
$("#target").hide().show();
$("#target").offset({ top:120, left:60 });
const pos = $("#target").offset();
$("#target").width(320).height(240);
```

---

## DOM Tree Changes: `.append()` / `.prepend()` / `.before()` / `.after()`  
## DOM 树结构变更：`.append()` / `.prepend()` / `.before()` / `.after()`

```html
<div id="box"><p>abc</p><p>123</p></div>
<script>
  $("#box").append($("<p>XYZ</p>"));   // last child / 最后一个子元素
  $("#box").prepend($("<p>XYZ</p>"));  // first child / 第一个子元素
  $("#p").after($("<p>XYZ</p>"));      // as next sibling / 后置兄弟
  $("#p").before($("<p>XYZ</p>"));     // as previous sibling / 前置兄弟
</script>
```

---

## Create New Elements from HTML Strings  
## 通过 HTML 字符串创建新元素

```js
const span = $("<span>所属</span>");
const emptyDiv = $("<div/>");
```
- Newly created elements are **not in the page** until inserted via **`.append()`/`.prepend()`/etc.**  
- 新创建的元素在通过 **`.append()`/`.prepend()`** 等方法插入之前，**不属于页面 DOM**。  

---

## Event Handling: `.on()` / `.off()` — Direct vs Delegated  
## 事件处理：`.on()` / `.off()` —— 直接绑定与事件委托

```html
<button id="b01" type="button">ボタン</button>
<script>
  // Direct binding: run after the element exists (e.g., put script at end of <body>)
  // 直接绑定：在元素已存在后执行（如将脚本写在 <body> 末尾）
  $("#b01").on("click", doThis);
  function doThis(){ /* ... */ }

  // Delegated binding: works for dynamically added children too
  // 事件委托：对子元素的后续新增也有效
  $("ol").on("click", "li", function(){
    $(this).toggleClass("on");
  });

  // Remove handlers
  // 解除绑定
  $("#b01").off("click");
</script>
```
- Use **delegation** when targets might be **added later**; bind on a **static ancestor**.  
- 当目标元素可能**动态新增**时，使用**事件委托**；把监听绑定在**稳定的祖先节点**上。  

---

## `this` in Callbacks and Anonymous Functions  
## 回调中的 `this` 与无名函数

```js
$("h1").on("click", function(){
  alert( $(this).text() ); // the clicked <h1> / 被点击的 <h1>
});
```
- Handlers can be **anonymous functions**; inside, **`this`** refers to the **event target** (wrapped by `$(this)`).  
- 处理函数可用**无名函数**；其内 **`this`** 指向**事件目标元素**（用 `$(this)` 包装）。  

---

## Practice 1: `selector.html` — Master the Selectors  
## 练习1：`selector.html` —— 熟练使用选择器

```js
$("table tr:nth-child(even)").addClass("on");     // even rows / 偶数行
$("table tr:last-child").addClass("on");          // last row / 最后一行
$("table tr td:last-child").addClass("on");       // rightmost cells / 每行最右侧单元格
$("td:contains(4)").addClass("on");               // cells containing “4” / 含“4”的单元格
$("tr:has(td:contains(DWH))").addClass("on");     // rows containing cell “DWH” / 含“DWH”的行
// Avoid hard-coding “3rd row”; use structural selectors.
// 避免硬编码“第3行”；请使用结构性选择器。
```

---

## Practice 2: `chooser.html` — Radio + Invert Highlight  
## 练习2：`chooser.html` —— 单选 + 反选高亮

- A bulleted list with **radio buttons**; checking an item **inverts its highlight**.  
- 带 **单选按钮**的项目列表；选中某项时**反转高亮**。  

```html
<ul id="choices">
  <li><label><input type="radio" name="c">Kyoto</label></li>
  <li><label><input type="radio" name="c">Tokyo</label></li>
</ul>
<script>
  $("#choices").on("change", "input[type=radio]", function(){
    // remove highlight from all, add to the chosen one
    // 先清除所有高亮，再给选中项加上
    $("#choices li").removeClass("on");
    $(this).closest("li").addClass("on");
  });
</script>
```
- Toggle **text-only** by adding class on the **label**; toggle **whole item** by adding class on the **`li`**.  
- 若只需**文字反色**，给 **`label`** 加类；若需**整项反色**，给 **`li`** 加类。  

---

## Practice 3: `movelist.html` — Move Items Between Lists  
## 练习3：`movelist.html` —— 在列表间移动条目

```html
<ol id="listA"><li>はまち</li><li>たい</li><li>ひらめ</li><li>うに</li></ol>
<ol id="listB"><li>はまち</li></ol>
<button id="ab">A→B</button><button id="ba">A←B</button>

<input id="in" placeholder="新項目"><button id="add">追加</button>

<script>
  $("#ab").on("click", () => { $("#listB").append($("#listA > li:first")); });
  $("#ba").on("click", () => { $("#listA").append($("#listB > li:first")); });

  // click to highlight (works on new items via delegation)
  // 点击条目高亮（委托确保对新增项也有效）
  $("ol").on("click", "li", function(){ $(this).toggleClass("on"); });

  // add new item from input
  // 从输入框追加新项到 listA
  $("#add").on("click", () => {
    const li = $("<li>").text($("#in").val());
    $("#listA").append(li);
  });
</script>
```
- Key selector: **`#listA > li:first`** picks the **first** item under list A.  
- 关键选择器：**`#listA > li:first`** 选择列表 A 下的**第一个**条目。  

---

## Quick Checklist  
## 快速清单

- Prefer **class helpers** and **`.css()`** over raw `attr('class')`/`style`.  
- 相比直接 `attr('class')`/`style`，优先用**类名方法**与 **`.css()`**。  
- For dynamic content, use **event delegation** with **`.on(parent, child, handler)`**.  
- 对动态内容使用**事件委托**（**`.on(父, 子, 处理函数)`**）。  
- Create elements with **`$("<tag>")`** and **insert** with `.append()`/`.prepend()`/`.before()`/`.after()`.  
- 用 **`$("<tag>")`** 创建元素，并用 `.append()`/`.prepend()`/`.before()`/`.after()` 插入页面。  
- Practice **selector patterns** like `:nth-child(even)`, `:last-child`, `:contains()`, and `:has()`.  
- 练习 **选择器模式**：`:nth-child(even)`、`:last-child`、`:contains()`、`:has()` 等。  

---

## Notes 
## 注释

<details><summary>Where to put the script / 脚本写在哪</summary>

- A simple rule: put your `<script>` **at the end of `<body>`**, after the elements it references.  
- 简单做法：把 `<script>` 写在 **`<body>` 末尾**，保证脚本运行时目标元素已加载。  
- For complex apps, consider **`$(function(){ … })`** or a **module bundler**.  
- 更复杂的工程可考虑 **`$(function(){ … })`** 或**模块化打包**。  
</details>

---

[← Previous Lecture / 上一讲](./lecture30.md) · [Next Lecture / 下一讲 →](./lecture32.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

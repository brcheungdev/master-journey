[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 33: jQuery Ajax (`.load()` / `$.get()` / `$.post()`) and phpMyAdmin & SQL Basics  
# 第33讲：jQuery Ajax（`.load()` / `$.get()` / `$.post()`）与 phpMyAdmin & SQL 基础

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Dynamic Elements & Event Delegation (`.on()` on parent)](#dynamic-elements--event-delegation-on-on-parent)  
- 动态元素与事件委托（在父节点上 `.on()`）
- [DOM Replacement Review: `replaceWith` / `.text()` / `.html()`](#dom-replacement-review-replacewith--text--html)  
- DOM 替换回顾：`replaceWith` / `.text()` / `.html()`
- [Ajax with jQuery: `.load()` Basics](#ajax-with-jquery-load-basics)  
- 使用 jQuery 的 Ajax：`.load()` 基本用法
- [Frame‑like Content Swap via `.load()`](#frame-like-content-swap-via-load)  
- 用 `.load()` 实现“类 frame”内容切换
- [POST Data with `.load(url, data)`](#post-data-with-loadurl-data)  
- 使用 `.load(url, data)` 发送 POST 数据
- [Generic Ajax Methods: `$.get()` and `$.post()`](#generic-ajax-methods-get-and-post)  
- 通用 Ajax 方法：`$.get()` 与 `$.post()`
- [Practice: Rewrite `calc.html` Using `$.get`/`$.post`](#practice-rewrite-calchtml-using-getpost)  
- 练习：用 `$.get`/`$.post` 重写 `calc.html`
- [phpMyAdmin: Start Services & Open UI](#phpmyadmin-start-services--open-ui)  
- phpMyAdmin：启动服务并打开界面
- [Create `users` Table (id, userID, password, name)](#create-users-table-id-userid-password-name)  
- 创建 `users` 表（id、userID、password、name）
- [SQL You Must Know: INSERT / SELECT / DELETE / UPDATE](#sql-you-must-know-insert--select--delete--update)  
- 必会 SQL：INSERT / SELECT / DELETE / UPDATE
- [Import & Export (CSV)](#import--export-csv)  
- 导入与导出（CSV）
- [Confirmation Questions (Submit Required)](#confirmation-questions-submit-required)  
- 确认问题
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Dynamic Elements & Event Delegation (`.on()` on parent)  
## 动态元素与事件委托（在父节点上 `.on()`）

- When **elements are added dynamically**, bind the event to a **stable parent** and specify the **child selector** in `.on()`.  
- 当**目标元素是动态新增**时，在**稳定的父元素**上绑定事件，并在 `.on()` 中指定**子选择器**。  

```html
<ol id="fish">
  <li>はまち</li><li>たい</li>
</ol>
<script>
  // Works for existing and future <li> under #fish
  // 对 #fish 下现有与未来新增的 <li> 均有效
  $("#fish").on("click", "li", function(){ $(this).toggleClass("on"); });
</script>
```

---

## DOM Replacement Review: `replaceWith` / `.text()` / `.html()`  
## DOM 替换回顾：`replaceWith` / `.text()` / `.html()`

- **`$(T).replaceWith($(R))`** replaces the **entire element** `T` with new element `R`.  
- **`$(T).replaceWith($(R))`** 用元素 `R` **整体替换**元素 `T`。  
- **`$(T).text("...")`** replaces **inner text** (HTML **not parsed**).  
- **`$(T).text("...")`** 替换**内部纯文本**（HTML **不解析**）。  
- **`$(T).html("...")`** replaces **inner HTML** (tags **parsed** by browser).  
- **`$(T).html("...")`** 替换**内部 HTML**（标签会被浏览器**解析**）。  

```js
$("h1").replaceWith($("<h3>Heading 3</h3>"));
$("h1").text("お知らせ");
$("h1").html("お知らせ <h3>10 月 30 日</h3>");
```

---

## Ajax with jQuery: `.load()` Basics  
## 使用 jQuery 的 Ajax：`.load()` 基本用法

- **`$(T).load(url)`** fetches the content at **`url`** and **replaces `T`’s inner HTML** with the response.  
- **`$(T).load(url)`** 获取 **`url`** 的内容并**替换 `T` 的内部 HTML**。  

```html
<div id="target"></div>
<script>
  $("#target").load("page01.html"); // replace inner HTML of #target
  // 替换 #target 的内部 HTML
</script>
```

---

## Frame‑like Content Swap via `.load()`  
## 用 `.load()` 实现“类 frame”内容切换

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
    $("#target").load(url);
    return false; // prevent navigation / 阻止默认跳转
  });
});
</script>
```
- Intercept link clicks, **prevent default**, and swap the content **into `#target`**.  
- 拦截链接点击，**阻止默认**，并将内容**注入 `#target`**。  

---

## POST Data with `.load(url, data)`  
## 使用 `.load(url, data)` 发送 POST 数据

```js
$("#result").load("calc.php", { x: 25, y: 40 }); // sends POST body
// 以 POST 发送到 calc.php
```
- The **second argument** is an **object** encoded as **POST** (e.g., `x=25&y=40`).  
- **第二个参数**是**对象**，会编码为 **POST**（如 `x=25&y=40`）。  

---

## Generic Ajax Methods: `$.get()` and `$.post()`  
## 通用 Ajax 方法：`$.get()` 与 `$.post()`

```js
$.get("calc.php",  { x: 25, y: 40 }, function(data){ $("#result").html(data); });
$.post("calc.php", { x: 25, y: 40 }, function(data){ $("#result").html(data); });
```
- These are **not called on a jQuery object**; they **return data** to the **callback** on success.  
- 这两个方法**不是在 jQuery 对象上调用**；成功后将**数据**传给**回调函数**。  
- For **GET**, read values in PHP with **`$_GET`**; for **POST**, use **`$_POST`**.  
- **GET** 请求在 PHP 中用 **`$_GET`** 接收；**POST** 用 **`$_POST`**。  

---

## Practice: Rewrite `calc.html` Using `$.get`/`$.post`  
## 练习：用 `$.get`/`$.post` 重写 `calc.html`

```html
<input id="x" type="number"><input id="y" type="number">
<button id="btn">計算</button>
<div id="result"></div>
<script>
$("#btn").on("click", function(){
  $.post("calc.php", { x: $("#x").val(), y: $("#y").val() },
         function(data){ $("#result").html(data); });
  return false;
});
</script>
```
- Replace `.load()` with **`$.post()`** or **`$.get()`**; in the callback, **insert** the returned HTML into `#result`.  
- 用 **`$.post()`** 或 **`$.get()`** 替换 `.load()`；在回调中将返回的 HTML **插入**到 `#result`。  

---

## phpMyAdmin: Start Services & Open UI  
## phpMyAdmin：启动服务并打开界面

- In **XAMPP Control Panel**, start **Apache** and **MySQL**, then open **`http://localhost/phpmyadmin/`**.  
- 在 **XAMPP 控制面板**启动 **Apache** 与 **MySQL** 后，访问 **`http://localhost/phpmyadmin/`**。  

---

## Create `users` Table (id, userID, password, name)  
## 创建 `users` 表（id、userID、password、name）

- In database **`test`**, create table **`users`** with **4 columns**: `id`, `userID`, `password`, `name`.  
- 在 **`test`** 数据库中创建 **`users`** 表，含 **4 列**：`id`、`userID`、`password`、`name`。  
- Set `id` as **PRIMARY KEY** and **AUTO_INCREMENT**; default collation **`utf8_general_ci`**.  
- 设定 `id` 为 **主键（PRIMARY KEY）**且**自增（AUTO_INCREMENT）**；默认整理顺序 **`utf8_general_ci`**。  

```sql
-- Example structure (one possible choice) / 示例结构（可按需调整）
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  userID VARCHAR(32) NOT NULL,
  password VARCHAR(64) NOT NULL,
  name VARCHAR(64) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
```

---

## SQL You Must Know: INSERT / SELECT / DELETE / UPDATE  
## 必会 SQL：INSERT / SELECT / DELETE / UPDATE

```sql
-- INSERT one record (NULL for AUTO_INCREMENT) / 插入一条记录（自增列用 NULL）
INSERT INTO users VALUES (NULL, 'user1', 'pass1', '山田');
INSERT INTO users VALUES (NULL, 'user2', 'pass2', '田中');
INSERT INTO users VALUES (NULL, 'user3', 'pass3', '佐藤');

-- SELECT all or specific columns / 选择所有或特定列
SELECT * FROM users;
SELECT id, userID, name FROM users;

-- SELECT with conditions / 带条件的选择
SELECT * FROM users WHERE id = 1;
SELECT * FROM users WHERE userID = 'user3';
SELECT * FROM users WHERE userID LIKE 'user%'; -- begins with 'user' / 以 'user' 开头

-- DELETE with conditions (ALWAYS give WHERE!) / 删除（务必带 WHERE!）
DELETE FROM users WHERE id = 2;

-- UPDATE with conditions (ALWAYS give WHERE!) / 更新（务必带 WHERE!）
UPDATE users SET userID = 'u1' WHERE id = 1;
UPDATE users SET password = 'p3', name = '鈴木' WHERE id = 3;
```

- **`INSERT`** adds rows; **`SELECT`** retrieves rows (optionally with **`WHERE`**/**`LIKE`**); **`DELETE`** removes rows; **`UPDATE`** changes column values.  
- **`INSERT`** 插入行；**`SELECT`** 检索行（可配 **`WHERE`**/**`LIKE`**）；**`DELETE`** 删除行；**`UPDATE`** 修改列值。  
- **Warning**: Missing **`WHERE`** on **`DELETE`** or **`UPDATE`** affects **all rows**.  
- **警告**：在 **`DELETE`** 与 **`UPDATE`** 上**缺少 `WHERE`** 会影响**整表所有行**。  

---

## Import & Export (CSV)  
## 导入与导出（CSV）

- phpMyAdmin can **export** a table to **CSV** and **import** CSV back to populate the table.  
- phpMyAdmin 支持将表**导出**为 **CSV**，并从 CSV **导入**以填充表数据。  

---

## Confirmation Questions 
## 确认问题

- **Q1**: Select **all columns** for the row where `userID` equals a **specific value** (e.g., `tcha238`).  
- **问题1**：选择 `userID` 为**特定值**（例：`tcha238`）的记录**全部列**。  

```sql
SELECT * FROM users WHERE userID = 'tcha238';
```

- **Q2**: Select **only the `id` column** for rows where `name` **starts with a letter**.  
- **问题2**：选择 `name` **以某个字母开头**的记录的 **`id` 列**。  

```sql
SELECT id FROM users WHERE name LIKE 'A%'; -- example for letter 'A' / 以字母 A 开头示例
```

- **Q3**: **Update** the `password` for the row specified by a particular `id`.  
- **问题3**：将指定 `id` 的记录的 `password` **更新**为新值。  

```sql
UPDATE users SET password = 'newpass' WHERE id = 5;
```

- **Q4**: **Delete** the row specified by a particular `userID`.  
- **问题4**：**删除** `userID` 为特定值的记录。  

```sql
DELETE FROM users WHERE userID = 'user3';
```

---

## Quick Checklist  
## 快速清单

- Use **delegated `.on()`** for **dynamic elements**.  
- 对**动态元素**使用**委托式 `.on()`**。  
- Choose **replacement level** appropriately: `replaceWith` vs `.html()` vs `.text()`.  
- 合理选择**替换级别**：`replaceWith` 与 `.html()` 与 `.text()`。  
- For Ajax: `.load(url)` for quick **inner HTML swap**; `$.get`/`$.post` for **generic requests**.  
- Ajax：用 `.load(url)` 快速**替换内部**；用 `$.get`/`$.post` 发起**通用请求**。  
- In phpMyAdmin, create **`users`** with **`id` AUTO_INCREMENT PRIMARY KEY**, **collation `utf8_general_ci`**.  
- 在 phpMyAdmin 中创建 **`users`** 表（**`id` 自增主键**，**`utf8_general_ci`** 整理）。  
- Practice **INSERT/SELECT/DELETE/UPDATE**; never forget **`WHERE`** on destructive queries.  
- 练习 **INSERT/SELECT/DELETE/UPDATE**；破坏性语句务必带 **`WHERE`**。  

---

## Notes
## 注释

<details><summary>Manuals / 手册</summary>

- MySQL Reference Manual (5.6/8.0) and MariaDB docs provide the **SQL syntax** reference.  
- MySQL 参考手册（5.6/8.0）与 MariaDB 文档提供**SQL 语法**参考。  
</details>

---

[← Previous Lecture / 上一讲](./lecture32.md) · [Next Lecture / 下一讲 →](./lecture34.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 27: PHP Basics — Environment (XAMPP), HTML/CSS Review, Forms, GET/POST, Variables & Arrays  
# 第27讲：PHP 基础 —— 开发环境（XAMPP）、HTML/CSS 复习、表单、GET/POST、变量与数组

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Course Overview & Tools](#course-overview--tools)  
- 课程概览与工具
- [XAMPP Environment Setup](#xampp-environment-setup)  
- XAMPP 开发环境搭建
- [Project Folder Structure & Access via `http://localhost/`](#project-folder-structure--access-via-httplocalhost)  
- 工程目录结构与通过 `http://localhost/` 访问
- [HTML Review: Template, Tags & Attributes](#html-review-template-tags--attributes)  
- HTML 复习：模板、标签与属性
- [Exercise (HTML Only): Login Form & Result Pages](#exercise-html-only-login-form--result-pages)  
- 练习（仅 HTML）：登录表单与结果页面
- [CSS Review: Selectors & Styling the Form](#css-review-selectors--styling-the-form)  
- CSS 复习：选择器与表单样式
- [PHP Overview & Execution Model](#php-overview--execution-model)  
- PHP 概述与执行模型
- [Run PHP via Apache: `.php` under `htdocs` (Not `file:///`)](#run-php-via-apache-php-under-htdocs-not-file)  
- 通过 Apache 运行 PHP：`htdocs` 下的 `.php`（不是 `file:///`）
- [`phpinfo()` and Embedded PHP](#phpinfo-and-embedded-php)  
- `phpinfo()` 与在 HTML 中嵌入 PHP
- [Variables & String Interpolation](#variables--string-interpolation)  
- 变量与字符串插值
- [Arrays: Indexed & Associative](#arrays-indexed--associative)  
- 数组：索引数组与关联数组
- [Useful Library Functions: `rand()` and `getdate()`](#useful-library-functions-rand-and-getdate)  
- 常用库函数：`rand()` 与 `getdate()`
- [Browser → Server Data Flow: GET vs POST](#browser--server-data-flow-get-vs-post)  
- 浏览器→服务器数据流：GET 与 POST
- [Receive Data in PHP: `$_GET` / `$_POST` + Practice](#receive-data-in-php-$_get--$_post--practice)  
- 在 PHP 中接收数据：`$_GET` / `$_POST` + 实践
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Course Overview & Tools  
## 课程概览与工具

- Course focus: **Web Programming III** — building **database‑centric** web apps (blog, shared calendar, online catalog).  
- 课程聚焦：**Web 编程 III** —— 构建**以数据库为中心**的 Web 应用（博客、共享日历、在线目录）。  
- Languages: **HTML, CSS, JavaScript (jQuery), PHP, SQL**; Software: **XAMPP**, a modern **text editor** (VS Code / Notepad++ / Atom / Sakura).  
- 使用语言：**HTML、CSS、JavaScript（jQuery）、PHP、SQL**；软件：**XAMPP** 与现代**文本编辑器**（VS Code / Notepad++ / Atom / 樱花编辑器）。  
- Grading: **in‑class tasks 40%**, **final project + presentation 60%**.  
- 成绩构成：**课内作业 40%**、**期末项目与展示 60%**。  

---

## XAMPP Environment Setup  
## XAMPP 开发环境搭建

- XAMPP bundles **Apache (Web Server)** + **MySQL** (and more); install under **`C:\xampp\`**.  
- XAMPP 打包了 **Apache（Web 服务器）**与 **MySQL**（及其他组件）；安装路径建议 **`C:\xampp\`**。  
- Use **XAMPP Control Panel** (`xampp_control.exe`) to **start/stop** services.  
- 使用 **XAMPP 控制面板**（`xampp_control.exe`）来**启动/停止**服务。  
- The web root is **`C:\xampp\htdocs\`**.  
- Web 根目录为 **`C:\xampp\htdocs\`**。  

---

## Project Folder Structure & Access via `http://localhost/`  
## 工程目录结构与通过 `http://localhost/` 访问

- Create folder **`C:\xampp\htdocs\<student-id>\<date>/`**; store all **HTML/PHP** for that class date.  
- 在 **`C:\xampp\htdocs\<学籍番号>\<日期>/`** 下创建文件夹；将当次课的 **HTML/PHP** 文件放入。  
- Access files **through Apache**: `http://localhost/<student-id>/<date>/<file>`.  
- **通过 Apache** 访问：`http://localhost/<学籍番号>/<日期>/<文件名>`。  
- **Do not** open PHP as local files (`file:///C:/...`) — **server must execute** them.  
- **不要**以本地文件方式打开 PHP（`file:///C:/...`）——必须让**服务器执行**。  

---

## HTML Review: Template, Tags & Attributes  
## HTML 复习：模板、标签与属性

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My HomePage</title>
</head>
<body>
  <h1>はじめに</h1>
  <p>この Web サイトは ...</p>
</body>
</html>
```
- Always **close opened tags**; attributes use **`name="value"`**; save files in **UTF‑8**.  
- **标签必须成对闭合**；属性用 **`name="value"`**；以 **UTF‑8** 编码保存文件。  

---

## Exercise (HTML Only): Login Form & Result Pages  
## 练习（仅 HTML）：登录表单与结果页面

- Build a **login form** with `<form>`, `<input>`, `<button>`; lay out with a **`<table>`**.  
- 用 `<form>`、`<input>`、`<button>` 制作**登录表单**；用 **`<table>`** 排版。  
- Prepare **`success.html`** and **`failure.html`** to display messages.  
- 准备 **`success.html`** 与 **`failure.html`** 用于显示成功/失败信息。  

```html
<!-- login.html -->
<form>
  <table>
    <tr><td>user ID：</td><td><input type="text" name="userID"></td></tr>
    <tr><td>password：</td><td><input type="password" name="password"></td></tr>
    <tr><td colspan="2" align="right"><button>ログイン</button></td></tr>
  </table>
</form>
```

---

## CSS Review: Selectors & Styling the Form  
## CSS 复习：选择器与表单样式

- Where to write CSS: **inline `style`**, **`<style>` in `<head>`**, or **external** `.css` via `<link>`.  
- CSS 的书写位置：**行内 `style`**、`<head>` 内的 **`<style>`**、或 **外部** `.css` 文件通过 `<link>` 引入。  
- Practice: **border** around the form, align the **Login** button to the **right**, set **background colors** for success (`lightblue`) and failure (`yellow`).  
- 练习：为表单加**边框**，将“登录”按钮**右对齐**，设置成功（`lightblue`）与失败（`yellow`）的**背景色**。  

---

## PHP Overview & Execution Model  
## PHP 概述与执行模型

- PHP is a **server‑side scripting language** for **dynamic pages**; **free**, **multi‑platform**, **OO since PHP 5**, **current major 8.x**.  
- PHP 是用于**动态页面**的**服务器端脚本语言**；**免费**、**跨平台**，**PHP 5 起支持面向对象**，当前主流为 **8.x**。  
- **HTML vs PHP**: HTML files are **sent as is**; PHP scripts are **executed on the server**, and **output HTML**.  
- **HTML 与 PHP 的区别**：HTML 文件**原样发送**；PHP 脚本在**服务器执行**并**输出 HTML**。  

```
HTML request / HTML 请求 → send file content  
→ 直接发送文件内容

PHP request / PHP 请求 → run script → send execution result  
→ 运行脚本后发送执行结果
```

---

## Run PHP via Apache: `.php` under `htdocs` (Not `file://`)  
## 通过 Apache 运行 PHP：`htdocs` 下的 `.php`（不是 `file://`）

- Save as **`.php`**, e.g., `C:\xampp\htdocs\<id>\<date>\test.php`.  
- 以 **`.php`** 扩展名保存，例如 `C:\xampp\htdocs\<学籍番号>\<日期>\test.php`。  
- Start **Apache** in XAMPP; open `http://localhost/<id>/<date>/test.php`.  
- 在 XAMPP 中**启动 Apache**；访问 `http://localhost/<学籍番号>/<日期>/test.php`。  

---

## `phpinfo()` and Embedded PHP  
## `phpinfo()` 与在 HTML 中嵌入 PHP

```php
<?php phpinfo(); ?>
```
- `phpinfo()` prints the **runtime environment**.  
- `phpinfo()` 输出 **PHP 运行环境**信息。  

```php
<!DOCTYPE html>
<html><body>
  <?php echo("<h1>おはよう，PHP！</h1>"); ?>
</body></html>
```
- Use **`<?php ... ?>`** blocks inside HTML; **`echo()`** outputs HTML.  
- 在 HTML 中使用 **`<?php ... ?>`** 代码块；**`echo()`** 用于输出 HTML。  
- **Error demo**: misspelling `echo` (e.g., `eco`) causes **“undefined function”**.  
- **错误示例**：将 `echo` 拼错（如 `eco`）会导致 **“未定义函数”** 错误。  

---

## Variables & String Interpolation  
## 变量与字符串插值

```php
<?php
  $message = "どうも，PHP！";
  echo("<h1>{$message}</h1>");
  echo("<h1>" . $message . "</h1>");
?>
```
- Variables **start with `$`**, are **case‑sensitive**, **no type declaration** needed; use **`{$var}`** in strings or **`.`** for concatenation.  
- 变量以 **`$`** 开头，**区分大小写**，**无需类型声明**；字符串中可用 **`{$var}`** 或使用 **`.`** 进行拼接。  

---

## Arrays: Indexed & Associative  
## 数组：索引数组与关联数组

```php
<?php
  // indexed
  $kcgi = array("百万遍","京都駅前","東京","札幌");
  echo($kcgi[0]);
  // associative
  $campus = array("h"=>"百万遍","k"=>"京都駅前","t"=>"東京","s"=>"札幌");
  echo($campus["k"]);
?>
```
- **Indexed arrays** use **numeric indices**; **associative arrays** use **string keys**.  
- **索引数组**使用**数字下标**；**关联数组**使用**字符串键**。  
- Elements can be **appended or set at arbitrary keys**.  
- 元素可**追加**或在**任意键**上设置。  

---

## Useful Library Functions: `rand()` and `getdate()`  
## 常用库函数：`rand()` 与 `getdate()`

```php
<?php
  // random campus 0..3
  $kcgi = array("百万遍","京都駅前","東京","札幌");
  echo($kcgi[rand(0, 3)]);
  // current Y-M-D from getdate()
  $now = getdate();
  echo($now['year'] . "年" . $now['mon'] . "月" . $now['mday'] . "日");
?>
```
- `rand(min, max)` returns a **random integer**; `getdate()` returns a **date/time associative array** (`year/mon/mday`).  
- `rand(min, max)` 返回**随机整数**；`getdate()` 返回**日期时间关联数组**（`year/mon/mday`）。  

---

## Browser → Server Data Flow: GET vs POST  
## 浏览器→服务器数据流：GET 与 POST

- **GET**: data in **URL query string** `?name=value&...`; not suited for **large or binary** data.  
- **GET**：将数据放在 **URL 查询串** `?name=value&...`；不适合**大量或二进制**数据。  
- **POST**: form submits data in **request body**; typical for **login** and **file uploads**.  
- **POST**：表单把数据放在**请求体**；常用于**登录**与**文件上传**。  

```html
<!-- GET example -->
<form method="GET" action="check.php"> ... </form>
<!-- POST example -->
<form method="POST" action="check.php"> ... </form>
```

---

## Receive Data in PHP: `$_GET` / `$_POST` + Practice  
## 在 PHP 中接收数据：`$_GET` / `$_POST` + 实践

```php
<!-- login.html -->
<form method="POST" action="check.php">
  <input name="userID">
  <input name="password" type="password">
  <input type="submit" value="送信">
</form>
```

```php
<?php // check.php
  $u = $_POST["userID"];
  $p = $_POST["password"];
  echo "あなたのユーザIDは {$u} で，パスワードは {$p} ですね。";
?>
```
- Use **`$_POST["name"]`** (for POST) or **`$_GET["name"]`** (for GET) to **receive values**.  
- 使用 **`$_POST["name"]`**（POST）或 **`$_GET["name"]`**（GET）来**接收表单值**。  
- Files live under **`C:\xampp\htdocs\<id>\<date>\`**; access via **`http://localhost/...`**.  
- 将文件放在 **`C:\xampp\htdocs\<学籍番号>\<日期>\`**；通过 **`http://localhost/...`** 访问。  

---

## Quick Checklist  
## 快速清单

- Start **XAMPP Apache** → visit files via **`http://localhost/...`**.  
- 先启动 **XAMPP 的 Apache** → 通过 **`http://localhost/...`** 访问文件。  
- Save PHP with **`.php`** extension; avoid **`file:///`**.  
- PHP 文件须以 **`.php`** 扩展名保存；避免 **`file:///`** 访问。  
- Use **UTF‑8**, close all tags, and use `name="value"` attributes.  
- 使用 **UTF‑8**，标签闭合完整，属性采用 `name="value"` 书写。  
- Practice **login.html / success.html / failure.html / check.php**; POST values and **echo** them back.  
- 练习 **login.html / success.html / failure.html / check.php**；使用 POST 提交并 **echo** 回显。  
- Arrays: choose **indexed** or **associative** appropriately; try **`rand()`/`getdate()`**.  
- 数组：按需选择**索引**或**关联**；练习 **`rand()`/`getdate()`**。  

---

## Notes
## 注释

<details><summary>Security note / 安全提示</summary>
- Never print **plain passwords** in real apps; this is for **learning only**.  
- 在真实应用中**不要回显明文密码**；本示例**仅用于学习**。  
- Prefer **`filter_input()`** for validation and **password hashing** for auth.  
- 实际开发请使用 **`filter_input()`** 做校验，并对密码进行**散列存储**。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture26.md) · [Next Lecture / 下一讲 →](./lecture28.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

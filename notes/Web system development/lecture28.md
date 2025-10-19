[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 28: PHP Control Flow — Conditions, Logical Operators, Loops (`for`/`foreach`), and Login Validation (GET/POST)  
# 第28讲：PHP 控制流——条件判断、逻辑运算、循环（`for`/`foreach`）与登录校验（GET/POST）

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Troubleshooting XAMPP & Running PHP via Apache](#troubleshooting-xampp--running-php-via-apache)  
- XAMPP 故障排查与通过 Apache 运行 PHP
- [Recap: HTML vs PHP Request/Response](#recap-html-vs-php-requestresponse)  
- 回顾：HTML 与 PHP 的请求/响应差异
- [Variables Recap](#variables-recap)  
- 变量回顾
- [Arrays Recap: Indexed & Associative](#arrays-recap-indexed--associative)  
- 数组回顾：索引与关联
- [Random & Date: `rand()` / `getdate()`](#random--date-rand--getdate)  
- 随机与日期：`rand()` / `getdate()`
- [Browser → Server: GET vs POST](#browser--server-get-vs-post)  
- 浏览器 → 服务器：GET 与 POST
- [Conditions: `if` / `if…else` / `if…elseif…else`](#conditions-if--ifelse--ifelseifelse)  
- 条件语句：`if` / `if…else` / `if…elseif…else`
- [Operators: Comparison & Logic (`==` `!=` `&&` `||` `!`)](#operators-comparison--logic----)  
- 运算符：比较与逻辑（`==` `!=` `&&` `||` `!`）
- [Printing HTML in PHP Blocks (Alternate Syntax)](#printing-html-in-php-blocks-alternate-syntax)  
- 在 PHP 代码块中输出 HTML（替代语法）
- [Looping Arrays: `for` + `count()` and `foreach` (values / `key => value`)](#looping-arrays-for--count-and-foreach-values--key--value)  
- 遍历数组：`for` + `count()` 与 `foreach`（值 / `key => value`）
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Troubleshooting XAMPP & Running PHP via Apache  
## XAMPP 故障排查与通过 Apache 运行 PHP

- If **XAMPP won’t start**, uninstall **older MySQL/Apache/XAMPP**, back up your HTML files, and retry.  
- 若 **XAMPP 无法启动**，请先卸载**旧版本的 MySQL/Apache/XAMPP**，备份 HTML 文件后再重装。  fileciteturn27file0
- Start **`xampp-control.exe`** and click **Start** for **Apache** (and MySQL when needed).  
- 打开 **`xampp-control.exe`**，点击 **Start** 启动 **Apache**（需要时启动 MySQL）。  fileciteturn27file0
- Run PHP **through Apache**: put files under **`C:\xampp\htdocs\<id>\<date>\`** and open via **`http://localhost/<id>/<date>/<file>.php`** (not `file:///`).  
- 通过 **Apache** 运行 PHP：将文件置于 **`C:\xampp\htdocs\<学籍番号>\<日期>\`**，通过 **`http://localhost/<学籍番号>/<日期>/<文件>.php`** 访问（不要用 `file:///`）。  fileciteturn27file0

---

## Recap: HTML vs PHP Request/Response  
## 回顾：HTML 与 PHP 的请求/响应差异

```
HTML → (server sends file as-is) → Browser renders
PHP  → (server executes script → result HTML) → Browser renders
HTML →（服务器直接发送文件）→ 浏览器渲染
PHP  →（服务器先执行脚本→输出 HTML）→ 浏览器渲染
```
- PHP pages must be **executed on server**; the browser receives the **execution result (HTML)**.  
- PHP 页面必须**在服务器执行**；浏览器接收的是**执行结果（HTML）**。  fileciteturn27file0

---

## Variables Recap  
## 变量回顾

```php
<?php
  $message = "おはよう，PHP！";
  echo("<h1>{$message}</h1>");
  // or: echo("<h1>" . $message . "</h1>");
?>
```
- Variable names **start with `$`**, are **case‑sensitive**, no type declaration; use **`{$var}`** or **`.`** for concatenation.  
- 变量名以 **`$`** 开头、**区分大小写**、无需类型声明；字符串中可用 **`{$var}`** 或 **`.`** 拼接。  fileciteturn27file0

---

## Arrays Recap: Indexed & Associative  
## 数组回顾：索引与关联

```php
<?php
  // indexed
  $kcgi = array("百万遍","京都駅前","東京","札幌");
  echo $kcgi[0];

  // associative
  $campus = array("h"=>"百万遍","k"=>"京都駅前","t"=>"東京","s"=>"札幌");
  echo $campus["k"];
?>
```
- Indexed arrays use **numeric indices**; associative arrays use **string keys**; both can be **appended/assigned** freely.  
- 索引数组使用**数字下标**；关联数组使用**字符串键**；两者均可**任意追加/赋值**。  fileciteturn27file0

---

## Random & Date: `rand()` / `getdate()`  
## 随机与日期：`rand()` / `getdate()`

```php
<?php
  $kcgi = array("百万遍","京都駅前","東京","札幌");
  echo $kcgi[rand(0,3)];          // random element
  $now = getdate();               // ['year','mon','mday']
  echo "{$now['year']}年{$now['mon']}月{$now['mday']}日";
?>
```
- **`rand(min, max)`** returns a random integer; **`getdate()`** returns a **date/time associative array**.  
- **`rand(min, max)`** 返回随机整数；**`getdate()`** 返回**日期/时间关联数组**。  fileciteturn27file0

---

## Browser → Server: GET vs POST  
## 浏览器 → 服务器：GET 与 POST

```html
<!-- GET puts data in URL query string -->
<form method="GET"  action="check.php"> … </form>
<!-- POST puts data in request body -->
<form method="POST" action="check.php"> … </form>
```
- **GET** encodes data in **`?name=value&...`** (not for large/binary data); **POST** sends in **request body** (typical for login/upload).  
- **GET** 将数据写入 **`?name=value&...`**（不适合大/二进制数据）；**POST** 在**请求体**中发送（常用于登录/上传）。  fileciteturn27file0

---

## Conditions: `if` / `if…else` / `if…elseif…else`  
## 条件语句：`if` / `if…else` / `if…elseif…else`

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
- Use **`if`**, **`if…else`**, or **`if…elseif…else`** depending on the number of branches.  
- 根据分支数量选择 **`if`**、**`if…else`** 或 **`if…elseif…else`**。  fileciteturn27file0

---

## Operators: Comparison & Logic (`==` `!=` `&&` `||` `!`)  
## 运算符：比较与逻辑（`==` `!=` `&&` `||` `!`）

```php
<?php
  $val = 10; $name = "abc";
  if ($val == 10 && $name == "abc") { echo "AND 成立"; }  // both
  if ($val == 10 || $name == "abc") { echo "OR 成立"; }   // either
  if (!($val == 20))                 { echo "NOT 成立"; }  // negate
  // Note:  !($val == 10)  is same as  $val != 10
?>
```
- Combine conditions with **`&&` (AND)** and **`||` (OR)**; **`!`** negates a condition.  
- 用 **`&&`（且）**与 **`||`（或）**组合条件；**`!`** 取反条件。  fileciteturn27file0

---

## Printing HTML in PHP Blocks (Alternate Syntax)  
## 在 PHP 代码块中输出 HTML（替代语法）

```php
<?php if ($ok) { ?>
  <p>OK!</p>
<?php } ?>

<?php if ($ok): ?>
  <p>OK!</p>
<?php endif; ?>
```
- Inside `if`/`else` blocks, you can **echo tags**, or use the **alternate colon syntax** (`if: … endif;`) to keep markup clean.  
- 在 `if`/`else` 代码块中可直接**输出标签**，也可用 **冒号语法**（`if: … endif;`）让标记更清晰。  fileciteturn27file0

---

## Looping Arrays: `for` + `count()` and `foreach` (values / `key => value`)  
## 遍历数组：`for` + `count()` 与 `foreach`（值 / `key => value`）

```php
<?php
  $a = array("京都","札幌","東京");
  // for + count()
  for ($i = 0; $i < count($a); $i++) {
    echo $a[$i] . "<br>";
  }
  // foreach: values
  foreach ($a as $v) {
    echo $v . "<br>";
  }

  // foreach: associative key => value
  $m = array("k"=>"京都","s"=>"札幌","t"=>"東京");
  foreach ($m as $k => $v) {
    echo $k . " => " . $v . "<br>";
  }
?>
```
- **`count($arr)`** is analogous to JS **`arr.length`**; **`foreach`** iterates **values**, or **`key => value`** for associative arrays.  
- **`count($arr)`** 类似 JS 的 **`arr.length`**；**`foreach`** 可遍历**值**，或用于**`key => value`** 的关联数组。  fileciteturn27file0

---

## Practice Tasks  
## 练习任务

**A — Simple login check (single ID/password)**  
**A —— 简单登录校验（单一学籍番号）**

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
$u = $_POST["userID"]  ?? "";
$p = $_POST["password"]?? "";
if ($u === "自分の学生番号" && $p === "自分的学生番号") {
  echo "成功 / Success";
} else {
  echo "失败 / Fail";
}
?>
```
- Use **POST** and compare both fields with your **student ID**.  
- 使用 **POST**，并将两项与自己的**学籍番号**比较。  fileciteturn27file0

**B — Validate against a predefined users list (`foreach`)**  
**B —— 用预置用户列表进行校验（`foreach`）**

```php
<?php // check2.php
$users = array(
  array("userID"=>"u1","password"=>"pass1"),
  array("userID"=>"u2","password"=>"pass2"),
  array("userID"=>"u3","password"=>"pass3"),
);
$u = $_POST["userID"]  ?? "";
$p = $_POST["password"]?? "";
$ok = false;
foreach ($users as $user) {
  if ($user["userID"] === $u && $user["password"] === $p) { $ok = true; break; }
}
echo $ok ? "成功 / Success" : "失败 / Fail";
```
- Iterate the **array of user records** with **`foreach`**; check whether a **matching pair** exists.  
- 用 **`foreach`** 遍历**用户记录数组**；判断是否存在**匹配的一对**。  fileciteturn27file0

---

## Quick Checklist  
## 快速清单

- Run **PHP via Apache** at `http://localhost/...`; store in **`htdocs`**.  
- 通过 `http://localhost/...` **经由 Apache 运行 PHP**；文件需存放在 **`htdocs`**。  fileciteturn27file0
- Prefer **POST** for login; receive via **`$_POST["name"]`**.  
- 登录表单建议使用 **POST**；用 **`$_POST["name"]`** 接收。  fileciteturn27file0
- Use **`if / elseif / else`** and **`&& / || / !`** to express logic clearly.  
- 使用 **`if / elseif / else`** 与 **`&& / || / !`** 清晰表达逻辑。  fileciteturn27file0
- Loop arrays with **`for(count())`** or **`foreach`** (`key => value` for associative).  
- 遍历数组可用 **`for(count())`** 或 **`foreach`**（关联数组用 `key => value`）。  fileciteturn27file0

---

## Notes
## 注释

<details><summary>Security note / 安全提示</summary>

- Do **not echo raw passwords** in real apps; hash them and use **secure comparisons**.  
- 真实应用中**不要回显明文密码**；应进行**哈希存储**并使用安全比较。  
- Validate inputs (e.g., `filter_input()` or libraries) and **escape outputs** when mixing HTML.  
- 校验输入（如 `filter_input()` 或库），并在输出 HTML 时**转义**。  
</details>

---

[← Previous Lecture / 上一讲](./lecture27.md) · [Next Lecture / 下一讲 →](./lecture29.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

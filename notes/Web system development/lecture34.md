 [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 34: PHP PDO — Connect to MySQL, `exec/query/fetch`, Login Authentication, CRUD, and Reusable Connection  
# 第34讲：PHP PDO —— 连接 MySQL、`exec/query/fetch`、登录认证、CRUD 与连接复用

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Why PDO (vs `mysql_*` / `mysqli_*`)](#why-pdo-vs-mysql_---mysqli_)  
- 为什么使用 PDO（对比 `mysql_*` / `mysqli_*`）
- [Start Services & phpMyAdmin](#start-services--phpmyadmin)  
- 启动服务与进入 phpMyAdmin
- [Create Database Table `users`](#create-database-table-users)  
- 创建数据库表 `users`
- [Connect via PDO: DSN, Charset, Port, Try/Catch](#connect-via-pdo-dsn-charset-port-trycatch)  
- 通过 PDO 连接：DSN、字符集、端口、异常处理
- [Execute SQL: `exec` (UPDATE/INSERT/DELETE) and `query` (SELECT)](#execute-sql-exec-updateinsertdelete-and-query-select)  
- 执行 SQL：`exec`（更改类）与 `query`（查询）
- [Fetch Records: `fetch()` and `foreach` over `PDOStatement`](#fetch-records-fetch-and-foreach-over-pdostatement)  
- 读取记录：`fetch()` 与遍历 `PDOStatement`
- [Login Authentication with PDO (`check.php`)](#login-authentication-with-pdo-checkphp)  
- 使用 PDO 实现登录认证（`check.php`）
- [Share Connection with `include('connect.php')`](#share-connection-with-includeconnectphp)  
- 用 `include('connect.php')` 共享连接
- [CRUD Mini‑Scripts: `create.php` / `read.php` / `update.php` / `delete.php`](#crud-mini-scripts-createphp--readphp--updatephp--deletephp)  
- CRUD 小脚本：`create.php` / `read.php` / `update.php` / `delete.php`
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释
---

## Why PDO (vs `mysql_*` / `mysqli_*`)  
## 为什么使用 PDO（对比 `mysql_*` / `mysqli_*`）

- **PDO = PHP Data Objects**, a **database abstraction** layer; easy to switch to **other DB engines**.  
- **PDO = PHP Data Objects**，一种**数据库抽象层**；可较容易切换到**其他数据库引擎**。  
- **`mysql_*` functions are removed since PHP 7**; **`mysqli_*`** exists, but this course uses **PDO**.  
- **`mysql_*` 函数在 PHP 7 起被移除**；虽有 **`mysqli_*`**，但本课采用 **PDO**。  fileciteturn33file0

---

## Start Services & phpMyAdmin  
## 启动服务与进入 phpMyAdmin

- In **XAMPP Control Panel**, start **Apache** and **MySQL**, then open **`http://localhost/phpmyadmin/`**.  
- 在 **XAMPP 控制面板**中启动 **Apache** 与 **MySQL**，然后访问 **`http://localhost/phpmyadmin/`**。  fileciteturn33file0

---

## Create Database Table `users`  
## 创建数据库表 `users`

- Database **`test`** → create table **`users`** with columns: `id`, `userID`, `password`, `name`.  
- 数据库 **`test`** → 新建表 **`users`**，列：`id`、`userID`、`password`、`name`。  
- Set `id` as **PRIMARY KEY** and **AUTO_INCREMENT**; set collation **`utf8_general_ci`**.  
- 将 `id` 设为 **主键**且 **AUTO_INCREMENT**；整理顺序设为 **`utf8_general_ci`**。  

```sql
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  userID VARCHAR(12) NOT NULL,
  password VARCHAR(12) NOT NULL,
  name VARCHAR(24) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
```
- phpMyAdmin supports **CSV export/import** for the table.  
- phpMyAdmin 支持对该表进行 **CSV 导出/导入**。  fileciteturn33file0

---

## Connect via PDO: DSN, Charset, Port, Try/Catch  
## 通过 PDO 连接：DSN、字符集、端口、异常处理

```php
<?php
// connect.php
$conn = null;
try{
  // DSN with charset (UTF-8) / 带字符集（UTF-8）的 DSN
  $conn = new PDO("mysql:host=localhost;dbname=test;charset=utf8;", "root", "YOUR_PASSWORD");
  // If MySQL listens on 13306, add ";port=13306"
  // 若 MySQL 端口为 13306，追加 ";port=13306"
}catch(PDOException $e){
  die($e->getMessage()); // stop on failure / 失败时输出并终止
}
```
- Create a **PDO connection object** with DSN `mysql:host=…;dbname=…;charset=utf8` (optionally `;port=13306`).  
- 使用 DSN `mysql:host=…;dbname=…;charset=utf8`（可选 `;port=13306`）创建 **PDO 连接对象**。  
- Close by setting `$conn = null;`.  
- 结束时设 `$conn = null;` 以关闭连接。  fileciteturn33file0

---

## Execute SQL: `exec` (UPDATE/INSERT/DELETE) and `query` (SELECT)  
## 执行 SQL：`exec`（更改类）与 `query`（查询）

```php
// UPDATE/INSERT/DELETE
$updated = $conn->exec("UPDATE users SET name='鈴木' WHERE id=3"); // returns affected rows / 返回受影响行数

// SELECT
$result  = $conn->query("SELECT id,userID,name FROM users");     // returns PDOStatement / 返回 PDOStatement
```
- **`exec()`** runs **update-type** SQL and returns **affected row count**.  
- **`exec()`** 执行**更改类** SQL 并返回**受影响行数**。  
- **`query()`** runs **`SELECT`** and returns a **`PDOStatement`**.  
- **`query()`** 执行 **`SELECT`** 并返回 **`PDOStatement`**。  fileciteturn33file0

---

## Fetch Records: `fetch()` and `foreach` over `PDOStatement`  
## 读取记录：`fetch()` 与遍历 `PDOStatement`

```php
$r = $result->fetch();       // get the first record / 取第一条记录
echo $r['id'] . " : " . $r['userID'] . " : " . $r['name'];

foreach ($result as $row) {  // iterate all rows / 逐行遍历
  echo $row['id'] . " => " . $row['name'] . "<br>";
}
```
- Default **fetch style** allows both **numeric indices** and **column-name keys**.  
- 默认 **fetch** 既可用**数字下标**也可用**列名**访问。  fileciteturn33file0

---

## Login Authentication with PDO (`check.php`)  
## 使用 PDO 实现登录认证（`check.php`）

```php
<?php // check.php (basic version for class demo / 课堂演示基础版)
$u = $_POST['userID']; $p = $_POST['password'];
require_once("connect.php");              // create $conn / 生成 $conn
$result = $conn->query("SELECT * FROM users WHERE userID='{$u}'");
$r = $result->fetch();                    // user record / 用户记录（或 false）
$conn = null;

// Compare submitted password with DB record
// 与数据库记录比较口令
if ($r && $r['password'] === $p) {
  echo "成功 / Success";
} else {
  echo "失败 / Fail";
}
```
- Read **POST** values, **select** the user row, and **compare** the password.  
- 读取 **POST** 值，**查询**用户行，并**比较**口令。  fileciteturn33file0

---

## Share Connection with `include('connect.php')`  
## 用 `include('connect.php')` 共享连接

```php
<?php // any script / 任意脚本
include("connect.php");  // provides $conn / 提供 $conn
// ... use $conn here ... / 在此处使用 $conn
```
- Since all DB scripts need the **same connection routine**, **share** it via **`include()`**.  
- 因所有脚本都需相同的**连接过程**，可通过 **`include()`** **共享**。  fileciteturn33file0

---

## CRUD Mini‑Scripts: `create.php` / `read.php` / `update.php` / `delete.php`  
## CRUD 小脚本：`create.php` / `read.php` / `update.php` / `delete.php`

```php
<?php // create.php (add a user) / 新增用户
include("connect.php");
$u = $_POST['userID']; $p = $_POST['password']; $n = $_POST['name'];
$rows = $conn->exec("INSERT INTO users VALUES (NULL,'{$u}','{$p}','{$n}')");
echo "Inserted: {$rows}";
$conn = null;
```

```php
<?php // read.php?id=1 (show one) / 显示指定用户
include("connect.php");
$id = $_GET['id'];
$result = $conn->query("SELECT * FROM users WHERE id={$id}");
$r = $result->fetch();
echo "<table><tr><th>id</th><th>userID</th><th>name</th></tr>";
echo "<tr><td>{$r['id']}</td><td>{$r['userID']}</td><td>{$r['name']}</td></tr></table>";
$conn = null;
```

```php
<?php // update.php (change password) / 修改密码
include("connect.php");
$id = $_POST['id']; $newp = $_POST['password'];
$rows = $conn->exec("UPDATE users SET password='{$newp}' WHERE id={$id}");
echo "Updated: {$rows}";
$conn = null;
```

```php
<?php // delete.php (delete by id) / 按 id 删除
include("connect.php");
$id = $_POST['id'];
$rows = $conn->exec("DELETE FROM users WHERE id={$id}");
echo "Deleted: {$rows}";
$conn = null;
```
- Each script performs **one function**; call them from forms or via Ajax.  
- 每个脚本只做**单一功能**；可通过表单或 Ajax 调用。  fileciteturn33file0

---

## Quick Checklist  
## 快速清单

- Use **PDO** (not `mysql_*`); `mysqli_*` exists but **PDO** is preferred here.  
- 采用 **PDO**（非 `mysql_*`）；虽有 `mysqli_*`，但此处**优先 PDO**。  fileciteturn33file0
- Connection DSN: **`mysql:host=localhost;dbname=test;charset=utf8`** (plus `;port=13306` if configured).  
- 连接 DSN：**`mysql:host=localhost;dbname=test;charset=utf8`**（如需可加 `;port=13306`）。  fileciteturn33file0
- **`exec()`** for **INSERT/UPDATE/DELETE** (returns affected rows); **`query()`** for **SELECT** (returns `PDOStatement`).  
- **`exec()`** 用于 **INSERT/UPDATE/DELETE**（返回影响行数）；**`query()`** 用于 **SELECT**（返回 `PDOStatement`）。  fileciteturn33file0
- **`fetch()`** gets one row; `foreach ($result as $r)` iterates remaining rows.  
- **`fetch()`** 取一行；`foreach ($result as $r)` 遍历余下各行。  fileciteturn33file0
- Share `$conn` with **`include('connect.php')`**; **close** via `$conn = null`.  
- 用 **`include('connect.php')`** 共享 `$conn`；以 `$conn = null` **关闭**。  fileciteturn33file0

---

## Notes 
## 注释

<details><summary>Supplement: Prepared statements & password hashing / 补充：预处理语句与口令散列</summary>

```php
// Safer version using prepared statements / 更安全的预处理版本
$stmt = $conn->prepare("SELECT * FROM users WHERE userID = :u");
$stmt->bindValue(":u", $u, PDO::PARAM_STR);
$stmt->execute();
$r = $stmt->fetch();
if ($r && password_verify($p, $r['password'])) { /* ok */ }
```
- Prefer **prepared statements** to avoid **SQL injection**; store **password hashes** and verify with `password_verify()`.  
- 为避免 **SQL 注入**建议使用**预处理语句**；口令应以**哈希**保存，并用 `password_verify()` 校验。  
</details>

<details><summary>Exception handling & where to put code / 异常处理与代码组织</summary>

- Wrap connection in **`try…catch`** with **`PDOException`**; common to **`require_once 'connect.php'`** at script top.  
- 使用 **`try…catch(PDOException)`** 捕获异常；常见做法是在脚本顶部 **`require_once 'connect.php'`**。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture33.md) · [Next Lecture / 下一讲 →](./lecture35.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

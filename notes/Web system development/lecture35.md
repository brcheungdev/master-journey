[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 35: PHP PDO Practice — Login, CRUD Scripts, Search (LIKE), and Update Workflow  
# 第35讲：PHP PDO 实战 —— 登录、CRUD 脚本、模糊搜索（LIKE）与更新流程

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [PDO Overview & Execution Flow](#pdo-overview--execution-flow)  
- PDO 概览与执行流程
- [Connect to MySQL via PDO (`new PDO`)](#connect-to-mysql-via-pdo-new-pdo)  
- 通过 PDO 连接 MySQL（`new PDO`）
- [Run SQL: `exec` (INSERT/UPDATE/DELETE) vs `query` (SELECT)](#run-sql-exec-insertupdatedelete-vs-query-select)  
- 执行 SQL：`exec`（增删改）与 `query`（查询）
- [Fetch Records: `fetch()` and `foreach` on `PDOStatement`](#fetch-records-fetch-and-foreach-on-pdostatement)  
- 读取记录：`fetch()` 与 `PDOStatement` 的 `foreach`
- [Practice 1: Login with DB (`check.php`)](#practice-1-login-with-db-checkphp)  
- 练习1：基于数据库的登录（`check.php`）
- [Share Connection: `include('connect.php')`](#share-connection-includeconnectphp)  
- 共享连接：`include('connect.php')`
- [Practice 2: `read.php` — Show One User by `id` (GET)](#practice-2-readphp--show-one-user-by-id-get)  
- 练习2：`read.php` —— 通过 `id`（GET）显示单个用户
- [Practice 3: `search.php` — Fuzzy Match by `name` (POST + `LIKE`)](#practice-3-searchphp--fuzzy-match-by-name-post--like)  
- 练习3：`search.php` —— 通过 `name` 模糊匹配（POST + `LIKE`）
- [Practice 4: `create.php` — Insert and `lastInsertId()`](#practice-4-createphp--insert-and-lastinsertid)  
- 练习4：`create.php` —— 插入并读取 `lastInsertId()`
- [Practice 5: `delete.php` — Delete by `id` (GET)](#practice-5-deletephp--delete-by-id-get)  
- 练习5：`delete.php` —— 通过 `id` 删除（GET）
- [Practice 6: `update.php` — Two‑Stage Update (GET→form→POST)](#practice-6-updatephp--two-stage-update-getformpost)  
- 练习6：`update.php` —— 两阶段更新（GET→表单→POST）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## PDO Overview & Execution Flow  
## PDO 概览与执行流程

- **PDO (PHP Data Objects)** abstracts DB access and returns **`PDO`** and **`PDOStatement`** objects.  
- **PDO（PHP 数据对象）**提供数据库抽象访问，涉及 **`PDO`** 与 **`PDOStatement`** 两类对象。

```
Application → new PDO (connect) → exec/query (run SQL) →
→ for SELECT: get PDOStatement → fetch() / foreach to read records
应用 → new PDO（建立连接）→ exec/query（执行 SQL）→
→ 若为 SELECT：得到 PDOStatement → fetch()/foreach 读取记录
```

---

## Connect to MySQL via PDO (`new PDO`)  
## 通过 PDO 连接 MySQL（`new PDO`）

```php
<?php
// connect.php
$conn = null;
try{
  $conn = new PDO(
    "mysql:host=localhost;port=13306;dbname=test;charset=utf8;",
    "root", "YOUR_PASSWORD"
  );
}catch(PDOException $e){
  die($e->getMessage()); // stop if connection fails / 连接失败则终止
}
```
- DSN format: **`mysql:host=<host>;[port=<port>;]dbname=<db>;charset=utf8;`**; default MySQL user often **`root`**.  
- DSN 格式：**`mysql:host=<主机>;[port=<端口>;]dbname=<数据库>;charset=utf8;`**；常见默认用户为 **`root`**。

---

## Run SQL: `exec` (INSERT/UPDATE/DELETE) vs `query` (SELECT)  
## 执行 SQL：`exec`（增删改）与 `query`（查询）

```php
$rows = $conn->exec("UPDATE users SET name='鈴木' WHERE id=3"); // returns affected rows / 返回受影响行数
$res  = $conn->query("SELECT id,userID,name FROM users");      // returns PDOStatement / 返回 PDOStatement
```
- Use **`exec()`** for **non‑SELECT** statements (returns **affected rows**).  
- **`exec()`** 用于 **非 SELECT** 语句（返回**受影响行数**）。  
- Use **`query()`** for **SELECT**, which gives a **`PDOStatement`** to read records.  
- **`query()`** 用于 **SELECT**，返回 **`PDOStatement`** 以读取记录。

---

## Fetch Records: `fetch()` and `foreach` on `PDOStatement`  
## 读取记录：`fetch()` 与 `PDOStatement` 的 `foreach`

```php
$r = $res->fetch();                          // first record / 第一条记录
echo $r['id'] . " : " . $r['userID'];

foreach ($res as $row) {                     // iterate all / 逐行遍历
  echo $row['id'] . " => " . $row['name'] . "<br>";
}
```
- Default fetch style allows both **numeric index** and **column‑name key** access.  
- 默认提取风格允许通过**数字下标**或**列名键**访问。

---

## Practice 1: Login with DB (`check.php`)  
## 练习1：基于数据库的登录（`check.php`）

```php
<?php // check.php
$u = $_POST['userID']; $p = $_POST['password'];
require_once("connect.php");
$result = $conn->query("SELECT * FROM users WHERE userID='{$u}'");
$r = $result->fetch();
$conn = null;

if ($r && $r['password'] === $p) {
  echo "成功 / Success";
} else {
  echo "失败 / Fail";
}
```
- Read **POST** values, **SELECT** by `userID`, then **compare** the password (row may be **`false`** if not found).  
- 读取 **POST** 值，按 `userID` **SELECT**，再**比较**口令（未找到时返回 **`false`**）。

---

## Share Connection: `include('connect.php')`  
## 共享连接：`include('connect.php')`

```php
<?php // any script
include("connect.php");  // provides $conn / 提供 $conn
// ... use $conn here ... / 在此处使用 $conn
```
- All DB scripts need the **same connection routine** — **share** with `include`.  
- 所有数据库脚本都需相同**连接过程**——用 `include` **复用**。

---

## Practice 2: `read.php` — Show One User by `id` (GET)  
## 练习2：`read.php` —— 通过 `id`（GET）显示单个用户

```php
<?php // read.php?id=1
include("connect.php");
$id = $_GET['id'];
$res = $conn->query("SELECT * FROM users WHERE id={$id}");
$r = $res->fetch();
echo "<table><tr><th>id</th><th>userID</th><th>name</th></tr>";
echo "<tr><td>{$r['id']}</td><td>{$r['userID']}</td><td>{$r['name']}</td></tr></table>";
$conn = null;
```
- Access via **`read.php?id=<number>`**; render the record with a **`<table>`** (avoid printing passwords).  
- 通过 **`read.php?id=<数字>`** 访问；用 **`<table>`** 输出记录（避免打印密码）。

---

## Practice 3: `search.php` — Fuzzy Match by `name` (POST + `LIKE`)  
## 练习3：`search.php` —— 通过 `name` 模糊匹配（POST + `LIKE`）

```php
<?php // search.php
include("connect.php");
$key = $_POST['key']; // e.g., contains '田'
$sql = "SELECT * FROM users WHERE name LIKE '%{$key}%'";
$res = $conn->query($sql);
echo "<table><tr><th>id</th><th>userID</th><th>name</th></tr>";
foreach ($res as $r) {
  echo "<tr><td>{$r['id']}</td><td>{$r['userID']}</td><td>{$r['name']}</td></tr>";
}
$conn = null;
```
- Use **`LIKE` + `%` wildcards** for **substring match**, and display **all** results.  
- 结合 **`LIKE` + `%` 通配**实现**子串匹配**，并显示**全部**结果。

---

## Practice 4: `create.php` — Insert and `lastInsertId()`  
## 练习4：`create.php` —— 插入并读取 `lastInsertId()`

```php
<?php // create.php
include("connect.php");
$u = $_POST['userID']; $p = $_POST['password']; $n = $_POST['name'];
$conn->exec("INSERT INTO users VALUES (NULL,'{$u}','{$p}','{$n}')");
echo "新记录 id = " . $conn->lastInsertId(); // get auto id / 获得自增 id
$conn = null;
```
- Insert **one record** using **`INSERT`**; read the **auto‑generated `id`** with **`lastInsertId()`**.  
- 用 **`INSERT`** 插入**一条记录**；用 **`lastInsertId()`** 获取**自增 `id`**。

---

## Practice 5: `delete.php` — Delete by `id` (GET)  
## 练习5：`delete.php` —— 通过 `id` 删除（GET）

```php
<?php // delete.php?id=3
include("connect.php");
$id = $_GET['id'];
$rows = $conn->exec("DELETE FROM users WHERE id={$id}");
echo "Deleted: {$rows}";
$conn = null;
```
- Use **`DELETE`** with **`WHERE`**; when success, `exec()` returns **1**.  
- 使用 **`DELETE`** 并加 **`WHERE`**；成功时 `exec()` 返回 **1**。

---

## Practice 6: `update.php` — Two‑Stage Update (GET→form→POST)  
## 练习6：`update.php` —— 两阶段更新（GET→表单→POST）

```php
<?php // update.php
include("connect.php");
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  $id = $_GET['id'];
  $r = $conn->query("SELECT * FROM users WHERE id={$id}")->fetch();
  echo '<form method="post">';
  echo '<input type="hidden" name="id" value="'.$r['id'].'">';
  echo 'userID: <input name="userID" value="'.$r['userID'].'"><br>';
  echo 'password: <input name="password" value="'.$r['password'].'"><br>';
  echo 'name: <input name="name" value="'.$r['name'].'"><br>';
  echo '<button>更新</button></form>';
} else {
  $id = $_POST['id'];
  $u = $_POST['userID']; $p = $_POST['password']; $n = $_POST['name'];
  $rows = $conn->exec("UPDATE users SET userID='{$u}', password='{$p}', name='{$n}' WHERE id={$id}");
  echo "Updated: {$rows}";
}
$conn = null;
```
- **Stage 1 (GET)**: fetch current values and **pre‑fill** an **edit form** (use a hidden input for `id`).  
- **阶段1（GET）**：读取当前值并**预填**编辑表单（用隐藏输入传递 `id`）。  
- **Stage 2 (POST)**: submit the form and run **`UPDATE ... WHERE id=?`** to persist changes.  
- **阶段2（POST）**：提交表单并执行 **`UPDATE ... WHERE id=?`** 保存变更。

---

## Quick Checklist  
## 快速清单

- **Connect** with `new PDO("mysql:...;charset=utf8;", "root", "…")`, handle exceptions.  
- 使用 `new PDO("mysql:...;charset=utf8;", "root", "…")` 建立连接并处理异常。  
- Use **`exec()`** for **INSERT/UPDATE/DELETE**; use **`query()`** for **SELECT**.  
- **增删改**用 **`exec()`**；**查询**用 **`query()`**。  
- Read one row via **`fetch()`**; iterate all with **`foreach ($stmt as $r)`**.  
- 用 **`fetch()`** 取一行；用 **`foreach ($stmt as $r)`** 遍历全部。  
- Implement **login** with a DB lookup; add **CRUD** scripts for admin.  
- 用数据库查询实现**登录**；为管理端实现 **CRUD** 脚本。  
- For substring search, use **`LIKE '%key%'`**; for UPDATE, use **two‑stage GET→POST**.  
- 子串搜索用 **`LIKE '%key%'`**；更新流程建议 **GET→POST 两阶段**。

---

## Notes
## 注释

<details><summary>Security best practices / 安全实践</summary>

- Prefer **prepared statements** with **placeholders** to prevent **SQL injection**.  
- 使用**预处理语句**与**占位符**防止 **SQL 注入**。  
- Store **password hashes** (e.g., `password_hash()` / `password_verify()`), not plaintext.  
- **不要存明文口令**，请存 **口令哈希**（如 `password_hash()` / `password_verify()`）。  
- Escape output when mixing HTML (`htmlspecialchars`) to avoid **XSS**.  
- 与 HTML 混输时用 `htmlspecialchars` 转义，避免 **XSS**。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture34.md) · [Next Lecture / 下一讲 →](./lecture36.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

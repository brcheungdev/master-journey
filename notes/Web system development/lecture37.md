[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 37: Sessions II — Simple Blog (Articles), Ownership Checks, and Prepared Statements  
# 第37讲：会话进阶 —— 简易博客（Articles）、所有权校验与预处理语句

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Review: Page Linking & Session Basics](#review-page-linking--session-basics)  
- 复习：页面互链与会话基础
- [Blog Spec Overview](#blog-spec-overview)  
- 博客规格概览
- [Prepare `articles` Table (JOIN with `users`)](#prepare-articles-table-join-with-users)  
- 准备 `articles` 表（与 `users` 连接）
- [Blog Page Wiring (Top = `search.php`)](#blog-page-wiring-top--searchphp)  
- 博客页面关联（入口为 `search.php`）
- [`read.php`: Show One Article (JOIN users.name)](#readphp-show-one-article-join-usersname)  
- `read.php`：显示单篇（连接 users.name）
- [`search.php`: Search by `subject` (POST + `LIKE`)](#searchphp-search-by-subject-post--like)  
- `search.php`：按 `subject` 搜索（POST + `LIKE`）
- [`create.php`: Insert Article (author from Session)](#createphp-insert-article-author-from-session)  
- `create.php`：新增文章（author 来自会话）
- [`update.php`: Two-Stage Edit (GET→Form→POST, Only Own Posts)](#updatephp-two-stage-edit-getformpost-only-own-posts)  
- `update.php`：两阶段编辑（GET→表单→POST，仅限本人）
- [`delete.php`: Ownership Check + Prepared Statement](#deletephp-ownership-check--prepared-statement)  
- `delete.php`：所有权校验 + 预处理语句
- [Minimum Security: Login Required & ID Match](#minimum-security-login-required--id-match)  
- 最低安全：登录必需与 ID 匹配
- [Export `test.sql` from phpMyAdmin](#export-testsql-from-phpmyadmin)  
- 从 phpMyAdmin 导出 `test.sql`
- [Enhancement Ideas (UI & Ajax)](#enhancement-ideas-ui--ajax)  
- 增强思路（界面与 Ajax）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Review: Page Linking & Session Basics  
## 复习：页面互链与会话基础

- Use **`search.php`** as the **users/articles management top**, linking to create/read/update/delete so you **don’t type URLs**.  
- 使用 **`search.php`** 作为**用户/文章管理入口**，互链 create/read/update/delete，避免**手动输入 URL**。  fileciteturn36file0
- **Sessions** = browser cookie **`PHPSESSID`** + server ledger **`$_SESSION`**; call **`session_start()`** before any output.  
- **会话**由浏览器 Cookie **`PHPSESSID`** + 服务器端 **`$_SESSION`** 组成；需在输出前调用 **`session_start()`**。  fileciteturn36file0
- On login success, store **`id`**/`name` into **`$_SESSION`**; provide **logout** to clear/destroy the session.  
- 登录成功后把 **`id`**/`name` 放入 **`$_SESSION`**；提供 **logout** 清空/销毁会话。  fileciteturn36file0

---

## Blog Spec Overview  
## 博客规格概览

- Build a **simple blog** where logged-in **users** can **create/edit/delete their own posts**; **everyone** can **search/read** all posts.  
- 实现一个**简易博客**：已登录**用户**可**新增/修改/删除自己的文章**；**任何人**都能**搜索/阅读**所有文章。  fileciteturn36file0

---

## Prepare `articles` Table (JOIN with `users`)  
## 准备 `articles` 表（与 `users` 连接）

```sql
-- One possible schema / 可选示例结构
CREATE TABLE articles (
  id       INT NOT NULL AUTO_INCREMENT,
  subject  VARCHAR(200) NOT NULL,
  body     TEXT NOT NULL,
  author   INT NOT NULL,            -- references users.id / 外键指向 users.id
  modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
           ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
```
- **`author`** stores the **`users.id`**; render **author name** via **JOIN** when selecting.  
- **`author`** 保存 **`users.id`**；选择时通过 **JOIN** 获取**作者姓名**。  fileciteturn36file0

```sql
-- Join articles with users to show author name / 连接 users 以显示作者名
SELECT  articles.*, users.name
FROM    articles, users
WHERE   articles.author = users.id;
```
- Use **phpMyAdmin** to **create `articles`** and insert some **sample rows** for testing.  
- 通过 **phpMyAdmin** 新建 **`articles`** 并插入若干**样例记录**以便测试。  fileciteturn36file0

---

## Blog Page Wiring (Top = `search.php`)  
## 博客页面关联（入口为 `search.php`）

```
search  →  create   (“New” button)
search  →  read?id=…   (click article id)
search  →  update?id=… (“Update” link)
search  →  delete?id=… (“Delete” link)
login → check → (success) → search → logout
```
```
search  →  create（“新建”按钮）
search  →  read?id=…（点击文章 id）
search  →  update?id=…（点击“更新”）
search  →  delete?id=…（点击“删除”）
login → check →（成功）→ search → logout
```
- Keep navigation **within the app** to accelerate testing and usage.  
- 通过**应用内导航**加速测试与使用。  fileciteturn36file0

---

## `read.php`: Show One Article (JOIN users.name)  
## `read.php`：显示单篇（连接 users.name）

```php
<?php // read.php?id=...
include("connect.php");
$id = (int)$_GET["id"];
$sql = "SELECT articles.*, users.name
        FROM articles, users
        WHERE articles.id={$id} AND articles.author=users.id";
$r = $conn->query($sql)->fetch();
echo "<table>
  <tr><th>id</th><td>{$r['id']}</td></tr>
  <tr><th>subject</th><td>{$r['subject']}</td></tr>
  <tr><th>author</th><td>{$r['name']}</td></tr>
  <tr><th>modified</th><td>{$r['modified']}</td></tr>
  <tr><th>body</th><td><pre>{$r['body']}</pre></td></tr>
</table>";
$conn = null;
```
- Include **author name** by joining **`users`**; render article fields in a **table**.  
- 通过连接 **`users`** 显示作者姓名；用 **表格**输出文章字段。  fileciteturn36file0

---

## `search.php`: Search by `subject` (POST + `LIKE`)  
## `search.php`：按 `subject` 搜索（POST + `LIKE`）

```php
<?php // search.php
include("connect.php");
$key = $_POST["key"] ?? "";
$sql = "SELECT articles.id, articles.subject, users.name, articles.modified
        FROM articles, users
        WHERE articles.author=users.id AND articles.subject LIKE '%{$key}%'";
$res = $conn->query($sql);
echo '<form method="post"><input name="key" placeholder="subject contains"><button>Search</button></form>';
echo "<table><tr><th>id</th><th>subject</th><th>author</th><th>modified</th></tr>";
foreach ($res as $r) {
  echo "<tr>
    <td><a href='read.php?id={$r['id']}'>{$r['id']}</a></td>
    <td>{$r['subject']}</td>
    <td>{$r['name']}</td>
    <td>{$r['modified']}</td>
  </tr>";
}
echo "</table>";
$conn = null;
```
- Use **`LIKE '%key%'`** to find posts whose **subject contains** the keyword; list all matches.  
- 用 **`LIKE '%key%'`** 搜索 **subject 含关键字**的文章；列出全部匹配结果。  fileciteturn36file0

---

## `create.php`: Insert Article (author from Session)  
## `create.php`：新增文章（author 来自会话）

```php
<?php // create.php
session_start();
if (!isset($_SESSION["id"])) { header("Location: login.html"); exit; } // must login
include("connect.php");
$subject = $_POST["subject"];
$body    = $_POST["body"];
$author  = (int)$_SESSION["id"];
$sql = "INSERT INTO articles VALUES (NULL, '{$subject}', '{$body}', {$author}, NOW())";
$conn->exec($sql);
echo "created id = " . $conn->lastInsertId();
$conn = null;
```
- Author is the **logged-in user** (`$_SESSION["id"]`); use **`NOW()`** for `modified`, and **`lastInsertId()`** to show the new id.  
- 作者为**当前登录用户**（`$_SESSION["id"]`）；使用 **`NOW()`** 赋值 `modified`，并通过 **`lastInsertId()`** 显示新 id。  fileciteturn36file0

---

## `update.php`: Two-Stage Edit (GET→Form→POST, Only Own Posts)  
## `update.php`：两阶段编辑（GET→表单→POST，仅限本人）

```php
<?php // update.php
session_start();
if (!isset($_SESSION["id"])) { header("Location: login.html"); exit; }
include("connect.php");

if ($_SERVER["REQUEST_METHOD"] === "GET") {
  $id = (int)$_GET["id"];
  // Only allow editing own post / 仅允许本人编辑
  $stmt = $conn->prepare("SELECT * FROM articles WHERE id=:id AND author=:a");
  $stmt->execute([":id"=>$id, ":a"=>$_SESSION["id"]]);
  $r = $stmt->fetch();
  if (!$r) { header("Location: search.php"); exit; }
  echo '<form method="post">';
  echo '<input type="hidden" name="id" value="'.$r['id'].'">';
  echo 'subject: <input name="subject" value="'.htmlspecialchars($r['subject']).'"><br>';
  echo 'body:<br><textarea name="body" rows="6" cols="60">'.htmlspecialchars($r['body']).'</textarea><br>';
  echo '<button>更新</button></form>';
} else {
  $id = (int)$_POST["id"];
  $stmt = $conn->prepare(
    "UPDATE articles SET subject=:s, body=:b, modified=NOW()
     WHERE id=:id AND author=:a");
  $ok = $stmt->execute([":s"=>$_POST["subject"], ":b"=>$_POST["body"],
                        ":id"=>$id, ":a"=>$_SESSION["id"]]);
  echo $ok ? "Updated" : "Not updated";
}
$conn = null;
```
- **Stage 1 (GET)**: fetch current values **only if author is self**; show an **edit form**.  
- **阶段1（GET）**：仅在**作者为本人**时取当前值；输出**编辑表单**。  fileciteturn36file0
- **Stage 2 (POST)**: run **`UPDATE ... WHERE id AND author`** to enforce ownership.  
- **阶段2（POST）**：以 **`UPDATE ... WHERE id AND author`** 强制所有权校验。  fileciteturn36file0

---

## `delete.php`: Ownership Check + Prepared Statement  
## `delete.php`：所有权校验 + 预处理语句

```php
<?php // delete.php?id=...
session_start();
if (!isset($_SESSION["id"])) { header("Location: login.html"); exit; }
include("connect.php");
$id = (int)$_GET["id"];
$stmt = $conn->prepare("DELETE FROM articles WHERE id=:id AND author=:a");
$ok = $stmt->execute([":id"=>$id, ":a"=>$_SESSION["id"]]);
echo $ok ? "Deleted" : "Not deleted (not owner?)";
$conn = null;
```
- Only **self-owned** posts can be deleted; use **prepared statements** to avoid **SQL injection**.  
- 仅允许**删除本人**文章；使用**预处理语句**避免**SQL 注入**。  fileciteturn36file0

---

## Minimum Security: Login Required & ID Match  
## 最低安全：登录必需与 ID 匹配

- Before **create/delete/update**, check **logged-in state**; redirect to **`login.html`** when absent.  
- 在 **新增/删除/更新**前检查**登录状态**；未登录则转送 **`login.html`**。  fileciteturn36file0
- In SQL `WHERE`, always **constrain by `author = $_SESSION['id']`**.  
- 在 SQL 的 `WHERE` 中**总是加上 `author = $_SESSION['id']`**。  fileciteturn36file0

---

## Export `test.sql` from phpMyAdmin  
## 从 phpMyAdmin 导出 `test.sql`

- In phpMyAdmin, choose database **`test`** → **Export** tab → **Execute** to download **`test.sql`** (contains **`users`** and **`articles`**).  
- 在 phpMyAdmin 中选择 **`test`** → **导出**标签 → **执行**，下载 **`test.sql`**（包含 **`users`** 与 **`articles`**）。  fileciteturn36file0

---

## Enhancement Ideas (UI & Ajax)  
## 增强思路（界面与 Ajax）

- Improve **typography/layout/colors** with **HTML + CSS**; make results **clearer**.  
- 用 **HTML + CSS** 改善**排版/布局/配色**，提升可读性。  fileciteturn36file0
- Use **jQuery** to enhance **interactions**; e.g., show `read.php` result **inline** via **Ajax** from `search.php`.  
- 使用 **jQuery** 增强**交互性**；例如在 `search.php` 内通过 **Ajax** **内嵌显示** `read.php` 的结果。  fileciteturn36file0
- Show **login form** in a **modal dialog** for smoother UX.  
- 以**模态对话框**展示**登录表单**以改善体验。  fileciteturn36file0

---

## Quick Checklist  
## 快速清单

- `articles` table with **`author` = `users.id`**; show author via **JOIN**.  
- `articles` 表用 **`author` = `users.id`**；通过 **JOIN** 显示作者名。  fileciteturn36file0
- `read.php` (JOIN), `search.php` (`LIKE`), `create.php` (`NOW()` + `lastInsertId()`), `update.php` (two-stage), `delete.php` (owner-only).  
- `read.php`（JOIN）、`search.php`（`LIKE`）、`create.php`（`NOW()` + `lastInsertId()`）、`update.php`（两阶段）、`delete.php`（仅本人）。  fileciteturn36file0
- Always **require login** and **enforce ownership** in **`WHERE`**.  
- 始终**要求登录**并在 **`WHERE`** 中**强制所有权**。  fileciteturn36file0
- Prefer **prepared statements** for all dynamic SQL.  
- 动态 SQL **优先使用预处理语句**。  fileciteturn36file0

---

## Notes
## 注释

<details><summary>Prepared Statements Recap / 预处理语句回顾</summary>

```php
// SELECT as prepared / 预处理的 SELECT
$stmt = $conn->prepare("SELECT * FROM articles WHERE id=:id AND author=:a");
$stmt->execute([":id"=>$id, ":a"=>$_SESSION["id"]]);
$r = $stmt->fetch(); // same as PDOStatement returned by query() / 与 query() 返回的 PDOStatement 相同
```
- `prepare()` returns a **PDOStatement**; `execute()` returns **boolean**; then **`fetch()`** to read row(s).  
- `prepare()` 返回 **PDOStatement**；`execute()` 返回 **布尔值**；随后用 **`fetch()`** 读取记录。  fileciteturn36file0
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture36.md) · [Next Lecture / 下一讲 →](./lecture38.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

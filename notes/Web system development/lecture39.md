[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 39: Simple Blog — Page Integration (Redux), Security (SQL Injection & Prepared Statements), Export & Final Report  
# 第39讲：简易博客 —— 页面关联（再强化）、安全（SQL 注入与预处理语句）、导出与最终报告

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Objectives & Recap](#objectives--recap)  
- 目标与复习
- [Link All Pages: `search` as the Top](#link-all-pages-search-as-the-top)  
- 互链所有页面：`search` 作为入口
- [Minimum Security: Login Check & Ownership Gate](#minimum-security-login-check--ownership-gate)  
- 最低安全：登录校验与所有权闸门
- [SQL Injection Risk: Why Raw String SQL Is Dangerous](#sql-injection-risk-why-raw-string-sql-is-dangerous)  
- SQL 注入风险：为何直接拼接 SQL 危险
- [Prepared Statements for SELECT/INSERT/UPDATE/DELETE](#prepared-statements-for-selectinsertupdatedelete)  
- 用预处理语句实现 SELECT/INSERT/UPDATE/DELETE
- [Articles CRUD Recap (read/search/create/delete/update)](#articles-crud-recap-readsearchcreatedeleteupdate)  
- 文章 CRUD 回顾（read/search/create/delete/update）
- [Export `test.sql` via phpMyAdmin](#export-testsql-via-phpmyadmin)  
- 通过 phpMyAdmin 导出 `test.sql`
- [Final Submission Checklist](#final-submission-checklist)  
- 最终提交清单
- [UI/Ajax Enhancements](#uiajax-enhancements-optional)  
- 界面/Ajax 增强
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Objectives & Recap  
## 目标与复习

- Build a **minimal blog** where logged-in users can **create/edit/delete their own posts**, and **anyone** can **search/read**.  
- 完成**最小可用博客**：已登录用户可**新增/修改/删除自己的文章**；**任何人**可**搜索/阅读**。  
- Use **sessions** (`session_start()` + `$_SESSION`) to keep login state; wire pages so you **don’t type URLs** by hand.  
- 使用**会话**（`session_start()` + `$_SESSION`）保持登录状态；通过页面互链**免手动输入 URL**。  

---

## Link All Pages: `search` as the Top  
## 互链所有页面：`search` 作为入口

```
search  →  create   (“New” button)
search  →  read?id=…   (click article id)
search  →  update?id=… (“Update” link)
search  →  delete?id=… (“Delete” link)
login → check →（success）→ search → logout
```
```
search  →  create（“新建”按钮）
search  →  read?id=…（点击文章 id）
search  →  update?id=…（点击“更新”）
search  →  delete?id=…（点击“删除”）
login → check →（成功）→ search → logout
```
- Make **`search.php`** the **post-login top page** to navigate all features.  
- 将 **`search.php`** 作为**登录后的首页**，从此进入全部功能。  

---

## Minimum Security: Login Check & Ownership Gate  
## 最低安全：登录校验与所有权闸门

```php
<?php // at the top of create/update/delete scripts / 放在 create/update/delete 顶部
session_start();
if (!isset($_SESSION['id'])) { header("Location: login.html"); exit; } // must login / 必须登录

// For update/delete — allow only the owner / 更新/删除仅允许本人
$login_id = (int)$_SESSION['id'];
$id = (int)($_GET['id'] ?? $_POST['id'] ?? 0);
// Later SQL must include: WHERE id=:id AND author=:author
// 后续 SQL 必须包含：WHERE id=:id AND author=:author
```
- **Block** create/update/delete if **not logged in**; for sensitive ops, ensure **`author == $_SESSION['id']`**.  
- **未登录禁止**新增/更新/删除；敏感操作必须保证 **`author == $_SESSION['id']`**。  

---

## SQL Injection Risk: Why Raw String SQL Is Dangerous  
## SQL 注入风险：为何直接拼接 SQL 危险

```php
// DANGEROUS (do NOT do this) / 危险示例（请勿使用）
$id = $_GET['id']; // untrusted
$sql = "DELETE FROM articles WHERE id='{$id}'"; // injection risk
```
- An attacker can pass a crafted `id`, e.g. **`' OR 't'='t`**, leading to **mass deletion**.  
- 攻击者可传入恶意 `id`，例如 **`' OR 't'='t`**，导致**全表删除**。  

```
DELETE FROM articles WHERE id='' OR 't'='t'
```
- Always use **prepared statements** instead.  
- 必须改用**预处理语句**。  

---

## Prepared Statements for SELECT/INSERT/UPDATE/DELETE  
## 用预处理语句实现 SELECT/INSERT/UPDATE/DELETE

```php
// DELETE with ownership / 带所有权校验的删除
$stmt = $conn->prepare("DELETE FROM articles WHERE id=:id AND author=:author");
$ok = $stmt->execute([":id"=>$id, ":author"=>$login_id]);
echo $ok ? "Deleted" : "Not deleted";
```

```php
// SELECT one article for edit (GET stage) / 读取本人文章以供编辑（GET 阶段）
$stmt = $conn->prepare("SELECT * FROM articles WHERE id=:id AND author=:author");
$stmt->execute([":id"=>$id, ":author"=>$login_id]);
$r = $stmt->fetch(); // or foreach($stmt as $r) {}
```

```php
// UPDATE (POST stage) / 更新（POST 阶段）
$stmt = $conn->prepare(
  "UPDATE articles SET subject=:s, body=:b, modified=NOW()
   WHERE id=:id AND author=:author");
$ok = $stmt->execute([":s"=>$subject, ":b"=>$body, ":id"=>$id, ":author"=>$login_id]);
```

```php
// INSERT new article / 新增文章
$stmt = $conn->prepare("INSERT INTO articles VALUES (NULL, :s, :b, :a, NOW())");
$stmt->execute([":s"=>$subject, ":b"=>$body, ":a"=>$login_id]);
echo "created id = " . $conn->lastInsertId();
```
- **Placeholders** (e.g., `:id`, `:author`) keep **user input** separate from SQL, preventing **injection**.  
- **占位符**（如 `:id`、`:author`）将**用户输入**与 SQL **隔离**，从而**防注入**。  

---

## Articles CRUD Recap (read/search/create/delete/update)  
## 文章 CRUD 回顾（read/search/create/delete/update）

```php
// read.php?id=...  (JOIN users to show author name) / 连接 users 显示作者名
$sql = "SELECT articles.*, users.name
        FROM articles, users
        WHERE articles.id=:id AND articles.author=users.id";
$stmt = $conn->prepare($sql);
$stmt->execute([":id"=>$id]);
$r = $stmt->fetch();
```

```php
// search.php  (subject LIKE '%key%') / 按 subject 模糊匹配
$key = $_POST['key'] ?? "";
$sql = "SELECT a.id, a.subject, u.name, a.modified
        FROM articles a, users u
        WHERE a.author=u.id AND a.subject LIKE :k";
$stmt = $conn->prepare($sql);
$stmt->execute([":k"=>"%"+key+"%"]);
```

```php
// create.php  (author from session + NOW()) / 作者来自会话 + NOW()
$stmt = $conn->prepare("INSERT INTO articles VALUES (NULL,:s,:b,:a,NOW())");
$stmt->execute([":s"=>$subject, ":b"=>$body, ":a"=>$login_id]);
```

```php
// update.php  two-stage (GET→form→POST) / 两阶段（GET→表单→POST）
```
- **`read.php`**: GET `id`, JOIN **`users`** for `name`.  
- **`read.php`**：GET `id`，连接 **`users`** 获取 `name`。  
- **`search.php`**: POST keyword, **`LIKE '%key%'`** on `subject`.  
- **`search.php`**：POST 关键字，在 `subject` 上 **`LIKE '%key%'`**。  
- **`create.php`**: `author = $_SESSION['id']`, `modified = NOW()`, show **`lastInsertId()`**.  
- **`create.php`**：`author = $_SESSION['id']`，`modified = NOW()`，显示 **`lastInsertId()`**。  
- **`update.php`**: GET stage shows current values (only own posts), POST stage runs **`UPDATE ... WHERE id AND author`**.  
- **`update.php`**：GET 阶段显示当前值（仅本人文章），POST 阶段执行 **`UPDATE ... WHERE id AND author`**。  
- **`delete.php`**: GET `id`, delete **only own** post.  
- **`delete.php`**：GET `id`，仅**删除本人**文章。  

---

## Export `test.sql` via phpMyAdmin  
## 通过 phpMyAdmin 导出 `test.sql`

- Open **phpMyAdmin** → choose DB **`test`** → **Export** tab → click **Execute** to download **`test.sql`**.  
- 打开 **phpMyAdmin** → 选择数据库 **`test`** → **导出**标签 → 点击**执行**下载 **`test.sql`**。  
- `test.sql` should contain **`users`** and **`articles`** schemas and data; **verify** with VS Code.  
- `test.sql` 应包含 **`users`** 与 **`articles`** 的结构与数据；用 VS Code **检查**内容。  

---

## Final Submission Checklist  
## 最终提交清单

- Include **all project files**: `.php`, `.html`, `.css`, **images/assets**, and **`test.sql`**.  
- 提交**完整项目文件**：`.php`、`.html`、`.css`、**图片/资源**以及 **`test.sql`**。  
- Ensure **login/logout** loop works and **ownership checks** are enforced on **update/delete**.  
- 确保 **登录/登出**链路可用，并在 **更新/删除**上**强制所有权校验**。  
- Use **prepared statements** everywhere; do **not** concatenate untrusted input into SQL.  
- 全面使用**预处理语句**；**不要**把不可信输入直接拼接进 SQL。  

---

## UI/Ajax Enhancements 
## 界面/Ajax 增强

- Improve **typography/layout/colors** with **HTML+CSS** for readability.  
- 用 **HTML+CSS** 改善**字体/布局/配色**以提升可读性。  
- Show `read.php` result **inline** from `search.php` via **`.load()`** or **`$.get()`**.  
- 在 `search.php` 中通过 **`.load()`** 或 **`$.get()`** **内联显示** `read.php` 结果。  
- Present **login form** in a **modal dialog** for smoother UX.  
- 用**模态对话框**展示**登录表单**，优化体验。  

---

## Quick Checklist  
## 快速清单

- `search` as **top**; link to **create/read/update/delete**; login → check → search → logout.  
- `search` 作为**入口**；互链 **create/read/update/delete**；login → check → search → logout。  
- Enforce **login state** and **ownership** (`author == $_SESSION['id']`).  
- 强制**登录状态**与**所有权**（`author == $_SESSION['id']`）。  
- Avoid injection with **prepared statements** for all SQL.  
- 全部 SQL 使用**预处理语句**以防注入。  
- Export and include **`test.sql`** in your submission.  
- 导出并随提交附上 **`test.sql`**。  

---

## Notes
## 注释

<details><summary>PDO statement behavior / PDO 语句对象要点</summary>

- `prepare()` returns a **PDOStatement** (same type as `query()` returns).  
- `prepare()` 返回 **PDOStatement**（与 `query()` 返回类型相同）。  
- `execute()` returns **boolean**; then use **`fetch()`** or **`foreach ($stmt as $r)`**.  
- `execute()` 返回**布尔值**；随后用 **`fetch()`** 或 **`foreach ($stmt as $r)`** 读取。  
- `rowCount()` gives **affected rows** for **DML** (similar to `exec()`’s return).  
- **DML** 语句可用 `rowCount()` 获取**受影响行数**（类似 `exec()` 返回值）。  
</details>

---

[← Previous Lecture / 上一讲](./lecture38.md) · [Next Lecture / 下一讲 →](./lecture40.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

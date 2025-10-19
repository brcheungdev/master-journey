[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 38: Simple Blog — Final Assembly, Security (Prepared Statements), UI/Ajax Enhancements, and Submission  
# 第38讲：简易博客 —— 最终组装、安全（预处理语句）、界面/Ajax 增强与提交说明

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Recap: Sessions, Ownership, and Page Wiring](#recap-sessions-ownership-and-page-wiring)  
- 复习：会话、所有权与页面关联
- [Final Feature Checklist (Minimum Requirements)](#final-feature-checklist-minimum-requirements)  
- 最终功能清单（最低要求）
- [Database: `users` and `articles` (JOIN)](#database-users-and-articles-join)  
- 数据库：`users` 与 `articles`（连接）
- [Security 1: Prepared Statements Everywhere](#security-1-prepared-statements-everywhere)  
- 安全一：到处使用预处理语句
- [Security 2: Login Required + Author Matching](#security-2-login-required--author-matching)  
- 安全二：必须登录 + 作者匹配
- [Security 3: Session Hygiene (Regenerate/Logout)](#security-3-session-hygiene-regeneratelogout)  
- 安全三：会话卫生（再生成/登出）
- [UI/UX: HTML+CSS Cleanup and jQuery Enhancements](#uiux-htmlcss-cleanup-and-jquery-enhancements)  
- 界面/体验：HTML+CSS 清理与 jQuery 增强
- [Ajax Options: `.load()` vs `$.get()`/`$.post()`](#ajax-options-load-vs-getpost)  
- Ajax 选项：`.load()` 与 `$.get()`/`$.post()`
- [Export & Submission: `test.sql` and Project Files](#export--submission-testsql-and-project-files)  
- 导出与提交：`test.sql` 与项目文件
- [Suggested Directory Layout](#suggested-directory-layout)  
- 推荐目录结构
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Recap: Sessions, Ownership, and Page Wiring  
## 复习：会话、所有权与页面关联

- Use **`session_start()`** and store **`$_SESSION['id']`/`$_SESSION['name']`** on successful login.  
- 成功登录后使用 **`session_start()`** 并写入 **`$_SESSION['id']`/`$_SESSION['name']`**。  
- Link pages within the app: `search → create/read/update/delete`, plus `login → check → (success) → search → logout`.  
- 在应用内部互链页面：`search → create/read/update/delete`，以及 `login → check →（成功）→ search → logout`。  
- Allow **edit/delete** only when **`author == $_SESSION['id']`**.  
- 仅当 **`author == $_SESSION['id']`** 时才允许**编辑/删除**。  

---

## Final Feature Checklist (Minimum Requirements)  
## 最终功能清单（最低要求）

- **Login**: `login.html` → `check.php` (on success, save to session and redirect to `search.php`).  
- **登录**：`login.html` → `check.php`（成功时写入会话并转送到 `search.php`）。  
- **Search**: `search.php` POST keyword; list articles matching **`subject LIKE '%key%'`** (JOIN to show author name).  
- **搜索**：`search.php` 以 POST 发送关键字；列出 **`subject LIKE '%key%'`** 的文章（JOIN 显示作者名）。  
- **Read**: `read.php?id=…` shows one record (JOIN users to show `name`).  
- **阅读**：`read.php?id=…` 显示一条记录（JOIN users 显示 `name`）。  
- **Create**: `create.php` inserts with `author = $_SESSION['id']`, `modified = NOW()`.  
- **新增**：`create.php` 插入记录，`author = $_SESSION['id']`，`modified = NOW()`。  
- **Update**: `update.php` (GET→form→POST), only own post; `UPDATE ... WHERE id=:id AND author=:a`.  
- **更新**：`update.php`（GET→表单→POST），仅限本人；`UPDATE ... WHERE id=:id AND author=:a`。  
- **Delete**: `delete.php?id=…`, only own post; return result message.  
- **删除**：`delete.php?id=…`，仅限本人；返回执行结果信息。  
- **Logout**: `logout.php` clears session and redirects `login.html`.  
- **登出**：`logout.php` 清空会话并转送 `login.html`。  

---

## Database: `users` and `articles` (JOIN)  
## 数据库：`users` 与 `articles`（连接）

```sql
-- users (as in previous lectures) / users（延续前面课程）
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  userID VARCHAR(32) NOT NULL,
  password VARCHAR(64) NOT NULL,
  name VARCHAR(64) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- articles
CREATE TABLE articles (
  id INT NOT NULL AUTO_INCREMENT,
  subject  VARCHAR(200) NOT NULL,
  body     TEXT NOT NULL,
  author   INT NOT NULL, -- references users.id
  modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
           ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- simple join to render author names / 简单连接以渲染作者名
SELECT articles.id, articles.subject, users.name, articles.modified
FROM articles, users
WHERE articles.author = users.id
  AND articles.subject LIKE '%keyword%';
```
- `articles.author` keeps the **user id**; use **JOIN** to display **author name**.  
- `articles.author` 保存**用户 id**；通过 **JOIN** 显示**作者名**。  

---

## Security 1: Prepared Statements Everywhere  
## 安全一：到处使用预处理语句

```php
// SELECT one article for editing / 读取待编辑文章（本人）
$stmt = $conn->prepare("SELECT * FROM articles WHERE id=:id AND author=:a");
$stmt->execute([":id"=>$id, ":a"=>$_SESSION["id"]]);
$r = $stmt->fetch();

// UPDATE (stage 2) / 更新（阶段二）
$stmt = $conn->prepare("UPDATE articles SET subject=:s, body=:b, modified=NOW() WHERE id=:id AND author=:a");
$ok = $stmt->execute([":s"=>$subject, ":b"=>$body, ":id"=>$id, ":a"=>$_SESSION["id"]]);

// DELETE / 删除
$stmt = $conn->prepare("DELETE FROM articles WHERE id=:id AND author=:a");
$ok = $stmt->execute([":id"=>$id, ":a"=>$_SESSION["id"]]);

// INSERT / 新增
$stmt = $conn->prepare("INSERT INTO articles VALUES (NULL, :s, :b, :a, NOW())");
$stmt->execute([":s"=>$subject, ":b"=>$body, ":a"=>$_SESSION["id"]]);
```
- Placeholders **`:id`/`:a`/`:s`/`:b`** prevent **SQL injection** and auto‑escape quotes.  
- 使用占位符 **`:id`/`:a`/`:s`/`:b`** 可防止 **SQL 注入**并自动处理引号转义。  

---

## Security 2: Login Required + Author Matching  
## 安全二：必须登录 + 作者匹配

```php
session_start();
if (!isset($_SESSION["id"])) { header("Location: login.html"); exit; } // must login
```
- Before **create/update/delete**, ensure **logged‑in** state; otherwise **redirect** to `login.html`.  
- 在 **新增/更新/删除** 之前必须检查**已登录**；否则**转送**到 `login.html`。  

```php
// Always constrain by author / 总是按作者加限制
WHERE id=:id AND author=:a
```
- Enforce **ownership** in SQL `WHERE` to avoid cross‑user modifications.  
- 在 SQL 的 `WHERE` 中强制**所有权**，避免用户越权修改。  

---

## Security 3: Session Hygiene (Regenerate/Logout)  
## 安全三：会话卫生（再生成/登出）

```php
// After successful login / 登录成功后
session_regenerate_id(true); // mitigate session fixation / 防会话固定
```
- Regenerate **session id** on login; provide **logout** to clear and destroy session.  
- 登录后**再生成会话 ID**；提供**登出**以清空并销毁会话。  

---

## UI/UX: HTML+CSS Cleanup and jQuery Enhancements  
## 界面/体验：HTML+CSS 清理与 jQuery 增强

- Use **semantic HTML** and consistent **typography/layout/colors** for clarity.  
- 使用**语义化 HTML**与统一的**字体/布局/配色**以提升可读性。  
- Add **links** in search results: **id → `read.php`**, **Update/Delete** buttons, **New** button to `create.php`.  
- 在搜索结果中添加**链接**：**id → `read.php`**、**更新/删除**按钮、**新建**按钮指向 `create.php`。  
- Use jQuery to **delegate events** on dynamic lists and to **toggle highlight** on selected rows.  
- 用 jQuery 对动态列表**委托事件**，并**切换高亮**选中行。  

---

## Ajax Options: `.load()` vs `$.get()`/`$.post()`  
## Ajax 选项：`.load()` 与 `$.get()`/`$.post()`

```js
// Inline article view / 内联查看文章
$("#result").load("read.php?id=" + artId);

// Or use $.get / 或使用 $.get
$.get("read.php", { id: artId }, function(html){ $("#result").html(html); });
```
- **`.load()`** quickly swaps **inner HTML**; **`$.get/$.post`** give you **callbacks** to handle data/errors.  
- **`.load()`** 可快速替换**内部 HTML**；**`$.get/$.post`** 提供**回调**便于处理数据/错误。  
- Respect **same‑origin** rules when fetching partials.  
- 获取局部页面时需遵守**同源策略**。  

---

## Export & Submission: `test.sql` and Project Files  
## 导出与提交：`test.sql` 与项目文件

- In **phpMyAdmin**, select database **`test`** → **Export** tab → click **Execute** to download **`test.sql`**.  
- 在 **phpMyAdmin** 选择数据库 **`test`** → **导出**标签 → 点击**执行**下载 **`test.sql`**。  
- Submit **all project files**: `.php`, `.html`, `.css`, **images/assets**, and the exported **`test.sql`**.  
- 提交**所有项目文件**：`.php`、`.html`、`.css`、**图片/资源**以及导出的 **`test.sql`**。  
- Open `test.sql` with **VS Code** to verify its content before submission.  
- 提交前用 **VS Code** 打开 `test.sql` 检查其内容。  

---

## Suggested Directory Layout  
## 推荐目录结构

```
/htdocs/<student-id>/blog/
├─ login.html
├─ check.php
├─ logout.php
├─ search.php
├─ read.php
├─ create.php
├─ update.php
├─ delete.php
├─ connect.php
├─ css/
│  └─ style.css
├─ js/
│  └─ app.js
├─ img/
│  └─ ...
└─ test.sql   (exported from phpMyAdmin)
```
```
/htdocs/<学籍番号>/blog/
├─ login.html
├─ check.php
├─ logout.php
├─ search.php
├─ read.php
├─ create.php
├─ update.php
├─ delete.php
├─ connect.php
├─ css/
│  └─ style.css
├─ js/
│  └─ app.js
├─ img/
│  └─ ...
└─ test.sql   （从 phpMyAdmin 导出）
```

---

## Quick Checklist  
## 快速清单

- All **CRUD** pages wired from **`search.php`**; **login/logout** work end‑to‑end.  
- 所有 **CRUD** 页面从 **`search.php`** 互链；**登录/登出**闭环可用。  
- DB tables: **`users`** and **`articles`**; join to show **author name**.  
- 数据表：**`users`** 与 **`articles`**；通过 join 显示**作者名**。  
- Use **prepared statements** for **SELECT/INSERT/UPDATE/DELETE**.  
- 对 **SELECT/INSERT/UPDATE/DELETE** 一律使用**预处理语句**。  
- Enforce **login** and **ownership** on **create/update/delete**.  
- 在 **新增/更新/删除** 上强制**登录**与**所有权**。  
- Polish **UI/UX** with **HTML+CSS**, optionally add **jQuery/Ajax** for inline read.  
- 用 **HTML+CSS** 打磨界面，选配 **jQuery/Ajax** 内联查看。  
- Submit **project files** + **`test.sql`**; verify `test.sql` content.  
- 提交**项目文件**与 **`test.sql`**；提交前检查 `test.sql`。  

---

## Notes
## 注释

<details><summary>Sanitization & XSS</summary>
- Escape any untrusted text with **`htmlspecialchars()`** when mixing into HTML.  
- 将不可信文本混入 HTML 时，请用 **`htmlspecialchars()`** 转义。  
</details>

<details><summary>Password storage</summary>
- Prefer **`password_hash()`/`password_verify()`** instead of plaintext passwords.  
- 推荐使用 **`password_hash()`/`password_verify()`**，不要存明文口令。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture37.md) · [Next Lecture / 下一讲 →](./lecture39.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

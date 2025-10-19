[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 36: PHP Sessions — Login State, `PHPSESSID` Cookie, and Authorization with PDO  
# 第36讲：PHP 会话 —— 登录状态、`PHPSESSID` Cookie 与基于 PDO 的访问控制

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Review: Share PDO Connection via `include('connect.php')`](#review-share-pdo-connection-via-includeconnectphp)  
- 复习：通过 `include('connect.php')` 复用 PDO 连接
- [CRUD Pages Wiring (Search as Entry, Link Others)](#crud-pages-wiring-search-as-entry-link-others)  
- 页面关联（以 Search 为入口，链接其他页面）
- [HTTP Is Stateless: Why We Need Sessions](#http-is-stateless-why-we-need-sessions)  
- HTTP 无状态：为何需要会话
- [What Is a Session: Cookie (`PHPSESSID`) + Server Ledger (`$_SESSION`)](#what-is-a-session-cookie-phpsessid--server-ledger-_session)  
- 会话的组成：Cookie（`PHPSESSID`）+ 服务器台账（`$_SESSION`）
- [Core Session APIs: `session_start()`, Lifetime, Destroy](#core-session-apis-session_start-lifetime-destroy)  
- 核心会话 API：`session_start()`、有效期、销毁
- [Login Flow: Save `id`/`name` in `$_SESSION` on Success](#login-flow-save-idname-in-_session-on-success)  
- 登录流程：成功后把 `id`/`name` 存入 `$_SESSION`
- [Show Username or “Guest” + Logout Button](#show-username-or-guest---logout-button)  
- 显示用户名或“Guest”+ 登出按钮
- [Logout Flow: Clear Session and Redirect](#logout-flow-clear-session-and-redirect)  
- 登出流程：清空会话并转送
- [Protect Operations: Allow `delete/update` Only for Self](#protect-operations-allow-deleteupdate-only-for-self)  
- 保护敏感操作：仅允许本人执行 `delete/update`
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Review: Share PDO Connection via `include('connect.php')`  
## 复习：通过 `include('connect.php')` 复用 PDO 连接

- Place the **PDO creation** into **`connect.php`**, and `include` it where DB is needed.  
- 将 **PDO 创建代码**放入 **`connect.php`**，在需要访问数据库的脚本中 `include`。  

```php
// connect.php
<?php
$conn = new PDO("mysql:host=localhost;dbname=test;charset=utf8;", "root", "YOUR_PASSWORD");
```
```php
// any script
<?php
include("connect.php"); // use $conn directly
// ... DB operations ...
```
- All **CRUD pages** can **reuse** the same `$conn`.  
- 所有 **CRUD** 页面均可**复用**同一 `$conn`。  

---

## CRUD Pages Wiring (Search as Entry, Link Others)  
## 页面关联（以 Search 为入口，链接其他页面）

```
search.php  →  create.php  （“新建”按钮）
search.php  →  read.php?id=…  （点击行的 id）
search.php  →  update.php?id=…（点击“更新”）
search.php  →  delete.php?id=…（点击“删除”）
```
```
search.php  →  create.php  (“New” button)
search.php  →  read.php?id=…  (click row id)
search.php  →  update.php?id=… (click “Update”)
search.php  →  delete.php?id=… (click “Delete”)
```
- Avoid typing URLs manually by **linking pages together**.  
- 通过**互链页面**避免每次手工输入 URL。  

---

## HTTP Is Stateless: Why We Need Sessions  
## HTTP 无状态：为何需要会话

- After a response, the server **forgets** prior requests; data **is not carried over** automatically.  
- 服务器响应后会**忘记**之前的访问；数据**不会自动传递**到其他脚本。  

```
login.php → (OK) → update.php   → “Who are you?” (no memory)
login.php → （成功）→ update.php → “你是谁？”（服务器没有记忆）
```
- To continue recognizing the same browser, we need a **“visit certificate”** and a **server ledger**.  
- 如需持续识别同一浏览器，需要**“来访证书”**与**服务器台账**。  

---

## What Is a Session: Cookie (`PHPSESSID`) + Server Ledger (`$_SESSION`)  
## 会话的组成：Cookie（`PHPSESSID`）+ 服务器台账（`$_SESSION`）

- The browser stores a cookie **`PHPSESSID=<session-id>`** and sends it **in HTTP headers** on subsequent requests.  
- 浏览器保存 **`PHPSESSID=<session-id>`** 并在后续请求里**通过 HTTP 头**发送。  
- The server keeps a **keyed associative array** **`$_SESSION`** as the ledger for that session id.  
- 服务器端以会话标识为键维护**关联数组** **`$_SESSION`** 作为该会话的台账。  

---

## Core Session APIs: `session_start()`, Lifetime, Destroy  
## 核心会话 API：`session_start()`、有效期、销毁

```php
<?php
// Start/continue session BEFORE output / 在输出任何内容前启动或续用会话
session_start();

// set cookie lifetime (seconds) / 设定 Cookie 有效期（秒）
session_set_cookie_params(3600);

// write / read session data / 写入 / 读取会话数据
$_SESSION["id"]   = 123;
$_SESSION["name"] = "Yamazaki";
echo $_SESSION["name"];

// clear one / all / destroy / 清单个 / 清全部 / 销毁
unset($_SESSION["name"]);
$_SESSION = array();
session_destroy(); // also call session_start() in this script first
```
- Call **`session_start()`** **before any output** to send/receive the `PHPSESSID` cookie.  
- **`session_start()`** 必须**先于任何输出**调用，以便发送/接收 `PHPSESSID`。  
- Use **`session_set_cookie_params()`** for **lifetime**; clear with **`unset`/`$_SESSION=array()`**; **`session_destroy()`** removes the **server‑side** session.  
- 用 **`session_set_cookie_params()`** 设定**有效期**；用 **`unset`/`$_SESSION=array()`** 清数据；**`session_destroy()`** 删除**服务器端**会话。  

---

## Login Flow: Save `id`/`name` in `$_SESSION` on Success  
## 登录流程：成功后把 `id`/`name` 存入 `$_SESSION`

```php
<!-- login.html -->
<form method="POST" action="check.php">
  <input name="userID"><input name="password" type="password">
  <button>ログイン</button>
</form>
```
```php
<?php // check.php
session_start();
$u = $_POST["userID"]; $p = $_POST["password"];
include("connect.php");
$r = $conn->query("SELECT * FROM users WHERE userID='{$u}'")->fetch();
$conn = null;

if ($r && $r["password"] === $p) {
  $_SESSION["id"] = $r["id"];
  $_SESSION["name"] = $r["name"];
  header("Location: search.php"); // go to post-login top
  exit;
} else {
  header("Location: login.html"); // or show an error page
  exit;
}
```
- On success, store **`id`** and **`name`** in **`$_SESSION`**, then **redirect** to the top page (e.g., `search.php`).  
- 登录成功后把 **`id`** 与 **`name`** 写入 **`$_SESSION`**，再**转送**到登录后首页（如 `search.php`）。  

---

## Show Username or “Guest” + Logout Button  
## 显示用户名或“Guest”+ 登出按钮

```php
<?php // search.php (top page after login) / 登录后的首页
session_start();
$user = isset($_SESSION["name"]) ? $_SESSION["name"] : "Guest";
echo "<p>{$user} さんログイン中 / {$user} 正在登录</p>";
echo '<form action="logout.php" method="post"><button>ログアウト</button></form>';
```
- If not logged in, display **“Guest”**; offer a **Logout** button to end the session.  
- 未登录则显示 **“Guest”**；提供 **登出** 按钮以结束会话。  

---

## Logout Flow: Clear Session and Redirect  
## 登出流程：清空会话并转送

```php
<?php // logout.php
session_start();
$_SESSION = array();   // clear data
session_destroy();     // destroy server-side session
header("Location: login.html");
exit;
```
- Logout **clears session data** and **destroys** the session, then **redirects** to `login.html`.  
- 登出时**清空会话数据**并**销毁**会话，随后**转送** `login.html`。  

---

## Protect Operations: Allow `delete/update` Only for Self  
## 保护敏感操作：仅允许本人执行 `delete/update`

```php
<?php // delete.php?id=...
session_start();
if (!isset($_SESSION["id"])) { header("Location: login.html"); exit; }

$mine = $_SESSION["id"];
$id   = (int)$_GET["id"];
if ($id !== $mine) { header("Location: login.html"); exit; } // only self

include("connect.php");
$rows = $conn->exec("DELETE FROM users WHERE id={$id}");
echo "Deleted: {$rows}";
$conn = null;
```
- Gate **delete/update** by checking **`$_SESSION["id"]`** against the **target `id`**; otherwise **redirect** to login.  
- 通过比较 **`$_SESSION["id"]`** 与目标 **`id`** 为 **删除/更新**设闸；不匹配则**转送**登录页。  

---

## Quick Checklist  
## 快速清单

- **Stateless HTTP** needs **sessions** to carry identity across requests.  
- **无状态 HTTP** 需用**会话**在多次请求间携带身份。  
- A session = **`PHPSESSID` cookie** + **server `$_SESSION` ledger**.  
- 会话 = **`PHPSESSID` Cookie** + **服务器 `$_SESSION` 台账**。  
- Call **`session_start()` before any output**; store **`id`/`name`** on login success.  
- **在任何输出之前**调用 **`session_start()`**；登录成功时存入 **`id`/`name`**。  
- Provide **logout** to **clear & destroy** the session and **redirect**.  
- 提供 **logout** 以**清空/销毁**会话并**转送**。  
- Restrict **delete/update** to the **logged‑in user** only.  
- 将 **删除/更新** 限定为**当前登录用户本人**。  

---

## Notes  
## 注释

<details><summary>Good practices / 更佳实践</summary>

- After login, **regenerate session id** to prevent **session fixation** (`session_regenerate_id(true)`).  
- 登录后建议**再生成会话 ID**，防止**会话固定攻击**（`session_regenerate_id(true)`）。  
- Set cookie flags: **`httponly`** and **`secure`** (when using HTTPS).  
- 配置 Cookie 标志：**`httponly`** 与 **`secure`**（HTTPS 场景）。  
- Store **password hashes** (e.g., `password_hash`/`password_verify`) instead of plaintext.  
- 口令请存**哈希**（如 `password_hash`/`password_verify`），不要存明文。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture35.md) · [Next Lecture / 下一讲 →](./lecture37.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

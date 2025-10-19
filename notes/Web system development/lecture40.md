[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 40: Final Project — Security, Export, Packaging, and Demo Checklist  
# 第40讲：期末项目 —— 安全性、导出、打包与演示清单

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Assignment Overview & Goals](#assignment-overview--goals)  
- 作业概览与目标
- [Minimum Security: Login Gate & Prepared Statements](#minimum-security-login-gate--prepared-statements)  
- 最低限度的安全：登录闸门与预处理语句
- [SQL Injection Example (Why String Concatenation Is Dangerous)](#sql-injection-example-why-string-concatenation-is-dangerous)  
- SQL 注入示例（为何字符串拼接很危险）
- [Prepared Statements: `prepare` → `execute` → `rowCount`/`fetch`](#prepared-statements-prepare--execute--rowcountfetch)  
- 预处理流程：`prepare` → `execute` → `rowCount`/`fetch`
- [Page Integration: `search` as the Top](#page-integration-search-as-the-top)  
- 页面关联：以 `search` 作为入口
- [UI & Interaction Improvements (HTML/CSS/jQuery/Ajax)](#ui--interaction-improvements-htmlcssjqueryajax)  
- 界面与交互改进（HTML/CSS/jQuery/Ajax）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Assignment Overview & Goals  
## 作业概览与目标

- Build an **original blog system** with the **minimum security** measures in place.  
- 开发一个**原创的博客系统**，并落实**最低限度的安全**措施。  
- The app must **protect operations** when **not logged in** and avoid **SQL injection**.  
- 应用需在**未登录**时**阻止敏感操作**并避免**SQL 注入**。  

---

## Minimum Security: Login Gate & Prepared Statements  
## 最低限度的安全：登录闸门与预处理语句

```php
<?php // At top of create/update/delete scripts / 写在 create/update/delete 开头
session_start();
if (!isset($_SESSION['id'])) {        // not logged in → redirect
  header("Location: login.html");
  exit;
}
```
- **Before processing** create/delete/update, **redirect** unauthenticated users to **`login.html`**.  
- 在执行新增/删除/更新**之前**，若未认证则**转送**到 **`login.html`**。  

```php
// Always use prepared statements / 始终使用预处理语句
$stmt = $conn->prepare("DELETE FROM articles WHERE id=:id AND author=:me");
$ok   = $stmt->execute([":id"=>$id, ":me"=>$_SESSION['id']]);
```
- Replace string‑concatenated SQL with **prepared statements** (bind values via `execute`).  
- 用**预处理语句**替代字符串拼接 SQL（通过 `execute` 绑定值）。  

---

## SQL Injection Example (Why String Concatenation Is Dangerous)  
## SQL 注入示例（为何字符串拼接很危险）

```php
// DANGEROUS: direct concatenation / 危险：直接拼接
$id = $_GET['id'];
$sql = "DELETE FROM articles WHERE id='{$id}'"; // injection risk
```
```
http://localhost/.../delete.php?id=' OR 't' = 't
```
```
DELETE FROM articles WHERE id='' OR 't' = 't'
```
- An attacker can craft input so the **condition is always true**, causing **mass deletion**.  
- 攻击者可构造输入使条件**恒为真**，从而**全表删除**。  

---

## Prepared Statements: `prepare` → `execute` → `rowCount`/`fetch`  
## 预处理流程：`prepare` → `execute` → `rowCount`/`fetch`

```php
// DELETE (returns affected rows with rowCount) / 删除（用 rowCount 返回影响行数）
$st = $conn->prepare("DELETE FROM articles WHERE id=:id");
$st->execute([":id"=>$id]);
$deleted = $st->rowCount();  // similar to exec() return / 类似 exec() 返回值

// SELECT (execute returns boolean; fetch to get record) / SELECT（execute 返回布尔；fetch 取记录）
$st = $conn->prepare("SELECT * FROM articles WHERE id=:id");
$ok = $st->execute([":id"=>$id]);
$r  = $st->fetch();          // or: foreach ($st as $r) {}
```
- **`prepare()`** returns a **`PDOStatement`** (same type as `query()`); **`execute()`** returns **boolean**.  
- **`prepare()`** 返回 **`PDOStatement`**（与 `query()` 同类型）；**`execute()`** 返回**布尔值**。  

---

## Page Integration: `search` as the Top  
## 页面关联：以 `search` 作为入口

```
search → create  (“New”)
search → read?id=…  (click id)
search → update?id=… (“Update”)
search → delete?id=… (“Delete”)
login → check →（success）→ search → logout
```
```
search → create（“新建”）
search → read?id=…（点 id）
search → update?id=…（点“更新”）
search → delete?id=…（点“删除”）
login → check →（成功）→ search → logout
```
- Keep navigation **in‑app** to avoid typing URLs and speed up testing.  
- 通过**应用内导航**避免手动输入 URL，加快测试。  

---

## UI & Interaction Improvements (HTML/CSS/jQuery/Ajax)  
## 界面与交互改进（HTML/CSS/jQuery/Ajax）

- Improve **readability** with **HTML + CSS** (typography, layout, color).  
- 用 **HTML + CSS** 提升**可读性**（字形、布局、配色）。  
- Use **jQuery** to enhance **interactivity**, e.g., show `read.php` **inline** from search results via **Ajax**.  
- 用 **jQuery** 增强**交互**，例如通过 **Ajax** 在搜索结果页**内联显示** `read.php`。  
- Optionally show the **login form** in a **modal dialog**.  
- 可选：在**模态对话框**中显示**登录表单**。  
  

---


## Quick Checklist  
## 快速清单

- Redirect unauthenticated users to **`login.html`** before create/delete/update.  
- 未登录时在新增/删除/更新**前**转送 **`login.html`**。  
- **Never** concatenate untrusted inputs into SQL; use **prepared statements**.  
- **切勿**将不可信输入拼接进 SQL；务必使用**预处理语句**。  
- Confirm **`test.sql`** contains both **schema** and **data**.  
- 确认 **`test.sql`** 同时包含**结构**与**数据**。  
- Submit **all files** + **`test.sql`**; prepare the **demo script** above.  
- 提交**所有文件** + **`test.sql`**；按上文**演示脚本**准备展示。  

---

## Notes
## 注释

<details><summary>Why `rowCount()` matters / 为什么要看 `rowCount()`</summary>
- For **DELETE/UPDATE/INSERT**, `rowCount()` reports **affected rows**; helpful for user feedback.  
- 对 **DELETE/UPDATE/INSERT**，`rowCount()` 可得**受影响行数**；便于反馈给用户。  
</details>

<details><summary>PDO object types / PDO 对象类型说明</summary>
- `prepare()` returns a **PDOStatement** (same as `query()` returns).  
- `prepare()` 返回 **PDOStatement**（与 `query()` 返回类型一致）。  
- `execute()` returns **boolean**; then call **`fetch()`** to read records for **SELECT**.  
- `execute()` 返回**布尔值**；对 **SELECT** 再用 **`fetch()`** 读记录。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture39.md) · [Next Lecture / 下一讲 →](./lecture41.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

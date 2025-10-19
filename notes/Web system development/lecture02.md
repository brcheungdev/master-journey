[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 02: Web Server, FTP (FileZilla), and Links  
# 第02讲：Web 服务器、FTP（FileZilla）与链接

> This file contains my notes, thoughts, and learning summaries during my master's degree study.
> 
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Is FTP](#what-is-ftp)  
- 什么是 FTP
- [Links: Concepts & `<a>` Tag](#links-concepts--a-tag)  
- 链接：概念与 `<a>` 标签
- [External Links (Absolute URL)](#external-links-absolute-url)  
- 外部链接（绝对 URL）
- [Internal Links (Same Site, Relative Paths)](#internal-links-same-site-relative-paths)  
- 站内链接（相对路径）
- [Paths: Absolute vs Relative](#paths-absolute-vs-relative)  
- 路径：绝对与相对
- [Relative Path Patterns: Same/Child/Parent/Sibling](#relative-path-patterns-samechildparentsibling)  
- 相对路径模式：同级/子级/上级/同级不同文件夹
- [`target` Attribute (`_self`, `_blank`, etc.)](#target-attribute-_self-_blank-etc)  
- `target` 属性（`_self`、`_blank` 等）
- [In-Page Anchors (`id`) & `name` (deprecated)](#in-page-anchors-id--name-deprecated)  
- 页面内锚点（`id`）与 `name`（已废弃）
- [Mail Links (`mailto:`)](#mail-links-mailto)  
- 邮件链接（`mailto:`）
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## What Is FTP  
## 什么是 FTP

- **FTP (File Transfer Protocol)** lets creators **upload/download** web content to/from servers.  
- **FTP（文件传输协议）**用于**上传/下载**网站内容到/自服务器。  

```
Creator uses FTP → Upload pages → Server
Viewer uses HTTP(S) → Request pages → Server → Browser renders
创作者用 FTP → 上传页面 → 服务器
访问者用 HTTP(S) → 请求页面 → 服务器 → 浏览器呈现
```

---

## FTP Clients & Protocol Variants  
## FTP 客户端与协议变体

- Common clients: **FFFTP**, **FileZilla**, **WinSCP**.  
- 常见客户端：**FFFTP**、**FileZilla**、**WinSCP**。  
- Secure variants: **FTPS (FTP over SSL/TLS)** and **SFTP (SSH File Transfer Protocol)**.  
- 安全变体：**FTPS（基于 SSL/TLS）**与 **SFTP（基于 SSH）**。  
- Choose a client and protocol **supported by your server**.  
- 请根据**服务器支持**选择客户端与协议。  


---

## Links: Concepts & `<a>` Tag  
## 链接：概念与 `<a>` 标签

- A web page can **link** to other pages identified by **URLs**.  
- 网页可以通过 **URL** 将**链接**指向其他页面。  
- Use the **`<a>` (anchor)** tag with the **`href`** attribute to define a link.  
- 使用 **`<a>`（锚点）**标签，并通过 **`href`** 属性指定链接目标。  

```html
<a href="https://www.kcg.edu/">KCGI</a>
```

---

## External Links (Absolute URL)  
## 外部链接（绝对 URL）

- Use **absolute URLs** starting with **`http://`** or **`https://`**.  
- 使用以 **`http://`** 或 **`https://`** 开头的**绝对 URL**。  

```html
<a href="https://www.kcg.edu/">Visit KCGI</a>
```

---

## Internal Links (Same Site, Relative Paths)  
## 站内链接（相对路径）

- You can link to **pages on the same server** using **relative paths**.  
- 可以用**相对路径**链接到**同一服务器**上的页面。  

```html
<!-- same folder -->
<a href="profile.html">Profile</a>
<!-- child folder -->
<a href="folderB/profile.html">Profile in folderB</a>
```

---

## Paths: Absolute vs Relative  
## 路径：绝对与相对

- **Absolute path**: a full URL, typically for **other sites** or resources.  
- **绝对路径**：完整 URL，常用于**其他网站**或资源。  
- **Relative path**: relative to the **current document’s location**.  
- **相对路径**：相对于**当前文档位置**进行描述。  
- Special segments: **`.`** (current folder), **`..`** (parent folder), **`/`** (path separator).  
- 常用段：**`.`**（当前目录）、**`..`**（上级目录）、**`/`**（路径分隔）。  

---

## Relative Path Patterns: Same/Child/Parent/Sibling  
## 相对路径模式：同级/子级/上级/同级不同文件夹

- **Same folder**: just the filename.  
- **同级目录**：直接写文件名。  
  - `index.html` → `profile.html` as `<a href="profile.html">`  
  - `index.html` → `profile.html` 写成 `<a href="profile.html">`  
- **Child folder**: include the **child folder** and filename.  
- **子级目录**：写**子目录名**与文件名。  
  - `<a href="folderB/profile.html">`  
  - `<a href="folderB/profile.html">`  
- **Parent folder**: prefix with **`../`**.  
- **上级目录**：用 **`../`** 前缀。  
  - `<a href="../index.html">`  
  - `<a href="../index.html">`  
- **Sibling folder**: go up, then into the sibling.  
- **同级其他文件夹**：先返回上级，再进入同级目录。  
  - `<a href="../folderC/hobby.html">`  
  - `<a href="../folderC/hobby.html">`  

---

## `target` Attribute (`_self`, `_blank`, etc.)  
## `target` 属性（`_self`、`_blank` 等）

- Controls **where** to open the linked page.  
- 控制链接页面**在何处打开**。  
- `_self` (default): **current tab**; `_blank`: **new tab/window**.  
- `_self`（默认）：**当前标签**；`_blank`：**新标签/窗口**。  

```html
<a href="hobby.html" target="_blank">Open in new tab</a>
```

---

## In-Page Anchors (`id`) & `name` (deprecated)  
## 页面内锚点（`id`）与 `name`（已废弃）

- To jump **within the same page**, assign an **`id`** and link to `#id`.  
- 在**同一页面内跳转**：给目标元素设置 **`id`**，链接写成 `#id`。  

```html
<h1 id="top">TOP</h1>
<a href="#top">Back to TOP</a>
```

- The old `<a name="top">` method is **deprecated** in HTML5.  
- 旧式的 `<a name="top">` 在 HTML5 中**已废弃**。  

---

## Mail Links (`mailto:`)  
## 邮件链接（`mailto:`）

- Use `mailto:` to open the default mail app for a recipient.  
- 使用 `mailto:` 打开默认邮件客户端并填入收件人。  

```html
<a href="mailto:h_an@kcg.ac.jp">Questions? Email here</a>
```

---

## Quick Checklist  
## 快速清单

- Use **relative paths** for internal linking; **absolute URLs** for off‑site links.  
- **站内链接用相对路径**；**站外链接用绝对 URL**。  
- Prefer **semantic HTML**, keep filenames **lowercase**, avoid spaces.  
- **语义化 HTML**；文件名**小写**，避免空格。  
- For new tabs, use **`target="_blank"`**; for in‑page jumps, use **`id`/`#id`**.  
- 新标签页使用 **`target="_blank"`**；页面内跳转使用 **`id`/`#id`**。  


<h2></h2>

[← Previous Lecture / 上一讲](./lecture01.md) · [Next Lecture / 下一讲 →](./lecture03.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

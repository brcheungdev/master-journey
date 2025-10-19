[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 01: Web Page Basics  
# 第01讲：网页基础

> This file contains my notes, thoughts, and learning summaries during my master's degree study.
> 
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- World Wide Web Overview  
- World Wide Web 概述
- How Websites Work  
- 网站的工作机制
- Web Browsers  
- Web 浏览器
- URL and Its Structure  
- URL 及其结构
- Domain Names  
- 域名
- Encrypted Communication: HTTP vs HTTPS (SSL/TLS)  
- 加密通信：HTTP 与 HTTPS（SSL/TLS）
- Ways to Create Web Pages (Editors & Tools)  
- 创建网页的方法（编辑器与工具）
- What Makes Up a Web Page (HTML/CSS/Assets)  
- 网页由哪些部分组成（HTML/CSS/资源）
- HTML & CSS Responsibilities  
- HTML 与 CSS 的职责分工
- Viewing Page Source  
- 查看页面源代码
- HTML Document Skeleton  
- HTML 文档骨架
- Tags, Elements & Doctype  
- 标签、元素与文档类型声明
- Core Head Elements: `<html>`, `<head>`, `<meta>`, `<title>`, `<body>`  
- 核心头部与主体元素：`<html>`、`<head>`、`<meta>`、`<title>`、`<body>`
- Authoring Workflow (VS Code → Save → Refresh)  
- 编写流程（VS Code → 保存 → 刷新）
- Text Structure: `<br>`, `<p>`, Headings `<h1>`–`<h6>`, `<hr>`, `<strong>`, `<em>`  
- 文本结构：`<br>`、`<p>`、标题 `<h1>`–`<h6>`、`<hr>`、`<strong>`、`<em>`

---

## World Wide Web Overview  
## World Wide Web 概述

- **Before the early 1990s**, the Internet was mainly used by academic institutions for **file sharing** and **email**.  
- **1990年代初以前**，互联网主要由学术机构用于**文件共享**与**电子邮件**。  
- With the **invention of the WWW**, ordinary users could easily access rich information (including images), and together with the success of **Windows 95**, the Internet spread rapidly.  
- 随着 **WWW（万维网）** 的发明，普通人也能轻松访问包含图像的丰富信息，并在 **Windows 95** 大获成功的推动下，互联网实现了爆发式普及。  
- Even **without prior programming experience**, users could create web pages, and both **personal** and **commercial** websites flourished.  
- 即使**没有编程经验**也能制作网页，**个人站点**与**商业站点**大量涌现。  
- Today, with **smartphone** adoption, it’s hard to imagine life **without websites**.  
- 今天，随着**智能手机**的普及，几乎难以想象**没有网站**的生活。  

```
Timeline (simplified) / 时间线（简化）
1980s: Academic use (files, email)
1990s: WWW invented → Win95 popularized the Internet
2000s–: Personal & commercial sites explode
Today: Smartphones + Web = daily life
```

---

## How Websites Work  
## 网站的工作机制

- The **site author** creates pages and **uploads** them to a **Web server**.  
- **网站作者**创建页面并将其**上传**到**Web 服务器**。  
- The **Web server** sends page contents **in response** to **viewer requests**.  
- **Web 服务器**根据**访问者请求**发送**页面内容**。  

```
+-------------------+           request            +------------------+
|  Viewer           | ---------------------------> |  Web Server      |
|  访问者            |                               |  Web 服务器        |
+-------------------+ <--------------------------- +------------------+
            response / 页面内容
```

---

## Web Browsers  
## Web 浏览器

- To view pages you need a **Web browser** (e.g., **Edge, Firefox, Chrome, Safari, Opera**).  
- 查看网页需要**浏览器**（如 **Edge、Firefox、Chrome、Safari、Opera**）。  
- **This course assumes Chrome.**  
- **本课程默认使用 Chrome。**  

---

## URL (Uniform Resource Locator)  
## URL（统一资源定位符）

- A **URL is the address** of a Web page and **identifies** where the page is on the Internet.  
- **URL 是网页的“地址”**，用于**定位**页面在互联网上的位置。  
- A URL consists of **protocol (scheme)**, **server/host name**, **domain**, **folder/path**, and **file name**.  
- URL 由**协议（scheme）**、**服务器/主机名**、**域名**、**目录/路径**与**文件名**等组成。  

**Example** / **示例**  
`http://www.kcg.edu/school_info/`

```
scheme     host / domain            path
http://     www.kcg.edu             /school_info/
协议         主机/域名                路径
```

---

### URL Structure  
### URL 的结构

- **Scheme**: indicates how to access the resource (e.g., `http`, `https`, `ftp`, `mailto`, `file`).  
- **方案（Scheme）**：表示访问资源的方式（如 `http`、`https`、`ftp`、`mailto`、`file`）。  
- **Host name**: which host holds the resource, typically **computer name + domain**.  
- **主机名（Host）**：资源所在的主机，通常由**计算机名 + 域名**组成。  
- **Path**: details that locate the resource, often **file** or **directory** in a file system.  
- **路径（Path）**：用于定位资源的详细信息，常对应文件系统中的**文件或目录**。  

---

## Domain Names  
## 域名

- A domain name **identifies computers or networks** on the Internet.  
- 域名用于**识别互联网上的计算机或网络**。  
- Like a real-world **address**, domains are **unique** and centrally managed.  
- 类似现实世界的**地址**，域名**唯一**且由机构统一管理。  
- Domains are **hierarchical**, separated by **dots (`.`)**: **TLD** at the right, then **second-level**, **third-level**, etc.  
- 域名是**分层结构**，用 **点（`.`）** 分隔：最右为**顶级域（TLD）**，向左依次为**二级域**、**三级域**等。  

```
example: www.kcg.edu
     └─ edu (TLD 顶级域)
        └─ kcg (2nd level 二级)
           └─ www (host 主机)
```

---

## Encrypted Communication: HTTP vs HTTPS  
## 加密通信：HTTP 与 HTTPS

- **`http` transmits in plaintext**; it’s **unsafe** for IDs, passwords, or personal data.  
- **`http` 以明文传输**；在输入账号、密码或个人信息时**不安全**。  
- Use **`https`** (SSL/TLS) for **encrypted** transport at the **transport layer**.  
- 使用 **`https`**（SSL/TLS）在**传输层**对数据进行**加密**。  
- **SSL (Secure Sockets Layer)** / **TLS (Transport Layer Security)** is widely used **beyond the Web** as well.  
- **SSL**（安全套接层）/ **TLS**（传输层安全）不仅用于 Web，在其他场景也被广泛使用。  

---

## Ways to Create Web Pages  
## 创建网页的方法

- Use **specialized tools** (e.g., **Adobe Dreamweaver**, **Homepage Builder**).  
- 使用**专用工具**（如 **Adobe Dreamweaver**、**Homepage Builder**）。  
- Or use a **text editor** (e.g., **Visual Studio Code**, **Notepad++**, **Sublime Text**, **Atom**).  
- 或使用**文本编辑器**（如 **Visual Studio Code**、**Notepad++**、**Sublime Text**、**Atom**）。  
- **This course uses VS Code.**  
- **本课程使用 VS Code。**  

---

## What Makes Up a Web Page  
## 网页由哪些部分组成

- A single page centers on an **HTML file**, plus **images**, **CSS** for layout/appearance, and other assets.  
- 单个网页以 **HTML 文件**为核心，结合**图片**、用于布局/样式的 **CSS** 及其他资源。  
- The browser **downloads related files** from the Web server and **renders** them as **one page**.  
- 浏览器从 Web 服务器**下载相关文件**，并**组合渲染**为**一个页面**。  

```
HTML + CSS + Images + Links → Rendered Page
HTML + CSS + 图片 + 链接 → 渲染后的页面
```

---

## HTML (HyperText Markup Language)  
## HTML（超文本标记语言）

- HTML defines **document structure** (text/image placement, links), **not the content itself**.  
- HTML 定义**文档结构**（文字/图像的布局与链接），**而非内容本身**。  
- It uses **tags** enclosed in `< >` — hence a **markup language**.  
- 使用包围在 `< >` 中的**标签**进行描述，因此称为**标记语言**。  
- **Hypertext** means **text containing references** (links) to other text.  
- **超文本**是指**包含对其他文本引用**（链接）的文本。  

---

## CSS (Cascading Style Sheets)  
## CSS（层叠样式表）

- HTML alone can control some presentation; **CSS** provides **fine-grained layout and styling**.  
- 仅用 HTML 也能做少量展示控制；但 **CSS** 可实现**更细致**的布局与样式。  
- CSS can be **embedded** in HTML or placed in **separate files** (best practice).  
- CSS 可**内嵌**于 HTML 或**独立文件**（推荐做法）。  
- **Division of roles**: **HTML** for **structure**; **CSS** for **presentation/design**.  
- **职责分工**：**HTML** 负责**结构**；**CSS** 负责**展示/设计**。  

---

## Viewing Page Source  
## 查看页面源代码

- Open a site (e.g., `https://www.kcg.edu/`) and view **page source**.  
- 打开网站（如 `https://www.kcg.edu/`），查看**页面源代码**。  
- On Mac Chrome: **View → Developer → View Source**; on Windows: **Right click → View page source**.  
- Mac 版 Chrome：**显示 → 开发/管理 → 显示源**；Windows：**右键 → 查看页面源代码**。  

---

## “Source Code”  
## “源代码”

- **Source code** is a set of **computer instructions** written per language specifications.  
- **源代码**是按语言规范编写的**计算机指令序列**。  

---

## HTML Document Skeleton  
## HTML 文档骨架

- Everything (except `<!DOCTYPE>`) lives **inside** `<html> ... </html>`.  
- 除 `<!DOCTYPE>` 外，所有内容都位于 **`<html> ... </html>`** 中。  

```html
<!DOCTYPE html>           <!-- declares HTML5 -->
<html lang="en">          <!-- 文档语言 -->
  <head>                  <!-- 文档信息（不直接显示） -->
    <!-- meta, title, links, styles, etc. -->
  </head>
  <body>                  <!-- 页面可见内容 -->
    <!-- headings, paragraphs, tables, forms... -->
  </body>
</html>
```

---

## Tags and Elements  
## 标签与元素

- A **tag** is an element name wrapped with `<` and `>`; write tags in **ASCII lowercase**.  
- **标签**是用 `<` 与 `>` 包裹的元素名；标签使用 **ASCII 小写**书写。  
- Most elements have a **start tag** and an **end tag**; together they form an **element**.  
- 多数元素有**开始标签**与**结束标签**，合在一起称为**元素**。  

```html
<p> ...content... </p>    <!-- <p> 是开始标签，</p> 是结束标签 -->
```

---

## `<!DOCTYPE>` (Document Type Declaration)  
## `<!DOCTYPE>`（文档类型声明）

- Placed at the **top** of the file; declares the **DTD / standard**.  
- 位于文档**最顶部**；用于声明**DTD/标准**。  
- `<!DOCTYPE html>` declares **HTML5**.  
- `<!DOCTYPE html>` 表示该文档为 **HTML5**。  
- **Note**: the declaration **differs by version** in older HTML specs.  
- **注意**：早期 HTML 版本的声明**写法不同**。  

---

## `<html>` Tag  
## `<html>` 标签

- Wraps the **entire HTML document**; commonly includes a `lang` attribute.  
- 包裹**整个 HTML 文档**；通常包含 `lang` 属性。  
- Example: `<html lang="ja">`.  
- 示例：`<html lang="ja">`。  

---

## `<head>` Tag  
## `<head>` 标签

- Holds **document metadata**: title, base URL, links, styles, authorship info, etc.  
- 保存**文档元信息**：标题、基准 URL、链接、样式、作者信息等。  

---

## `<meta>` Tag  
## `<meta>` 标签

- For document **metadata** such as **character encoding**, **keywords**, **description**, and **author**.  
- 用于**元数据**，如**字符编码**、**关键词**、**摘要**与**作者**。  

```html
<meta charset="utf-8">
<meta name="description" content="...">
<meta name="keywords" content="...">
<meta name="author" content="...">
```

---

## `<title>` Tag  
## `<title>` 标签

- Sets the **page title** (shown on the **tab** and used for **bookmarks/favorites**).  
- 指定**页面标题**（显示在浏览器**标签**上，也用于**书签**名称）。  

---

## `<body>` Tag  
## `<body>` 标签

- Contains the **visible content** of the page. Only **one** `<body>` per document.  
- 放置页面的**可见内容**；每个文档**仅有一个** `<body>`。  
- Inside it go headings, paragraphs, tables, forms, etc.  
- 其中可包含标题、段落、表格、表单等元素。  

---

## Authoring Workflow  
## 编写流程

1. Write HTML source in **VS Code**.  
1. 在 **VS Code** 中编写 HTML 源码。  
   - Fill **`<head>`** with document info; **`<body>`** with visible content.  
   - 在 **`<head>`** 写文档信息；在 **`<body>`** 写可见内容。  
2. **Save** the HTML file (`Ctrl+S` / `Cmd+S`).  
2. **保存** HTML 文件（`Ctrl+S` / `Cmd+S`）。  
3. **Open & verify** in a browser (double-click in Explorer, or VS Code “Open in Other Browsers” → Chrome).  
3. 在浏览器中**打开与查看**（资源管理器双击，或 VS Code“Open in Other Browsers”→ 选择 Chrome）。  
4. After edits, **save** and **refresh** the browser (Refresh button or **F5**).  
4. 修改后**保存**并**刷新**浏览器（刷新按钮或 **F5**）。  

---

## Text & Structure Elements  
## 文本与结构元素

### `<br>`: Line Break  
### `<br>`：换行

- In HTML, multiple spaces or newlines in source render as **a single space**.  
- 在 HTML 中，源码里多个空格或换行会被渲染为**一个空格**。  
- Use `<br>` to **force a line break**; it has **no closing tag**.  
- 使用 `<br>` **强制换行**；它**没有结束标签**。  
- **Avoid** stacking many `<br>` just to create spacing.  
- **避免**用多个 `<br>` 来制造大空白。  

```html
Line 1<br>
Line 2
```

---

### `<p>`: Paragraph  
### `<p>`：段落

- Wrap paragraphs with `<p> ... </p>`; browsers typically insert **one blank line** between paragraphs.  
- 用 `<p> ... </p>` 包裹段落；浏览器通常在段落之间**空一行**。  

```html
<p>This is a paragraph.</p>
<p>这是一个段落。</p>
```

---

### Headings `<h1>`–`<h6>`  
### 标题 `<h1>`–`<h6>`

- Provide **section headings** and are rendered **bold**; there are **six levels**.  
- 用于创建**章节标题**且常为**粗体**显示；共有**六级**。  
- **Smaller number = larger text** (`h1` largest, `h6` smallest).  
- **数字越小字体越大**（`h1` 最大，`h6` 最小）。  
- Use them to reflect **hierarchy**, **not to change size**.  
- 根据**内容层级**选择，不要仅为**变大字体**而使用。  

---

### `<hr>`: Thematic Break  
### `<hr>`：主题分隔线

- Indicates a **section break** (thematic change).  
- 表示**主题/段落的分隔**。  
- **Do not** use `<hr>` to **draw lines**; use **CSS** for visual rules.  
- **不要**用 `<hr>` 画装饰线；绘制直线应使用 **CSS**。  

---

### `<strong>` and `<em>`  
### `<strong>` 与 `<em>`

- `<strong>` marks **importance**; `<em>` marks **emphasis** (stress).  
- `<strong>` 表示**重要性**；`<em>` 表示**强调（语气重读）**。  
- Rendering can vary by font; some fonts may not visibly change for `<em>`.  
- 实际显示取决于字体；部分字体对 `<em>` 的视觉变化不明显。  

```html
<p><strong>Important:</strong> use semantic tags.</p>
<p><em>Emphasis</em> may render subtly.</p>
```

---

## Quick Checklist  
## 快速清单

- Use **semantic HTML**; separate **structure** (HTML) from **presentation** (CSS).  
- 使用**语义化 HTML**；将**结构**（HTML）与**表现**（CSS）分离。  
- Prefer **HTTPS** for any page handling **personal data**.  
- 处理**个人信息**的页面应优先使用 **HTTPS**。  
- Keep titles, meta, and language settings **complete and correct**.  
- **标题、meta 与语言设置**要完整、正确。  
- Test changes with **save + refresh** cycle.  
- 通过**保存 + 刷新**循环验证修改效果。  

---

## Appendix: Minimal HTML5 Template  
## 附录：最小 HTML5 模板

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p>This is a minimal HTML5 page.</p>
  </body>
</html>
```

---

> Notes expand the original slides into structured, bilingual text while preserving all key points (WWW history, URL parts, domain hierarchy, HTTP/HTTPS, tools, HTML/CSS roles, document skeleton, authoring flow, and fundamental tags).  
> 本笔记在保留要点的基础上做了结构化与双语扩展（WWW 历史、URL 组成、域名层次、HTTP/HTTPS、工具、HTML/CSS 分工、文档骨架、编写流程与基础标签）。
>  
---

[Next Lecture / 下一讲 →](./lecture02.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 26: AJAX (XMLHttpRequest) and Google Maps JavaScript API  
# 第26讲：AJAX（XMLHttpRequest）与 Google Maps JavaScript API

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Synchronous vs Asynchronous Communication](#synchronous-vs-asynchronous-communication)  
- 同步通信 vs 非同步通信
- [What Is AJAX](#what-is-ajax)  
- 什么是 AJAX
- [Implementing AJAX with `XMLHttpRequest`](#implementing-ajax-with-xmlhttprequest)  
- 用 `XMLHttpRequest` 实现 AJAX
- [Exercise 1: Load `data13-1.txt` into `#content` (textContent)](#exercise-1-load-data13-1txt-into-content-textcontent)  
- 练习1：将 `data13-1.txt` 加载到 `#content`（textContent）
- [Exercise 2: Load `data13-2.html` into `#content` (innerHTML)](#exercise-2-load-data13-2html-into-content-innerhtml)  
- 练习2：将 `data13-2.html` 加载到 `#content`（innerHTML）
- [Same‑Origin Note & Error Handling (`error` event)](#sameorigin-note--error-handling-error-event)  
- 同源限制与错误处理（`error` 事件）
- [Google Maps JS API: Load Script with API Key](#google-maps-js-api-load-script-with-api-key)  
- Google Maps JS API：携带 API Key 加载脚本
- [Initialize a Map (`initMap`), Center/Zoom](#initialize-a-map-initmap-centerzoom)  
- 初始化地图（`initMap`）、中心与缩放
- [Add a Marker](#add-a-marker)  
- 添加标记（Marker）
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## Synchronous vs Asynchronous Communication  
## 同步通信 vs 非同步通信

- **Synchronous**: the browser **waits** for the server response; during processing, the UI is **blocked**.  
- **同步通信**：浏览器**等待**服务器响应；处理期间界面**被阻塞**。  

```
Browser → Request → Server (processing...) → Response → Browser updates UI
浏览器 → 请求 → 服务器（处理中…）→ 响应 → 浏览器更新界面
```

- **Asynchronous**: the browser can **continue other work** while the server is processing; when the response arrives, a **handler** runs.  
- **非同步通信**：服务器处理时浏览器可**继续其他任务**；响应到达时触发**处理函数**。  

```
Browser → Request → (continue doing other things) … → Response event → Handler runs
浏览器 → 请求 →（继续做其他事）… → 响应事件 → 处理函数执行
```

---

## What Is AJAX  
## 什么是 AJAX

- **AJAX = Asynchronous JavaScript and XML**: JavaScript **fetches content from a URL asynchronously** and **partially updates** the current page.  
- **AJAX = Asynchronous JavaScript and XML**：用 JavaScript **异步获取 URL 指向的内容**，并**局部更新**当前页面。  

```
JavaScript —(request URL / 请求 URL)→ Server or Local file
←— content/response / 内容/响应 —
Update part of DOM / 局部更新 DOM
```

---

## Implementing AJAX with `XMLHttpRequest`  
## 用 `XMLHttpRequest` 实现 AJAX

- Pattern: **(1)** create **request object**, **(2)** register **`load` listener** to process `responseText`, **(3)** `open` with method+URL, **(4)** `send`.  
- 基本流程：**（1）** 创建**请求对象**，**（2）** 注册 **`load` 监听**处理 `responseText`，**（3）** 用方法+URL **`open`**，**（4）** **`send`** 发送。  

```html
<!-- wp13-1.html -->
<button id="btn">Load</button>
<div id="content">-</div>

<script>
  document.querySelector("#btn").addEventListener("click", () => {
    // (1) create request object / 创建请求对象
    const req = new XMLHttpRequest();

    // (2) on load: use the received text to update the page / 载入后更新页面
    req.addEventListener("load", () => {
      document.querySelector("#content").textContent = req.responseText;
    });

    // (3) set up method and relative URL (same folder) / 设定方法与相对URL（同目录）
    req.open("GET", "data13-1.txt");

    // (4) send request / 发送
    req.send();
  });
</script>
```

---

## Exercise 1: Load `data13-1.txt` into `#content` (textContent)  
## 练习1：将 `data13-1.txt` 加载到 `#content`（textContent）

- **Goal**: when the button is clicked, fetch **`data13-1.txt`** (same folder) and write it into **`#content.textContent`**.  
- **目标**：点击按钮，获取同目录 **`data13-1.txt`**，写入 **`#content.textContent`**。  

```text
Files to upload / 需上传的文件：
wp13-1.html
data13-1.txt
Target folder / 目标目录：public_html/web2/wp13/
```

---

## Exercise 2: Load `data13-2.html` into `#content` (innerHTML)  
## 练习2：将 `data13-2.html` 加载到 `#content`（innerHTML）

- Change the URL to **`data13-2.html`** and assign **`req.responseText`** to **`#content.innerHTML`** to render markup.  
- 将 URL 改为 **`data13-2.html`**，并把 **`req.responseText`** 赋给 **`#content.innerHTML`** 以渲染 HTML。  

```html
req.addEventListener("load", () => {
  document.querySelector("#content").innerHTML = req.responseText;
});
req.open("GET", "data13-2.html");
req.send();
```

---

## Same‑Origin Note & Error Handling (`error` event)  
## 同源限制与错误处理（`error` 事件）

- For security, **AJAX typically must access the same domain** (use **relative paths** under your server space).  
- 出于安全，**AJAX 通常必须访问同一域名**（在自己的服务器空间下使用**相对路径**）。  
- If the content **fails to load**, the **`error` event** fires; handle it with an **event listener**.  
- 若**获取失败**会触发 **`error` 事件**；用**事件监听**进行处理。  

```js
req.addEventListener("error", () => {
  console.log("エラー発生 / Error occurred");
});
```

---

## Google Maps JS API: Load Script with API Key  
## Google Maps JS API：携带 API Key 加载脚本

- Include the **Google Maps JavaScript API** via `<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>`.  
- 通过 `<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>` 引入 **Google Maps JavaScript API**。  

```html
<!-- wp13-map.html -->
<style>#mymap{width:640px;height:480px}</style>
<div id="mymap"></div>

<script src="https://maps.googleapis.com/maps/api/js?key=API_KEY&callback=initMap" async defer></script>
<script>
  function initMap(){
    const target = document.querySelector("#mymap");
    const location = { lat: 34.9948282, lng: 135.7848819 }; // 清水寺 / Kiyomizu-dera
    let map = new google.maps.Map(target, { center: location, zoom: 14 });
  }
</script>
```

- **`key`** is your API key; **`callback`** names the function to call **after** the API loads; **`async`/`defer`** load the script **asynchronously**.  
- **`key`** 为你的 API 密钥；**`callback`** 指 API 加载后要调用的函数；**`async`/`defer`** 以**异步**方式加载脚本。  

---

## Initialize a Map (`initMap`), Center/Zoom  
## 初始化地图（`initMap`）、中心与缩放

- Create a map with `new google.maps.Map(target, { center, zoom })`; **`zoom`** ranges from **1 (world)** to **~20 (building)**.  
- 通过 `new google.maps.Map(target, { center, zoom })` 创建地图；**`zoom`** 范围 **1（世界）**到 **约20（建筑）**。  

```js
const target = document.querySelector("#mymap");
const location = { lat: 34.9948282, lng: 135.7848819 };
let map = new google.maps.Map(target, { center: location, zoom: 14 });
```

---

## Add a Marker  
## 添加标记（Marker）

- Create a **marker** with `new google.maps.Marker({ position, map, title })` to pin the location.  
- 用 `new google.maps.Marker({ position, map, title })` 在地图上**打点**。  

```js
let marker = new google.maps.Marker({
  position: location,
  map: map,
  title: "目的地 / Destination"
});
```

---

## Quick Checklist  
## 快速清单

- Use **`XMLHttpRequest`**: create → listen **`load`**/**`error`** → `open("GET", "<relative URL>")` → `send()`.  
- 使用 **`XMLHttpRequest`**：创建 → 监听 **`load`**/**`error`** → `open("GET", "<相对URL>")` → `send()`。  
- Write **plain text** with **`textContent`**; write **HTML** with **`innerHTML`**.  
- **纯文本**用 **`textContent`**；**HTML** 用 **`innerHTML`**。  
- Keep requests **same‑origin** (relative paths under your account on `web1.kcg.edu`).  
- 保持**同源**（在 `web1.kcg.edu` 自己账号下用**相对路径**）。  
- For Google Maps: **script with `key` + `callback`**, implement **`initMap`**, set **`center`** and **`zoom`**, optionally add **markers**.  
- 对 Google 地图：**带 `key` 与 `callback` 的脚本**，实现 **`initMap`**，设置 **`center`** 与 **`zoom`**，并可添加 **标记**。  

---

## Notes  
## 注释（

<details><summary>Modern alternative: <code>fetch()</code> / 现代替代方案：<code>fetch()</code></summary>

- While this lecture uses **`XMLHttpRequest`**, modern code often prefers **`fetch()`** with **Promises/`async`–`await`**.  
- 虽然本讲使用 **`XMLHttpRequest`**，但现代代码更常用带 **Promise/`async`–`await`** 的 **`fetch()`**。  

```js
// Example: text / 文本
const s = await (await fetch("data13-1.txt")).text();
document.querySelector("#content").textContent = s;

// Example: HTML / HTML 片段
const h = await (await fetch("data13-2.html")).text();
document.querySelector("#content").innerHTML = h;
```
</details>

---

[← Previous Lecture / 上一讲](./lecture25.md) · [Next Lecture / 下一讲 →](./lecture27.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

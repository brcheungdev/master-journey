[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 19: JavaScript Programming Notation & Task 06 — Converting Exercises to DOM Apps  
# 第19讲：JavaScript 编程记号速查 & 第6回任务 —— 将练习改造成 DOM 应用

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [Overview & Goals](#overview--goals)  
- 课程概览与目标
- [Programming Notation Cheat Sheet](#programming-notation-cheat-sheet)  
- 编程记号速查表
- [Quoting Strategies for HTML Attributes](#quoting-strategies-for-html-attributes)  
- HTML 属性中的引号策略
- [Separators: Semicolon, Comma, Colon](#separators-semicolon-comma-colon)  
- 分隔符：分号、逗号、冒号
- [Operators & Special Signs](#operators--special-signs)  
- 运算符与常用符号
- [Task 06: Convert Prompt/Alert Apps to DOM I/O](#task-06-convert-promptalert-apps-to-dom-io)  
- 任务06：把 prompt/alert 程序改造成 DOM 入出力
- [Exercise A: Four Operations (with Buttons)](#exercise-a-four-operations-with-buttons)  
- 练习A：四则运算（带按钮）
- [Exercise B: Coin Change (Greedy, JPY)](#exercise-b-coin-change-greedy-jpy)  
- 练习B：硬币找零（贪心，日元）
- [Exercise C: Grade Evaluation (Ranges & Validation)](#exercise-c-grade-evaluation-ranges--validation)  
- 练习C：成绩判定（区间与校验）
- [Exercise D: Three Greeting Buttons (Console → HTML)](#exercise-d-three-greeting-buttons-console--html)  
- 练习D：三个问候按钮（控制台 → HTML）
- [Exercise E: Number Guessing Game (1–100)](#exercise-e-number-guessing-game-1100)  
- 练习E：数当て游戏（1–100）
- [Submission Rules](#submission-rules)  
- 提交规范
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes (Optional)](#notes-optional)  
- 注释（可选）

---

## Overview & Goals  
## 课程概览与目标

- Summarize **common programming notations** (parentheses/brackets/quotes, separators, operators, selectors).  
- 总结**常用编程记号**（圆/花/方括号、引号、分隔符、运算符、选择器）。  
- Upgrade earlier exercises so **inputs/outputs** happen **inside the web page** using **DOM** (no `prompt/alert` for main UI).  
- 将前面练习**升级**为使用 **DOM** 在**页面内**完成**输入/输出**（主交互不再使用 `prompt/alert`）。 

---

## Programming Notation Cheat Sheet  
## 编程记号速查表

- **Parentheses `()`** — wrap **conditions** and **arguments**; e.g., `if (cond) {}`, `window.alert()`.  
- **圆括号 `()`** —— 包裹**条件**与**参数**；如 `if (条件) {}`、`window.alert()`。 
- **Braces `{}`** — **blocks** and **object literals**; e.g., `{ id: 'M10W999', name: "星野" }`, `function(){...}`.  
- **花括号 `{}`** —— **代码块**与**对象字面量**；示例 `{ id: 'M10W999', name: "星野" }`、`function(){...}`。 
- **Brackets `[]`** — **index/key** access; e.g., `obj["key"]`, `arr[1]`.  
- **方括号 `[]`** —— **索引/键**访问；如 `obj["key"]`、`arr[1]`。 
- **Quotes `'…'` / `"…"`** — define **strings**; mix `'` outside, `"` inside for HTML attributes with JS calls.  
- **引号 `'…'` / `"…"`** —— 定义**字符串**；HTML 属性中 JS 调用常用**外单内双**的嵌套写法。 
- **Dot `.`** — **property/method** access: `document.querySelector()`, `student.id` (**not** “period”).  
- **点号 `.`** —— **属性/方法**访问：`document.querySelector()`、`student.id`（编程中**不称 period**）。 
- **Hash `#`** — **id selector** in CSS/DOM queries: `document.querySelector("#btn")` (`.` for class).  
- **井号 `#`** —— CSS/DOM 查询的 **id 选择器**：`document.querySelector("#btn")`（类选择器用 `.`）。 
- **Semicolon `;`** — **end of statement**.  
- **分号 `;`** —— **语句结束符**。 
- **Comma `,`** — **property/value** separators or **selector** separators: `{ id:'M10W999', name:"星野" }`, `h1, h2, h3`.  
- **逗号 `,`** —— **属性/值**分隔或**选择器**分隔：`{ id:'M10W999', name:"星野" }`、`h1, h2, h3`。 
- **Colon `:`** — used in **key–value** pairs and `switch case` syntax.  
- **冒号 `:`** —— 用于**键值对**与 `switch case` 语法。 
- **Exclamation `!`** — **logical NOT** and `!=` **inequality**.  
- **感叹号 `!`** —— **逻辑非**与 `!=` **不等**。 
- **Asterisk `*`** / **Slash `/`** — **multiply/divide**; also `/` in **paths/URLs**: `user/web2/css`.  
- **星号 `*`** / **斜杠 `/`** —— **乘/除**；`/` 也用于**路径/URL**：`user/web2/css`。 
- **Hyphen `-`** — **subtraction**; also used in CSS property names (JS uses **camelCase**).  
- **连字符 `-`** —— **减法**；亦用于 CSS 属性名（在 JS 中改用**小驼峰**）。 
- **Ampersand `&`**, **Vertical bar `|`** — make **`&&`** (AND) and **`||`** (OR).  
- **与号 `&`**、**竖线 `|`** —— 组成 **`&&`**（且）与 **`||`**（或）。 
- **Backslash `\`** — escape sequences like **`\n`** for **newline**.  
- **反斜杠 `\`** —— 转义序列，如 **`\n`** 表示**换行**。 
- **Underscore `_`**, **Tilde `~`** — commonly seen in identifiers or shell patterns.  
- **下划线 `_`**、**波浪号 `~`** —— 常见于标识符或命令行模式中。 

---

## Quoting Strategies for HTML Attributes  
## HTML 属性中的引号策略

```html
<!-- outer single quotes, inner double quotes / 外单内双 -->
<button onclick='show("どかーん")'>OK</button>
```
- Use **outer `'…'`** for the **HTML attribute**, and **inner `"…"`** for **JS string** to avoid escaping.  
- 对 **HTML 属性**用**外层单引号**，对 **JS 字符串**用**内层双引号**，避免转义冲突。 

---

## Separators: Semicolon, Comma, Colon  
## 分隔符：分号、逗号、冒号

- **` ; `** ends **statements**; **`,`** separates **properties** or **selectors**; **`:`** separates **keys and values** or labels `case:`.  
- **` ; `** 结束**语句**；**`,`** 分隔**属性**或**选择器**；**`:`** 用于**键值分隔**或 `case:` 标签。 

---

## Operators & Special Signs  
## 运算符与常用符号

- Arithmetic: **`+ - * /`**; Comparison: **`< <= > >= == === != !==`**; Logic: **`&& || !`**.  
- 算术：**`+ - * /`**；比较：**`< <= > >= == === != !==`**；逻辑：**`&& || !`**。 
- **`#id`** and **`.class`** are used in **selectors** (`querySelector`).  
- **`#id`** 与 **`.class`** 用于 **选择器**（`querySelector`）。 

---

## Task 06: Convert Prompt/Alert Apps to DOM I/O  
## 任务06：把 prompt/alert 程序改造成 DOM 入出力

- Convert **five designated exercises** so that **input = `<input>` `.value`** and **output = set DOM text/HTML**.  
- 选取指定的**5道练习**进行改造：**输入来自 `<input>` 的 `.value`**，**输出写入 DOM 文本/HTML**。 
- Replace **`window.prompt()`** with **form inputs**; replace **`window.alert()` / `console.log()`** with **`textContent` or `innerHTML`**.  
- 用**表单输入**替换 **`window.prompt()`**；用 **`textContent`/`innerHTML`** 替代 **`window.alert()` / `console.log()`**。 

---

## Exercise A: Four Operations (with Buttons)  
## 练习A：四则运算（带按钮）

- Two numbers via **`<input>`**; provide **`+ − × ÷`** buttons; show result in the **browser**.  
- 两个 **`<input>`** 输入；提供 **`+ − × ÷`** 四个按钮；结果**在页面显示**。 

```html
<input id="a" type="text"> <input id="b" type="text">
<div class="ops">
  <button onclick="calc('+')">＋</button>
  <button onclick="calc('-')">－</button>
  <button onclick="calc('*')">×</button>
  <button onclick="calc('/')">÷</button>
</div>
<p id="ans"></p>
<script>
  function calc(op){
    const x = Number(document.querySelector('#a').value);
    const y = Number(document.querySelector('#b').value);
    const r = op==='+'? x+y : op==='-'? x-y : op==='*'? x*y : x/y;
    document.querySelector('#ans').textContent = `結果: ${r}`;
  }
</script>
```

---

## Exercise B: Coin Change (Greedy, JPY)  
## 练习B：硬币找零（贪心，日元）

- Input an **amount** and compute minimal counts of **500/100/50/10/5/1** yen coins, **highest first**.  
- 输入**金额**，按**面额从大到小**计算 **500/100/50/10/5/1** 日元硬币的**最少枚数**。 

```html
<input id="money" type="text" placeholder="金額を入力">
<button onclick="change()">硬貨枚数</button>
<pre id="out"></pre>
<script>
  function change(){
    let n = parseInt(document.querySelector('#money').value, 10);
    const coins = [500,100,50,10,5,1];
    const ans = [];
    for(const c of coins){
      const k = Math.floor(n / c);
      ans.push(`${c}円：${k}枚`);
      n -= k * c;
    }
    document.querySelector('#out').textContent = ans.join('\n');
  }
</script>
```


---

## Exercise C: Grade Evaluation (Ranges & Validation)  
## 练习C：成绩判定（区间与校验）

- Input **score**; output **A/B/C/D** by ranges; **0–100 only** else show **error**.  
- 输入**分数**；按区间输出 **A/B/C/D**；**仅允许 0–100**，否则输出**错误**。 

```html
<input id="score" type="text" placeholder="0〜100">
<button onclick="judge()">成績判定</button>
<p id="result"></p>
<script>
  function judge(){
    const s = Number(document.querySelector('#score').value);
    const r = (s<0 || s>100) ? 'エラー' :
              s<60 ? 'D' : s<70 ? 'C' : s<80 ? 'B' : 'A';
    document.querySelector('#result').textContent = r;
  }
</script>
```

---

## Exercise D: Three Greeting Buttons (Console → HTML)  
## 练习D：三个问候按钮（控制台 → HTML）

- Prepare **three buttons**; **one handler** outputs **different messages** into **HTML**, not Console.  
- 准备**三个按钮**；用**一个处理函数**将**不同消息**输出到 **HTML**，而非 Console。 

```html
<div class="btns">
  <button onclick="greet('おはよう')">朝</button>
  <button onclick="greet('こんにちは')">昼</button>
  <button onclick="greet('こんばんは')">夜</button>
</div>
<p id="gout"></p>
<script>
  function greet(msg){ document.querySelector('#gout').textContent = msg; }
</script>
```

---

## Exercise E: Number Guessing Game (1–100)  
## 练习E：数当て游戏（1–100）

- Generate a **random integer 1–100**; user submits guesses repeatedly; show **higher/lower/correct** hints in **HTML**.  
- 生成 **1–100** 的**随机整数**；用户可反复提交猜测；在 **HTML** 显示**更大/更小/正确**提示。 

```html
<input id="guess" type="text" placeholder="1〜100">
<button onclick="tryGuess()">予想する</button>
<p id="hint"></p>
<script>
  let secret = Math.floor(Math.random()*100)+1;
  function tryGuess(){
    const v = parseInt(document.querySelector('#guess').value, 10);
    const h = document.querySelector('#hint');
    if (v === secret)      h.textContent = "正解です";
    else if (v < secret)   h.textContent = "それより大きい数です";
    else if (v > secret)   h.textContent = "それより小さい数です";
  }
</script>
```

---

## Quick Checklist  
## 快速清单

- Use the **notation cheatsheet** for symbols, quoting, selectors.  
- 参考**记号速查表**掌握符号、引号与选择器写法。 
- Replace **prompt/alert/console** with **`<input>.value` + `textContent/innerHTML`**.  
- 用 **`<input>.value` + `textContent/innerHTML`** 替换 **prompt/alert/console**。 
- Validate numeric input via **`Number()`/`parseInt`**.  
- 使用 **`Number()`/`parseInt`** 校验**数值输入**。 
- Keep **file/folder names** and **title** per the rules; submit as **zip**.  
- 按规则设置**文件/文件夹名**与 **title**；以 **zip** 形式提交。 

---

## Notes
## 注释

<details><summary>Why `textContent` vs `innerHTML`? / 何时用 `textContent`，何时用 `innerHTML`？</summary>

- Prefer **`textContent`** for plain text; it **escapes** special chars.  
- 纯文本优先 **`textContent`**；其会**正确转义**特殊字符。  
- Use **`innerHTML`** to **append fragments** (e.g., `<li>…</li>`); be careful with **untrusted input**.  
- 需要**追加 HTML 片段**（如 `<li>…</li>`）时用 **`innerHTML`**；当心**不可信输入**。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture18.md) · [Next Lecture / 下一讲 →](./lecture20.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

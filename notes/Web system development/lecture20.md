[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 20: JavaScript Arrays — Elements, Index, Length, and Common Methods  
# 第20讲：JavaScript 数组 —— 元素、下标、长度与常用方法

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Is an Array? Elements & Index](#what-is-an-array-elements--index)  
- 什么是数组？元素与下标
- [Create an Array (Literal)](#create-an-array-literal)  
- 创建数组（字面量）
- [Access & Update by Index](#access--update-by-index)  
- 按下标访问与更新
- [Replace `if/else` with Array Lookup](#replace-ifelse-with-array-lookup)  
- 用数组查表替代 `if/else`
- [Count Elements: `.length`](#count-elements-length)  
- 统计元素个数：`.length`
- [Add/Remove Elements: `push/pop/unshift/shift`](#addremove-elements-pushpopunshiftshift)  
- 添加/删除元素：`push/pop/unshift/shift`
- [Array ⇄ String: `join()` and `split()`](#array--string-join-and-split)  
- 数组 ⇄ 字符串：`join()` 与 `split()`
- [Use Case: Input History & CSV to Array](#use-case-input-history--csv-to-array)  
- 用例：输入历史与将逗号分隔文本转数组
- [Practice Tasks](#practice-tasks)  
- 练习任务
- [Quick Checklist](#quick-checklist)  
- 快速清单
- [Notes](#notes-optional)  
- 注释

---

## What Is an Array? Elements & Index  
## 什么是数组？元素与下标

- An **array** is a data structure that groups **multiple values (elements)** together and identifies each one by a numeric **index**.  
- **数组（array）**是一种把**多个值（元素）**放在一起并用**数字下标（index）**标识每个元素的数据结构。  

```
menu (array)
index:   0        1        2        3
        青椒肉絲   回鍋肉    油淋鶏    八宝菜

“Give me menu #3 (index)!” → means the element “八宝菜”.
“给我第 3 号（下标）的菜单！” → 指的是元素 “八宝菜”。
```

> Note: Don’t confuse **HTML “elements” (tags)** with **array elements**.  
> 注意：不要把 **HTML 的“元素/标签”**与**数组的元素**混淆。  

---

## Create an Array (Literal)  
## 创建数组（字面量）

- Put values **inside square brackets** `[...]`, **comma‑separated**.  
- 将值写在**方括号** `[...]` 中，使用**逗号分隔**。  

```js
let menu = ["青椒肉絲", "回鍋肉", "油淋鶏", "八宝菜"];
// indices are 0, 1, 2, 3 / 下标从 0 开始：0、1、2、3
```

---

## Access & Update by Index  
## 按下标访问与更新

- Access with **`array[index]`**; indices **start from 0**.  
- 使用 **`数组[下标]`** 访问；下标**从 0 开始**。  

```js
console.log(menu[1]); // "回鍋肉"
menu[1] = "餃子";      // update element / 更新元素
```

```
Before 更新前              After 更新后
index: 0   1    2    3    index: 0   1   2    3
       青椒肉絲 回鍋肉 油淋鶏 八宝菜         青椒肉絲 餃子  油淋鶏 八宝菜
```

---

## Replace `if/else` with Array Lookup  
## 用数组查表替代 `if/else`

- Instead of branching `if (i===0) … else if (i===1) …`, **store options in an array** and read `menu[i]`.  
- 相比 `if (i===0)… else if (i===1)…` 这类分支，把选项**放入数组**后直接读取 `menu[i]`。  

```js
// if/else version / 分支写法
let i = 2;
let dish;
if (i === 0)      dish = "青椒肉絲";
else if (i === 1) dish = "回鍋肉";
else if (i === 2) dish = "油淋鶏";
else              dish = "八宝菜";

// array version / 数组查表
const menu2 = ["青椒肉絲","回鍋肉","油淋鶏","八宝菜"];
const dish2 = menu2[i]; // one line! / 一行搞定
```

---

## Count Elements: `.length`  
## 统计元素个数：`.length`

- The **number of elements** is available via the **`.length` property** on the array.  
- 数组的**元素个数**可通过 **`.length` 属性**获取。  

```js
let numFoods = menu.length; // 4
```

---

## Add/Remove Elements: `push/pop/unshift/shift`  
## 添加/删除元素：`push/pop/unshift/shift`

- **`push(x)`**: add to **end**; **`pop()`**: remove from **end** (and **returns** the removed value).  
- **`push(x)`**：在**尾部**追加；**`pop()`**：在**尾部**删除（并**返回**被删的值）。  
- **`unshift(x)`**: add to **front**; **`shift()`**: remove from **front** (and **returns** it).  
- **`unshift(x)`**：在**头部**追加；**`shift()`**：在**头部**删除（并**返回**被删的值）。  
- These methods are **destructive**: they **change the original array**.  
- 这些方法是**破坏性**的：会**修改原数组**。  

```js
let a = [2, 4, 6];
a.push(8);   // [2, 4, 6, 8]
a.pop();     // [2, 4, 6]
a.unshift(0);// [0, 2, 4, 6]
a.shift();   // [2, 4, 6]
```

---

## Array ⇄ String: `join()` and `split()`  
## 数组 ⇄ 字符串：`join()` 与 `split()`

- **Array → String**: use **`array.join(", ")`** to merge elements with a separator (returns a **string**).  
- **数组 → 字符串**：用 **`array.join(", ")`** 按分隔符合并元素（返回**字符串**）。  

```js
let menu = ["青椒肉絲","回鍋肉","油淋鶏","八宝菜"];
let menuStr = menu.join(", "); // "青椒肉絲, 回鍋肉, 油淋鶏, 八宝菜"
```

- **String → Array**: use **`string.split(",")`** to split a comma‑separated string into an **array**.  
- **字符串 → 数组**：用 **`string.split(",")`** 把逗号分隔字符串切成**数组**。  

```js
let menuStr1 = "青椒肉絲,回鍋肉,油淋鶏,八宝菜";
let menuAry1 = menuStr1.split(","); // ["青椒肉絲","回鍋肉","油淋鶏","八宝菜"]
```

---

## Use Case: Input History & CSV to Array  
## 用例：输入历史与将逗号分隔文本转数组

- **Input history**: push each user input into an array, then **`join()`** to display a **comma‑separated** log in a `<div>`.  
- **输入历史**：把每次用户输入 **`push()`** 到数组，再用 **`join()`** 合并，在 `<div>` 中显示**逗号分隔**的历史。  

```html
<input id="word"><button onclick="add()">Add</button>
<div id="log"></div>
<script>
  const words = [];
  function add(){
    words.push(document.querySelector('#word').value);
    document.querySelector('#log').textContent = words.join(', ');
  }
</script>
```

- **CSV to Array**: read a comma‑separated string, **`split(",")`** to get an array of entries.  
- **CSV 转数组**：读取逗号分隔的字符串，使用 **`split(",")`** 获得条目数组。  

```html
<input id="csv" placeholder="青椒肉絲,回鍋肉,油淋鶏,八宝菜">
<button onclick="parseCSV()">Parse</button>
<pre id="out"></pre>
<script>
  function parseCSV(){
    const s = document.querySelector('#csv').value;
    const arr = s.split(',');
    document.querySelector('#out').textContent = JSON.stringify(arr, null, 2);
  }
</script>
```

---

## Practice Tasks  
## 练习任务

1) **Access/Update**: Create `menu` array; print `menu[1]`; **update** it to `"餃子"` and print the whole array.  
1) **访问/更新**：创建 `menu` 数组；打印 `menu[1]`；将其**改为** `"餃子"` 并打印整个数组。  
2) **Select by index**: Replace a multi‑`if` switcher with **array lookup** `menu[i]`.  
2) **按下标选择**：用 **数组查表** `menu[i]` 替换多重 `if`。  
3) **Mutating methods**: Practice **`push/pop/unshift/shift`** and observe length changes.  
3) **可变方法**：练习 **`push/pop/unshift/shift`** 并观察长度变化。  
4) **Join/Split**: Turn an array into a **comma‑string** with `join()`, then parse a string back with `split(",")`.  
4) **合并/拆分**：用 `join()` 变成**逗号字符串**，再用 `split(",")` 还原为数组。  

---

## Quick Checklist  
## 快速清单

- Array indices **start at `0`**; access with **`arr[i]`**.  
- 数组下标**从 `0` 开始**；用 **`arr[i]`** 访问。  
- Prefer **array lookup** over repetitive **`if/else`** for discrete options.  
- 离散选项优先用**数组查表**替代重复的 **`if/else`**。  
- Get length with **`.length`**; it’s a **property**, not a function.  
- 用 **`.length`** 获取长度；它是**属性**不是函数。  
- **`push/pop`**(tail) and **`unshift/shift`**(head) **mutate** the array.  
- **`push/pop`**（尾部）与 **`unshift/shift`**（头部）会**修改**原数组。  
- Use **`join()`** (Array → String) and **`split()`** (String → Array) for conversions.  
- 用 **`join()`**（数组→字符串）与 **`split()`**（字符串→数组）进行转换。  

---

## Notes 
## 注释

<details><summary>About mutation & performance / 关于“可变”与性能</summary>

- Repeated **`unshift/shift`** on large arrays may be **slower** because items shift positions.  
- 在**大数组**上频繁使用 **`unshift/shift`** 可能**较慢**，因为需要移动大量元素。  
- If you just need to **read** without modifying, prefer **non‑destructive** methods (e.g., `slice`, `concat`) — covered later.  
- 仅需**读取**时可优先考虑**非破坏性**方法（如 `slice`、`concat`）——后续课程将覆盖。  
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture19.md) · [Next Lecture / 下一讲 →](./lecture21.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

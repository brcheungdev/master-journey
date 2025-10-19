[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Lecture 17: JavaScript Objects — Properties, Methods, Browser Objects, and JSON  
# 第17讲：JavaScript 对象 —— 属性、方法、浏览器对象与 JSON

> This file contains my notes, thoughts, and learning summaries during my master's degree study.  
> 该文件记录了攻读硕士期间的学习笔记、思考内容以及学习总结。

---

## Table of Contents  
## 目录

- [What Is an Object](#what-is-an-object)  
- 什么是对象
- [Create an Object (Object Literal)](#create-an-object-object-literal)  
- 创建对象（对象字面量）
- [Access Properties: Dot vs Bracket](#access-properties-dot-vs-bracket)  
- 访问属性：点号与中括号
- [Change, Add, and Delete Properties](#change-add-and-delete-properties)  
- 修改、添加与删除属性
- [Methods: Functions Inside Objects & `this`](#methods-functions-inside-objects--this)  
- 方法：对象中的函数与 `this`
- [Objects = Data + Behavior](#objects--data--behavior)  
- 对象 = 数据 + 行为
- [Built-in Objects (Number/String/Array…)](#built-in-objects-numberstringarray)  
- 内置对象（Number/String/Array…）
- [Browser Objects: `window`, `console`, `document`, `location`](#browser-objects-window-console-document-location)  
- 浏览器对象：`window`、`console`、`document`、`location`
- [JSON: JavaScript Object Notation](#json-javascript-object-notation)  
- JSON：JavaScript 对象表示法
- [Quick Practice](#quick-practice)  
- 快速练习
- [Quick Checklist](#quick-checklist)  
- 快速清单

---

## What Is an Object  
## 什么是对象

- An **object** groups multiple **name–value** pairs under one variable for organized access.  
- **对象**把多个**“名字–值”**对组合在一个变量下，便于有序管理与访问。  

```
student
├─ id: "M23W9999"
├─ name: "Yamada Makoto"
├─ year: 2023
└─ hobby: "Baseball"
学生信息以对象 student 统一管理：通过“名字”找到对应“值”。
```

---

## Create an Object (Object Literal)  
## 创建对象（对象字面量）

- Use **curly braces** with **`name: value`** pairs separated by **commas**.  
- 使用**花括号**写出 **`名字: 值`** 对，之间以**逗号**分隔。  
- **Property name** (key) is usually **ASCII letters/digits/`_`**; quotes are **optional** if it’s a valid identifier.  
- **属性名**通常为**半角字母/数字/`_`**；若是合法标识符，可**不加引号**。  
- **Value** can be **number/string/boolean/object/array/null**.  
- **属性值**可以是**数值/字符串/布尔/对象/数组/null**。  

```html
<script>
  const student = {
    id: "M23W9999",
    name: "Yamada Makoto",
    year: 2023,
    hobby: "Baseball" // trailing comma optional / 末尾逗号可省
  }; // assignment needs ';' / 赋值句末需分号
</script>
```

---

## Access Properties: Dot vs Bracket  
## 访问属性：点号与中括号

- **Dot**: `obj.prop` (concise).  
- **点号**：`obj.prop`（简洁）。  
- **Bracket**: `obj["prop"]` (for **dynamic names** or names **with spaces/symbols**).  
- **中括号**：`obj["prop"]`（用于**动态属性名**或**含空格/符号**的属性名）。  

```html
<script>
  const id1 = student.id;
  const id2 = student["id"];
  console.log(student.id);
  console.log(student["id"]);
</script>
```

---

## Change, Add, and Delete Properties  
## 修改、添加与删除属性

- **Change**: assign a new value to an existing property.  
- **修改**：给现有属性**重新赋值**。  
- **Add**: assign to a **new property name** to create it.  
- **新增**：对**新属性名**赋值即可创建。  
- **Delete**: use **`delete obj.prop`** or **`delete obj["prop"]`**.  
- **删除**：使用 **`delete obj.prop`** 或 **`delete obj["prop"]`**。  

```html
<script>
  student.hobby = "Basketball";           // change / 修改
  student.age = 24;                        // add / 新增
  // student["age"] = 24;                  // bracket add / 中括号新增
  delete student.year;                     // delete / 删除
  // delete student["year"];               // bracket delete / 中括号删除
</script>
```

---

## Methods: Functions Inside Objects & `this`  
## 方法：对象中的函数与 `this`

- A **function value** stored on an object is called a **method**; call with **`()`.**  
- 存在对象上的**函数值**称为**方法**；调用时必须**加 `()`**。  
- Use **`this.prop`** to refer to **other properties of the same object**.  
- 使用 **`this.prop`** 引用**同一对象中的其他属性**。  

```html
<script>
  const student2 = {
    name: "Hanako",
    bow: "90°",
    greet: function() {                // method / 方法
      console.log("申し訳ございません"); // apologize / 道歉台词
      console.log("おじぎ:", this.bow); // refer to sibling prop / 引用同对象属性
    }
  };
  student2.greet(); // () required / 必须带括号
</script>
```

---

## Objects = Data + Behavior  
## 对象 = 数据 + 行为

- An object **bundles data and the operations** that use it, so callers just say **“do X”** to the object.  
- 对象**把数据与处理封装在一起**，调用者只需对对象**发出动作指令**即可。  

---

## Built-in Objects (Number/String/Array…)  
## 内置对象（Number/String/Array…）

- Core types like **Number**, **String**, **Array** are implemented as **objects with built‑in methods**.  
- **Number**、**String**、**Array** 等核心类型本质上是**带有内置方法的对象**。  
- That’s why we write **`str.toLowerCase()`** instead of **`toLowerCase(str)`**.  
- 这就是为何我们写 **`str.toLowerCase()`** 而不是 **`toLowerCase(str)`**。  

---

## Browser Objects: `window`, `console`, `document`, `location`  
## 浏览器对象：`window`、`console`、`document`、`location`

- The browser exposes many **environment objects** with properties and methods.  
- 浏览器提供了许多**环境对象**及其属性与方法。  
- Examples: **`window`** (browser window), **`console`** (DevTools), **`document`** (page DOM), **`location`** (current URL).  
- 例如：**`window`**（浏览器窗口）、**`console`**（开发者工具）、**`document`**（页面 DOM）、**`location`**（当前 URL）。  
- Familiar APIs like **`window.alert`**, **`window.prompt`**, **`console.log`** are **methods of these objects**.  
- 常用的 **`window.alert`**、**`window.prompt`**、**`console.log`** 都是**这些对象的方法**。  

```html
<script>
  window.alert("Hello");
  const url = window.location.href;
  console.log("Now at:", url);
  document.body.style.background = "#f7f7f7";
</script>
```

---

## JSON: JavaScript Object Notation  
## JSON：JavaScript 对象表示法

- **JSON** is a **data interchange format** based on JavaScript **object/array** syntax.  
- **JSON** 是基于 JavaScript **对象/数组**语法的**数据交换格式**。  
- Commonly used between **client apps** and **server apps**; **simpler than XML** for most cases.  
- 常用于**客户端应用**与**服务器应用**之间的数据传输；多数场景下 **比 XML 更简洁**。  

```json
// JSON file / JSON 文件
[
  {"id": "1", "name": "tanaka"},
  {"id": "2", "name": "an"}
]
```
```xml
<!-- XML file / XML 文件 -->
<?xml version="1.0" encoding="utf-8"?>
<data>
  <item><id>1</id><name>tanaka</name></item>
  <item><id>2</id><name>an</name></item>
</data>
```

---

## Quick Practice  
## 快速练习

1) **Make `student`**: create an object with **`id`/`name`/`year`/`hobby`**; log two properties.  
1) **创建 `student`**：含 **`id`/`name`/`year`/`hobby`** 的对象；输出两个属性。  
2) **Access styles**: change **`document.body.style.background`** to a light color.  
2) **访问样式**：修改 **`document.body.style.background`** 为浅色。  
3) **Add & delete**: add **`age`** then **delete `year`**.  
3) **新增与删除**：新增 **`age`** 后**删除 `year`**。  
4) **Method**: give `student` a **`greet()`** method that logs **bow + message** using **`this`**.  
4) **方法**：给 `student` 增加 **`greet()`**，使用 **`this`** 打印**鞠躬角度与问候**。  
5) **JSON glance**: write a small **JSON array** of two students.  
5) **JSON 练习**：写一个包含两位学生的小型 **JSON 数组**。  

---

## Quick Checklist  
## 快速清单

- Prefer **dot** for simple names, use **bracket** for **dynamic/invalid identifiers**.  
- 简单属性名优先用**点号**，**动态或非常规属性名**用**中括号**。  
- **Assign** to change or add; use **`delete`** to remove properties.  
- 用**赋值**修改或新增；用 **`delete`** 删除属性。  
- Methods are **functions on objects**; remember **`()`** and **`this`**.  
- **方法**是对象上的**函数**；别忘 **`()`** 与 **`this`**。  
- Core types and the browser environment are **object-based** with **built‑in methods**.  
- 核心数据类型与浏览器环境都是**基于对象**并带有**内置方法**。  
- **JSON**: lightweight object/array syntax for **data exchange**.  
- **JSON**：用于**数据交换**的轻量对象/数组语法。  

<h2></h2>

[← Previous Lecture / 上一讲](./lecture16.md) · [Next Lecture / 下一讲 →](./lecture18.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

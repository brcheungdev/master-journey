[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 03 / 人工知能ソフトウェア活用Ⅰ — 第3讲
**Topic:** Core Libraries for AI Programming (NumPy · Pandas · Matplotlib — Part 1)  
**主题：** 人工智能编程核心库（NumPy · Pandas · Matplotlib — 上）

---

## Table of Contents / 目录
- [Overview & Goals / 概览与目标](#overview--goals--概览与目标)
- [NumPy Fundamentals / NumPy 基础](#numpy-fundamentals--numpy-基础)
- [Vectorization & Speed / 向量化与速度](#vectorization--speed--向量化与速度)
- [Multi‑Dimensional Arrays / 多维数组](#multidimensional-arrays--多维数组)
- [Arrays ↔ Images / 数组与图像](#arrays--images--数组与图像)
- [Pandas Fundamentals / Pandas 基础](#pandas-fundamentals--pandas-基础)
- [Matplotlib Essentials / Matplotlib 基础](#matplotlib-essentials--matplotlib-基础)
- [Hands‑on Tasks / 上机练习](#handson-tasks--上机练习)
- [Homework / 课后作业](#homework--课后作业)

---

## Overview & Goals / 概览与目标
- **We learn the three pillars for Python data/AI work: NumPy, Pandas, Matplotlib.**  
**本讲学习 Python 数据/AI 工作的三大支柱：NumPy、Pandas、Matplotlib。**
- **By the end, you can load CSVs, clean columns, and visualize distributions & relationships.**  
**完成本讲后，你能加载 CSV、清洗列，并可视化分布与关系。**
- **Colab already ships with these libraries; local Anaconda installs also work.**  
**Colab 已预装这些库；本地 Anaconda 环境亦可使用。**

---

## NumPy Fundamentals / NumPy 基础
- **NumPy provides fast N‑dimensional arrays and vectorized operations.**  
**NumPy 提供快速的 N 维数组与向量化操作。**
- **Conventional Python loops are slow for elementwise math over large lists.**  
**传统 Python 循环在大列表上逐元素运算较慢。**
- **Import with a short alias `np` to reduce typing.**  
**用短别名 `np` 导入以减少输入。**

```python
import numpy as np              # English
import numpy as np              # 中文：导入 NumPy 并命名为 np
```

### Creating Arrays / 创建数组
- **From Python data:** `np.array([1,2,3])` or ranges via `np.arange(start, stop, step)`.  
**由 Python 数据创建：`np.array([1,2,3])`；或用 `np.arange(起,止,步)` 生成序列。**
- **Zeros/ones and shapes:** `np.zeros((2,3))`, `np.ones(5)`.  
**零/一数组及形状：`np.zeros((2,3))`、`np.ones(5)`。**
- **Random samples:** `np.random.randn(3,2)` for standard normal.  
**随机采样：`np.random.randn(3,2)` 生成标准正态分布样本。**

```python
a = np.arange(5)        # [0 1 2 3 4]
b = np.zeros((2,3))     # 2×3 全零
c = np.random.randn(3,2)# 3×2 高斯随机
```

### Array Attributes / 数组属性
- **`arr.shape`, `arr.ndim`, `arr.size`, `arr.dtype` describe layout & type.**  
**`arr.shape`、`arr.ndim`、`arr.size`、`arr.dtype` 描述布局与数据类型。**
- **Reshape without copy when possible:** `arr.reshape(…); arr.ravel()`.  
**在可能时无拷贝重塑：`arr.reshape(…)；arr.ravel()`。**

```python
arr = np.arange(12)          # 1×12
arr2 = arr.reshape(3,4)      # 3×4 视图
arr2.shape, arr2.ndim        # ((3,4), 2)
```

---

## Vectorization & Speed / 向量化与速度
- **Vectorization applies operations to entire arrays at once in C‑level loops.**  
**向量化让操作在底层 C 循环中一次性作用于整个数组。**
- **Compared with Python `for` loops, vectorized NumPy code is usually tens to hundreds of times faster.**  
**与 Python `for` 循环相比，向量化 NumPy 代码常快数十到数百倍。**

```python
# Python loop (slow) / 纯 Python 循环（较慢）
data = list(range(1_000_00))         # 10万元素示例
out  = [x + 1 for x in data]

# NumPy vectorized (fast) / NumPy 向量化（较快）
arr = np.arange(1_000_00)
out_np = arr + 1
```

> **Tip：** Prefer **broadcasting** (`arr + 3`, `arr1 + arr2`) over explicit loops when shapes align.  
> **提示：** 当形状兼容时优先使用**广播**（`arr + 3`、`arr1 + arr2`）替代显式循环。

### Timing Sketch / 计时示意
- **Loops must touch Python objects one by one; arrays do the math in contiguous memory.**  
**循环逐个触碰 Python 对象；数组在连续内存中成批计算。**
- **For huge sizes, avoid printing entire arrays to prevent memory/IO stalls.**  
**大尺寸时避免打印全量数组以免内存/IO 阻塞。**

---

## Multi‑Dimensional Arrays / 多维数组
- **Matrices are 2‑D arrays; higher‑D tensors generalize further.**  
**矩阵是二维数组；更高维推广为张量。**
- **Elementwise arithmetic uses `+ - * /`, while matrix multiplication uses `@` or `np.dot`.**  
**逐元素运算用 `+ - * /`；矩阵乘法用 `@` 或 `np.dot`。**
- **`np.sum/mean/max(axis=…)` reduce along chosen dimensions.**  
**`np.sum/mean/max(axis=…)` 沿指定轴做聚合。**

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

A + B          # elementwise / 逐元素
A @ B          # matrix product / 矩阵乘法
A.sum(axis=0)  # 列和
A.sum(axis=1)  # 行和
```

### Broadcasting / 广播
- **Align trailing dimensions; size 1 dims can stretch to match.**  
**尾部维度对齐；长度为 1 的维度可拉伸匹配。**
```
(3, 1)  ⊕  (1, 4)  →  (3, 4)
(3, 1)  ⊕     (4)  →  (3, 4)
```
**Example:** add a column vector to every row.  
**示例：** 将列向量加到每一行上。

```python
x = np.arange(12).reshape(3,4)
bias = np.array([[10],[20],[30]])
y = x + bias    # broadcasts to (3,4)
```

---

## Arrays ↔ Images / 数组与图像
- **Grayscale images are 2‑D arrays; RGB images are H×W×3 tensors.**  
**灰度图是二维数组；RGB 图是 H×W×3 张量。**
- **Pixels are numeric intensities; image processing is matrix/array manipulation.**  
**像素是数值强度；图像处理本质是矩阵/数组操作。**

```
Grayscale / 灰度
[[  0, 127, 255],
 [255, 195,   0],
 [  0, 127, 255]]

RGB / 彩色 (R,G,B)
[(255, 0, 0), (0,255,0), (0,0,255), ...]
```
- **Filters (blur/edge) are convolutions; resizing/cropping are resampling & slicing.**  
**滤波（模糊/边缘）是卷积；缩放/裁剪是重采样与切片。**

---

## Pandas Fundamentals / Pandas 基础
- **Pandas offers the `DataFrame` for efficient, table‑like data handling.**  
**Pandas 提供类似表格且高效的 `DataFrame` 结构。**
- **Typical flow: load → inspect → select/drop → transform → analyze/plot.**  
**典型流程：加载→查看→选取/删除→变换→分析/绘图。**

```python
import pandas as pd                       # English
import pandas as pd                       # 中文：导入 Pandas 并命名为 pd

bmi = pd.read_csv("bmi.csv")              # load CSV / 读取 CSV
bmi.head()                                # first 5 rows / 前 5 行
bmi.info()                                # schema & types / 结构与类型
```

### Drop Columns / 删除列
- **Separate useful vs. unused columns; drop identifier columns like `No.` when necessary.**  
**区分有用与无用列；必要时删除如 `No.` 的标识列。**
```python
bmi = bmi.drop(columns=["No."])           # drop a column / 删除一列
bmi.head()
```

### Select & Filter / 选择与筛选
- **Column access: `df["col"]` or `df.col`; row filter: boolean masks.**  
**取列：`df["列名"]` 或 `df.列名`；行筛选：布尔掩码。**
```python
heights = bmi["height"]
adults = bmi[bmi["age"] >= 18]
```

### Missing Values / 缺失值（补充）
- **Detect with `isna()`, drop with `dropna()`, fill with `fillna(value)`.**  
**用 `isna()` 检测，`dropna()` 删除，`fillna(value)` 填充。**

```python
bmi["weight"] = bmi["weight"].fillna(bmi["weight"].median())
```

---

## Matplotlib Essentials / Matplotlib 基础
- **Matplotlib draws line charts, histograms, boxplots, scatter plots, etc.**  
**Matplotlib 可绘制折线、直方图、箱线图、散点图等。**
- **Visualization reveals distributions, outliers, and relationships at a glance.**  
**可视化能一眼看清分布、离群点与变量关系。**

```python
import matplotlib.pyplot as plt           # English
import matplotlib.pyplot as plt           # 中文：导入绘图库为 plt
```

### Line Plot / 折线图
- **Example: plot daily temperatures to spot peaks quickly.**  
**示例：绘制每日体温，快速发现峰值。**
```python
temps = [36.61,36.69,36.45,36.52,36.68,36.41]
plt.plot(temps); plt.title("Daily Temperature"); plt.xlabel("Day"); plt.ylabel("°C"); plt.show()
```

### Histogram / 直方图
- **Use `plt.hist(data, bins=5)` to view distribution across bins (classes).**  
**用 `plt.hist(data, bins=5)` 观察分布（分为若干“阶级”）。**
```python
plt.hist(bmi["height"], bins=10)
plt.title("Height Distribution"); plt.xlabel("Height"); plt.ylabel("Count"); plt.show()
```

### Boxplot / 箱线图
- **Shows medians, quartiles, and potential outliers—not necessarily wrong data.**  
**展示中位数、四分位与潜在离群值——离群并不等于错误数据。**
```python
plt.boxplot(bmi["height"], vert=True, labels=["Height"])
plt.title("Height Spread"); plt.ylabel("Height"); plt.show()
```

### Scatter / 散点图
- **Plot two variables to see correlation & clusters.**  
**将两变量作图以观察相关性与聚类。**
```python
plt.scatter(bmi["height"], bmi["weight"])
plt.xlabel("Height"); plt.ylabel("Weight"); plt.title("Height vs Weight"); plt.show()
```

<details><summary>Correlation & Summary (optional) / 相关性与摘要（可选）</summary>

```python
bmi[["height","weight"]].corr()   # Pearson correlation / 皮尔逊相关
bmi.describe()                    # Summary stats / 统计摘要
```
**Interpretation:** positive correlation suggests taller → heavier on average.  
**解读：** 正相关通常表示更高者平均更重。
</details>

---

## Hands‑on Tasks / 上机练习
- **Matrix arithmetic drill:** given matrices `a` and `b`, perform `+ − × ÷` elementwise and `a @ b`.  
**矩阵演练：** 给定矩阵 `a` 与 `b`，进行逐元素 `+ − × ÷` 与 `a @ b`。**
- **Broadcasting practice:** add a `(3,1)` column vector to a `(3,4)` matrix.  
**广播练习：** 将 `(3,1)` 列向量加到 `(3,4)` 矩阵上。**
- **Data wrangling:** load `bmi.csv`, drop `No.`, preview with `head()` and `info()`.  
**数据整理：** 载入 `bmi.csv`，删除 `No.`，用 `head()` 与 `info()` 预览。**
- **Visualization:** draw a **histogram** (heights) and a **boxplot** (weights).  
**可视化：** 绘制**身高直方图**与**体重箱线图**。**

```python
# Template / 模板
import pandas as pd, numpy as np, matplotlib.pyplot as plt

bmi = pd.read_csv("bmi.csv").drop(columns=["No."])
plt.hist(bmi["height"], bins=5); plt.title("Height Histogram"); plt.show()
plt.boxplot(bmi["weight"], vert=True, labels=["Weight"]); plt.title("Weight Boxplot"); plt.show()
```

---

## Homework / 课后作业
- produce a boxplot for Weight and a 5‑bin histogram for Weight.**  
**针对**体重（Weight）**绘制**箱线图**与**5 阶级直方图**。**

<h2></h2>

[← Previous Lecture / 上一讲](./lecture02.md) · [Next Lecture / 下一讲 →](./lecture04.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 07 / 人工知能ソフトウェア活用Ⅰ — 第7讲
**Topic:** Classification Basics — Confusion Matrix & Naive Bayes (with exercises)  
**主题：** 分类基础 —— 混淆矩阵与朴素贝叶斯（含演练）

---

## Table of Contents / 目录
- [Recap of Last Homework / 上次作业回顾](#recap-of-last-homework--上次作业回顾)
- [Common Pitfalls in Code / 代码常见问题](#common-pitfalls-in-code--代码常见问题)
- [From Clustering to Classification / 从聚类到分类](#from-clustering-to-classification--从聚类到分类)
- [Confusion Matrix / 混淆矩阵](#confusion-matrix--混淆矩阵)
- [Performance Metrics / 性能指标](#performance-metrics--性能指标)
- [Exercise A: Build Metrics from Cabbage vs Lettuce / 练习A：由卷心菜vs生菜计算指标](#exercise-a-build-metrics-from-cabbage-vs-lettuce--练习a由卷心菜vs生菜计算指标)
- [Why So Many Metrics? / 为什么有这么多指标？](#why-so-many-metrics--为什么有这么多指标)
- [Naive Bayes / 朴素贝叶斯](#naive-bayes--朴素贝叶斯)
- [Exercise B: Naive Bayes on Synthetic Data / 练习B：在合成数据上用朴素贝叶斯](#exercise-b-naive-bayes-on-synthetic-data--练习b在合成数据上用朴素贝叶斯)
- [Homework / 课后作业](#homework--课后作业)


---

## Recap of Last Homework / 上次作业回顾
- **Task:** Cluster the UCI **Wholesale customers** into **4 clusters** and analyze the results (**Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen**).  
**任务：** 将 UCI 的 **批发客户数据**分为 **4 个簇**并分析结果（字段：**Fresh、Milk、Grocery、Frozen、Detergents_Paper、Delicassen**）。 

### Sample Analysis Hints / 样例分析提示
- **Many customers spend ≤ 20,000 overall;** among them **Fresh ≈ half** of sales.  
**许多客户总消费量 ≤ 20,000；** 其中**生鲜（Fresh）约占一半**。 
- **Cluster 2** is **few in count but very high spend;** may correspond to **retail/restaurant sourcing**; consider **VIP services** (discounts/special contracts).  
**“簇2”** **数量少但消费极高；** 可能对应**零售/餐饮进货**；可考虑**优待服务**（折扣/另签合约）。 

---

## Common Pitfalls in Code / 代码常见问题
- **Typos:** `pd.read_csv` (correct) vs `pd,read_csv` (wrong); `np.int32` vs `np,int32`.  
**拼写错误：** `pd.read_csv`（正确）vs `pd,read_csv`（错误）；`np.int32` vs `np,int32`。 
- **Variable shadowing:** reusing the same name for **DataFrame** and **model** (e.g., `cust = pd.read_csv(...)` then `cust = KMeans(...)`) leads to errors.  
**变量名复用：** 同一个名字既当 **DataFrame** 又当 **模型**（如先 `cust = pd.read_csv(...)` 又 `cust = KMeans(...)`）会报错。 

<details><summary>Best Practices / 最佳实践</summary>

- Use **distinct names**: `df_cust`, `kmeans_cust`, `pred_labels`.  
**使用**不同名称**：`df_cust`、`kmeans_cust`、`pred_labels`。  
- Keep **immutable inputs**; write outputs to **new variables/columns**.  
**尽量保持**输入不可变**；将输出写入**新变量/新列**。

</details>

---

## From Clustering to Classification / 从聚类到分类
- **Some datasets separate cleanly (clear boundary).**  
**有些数据能清晰分界（明显边界）。** 
- **Others lack a sharp boundary;** a separating line can misclassify points; we need **metrics** to quantify correctness vs mistakes.  
**另一些数据没有清晰边界；** 即使能画分隔线，也可能误分，需要**指标**衡量对错。 

---

## Confusion Matrix / 混淆矩阵
- **A table to evaluate a classifier’s performance.**  
**用于评估分类器性能的表格。** 

```
               Predicted Positive   Predicted Negative
Actual Positive         TP                  FN
Actual Negative         FP                  TN
```
**TP=True Positive, FP=False Positive, FN=False Negative, TN=True Negative.**  
**TP=真阳性，FP=假阳性，FN=假阴性，TN=真阴性。** 

### Cabbage vs Lettuce Example / 卷心菜 vs 生菜示例
- **100 lettuces:** 85 correct, 15 wrong.  
**100 颗生菜：** 85 正确，15 错误。  
- **100 cabbages:** 95 correct, 5 wrong.  
**100 颗卷心菜：** 95 正确，5 错误。 

> **Convention here:** **Positive = Lettuce**.  
> **本例约定：** **阳性 = 生菜（lettuce）**。 

---

## Performance Metrics / 性能指标
- **Accuracy:**  \n  **Definition / 定义：** `(TP + TN) / (TP + FP + FN + TN)` \n  **Example / 例：** `(85 + 95) / (85 + 5 + 15 + 95) = 90%`.  
**准确率（Accuracy）：**  \n  **定义：** `(TP + TN) / (TP + FP + FN + TN)` \n  **例：** `(85 + 95) / (85 + 5 + 15 + 95) = 90%`。 

- **Precision:**  \n  **Definition / 定义：** `TP / (TP + FP)` \n  **Example / 例：** `85 / (85 + 5) = 94.44%`.  
**精确率（Precision）：**  \n  **定义：** `TP / (TP + FP)` \n  **例：** `85 / (85 + 5) = 94.44%`。 

- **Recall (TPR):**  \n  **Definition / 定义：** `TP / (TP + FN)` \n  **Example / 例：** `85 / (85 + 15) = 85%`.  
**召回率（Recall/真阳性率）：**  \n  **定义：** `TP / (TP + FN)` \n  **例：** `85 / (85 + 15) = 85%`。 

- **F1‑score:**  \n  **Definition / 定义：** `2*TP / (2*TP + FP + FN)` \n  **Example / 例：** `2*85 / (2*85 + 5 + 15) = 89.47%`.  
**F1 值：**  \n  **定义：** `2*TP / (2*TP + FP + FN)` \n  **例：** `2*85 / (2*85 + 5 + 15) = 89.47%`。 

---

## Exercise A: Build Metrics from Cabbage vs Lettuce / 练习A：由卷心菜vs生菜计算指标
- **Goal:** Using the provided **prediction** (`PREDICT`) and **ground truth** (`TRUE`) columns, compute the confusion matrix and all four metrics.  
**目标：** 使用数据中的 **预测**列（`PREDICT`）与 **真实**列（`TRUE`），计算混淆矩阵与四类指标。 

```python
# English / 中文：从“卷心菜 vs 生菜”结果计算四类指标
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("cabbage_lettuce_results.csv")  # columns: TRUE, PREDICT
y_true = df["TRUE"]
y_pred = df["PREDICT"]

cm = confusion_matrix(y_true, y_pred, labels=["lettuce","cabbage"])
acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, pos_label="lettuce")
rec = recall_score(y_true, y_pred, pos_label="lettuce")
f1 = f1_score(y_true, y_pred, pos_label="lettuce")

print("CM:\n", cm)
print("Accuracy:", acc, "Precision:", prec, "Recall:", rec, "F1:", f1)
```
**Note:** specify `pos_label='lettuce'` to match the slide convention.  
**注意：** 将 `pos_label='lettuce'`，与幻灯的阳性类别保持一致。 

---

## Why So Many Metrics? / 为什么有这么多指标？
- **Accuracy can mislead under class imbalance:** if **10 lettuces** vs **90 cabbages**, a classifier predicting **all “cabbage”** yields **90% accuracy** but **0% recall for lettuce**.  
**在类别极不平衡时 Accuracy 可能误导：** 若 **10 生菜** vs **90 卷心菜**，分类器**全判“卷心菜”**则 **Accuracy=90%**，但**生菜的 Recall=0%**。 

---

## Naive Bayes / 朴素贝叶斯
- **Definition:** a probabilistic method to decide which **category** a data point belongs to; widely used for **text classification (spam filtering)**.  
**定义：** 基于概率判断样本所属**类别**的方法；常用于**文本分类（垃圾邮件过滤）**。 

### Bayes’ Theorem / 贝叶斯定理
```
P(A|B) = P(A) * P(B|A) / P(B)
P(A|B) = P(A) 与 P(B|A) 的乘积再除以 P(B)
```
**`P(X)` = probability of X; `P(X|Y)` = probability of X given Y.**  
**`P(X)` 表示 X 的概率；`P(X|Y)` 表示在 Y 条件下 X 的概率。** 

### Intuition via Weight Ranges / 通过重量范围直觉化理解
- **Lettuce** averages **400–800 g**; **Cabbage** averages **700–1200 g** (toy example).  
**生菜**平均 **400–800 g**；**卷心菜**平均 **700–1200 g**（玩具示例）。  
- For **400 g**, likely **lettuce**; for **800 g**, both are plausible → need probabilities.  
**若** 400g，**更可能是生菜**；若 **800g**，两者都可能 → 需要使用概率判断。 

---

## Exercise B: Naive Bayes on Synthetic Data / 练习B：在合成数据上用朴素贝叶斯
- **Steps:** generate data → fit **GaussianNB** → plot decision boundary → map to lettuce/cabbage story.  
**步骤：** 生成数据 → 训练 **GaussianNB** → 绘制决策边界 → 对应到生菜/卷心菜示例。 

```python
# English / 中文：朴素贝叶斯二维玩具数据
import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB

X, y = make_blobs(n_samples=400, centers=2, cluster_std=2.0, random_state=0)
gnb = GaussianNB().fit(X, y)

# grid for boundary / 决策边界网格
xs = np.linspace(X[:,0].min()-1, X[:,0].max()+1, 200)
ys = np.linspace(X[:,1].min()-1, X[:,1].max()+1, 200)
xx, yy = np.meshgrid(xs, ys)
zz = gnb.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.figure()
plt.contourf(xx, yy, zz, alpha=0.2)
plt.scatter(X[:,0], X[:,1], c=y, s=14)
plt.title("Naive Bayes decision boundary"); plt.xlabel("Feature 1"); plt.ylabel("Feature 2")
plt.show()
```
**Observation:** regions with **ambiguous overlap** reflect **uncertainty**; NB outputs class probabilities.  
**观察：** **重叠区域**表示**不确定性**；朴素贝叶斯可给出类别概率。 

---

## Homework / 课后作业
- **Compute** the confusion matrix and **four metrics** (`accuracy`, `precision`, `recall`, `f1`) for the cabbage–lettuce dataset using scikit‑learn’s APIs as shown.  
**用 scikit‑learn 计算**混淆矩阵**与四项指标（`accuracy`、`precision`、`recall`、`f1`）。** 
- **Train** a Naive Bayes model on a **2‑D synthetic dataset** and **plot** its decision boundary.  
**在**二维合成数据**上训练朴素贝叶斯并**绘制**决策边界。** 


<h2></h2>

[← Previous Lecture / 上一讲](./lecture06.md) · [Next Lecture / 下一讲 →](./lecture08.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

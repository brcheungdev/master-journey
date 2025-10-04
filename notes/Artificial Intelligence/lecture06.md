[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 06 / 人工知能ソフトウェア活用Ⅰ — 第6讲
**Topic:** Unsupervised Learning — Clustering (K‑means) & PCA with Wholesale Customers Dataset  
**主题：** 无监督学习 —— 用 **K‑means 聚类** 与 **PCA 主成分分析** 解析批发客户数据集

---

## Table of Contents / 目录
- [Why Unsupervised Learning? / 为什么要学无监督？](#why-unsupervised-learning--为什么要学无监督)
- [Dataset: Wholesale Customers / 数据集：批发客户](#dataset-wholesale-customers--数据集批发客户)
- [Feature Scaling & Log Transform / 特征缩放与对数变换](#feature-scaling--log-transform--特征缩放与对数变换)
- [K‑means Clustering / K‑means 聚类](#kmeans-clustering--kmeans-聚类)
- [Choosing K: Elbow & Silhouette / 选择簇数：肘部法与轮廓系数](#choosing-k-elbow--silhouette--选择簇数肘部法与轮廓系数)
- [PCA for Visualization & Insight / 用 PCA 可视化与洞察](#pca-for-visualization--insight--用-pca-可视化与洞察)
- [Putting It Together / 综合流程](#putting-it-together--综合流程)
- [Hands‑on Exercises / 上机练习](#handson-exercises--上机练习)
- [Homework / 课后作业](#homework--课后作业)
- [Notes & Assumptions / 说明与假设](#notes--assumptions--说明与假设)

---

## Why Unsupervised Learning? / 为什么要学无监督？
- **We have data but no labels; we seek structure or groups.**  
**我们只有数据、没有标签；目标是发现结构或分组。**
- **Typical goals:** customer segmentation, anomaly detection, visualization.  
**典型目标：** 客户分群、异常检测、可视化降维。**

---

## Dataset: Wholesale Customers / 数据集：批发客户
- **Features (annual spending):** **Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen**.   
**特征（年度开销）：** **Fresh、Milk、Grocery、Frozen、Detergents_Paper、Delicassen**。 
- **Goal:** cluster customers into purchasing patterns; visualize in 2‑D.  
**目标：** 将客户按购买模式分群，并在二维中可视化。**

```python
import pandas as pd

# English / 中文：读取数据（示例文件名，可按幻灯配套数据重命名）
df = pd.read_csv("wholesale_customers.csv")
df.head()
```

<details><summary>Basic checks / 基本检查</summary>

```python
df.info()                  # dtypes & missing / 类型与缺失
df.describe()              # quick stats / 统计摘要
df.isna().mean()           # missing ratio / 缺失占比
```
**Ensure numeric types and reasonable ranges.**  
**确保类型为数值且范围合理。**
</details>

---

## Feature Scaling & Log Transform / 特征缩放与对数变换
- **K‑means uses Euclidean distance ⇒ scale matters.**  
**K‑means 基于欧式距离 ⇒ 特征尺度很重要。**
- **Highly skewed spending ⇒ consider `log1p` (log(1+x)) + standardization.**  
**年度消费通常偏态严重 ⇒ 建议使用 `log1p`（log(1+x)）并进行标准化。**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

X = df[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]].copy()
X_log = np.log1p(X)                    # stabilize variance / 稳定方差
scaler = StandardScaler()
Xz = scaler.fit_transform(X_log)
```

> **Tip / 小贴士：** Always **fit** scalers on training data and **transform** both train/test the same way.  
> **提示：** 训练/评估一致缩放；实际部署时保存缩放器参数。

---

## K‑means Clustering / K‑means 聚类
- **Idea:** pick **K centroids**, assign each point to nearest centroid, update centroids, repeat.  
**思想：** 设定 **K 个质心**，分配样本到最近质心，更新质心，迭代收敛。**
- **Objective:** minimize **within‑cluster sum of squares (WCSS / inertia)**.  
**目标：** 最小化**簇内平方和（惯性）**。**

```python
from sklearn.cluster import KMeans

k = 4  # try 3–6
km = KMeans(n_clusters=k, n_init=20, random_state=42)
labels = km.fit_predict(Xz)
df["cluster"] = labels
km.inertia_, km.cluster_centers_.shape
```
**`inertia_` is the WCSS; lower is better (for fixed K).**  
**`inertia_` 为簇内平方和；同一 K 下越小越好。**

<details><summary>Cluster profiling / 簇画像（理解各簇特征）</summary>

```python
# inverse transform to original scale (median to resist skew)
centers_z = km.cluster_centers_
centers_log = scaler.inverse_transform(centers_z)   # back to log-space
centers = np.expm1(centers_log)                     # back to original
cluster_profile = pd.DataFrame(centers, columns=X.columns)
cluster_profile.round(0)
```
**Interpret spending levels by cluster to name segments (e.g., “Grocery‑heavy”).**  
**根据各簇的消费结构给出命名（如“日配重度”“生鲜导向”）。**
</details>

---

## Choosing K: Elbow & Silhouette / 选择簇数：肘部法与轮廓系数
- **Elbow method:** plot **K vs inertia**; look for a noticeable “knee”.  
**肘部法：** 绘制 **K 与惯性**曲线；寻找明显“拐点”。**
- **Silhouette score (−1..1):** higher is better; measures cluster separation.  
**轮廓系数（−1..1）：** 越高越好；度量簇内紧密与簇间分离。**

```python
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

Ks = range(2, 10)
inertias, sils = [], []
for k in Ks:
    km = KMeans(n_clusters=k, n_init=20, random_state=42).fit(Xz)
    inertias.append(km.inertia_)
    sils.append(silhouette_score(Xz, km.labels_))

plt.figure(); plt.plot(list(Ks), inertias, marker="o")
plt.xlabel("K"); plt.ylabel("Inertia (WCSS)"); plt.title("Elbow"); plt.show()

plt.figure(); plt.plot(list(Ks), sils, marker="o")
plt.xlabel("K"); plt.ylabel("Silhouette"); plt.title("Silhouette vs K"); plt.show()
```

---

## PCA for Visualization & Insight / 用 PCA 可视化与洞察
- **PCA finds orthogonal directions capturing maximum variance.**  
**PCA 找到最大方差的正交方向。**
- **Use first 2 components for 2‑D scatter; color by cluster.**  
**前两主成分用于二维散点，并用颜色区分簇。**

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=42)
X2 = pca.fit_transform(Xz)
print("Explained variance ratio:", pca.explained_variance_ratio_)

plt.figure()
plt.scatter(X2[:,0], X2[:,1], c=df["cluster"], s=18)
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("K-means clusters in PCA space"); plt.show()
```

<details><summary>Component loadings / 主成分载荷（解释每个特征的贡献）</summary>

```python
loadings = pd.DataFrame(pca.components_.T,
                        index=X.columns, columns=["PC1","PC2"])
loadings.sort_values("PC1", ascending=False)
```
**Large absolute loadings indicate features defining each PC.**  
**载荷绝对值大说明该特征对该主成分贡献大。**
</details>

---

## Putting It Together / 综合流程
- **Pipeline:** `Log1p → Standardize → KMeans → Profile → PCA plot`.  
**流水线：** `对数变换 → 标准化 → KMeans → 簇画像 → PCA 可视化`。**
- **Deliverables:** inertia/silhouette plots, PCA scatter, cluster table.  
**产出：** 惯性/轮廓图、PCA 散点、簇画像表。**

```python
summary = (df.groupby("cluster")[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]]
             .median()
             .astype(int))
summary
```

---

## Hands‑on Exercises / 上机练习
1. **Scaling:** Compare clustering with and without `log1p` (fix K).  
**缩放：** 在相同 K 下比较是否使用 `log1p` 的效果。**
2. **Model selection:** Use elbow & silhouette to choose **K∈[3..8]**.  
**模型选择：** 用肘部与轮廓在 **K=3..8** 中选最优。**
3. **Profiling:** Name each cluster in plain language from the median spending table.  
**画像：** 根据各簇中位消费表用自然语言给簇命名。**
4. **PCA:** Report the explained variance of PC1+PC2 and discuss sufficiency.  
**PCA：** 汇报 PC1+PC2 解释的方差占比并讨论是否足够。**

---

## Homework / 课后作业
- **Task:** Reproduce the full pipeline on the lecture dataset; **submit the `.ipynb`** with elbow, silhouette, PCA, and a **cluster profile table**.   
**作业：** 在课堂数据上复现完整流程；提交包含 **肘部、轮廓、PCA 散点、簇画像表** 的 **`.ipynb`**。 
- Try **k‑means++ init** (default), different `n_init`, and discuss stability.  
试验 **k‑means++ 初始化**（默认）、不同 `n_init`，讨论结果稳定性。**

<h2></h2>

[← Previous Lecture / 上一讲](./lecture05.md) · [Next Lecture / 下一讲 →](./lecture07.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

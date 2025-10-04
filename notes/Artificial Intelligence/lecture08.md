[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 08 / 人工知能ソフトウェア活用Ⅰ — 第8讲
**Topic:** Support Vector Machines — Linear SVM, Non‑linear Separation & Kernel Trick (with Exercises)  
**主题：** 支持向量机 —— 线性 SVM、非线性可分与核技巧（含演练）

---

## Table of Contents / 目录
- [Today’s Agenda / 今日内容](#todays-agenda--今日内容)
- [What is SVM? / SVM 是什么？](#what-is-svm--svm-是什么)
- [Why Maximize the Margin? / 为什么要最大化间隔？](#why-maximize-the-margin--为什么要最大化间隔)
- [Exercise 1: Two‑blob Data — NB vs Linear SVM / 练习1：双团簇数据——朴素贝叶斯 vs 线性SVM](#exercise-1-two-blob-data--nb-vs-linear-svm--练习1双团簇数据朴素贝叶斯-vs-线性svm)
- [Exercise 2: “Moons” Dataset — NB vs Linear SVM / 练习2：“新月”数据——朴素贝叶斯 vs 线性SVM](#exercise-2-moons-dataset--nb-vs-linear-svm--练习2新月数据朴素贝叶斯-vs-线性svm)
- [Linear Separability & Its Limits / 线性可分与局限](#linear-separability--its-limits--线性可分与局限)
- [Kernel Trick / 核技巧](#kernel-trick--核技巧)
- [Exercise 3: Kernel SVM on Moons / 练习3：核SVM 处理“新月”数据](#exercise-3-kernel-svm-on-moons--练习3核svm-处理新月数据)
- [Exercise 4: Kernel SVM on Concentric Circles / 练习4：核SVM 处理同心圆数据](#exercise-4-kernel-svm-on-concentric-circles--练习4核svm-处理同心圆数据)
- [Feature Mapping & 3D View / 特征映射与三维视图](#feature-mapping--3d-view--特征映射与三维视图)
- [Kernel SVM: Caveats / 核SVM 的注意点](#kernel-svm-caveats--核svm-的注意点)
- [Supplement (optional) / 补充说明（可选）](#supplement-optional--补充说明可选)

---

## Today’s Agenda / 今日内容
- **Think about classification problems; then SVM; then SVM exercises; discuss non‑linear separation; introduce kernel method.**   
**围绕分类问题展开；学习 SVM；完成 SVM 演练；讨论非线性分离；介绍核方法。** 

---

## What is SVM? / SVM 是什么？
- **SVM (Support Vector Machine) determines a decision boundary for classification.**   
**SVM（支持向量机）用于确定分类的决策边界。** 
- **It chooses the boundary by “maximizing the margin”.**   
**通过“最大化间隔（margin）”来确定边界。** 

---

## Why Maximize the Margin? / 为什么要最大化间隔？
- **Shift the line left ⇒ margin to class A shrinks ⇒ more A may become misclassified.**   
**若将分界线左移 ⇒ 与 **A 类** 的间隔变小 ⇒ 更多 A 可能被误分。** 
- **Shift the line right ⇒ margin to class B shrinks ⇒ more B may become misclassified.**   
**若将分界线右移 ⇒ 与 **B 类** 的间隔变小 ⇒ 更多 B 可能被误分。** 

---

## Exercise 1: Two‑blob Data — NB vs Linear SVM / 练习1：双团簇数据——朴素贝叶斯 vs 线性SVM
- **Load libs; code outside the red box is same as last homework; train Naive Bayes as baseline; plot decision.**   
**加载库；红框外代码与上次作业相同；先用朴素贝叶斯做基线；绘制决策结果。** 

```python
# Template: blobs + NB + linear SVM / 模板：双团簇 + NB + 线性SVM
import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

X, y = make_blobs(n_samples=400, centers=2, cluster_std=1.8, random_state=0)

def plot_boundary(clf, X, y, title):
    xs = np.linspace(X[:,0].min()-1, X[:,0].max()+1, 300)
    ys = np.linspace(X[:,1].min()-1, X[:,1].max()+1, 300)
    xx, yy = np.meshgrid(xs, ys)
    zz = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.figure(); plt.contourf(xx, yy, zz, alpha=0.2)
    plt.scatter(X[:,0], X[:,1], c=y, s=14)
    plt.title(title); plt.xlabel("x1"); plt.ylabel("x2"); plt.show()

nb = GaussianNB().fit(X, y)
plot_boundary(nb, X, y, "Naive Bayes — Two blobs")

lin_svm = SVC(kernel="linear", C=1.0).fit(X, y)
plot_boundary(lin_svm, X, y, "Linear SVM — Two blobs")
```
**Compare NB vs Linear SVM decision boundaries.**   
**对比 NB 与线性 SVM 的决策边界。** 

---

## Exercise 2: “Moons” Dataset — NB vs Linear SVM / 练习2：“新月”数据——朴素贝叶斯 vs 线性SVM
- **Use the interleaving two‑moons data; train NB and plot; then try linear SVM and plot; observe misclassifications.**   
**使用交错的“两新月”数据；先训练 NB 并绘制；再试线性 SVM 并绘制；观察误分。** 

```python
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=400, noise=0.25, random_state=0)
nb = GaussianNB().fit(X, y)
plot_boundary(nb, X, y, "Naive Bayes — Moons")

lin_svm = SVC(kernel="linear", C=1.0).fit(X, y)
plot_boundary(lin_svm, X, y, "Linear SVM — Moons")
```
**Result on slides: many points correct, but many still misclassified; linear SVM fails on curved boundary.**   
**幻灯结论：大多数点被正确分类，但错误也不少；线性 SVM 难以处理曲线边界。** 

---

## Linear Separability & Its Limits / 线性可分与局限
- **Some datasets cannot be separated by a straight line — not linearly separable.**   
**有些数据无法用直线分开——即**非线性可分**。** 

---

## Kernel Trick / 核技巧
- **Kernel method creates new features from existing ones to enable SVM in a higher‑dimensional space.**   
**核方法（核技巧）从已有特征**构造新特征**，在更高维空间用 SVM 可分。** 
- **Cultural note:** the “dimension attack” (**降维打击**) meme from Liu Cixin’s *The Three‑Body Problem* is the opposite; **kernel adds dimensions** instead.   
**文化旁注：** 刘慈欣《三体》里的“**降维打击**”与此相反；**核技巧是“升维”**。 

---

## Exercise 3: Kernel SVM on Moons / 练习3：核SVM 处理“新月”数据
- **Train kernel SVM (e.g., RBF) on moons and plot; classification succeeds.**   
**在新月数据上用核 SVM（如 RBF）训练并绘制；分类效果良好。** 

```python
rbf_svm = SVC(kernel="rbf", C=1.0, gamma="scale").fit(X, y)
plot_boundary(rbf_svm, X, y, "RBF‑kernel SVM — Moons")
```

---

## Exercise 4: Kernel SVM on Concentric Circles / 练习4：核SVM 处理同心圆数据
- **Use circle‑shaped data; kernel SVM classifies successfully.**   
**使用同心圆形数据；核 SVM 能成功分类。** 

```python
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=500, noise=0.09, factor=0.5, random_state=0)
rbf_svm = SVC(kernel="rbf", C=1.0, gamma="scale").fit(X, y)
plot_boundary(rbf_svm, X, y, "RBF‑kernel SVM — Circles")
```

---

## Feature Mapping & 3D View / 特征映射与三维视图
- **Define “width/height/depth” axes; depth uses a new feature such as `X1^2 + X2^2`; 3D plot helps intuition; interactive rotation allowed in class demo.**   
**通过定义“横/纵/深度”，其中深度可用新特征 `X1^2 + X2^2`；用 3D 图直观展示；课堂演示可交互旋转。** 

```python
# Static 3D hint (matplotlib); in-class used interactive 3D. / 静态3D示意
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import matplotlib.pyplot as plt
Z = (X[:,0]**2 + X[:,1]**2)
fig = plt.figure(); ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Z, c=y, s=8)
ax.set_xlabel("X1"); ax.set_ylabel("X2"); ax.set_zlabel("X1^2 + X2^2")
plt.title("Feature mapping to 3D"); plt.show()
```

---

## Kernel SVM: Caveats / 核SVM 的注意点
- **There are multiple kernels beyond RBF; a wrong choice can underperform — trial and error may be needed.**   
**除了 RBF 之外还有多种核；**选择不当**可能分类不准——通常需**试错**。** 
- **Creating new features from existing ones increases dimensionality and compute; large‑feature or large‑sample datasets can be expensive.**   
**基于现有特征构造新特征会**升维**并增大计算；当特征/样本很多时成本很高。** 

---

## Supplement  / 补充说明
<details><summary>Soft‑margin Linear SVM / 软间隔线性 SVM</summary>

- **Add slack with parameter `C`: smaller `C` ⇒ wider margin but more violations; larger `C` ⇒ narrower margin but fewer violations.**  
**用参数 `C` 引入“松弛”：`C` 较小 ⇒ 间隔更宽但容许更多违例；`C` 较大 ⇒ 间隔更窄但违例更少。**

```python
for C in [0.1, 1, 10]:
    clf = SVC(kernel="linear", C=C).fit(X, y)
    plot_boundary(clf, X, y, f"Linear SVM (C={C})")
```
</details>

<details><summary>RBF kernel intuition & `gamma` / RBF 核直觉与 `gamma`</summary>

- **`gamma` controls kernel width: small ⇒ smoother boundary; large ⇒ tight, risk of overfitting.**
**`gamma` 控制核宽：小 ⇒ 边界更平滑；大 ⇒ 边界更紧、易过拟合。**

```python
for g in [0.05, 0.2, 1.0]:
    clf = SVC(kernel="rbf", gamma=g).fit(X, y)
    plot_boundary(clf, X, y, f"RBF SVM (gamma={g})")
```
</details>

<details><summary>Scaling matters / 特征缩放很重要</summary>

- **Always scale inputs (e.g., `StandardScaler`) before SVM, especially with RBF/poly kernels.**  
**SVM 前通常需进行标准化，特别是 RBF/多项式核。**
</details>

<details><summary>Model selection / 模型选择</summary>

- **Try kernels (`linear`, `rbf`, `poly`) and tune `C`, `gamma`, `degree` with cross‑validation.**  
**结合交叉验证选择核类型与 `C`、`gamma`、`degree` 等超参。**
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture07.md) · [Next Lecture / 下一讲 →](./lecture09.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

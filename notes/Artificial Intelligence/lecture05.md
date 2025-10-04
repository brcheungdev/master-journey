[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.
  
# Artificial Intelligence Software Utilization I — Lecture 05 / 人工知能ソフトウェア活用Ⅰ — 第5讲
**Topic:** Regression — Simple · Multiple · Ridge (+ Polynomial intro)  
**主题：** 回归 —— 单回归 · 重回归 · 岭回归（含多项式回归导引）

---

## Table of Contents / 目录
- [What is Regression? / 什么是回归？](#what-is-regression--什么是回归)
- [Correlation & Coefficient / 相关与相关系数](#correlation--coefficient--相关与相关系数)
- [Supervised Learning: Regression / 监督学习：回归](#supervised-learning-regression--监督学习回归)
- [Least Squares / 最小二乘法](#least-squares--最小二乘法)
- [Simple Regression (Height→Weight) / 单回归（身高→体重）](#simple-regression-heightweight--单回归身高→体重)
- [Multiple Regression (Real‑estate) / 重回归（不动产示例）](#multiple-regression-realestate--重回归不动产示例)
- [Polynomial vs Ridge / 多项式回归 vs 岭回归](#polynomial-vs-ridge--多项式回归-vs-岭回归)
- [Evaluation & Diagnostics / 评估与诊断（补充）](#evaluation--diagnostics--评估与诊断补充)
- [Hands‑on Templates / 上机模板](#handson-templates--上机模板)
- [Homework / 课后作业](#homework--课后作业)

---

## What is Regression? / 什么是回归？
- **Question:** *How are height and weight related?*  
**问题：** *身高与体重之间有什么关系？*
- **Goal:** **predict continuous values** (e.g., sales from ad budget).  
**目标：** **预测连续数值**（例如由广告预算预测销量）。

---

## Correlation & Coefficient / 相关与相关系数
- **Positive correlation:** as **height increases, weight increases**.  
**正相关：** **身高越高，体重越大**。
- **Negative correlation:** **latitude↑ → annual mean temp↓**.  
**负相关：** **纬度越高 → 年平均气温越低**。
- **No correlation:** e.g., certain **language vs math scores**.  
**无相关：** 例如某些情况下 **语文与数学成绩**。

**Correlation coefficient r (−1 … +1).**  
**相关系数 r（范围 −1 … +1）。**

```
r =  cov(x, y) / (σ_x · σ_y)
r 的计算：以 x、y 的协方差除以各自标准差的乘积
```
- **Closer to ±1 ⇒ points lie near a line; 0 ⇒ weak/none.** 
**越接近 ±1 ⇒ 数据点越接近直线；接近 0 ⇒ 相关弱/无。** 

> **Note / 注意：** **Correlation ≠ Causation.** Always combine **domain knowledge** and **plots** (scatter).  
> **提示：** **相关不等于因果。** 请结合**领域知识**与**散点图**进行判断。

---

## Supervised Learning: Regression / 监督学习：回归
- **Regression predicts numeric outputs**; common forms: **linear, polynomial**. 
**回归用于预测数值输出**；常见形式：**线性回归、多项式回归**。
- **Model line (simple):** `y = β x + α` (slope β, intercept α). 
**（单变量）模型直线：** `y = β x + α`（斜率 β，截距 α）。

---

## Least Squares / 最小二乘法
- **Idea:** choose β, α to **minimize the sum of squared residuals**. 
**思想：** 选择 β、α，使**残差平方和**最小。

```
Given points (x_i, y_i), residual e_i = y_i − (β x_i + α)
Objective: minimize  Σ e_i^2
给定样本 (x_i, y_i)，残差 e_i = y_i − (β x_i + α)
目标：最小化  Σ e_i^2
```

---

## Simple Regression (Height→Weight) / 单回归（身高→体重）
- **Task:** clarify the relation and predict **weight from height** with `bmi.csv`.  
**任务：** 用 `bmi.csv` **阐明身高→体重**的关系并进行预测。
- **Libraries:** Pandas · Matplotlib · scikit‑learn.  
**使用库：** Pandas · Matplotlib · scikit‑learn。
- **Plot all points (blue) and the fitted line (red).**  
**绘制所有点（蓝）及拟合直线（红）。**
- **Predict for new heights.**  
**对新输入的身高进行预测。**

---

## Multiple Regression (Real‑estate) / 重回归（不动产示例）
- **Task:** model **price** using **area** and **time‑to‑nearest‑station** with `nara.csv`.  
**任务：** 使用 `nara.csv` 用**面积**与**到最近车站所需时间**预测**房价**。
- **Note:** the **target y uses log** in slides; **invert** to get price.  
**说明：** 幻灯里 **y 取对数**；预测后需**反变换**为价格。
- **Predict price for “10 min, 90㎡” and compare with real data (mean ≈ 18.6M).**  
**示例：** 预测“10 分钟、90㎡”的不动产价格，并与真实数据比较（均值约 **1860 万**）。

---

## Polynomial vs Ridge / 多项式回归 vs 岭回归
- **For complex patterns**, **polynomial** and **ridge** can help.  
**当分布更复杂时**，**多项式回归**与**岭回归**可能更合适。
- **Ridge:** add **L2 penalty** to control coefficient size and reduce overfitting.  
**岭回归：** 添加 **L2 正则化**以限制系数大小、缓解过拟合。
- **Polynomial:** expand features with powers (`x, x², x³, …`) then fit a linear model.  
**多项式回归：** 先构造幂特征（`x, x², x³, …`），再拟合线性模型。

<details><summary>Scaling & Pipelines (best practice) / 特征缩放与流水线（最佳实践）</summary>

- **Feature scaling** (e.g., `StandardScaler`) is important for **ridge**.  
**岭回归前进行**特征缩放**（如标准化）很重要。**
- Use **`Pipeline`** to chain `Scaler → PolyFeatures → Ridge`.  
**用 **`Pipeline`** 串联 `缩放 → 多项式特征 → 岭回归`。**
- Tune hyperparameters (degree, α) via **`GridSearchCV`**.  
**用 **`GridSearchCV`** 调参（多项式次数、岭回归系数 α）。**

</details>

---

## Evaluation & Diagnostics (补充) / 评估与诊断（补充）
- **Train/Validation split:** keep a hold‑out set to gauge generalization.  
**训练/验证拆分：** 留出验证集评估泛化。**
- **Metrics:** **MAE**, **MSE**, **RMSE**, **R²**.  
**指标：** **MAE**、**MSE**、**RMSE**、**R²**。**
- **Residual plots:** check linearity & heteroscedasticity.  
**残差图：** 检查线性关系与方差齐性。**
- **Multicollinearity:** compute **VIF** when features may correlate.  
**多重共线：** 当特征可能相关时计算 **VIF**。**

---

## Hands‑on Templates / 上机模板

### 1) Simple Linear Regression (Height→Weight) / 单回归（身高→体重）
```python
# English / 中文：用身高预测体重（bmi.csv）
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("bmi.csv").drop(columns=["No."], errors="ignore")
df = df.dropna(subset=["height","weight"])

X = df[["height"]].values
y = df["weight"].values

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(Xtr, ytr)
print("coef, intercept:", model.coef_, model.intercept_)

yp = model.predict(Xte)
print("MAE:", mean_absolute_error(yte, yp), "R2:", r2_score(yte, yp))

plt.scatter(X, y, s=12)                       # blue points / 蓝点：原始数据
xs = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
plt.plot(xs, model.predict(xs))               # red line / 红线：回归直线
plt.xlabel("Height"); plt.ylabel("Weight"); plt.title("Height→Weight"); plt.show()

new_heights = np.array([[160],[170],[180]])
print("Predicted weights:", model.predict(new_heights))
```

### 2) Multiple Regression (Nara real‑estate) / 重回归（奈良房价）
```python
# English / 中文：用面积与到站时间预测房价（nara.csv）
import numpy as np, pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("nara.csv")  # columns: area, time_to_station, price_log (示例列名)
X = df[["time_to_station","area"]].values
y_log = df["price_log"].values

Xtr, Xte, ytr_log, yte_log = train_test_split(X, y_log, test_size=0.2, random_state=42)

lin = LinearRegression().fit(Xtr, ytr_log)
print("coef, intercept (on log-price):", lin.coef_, lin.intercept_)

# Inference: invert log to get price / 反变换得到价格
def inv_log(p): return np.exp(p)  # 若为自然对数；若为log10，请改用 10**p

# Example prediction: 10 min, 90 m^2
example = np.array([[10, 90]])
pred_price = inv_log(lin.predict(example))[0]
print("Predicted price (10min, 90㎡):", int(pred_price))
```

### 3) Polynomial + Ridge via Pipeline / 通过流水线实现多项式 + 岭回归
```python
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

pipe = Pipeline([
    ("poly", PolynomialFeatures(include_bias=False)),
    ("scaler", StandardScaler()),
    ("ridge", Ridge())
])

param_grid = {
    "poly__degree": [1, 2, 3],
    "ridge__alpha": [0.1, 1.0, 10.0]
}

gscv = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
gscv.fit(Xtr, ytr)  # 用你的 Xtr, ytr（例如 height->weight 任务）
print("Best params:", gscv.best_params_, "R2 (cv):", gscv.best_score_)
```

---

## Homework / 课后作业
- **Q:** Using the **same height–weight dataset**, if we want to **input weight and predict height**, **how should we modify the code?**  
**题：** 使用同一 **身高–体重数据**，若要**输入体重预测身高**，**应如何修改代码？**

<details><summary>Hint (code pattern) / 提示（代码范式）</summary>

```python
# Swap roles: X <- weight, y <- height / 交换自变量与目标：X=体重，y=身高
X = df[["weight"]].values
y = df["height"].values

# The rest stays the same (split, fit, predict, evaluate).
# 其余流程相同（划分、训练、预测、评估）。
```
</details>


<h2></h2>

[← Previous Lecture / 上一讲](./lecture04.md) · [Next Lecture / 下一讲 →](./lecture06.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

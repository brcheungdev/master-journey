[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.
  
# Artificial Intelligence Software Utilization I — Lecture 10 / 人工知能ソフトウェア活用Ⅰ — 第10讲
**Topic:** Neural Networks — Data Processing · Activation Functions · Loss Functions · Optimizers  
**主题：** 神经网络 —— 数据加工 · 激活函数 · 损失函数 · 优化算法

---

## Table of Contents / 目录
- [Today’s Agenda / 今日内容](#todays-agenda--今日内容)
- [NN Structure / 神经网络的结构](#nn-structure--神经网络的结构)
- [Data Processing (to Numbers) / 数据加工（转成数值）](#data-processing-to-numbers--数据加工转成数值)
- [Activation Functions / 激活函数](#activation-functions--激活函数)
- [Loss Functions / 损失函数](#loss-functions--损失函数)
- [Optimizers / 优化算法](#optimizers--优化算法)
- [Exercises / 课堂练习](#exercises--课堂练习)
- [Supplement / 补充说明 ](#supplement-optional--补充说明)


---

## Today’s Agenda / 今日内容
- **NN composition and training steps: data processing → activation → loss → optimizer.**   
**神经网络的组成与训练流程：数据加工 → 激活函数 → 损失函数 → 优化算法。** 

---

## NN Structure / 神经网络的结构
- **A neural network consists of multiple layers (each with many neurons).**   
**神经网络由多层构成（每层包含多个神经元）。** 
- **Layout:** *Input layer → Hidden layer(s) → Output layer*.   
**结构：** *输入层 → 隐藏层（中间层）→ 输出层*。 
- **Input/Output are numbers; an NN is a machine that performs numeric transformation.**   
**输入/输出均为数值；神经网络是执行数值变换的“机器”。** 

```text
Input / 输入  ┃  Hidden / 隐藏  ┃  Output / 输出
[ x ]  ──▶  [ f(Wx+b) ]  ──▶  [ ŷ ]
```
**Schematic of forward pass: affine → activation.**  
**前向传播示意：仿射变换 → 激活函数。**

---

## Data Processing (to Numbers) / 数据加工（转成数值）
- **NNs operate on numbers only; text/images/audio/video must be converted to numeric form (and sometimes back).**   
**神经网络只能处理数值；文本/图像/音频/视频需转换为数值形式（并可能需要再转回）。** 

### Images & Video / 图像与视频
- **Images are matrices/tensors of pixel intensities (e.g., RGB 0–255); video is a sequence of image frames over time (thus frame info + temporal info).**   
**图像是像素强度的矩阵/张量（如 RGB 0–255）；视频是按时间序排列的多帧图像（因此包含帧信息 + 时间序列信息）。** 

```
RGB triplets / RGB 三元组示例
(0,0,255) (0,255,0) (255,0,0) (255,127,39) (195,195,195) (0,0,0) (163,73,164) (127,127,127) (255,255,255)
```
**Video = frames sequence + time dimension.**   
**视频 = 帧序列 + 时间维度。** 

### Audio / 音频
- **Speech is characterized by frequency, amplitude, and temporal change; human voice often fits within a specific frequency range.**   
**语音由频率、幅度与时间变化构成；人声通常位于特定频段。** 
- **Music can span multiple frequency bands (spectrogram as 2‑D view).**   
**音乐往往覆盖多个频带（可用二维频谱图表示）。** 

### Text / 文本
- **Categorical strings:** **One‑Hot Encoding** (OHE) or **Label Encoding**.   
**类别型字符串：** 使用 **One‑Hot 编码** 或 **标签编码**。 
- **Sentences:** **word embedding** maps tokens to vectors.   
**句子：** **词向量（embedding）**将词元映射为向量。 

#### One‑Hot Encoding / One‑Hot 编码
- **Use Pandas `get_dummies`; see `OHE.csv` on KING‑LMS.**   
**使用 Pandas `get_dummies`；数据见 KING‑LMS 的 `OHE.csv`。** 

```python
import pandas as pd
df = pd.read_csv("OHE.csv")
X_ohe = pd.get_dummies(df, drop_first=False)
X_ohe.head()
```
**Each category becomes a binary flag column.**  
**每个类别变成一个二进制标志列。**

#### Label Encoding / 标签编码
- **Use `sklearn.preprocessing.LabelEncoder`; same `OHE.csv`.**   
**使用 `sklearn.preprocessing.LabelEncoder`；同样使用 `OHE.csv`。** 

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(df["color"])
```
**Map string labels to integers (1,2,3,…).**  
**将字符串标签映射为整数（1,2,3,…）。**

---

## Activation Functions / 激活函数
- **They control neuron “firing” (whether and how strongly to pass information on).**   
**激活函数控制神经元“发火”（是否、以及以多强的强度传递信息）。** 

### Neuron Firing & Threshold / 神经元发火与阈值
- **Pain‑related neurons don’t fire at rest; thresholds vary among people and can shift after stimuli (e.g., injections).**   
**痛觉相关神经在静息时不发火；阈值因人而异，且可受外部刺激（如注射）影响而改变。** 

### Identity / 恒等函数
- **Linear pass‑through: `f(x) = x`.**   
**线性直通：`f(x) = x`。** 

### Step / 阶跃函数
- **Threshold at 0: output 1 if `x ≥ 0`, else 0.**   
**阈值在 0：`x ≥ 0` 输出 1，否则 0。** 

### ReLU
- **Rectified Linear Unit: `f(x)=0 (x<0), f(x)=x (x≥0)`; captures both firing decision and strength.**   
**修正线性单元：`f(x)=0 (x<0), f(x)=x (x≥0)`；既体现是否发火也体现强度。** 

### Sigmoid / S‑curve / S 形（Sigmoid）
- **Range (0,1) with probabilistic interpretation; widely used in binary output layers. `f(x)=1/(1+e^{-x})`.**   
**取值 (0,1)，可作概率解释；常用于二分类输出层。`f(x)=1/(1+e^{-x})`。** 

---

## Loss Functions / 损失函数
- **Why not accuracy/precision/recall during training?** We need **differentiable** objectives to guide gradient‑based updates.   
**为什么训练时不用准确率/精确率/召回率？** 因为需要**可微**的目标来指导基于梯度的更新。 

### Regression: MAE / 回归：MAE 绝对平均误差
- **Definition:** average absolute error between predictions and targets.   
**定义：** 预测与真值之差的绝对值的平均。 

```
MAE = (1/n) * Σ_i |ŷ_i − y_i|
```
**Example values (targets/preds):** `y=[10,10,20,20,30]`, `ŷ=[9,13,22,21,27]`.   
**示例数值（真值/预测）：** `y=[10,10,20,20,30]`，`ŷ=[9,13,22,21,27]`。 

### Classification: Cross‑Entropy / 分类：交叉熵
- **Measures proximity between true distribution `p` and predicted `q`:** `E = − Σ_k p(k) log q(k)`.   
**衡量真实分布 `p` 与预测分布 `q` 之间的接近程度：** `E = − Σ_k p(k) log q(k)`。 
- **Example 1 (cat photo): model outputs `(0.8,0.1,0.1)` → compute cross‑entropy.**   
**示例 1（猫的照片）：模型输出 `(0.8,0.1,0.1)` → 计算交叉熵。** 
- **Example 2 (dog photo): model outputs `(0.4,0.3,0.3)` → compute cross‑entropy; smaller means closer to the true distribution.**   
**示例 2（狗的照片）：模型输出 `(0.4,0.3,0.3)` → 计算交叉熵；越小表示越接近真实分布。** 

---

## Optimizers / 优化算法
- **Optimizers adjust weights to minimize loss; the number of weights grows quickly with network size.**   
**优化算法通过调整权重最小化损失；网络规模增大时权重数会快速增加。** 
- **Gradient Descent updates weights along the negative gradient; Adam is a widely used, robust, general‑purpose optimizer (used last time).**   
**梯度下降沿负梯度方向更新；Adam 兼具通用性与鲁棒性，被广泛使用（上次已用）。** 

```text
w ← w − η · ∂Loss/∂w
```
**Basic weight update rule (η = learning rate).**  
**基本权重更新规则（η 为学习率）。**

---

## Exercises / 课堂练习
- **Define ReLU & Sigmoid in Python; evaluate at inputs `-1, 0, 1, 3`** (use `math.exp` for `e^x`).   
**在 Python 中定义 ReLU 与 Sigmoid；在 `-1, 0, 1, 3` 上求值**（`e^x` 用 `math.exp`）。 

```python
# English / 中文：实现 ReLU 与 Sigmoid，并在样例点上测试
import math

def relu(x): 
    return x if x >= 0 else 0.0

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

for x in [-1, 0, 1, 3]:
    print(x, "ReLU=", relu(x), "Sigmoid=", round(sigmoid(x), 6))
```
**Run and confirm outputs match intuition (threshold & S‑curve).**  
**运行后确认输出符合直觉（阈值与 S 形）。**

- **Compute MAE** for the given vectors `y` and `ŷ`.   
**为给定向量 `y` 与 `ŷ` 计算 MAE。** 

```python
y  = [10,10,20,20,30]
yp = [ 9,13,22,21,27]
mae = sum(abs(a-b) for a,b in zip(y,yp)) / len(y)
print("MAE =", mae)
```

- **Compute cross‑entropy** for the 3‑class examples (one‑hot `p`, predicted `q`).   
**为三分类示例（one‑hot 的 `p`，预测 `q`）计算交叉熵。** 

```python
import math
def cross_entropy(p, q):
    return -sum(pi * math.log(qi + 1e-12) for pi, qi in zip(p, q))

print("Cat example:", cross_entropy([1,0,0], [0.8,0.1,0.1]))
print("Dog example:", cross_entropy([0,1,0], [0.4,0.3,0.3]))
```


---

## Supplement  / 补充说明
<details><summary>Activation tips / 激活函数选型小贴士</summary>

- **ReLU** is default for hidden layers; watch for **dead ReLUs** (try LeakyReLU).  
**隐藏层默认用 ReLU；注意“ReLU 死亡”，可试 LeakyReLU。**
- **Sigmoid** saturates (gradients vanish) for large |x|; reserve for **binary outputs**.  
**Sigmoid 在 |x| 大时饱和（梯度消失）；多用于**二分类输出层**。**
</details>

<details><summary>Loss choices / 损失函数选用</summary>

- **MAE vs MSE vs Huber:** MSE penalizes outliers more; **Huber** blends both.  
**MAE/MSE/Huber：MSE 对离群更敏感；**Huber**兼具两者优点。**
- **Cross‑entropy & Softmax:** prefer **`log-softmax`** for numerical stability.  
**交叉熵与 Softmax：更推荐 **`log-softmax`** 以提升数值稳定性。**
</details>

<details><summary>Optimizers & schedules / 优化器与学习率</summary>

- **SGD/Momentum/Adam** are common; try **learning‑rate decay** or **cosine annealing**.  
**常见有 SGD/Momentum/Adam；可使用**学习率衰减**或**余弦退火**。**
</details>

<h2></h2>

[← Previous Lecture / 上一讲](./lecture09.md) · [Next Lecture / 下一讲 →](./lecture11.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

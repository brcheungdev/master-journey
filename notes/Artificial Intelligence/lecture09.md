[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.
  
# Artificial Intelligence Software Utilization I — Lecture 10 / 人工知能ソフトウェア活用Ⅰ — 第10讲
**Topic:** Neural Networks Overview — DNN · CNN · RNN · Autoencoder · GAN · DQN (+ Spiral Classification Practice)  
**主题：** 神经网络总览 —— DNN · CNN · RNN · 自编码器 · 生成对抗网络 · DQN（含螺旋数据分类实操）


---

## Table of Contents / 目录
- [When Kernel SVM Fails / 当核 SVM 也无能为力](#when-kernel-svm-fails--当核-svm-也无能为力)
- [Neural Networks: Intuition / 神经网络：直觉](#neural-networks-intuition--神经网络直觉)
- [NN Structure & Capacity / 神经网络结构与容量](#nn-structure--capacity--神经网络结构与容量)
- [TensorFlow Playground & Loss Curves / Playground 与损失曲线](#tensorflow-playground--loss-curves--playground-与损失曲线)
- [Compute & GPU / 计算量与 GPU](#compute--gpu--计算量与-gpu)
- [NN Families: DNN · CNN · RNN · AE · GAN · DQN / 神经网络家族](#nn-families-dnn--cnn--rnn--ae--gan--dqn--神经网络家族)
- [Practice: Classify Spiral Data / 实操：分类螺旋数据](#practice-classify-spiral-data--实操分类螺旋数据)



---

## When Kernel SVM Fails / 当核 SVM 也无能为力
- **Example:** **spiral‑shaped** data cannot be separated well even with kernel SVM .   
**示例：** **螺旋数据**即使使用核 SVM 也难以良好分割。 

---

## Neural Networks: Intuition / 神经网络：直觉
- **Brains contain countless neurons interconnected; they control our actions, thoughts, and awareness.**   
**大脑含有无数相互连接的**神经元**；它们共同控制我们的动作、思想与意识。** 
- **Neural Networks (NN) are mathematical models inspired by biological neurons; invented in the 1st AI boom and widely used in today’s 3rd boom (ML).**   
**神经网络（NN）是受生物神经元启发的数学模型；在**第一次 AI 热潮**即被提出，现处于以**机器学习**为核心的**第三次 AI 热潮**中广泛应用。** 
- **NN can classify spiral data with high accuracy .**   
**NN 能**高精度**分类螺旋数据。** 

---

## NN Structure & Capacity / 神经网络结构与容量
- **NNs stack layers:** **input → hidden (one or more) → output**.   
**NN 由多层堆叠：**输入层 → 隐藏层（1 层或多层）→ 输出层**。** 
- **Increasing neurons/layers changes representational power; experiment interactively at TensorFlow Playground.**   
**增减神经元/层数会改变表征能力；可在 TensorFlow Playground 上交互实验。** 

---

## TensorFlow Playground & Loss Curves / Playground 与损失曲线
- **Loss** gets **smaller** as the model improves; often plateaus after enough epochs.   
**随着模型改进，**损失（Loss）**会**降低**；达到一定轮数后常进入平台期。** 
- **Learning curve:** plot of loss vs epochs; **L‑shaped** curves indicate good training; **zig‑zag** can mean unstable learning (sometimes temporary).   
**学习曲线：** 损失随轮数变化的曲线；**L 形**通常表示学习良好；**锯齿**可能代表不稳定（也可能是暂时波动）。** 
- **Target on slide:** **Test loss < 0.02** and **epochs < 500** for classification at Playground.   
**幻灯目标：** 在 Playground 上**测试损失 < 0.02** 且 **轮数 < 500** 完成分类。** 

---

## Compute & GPU / 计算量与 GPU
- **Complexity note:** kernel SVM scales roughly with data²; **NNs scale ~ data³** .   
**复杂度提示：** 核 SVM 近似随**数据量平方**增长；**NN 近似随数据量立方**增长。** 
- **Therefore, training large NNs on CPU can be slow; prefer **GPU** (e.g., GTX 1080Ti vs i9 core counts).**   
**因此在 CPU 上训练大规模 NN 可能很慢；建议使用 **GPU**（对比了 i9 与 1080Ti 的核心数）。** 

---

## NN Families: DNN · CNN · RNN · AE · GAN · DQN / 神经网络家族
- **DNN (Deep Neural Network):** “deep” nets with **≥4 layers** (≥2 hidden); widely used for **tabular/high‑dimensional** data classification.   
**DNN（深度神经网络）：** 层数“更深”的网络，通常 **≥4 层**（隐藏层 ≥2）；常用于**高维表格数据**分类。 
- **CNN (Convolutional Neural Network):** contains **convolutions**; dominant in **computer vision** (e.g., face recognition, autonomous driving).   
**CNN（卷积神经网络）：** 含 **卷积** 运算；在**计算机视觉**中占主导（如人脸识别、自动驾驶）。 
- **RNN (Recurrent NN):** internal **loops** handle **sequences** (speech, text); widely used in **NLP**.   
**RNN（循环网络）：** 通过**循环结构**处理**时序**（语音、文本）；广泛用于 **NLP**。 
- **Autoencoder & GAN:** **image generation** capable models; quality improves with more training.   
**自编码器与 GAN：** 能**生成图像**的模型；随训练轮数增多，生成图像越来越像目标。 
- **DQN (Deep Q‑Network):** **deep reinforcement learning**; learns strategies that **maximize rewards** (state/actions/reward idea).   
**DQN（深度 Q 网络）：** **深度强化学习**；学习**最大化回报**的策略（展示状态/动作/回报示意）。 

---

## Practice: Classify Spiral Data / 实操：分类螺旋数据
- **Goal:** build a small NN to classify **spiral‑shaped** 2‑D data. **Code is provided on KING‑LMS** .   
**目标：** 构建一个小型 NN 对**螺旋形**二维数据分类。**代码见 KING‑LMS**。 

```python
# Minimal Keras template (binary spiral) / 二分类螺旋最小样例（Keras）
# Note: Replace `make_spiral()` with the course-provided data generator.
# 注意：将 `make_spiral()` 替换为课程提供的数据生成器。

import numpy as np, tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# X shape: (N,2), y shape: (N,1) with {0,1}
X, y = make_spiral(n_points=1000, noise=0.2, random_state=0)  # placeholder
y = y.astype("float32")

model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(16, activation="tanh"),
    layers.Dense(16, activation="tanh"),
    layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer=keras.optimizers.Adam(1e-2),
              loss="binary_crossentropy",
              metrics=["accuracy"])

history = model.fit(X, y, epochs=300, batch_size=64, verbose=0,
                    validation_split=0.2)

print("Final val acc:", history.history["val_accuracy"][-1])

# Decision boundary visualization (toy) / 决策边界可视化（示意）
xs = np.linspace(X[:,0].min()-1, X[:,0].max()+1, 300)
ys = np.linspace(X[:,1].min()-1, X[:,1].max()+1, 300)
xx, yy = np.meshgrid(xs, ys)
grid = np.c_[xx.ravel(), yy.ravel()].astype("float32")
pp = model.predict(grid, verbose=0).reshape(xx.shape)

import matplotlib.pyplot as plt
plt.contourf(xx, yy, (pp>0.5).astype(int), alpha=0.2)
plt.scatter(X[:,0], X[:,1], c=y, s=8)
plt.title("NN on Spiral"); plt.xlabel("x1"); plt.ylabel("x2"); plt.show()
```

---


<h2></h2>

[← Previous Lecture / 上一讲](./lecture09.md) · [Next Lecture / 下一讲 →](./lecture11.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 11 / 人工知能ソフトウェア活用Ⅰ — 第11讲
**Topic:** Convolutional Neural Networks — Convolution & Pooling; Casting Defect Classification Practice  
**主题：** 卷积神经网络（CNN）—— **卷积** 与 **池化**；铸件缺陷识别实操

---

## Table of Contents / 目录
- [Why CNN for Images? / 为什么用 CNN 处理图像？](#why-cnn-for-images--为什么用-cnn-处理图像)
- [CNN Learns Features / CNN 会从图片中学“特征”](#cnn-learns-features--cnn-会从图片中学特征)
- [Convolution / 卷积](#convolution--卷积)
- [Pooling / 池化](#pooling--池化)
- [Exercise A: Paper‑and‑Pencil CNN / 练习A：手算模拟 CNN](#exercise-a-paperandpencil-cnn--练习a手算模拟-cnn)
- [Exercise B: Casting Classification with CNN / 练习B：用 CNN 识别铸件缺陷](#exercise-b-casting-classification-with-cnn--练习b用-cnn-识别铸件缺陷)

---

## Why CNN for Images? / 为什么用 CNN 处理图像？
- **Images of the same factory parts vary in camera distance and angle; two classes: “normal” and “defect”. How to classify?**   
**同一工厂部件的照片会因为相机距离与角度不同而变化；存在“正常品 / 缺陷品”两类。如何分类？** 
- **Answer: use a **Convolutional Neural Network (CNN)**.**   
**答案：使用 **卷积神经网络（CNN）**。** 

---

## CNN Learns Features / CNN 会从图片中学“特征”
- **CNNs, inspired by the visual cortex, automatically extract features from images.**   
**CNN 受视觉皮层启发，能从图像中**自动提取特征**。** 
- **Examples: stripe patterns of a cat; contour of a dog’s head.**   
**示例：猫的条纹、狗头的轮廓。** 

---

## Convolution / 卷积
- **definition:** slide a **filter/kernel** over the image matrix; multiply‐accumulate (MAC) numbers and sum to get the output.   
**定义：** 将**卷积核/滤波器**在图像矩阵上滑动；做逐元素**乘加**并求和得到输出。 

```text
Input (example) / 输入（示例）
1 0 1
1 1 1
0 0 1

Kernel / 卷积核
1 0
-1 1

Slide & MAC / 滑动与乘加 → Output / 输出
① 1×1 + 0×0 + 1×(-1) + 1×1 = 1
② 0×1 + 1×0 + 1×(-1) + 1×1 = 0
③ 1×1 + 1×0 + 0×(-1) + 0×1 = 1
④ 1×1 + 1×0 + 0×(-1) + 1×1 = 2

Output map / 输出特征图
1 0
1 2
```

<details><summary>Padding · Stride (supplement) / 填充与步幅（补充）</summary>

- **Padding:** pad borders with zeros to preserve size; avoids shrinking after convolution.  
**填充：** 在边界补 0 以保持尺寸，避免每次卷积都缩小。
- **Stride:** step length of the kernel; larger stride downsamples faster.  
**步幅：** 卷积核每次移动的步长；步幅越大，下采样越快。
</details>

---

## Pooling / 池化
- **Operation: select a representative number from a local region (e.g., max or average).**   
**操作：在局部区域内选择一个代表性数值（如最大值或均值）。** 

```text
Input / 输入
1 0
1 2

Max Pooling → 2        Average Pooling → 1
```
**Max picks the largest; Average computes the mean.**   
**最大池化取最大值；平均池化取算术平均值。** 

<details><summary>Why pooling? (supplement) / 为什么池化？（补充）</summary>

- **Translation tolerance:** reduces sensitivity to small shifts and noise.  
**平移容忍：** 降低对小位移与噪声的敏感。
- **Computational savings:** halves or quarters spatial size → fewer parameters later.  
**计算节省：** 缩小空间尺寸 → 随后层参数更少。
</details>

---

## Exercise A: Paper‑and‑Pencil CNN / 练习A：手算模拟 CNN
- **Task:** for two images (`digit 0` and `digit 1`), apply **convolution → average pooling** in order, and compute results by hand.   
**任务：** 针对两张图片（“数字 **0**”与“数字 **1**”），依次执行**卷积 → 平均池化**，并手算出结果。 

```text
Digit 0 / 数字 0
1 1 1
1   1
1 1 1

Digit 1 / 数字 1
  1
  1
  1

Filter / 滤波器
-1  1
-1  1
```
**Follow the same multiply‑accumulate rules as above.**   
**按前述乘加规则逐步计算。** 

---

## Exercise B: Casting Classification with CNN / 练习B：用 CNN 识别铸件缺陷
- **Goal:** classify **100 test images** under `test_data/` using a trained CNN.   
**目标：** 使用训练好的 CNN 识别 `test_data/` 目录下的 **100 张**测试图片。 

### Data Package & Setup / 数据包与环境
- **Use `exercise_data.zip` from KING‑LMS.** Unzip; **read CSV**, and **one‑hot encode labels**.   
**使用 KING‑LMS 的 `exercise_data.zip`。** 解压；**读入 CSV**；**将标签做 One‑Hot**。 

```python
# English / 中文：解压、读 CSV、标签 One-Hot（示意）
import pandas as pd
df = pd.read_csv("train_labels.csv")     # file name per package / 名称以数据包为准
y = pd.get_dummies(df["label"])          # One-Hot
```

### Count & Inspect Images / 统计并检查图片
- **Count images in train/validation folders; prepare image reading.**   
**统计训练/验证集图片数量；准备图片读取。** 

```python
# Example with tf.keras utilities / 使用 Keras 工具（示意）
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_it = gen.flow_from_directory("train_data", target_size=(128,128),
                                   class_mode="categorical", subset="training")
val_it   = gen.flow_from_directory("train_data", target_size=(128,128),
                                   class_mode="categorical", subset="validation")
```

### Train/Validation Split & Rules / 训练-验证划分与输入规则
- **Set the training/validation ratio; define input shape, normalization, and batch size.**   
**设置训练/验证比例；明确输入尺寸、归一化与批大小等规则。** 

### Build the CNN / 构建 CNN
- **Stack `Conv2D → Pooling → … → Dense` to form the model.**   
**使用 `Conv2D → 池化 → … → Dense` 堆叠形成模型。** 

```python
# Minimal CNN (template) / 最小 CNN 模板（示意）
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Input(shape=(128,128,3)),
    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(2),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(2),
    layers.Conv2D(128, 3, activation="relu"),
    layers.GlobalAveragePooling2D(),
    layers.Dense(64, activation="relu"),
    layers.Dense(train_it.num_classes, activation="softmax")
])
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()
```

### Train / 训练
- **Set learning parameters and start training; plot the learning curves.**   
**设置学习参数并开始训练；绘制学习曲线。** 

```python
hist = model.fit(train_it, epochs=20, validation_data=val_it)

import matplotlib.pyplot as plt
plt.plot(hist.history["accuracy"]); plt.plot(hist.history["val_accuracy"]); plt.title("Accuracy"); plt.show()
plt.plot(hist.history["loss"]); plt.plot(hist.history["val_loss"]); plt.title("Loss"); plt.show()
```

### Evaluate & Predict / 评估与预测
- **Use the trained CNN to classify photos and save results to file; list example predictions.**   
**用训练好的 CNN 对照片做识别，并将结果写入文件；展示预测示例。** 

```python
test_it = gen.flow_from_directory("test_data", target_size=(128,128),
                                  class_mode=None, shuffle=False)
probs = model.predict(test_it)
preds = probs.argmax(axis=1)

import numpy as np, csv
with open("predictions.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["filename","pred_label"])
    for fn, p in zip(test_it.filenames, preds):
        w.writerow([fn, test_it.class_indices_inv[p]])  # class_indices_inv: 需自行构造反查表
```

> **Tip ：** In real projects, we typically add **data augmentation** (flip/rotate/crop), **early stopping**, and **learning‑rate scheduling** as standard practice.  
> **提示：** 实际项目中常配合**数据增强**（翻转/旋转/裁剪）、**提前停止**与**学习率调度**。

<h2></h2>

[← Previous Lecture / 上一讲](./lecture10.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

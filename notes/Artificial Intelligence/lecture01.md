[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Artificial Intelligence Software Utilization I — Lecture 01 / 人工知能ソフトウェア活用Ⅰ — 第1讲


---

## Today’s Agenda / 本讲次安排

- **What is the course “AI Software Utilization”?**  
**本课程“人工知能ソフトウェア活用”讲什么？**
- **What is “Artificial Intelligence” anyway?**  
**“人工智能”到底是什么？**

## Please first ask yourself / 请先自问

- **What is your Python level?**  
- **你的 Python 水平？**
  1. **Can write simple calculator‑like programs (or higher).**  
     **能写“计算器级”的小程序（或更高）。**
  2. **Studied before and know most syntax.**  
     **学过，语法基本了解。**
  3. **Studied before but nearly forgotten.**  
     **学过，但差不多忘了。**
  4. **Never studied, but know the name.**  
     **没学过，但听过名字。**
  5. **Python? What’s that?**  
     **Python?那是啥?**

<details><summary>Placement advice by level / 分层学习建议</summary>

- **Levels 1–2:** start from **NumPy/Pandas quickstart** below; finish Week‑1 checklist.  
**1–2 级：** 从下文 **NumPy/Pandas 快速上手** 开始；完成第 1 周清单。
- **Level 3:** refresh **Python syntax + plotting**; then ML pipeline.  
**3 级：** 复习 **Python 语法 + 画图**；随后进入 ML 流程。
- **Levels 4–5:** finish **Colab onboarding** first; use notebooks as guided worksheets.  
**4–5 级：** 先完成 **Colab 环境**；用示例笔记本作为引导式习题。

</details>

## Course Goals / 课程目标
- **This is not a Windows‑software introduction course; it is a programming course.**  
**本课并非 Windows 工具使用介绍，而是**编程课程**。**
- **(Option) Understand Python basic syntax.**  
**（可选）掌握 Python 基础语法。**
- **Become familiar with libraries used in AI programming.**  
**熟悉用于人工智能编程的常用库。**
- **Understand the minimal workflow of simple AI projects.**  
**理解简易 AI 项目的最小工作流。**
- **Be able to analyze simple datasets with ML.**  
**能用机器学习分析入门数据集。**

<details><summary>Minimal AI workflow (cheatsheet) / 最小 AI 工作流（速查）</summary>

```
1) Define problem → choose task type (classification/regression/clustering)
2) Collect/inspect data → split train/validation/test
3) Baseline model → metrics → error analysis
4) Improve (features/model/hyperparams) → log experiments
5) Package results → demo/paper/poster → reproducibility
```
**1）** 定义问题→选择任务类型（分类/回归/聚类）  
**2）** 收集/检查数据→划分训练/验证/测试  
**3）** 基线模型→度量→误差分析  
**4）** 改进（特征/模型/超参）→记录实验  
**5）** 打包成果→演示/论文/海报→可复现性
</details>

<details><summary>Fix‑it plan / 自救方案</summary>

- **Daily 60–90 min focused coding;** one notebook/day.  
**每天 60–90 分钟专注编码；一日一 Notebook。**
- **Re‑implement baselines from scratch;** understand each line.  
**从零复现基线；逐行搞懂。**
- **Maintain an “error log”;** write what went wrong and why.  
**维护“错误日志”；记录错因与修复。**

</details>

## AI: Current Trend / 当下的“人工智能”
- **Examples: face recognition, autonomous driving, speech recognition, LLMs ...**  
**常见例子：人脸识别、自动驾驶、语音识别、大语言模型 等**
- **What other examples can you name?**  
**你还想到哪些例子？**

<details><summary>Pipeline snapshot (vision) / 视觉任务典型流程</summary>

```
Data → Augmentation → Model (CNN/ViT) → Loss → Optimizer → Metrics
数据 → 增广 → 模型（CNN/ViT）→ 损失 → 优化器 → 指标
```
</details>

## Definition of AI / 人工智能的定义
- **Term coined in 1956.**  
**“人工智能”一词诞生于 **1956 年**。**
- **A research field on designing/realizing intelligent information processing systems by computers.**  
**研究利用计算机**设计与实现**智能信息处理系统的领域。**
- **Study how to mechanically perform previously human‑only intelligent acts (recognition, inference, language use, creation) via appropriate algorithms and data/knowledge. (Nipponica)**  
**探究如何通过**算法**与**数据/知识**，让计算机**机械地执行**原本只有人类能完成的**认知、推理、语言运用、创造**等智能行为。（日本大百科全书《ニッポニカ》）**

## “Intelligent” Components / “智能”构成
- **Recognition, Inference, Language use, Creation.**  
**识别、推论、语言运用、创造。**

## Recognition (Quizzes) / 识别（提问）
- **Rule‑based object recognition in images is extremely hard.**  
**用“规则”识别图像中的物体非常困难。**
- **We know “apple” because we were taught with many examples.**  
**我们之所以会识别，是因大量示例的“教学”。**

<details><summary>Feature pitfalls / 特征陷阱</summary>
  
- **Spurious cues (背景、光线) can fool rules or models.**  
**伪相关线索（背景、光照）会误导规则/模型。**
- **Mitigation:** diverse data + augmentation + validation splits.  
**缓解：多样数据 + 增广 + 合理划分验证集。**
</details>

- **Quiz 1: Summarize the features of a given fruit in words.**  
**提问 1：用语言归纳某种水果的特征。**
- **Examples: “Red and round”, “Has a stem”, “Glossy surface” … but ambiguity remains.**  
**例如：“红且圆”“有果梗”“有光泽”……但仍存在歧义。**
- **Even for apples, rule‑based discrimination is hard.**  
**即使是“苹果”这样简单的对象，基于规则的判别也很难。**
- **Quiz 2: Why do you know it’s an apple?**  
**提问 2：你为何知道它是“苹果”？**
- **Answer: Because we were taught so.**  
**答案：因为**被教导**如此。**

## From Teaching to Machine Learning / 从“被教”到机器学习
- **Label many varied examples ⇒ model learns a mapping X→Y.**  
**标注多样样本 ⇒ 模型学习 X→Y 的映射。**
- **Generalizes to unseen apples if training covered the variation.**  
**若覆盖足够变体，模型可泛化到未见样本。**
- **If we teach computers (with many labeled examples), they can recognize apples ⇒ machine learning (a kind of AI).**  
**若向计算机“示范+标注”大量样本，它也能学会识别苹果 ⇒ **机器学习**（人工智能的一种）。**
- **Different shapes/colors but all labeled “apple”.**  
**形状与颜色各异，但标签同为“苹果”。**

## Reasoning Example / 推论示例
- **Computer trained on many apple photos can infer: “Apple” vs. “Not an apple”.**  
- **在大量苹果照片上训练的计算机可推断：“苹果”/“非苹果”。**

<details><summary>Confusion matrix & metrics / 混淆矩阵与指标</summary>

```
               Predicted Positive    Predicted Negative
Actual Positive        TP                    FN
Actual Negative        FP                    TN
```
**Precision = TP / (TP + FP)**  
**准确率（精确率）= TP / (TP + FP)**  
**Recall = TP / (TP + FN)**  
**召回率 = TP / (TP + FN)**  
**F1 = 2PR / (P + R)**  
**F1 = 2PR / (P + R)**
</details>

## Creation Example / 创造示例
- **Teach “green apple” then ask the computer to draw one.**  
**教会“青苹果”的概念后，要求计算机“画出一只”。**
- **Generative models can synthesize a “green apple”.**  
**生成式模型可合成“青苹果”。**
- **Initial outputs vary from very wrong to somewhat similar—like how we learn to draw.**  
**早期结果从“完全不对”到“有点像”——与人类学画类似。**
- **Early outputs may be rough; training improves fidelity.**  
**早期结果粗糙；训练可提升逼真度。**

<details><summary>Discriminative vs Generative / 判别式 vs 生成式</summary>

- **Discriminative:** learn **p(y|x)** (e.g., logistic regression, ResNet).  
**判别式：** 学 **p(y|x)**（如逻辑回归、ResNet）。
- **Generative:** learn **p(x|y)** or **p(x)** (e.g., Naive Bayes, VAE).  
**生成式：** 学 **p(x|y)** 或 **p(x)**（如朴素贝叶斯、VAE）。

</details>

## Ada Lovelace & 19th‑Century Computer / 艾达·拉夫莱斯与19世纪计算机
- **Augusta Ada King, Countess of Lovelace (1815‑12‑10 – 1852‑11‑27): often regarded as the world’s first programmer.**  
**艾达·拉夫莱斯（1815‑12‑10 – 1852‑11‑27），常被视为**世界上第一位程序员**。**
- **She foresaw abilities of computers beyond mathematics ⇒ early vision of AI.**  
**她预见计算机可超越纯数学计算 ⇒ **人工智能**的先声。**
- **Analytical Engine: steam‑powered mechanical general‑purpose computer; Ada devised “programs” (procedures) for it.**  
**解析机：以蒸汽驱动的**机械式通用计算机**；艾达为其设想了“程序”。**
- **Hypothesis: If musical notes and harmony theory are numerically encoded, the engine could generate music.**  
**预想：若将**音律与和声理论**数字化，解析机可**生成音乐**。**

## Realizing AI via Numbers / 用数值表征实现AI
- **If colors/pixels are encoded as numbers (e.g., RGB/arrays), computers can classify or generate images.**  
若将颜色/像素数字化（如 **RGB/数组**），计算机即可进行**图像识别或生成**。
- **If characters/language units are encoded as numbers, computers can translate or generate text.**  
若将**文字/语言单元**数字化，计算机即可进行**翻译或文本生成**。
- **Text as numbers (tokens/embeddings) ⇒ translate or write.**  
文本转数值（词元/嵌入）⇒ 翻译或写作。

```
Pixel Grid → Flatten/Conv → Features → Classifier
像素网格 → 展平/卷积 → 特征 → 分类器
```

<details><summary>Sample RGB Swatches / RGB 示例色块</summary>

```
(255, 0, 0)   (0, 255, 0)   (0, 0, 255)
(255,127,39)  (195,195,195) (0, 0, 0)
(163,73,164)  (127,127,127) (255,255,255)
```
</details>


## **Set up your programming environment.**  
## **完成编程环境搭建。**
- **Default: Google Colab.**  
**默认：使用 **Google Colab**。**
- **Optional local install: Anaconda + Jupyter Notebook.**  
**本地可选：安装 **Anaconda + Jupyter Notebook**。**

### Step‑by‑Step: Colab Onboarding / Colab 入门分步
1. **Sign in to Google; open `colab.new`.**  
**登录 Google；打开 `colab.new`。**
2. **Change runtime → GPU (if needed).**  
**需要时将运行时改为 GPU。**
3. **Create a first cell; run `print("Hello AI")`.**  
**创建首个单元；运行 `print("Hello AI")`。**
4. **Mount Drive if using datasets.**  
**使用数据集时挂载 Drive。**

```
from google.colab import drive
drive.mount('/content/drive')
```
**在 Colab 中挂载云盘以访问数据。**

### Step‑by‑Step: Anaconda Local / 本地 Anaconda 分步
1. **Install Anaconda (Python 3.x).**  
**安装 Anaconda（Python 3.x）。**
2. **Create env & install libs.**  
**创建环境并安装库。**
```
conda create -n aisoft python=3.10 -y
conda activate aisoft
pip install numpy pandas matplotlib scikit-learn notebook
```
**创建并激活虚拟环境，安装必需库。**
3. **Launch Jupyter Notebook.**  
**启动 Jupyter Notebook。**

```
jupyter notebook
```

<details><summary>Troubleshooting / 故障排除</summary>

- **Pip/Conda conflicts:** prefer **conda‑forge** or pin versions.  
**Pip/Conda 冲突：** 优先 conda‑forge 或固定版本。
- **CUDA not found:** ensure GPU toolkit matches driver.  
**缺少 CUDA：** 确认 GPU 工具包与驱动匹配。

</details>


## Hints / 提示链接
- **Google Colab (JA):** `https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja`  
- **Google Colab（日文）：**`https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja`
- **Tianchi Lab Notebook:** `https://tianchi.aliyun.com/notebook-ai/detail?postId=127457`  
- **天池 Notebook：**`https://tianchi.aliyun.com/notebook-ai/detail?postId=127457`
- **Anaconda + Jupyter (JA):** `https://qiita.com/tttamaki/items/0d4fc01c10dd40a13552`  
- **Anaconda + Jupyter（日文）：**`https://qiita.com/tttamaki/items/0d4fc01c10dd40a13552`
- **Anaconda + Jupyter (ZH):** `https://zhuanlan.zhihu.com/p/112256678`  
- **Anaconda + Jupyter（中文）：**`https://zhuanlan.zhihu.com/p/112256678`

<details><summary>Quick Check / 快速自检</summary>

```
Task 1: Open Colab, run: print(1+1)
任务1：打开 Colab，运行：print(1+1)
Expected: 2
期望输出：2
```
</details>

## Hands‑on Primer / 代码动手速成
- **NumPy arrays & shapes.**  
**NumPy 数组与形状。**
```
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)  # (2,3)
```
**形状用于描述数据维度，是调试要点。**

- **Pandas DataFrame basics.**  
**Pandas 表格基础。**
```
import pandas as pd
df = pd.DataFrame({"x":[1,2,3], "y":[2,4,6]})
print(df.describe())
```
**`describe()` 快速查看统计摘要。**

- **Matplotlib plotting.**  
**Matplotlib 画图。**
```
import matplotlib.pyplot as plt
plt.plot(df["x"], df["y"]); plt.xlabel("x"); plt.ylabel("y"); plt.title("Line")
plt.show()
```
**图可视化有助于发现数据问题。**

- **Scikit‑learn minimal classification (k‑NN).**  
**Scikit‑learn 极简分类（k‑近邻）。**
```
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(Xtr, ytr)
yp = clf.predict(Xte)
print(classification_report(yte, yp))
```
**分层抽样 `stratify` 有助于类别均衡。**

<details><summary>Overfitting vs Underfitting / 过拟合 vs 欠拟合</summary>

- **Overfitting:** train↑, test↓ ⇒ too complex.  
**过拟合：** 训练高、测试低 ⇒ 模型过复杂。
- **Underfitting:** both low ⇒ too simple.  
**欠拟合：** 训练与测试都低 ⇒ 模型过简单。
- **Fixes:** more data, regularization, early stop, better features.  
**缓解：** 增数据、正则化、早停、更优特征。

</details>

<h2></h2>

[Next Lecture / 下一讲 →](./lecture02.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)


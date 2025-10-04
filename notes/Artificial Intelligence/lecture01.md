[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

# Artificial Intelligence Software Utilization I — Lecture 01 / 人工知能ソフトウェア活用Ⅰ — 第1讲


---

## Today’s Agenda / 本讲次安排

- **What is the course “AI Software Utilization”?**  
- **本课程“人工知能ソフトウェア活用”讲什么？**
- **What is “Artificial Intelligence” anyway?**  
- **“人工智能”到底是什么？**

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
- **本课并非 Windows 工具使用介绍，而是**编程课程**。**
- **(Option) Understand Python basic syntax.**  
- **（可选）掌握 Python 基础语法。**
- **Become familiar with libraries used in AI programming.**  
- **熟悉用于人工智能编程的常用库。**
- **Understand the minimal workflow of simple AI projects.**  
**理解简易 AI 项目的最小工作流。**
- **Be able to analyze simple datasets with ML.**  
**能用机器学习分析入门数据集。**

## AI: Current Trend / 当下的“人工智能”
- **Typical examples:** Face recognition, Autonomous driving, Speech recognition, etc.  
- **常见例子：**人脸识别、自动驾驶、语音识别**等**。  
- **What other examples can you name?**  
- **你还想到哪些例子？**

## Definition of AI / 人工智能的定义
- **Term coined in 1956.**  
- **“人工智能”一词诞生于 **1956 年**。**
- **A research field on designing/realizing intelligent information processing systems by computers.**  
- **研究利用计算机**设计与实现**智能信息处理系统的领域。**
- **Study how to mechanically perform previously human‑only intelligent acts (recognition, inference, language use, creation) via appropriate algorithms and data/knowledge. (Nipponica)**  
- **探究如何通过**算法**与**数据/知识**，让计算机**机械地执行**原本只有人类能完成的**认知、推理、语言运用、创造**等智能行为。（日本大百科全书《ニッポニカ》）**

## “Intelligent” Components / “智能”构成
- **Recognition, Inference, Language use, Creation.**  
- **识别、推论、语言运用、创造。**

## Recognition (Quizzes) / 识别（提问）
- **Rule‑based object recognition in images is extremely hard.**  
- **用“规则”识别图像中的物体非常困难。**
- **Quiz 1: Summarize the features of a given fruit in words.**  
- **提问 1：用语言归纳某种水果的特征。**
- **Examples: “Red and round”, “Has a stem”, “Glossy surface” … but ambiguity remains.**  
- **例如：“红且圆”“有果梗”“有光泽”……但仍存在歧义。**
- **Even for apples, rule‑based discrimination is hard.**  
- **即使是“苹果”这样简单的对象，基于规则的判别也很难。**
- **Quiz 2: Why do you know it’s an apple?**  
- **提问 2：你为何知道它是“苹果”？**
- **Answer: Because we were taught so.**  
- **答案：因为**被教导**如此。**

## From Teaching to Machine Learning / 从“被教”到机器学习
- **If we teach computers (with many labeled examples), they can recognize apples ⇒ machine learning (a kind of AI).**  
- **若向计算机“示范+标注”大量样本，它也能学会识别苹果 ⇒ **机器学习**（人工智能的一种）。**
- **Different shapes/colors but all labeled “apple”.**  
- **形状与颜色各异，但标签同为“苹果”。**

## Reasoning Example / 推论示例
- **Computer trained on many apple photos can infer: “Apple” vs. “Not an apple”.**  
- **在大量苹果照片上训练的计算机可推断：“苹果”/“非苹果”。**

## Creation Example / 创造示例
- **Teach “green apple” then ask the computer to draw one.**  
- **教会“青苹果”的概念后，要求计算机“画出一只”。**
- **Initial outputs vary from very wrong to somewhat similar—like how we learn to draw.**  
- **早期结果从“完全不对”到“有点像”——与人类学画类似。**

## Ada Lovelace & 19th‑Century Computer / 艾达·拉夫莱斯与19世纪计算机
- **Augusta Ada King, Countess of Lovelace (1815‑12‑10 – 1852‑11‑27): often regarded as the world’s first programmer.**  
- **艾达·拉夫莱斯（1815‑12‑10 – 1852‑11‑27），常被视为**世界上第一位程序员**。**
- **She foresaw abilities of computers beyond mathematics ⇒ early vision of AI.**  
- **她预见计算机可超越纯数学计算 ⇒ **人工智能**的先声。**
- **Analytical Engine: steam‑powered mechanical general‑purpose computer; Ada devised “programs” (procedures) for it.**  
- **解析机：以蒸汽驱动的**机械式通用计算机**；艾达为其设想了“程序”。**
- **Hypothesis: If musical notes and harmony theory are numerically encoded, the engine could generate music.**  
- **预想：若将**音律与和声理论**数字化，解析机可**生成音乐**。**

## Realizing AI via Numbers / 用数值表征实现AI
- **If colors/pixels are encoded as numbers (e.g., RGB), computers can classify or generate images.**  
- **若将颜色/像素数字化（如 **RGB**），计算机即可进行**图像识别或生成**。**
- **If characters/language units are encoded as numbers, computers can translate or generate text.**  
- **若将**文字/语言单元**数字化，计算机即可进行**翻译或文本生成**。**

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
- **默认：使用 **Google Colab**。**
- **Optional local install: Anaconda + Jupyter Notebook.**  
- **本地可选：安装 **Anaconda + Jupyter Notebook**。**

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



<h2></h2>

[Next Lecture / 下一讲 →](./lecture02.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)


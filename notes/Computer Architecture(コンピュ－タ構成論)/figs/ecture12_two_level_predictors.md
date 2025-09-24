为什么要两级预测
位 / 2位饱和计数器 预测器，只看上一次分支结果，或者靠一个短状态机记忆最近几次分支，但它无法捕捉分支的模式，比如：
- 一个分支每 3 次跳一次：TTNTTNTTNT...
- 需要知道最近 3 次历史，才能预测下一个分支
于是研究人员提出了 Two-Level Adaptive Branch Prediction：
- 第一级：记录分支历史（局部或全局）
- 第二级：用这个历史模式去索引一个预测表，从而预测下一次分支的走向
三种主要类型：
-(a) Local Predictor / 局部分支预测
  - 每个分支都有自己独立的历史寄存器，记录这个分支最近 N 次的走向（Taken / Not Taken）
  - 适合单个分支有稳定规律的情况，比如循环
 
-(b) Global Predictor / 全局分支预测
  - 所有分支共享一个全局分支历史寄存器 (GHR)，记录最近 N 次所有分支的走向
  - 适合跨分支相关的模式，比如分支 A 和分支 B 的结果相关联
  - 
-(c) Hybrid Predictor / 混合分支预测
  - 把 Local 和 Global 两个预测器的结果都算出来
  - 用一个选择器 (Chooser) 决定用哪一个预测结果作为最终答案

---
# Two-level Branch Predictors  
# 局部/全局/混合两级分支预测示意

---

## Local Predictor / 局部分支预测
- **思想**: 针对**每个分支**维护其最近 N 次历史位串 → 索引到预测表  
- **适用**: 单个分支有稳定的可预测模式（如循环计数）  

```
Branch PC --> Local History Reg (N bits) --> Pattern Table --> Predict T/NT
```
Global Predictor / 全局分支预测
- 思想: 维护全局分支历史寄存器 (GHR)，所有分支共享一条历史位串 → 索引预测表
- 适用: 跨分支相关模式（多个分支交替决定路径）
```
Global History Reg (GHR) --> Pattern Table --> Predict T/NT
```
Hybrid Predictor / 混合分支预测
- 思想: 局部+全局两个预测器并行 → 由选择器表仲裁最终预测结果
- 典型结构: Alpha 21264 (local+global+chooser)
```

         +--> Local Predictor --+
         |                      |--> Chooser --> Final Prediction
PC/Hist -+--> Global Predictor -+

```

命名示例
- gshare: GHR 与 PC 异或 → 索引全局表
- GAs / GAg: 全局历史 + 分支地址选择模式表
- PAs: 每个分支有私有历史表
- TAGE / Perceptron: 高级方法，多表 / 神经网络加权决策
- 

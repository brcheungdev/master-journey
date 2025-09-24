1位/2位饱和计数器状态机（branch_counter_fsm.md）
在现代 CPU 里，指令通常是流水线执行的。
- 分支指令（if/else、循环跳转）会打断流水线，因为 CPU 必须等到分支条件算出来，才能知道下一条该取哪条指令。
- 如果分支多、预测错，流水线就得“清空”重新取指，性能会大幅下降。
所以 CPU 里引入了 分支预测（Branch Prediction）：
- 预测分支跳还是不跳，让流水线提前取指，尽量减少停顿。
- 如果预测错了，就回退并修正。

最简单的分支预测器是1位饱和计数器：
只记住上次分支的结果：
- 上次跳 → 下次预测跳
  - 上次不跳 → 下次预测不跳
  - 但如果分支模式是 TNTNTN…，就会每次都预测错，性能很差。
于是有了2位饱和计数器：
- 4 个状态：
  - 强跳 ST (Strongly Taken)
  - 弱跳 WT (Weakly Taken)
  - 弱不跳 WN (Weakly Not Taken)
  - 强不跳 SN (Strongly Not Taken)
- 只有连续两次反向分支才会切换预测方向，抗抖动更强。

# 1-bit vs 2-bit Saturating Counter FSM  
# 1位/2位饱和计数器状态机

## 1-bit Predictor / 1位预测器
- **状态数**: 2  
- **预测规则**:  
  - 上次分支 **Taken** → 预测 Taken  
  - 上次分支 **Not Taken** → 预测 Not Taken  
- **问题**: 在 `TNTNTN...` 或 `TFTF...` 模式中频繁抖动（即每次都错）。
```
States:
 [ N ] --T--> [ T ]
 [ T ] --N--> [ N ]

Legend:
 N = Predict Not Taken
 T = Predict Taken
```

---

## 2-bit Predictor / 2位预测器
- **状态数**: 4  
- **预测规则**:
    - 需连续两次反向才切换预测方向 → 抗抖动
    - T = 预测 Taken
    - N = 预测 Not Taken 
- **状态定义**:  
  - `ST` = Strongly Taken  
  - `WT` = Weakly Taken  
  - `WN` = Weakly Not Taken  
  - `SN` = Strongly Not Taken
```
         +-----------+      N      +-----------+
         |    ST     |------------>|    WT     |
         +-----------+             +-----------+
                ^                       |
                | T                     | N
                |                       v
         +-----------+      N      +-----------+
         |    SN     |<-------------|    WN     |
         +-----------+              +-----------+
                ^                        |
                | N                      | T
                |                        v
         +-----------+      T      +-----------+
         |    ST     |<-------------|    WT     |
         +-----------+              +-----------+
```
- **好处**: 在循环或轻微波动分支中比 1-bit 更稳定，典型误判率示例：  
  - 1-bit ≈ 10%  
  - 2-bit ≈ 4%  


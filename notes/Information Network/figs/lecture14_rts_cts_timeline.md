# RTS/CTS Timeline Quick Reference  
# RTS/CTS 时序速查表

---

## ⚪ Hidden Terminal Problem | 隐藏终端问题
- 无线终端 A/B → AP  
- B 听不到 A 的发送 → 可能在 A 正发数据时开始发送 → 碰撞  

---

## ⚪ RTS/CTS Solution | RTS/CTS 解决方案
1. **RTS**: A 向 AP 请求发送权限  
2. **CTS**: AP 同意 → 通知所有能听到 AP 的终端 → 保持静默  
3. **DATA**: A 发送数据  
4. **ACK**: AP 成功接收后，返回 ACK 确认 → 其他终端恢复竞争  

---

## ⚪ Timing Sequence | 时序流程
```
A: DIFS → RTS → SIFS → CTS (AP) → SIFS → DATA → SIFS → ACK (AP)
B: 监听到 CTS / ACK → 在此期间保持静默
```

---

## ⚪ Key Points | 关键要点

- CTS 覆盖区域 > A 发送范围 → 隐藏终端也能听到 CTS
- 期间所有终端静默，避免碰撞
- ACK 确认后其他终端才重新竞争信道

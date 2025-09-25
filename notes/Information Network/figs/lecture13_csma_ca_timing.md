# CSMA/CA Timing Quick Reference  
# CSMA/CA 时序速查表

---

## ⚪ Basics | 基础
- **CSMA**: Carrier Sense Multiple Access  
- **CA**: Collision Avoidance (无线无法边发边听, 只能避免碰撞)  

---

## ⚪ Timing Elements | 时序要素
| Symbol  | Meaning (English)                  | 含义（中文）           |
|---------|-------------------------------------|------------------------|
| DIFS    | Distributed Inter-Frame Space       | 分布式帧间间隔          |
| SIFS    | Short Inter-Frame Space             | 短帧间间隔             |
| ACK     | Acknowledgment Frame                | 确认帧                 |
| Backoff | Random backoff before transmission  | 退避等待随机时隙        |

---

## ⚪ Sequence Example | 典型时序
```
DIFS → Backoff Countdown → DATA Frame → SIFS → ACK
```
多个节点竞争：空闲则继续倒计时，碰撞 → 退避窗口加倍


## ⚪ Backoff Algorithm | 退避算法
- Binary Exponential Backoff: 碰撞后退避窗口翻倍，减少再次碰撞概率

## Key Points
-  DIFS 空闲检测, SIFS 优先级高于 DIFS
-  成功帧后必须收到 ACK, 否则重传
-  ackoff 决定发送顺序, 碰撞后加倍退避

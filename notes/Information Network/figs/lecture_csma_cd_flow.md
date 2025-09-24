# CSMA/CD Operation Flow & Timing  
# CSMA/CD 工作流程与时序图

---

## ⚪ Purpose 目的
- 展示 **CSMA/CD** 在以太网中的**完整发送流程**  
- 说明 **退避算法 (Binary Exponential Backoff)** 的工作原理  
- 提供 **ASCII 时序图** 与**参数说明**，便于理解  

---

## ⚪ CSMA/CD Steps 工作步骤

```
1. Carrier Sense (载波侦听)
   - Before sending, listen to the channel.
   - If the channel is busy → wait until idle.

2. Interframe Gap (帧间隔)
   - Even when idle, wait a minimum IFG before sending new frame.
   - IFG @10 Mb/s = 9.6 μs (96 bit times).

3. Transmit (发送)
   - Begin sending frame while continuously monitoring for collision.

4. Collision Detection (碰撞检测)
   - If collision detected → immediately abort sending.
   - Send JAM signal to inform all nodes.

5. Backoff (退避)
   - After abort, wait random backoff time before retry.
   - Backoff time = t × SlotTime
   - SlotTime = 512 bit times = 51.2 μs @10 Mb/s
   - Random t ∈ [0, 2^k − 1]
     where k = min(n, 10); n = collision count for this frame
   - If n > 16 → give up & report error to upper layer

6. Retry
   - After backoff time expires → return to step 1.
```

## ⚪ ASCII Timing Diagram 时序图
```
Time →
+-----------------------------------------------------------+
| Listen (Idle?) | IFG wait | Transmit Frame  | Collision?  |
|                |         |                 | Yes → JAM   |
+-----------------------------------------------------------+
                               |                | 
                               v                v
                           Abort Tx        Backoff Timer
                               |                |
                               +------- Retry --+
```
## Parameters 参数总结
```
IFG (Interframe Gap):
  - 9.6 μs = 96 bit times @10 Mb/s

Slot Time:
  - 512 bit times = 51.2 μs @10 Mb/s
  - Minimum frame size = 64 B = 512 bits
  - Ensures collision is detectable before frame ends

Backoff Algorithm (Binary Exponential):
  - After nth collision, choose random t ∈ [0, 2^k − 1]
    where k = min(n, 10)
  - Backoff time = t × SlotTime
  - n > 16 → Abort frame, report error
```

---
## Key Points
- CSMA/CD = Carrier Sense + Multiple Access + Collision Detection
- Key timers:
  - IFG ensures spacing between frames
  - SlotTime ensures collisions are detected in minimum frame
- Binary Exponential Backoff reduces collisions under heavy load
- After 16 collisions, frame is discarded → upper layer notified

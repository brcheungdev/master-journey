# TCP Congestion Control Quick Reference  
# TCP 拥塞控制速查表

---

## ⚪ Key Variables | 关键变量
| Variable   | Meaning (English)          | 含义（中文）               |
|------------|----------------------------|----------------------------|
| cwnd       | Congestion Window           | 拥塞窗口，限制发送速率      |
| ssthresh   | Slow Start Threshold        | 慢启动阈值，指数/线性分界点 |

---

## ⚪ Phases | 阶段
1. **Slow Start (SS)**  
   - cwnd 初始 = 1 MSS  
   - 每个 RTT **指数**增长：`cwnd = cwnd × 2` 直到 `cwnd ≥ ssthresh`

2. **Congestion Avoidance (CA)**  
   - cwnd ≥ ssthresh 后 → **线性**增长：`cwnd = cwnd + 1 MSS / RTT`

---

## ⚪ Events | 事件处理
| Event             | cwnd Update                     | ssthresh Update       | Mode After     |
|-------------------|----------------------------------|-----------------------|----------------|
| Timeout            | cwnd=1 MSS                      | ssthresh=cwnd/2        | Slow Start      |
| 3 DupACKs (Fast RT)| cwnd=ssthresh+3 MSS → 线性增      | ssthresh=cwnd/2        | Cong Avoidance  |

---

## ⚪ AIMD Behavior | 加性增乘性减
- **Additive Increase**: 线性增（+1 MSS 每 RTT）  
- **Multiplicative Decrease**: 丢包 → cwnd 减半  

---

## ⚪ Key Points 
- Timeout → cwnd = 1, ssthresh = cwnd/2, 慢启动
- Fast Retransmit → cwnd 线性增加, 不回到1
- AIMD 平衡吞吐与公平, 防止网络拥塞崩溃

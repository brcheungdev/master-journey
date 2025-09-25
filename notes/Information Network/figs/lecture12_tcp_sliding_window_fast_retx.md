# TCP Sliding Window & Fast Retransmit Quick Reference  
# TCP 滑动窗口与快速重传速查表

---

## ⚪ Sliding Window Basics | 滑动窗口基础
- **Purpose**: 提高吞吐量，避免停等式传输  
- **Mechanism**: 未确认前允许连续发送一定数据量；收到 ACK 后窗口前移  
- **Window Size**: 由接收端通告，限制发送方未确认数据量  

```
Sender Window = [Sent but unacked] + [Allowed to send next]
ACK arrives → slide window right → send new data
```

---

## ⚪ Sliding Window Example | 滑动窗口示例
```
Window Size = 3000 bytes, MSS = 1000
Send: SEQ=1..1000, 1001..2000, 2001..3000
Receive ACK=1001 → Slide window → Send 3001..4000
```

---

## ⚪ Fast Retransmit | 快速重传
- **Conventional Retransmission**: 等待超时再重传，延迟较大
- **Fast Retransmit**: 收到**3个或以上重复ACK** → 立即重传丢失段，无需等超时
```
If ACK=1001 duplicated ≥3 times → retransmit missing segment at once
```

---

## ⚪ Timeout & RTT | 超时与往返时延
- RTT (Round Trip Time): 报文发送到接收 ACK 所需时间
- RTO (Retransmission Timeout): 动态调整，略大于 RTT，避免过早重传

---

## ⚪ Key Points
- 滑动窗口提高吞吐，允许管道化发送
- 重复 ACK ≥3 → 快速重传，减少等待
- RTO 动态调节，兼顾及时性与稳定性
- 流量控制避免接收端缓存溢出

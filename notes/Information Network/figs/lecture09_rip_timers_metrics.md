# RIP Protocol Quick Reference  
# RIP 协议速查表

---

## ⚪ RIP Basics | RIP 基础
- **Algorithm**: Distance Vector  
- **Metric**: Hop Count (1 hop = 1 router)  
- **Max Hop**: 16 → Unreachable  
- **Transport**: UDP (port 520)  

---

## ⚪ RIP Timers | RIP 定时器

| Timer                   | Default Value  | Purpose (English)                          | 作用（中文）                   |
|-------------------------|----------------|--------------------------------------------|--------------------------------|
| Update Timer            | 30s            | Periodic route update                       | 定期路由更新周期                |
| Timeout (Invalid) Timer | 180s           | Mark route invalid if no update received    | 未更新则标记路由失效            |
| Garbage Collection Timer| 120s           | Time to remove invalid routes after timeout | 超时后删除无效路由              |

---

## ⚪ RIP Metrics & Limits | RIP 度量与限制
- **Hop Count**: 1–15 → Reachable; 16 → Unreachable  
- **Split Horizon** & **Poison Reverse**: 防止无穷计数环路  
- **Count-to-Infinity**: 度量逐渐增加直到 16 才丢弃，收敛较慢

---

## ⚪ RIP Message Format | RIP 报文格式
```
| Command | Version | Address Family ID | IP Address | Metric |
|  (Up to 25 route entries per message)                  |
```
- **Command**: Request / Response
- **Version**: RIP v1 / v2
- **Metric**: 1–16 (Hop Count)

---
## ⚪ Key Points
• 简单、轻量，适合小型网络
• 30s 周期更新，180s 超时，120s 垃圾回收
• 最大跳数 16 避免真正无穷，但收敛慢

# STP (Spanning Tree Protocol) Quick Reference  
# 生成树协议速查表

---

## ⚪ Purpose 目的
避免交换网络中的**环路 (loops)** 和**广播风暴**，通过**计算生成树**自动阻塞冗余链路，并在链路故障时**快速收敛**。

---

## ⚪ STP Process | STP 流程

```
1) Root Bridge 选举
   - Bridge ID = 优先级 + MAC地址
   - 最小 Bridge ID 成为 Root Bridge

2) Path Cost 计算
   - 每条链路有路径代价
   - 从 Root Bridge 出发到各交换机的总代价最小路径获胜

3) 端口角色分配
   - Root Port: 指向根桥的最优路径端口
   - Designated Port: 每个网段上负责转发的端口
   - Blocking Port: 既非 Root 也非 Designated，阻塞避免环路

4) Forwarding / Blocking
   - 最终形成无环的生成树
   - 仅 Root/Designated 端口转发流量
```

---
## ⚪ STP Port Roles | 端口角色

| Role            | Function (English)       | 功能（中文）       |
| --------------- | ------------------------ | ------------ |
| Root Port       | Best path to Root Bridge | 通向根桥的最优路径端口  |
| Designated Port | Forward for each segment | 每个链路段的代表转发端口 |
| Blocking Port   | Prevent loops            | 阻塞以防止环路      |
| Disabled Port   | Administratively down    | 人工关闭，不参与 STP |

---
## ⚪ STP Convergence | 收敛过程
- 链路或端口故障时，STP 重新计算生成树，将原本阻塞的端口切换为转发状态。
- 传统 **STP **收敛约 30–50 秒；**RSTP** 将其降到数秒级。
 
---
## ⚪ STP Timers | 计时器

| Timer         | Default | Purpose (English)         | 作用（中文）              |
| ------------- | ------- | ------------------------- | ------------------- |
| Hello Time    | 2s      | Root Bridge 发 BPDU 间隔     | 根桥发送 BPDU 的周期       |
| Max Age       | 20s     | BPDU 超时时间                 | 超过此时间未收 BPDU → 端口老化 |
| Forward Delay | 15s     | Listening/Learning 阶段持续时间 | 转发延迟（两阶段各 15 秒）     |


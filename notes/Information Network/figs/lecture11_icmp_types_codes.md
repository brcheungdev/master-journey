# ICMP Types & Codes Quick Reference  
# ICMP 报文类型与代码速查表

---

## ⚪ ICMP Overview | ICMP 概览
- **Purpose**: 网络连通性探测、差错报告、路由重定向  
- **Encapsulation**: ICMP 在 **IP 数据部分**，由 Type & Code 表示含义  
- **Typical Usage**: `ping`, `traceroute`, 路由器差错通知

---

## ⚪ Common ICMP Types | 常见类型

| Type | Name (English)         | 名称（中文）           | Usage / Meaning (English)        | 用途 / 含义（中文）                |
|------|-------------------------|------------------------|----------------------------------|----------------------------------|
| 0    | Echo Reply              | 回显应答               | Reply to ping                    | `ping` 应答                       |
| 3    | Destination Unreachable | 目的不可达             | Codes: 0=Network, 1=Host, 3=Port  | 无到目的网络/主机/端口的路由       |
| 5    | Redirect                | 重定向                 | Suggest better gateway           | 建议主机改走更优网关              |
| 8    | Echo Request            | 回显请求               | Sent by ping                     | `ping` 请求                       |
| 11   | Time Exceeded           | 超时                   | TTL expired                      | TTL 耗尽或分片重组超时            |

---

## ⚪ ICMP Destination Unreachable Codes | 目的不可达代码

| Code | Meaning (English)                | 含义（中文）                 |
|------|----------------------------------|------------------------------|
| 0    | Network Unreachable               | 网络不可达                   |
| 1    | Host Unreachable                  | 主机不可达                   |
| 2    | Protocol Unreachable              | 协议不可达                   |
| 3    | Port Unreachable                   | 端口不可达                   |
| 4    | Fragmentation Needed & DF Set      | 需分片但 DF 置位              |

---

## ⚪ TTL & Time Exceeded | TTL 与超时
- **TTL** 每经过一台路由器减 1  
- 减到 **0** → 丢弃报文并发 **Type 11** (Time Exceeded) 给源主机  
- 用于 `traceroute` 探测路径  

---

## ⚪ Key Points 
```
• Echo Req/Rep 构成 ping 基础
• Type 3 不可达，含多种 Code
• Type 5 重定向用于优化路由
• Type 11 超时用于路径探测
```

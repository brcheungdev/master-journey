# RIP v2 Packet Fields Quick Reference  
# RIP v2 报文字段速查表

---

## ⚪ RIP v2 Overview | RIP v2 概览
- **Routing Protocol**: Distance Vector  
- **Transport**: UDP port 520  
- **Metric**: Hop Count (1–15 = reachable; 16 = unreachable)  
- **Update Interval**: 30s periodic updates  
- **Supports**: CIDR masks, Authentication, Multicast (224.0.0.9)

---

## ⚪ RIP v2 Packet Format | RIP v2 报文结构
```
| Command | Version=2 | Address Family ID | Route Tag |
|   IP Address        |   Subnet Mask     | Next Hop  | Metric (1..15; 16=unreachable) |
(… up to 25 route entries per RIP message …)
```

---
## ⚪ Field Descriptions | 字段说明

| Field             | Bits / Type | Meaning (English)              | 含义（中文）         |
| ----------------- | ----------- | ------------------------------ | -------------- |
| Command           | 8 bits      | 1=Request, 2=Response          | 1=请求, 2=响应     |
| Version           | 8 bits      | Always 2 for RIP v2            | RIP v2 固定值 2   |
| Address Family ID | 16 bits     | 2 = IP (IPv4)                  | 地址族标识，2=IPv4   |
| Route Tag         | 16 bits     | External routes tag            | 外部路由标识         |
| IP Address        | 32 bits     | Destination network            | 目的网络地址         |
| Subnet Mask       | 32 bits     | Netmask for the route          | 子网掩码           |
| Next Hop          | 32 bits     | Next-hop router IP             | 下一跳路由器地址       |
| Metric            | 32 bits     | 1–15 reachable; 16=unreachable | 1–15=可达，16=不可达 |

---
## ⚪ Key Points 
- RIP v2 增加子网掩码支持 (CIDR)
- 支持多播地址 224.0.0.9 发送更新
- 可配置报文认证 (Password / MD5)
- Metric ≥16 视为不可达，避免无穷计数

# DNS Resolution Flow Quick Reference  
# DNS 名称解析流程速查表

---

## ⚪ DNS Basics | DNS 基础
- **Forward Lookup**: Domain → IP Address  
- **Reverse Lookup**: IP Address → Domain  
- **Recursive Query**: Server queries others on behalf of client  
- **Iterative Query**: Server refers client to another server  

---

## ⚪ DNS Resolution Process | DNS 解析过程

```
Client → Local DNS → Root DNS → TLD DNS → Authoritative DNS → Response
```
**Detailed Steps | 详细步骤**
```
1) Client requests <domain> resolution
2) Local DNS checks cache
3) If unknown, query Root DNS → returns TLD DNS info
4) Query TLD DNS → returns Authoritative DNS info
5) Query Authoritative DNS → returns final A/AAAA record
6) Local DNS caches result, returns IP to client

```

---
## ⚪ DNS Server Roles | DNS 服务器角色

| Role                  | Function (English)                     | 功能（中文）         |
| --------------------- | -------------------------------------- | -------------- |
| Root DNS              | Knows TLD servers                      | 管理顶级域服务器       |
| TLD DNS               | Knows authoritative servers per TLD    | 管理各顶级域的权威服务器信息 |
| Authoritative DNS     | Stores actual domain records           | 存储域名的权威记录      |
| Caching/Recursive DNS | Caches responses, resolves recursively | 缓存/递归解析服务器     |

---
## ⚪ Redundancy & Reliability | 冗余与可靠性
- Deploy at least Primary & Secondary DNS servers
- Zone Transfer keeps secondary synchronized with primary
- Different geographic locations recommended


---
## ⚪ Key Points 
- DNS 查询可递归或迭代，缓存可减少查询次数
- Root → TLD → Authoritative 层级逐级解析
- 正向解析: 域名 → IP；反向解析: IP → 域名
- 主/辅 DNS 提高可靠性，区域传送同步数据

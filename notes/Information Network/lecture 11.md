#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)‘

# Lecture 11: ARP / RARP / ICMP / DHCP / TCP vs UDP / Ports  
# 情報ネットワーク概論 第11回：ARP・RARP・ICMP・DHCP・TCPとUDP・ポート

---

## ⚪ Lecture Overview 
- **ARP**：在同一二层网段内，将 **目的 IP → 目的 MAC**；若目的不在本段，则解析**默认网关（路由器）的 MAC** 作为下一跳。IPv4 专用；IPv6 用 **邻居发现**（ND）替代。
- **RARP**：与 ARP 相反，用 **设备的 MAC → 分配 IP**（需 RARP 服务器，为早期无盘/嵌入设备获取地址）。
- **ICMP**：用于**连通性检测与差错通知**（例如 `ping`），包含**回显请求/应答**与**不可达/重定向/超时**等类型。
- **DHCP**：在 LAN 内**自动分配私有 IP**、掩码、网关、DNS 等；采用**租约**机制（Discover/Offer/Request/ACK）。
- **TCP vs UDP**：IP 为**无连接/不可靠**；传输层提供两类服务：**TCP（面向连接、可靠）**与 **UDP（无连接、尽力而为）**。
- **Ports**：用**五元组**（源/目的 IP、源/目的端口、协议号）识别一次会话；端口分 **Well-known/Registered/Dynamic**，由 **IANA** 统一管理。

---

## ⚪ Lecture Content 

### 1) ARP — Address Resolution Protocol  
### 通过 ARP 将 IP 映射为 MAC
**用途 / Purpose**  
- 让 IP 报文能在**数据链路层**被正确封装与转发：根据**目的 IP**查询**目的 MAC**。若目的主机与本机**同段**，解析其 MAC；若**不同段**，则解析**默认网关的 MAC** 作为下一跳。*（仅 IPv4；IPv6 使用邻居发现 ND）* 

**同段时的基本流程 / Same Segment Flow**  
```
1) 上层交给 IP：需要发往 目的IP
2) ARP 先查 本机 ARP 表（IP↔MAC 映射缓存）
3) 命中 → 直接得到 目的MAC
   未命中 → 以广播 发送 ARP Request(问：谁是 目的IP？)
4) 目标主机 收到请求 → 以单播 回复 ARP Reply(我是 目的IP，对应MAC是 ...)
5) 本机 记录(学习) {目的IP, 目的MAC} 到 ARP 表（有超时生命周期）
```
备注：ARP 表项**数分钟**后过期删除；非目标主机**不回复**。

**不同段时的流程 / Different Segment via Router**
```
1) 本机根据 目的IP 与 子网掩码 计算网络地址 → 发现 目的不在本段
2) 以 “默认网关 的 IP” 为目标发起 ARP Request → 获得 “网关的 MAC”
3) IP 层将 目的IP 的报文，封装到 以太帧：DestMAC=网关MAC，送往路由器
4) 路由器查路由表，若下一跳在其直连网段：
   - 对 目的IP 再做 ARP 解析，得到 “目的主机 MAC”
   - 以 DestMAC=目的MAC 转发
   否则 → 继续向下一跳重复
```
讲义两页配图说明了“不同段时先解析网关 MAC”的要点。

**ARP 表查看 / Inspect ARP Cache**
- **Windows**：在命令提示符执行
```
arp -a
```
列出当前缓存的 IP ↔ MAC（“物理地址”即 MAC）。
 
---

### 2) RARP — Reverse ARP
用途 / Purpose
- 与 ARP 相反：已知** MAC**，向 **RARP 服务器**查询应分配的**IP**。常用于**无盘/嵌入式**设备早期上电自动获取地址。须在服务器上**预配置**该设备的 MAC ↔ IP 对。
 
---

### 3) ICMP — Internet Control Message Protocol 
作用 / What it provides
- **连通性探测**（目的可达性）与**差错通知**（为何被丢弃/无法转发等）。`ping `使用 **Echo** 报文对时延和连通性做粗测；IP 自身不提供这些功能，故由** ICMP **补充。

**常见类型与代码 / Main Types & Codes**
| Type (十进制) | 名称 (JP/EN)                       | 说明                        |   |
| ---------- | -------------------------------- | ------------------------- | - |
| 8          | Echo Request（エコー要求）              | `ping` 请求                 |   |
| 0          | Echo Reply（エコー応答）                | `ping` 应答                 |   |
| 3          | Destination Unreachable（あて先到達不能） | 目的不可达（含多种 **Code**）       |   |
| 5          | Redirect（経路変更/リダイレクト）            | 指示主机改走更优网关                |   |
| 11         | Time Exceeded（時間超過）              | **TTL 耗尽**（每过一台路由器 TTL–1） |   |


**ICMP 消息的封装 / Message Encapsulation**
- **ICMP 位于 IP 数据部分**；通过 **Type/Code** 表示具体情形。TTL 由路由器每转发一次减 1，至**0**触发 **Type 11**。
**Destination Unreachable 示例 / 不可达示例**
- **Code 0**：无到该目的 IP 的路由
- **Code 1**：目的主机未接入网络
- **路由器丢弃后**，给源主机回送“不可达”以便调整（例如缩小分片、改目的等）。
 
---

### 4) DHCP — Dynamic Host Configuration Protocol
功能 / Function
- 在同一 LAN 内**自动为主机分配**：**私有 IP、子网掩码、默认网关、主/备 DNS** 等；采用**租约（Lease）**并可续租/释放；未开机主机**不占用**地址资源。
**工作机制 / How it works（概览） **
```
1) 客户端 请求配置（含期望参数）；服务器 选择可用地址并返回；包含 租约时长
2) 租约到期需续租；不再需要时（关机/断网）客户端 释放地址并通知服务器
```
**获取 IP 的 DORA 流 / DHCP Client Obtains Address**
```
D  Discover  : 客户端以 0.0.0.0 为源、广播探测 DHCP 服务器
O  Offer     : 服务器广播提供可用地址的要约
R  Request   : 客户端广播请求所选地址（仍以 0.0.0.0 为源）
A  ACK       : 服务器确认分配，携带租约等参数
(同段可能有多台服务器，因此均用广播)
```
Windows 设置提示 / Windows Hint
- 勾选“自动获取 IP / DNS”即可使用 DHCP；参数由服务器下发。
 
---

### 5) TCP/IP 模型中的传输层：TCP 与 UDP
**IP 特性 / IP Properties**
- **无连接、不可靠（不确认、不重传）**；因此**可靠性**需由**更上层**提供。
**TCP（面向连接）**
- **可靠传输**：有**顺序控制、重传控制、流量控制、拥塞控制**。适合必须可靠的应用。
**UDP（无连接）**
- **尽力而为**、开销小、实时性强；常用于**IP 语音/多播/广播**、以及**RIP、DHCP**等协议。
 
---

### 6) 端口与会话识别 / Ports & Session Identification
**会话五元组 / 5-tuple**
- 通过以下组合唯一识别一次通信：
**目的 IP、源 IP、目的端口、源端口、协议号（TCP/UDP）**。
**常见服务端口 / Examples**
- HTTP`80`、POP3`110` 等（讲义举例）。
- 
**端口分类 / Port Ranges（IANA 管理）**
  | 类型                    | 范围            | 说明                         |   |
| --------------------- | ------------- | -------------------------- | - |
| **Well-known**        | `0–1023`      | 固定用途、静态分配                  |   |
| **Registered**        | `1024–49151`  | 注册但可复用                     |   |
| **Dynamic/Ephemeral** | `49152–65535` | **客户端**临时端口，由 OS 动态分配，避免冲突 |   |
备注：**IANA**统一管理 IP、域名、端口等互联网编号资源。

---
## Key Points
- **ARP**：同段解析目的主机**MAC**；异段先解析默认**网关MAC**，由路由器继续转发；`arp -a`查看缓存。
- **RARP**：用 MAC 向服务器取 IP，适配无盘/嵌入式场景（需预配对）。
- **ICMP**：`ping`的 Echo Req/Rep；常见类型**3/5/11**；消息在**IP 数据中**，**TTL**触发**Time Exceeded**。
- **DHCP**：自动配置 IP/Mask/GW/DNS；**DORA**交互与租约管理，广播用于多服务器场景。
- **TCP vs UDP**：TCP 可靠（顺序/重传/流/拥塞控制）；UDP 轻量（适合实时/多播/广播）。
- **Ports**：用五元组识别会话；端口分**well-known/registered/dynamic**，由**IANA**管理。

---

## ※※Supplementary Cheat Sheets | 速查单

### ICMP & DHCP Quick Reference
- [ICMP Types & Codes | ICMP 报文类型与代码速查](./figs/lecture11_icmp_types_codes.md)  
  *常见 ICMP 类型、不可达代码、TTL 超时与重定向*

- [DHCP DORA Flow | DHCP DORA 流程速查](./figs/lecture11_dhcp_dora_flow.md)  
  *DHCP Discover/Offer/Request/ACK 四步流程与租约管理*


  

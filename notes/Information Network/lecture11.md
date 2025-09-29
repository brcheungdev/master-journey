[← Back to Course README / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)‘

# Lecture 11: ARP / RARP / ICMP / DHCP / TCP vs UDP / Ports  
# ARP・RARP・ICMP・DHCP・TCP 与 UDP・端口

---

## ⚪ Lecture Overview 
- **ARP**: On a single L2 segment, resolve **destination IP → destination MAC**; if the destination is off-link, resolve the **default gateway’s MAC** as the next hop. IPv4 only; IPv6 uses **Neighbor Discovery (ND)**.  
  **ARP**：在同一二层网段内，将 **目的 IP → 目的 MAC**；若目的不在本段，则解析**默认网关（路由器）的 MAC** 作为下一跳。仅适用于 IPv4；IPv6 使用**邻居发现（ND）**。
- **RARP**: Reverse of ARP; use **device MAC → assigned IP** (via a RARP server) for early diskless/embedded devices.  
  **RARP**：与 ARP 相反，用 **设备的 MAC → 分配 IP**（需 RARP 服务器），多用于早期无盘/嵌入设备。
- **ICMP**: For **reachability tests and error reporting** (e.g., `ping`); includes **Echo** and **Unreachable/Redirect/Time Exceeded**.  
  **ICMP**：用于**连通性检测与差错通知**（如 `ping`），包含**回显请求/应答**与**不可达/重定向/超时**等类型。
- **DHCP**: **Automatically assigns** private IP, mask, gateway, DNS in a LAN; **lease-based** (Discover/Offer/Request/ACK).  
  **DHCP**：在 LAN 内**自动分配**私有 IP、掩码、网关、DNS 等；采用**租约**机制（Discover/Offer/Request/ACK）。
- **TCP vs UDP**: IP is **connectionless/unreliable**; transport offers **TCP (connection-oriented, reliable)** vs **UDP (connectionless, best-effort)**.  
  **TCP vs UDP**：IP 为**无连接/不可靠**；传输层提供 **TCP（面向连接、可靠）** 与 **UDP（无连接、尽力而为）**。
- **Ports**: Identify a flow via the **5‑tuple** (src/dst IP, src/dst port, protocol). Port ranges: **Well‑known/Registered/Dynamic** (managed by **IANA**).  
  **端口**：用**五元组**（源/目的 IP、源/目的端口、协议号）识别一次会话；端口分 **Well-known/Registered/Dynamic**，由 **IANA** 统一管理。

---

## ⚪ Lecture Content 

### 1) ARP — Address Resolution Protocol  
### 通过 ARP 将 IP 映射为 MAC

**Purpose / 用途**  
- Enable correct **L2 encapsulation & forwarding**: given a **destination IP**, find the **destination MAC**. If the destination host is **on-link**, resolve its MAC; if **off-link**, resolve the **default gateway’s MAC** as the next hop. *(IPv4 only; IPv6 uses ND.)*  
  让 IP 报文能在**数据链路层**被正确封装与转发：根据**目的 IP**查询**目的 MAC**。若目的主机与本机**同段**，解析其 MAC；若**不同段**，则解析**默认网关的 MAC** 作为下一跳。*（仅 IPv4；IPv6 使用邻居发现 ND）* 

**Same Segment Flow / 同段时的流程**  
```
1) Upper layer gives IP: needs to send to <dst-IP>
2) ARP checks local ARP cache (IP↔MAC)
3) Hit → get <dst-MAC>
   Miss → broadcast ARP Request (“Who has <dst-IP>?”)
4) Target host replies ARP Reply (unicast): “<dst-IP> is at <dst-MAC>”
5) Sender learns {dst-IP, dst-MAC} into ARP cache (with timeout)
```
```
1) 上层交给 IP：需要发往 <目的IP>
2) ARP 先查 本机 ARP 表（IP↔MAC 映射缓存）
3) 命中 → 直接得到 <目的MAC>
   未命中 → 以广播 发送 ARP Request（谁是 <目的IP>?）
4) 目标主机 单播 ARP Reply："<目的IP> 的 MAC 是 <目的MAC>"
5) 本机 学习并缓存 {目的IP, 目的MAC}（有超时生命周期）
```
备注：ARP 表项**数分钟**后过期删除；非目标主机**不回复**。

**Off-link via Router / 不同段经路由转发**  
```
1) Host computes network via IP & mask → discovers off-link
2) ARP the Default Gateway’s IP → obtain GW-MAC
3) L2 frame uses DestMAC = GW-MAC; router forwards by L3 table
4) Router, if next hop on-link: ARPs for final host’s MAC and forwards
   else: forwards to next hop; repeats
```
```
1) 本机根据 目的IP 与 子网掩码 计算网络地址 → 发现目的不在本段
2) 以 “默认网关 的 IP” 为目标发起 ARP Request → 获得 “网关的 MAC”
3) IP 层将 目的IP 的报文，封装到 以太帧：DestMAC=网关MAC，送往路由器
4) 路由器查路由表，若下一跳在其直连网段：
   - 对 目的IP 再做 ARP 解析，得到 “目的主机 MAC”
   - 以 DestMAC=目的MAC 转发
   否则 → 继续向下一跳重复
```


**Inspect ARP Cache / 查看 ARP 表** 
- **Windows**：在命令提示符执行
```
arp -a
```
显示当前缓存的 IP ↔ MAC（“物理地址”即 MAC）。
 
---

### 2) RARP — Reverse ARP / 反向地址解析协议

**Purpose / 用途**  
- Opposite of ARP: given a device’s **MAC address**, query a **RARP server** to obtain the device’s **IP address**. Commonly used by **diskless/embedded** devices during early boot. Requires a **preconfigured MAC↔IP** mapping on the server.  
- ARP 相反：已知设备的 **MAC 地址**，向 **RARP 服务器**查询应分配的 **IP 地址**。常用于**无盘/嵌入式**设备的上电自举阶段；服务器端需**预先配置 MAC↔IP** 对。
 **Basic flow / 基本流程**  
1. Client boots with only a NIC MAC, broadcasts a **RARP Request** asking “Who am I (IP)?”.  
   设备上电仅有网卡 MAC，广播发送 **RARP Request**（“我的 IP 是什么？”）。  
2. RARP server looks up the MAC in its static table and unicasts a **RARP Reply** with the IP.  
   RARP 服务器在静态表中查询该 MAC，单播返回 **RARP Reply**，告知对应的 IP。  
3. Client configures its IP address and proceeds with boot.  
   客户端据此配置 IP，继续后续启动流程。

> **Note / 说明：** RARP is largely historical and has been superseded by **BOOTP/DHCP** (which provide IP, mask, gateway, DNS, etc.).  
> **提示：** RARP 现已基本被 **BOOTP/DHCP** 取代（后者还能下发掩码、网关、DNS 等参数）。

---

### 3) ICMP — Internet Control Message Protocol / 网际控制报文协议

**What it provides / 作用**  
- **Connectivity probing** (reachability) and **error reporting** (why a packet was dropped or couldn’t be forwarded). `ping` uses **Echo Request/Reply** to roughly measure latency and reachability. IP itself doesn’t provide these functions, so **ICMP** augments it.  
- 提供**连通性探测**（目的可达性）与**差错通知**（说明报文为何被丢弃/无法转发）。`ping` 使用 **回显请求/回显应答（Echo Request/Reply）** 粗略测量时延与可达性。IP 本身不具备这些功能，由 **ICMP** 予以补充。

**Common examples / 常见示例**  
- *Echo Request/Reply* (used by `ping`), *Destination Unreachable*, *Redirect*, *Time Exceeded* (TTL expired).  
- *回显请求/应答*（`ping`）、*目的不可达*、*重定向*、*超时*（TTL 到期）。



**常见类型与代码 / Main Types & Codes**
| Type (十进制) | 名称 (JP/EN)                       | 说明                        |   |
| ---------- | -------------------------------- | ------------------------- | - |
| 8          | Echo Request（エコー要求）              | `ping` 请求                 |   |
| 0          | Echo Reply（エコー応答）                | `ping` 应答                 |   |
| 3          | Destination Unreachable（あて先到達不能） | 目的不可达（含多种 **Code**）       |   |
| 5          | Redirect（経路変更/リダイレクト）            | 指示主机改走更优网关                |   |
| 11         | Time Exceeded（時間超過）              | **TTL 耗尽**（每过一台路由器 TTL–1） |   |


**ICMP Message Encapsulation / ICMP 消息的封装**

- **ICMP sits inside the IP packet’s data area** and uses **Type/Code** to indicate the specific condition. Each router decreases **TTL by 1** when forwarding; when TTL reaches **0**, it triggers **Type 11 (Time Exceeded)**.  
- **ICMP 位于 IP 报文的数据部分**，通过 **Type/Code** 表示具体情形。路由器每转发一次就使 **TTL 减 1**；当 TTL 减到 **0** 时触发 **Type 11（时间超时）**。

**Destination Unreachable — examples / 不可达（Destination Unreachable）示例**

- **Code 0**: No route to the destination IP.  
  **Code 0**：无到该目的 IP 的路由。  

- **Code 1**: Destination host is unreachable (e.g., host not attached).  
  **Code 1**：目的主机不可达（例如主机未接入）。  

- After a router drops the packet, it **sends an ICMP Unreachable** back to the source so the sender can adjust (e.g., reduce fragment size, change destination, etc.).  
- **路由器丢弃报文后**，会向源主机**回送 ICMP 不可达**以便其调整（例如**缩小分片**、**更改目的**等）。

 
---

### 4) DHCP — Dynamic Host Configuration Protocol / 动态主机配置协议

**Function / 功能**  
- Automatically assigns **private IP, subnet mask, default gateway, DNS (primary/secondary)** within the same LAN; uses a **lease** mechanism (renew/release). Hosts **do not consume** addresses while powered off.  
- 在同一 LAN 内**自动为主机分配**：**私有 IP、子网掩码、默认网关、主/备 DNS** 等；采用**租约（Lease）**机制（可续租/释放）；未开机主机**不占用**地址资源。
**How it works (overview) / 工作机制（概览）**  

```
1) Client requests configuration (may include desired parameters); the server selects a free address and replies, including the lease duration.
1) 客户端 请求配置（含期望参数）；服务器 选择可用地址并返回；包含 租约时长
2) Before lease expiry the client must renew; when no longer needed (shutdown/disconnect) the client releases the address and notifies the server.
2) 租约到期需续租；不再需要时（关机/断网）客户端 释放地址并通知服务器
```
**DORA Flow / 获取 IP 的 DORA 流**
```

D  Discover  : Client broadcasts from 0.0.0.0 to discover DHCP servers.  
O  Offer     : Server(s) broadcast an offer with an available address.  
R  Request   : Client broadcasts a request for the chosen address (still src 0.0.0.0).  
A  ACK       : Server confirms the assignment and includes lease parameters.  
Note: Multiple DHCP servers may exist on the same segment, so broadcast is used.


D  Discover  ：客户端以 0.0.0.0 为源、广播探测 DHCP 服务器  
O  Offer     ：服务器广播提供可用地址的要约  
R  Request   ：客户端广播请求所选地址（仍以 0.0.0.0 为源）  
A  ACK       ：服务器确认分配，携带租约等参数  
注：同段可能有多台服务器，因此均用广播

```
**Windows Hint / Windows 设置提示**

- heck **“Obtain an IP address automatically”** and **“Obtain DNS server address automatically”** to use parameters are provided by the server.
- 勾选 **“自动获取 IP 地址”** 和 **“自动获取 DNS 服务器地址”**，即可使用 DHCP；参数由服务器下发。

 
---

### 5) Transport Layer in the TCP/IP Model — TCP vs UDP  
### TCP/IP 模型中的传输层：TCP 与 UDP

**IP Properties / IP 特性**  
- **Connectionless and unreliable** (no acknowledgments, no retransmissions); therefore **reliability must be provided by upper layers**.  
- **无连接、不可保证送达**（不确认、不重传）；因此**可靠性需由更上层提供**。
**TCP (Connection-Oriented) / TCP（面向连接）**  
- **Reliable transport** with **ordering, retransmission, flow control, and congestion control**. Suitable for applications that require guaranteed delivery.  
- **可靠传输**，具备**顺序控制、重传控制、流量控制、拥塞控制**；适合需要保证送达的应用。
**UDP (Connectionless) / UDP（无连接）**  
- **Best-effort**, low overhead, and good for real-time. Common for **IP voice/multicast/broadcast** and control protocols like **RIP, DHCP**.  
-**尽力而为**、开销小、实时性好；常用于**IP 语音/多播/广播**以及 **RIP、DHCP** 等协议。

---

### 6) Ports & Session Identification  
### 端口与会话识别

**5-tuple (Session Key) / 会话五元组**  
- A communication is uniquely identified by **Destination IP, Source IP, Destination Port, Source Port, Protocol (TCP/UDP)**.  
- 一次通信可由 **目的 IP、源 IP、目的端口、源端口、协议号（TCP/UDP）** 唯一标识。

**Common Service Ports (Examples) / 常见服务端口（示例）**  
- **HTTP `80`**, **POP3 `110`**, etc. (as in the slides).  
- **HTTP `80`**、**POP3 `110`** 等（与讲义示例一致）。

**Port Ranges (IANA) / 端口范围（IANA 管理）**  
- 
  - **Well-known**: `0–1023` — fixed purposes (privileged services).  
  - **Registered**: `1024–49151` — registered but reusable by vendors/apps.  
  - **Dynamic/Ephemeral**: `49152–65535` — **client** temporary ports, auto-assigned by OS.  
- 
  - **知名端口**：`0–1023` —— 固定用途（特权服务）。  
  - **注册端口**：`1024–49151` —— 由厂商/应用注册，但可复用。  
  - **动态/短暂端口**：`49152–65535` —— **客户端**临时端口，由操作系统自动分配。

**Notes / 说明**  
- Ephemeral ports are chosen to avoid collisions with well-known/registered ports, enabling multiple simultaneous client sessions using distinct 5-tuples.  
- 短暂端口会避开知名/注册端口，从而让同一主机可并发多会话（依靠不同的五元组区分）。

**端口分类 / Port Ranges（IANA 管理）**
  | 类型                    | 范围            | 说明                         |   |
| --------------------- | ------------- | -------------------------- | - |
| **Well-known**        | `0–1023`      | 固定用途、静态分配                  |   |
| **Registered**        | `1024–49151`  | 注册但可复用                     |   |
| **Dynamic/Ephemeral** | `49152–65535` | **客户端**临时端口，由 OS 动态分配，避免冲突 |   |
备注：**IANA**统一管理 IP、域名、端口等互联网编号资源。

---

## Key Points 

- **ARP**: On the same L2 segment, resolve the **destination host’s MAC**; on different segments, first resolve the **default gateway’s MAC**, then the router forwards; check cache with `arp -a`.  
  **ARP**：同段解析目的主机**MAC**；异段先解析默认**网关 MAC**，由路由器继续转发；可用 `arp -a` 查看缓存。
- **RARP**: Query a **RARP server** with a device’s **MAC** to obtain its **IP**; suited to diskless/embedded devices (requires preconfigured MAC↔IP mapping).  
  **RARP**：用设备 **MAC** 向 **RARP 服务器**获取 **IP**，适用于无盘/嵌入式场景（需预配 MAC↔IP 对）。
- **ICMP**: `ping` uses **Echo Request/Reply**; common types include **3 (Destination Unreachable) / 5 (Redirect) / 11 (Time Exceeded)**; ICMP messages are carried **inside the IP payload**, and **TTL expiry** triggers **Type 11**.  
  **ICMP**：`ping` 使用 **Echo 请求/应答**；常见类型有 **3/5/11**；消息位于**IP 数据部分**，**TTL** 耗尽触发 **Type 11**。
- **DHCP**: Automatically configures **IP/Mask/GW/DNS**; uses the **DORA** exchange and lease management; **broadcasts** are used when multiple servers may exist on the segment.  
  **DHCP**：自动配置 **IP/掩码/网关/DNS**；采用 **DORA** 交互与租约管理；同段多服务器时通过**广播**工作。
- **TCP vs UDP**: **TCP** is reliable (ordering, retransmission, flow & congestion control); **UDP** is lightweight and best-effort (good for real-time/multicast/broadcast).  
  **TCP vs UDP**：**TCP** 可靠（顺序、重传、流量与拥塞控制）；**UDP** 轻量、尽力而为（适合实时/多播/广播）。
- **Ports**: Sessions are identified by a **5-tuple**; port ranges follow IANA: **well-known / registered / dynamic (ephemeral)**.  
  **端口**：通过**五元组**区分会话；由**IANA**管理，分为 **well-known / registered / dynamic（短暂）**。


---

## ※※Supplementary Cheat Sheets | 速查单

### ICMP & DHCP Quick Reference
- [ICMP Types & Codes | ICMP 报文类型与代码速查](./figs/lecture11_icmp_types_codes.md)  
  *常见 ICMP 类型、不可达代码、TTL 超时与重定向*

- [DHCP DORA Flow | DHCP DORA 流程速查](./figs/lecture11_dhcp_dora_flow.md)  
  *DHCP Discover/Offer/Request/ACK 四步流程与租约管理*

<h2></h2>
  

[← Previous Lecture / 上一讲](./lecture10.md) · [Next Lecture / 下一讲 →](./lecture12.md)· [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md) 


[← Back to Course Directory / 返回课程目录](./README.md#toc)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 6: IPv4 — Internet Layer, Header, Fragmentation & Addressing  
# 信息网络概论 第6讲：IPv4（互联网层、首部、分片/重组、地址）

---

## ⚪ Lecture Overview 
- **Where IP sits**: In TCP/IP, IP resides at the **Internet layer**; in OSI, it is the **Network layer (L3)**. Its role is to deliver data from a **non-directly connected** source host to the **destination host**, traversing multiple subnets and routers.  
  **IP 所处位置**：在 TCP/IP 中，IP 位于**Internet 层**；在 OSI 中对应**第 3 层（网络层）**。其职责是将数据从**非直连**的源主机送达**目的主机**，跨越多个网段与路由器。  

- **Two meanings of “segment”**: (1) the **TCP sending unit** (“TCP segment”) at the transport layer; (2) a **network/host group split by routers** (a “network segment”).  
  **“Segment/段”的两种含义**：① 传输层 **TCP 的发送单元**（“TCP segment”）；② 被路由器划分的**网络/主机集合**（网络“段”）。  

- **Nature of IP**: **Abstracts away** lower-layer link differences (Ethernet/FDDI/ATM…); **connectionless**; **unreliable (best-effort)** — it does **not retransmit** losses; reliability is provided by **TCP**.  
  **IP 的性质**：对下层数据链路差异（Ethernet/FDDI/ATM…）进行**抽象**；**无连接**；**不可靠（best-effort）**，丢失不重传，可靠性交由 **TCP** 提供。  

- **IPv4 header layout & fields**: Version/IHL/TOS (→ DSCP, ECN)/Total Length/Identification/Flags/Fragment Offset/TTL/Protocol/Header Checksum/Source/Destination/Options/Padding/Data.  
  **IPv4 头部结构与字段**：Version/IHL/TOS(或 DSCP/ECN)/Total Length/Identification/Flags/Fragment Offset/TTL/Protocol/Header Checksum/源/目的/Options/Padding/Data。  

- **Field highlights**: IHL counts in **32-bit words**; Total Length is **16-bit** (max **65,535** bytes); fragmentation uses Identification/Flags/FO; **TTL** decrements per hop to 0 then discard; **Protocol** indicates upper layer (e.g., ICMP=1, TCP=6, UDP=17).  
  **字段要点**：IHL 以 **32 位**为单位；Total Length **16 位**（上限 **65,535 字节**）；分片用 Identification/Flags/FO；**TTL** 每过一跳减 1，至 0 丢弃；**Protocol** 指示上层（如 ICMP=1、TCP=6、UDP=17）。  

- **Three roles of IP**: (1) addressing; (2) forwarding to end host; (3) fragmentation & reassembly.  
  **IP 的三大职责**：① 地址分配；② 到终点主机的包转发；③ 分片与重组。  

- **IPv4 addresses**: 32-bit unsigned integers in dotted decimal; same format across different L2 (Ethernet/FDDI/ATM…); LANs can use **private** addresses, the Internet uses **global** ones; **L1/L2 devices** (repeaters/bridges/switches) **do not need IP**.  
  **IPv4 地址**：32 位无符号整数，点分十进制；不同链路（以太网/FDDI/ATM…）格式一致；LAN 可用**私有地址**，Internet 用**全球地址**；**L1/L2 设备**（中继器/桥/交换机）**不需要 IP**。  

- **On Windows**: `ipconfig /all | more`. Also include **binary↔decimal** conversion examples (e.g., 172.20.1.1).  
  **Windows 查询**：`ipconfig /all | more`。并给出**二进制↔十进制**换算示例（如 172.20.1.1）。  

---

## ⚪ Lecture Content 

### 1) IP in the Stack / 协议栈中的 IP
- **TCP/IP**: IP is defined at the **Internet layer**.  
  **TCP/IP**：IP 定义在 **Internet 层**。  
- **OSI**: corresponds to the **Network layer (L3)**.  
  **OSI**：对应 **网络层（L3）**。  
- **Role**: from a **non-directly connected** source host to a destination host, across one or more subnets; **L2** only handles **directly connected** devices.  
  **作用**：从**非直连**的源主机到目的主机，跨越一个或多个网段；**L2** 只负责**直连设备**之间的通信。  

---

### 2) Two Meanings of “Segment” / “Segment”的两种用法
- **Meaning 1 (Transport)**: the TCP sending unit (**TCP segment**).  
  **定义 1（传输层）**：TCP 发送的数据单位（**TCP segment**）。  
- **Meaning 2 (Topology)**: a group of hosts/networks **separated by routers** (a **network segment**).  
  **定义 2（网络拓扑）**：被路由器分隔的主机/网络设备组（一个“网段”）。 

---

### 3) Properties of IP  / IP 的设计性质
- **Hides link differences**: Ethernet, FDDI, ATM differences are **transparent** upward.  
  **屏蔽链路差异**：以太网、FDDI、ATM 等差异对上层**透明**，上层实现无需关心具体 L2。     
- **Connectionless**: no connection setup before sending.  
  **无连接**：发送前不建立连接。
- **Unreliable (Unreliable/Best-effort)**: **no retransmission** on loss; rely on **TCP** for reliability.  
  **不保证送达（Unreliable/Best-effort）**：即使未到达也**不重传**；可靠性交由上层 **TCP（面向连接）** 负责。    

---

### 4) IPv4 头部总览 / IPv4 Header Layout
```
32 bits per row → 4 bytes × 8 columns

| Version |  IHL  |     DSCP/ECN     |        Total Length        |
|        Identification       | Flags |   Fragment Offset         |
|   Time To Live  | Protocol |        Header Checksum        |
|                 Source Address (32)                         |
|              Destination Address (32)                       |
|  Options (if any)  |  Padding  |             Data ...        |
```

- **Version (4b)**: 4 for IPv4.  
  **Version（4 位）**：IPv4 填 4。  
- **IHL (4b)**: header length in **32-bit words**; typical is **5** (20 bytes) without options.  
  **IHL（4 位）**：头部长度，以 **32 位**为单位；无选项时典型值 **5**（=20 字节）。  
- **TOS/DSCP/ECN(TOS) (8b)**: QoS-related; often lightly used in practice.  
  **TOS/DSCP/ECN(TOS)（8 位）**：服务质量相关（现含 DSCP/ECN）；实际常较少使用。  
- **Total Length (16b)**: total packet length, max **65,535** bytes.  
  **Total Length（16 位）**：IP 包总长，上限 **65,535 字节**。

**Fragmentation / 分片相关**  
- **Identification (16b)**: same for all fragments of an original packet; typically increments per packet.  
  **Identification（16 位）**：同一原始包的所有分片相同；通常每发一包递增。  
- **Flags (3b)**: control fragmentation / “more fragments” info.  
  **Flags（3 位）**：分片控制与是否为最后一个分片等
- **Fragment Offset (13b)**: fragment position in 8-byte units (0–8192).  
  **Fragment Offset（13 位）**：分片在原包中的相对位置（以 8 字节为单位，范围 0～8192，对应 0～65,536 位范围）。  

**Forwarding & Upper-layer indicator / 转发与上层指示**  
- **TTL (8b)**: decremented by 1 per router; drop at 0.  
  **TTL（8 位）**：每过 1 台路由器减 1；减到 0 即丢弃。  
- **Protocol (8b)**: next-header protocol; e.g., **ICMP=1, TCP=6, UDP=17, OSPF=89**.  
  **Protocol（8 位）**：指出“IP 之后的下一层协议”，如 **ICMP=1、TCP=6、UDP=17、OSPF=89、Fibre Channel=133**。  
- **Header Checksum (16b)**: covers **only the IP header**.  
  **Header Checksum（16 位）**：**仅覆盖 IP 头部，用于头部差错检测**。
  
**Addresses / Options / Data**  
- **Source/Destination**: 32-bit each.  
  **源/目的地址**：各 32 位。  
- **Options**: rarely used; timestamps, security labels, etc.  
  **Options**：通常不使用；测试/调试时可放时间戳、安全标签等。  
- **Padding**: pad to a multiple of 32 bits.  
  **Padding**：为使头部长度成为 32bit 整数倍而填充的 0 
- **Data**: from the upper layer (its header + payload).  
  **Data**：上层的头与数据在 IP 看来均为“数据”。  

---
### 5) Three Roles of IP / IP 的三大职责
1. **Addressing**.  
   **地址分配**。  
2. **Delivery to the end host**.  
   **包到终点主机的递送**。  
3. **Fragmentation & reassembly**.  
   **IP 包的分片与重组**。

---
### 6) Devices & IP / 设备与 IP 地址
- **Need IP**: any **host/router** that communicates in TCP/IP has at least one IP address.  
  **需要 IP**：所有在 TCP/IP 中通信的节点**主机/路由器**至少一个 IP。  
- **Do NOT need IP**: **repeater hubs / bridges / switching hubs** — they operate at **L1/L2**.  
  **不需要 IP**：**中继器/桥/交换机**——仅在 **L1/L2** 转发信号/帧，不工作在 IP 层。  
- **Identifiers**: **MAC** is for **link-local** identity; **IP** is for **inter-network** identity.  
  **标识对比**：**MAC** 识别链路内设备；**IP** 识别跨链路/跨网主机。  
- **Uniqueness**: no duplicates on LAN/Internet; global vs private addressing.  
  **唯一性**：在 LAN/Internet 中均不可重复；Internet 使用全球地址，局域网可使用私有地址。  
- **L2-agnostic**: IP format is identical over Ethernet/FDDI/ATM, etc.  
  **与 L2 无关**：无论以太网/FDDI/ATM，IP 地址格式一致。  
 
---
### 7) Check IP on Windows / 在 Windows 上查看 IP
- Open **Command Prompt** and run:  
  打开 **命令提示符** 并执行：
```
ipconfig /all | more
```
- You can page through IPv4 address, gateway, DNS, physical address, etc.  
  可以分页查看本机的 IPv4 地址、网关、DNS、物理地址等。
 
---
### 8) IPv4 Address & Notation / IPv4 地址与表示法
- A **32-bit unsigned integer** → theoretical space of **2^32 ≈ 4.29×10^9** addresses.  
  **32 位无符号（非负）整数** → 理论可分配 **2^32 ≈ 4.29×10^9（4,294,967,296）（约 43 亿）** 个地址。  
- **Dotted decimal** is used for readability (each octet 0–255).  
   二进制不便阅读，故采用**点分十进制**（每 8 位转为 0–255 的十进制），形如：  
```
10101100.00010100.00000001.00000001  →  172.20.1.1
```
- Each chunk is an **octet (8 bits)**.  
  每一段是一个 **octet（8 位）**。  
 
---
### 9) Binary ↔ Decimal Conversions / 二进制 ↔ 十进制换算方法
#### (A) Binary → Decimal (expand by weights)  
#### （A）二进制 → 十进制（按位权展开）
```
Example / 示例： (110101)₂
= 1×2^0 + 0×2^1 + 1×2^2 + 0×2^3 + 1×2^4 + 1×2^5
= 1 + 0 + 4 + 0 + 16 + 32
= (53)₁₀
```
#### (B) Decimal → Binary (divide by 2; read remainders bottom-up)  
#### （B）十进制 → 二进制（连除取余，余数自下而上读）
```
Example / 示例： (172)₁₀ → binary / 二进制
172 ÷ 2 = 86 … 0
 86 ÷ 2 = 43 … 0
 43 ÷ 2 = 21 … 1
 21 ÷ 2 = 10 … 1
 10 ÷ 2 =  5 … 0
  5 ÷ 2 =  2 … 1
  2 ÷ 2 =  1 … 0
  1 ÷ 2 =  0 … 1   ← stop / 终止
Read remainders bottom-up → 10101100
自下而上读余数 → 10101100

Example / 示例： (20)₁₀ → binary / 二进制
20 ÷ 2 = 10 … 0
10 ÷ 2 =  5 … 0
 5 ÷ 2 =  2 … 1
 2 ÷ 2 =  1 … 0
 1 ÷ 2 =  0 … 1
→ 10100; pad left to 8 bits for an octet → 00010100
→ 10100；若需 8 位 octet，左侧补 0 → 00010100
```
#### (C) Assemble into dotted decimal  
#### （C）组装成点分十进制
```
10101100.00010100.00000001.00000001
→ 172.20.1.1
```

---

## Key Points / 关键要点
- **IP layer position**: OSI **L3** / TCP-IP **Internet layer** → cross-subnet delivery; L2 handles only directly connected devices.  
  **IP 的层级定位**：OSI **第 3 层** / TCP-IP **Internet 层** → 负责跨网段递送；L2 仅处理直连通信。  
- **Connectionless & best-effort**: no connection, no retransmission; rely on **TCP** for reliability.  
  **无连接与尽力而为**：不建连、不重传；可靠性交由 **TCP**。  
- **Header essentials**: **IHL** in 32-bit words; **Total Length ≤ 65,535**; **Identification/Flags/FO** for fragmentation; **TTL** decrements hop-by-hop; **Protocol** indicates the next header; **Checksum** covers header only.  
  **首部要点**：**IHL** 以 32 位计；**总长 ≤ 65,535**；**Identification/Flags/FO** 控制分片；**TTL** 逐跳递减；**Protocol** 指示上层；**Checksum** 仅校验头部。  
- **Three IP roles**: **addressing**, **end-to-end forwarding**, **fragmentation & reassembly**; **L1/L2 devices** do **not** need IP.  
  **三大职责**：**地址分配**、**端到端转发**、**分片与重组**；**L1/L2 设备**无需 IP。  
- **IPv4 address**: 32-bit dotted decimal; know **binary↔decimal** conversions; pad octets on the left to 8 bits when needed.  
  **IPv4 地址**：32 位点分十进制；熟练掌握**二进制↔十进制**换算；不足 8 位时左侧补 0。  



<h2></h2>

[← Previous Lecture / 上一章](./lecture05.md) ·[Next Lecture / 下一章](./lecture07.md) ·[Back to Course Directory / 返回课程目录](./README.md#toc) ·[Notes Home / 笔记首页](../) ·[Repository Home / 仓库首页](../../README.md)


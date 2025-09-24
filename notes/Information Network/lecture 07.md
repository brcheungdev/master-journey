#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 7: IPv4 Addressing — Classes, Private Ranges, Broadcast, Subnet Mask & CIDR  
# 情報ネットワーク概論 第7回：IPv4アドレス（クラス・プライベート・ブロードキャスト・サブネットマスク・CIDR）

---

## ⚪ Lecture Overview 
- IPv4 address structure: **network part + host part**；routers forward by **network part** with routing tables  
  IPv4 地址结构：**网络部 + 主机部**；路由器依据**网络部**查路由表转发  
- **Classful addressing (A/B/C/D)** & their bit patterns, usable ranges, special/reserved addresses  
  **有类地址**（A/B/C/D）的比特模式、可用范围与保留地址  
- **Broadcast / Unicast / Loopback** semantics  
  **广播 / 单播 / 回环** 的意义与用法  
- **Private address ranges** (A/B/C) and usable-host counts (= total − network − broadcast)  
  **私有地址段**（A/B/C）与可分配主机数（总数减网络/广播）  
- **Subnet mask** concept, how routers compute **network address = IP AND mask**, worked examples  
  **子网掩码**；路由器通过 **IP 与掩码按位与** 求网络地址；完整示例  
- **CIDR** notation (`/prefix`), writing rules, aggregation of multiple class-C blocks  
  **CIDR** 记法与书写规则，聚合多个 C 类网段

---

## ⚪ Lecture Content 
### 1) IPv4 Address: Network Part & Host Part / IPv4 地址：网络部与主机部
- An IPv4 address consists of **Network part** (identifies the subnet/segment) and **Host part** (unique within the subnet).  
  IPv4 由**网络部**（标识网段/子网）与**主机部**（在子网内唯一）组成。  
- Router looks at the **network part** of the destination address, compares with its **routing table**, and forwards to the proper next hop.  
  路由器检查目的地址的**网络部**并与**路由表**比对，转发到相应下一跳。

---

### 2) Classful Addressing (A/B/C/D) / 有类地址
> 传统 IPv4 将网络部长度固定化（A/B/C 类），本节给出每类的**首比特标志、数值范围、可分配主机数**与**保留地址**。

#### Class A
- **Leading bits**: `0`（1 bit） → Network = **8 bits**, Host = **24 bits**  
  首比特为 `0`；网络部 8 位，主机部 24 位  
- **Numerical range (theoretical)**: `0.0.0.0` – `127.255.255.255`；**global-usable** examples exclude reserved blocks; slides list global ranges as `1.0.0.0–9.255.255.255` and `11.0.0.0–126.255.255.255`.  
  计算范围 `0.0.0.0`–`127.255.255.255`；讲义中的全球可用段示例排除了保留块  
- **Usable host count**: `2^24 − 2 = 16,777,214`（减去全 0 网络地址与全 1 广播地址）  
  可分配主机数 `2^24 − 2`  
- **Special**: `127.0.0.0/8` 为 loopback（回环）保留。 

#### Class B
- **Leading bits**: `10`（2 bits） → Network = **16 bits**, Host = **16 bits**  
- **Range (theoretical)**: `128.0.0.0` – `191.255.255.255`  
- **Usable hosts per network**: `2^16 − 2 = 65,534`  
- **Global range**（slides示例）: `128.0.0.0–172.15.255.255`, `172.32.0.0–191.255.255.255`（中间空缺用于保留/私有）。
#### Class C
- **Leading bits**: `110`（3 bits） → Network = **24 bits**, Host = **8 bits**  
- **Range (theoretical)**: `192.0.0.0` – `223.255.255.255`  
- **Usable hosts**: `2^8 − 2 = 254`  
- **Global range**（slides示例）: `192.0.0.0–192.167.255.255` 与 `192.169.0.0–223.255.255.255`（中间空缺用于保留/私有）。
#### Class D (Multicast)
- **Leading bits**: `1110`（4 bits） → **Used for multicast**, **no host part**  
  首四比特 `1110`；用于 **多播**，**无主机部**  
- **Range**: `224.0.0.0` – `239.255.255.255`；host 不按传统方式分配。

---

### 3) Broadcast, Unicast & Loopback / 广播、单播与回环
- **Broadcast address**: host part **all 1s**; reserved—**cannot** be assigned to a host; used to send to **all hosts in the same segment**.  
  **广播地址**：主机部全 1；系统保留，不能分配；向**同一网段的所有主机**发送。  
  ```
  Example: Class A broadcast  0.255.255.255
           Class A top        127.255.255.255
  ```
- **Unicast address**: destination is a single host (normal case).
**单播地址**：指向**单一主机**（常见场景）。
- **Loopback**:`127.0.0.1` reserved; packets loop back to self.
**回环地址**：`127.0.0.1`；发往本机自身。

---
### 4) Multicast (Class D) / 多播（D 类）
- Send to all hosts in a subscribed group; routers can forward across segments; commonly used by multimedia applications (voice/video one-to-many).
发送给预先加入组的主机；可跨路由；常被多媒体应用用于一对多。
- Some multicast addresses are well-known（特定用途保留）。

---
### 5) Private Address Ranges / 私有地址段
 私有地址只在 LAN/组织内部使用，Internet 不可路由（需 NAT）。
- **Class A**:`10.0.0.0 – 10.255.255.255`（`10.0.0.0/8`）
可分配主机数：`2^24 − 2 = 16,777,214`
- **Class B**:`172.16.0.0 – 172.31.255.255`（`172.16.0.0/12`）
可分配主机数：`2^16 − 2 = 65,534`
- **Class C**:`192.168.0.0 – 192.168.255.255`（`192.168.0.0/16`）
可分配主机数：`2^8 − 2 = 254`
（上述主机数均为**每个网络**的可用数，扣除了**网络地址**与**广播地址**。）

---
### 6) Subnet Mask — Concept & Notation / 子网掩码：概念与记法
- Motivation: Class C too small, Class B too large for many orgs → need finer control of network/host split.
动机：很多组织在 C 与 B 之间缺乏合适规模 → 需要灵活划分网络/主机位数。
- Subnet: take some host bits and relabel them as network bits (= subnet ID)。
子网：把原主机位的一部分划作网络位（子网号）。
- Subnet mask is a 32-bit integer; in binary, network bits are 1, host bits are 0。
掩码是 32 位整数；二进制中网络部用 1、主机部用 0 表示。
- IP is then written as IP + Mask (or CIDR /prefix；见下一节)。

---
### 7) Worked Example with Subnet Mask / 子网掩码完整示例
- **Given**:
IP address `172.20.100.52`
Subnet mask `255.255.254.0`
- **Ask**: network address? broadcast address? host range & count?

**Binary view**（二进制视图）
```
IP (172.20.100.52)
10101100.00010100.01100100.00110100

Mask (255.255.254.0)
11111111.11111111.11111110.00000000
```
Router computes network by bitwise AND（路由器通过按位与运算计算网络）
```
Network = IP AND Mask
= 10101100.00010100.01100100.00110100
  AND 11111111.11111111.11111110.00000000
= 10101100.00010100.01100100.00000000  → 172.20.100.0

```
Broadcast: host bits all 1
```
Broadcast = 10101100.00010100.01100101.11111111 → 172.20.101.255
```
Usable hosts
```
Host bits = 32 − prefix = 32 − 23 = 9 bits
Usable = 2^9 − 2 = 512 − 2 = 510
Range = 172.20.100.1  …  172.20.101.254

```
（与讲义示例一致：网络`172.20.100.0`，广播`172.20.101.255`，主机 510 台。）

---
### 8) CIDR (Classless Inter-Domain Routing) / 无类域间路由
-** Why**: Class-based assignment wastes space; many orgs wanted a whole Class B though they needed “a bit more than **C**”。
**原因**：有类地址粒度粗 → 浪费；很多机构只比 C 稍大却要 B 类。
- **What**: No classes; explicitly write prefix length`/n`(network bits from the left).
**做法：取消类**；用`/前缀长度` 明示网络位数。
- **Notation rules**
  - `A.B.C.D/n` → first n bits are network; remaining are **host**。
  - The trailing`.0 `in a network address can be omitted in the last octet only（如`172.20/16` 代表 `172.20.0.0/16`）。
  - **Aggregation** is possible: combine contiguous blocks that share a common prefix.
CIDR Examples（from slides）
-`172.20.100.52/26`: first 26 bits are network → host bits = 6。
对应网络`172.20.100.0/26`，广播`172.20.100.63/26`。
- **Aggregate 2 class-C**:`203.183.224.0/23`
```
Hosts usable = 2^(32−23) − 2 = 510
Range: 203.183.224.1  …  203.183.225.254
```
- **Aggregate 8 class-C**:`202.244.160.0/21`
```
Hosts usable = 2^(32−21) − 2 = 2046
Range: 202.244.160.1  …  202.244.167.254
```
（与讲义二进制图一一对应）

--- 
## Key Points
- IPv4 地址 = 网络部 + 主机部；路由器按网络部查表并转发。
- **Class A/B/C/D**：识别首比特，掌握各类数值范围与可分配主机数。
- **广播地址**（主机位全 1）与 **网络地址**（主机位全 0）**不可分配**；`127.0.0.1` 为 loopback。
- **私有地址**：`10/8`, `172.16/12`, `192.168/16`；Internet 不路由，常配合** NAT **使用。
- **子网掩码**把“主机位的一部分”变为“网络位”；路由器用** IP AND Mask **求网络地址。
- **CIDR** 用`/prefix `显式指定网络位数，可聚合连续网段（/23、/21 等），比 classful 更灵活、节省地址空间。

---

## ※※ Supplementary Cheat Sheets | 速查单

###  IPv4 Subnet & CIDR Quick Reference
- [Subnet Mask Calculation Steps | 子网掩码按位与计算步骤](./figs/lecture07_ipv4_subnet_calc.md)  
  *如何通过 IP 和掩码求网络地址、广播地址、主机范围*

- [CIDR Prefix vs Host Count Table | CIDR 前缀与主机数对照表](./figs/lecture07_ipv4_cidr_table.md)  
  *不同前缀长度对应的可用主机数、掩码与示例网络*




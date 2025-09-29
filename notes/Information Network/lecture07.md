[← Back to Course Directory / 返回课程目录](./README.md#toc)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 7: IPv4 Addressing — Classes, Private Ranges, Broadcast, Subnet Mask & CIDR  
# IPv4 地址编址：类别、私有地址范围、广播、子网掩码与 CIDR

---

## ⚪ Lecture Overview 
- IPv4 address structure: **network part + host part**; routers forward by **network part** with routing tables  
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
> Legacy IPv4 fixed the network length by class (A/B/C). Below list shows **leading-bit flags, numeric ranges, usable hosts** and **reserved blocks**.  
> 传统 IPv4 将网络部长度固定化（A/B/C 类）。下表概述各类的**首比特、数值范围、可用主机数**与**保留地址**。

#### Class A
- **Leading bits**: `0` (1 bit) → Network **8 bits**, Host **24 bits**  
  首比特为 `0`；网络部 8 位，主机部 24 位  
- **Numerical range (theoretical)**: `0.0.0.0` – `127.255.255.255`; global-usable examples exclude reserved blocks.  
  计算范围 `0.0.0.0`–`127.255.255.255`；全球可用段需排除保留块  
- **Usable host count**: `2^24 − 2 = 16,777,214`（exclude all-0 network & all-1 broadcast）  
  可分配主机数 `2^24 − 2`（扣除全 0 网络与全 1 广播）  
- **Special**: `127.0.0.0/8` is reserved for loopback.  
  特殊：`127.0.0.0/8` 为回环保留。

#### Class B
- **Leading bits**: `10` (2 bits) → Network **16 bits**, Host **16 bits**  
  首两位 `10`；网络部 16 位，主机部 16 位  
- **Range (theoretical)**: `128.0.0.0` – `191.255.255.255`  
  范围 `128.0.0.0`–`191.255.255.255`  
- **Usable hosts per network**: `2^16 − 2 = 65,534`  
  每网可分配 `2^16 − 2 = 65,534` 台主机
<details>
<summary><strong>Note on “Global ranges” for Class B / 关于 Class B “全球可用范围”的说明</strong></summary>

- In some slides/books, the **globally usable Class B space** is shown as two chunks because certain blocks inside 128.0.0.0/3 are **reserved or special-use**.  
  一些讲义/教材把 **可在公网使用的 B 类地址** 写成两段，是因为 128.0.0.0/3 中有若干网段被**保留或用于特殊用途**。

- Typical exclusions include:  
  常见的排除项包括：  
  - `172.16.0.0/12` — **private** (RFC1918), not routed on the public Internet.  
    `172.16.0.0/12` — **私有地址**（RFC1918），**公网不可路由**。  
  - `169.254.0.0/16` — **link-local (APIPA)**; autoconfig addresses not intended to be routed.  
    `169.254.0.0/16` — **链路本地 (APIPA)**；自动配置地址，不用于路由。  
  - Other small **special-use** ranges may be carved out by standards bodies over time.  
    还有一些零散的 **特殊用途** 网段可能被标准机构保留。

- That’s why you might see Class B “global ranges” written as:  
  因此，你可能会在讲义中看到把 B 类“全球可用范围”写成两段：  
  - `128.0.0.0 – 172.15.255.255`  
    `128.0.0.0 – 172.15.255.255`  
  - `172.32.0.0 – 191.255.255.255`  
    `172.32.0.0 – 191.255.255.255`

- Practical takeaway: **use CIDR and current allocations**—real-world routability depends on **today’s registry data and your ISP’s routing policies**, not just the historic classful ranges.  
  实务要点：**以 CIDR 与最新分配为准**——实际能否在公网路由取决于**当前注册信息与运营商路由策略**，而不仅是传统 B 类范围。

</details>


#### Class C
- **Leading bits**: `110` (3 bits) → Network **24 bits**, Host **8 bits**  
  首三位 `110`；网络部 24 位，主机部 8 位  
- **Range (theoretical)**: `192.0.0.0` – `223.255.255.255`  
  范围 `192.0.0.0`–`223.255.255.255`  
- **Usable hosts**: `2^8 − 2 = 254`  
  可分配主机数 `2^8 − 2 = 254`
<details>
<summary><strong>Note on “Global ranges” for Class C / 关于 Class C “全球可用范围”的说明</strong></summary>

- In many slides/books, the **globally usable Class C space** is shown as two chunks because some blocks inside 192.0.0.0/8 are **reserved or private**.  
  许多讲义/教材把 **可在公网使用的 C 类地址** 写成两段，是因为 192.0.0.0/8 里有一些网段被**保留或划为私有**。

- Typical exclusions include:  
  常见的排除项包括：  
  - `192.168.0.0/16` — **private** (RFC1918), not routed on the public Internet.  
    `192.168.0.0/16` — **私有地址**（RFC1918），**公网不可路由**。  
  - `192.0.2.0/24` (and `198.51.100.0/24`, `203.0.113.0/24`) — **TEST-NET** for documentation/examples.  
    `192.0.2.0/24`（以及 `198.51.100.0/24`, `203.0.113.0/24`）— **测试/示例**专用。  
  - Other small **special-use** ranges may also be carved out by standards.  
    还有一些零散的 **特殊用途** 网段按标准保留。

- That’s why you might see Class C “global ranges” written as:  
  因此，你可能会在讲义中看到把 C 类“全球可用范围”写成两段：  
  - `192.0.0.0 – 192.167.255.255`  
    `192.0.0.0 – 192.167.255.255`  
  - `192.169.0.0 – 223.255.255.255`  
    `192.169.0.0 – 223.255.255.255`

- Practical takeaway: **always check with CIDR**—real-world routability depends on **current allocations and your ISP’s routing policies**, not just the classful ranges.  
  实务要点：**以 CIDR 为准**——实际能否在公网路由取决于**当前分配与运营商的路由策略**，而不只看传统 C 类范围。

</details>

- 
#### Class D (Multicast) / D 类（多播）
- **Leading bits**: `1110` → used for **multicast**; **no host part**.  
  首四比特 `1110`；用于**多播**，**无主机部**  
- **Range**: `224.0.0.0` – `239.255.255.255`  
  范围 `224.0.0.0`–`239.255.255.255`；host 不按传统方式分配。
---

### 3) Broadcast, Unicast & Loopback / 广播、单播与回环
- **Broadcast address**: host part **all 1s**; reserved—**cannot** be assigned; sends to **all hosts in the same segment**.  
  **广播地址**：主机部全 1；系统保留不可分配；向**同网段所有主机**发送。  
  ```
  Example: Class A broadcast  0.255.255.255
           Class A top        127.255.255.255
  ```
- **Unicast address**: destination is a **single** host (normal case).  
  **单播地址**：目的为**单一主机**（常见场景）。  
- **Loopback**: `127.0.0.1` reserved; packets loop back to self.  
  **回环地址**：`127.0.0.1`；发往本机自身。

---
### 4) Multicast Semantics & Usage (Class D) / 多播的语义与用法（D 类）
- Send to all hosts in a subscribed group; routers can forward across segments; common in one-to-many media (voice/video).  
  面向加入组的主机；路由器可跨网段转发；常见于一对多的音视频应用。  

- Well-known/reserved scopes (quick notes):  
  常见保留/约定作用域（速记）：  
  - `224.0.0.0/24` link-local（不跨路由）  
    链路本地（不跨越路由）。  
  - `239.0.0.0/8` administratively scoped（私有多播域）  
    管理域（组织内私有多播）。  

---
### 5) Private Address Ranges / 私有地址段
Private ranges are used inside LANs and are **not routed on the Internet** (NAT required).  
私有地址用于局域网，**不会在 Internet 上被路由**（通常需要 NAT 才能访问公网）。

- **Class A**: `10.0.0.0 – 10.255.255.255` (`10.0.0.0/8`)  
  **A 类**：`10.0.0.0 – 10.255.255.255`（`10.0.0.0/8`）  
  Usable hosts per network: `2^24 − 2 = 16,777,214`.  
  每个网络的可用主机数：`2^24 − 2 = 16,777,214`。

- **Class B**: `172.16.0.0 – 172.31.255.255` (`172.16.0.0/12`)  
  **B 类**：`172.16.0.0 – 172.31.255.255`（`172.16.0.0/12`）  
  Usable hosts per network: `2^16 − 2 = 65,534`.  
  每个网络的可用主机数：`2^16 − 2 = 65,534`。

- **Class C**: `192.168.0.0 – 192.168.255.255` (`192.168.0.0/16`)  
  **C 类**：`192.168.0.0 – 192.168.255.255`（`192.168.0.0/16`）  
  Usable hosts per network: `2^8 − 2 = 254`.  
  每个网络的可用主机数：`2^8 − 2 = 254`。

> The usable-host counts above are **per subnet**, excluding the **network address** (all host bits 0) and the **broadcast address** (all host bits 1).  
> 上述可用主机数均为**每个子网**的数量，已扣除**网络地址**（主机位全 0）与**广播地址**（主机位全 1）。

---
### 6) Subnet Mask — Concept & Notation / 子网掩码：概念与记法
- **Motivation**: Class C is too small, Class B too large for many orgs → need finer control.  
  **动机**：许多组织规模在 C 与 B 之间缺乏合适规模 → 需要灵活划分网络/主机位数。  
- **Subnet**: take some **host bits** and relabel them as **network bits** (= subnet ID).  
  **子网**：把原**主机位**的一部分划作**网络位**（子网号）。  
- **Subnet mask** is 32-bit; **1s** for network bits, **0s** for host bits.  
  **掩码**是 32 位整数；二进制中网络位用 **1**，主机位用 **0**表示。  
- IP is written as **IP + Mask** (or **CIDR /prefix**).  
  写作 **IP + 掩码**（或 **CIDR /前缀**）。

---
### 7) Worked Example with Subnet Mask / 子网掩码完整示例
- **Given / 已知**:
IP address `172.20.100.52`
Subnet mask `255.255.254.0`
- **Ask / 求**: network address? broadcast address? host range & count? / 网络地址、广播地址、主机范围与数量

**Binary view / 二进制视图**
```
IP (172.20.100.52)
10101100.00010100.01100100.00110100

Mask (255.255.254.0)
11111111.11111111.11111110.00000000
```
Router computes the network by bitwise AND（路由器通过按位与运算计算网络）
**Network = IP AND Mask**
```
Network = IP AND Mask
= 10101100.00010100.01100100.00110100
  AND 11111111.11111111.11111110.00000000
= 10101100.00010100.01100100.00000000  → 172.20.100.0

```
**Broadcast**: host bits all 1 → `172.20.101.255`  
**广播**：主机位全 1 → `172.20.101.255`
```
Broadcast = 10101100.00010100.01100101.11111111 → 172.20.101.255
```
**Usable hosts / 可用主机数**
```
Host bits = 32 − prefix = 32 − 23 = 9 bits
Usable = 2^9 − 2 = 512 − 2 = 510
Range = 172.20.100.1  …  172.20.101.254

```
（网络`172.20.100.0`，广播`172.20.101.255`，主机 510 台。）

---
### 8) CIDR (Classless Inter-Domain Routing) / 无类域间路由
- **Why**: Class-based addressing wastes space; many orgs needed “a bit more than Class C” but far less than Class B.  
  **原因**：有类地址粒度过粗，容易浪费；许多机构只比 C 类稍大，却远小于 B 类的规模需求。  

- **What**: Drop classes; write **`A.B.C.D/n`** — the first `n` bits are the **network** part, the rest are **host** bits.  
  **做法**：取消类别；使用 **`A.B.C.D/n`** 表示**前 n 位为网络部**、其余为**主机部**。  

- **Notation rules**  
  **记法规则**  
  1) `A.B.C.D/n` → first `n` bits are network; remaining are host.  
     `A.B.C.D/n` 表示**前 n 位**为网络部，剩余为主机部。  
  2) A pure network address may omit a trailing “`.0`” in the **last octet only** (e.g., `172.20/16` ≡ `172.20.0.0/16`).  
     纯网络地址在**最后一个八位段**可以省略结尾的 “`.0`”（如 `172.20/16` 等价于 `172.20.0.0/16`）。  
  3) **Aggregation**: contiguous blocks sharing a common prefix can be summarized into a single route.  
     **聚合**：将具有共同前缀的相邻网段汇总为一条汇总路由。  

- **Examples (from slides)**  
  **示例（对应讲义）**

  - `172.20.100.52/26` → network bits = 26, host bits = 6  
    `172.20.100.52/26` → 网络位 26，主机位 6  
    ```
    Network:   172.20.100.0/26
    Broadcast: 172.20.100.63
    ```
    ```
    网络地址：172.20.100.0/26
    广播地址：172.20.100.63
    ```

  - **Aggregate 2 Class-C blocks** → `203.183.224.0/23`  
    **聚合两个 C 类网段** → `203.183.224.0/23`
    ```
    Usable hosts = 2^(32−23) − 2 = 510
    Range: 203.183.224.1  …  203.183.225.254
    ```
    ```
    可用主机数 = 2^(32−23) − 2 = 510
    主机范围：203.183.224.1  …  203.183.225.254
    ```

  - **Aggregate 8 Class-C blocks** → `202.244.160.0/21`  
    **聚合八个 C 类网段** → `202.244.160.0/21`
    ```
    Usable hosts = 2^(32−21) − 2 = 2046
    Range: 202.244.160.1  …  202.244.167.254
    ```
    ```
    可用主机数 = 2^(32−21) − 2 = 2046
    主机范围：202.244.160.1  …  202.244.167.254
    ```


--- 
## Key Points
- IPv4 address = **network + host**; routers forward by the **network part**.  
  IPv4 地址 = **网络部 + 主机部**；路由器按**网络部**查表并转发。  
- **Class A/B/C/D**: know leading bits, numeric ranges, and usable hosts.  
  **A/B/C/D 类**：识别首比特、，掌握各类数值范围与可分配主机数。  
- **Broadcast** (all-1 host) & **network** (all-0 host) are **not assignable**; `127.0.0.1` is loopback.  
  **广播地址**（主机全 1）与**网络地址**（主机位全 0）**不可分配**；`127.0.0.1` 为回环。  
- **Private ranges**: `10/8`, `172.16/12`, `192.168/16`; typically used with **NAT**.  
  **私有地址**：`10/8`、`172.16/12`、`192.168/16` 不路由；常与 **NAT** 搭配使用。  
- **Subnet mask** converts some host bits to network bits; routers compute **network = IP AND Mask**.  
  **子网掩码**将部分主机位变为网络位；路由器以 **IP 与 掩码**求网络地址。  
- **CIDR** uses `/prefix` and supports **aggregation**, saving address space.  
  **CIDR** 用 `/前缀` 显式指定网络位数，可**聚合**连续网段（/23、/21 等），比 classful 更灵活、节省地址空间。

---

## ※※ Supplementary Cheat Sheets | 速查单

###  IPv4 Subnet & CIDR Quick Reference
- [Subnet Mask Calculation Steps | 子网掩码按位与计算步骤](./figs/lecture07_ipv4_subnet_calc.md)  
  *如何通过 IP 和掩码求网络地址、广播地址、主机范围*

- [CIDR Prefix vs Host Count Table | CIDR 前缀与主机数对照表](./figs/lecture07_ipv4_cidr_table.md)  
  *不同前缀长度对应的可用主机数、掩码与示例网络*


<h2></h2>

[← Previous Lecture / 上一章](./lecture06.md) · [Next Lecture / 下一章](./lecture08.md) · [Back to Course Directory / 返回课程目录](./README.md#toc)


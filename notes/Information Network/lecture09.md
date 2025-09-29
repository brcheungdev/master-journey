[← Back to Course README / 返回课程目录](./README.md#toc)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 9: STP (Spanning Tree), Routing Basics, Static/Dynamic Routing, RIP & Count-to-Infinity  
# 生成树（STP）／路由基础／静态与动态路由／RIP 与无穷计数

---

## ⚪ Lecture Overview / 课程概览
- **STP (Spanning Tree Protocol)**: blocks redundant L2 links to avoid **broadcast storms**; uses **root bridge / port roles / path cost**; can **fail over** on link/port failures (classic STP converges in tens of seconds; **RSTP** improves to a few seconds).  
  **STP（生成树协议）**：为避免二层环路导致的**广播风暴**，通过**根桥/端口角色/路径代价**自动屏蔽冗余链路；链路/端口故障时可**自动切换**（传统 STP 收敛需数十秒；**RSTP** 将其降到数秒级）。  
- **Routing basics**: routers forward hop-by-hop using **routing tables** (destination network → next hop).  
  **路由基础**：路由器依据**路由表**（目的网络 → 下一跳）逐跳转发；路由表需保持**正确信息**。  
- **Static vs Dynamic routing**: static = manual config; dynamic = **protocols** exchange/learn routes periodically.  
  **静态路由 vs 动态路由**：静态=手工配置，变更/故障需人工维护；动态=路由协议**自动**学习/更新（定期交换信息）。  
- **Internet & routing protocols**: the Internet is a set of **AS**es; **IGP** (RIP/RIP2/OSPF/IS-IS) inside an AS; **BGP** between ASes.  
  **互联网与路由协议**：互联网可视为由多个 **AS（Autonomous System，自治系统）** 的集合；**IGP**（RIP/RIP2/OSPF/IS-IS）用于 AS 内，**EGP/BGP** 用于 AS 间。  
- **RIP**: distance-vector IGP with **hop-count metric**, **30 s** updates, **max hop = 16** (≥16 means unreachable); timers for timeout/garbage-collection; **count-to-infinity** issue and mitigations.  
  **RIP**：距离向量型 IGP，**度量=跳数**，**30s 周期更新**、**最大跳数=16（≥16 视为不可达）**、超时/垃圾回收定时器；**无穷计数（Count-to-Infinity）**问题与其抑制。   

---

## ⚪ Lecture Content 

### 1) Spanning Tree Protocol (STP) / 生成树协议：避免二层环路

**Problem & Goal / 问题与目标**  
- **Broadcast storm**: when a **Layer-2 loop** exists, broadcast frames / unknown unicasts can **circulate indefinitely**, congesting links and overloading devices.  
  **广播风暴**：交换网络中存在**二层环路**时，广播帧/未知单播会**无限循环**，造成链路拥塞与设备过载。  
- **What STP does**: automatically computes a **loop-free topology (spanning tree)**, sets redundant ports to **blocking**, and keeps only forwarding paths to **prevent storms**.  
  **STP 作用**：自动计算**无环拓扑（生成树）**，将冗余端口置为**阻塞**，仅保留可转发路径，从而**防止广播风暴**。

**Core Elements / 核心要素**  
- **Bridge ID**: priority + MAC; the **smallest** becomes the **Root Bridge**.  
  **桥 ID**：由优先级 + MAC 组成；**最小**者成为**根桥（Root Bridge）**。  
- **Path Cost**: cost based on link speed; per-switch, choose the path with the **minimum total cost** toward the root.  
  **路径代价**：依据链路速率确定；从每台交换机到根桥选择**总代价最小**的路径。  
- **Port roles / 端口角色**  
  - **Root Port**: on each non-root bridge, the port **toward the root** on the best-cost path.  
    **根端口**：每台非根桥上**朝向根桥的最优路径**端口。  
  - **Designated Port**: on each segment, the port **designated to forward** for that segment (wins by lower cost / Bridge ID).  
    **指定端口**：在每段链路上**负责该段转发**的端口（按代价/Bridge ID 比较胜出）。  
  - **Blocking / Disabled Port**: ports that are neither Root nor Designated are **disabled for forwarding** to **break loops**.  
    **阻塞/无效端口**：既非根端口也非指定端口者，被**禁用转发**，以**打破环路**。

**Failure & Convergence / 故障与收敛**  
- On **link or port failure**, STP **recomputes** the tree and can **activate** previously blocked ports (change roles) to restore connectivity.  
  当**链路断开/端口故障**时，STP 会**重新计算**生成树，把原阻塞端口**切换**为 Root/Designated 等角色（改变角色）以恢复连通。  
- **Classic STP** convergence can take **tens of seconds**; **RSTP (Rapid STP)** reduces this to **a few seconds**.  
  **传统 STP** 收敛需**数十秒**；为改进此问题，出现了**RSTP（快速生成树）** 等快速收敛标准，可降至**数秒**。

<details>
<summary>补充说明 / Additional notes</summary>

- **BPDU**（Bridge Protocol Data Unit）承载根桥信息、路径代价与端口角色，用于计算/维护生成树。  
  **BPDUs** carry root information, path costs, and port role data to build/maintain the tree.

- **典型定时器 / Timers**：Hello（默认 2 s）、Max Age（默认 20 s）、Forward Delay（默认 15 s）。  
  **Typical timers**: Hello (2 s), Max Age (20 s), Forward Delay (15 s).

- **RSTP 端口状态 / RSTP states**：Discarding → Learning → Forwarding；较 802.1D 大幅加速。  
  **RSTP states**: Discarding → Learning → Forwarding; faster than 802.1D STP.

</details>

---

### 2) Routing Basics: Routing Table & Hop-by-hop Forwarding / 路由基础：路由表与逐跳转发

- The Internet is formed by **interconnecting many networks with routers**.  
  互联网由多个网络通过**路由器**互联而成。  
- A router **consults its routing table** (Destination Network → Next Hop) to forward packets to the **correct destination**; entries must be **accurate**.  
  路由器需要**查路由表**（Destination Network → Next Hop）以转发到**正确的目的地**；表项必须**准确**。  
- Forwarding workflow: inspect the packet’s **destination IP** → compare against the **routing table** → decide the **next-hop router or directly connected host** → **hop-by-hop** forwarding (a **bucket-brigade** style).  
  转发过程：检查报文**目的 IP** → 与**路由表**比对 → 决定**下一跳路由器或直连主机** → **逐跳**转发（**“接力式”/bucket-brigade**）。  
- Each node only needs to **know the next hop**; details **beyond the next hop** (two or more hops away) are **unnecessary** to know.  
  每个节点**只需知道下一跳**；“两跳以外”的路径细节**无需感知**。  

---

### 3) Static vs Dynamic Routing / 静态路由 vs 动态路由

**Static Routing / 静态路由**  
- **Method**: Manually **configure fixed next hops** to each destination network on routers/hosts.  
  **方法**：在路由器/主机上**固定配置**到各目的网络的下一跳。  
- **Pros**: No routing protocol needed; good for **small networks** with few routers.  
  **优点**：无需配置路由协议；适合**路由器数量少**的场景。  
- **Cons**: When networks change or links/devices fail, it requires **manual edits**; **no automatic reroute**, higher ops burden.  
  **缺点**：网络新增/删除、链路/设备故障时需要**人工修改**；**无法自动绕行**，运维负担大。  

**Dynamic Routing / 动态路由**  
- **Method**: **Routing protocols** automatically **exchange and update** routes between routers (periodic or event-driven).  
  **方法**：由**路由协议**在路由器之间**自动传播/更新**路由信息（定期或事件触发）。  
- **Pros**: **Automatically adapts** to topology changes/failures and **selects alternate paths**; suitable for **large-scale** networks.  
  **优点**：拓扑变化或故障时**自动更新**并**选择绕行路径**，大幅降低运维负担；适合**大规模**网络。  
- **Cons**: Requires **protocol configuration and maintenance** (complexity varies by protocol).  
  **缺点**：需要配置/维护路由协议（不同协议复杂度不同）。  

---

### 4) Internet & Routing Protocols: AS, IGP, and EGP / 互联网与路由协议：AS、IGP 与 EGP

- **AS (Autonomous System)**: A set of routers under the **same routing policy/administrative domain** (e.g., universities, research institutes, ISPs).  
  **AS（Autonomous System, 自治系统）**：在**相同路由策略/管理域**下的一组路由器（如高校/研究机构/ISP）。  
- **IGP (Interior Gateway Protocol)**: Routing protocols used **inside an AS** — **RIP/RIP2** (small-scale), **OSPF** (medium/large), **IS-IS** (early IP ancestor/similar concept).  
  **IGP（Interior Gateway Protocol）**：用于**AS 内部**的路由协议 —— **RIP/RIP2**（小规模）、**OSPF**（中大型）、**IS-IS**（IP 早期祖先/同类思想）。  
- **EGP/BGP**: Used for **inter-AS** routing and policy control (the Internet uses **BGP**).  
  **EGP/BGP**：用于**AS 间**的路由选择与策略控制（Internet 采用 **BGP**）。  

---

### 5) Dynamic Routing Algorithm Types / 动态路由算法类型

- **Distance Vector**: e.g., **RIP/RIP2**; each router **advertises (distance, direction/next hop)** to neighbors, and picks the **lowest-cost** path.  
  **距离向量型**：如 **RIP/RIP2**；路由器向邻居**通告（距离、方向/下一跳）**，据此选择**最小代价**路径。  
- **Link State**: e.g., **OSPF**; routers **flood** local link states within an area, and **each router** runs SPF locally to compute the **shortest paths**.  
  **链路状态型**：如 **OSPF**；路由器在区域内**泛洪**本地链路状态，**每台路由器**在本地运行 SPF 计算**最短路径**。  

<details>
<summary>Supplement / 补充</summary>

- Distance Vector typical loop-prevention techniques: **split horizon**, **poison reverse**, **hold-down timers**.  
  距离向量常见环路抑制：**水平分割（split horizon）**、**反向毒化（poison reverse）**、**抑制定时器（hold-down）**。  
- Link State key steps: **LSA generation**, **flooding with sequence/age**, **SPF (Dijkstra)** over the **topology DB**; supports areas (e.g., OSPF **backbone area 0**).  
  链路状态关键流程：**LSA 生成**、**带序号/老化的泛洪**、在**拓扑数据库**上运行 **SPF（Dijkstra）**；支持多区域（如 OSPF **骨干区 0**）。  
</details>

---

### 6) RIP (Routing Information Protocol) / 路由信息协议

**Overview / 概览**  
- A long-standing **IP routing protocol** (rooted in early ARPANET ideas).  
  历史悠久的 **IP 路由协议**（源自 ARPANET 早期思想）。  
- **Metric = hop count**; advertises routes to neighbors using **UDP broadcast**.  
  **度量（Metric）= 跳数（Hop Count）**；通过 **UDP 广播**向相邻路由器通告路由信息。  
- Captures topology via “distance”, a **distance-vector** algorithm.  
  以“距离”刻画拓扑，属于**距离向量算法**。

**Basic Behavior / 基本行为**  
- **+1 hop** for each router traversed.  
  每**经过 1 个路由器**，跳数 **+1**。  
- **Periodic updates**: by default **every 30 s** to neighbors; upon receipt, set **sender as next hop**, **hop++**, and **update routing table** (if better or original route failed).  
  **周期更新**：默认**每 30 s**向邻居通告；收到通告后将**发送方作为下一跳**、**跳数+1**，并**更新路由表**（若更优或原路由失效）。  
- **Max metric = 16**: **≥16** means **unreachable**; such destinations are discarded.  
  **最大度量 = 16**：当度量 **≥16** 时视为**不可达**，相应目的**丢弃**。

**Timers / 定时器**  
- **Route Timeout (180 s)**: if no periodic update from a neighbor for **180 s**, mark routes via that neighbor **unreachable (metric=16)**, advertise this, and start **garbage collection**.  
  **Route Timeout（180 s）**：若 **180 s** 未收到某邻居更新，则将经其学习的路由标记为**不可达（metric=16）**并通告，同时启动**垃圾回收**。  
- **Garbage Collection (120 s)**: after **120 s**, **remove** the unreachable route from the table.  
  **Garbage Collection（120 s）**：**120 s** 到期后，从路由表**删除**该不可达路由。  

**Pros / 优点**  
- Simple to implement, widely deployed; many server OSes (e.g., Linux) **include support**; still useful in **small networks**.  
  实现简单、部署广，许多服务器操作系统（如 Linux）**内置支持**；在**小型网络**中仍然实用。  

<details>
<summary>Supplement / 补充</summary>

- Transport: **UDP port 520** (RIPv2 supports multicast **224.0.0.9** for updates).  
  传输层：**UDP 520 端口**（RIPv2 支持使用多播 **224.0.0.9** 发布更新）。  

- Improvements in **RIPv2**: carries subnet masks (CIDR), supports authentication, uses multicast instead of broadcast.  
  **RIPv2** 改进：携带子网掩码（CIDR）、支持认证、可用多播替代广播。  
</details>


---

### 7) RIP 报文格式（简）
```
Operation | Version | Address Family Identifier | IP Address | Metric
   ... up to 25 route entries per RIP message ...
```
- **Operation**：请求/响应。
- **Version**：版本号。
- **Address Family**：地址族标识。
- **IP Address**：目的网络地址。
- **Metric**：1～16（**16=不可达**）。
- **每条报文**可携带**最多约 25** 条路由项。
 
---
### 8) Count-to-Infinity Problem / 无穷计数（Count-to-Infinity）问题

**Symptom / 现象**  
- When a link/network fails, neighbors may **misinterpret each other’s advertisements as still reachable** due to the **gradual propagation** nature of distance-vector, so the metric to that destination **keeps increasing** (in RIP it rises up to **16**).  
  当某条链路/网络失效后，由于距离向量的**渐进传播**，邻居路由器会把对方的通告**误认为可达**，导致该目的的度量**不断增大**（在 RIP 中最高涨到 **16**）。  
- Although the **cap of 16** prevents a truly infinite loop, **invalid routes keep being advertised/updated** during convergence, **wasting bandwidth and time**.  
  虽有 **16 上限**避免“真正无穷”，但在此过程中会发生**无效路由反复被转发/更新**，浪费带宽并拉长**收敛时间**。

**Step-by-step illustration / 逐步过程示意**  
```
(1) Link goes down: R1 immediately removes 192.168.0.0/24
(2) R1 still receives an update from R2 saying "192.168.0.0/24 reachable"
(3) R1 re-adds the route via R2 with a larger metric (hop+1)
(4) R1 advertises this back to R2/R3...
(5) R2 increases the metric again based on R1's new update...
(6) Repeats until metric reaches 16 → marked unreachable and flushed
```
```
(1) 链路Down：R1 立即把 192.168.0.0/24 从表中删除
(2) R1 仍可能从 R2 收到“到 192.168.0.0/24 可达”的更新
(3) R1 依据 R2 的更新，误将该网段重新加入（度量更大）
(4) R1 把该更新再通告给 R2/R3 ...
(5) R2 又据 R1 的更新提高度量并通告 ...
(6) 如此往复，度量逐步攀升，直到 16 → 标记不可达
```

<details>
<summary>Mitigations / 缓解手段（补充）</summary>

- **Split Horizon**：do not advertise a route back out the interface from which it was learned.  
  **水平分割**：不从学到该路由的同一接口再通告该路由。  
- **Poison Reverse**：advertise that route back to the learned interface with **metric=∞ (16)**.  
  **毒性逆转**：向原接口通告该路由但将度量置为**不可达（16）**。  
- **Holddown Timers**：suppress flapping by delaying acceptance of worse routes for a period.  
  **抑制定时器**：一段时间内拒绝接受更差的路由，抑制抖动。  
</details>

> the process is illustrated via interactions among **R1/R2/R3**. RIP limits divergence with **max hop count = 16**, but there is still a period of **needless advertisements** and **routing-table oscillations** during convergence.
> **注**：讲义中以 **R1/R2/R3** 的交互说明该过程；RIP 通过 **“最大跳数 = 16”** 限制发散，但仍会造成一段时间的**无谓广播**与**表项震荡**。  
 
---

## Key Points

- **STP** computes a loop-free topology via **root bridge / path cost / port roles**, **blocks redundant ports** to prevent **broadcast storms**, and **fails over** on link/port failures; classic STP converges in **tens of seconds**, while **RSTP** brings this down to **a few seconds**.  
  **STP** 通过**根桥/路径代价/端口角色**计算无环拓扑，**阻塞冗余端口**以抑制**广播风暴**；故障时可自动切换，传统 STP 收敛**数十秒**，**RSTP** 降至**数秒**。
- **Routers forward hop-by-hop**: each node only needs the **next hop**; forwarding correctness depends on an **accurate routing table**.  
  **路由器逐跳转发**：每个节点只需知道**下一跳**；转发正确性取决于**路由表的准确性**。
- **Static routing** is simple to configure but **doesn’t adapt** to topology changes; **dynamic routing** **exchanges updates periodically**, can **reroute automatically**, and suits larger networks.  
  **静态路由**配置简单但**不随拓扑自适应**；**动态路由**会**定期交换更新**、可**自动绕行**，更适合大规模网络。
- **AS / IGP / EGP**: within an AS use **RIP/RIP2/OSPF/IS-IS**; across ASes use **BGP**.  
  **AS/IGP/EGP**：AS 内常用 **RIP/RIP2/OSPF/IS-IS**；AS 间使用 **BGP**。
- **RIP**: **30 s** periodic updates, **metric = hop count**, **max = 16**; **180 s** timeout to mark routes unreachable, **120 s** garbage collection to remove them; suffers from the **count-to-infinity** problem (bounded by 16 but still incurs convergence overhead).  
  **RIP**：**30 s** 定期更新、**度量=跳数**、**最大=16**；**180 s** 超时标记不可达、**120 s** 垃圾回收删除；存在**无穷计数问题**（以上限 16 抑制但仍有收敛开销）。
  
---

## ※※ Supplementary Cheat Sheets | 速查单

### STP & RIP Quick Reference
- [STP Port Roles & Convergence | STP 端口角色与收敛流程](./figs/lecture09_stp_port_roles.md)  
  *生成树协议的根桥选举、端口角色、收敛过程与定时器*

- [RIP Timers & Metrics | RIP 定时器与度量](./figs/lecture09_rip_timers_metrics.md)  
  *RIP 协议的定时器、最大跳数、无穷计数问题与报文字段*


<h2></h2>


[← Previous / 上一章](./lecture08.md) ·[Next / 下一章：Lecture 10](./lecture10.md) ·[Course README / 课程目录](./README.md#toc) ·[Notes Home / 笔记首页](../) ·[Repository Home / 仓库首页](../../README.md)


[← Back to Course README / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 10: RIP Enhancements (Split Horizon/Poison Reverse, RIP v2) & DNS (Domain Names, Nameservers, Resolution)
# RIP 改进（分隔视界/毒性逆转、RIP v2）与 DNS（域名、名称服务器、名称解析）

---

## ⚪ Lecture Overview 
- **Loop-avoidance in distance-vector**: **Split Horizon** & **Poison Reverse** principles and comparison.  
  距离向量路由的**环路抑制**：**分隔视界**与**毒性逆转**的原理与对比。  
- **RIP limitations** & **RIP v2** improvements (mask carrying, authentication, multicast).  
  **RIP 局限**与 **RIP v2** 的改进（可携带掩码、报文认证、默认多播）。  
- **RIP v2 packet format**: fields and metric range (1–15; **16 = unreachable**).  
  **RIP v2 报文结构**：关键字段与度量范围（1–15；**16=不可达**）。  
- **Domain Names & DNS**: hierarchy (gTLD/ccTLD), length limits, **Name Server** & **Root**, **forward/reverse** lookups.  
  **域名与 DNS**：树状层次（通用/国家顶级域）、长度限制、**名称服务器**与**根服务器**、**正向/反向解析**。 
- **How name resolution works**: recursive/iterative queries, caching, HA (primary/secondary NS, zone transfer).  
  **名称解析流程**：递归/迭代、缓存、高可用（主/从服务器、区域传送）。
  
---

## ⚪ Lecture Content 

## 1) Split Horizon & Poison Reverse — Loop Avoidance  
## 分隔视界与毒性逆转——抑制路由环路

**Motivation.** In distance-vector protocols (e.g., RIP), failures can cause neighbors to re-advertise stale routes, leading to **count-to-infinity**.  
**动机。** 在距离向量协议（如 RIP）中，故障可能导致邻居**反复通告错误路由**，引发**无穷计数**。
- **Split Horizon.** “Do **not** advertise a route back out the **interface it was learned on**.”  
  **分隔视界。** “**不**将从接口 X 学到的前缀**再从接口 X 通告回去**。” 这样避免 A↔B 之间的信息回环。
- **Poison Reverse.** If you must mention it, **advertise it with maximum metric** (RIP: **16**) to the neighbor you learned it from.  
  **毒性逆转。** 若必须告知原邻居，则以**最大度量**（RIP：**16**）通告，显式表示“**不要走我**”。
**Summary.** Split Horizon = **suppress**; Poison Reverse = **advertise-as-unreachable**. Both reduce loops and speed convergence.  
**小结。** 分隔视界＝**不通告**；毒性逆转＝**通告为不可达**。二者均减少环路并加快收敛。

---

## 2) RIP: Problems & Limitations  
## RIP 的局限与问题
- **Metric = hop-count only** → ignores link speed/latency; fewest hops ≠ fastest path.  
  **度量仅为跳数** → 忽略**链路速率**；最短“跳数”路径**不一定**是**最短时延**路径。 
- **Slow reaction** to topology changes.  
  **拓扑变化**（增删结点/链路）**反映慢**。  
- **Max hop = 15** (16 = unreachable) → **scalability limit**.  
  **最大跳数=15**（**16=不可达**）→ **规模受限**。  
- **RIP v1 lacks subnet masks** (fixed classes).  
  **RIP v1 不携带子网掩码**（RIP2 解决）。  
- **Periodic broadcasts** even when unchanged → waste; better to send on **change/request**.  
  **周期性广播更新**（即使无变化）→ **无谓流量**；更理想的做法是**仅变化/被请求时**发送。
  
---

## 3) RIP v2 — Improvements & Packet Format  
## RIP v2 —— 改进与报文格式

- **Improvements vs RIP v1.**
  **RIP2 相比 RIP1 的改进**：
1) **Carries subnet mask** (CIDR-capable).  
   **可携带子网掩码**（支持无类/CIDR 的前缀）。  
2) **Message authentication** (to prevent spoofing).  
   **报文级认证**（防伪造）。  
3) **Multicast updates by default** (224.0.0.9) instead of broadcast.  
   **默认使用多播**（224.0.0.9）进行更新分发 而非广播。
   
- **RIP2 Packet Format 报文结构**（每报文最多约 25 条路由项）：  
```
  | Command | Version=2 | Address Family ID | Route Tag |
  |   IP Address        |   Subnet Mask     | Next Hop  | Metric (1..15; 16=unreachable) |
  (… repeat per route entry …)
```
- **IP Address**: Destination network or host address.  
  **IP Address**：目的网络或目的主机地址
- **Subnet Mask**: Network mask for this route entry.  
  **Subnet Mask**：该条目的网络掩码
- **Next Hop**: Next-hop router IP (may differ per entry).  
  **Next Hop**：下一跳路由器 IP（可因条目不同而不同）
- **Metric**: 1–15 valid; **16 = unreachable**.  
  **Metric**：1–15；**16 表示不可达**

 
---

### 4) Domain Names — Concept & Need
- **Why domain names exist**: Compared to hard-to-remember numeric IPs, **letter+dot** names are easier to remember and type; we need a system to **map Domain ⇄ IP** for both humans and machines.  
  **域名为何存在**：与难记的数字型 IP 相比，**字母+点号** 的域名更便于记忆与输入；需要一个把 **域名 ⇄ IP** 互相转换的系统来服务人和机器。
- **DNS (Domain Name System)**: Provides the **mapping database** and query mechanisms (name resolution) from **domain name to IP**.  
  **DNS（域名系统）**：提供**域名到 IP** 的**映射数据库**与查询机制（名称解析）。
- **Multilingual support**: Domain names support multiple languages (including Japanese) via Internationalized Domain Names.  
  **多语言支持**：域名通过国际化域名机制可支持多种语言（包括日文）。
- **Examples**:  
  - Email address (contains domain): `aoki@mail.example.co.jp`  
    **邮件地址（含域名）**：`aoki@mail.example.co.jp`  
  - Homepage address (host = domain name): `www.example.co.jp`  
    **主页地址（域名即主机名）**：`www.example.co.jp`
- **Global uniqueness**: Public server domain names on the Internet must be **globally unique**, consistent with the **global uniqueness of IP addresses**.  
  **全局唯一性**：在互联网上公开的服务器域名必须**全局唯一**，这一点与 **IP 地址的全局唯一性** 相一致。

---

## 5) DNS — What It Does & How to Check / DNS 的作用与本机查询

- **What it does**: When you enter a domain name, DNS looks up the **domain ↔ IP** mapping in its databases and automatically converts the name to an IP address (**name resolution**).  
  **作用**：输入域名时，DNS 会查询其数据库中的 **域名 ↔ IP** 映射，自动将域名转换为 IP 地址（**名称解析**）。
- **Windows commands**:  
  **Windows 命令**：
```
nslookup <domain>
nslookup www.kcg.ac.jp
```
- **Example**: With DNS, you don’t need to enter `153.127.246.22`; just type `www.kcg.ac.jp`.  
  **示例**：利用 DNS，访问 KCG 网站时**无需**直接输入 `153.127.246.22`，而是输入 `www.kcg.ac.jp`。
  
---

## 6) Domain Name Hierarchy / 域名层次结构（树形）

- **Tree structure**: a hierarchical **tree** with the **root** at the top and branches below.  
  **树状结构**：以 **root（根）** 为顶点，向下分支的**层级树**。
- **TLD (Top-Level Domain) categories**:  
  - **gTLD (generic TLDs)**: e.g., `.com .net .org .edu .gov .int`, and some **geographic-style** generics like `.kyoto` `.tokyo`.  
    **gTLD（通用顶级域）**：如 `.com .net .org .edu .gov .int`，以及地名类通用域如 `.kyoto` `.tokyo`。  
  - **ccTLD (country-code TLDs)**: e.g., `.jp .uk .cn`.  
    **ccTLD（国家/地区顶级域）**：如 `.jp .uk .cn`。
- **Examples**: `www.kcg.ac.jp`, `www.kcgi.ac.edu`.  
  **示例**：`www.kcg.ac.jp`、`www.kcgi.ac.edu`。
- **JP second-level domains (managed by JPNIC)**: `ac, co, ed, go, or, ne, gr, ad, lg`, etc., roughly mapping to **academia, companies, education, government, nonprofit, network services, groups/individuals, members, local governments**.  
  **日本（.jp）二级域（由 JPNIC 管理）**：`ac, co, ed, go, or, ne, gr, ad, lg` 等，对应**教育机构、企业法人、教育、政府、非营利、网络服务、团体/个人、会员、地方自治体**等用途。
- **Common gTLDs**: `.com .net .edu .org .int .gov`, administered globally by **ICANN** (there are **159** generic categories/background items).  
  **常见通用域**：`.com .net .edu .org .int .gov`，由 **ICANN** 统一管理（**通用域项约 159 种**）。
 
---

### 7) Domain Levels & Length Limits / 层级与长度限制

- **Decomposition example 1 (URL)**: `www.example.co.jp`  
  **层级拆解示例 1（URL）**：`www.example.co.jp`
  - **TLD**: `jp`  
    **顶级域（TLD）**：`jp`
  - **2nd level**: `co`  
    **二级域**：`co`
  - **3rd level**: `example`  
    **三级域**：`example`
  - **4th level**: `www`  
    **四级域**：`www`
- **Decomposition example 2 (Email)**: `aoki@mail.example.co.jp`  
  **层级拆解示例 2（Email）**：`aoki@mail.example.co.jp`
  - **TLD**: `jp`; **2nd**: `co`; **3rd**: `example`; **4th**: `mail`  
    **顶级域**：`jp`；**二级**：`co`；**三级**：`example`；**四级**：`mail`
  - **local-part** (non-domain portion): `aoki`  
    **local-part（非域名部分）**：`aoki`
- **Length limits**  
  **长度限制**
  - **Per label** ≤ **64** characters  
    **每级（Label）** ≤ **64** 个字符
  - **Full domain name (FQDN)** ≤ **253** characters  
    **完整域名（FQDN）** ≤ **253** 个字符
  - **Email local-part** ≤ **64** characters  
    **电子邮件 local-part** ≤ **64** 个字符

---
### 8) Name Servers & Root / 名称服务器与根服务器

- **Name Server (DNS server)**: Manages domain data for a specific **zone** (administrative region); it only maintains **its own zone’s** records, but must also register the **next-lower-level** name servers’ IPs.  
  **名称服务器（DNS 服务器）**：负责某一层级（**Zone** 区域）的域名信息；只管理**本区域**记录，但需登记**下一层**名称服务器的 IP。
- **Root Name Servers**: There are **13 logical root server letters** worldwide. The slide’s example distribution notes **10 in the US, 1 in Japan, 1 in the UK, and 1 in Sweden**. The **NS records of TLDs** are stored at the Root, so **any addition/change of a TLD** must be reflected at the Root layer.  
  **根名称服务器（Root）**：全球有 **13 组逻辑根服务器**。讲义示例分布为：**美国 10、日本 1、英国 1、瑞典 1**。**顶级域（TLD）的 NS 记录**存放在 Root，故**顶级域的新增/变更**需要在 Root 层反映。

---

## 9) How DNS Resolution Works / 名称解析过程（递归/迭代）

**High-level steps (with caching) / 高层步骤（含缓存）**
```
1. App → Stub Resolver: The application (e.g., browser) asks the OS **stub resolver** to resolve `<domain>`.  
   应用 → 桩解析器：应用（如浏览器）把 `<domain>` 的解析请求交给操作系统的**桩解析器**。
2. Stub → Recursive Resolver: The stub sends the query to the organization/ISP’s recursive resolver (caching DNS).  
   桩 → 递归解析器：桩解析器把查询发给单位/ISP 的递归解析器（带缓存的 DNS）。
3. Check Cache: If the answer is cached and the TTL hasn’t expired, return it immediately.  
   检查缓存：若缓存命中且 TTL 未过期，立刻返回结果。
4. Ask Root (iterative): If unknown, the recursive resolver queries a Root server and gets a referral to the TLD (e.g., `.com`).  
   询问根（迭代）：若未知，递归解析器询问根服务器，获得指向顶级域（TLD）（如 `.com`）的转介。
5. Ask TLD: Query the TLD name server to obtain a referral to the authoritative server for the second-level zone (e.g., `example.com`).  
   询问 TLD：向 TLD 服务器查询，得到该二级域（如 `example.com`）权威服务器的转介。
6. Ask Authoritative: Query the authoritative server for the final A/AAAA (and any CNAME) records.  
   询问权威服务器：向权威服务器查询，获得最终的 A/AAAA（以及可能的 CNAME）记录。
7. Return & Cache: Send the answer back to the client and cache it for the duration of its TTL.  
   返回并缓存：把答案返回给客户端，并按其 TTL 缓存结果。
```
**Slides emphasize**: A **Name Server** basically knows only **its own zone** and the **next-lower-level NS** addresses; **DNS caching** reduces repeated queries.  
**讲义强调**：**名称服务器（Name Server）**基本只知道**本区域（Zone）**与**下一层 NS 的地址**；启用**DNS 缓存（DNS cache）**可减少重复查询。

**Recursive vs Iterative / 递归与迭代**
- **Recursive query**: The client asks a resolver to **do all the work** and return the final answer.  
  **递归查询**：客户端让解析器**代为完成全部查询**并返回最终答案。  
- **Iterative query**: The resolver queries each tier and follows **referrals** until it reaches the authority.  
  **迭代查询**：解析器逐级查询并沿着**转介**继续，直至到达权威服务器。
  
**Caching & TTL / 缓存与生存时间**

- **TTL (Time To Live)** controls how long an answer is valid in caches; shorter TTL → fresher data but more queries.  
  **TTL（生存时间）**决定答案在缓存中的有效期；TTL 越短 → 数据越新，但查询次数越多。
- Negative caching stores **non-existence** results (e.g., NXDOMAIN) for a short TTL to reduce repeated misses.  
  **负缓存**会在短 **TTL** 内缓存“**不存在**”（如 NXDOMAIN）的结果，减少重复未命中查询。
- Caches may honor authoritative **minimum TTL** and zone **SOA** timers to balance freshness and load.  
  缓存会遵循权威服务器的**最小 TTL**与区域 **SOA** 定时器，以平衡新鲜度与负载。
  
---

### 10) Forward vs Reverse Lookup / 正向与反向解析

- **Forward lookup**: **Domain → IP** (common for visiting websites, SSH, etc.).  
  **正向解析**：**域名 → IP**（访问网站、远程登录等常用）。  
  *Example / 例*：`www.example.com → A/AAAA → 203.0.113.10`
- **Reverse lookup**: **IP → Domain** (used by servers for source verification/analytics).  
  **反向解析**：**IP → 域名**（服务器端来源确认/日志分析常用）。  
  *Example / 例*：`203.0.113.10 → PTR → host-10.example.com`
- **Cross-check (validation)**: Do a **reverse** to get a domain, then **forward** that domain to get an IP; compare with the original IP to increase trust.  
  **交叉校验（提高可信度）**：先做**反向解析**得到域名，再对该域名做**正向解析**取回 IP，并与原始 IP **比对**。

--- 

### 11) Redundancy: Primary & Secondary NS / 冗余：主/辅名称服务器

- **Why at least two NS**: Any single NS failure can disrupt web/mail and downstream subdomains. For **fault tolerance and load sharing**, deploy **≥ 2** NS, preferably on **different sites/hardware**.  
  **为何至少两台 NS**：任一 NS 故障都会影响网页/邮件以及更下层子域。为实现**容灾与负载分担**，应部署**至少 2 台**，且尽量位于**不同地点/不同硬件**。
- **Primary / Secondary roles**  
  **Primary（master）**: handles day-to-day edits and zone authority.  
  **Secondary（slave）**: standby and query offload; stays in sync via **Zone Transfer (AXFR/IXFR)**.  
  **主/从角色**  
  **Primary（主）**：负责日常更新与区权威。  
  **Secondary（从）**：承担读取与备援；通过**区域传送（AXFR/IXFR）**与主同步。
- **N>2 layout**: If you run **3+** NS, keep **exactly 1 Primary** and make the rest **Secondary**.  
  **多于 2 台的布局**：当部署 **3 台及以上** 时，保持**仅 1 台主服务器**，其余均为**从服务器**。
- **Typical implementation**: The widely used DNS software is **BIND (Berkeley Internet Name Domain)**; current mainstream is **BIND 9**.  
  **常见实现**：业界广泛使用 **BIND（Berkeley Internet Name Domain）**，当前主流为 **BIND 9**。

---

## Key Points

- **Split Horizon & Poison Reverse**: Do **not** advertise a route back out the interface it was learned on (**Split Horizon**); if you must send it back, advertise it with **metric=16 (unreachable)** (**Poison Reverse**). Both reduce loops and **count-to-infinity**.  
  **Split Horizon 与 Poison Reverse**：**不要**把从某接口学到的路由再从该接口通告出去（**Split Horizon**）；如必须回告，则以 **metric=16（不可达）** 通告（**Poison Reverse**）。二者均可抑制环路与**无穷计数**。
- **RIP limitations & RIP v2 improvements**: RIP uses **hop count only**, converges **slowly**, caps at **15 hops** (16=unreachable), **v1 carries no mask**, and **periodically broadcasts**. **RIP v2** carries **subnet masks**, supports **authentication**, and uses **multicast** by default; entries include **Next Hop** and **Metric (1–15)**.  
  **RIP 的局限与 RIP v2 改进**：RIP 仅以**跳数**为度量、**收敛慢**、**15 跳上限**（16=不可达）、**v1 不携带掩码**、且**周期广播**。**RIP v2** 可携带**子网掩码**、支持**认证**、默认**多播**；条目含 **Next Hop/Metric（1–15）**。
- **Domain & DNS essentials**: Hierarchical tree (**gTLD/ccTLD**), constraints `label ≤ 64`, `FQDN ≤ 253`; **Name Server / Root** layered management; **forward/reverse** lookups and **caching**; production deployments should run **at least two NS** (Primary/Secondary with **zone transfer**).  
  **域名与 DNS 要点**：树状层级（**gTLD/ccTLD**），长度限制 `label ≤ 64`、`FQDN ≤ 253`；**Name Server/Root** 分层管理；**正引/逆引**与**缓存**机制；生产环境应至少部署**两台 NS**（主/从并进行**区域传送**）。

---

## ※※ Supplementary Cheat Sheets | 速查单

### RIP v2 & DNS Quick Reference
- [RIP v2 Packet Fields | RIP v2 报文字段速查](./figs/lecture10_rip2_packet_fields.md)  
  *RIP v2 报文结构、字段说明与主要改进*

- [DNS Resolution Flow | DNS 名称解析流程速查](./figs/lecture10_dns_resolution_flow.md)  
  *DNS 递归/迭代解析过程、服务器角色与冗余设计*

<h2></h2>

[← Previous Chapter / 上一章](./lecture09.md) ·[Next Chapter / 下一章 →](./lecture11.md) ·[Course README / 课程目录](./README.md#toc) ·[Notes Home / 笔记首页](../) ·[Repository Home / 仓库首页](../../README.md)



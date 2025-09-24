#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 10: RIP Enhancements (Split Horizon/Poison Reverse, RIP v2) & DNS (Domain Names, Nameservers, Resolution)
# 情報ネットワーク概論 第10回：RIPの改良（スプリットホライズン／ポイズンリバース・RIP2）とDNS（ドメイン名・ネームサーバ・名前解決）

---

## ⚪ Lecture Overview 
- **Loop-avoidance in distance-vector**: **Split Horizon** & **Poison Reverse** 原理与对比  
  距离向量路由的**环路抑制**：**分隔视界**与**毒性逆转**机制  
- **RIP limitations** & **RIP v2** improvements（mask carrying, auth, multicast）  
  **RIP 局限**与 **RIP v2** 改进（可携带掩码、报文认证、默认多播）  
- **RIP v2 packet format**：字段与度量范围（1–15；**16=不可达**）  
  **RIP v2 报文结构**：关键字段与度量（1–15；**16=不可达**）  
- **Domain Names & DNS**：层次结构（gTLD/ccTLD）、长度限制、**Name Server** 与 **Root**、**正引き/逆引き**  
  **域名与 DNS**：树状层次（通用/国家顶级域）、长度约束、**名称服务器**与**根服务器**、**正向/反向解析**  
- **How name resolution works**：递归/迭代查询流程、缓存与高可用（主/辅 NS、区域传送）  
  **名称解析流程**：递归/迭代、缓存、冗余（主/从服务器、区域传送）

---

## ⚪ Lecture Content 

### 1) Split Horizon & Poison Reverse — Loop Avoidance  
### 分隔视界与毒性逆转 —— 路由环路抑制
- **Motivation 动机**：在距离向量协议（如 RIP）中，链路/节点失效后，错误路由可能被邻居**反复通告**导致**无穷计数**趋势。引入策略以抑制从**原路返回**的虚假最短路信息。
- **Split Horizon 分隔视界**：  
  “**不要把从接口 X 学到的某前缀，再从接口 X 通告回去**”。  
  例：A 从 B 得知到网段 C 的路由，**A 不会**再把该路由**发还给 B**。这样 A↔B 间不形成**信息回环**。
- **Poison Reverse 毒性逆转**：  
  若必须向**原发送者**通告与其相关的前缀，则将其**度量设为最大**（RIP 中 **16=不可达**），显式告知“**不要走我这条路**”。 
- **差异小结**：Split Horizon=**不通告**；Poison Reverse=**通告为不可达**。两者均减少环路与无穷计数发生概率。
---

### 2) RIP: Problems & Limitations  局限与问题点
- **度量仅考虑跳数**，忽略**链路速率** → 最短“跳数”路径**不一定**是**最短时延**路径。  
- **拓扑变化**（增删结点/链路）**反映慢**。  
- **最大跳数=15**（**16=不可达**）→ **规模受限**。  
- **RIP v1 不携带子网掩码**（RIP2 解决）。  
- **周期性广播更新**（即使无变化）→ **无谓流量**；更理想的做法是**仅变化/被请求时**发送。 

---

### 3) RIP v2 — Improvements & Packet Format  改进与报文格式
- **RIP2 相比 RIP1 的改进**：  
  1) **携带子网掩码**（支持无类/CIDR 的前缀）  
  2) **报文级认证**（message-level authentication）  
  3) **默认使用多播** 进行更新分发（而非广播）
- **RIP2 Packet Format 报文结构**（每报文最多约 25 条路由项）：  
```
  | Command | Version=2 | Address Family ID | Route Tag |
  |   IP Address        |   Subnet Mask     | Next Hop  | Metric (1..15; 16=unreachable) |
  (… repeat per route entry …)
```
- **IP Address**：目的网络或目的主机地址
- **Subnet Mask**：该条目的网络掩码
- **Next Hop**：下一跳路由器 IP（可因条目不同而不同）
- **Metric**：1–15；**16 表示不可达**
 
---
### 4) Domain Names — Concept & Need 域名的概念与必要性
- **Why 域名为何存在**：与难记的 IP（数字串）相比，**字母+点号** 的域名便于记忆与输入；需将**域名 ↔ IP** 互换的系统来服务人/机两侧。
- **DNS (Domain Name System)**：提供**域名到 IP** 的**映射数据库**与查询机制（名称解析）。
- **多语言**支持：域名支持包括日文在内的多语言（讲义强调）。
- **示例**：
  - 邮件地址（含域名）：`aoki@mail.example.co.jp`
  - 主页地址（域名即主机名）：`www.example.co.jp`
在互联网公开的服务器域名必须**全局唯一**，与**全球 IP 唯一性**一致。

 
---
## 5) DNS — What It Does & How to Check DNS 的作用与本机查询
- **作用**：输入域名时，DNS 访问保存域名↔IP 对应关系的数据库，完成自动转换（名称解析）。
-** Windows 命令**：
```
nslookup <domain>
nslookup www.kcg.ac.jp
```
利用 DNS，访问 KCG 网站时**无需**直接输入 `153.127.246.22`，而是输入 `www.kcg.ac.jp`。
 
---
## 6) Domain Name Hierarchy 域名层次结构（树/木结构）
- **树状结构**：顶层为**root**，下分多枝。
- **TLD（Top Level Domain）顶级域**分为：
  - **gTLD**（一般/通用顶级域）：如 `.com .net .org .edu .gov .int`，以及地名类` .kyoto .tokyo `等
  - **ccTLD**（国家/地区顶级域）：如` .jp .uk .cn `等
- **示例**：`www.kcg.ac.jp`、`www.kcgi.ac.edu`
**JP 的第二层域（二级域）（由 JPNIC 管理）**：`ac, co, ed, go, or, ne, gr, ad, lg `等（对应教育机构、企业法人、政府、非营利、网络服务、团体/个人、会员、地方自治体…）。

**一般域举例**：`.com .net .edu .org .int .gov` 等，由**ICANN **统一管理（讲义指出**一般域现有 159 种**的背景说明）。
 
---
## 7) Domain Levels & Length Limits 层级与长度限制
- **层级拆解示例 1（URL）**：`www.example.co.jp`
  - TLD：`jp`
  - 2nd level：`co`
  - 3rd level：`example`
  - 4th level：`www`
- **层级拆解示例 2（Email）**：`aoki@mail.example.co.jp`
  - TLD：`jp`；2nd：`co`；3rd：`example`；4th：`mail`
  - local-part（非域名部分）：`aoki`
- **长度限制**：
  - 每级（Label）≤ 64 个字符
  - 完整域名 ≤ 253 个字符
  - local-part ≤ 64 个字符（电子邮件）

---
## 8) Name Servers & Root 名称服务器与根服务器
- **Name Server（DNS 服务器）**：负责某一层级（**Zone **区域）的域名信息；只管理**本区域**信息，但需登记**下一层**名称服务器 IP。
- **Root Name Servers（根服务器）**：全局 13 个系列；讲义给出分布示例：**美国 10、日本 1、英国 1、瑞典 1**。<br/>顶级域的 NS 记录存放在 Root，故**顶级域的新增/变更**需要在 Root 层反映。

---
##  9) How DNS Resolution Works 名称解析过程（递归/迭代）
高层步骤（含缓存）：
```
1) 浏览器/应用发起对 <domain> 的解析请求
2) 本地/组织的 Name Server 查询缓存
   - 若命中，直接返回给客户端
3) 若未知，向 Root Name Server 询问
   - Root 返回该 TLD 的 Name Server IP
4) 向 TLD Name Server 询问
   - TLD 返回该二级域的 Name Server IP
5) 向二级域 Name Server 询问
   - 返回第三级（或权威）Name Server IP
6) 向权威 Name Server 询问
   - 返回最终的 A/AAAA 记录（目的 IP）
7) 组织 NS 将结果返回给客户端，并按 TTL 缓存
```
讲义强调：**Name Server 基本只知道本 Zone 与下一层 NS 的地址**；**缓存（DNS cache）**可减少重复查询。

---
## 10) Forward vs Reverse Lookup 正向与反向解析
- **正引き（Forward）**：**域名 → IP**（访问网站、远程登录等常用）。
- **逆引き（Reverse）**：**IP → 域名**（服务器端来源确认/分析）。
- **校验**：以**逆引**得到的域名再做**正引**得到 IP，与原 IP **比对**以提升可信度。

--- 11) Redundancy: Primary & Secondary NS 冗余：主/辅名称服务器
- **为何至少两台 NS**：任何 NS 故障都会影响网页/邮件等服务；更下层域也受影响。故为**容灾与负载分担**，至少部署**2 台**，且尽量**不同地点/硬件**。
- **Primary / Secondary**：
  - **Primary（主）**：日常使用/更新；
  - **Secondary（从）**：备援/分担；通过**Zone Transfer（区域传送）**自动与主同步。
  - 若有 3 台以上，仅**1 台主**，其余均为从。
- **实现**：讲义指出最常用 DNS 服务为** BIND（Berkeley Internet Name Domain）**，当前系列** BIND9**。


---
## Key Points
- **Split Horizon**：不把从某接口学到的路由再从该接口通告回去；<br/>
**Poison Reverse**：向原接口通告** metric=16（不可达）** ———— 二者均抑制环路/无穷计数。
- **RIP 限制**：仅以跳数为度量、收敛慢、15 跳上限、不携带掩码、周期广播；<br/>
RIP2：携带掩码、支持认证、默认多播，报文字段含 **Next Hop/Metric(1–15)**。
- **域名/DNS**：树状层级（gTLD/ccTLD），`label ≤ 64`、`FQDN ≤ 253`；
**Name Server/Root **分层管理，**正引/逆引**与**缓存**机制；生产上至少两台 NS（主/从、区传）。

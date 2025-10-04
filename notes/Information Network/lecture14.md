[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor :Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 14: Hidden Terminal & RTS/CTS, Handover/Roaming, Bluetooth, Firewall/IDS/IPS/AV, DMZ, IDS/IPS Methods, VPN & IPsec, Proxies (Forward/Reverse)
# 第14讲：隐藏终端与 RTS/CTS、切换/漫游、蓝牙、防火墙 / IDS / IPS / 杀毒、DMZ、IDS/IPS 方法、VPN 与 IPsec、代理（正向 / 反向）

---

## ⚪ Lecture Overview 
- **Hidden Terminal** in WLAN & **RTS/CTS** handshake for collision avoidance  
  无线局域网**隐藏终端**问题与 **RTS/CTS** 碰撞回避流程 
- **Handover (handoff)** & **Roaming** differences and continuity  
  **切换**与**漫游**的区别与连续通信 
- **Bluetooth** basics: versions, classes, profiles, pairing, vs Wi-Fi  
  **蓝牙**基础：版本/功率等级/配置文件/配对，与 Wi-Fi 的对比
- **Security middleboxes**: Firewall, **IDS/IPS**, **Antivirus**; **DMZ** design  
  安全中间件：防火墙、**入侵检测/防御**、**杀毒**；**隔离区 DMZ** 设计 
- **IDS/IPS methods**: Signature-based vs Anomaly-based  
  **签名法**与**异常检测法**的对比与组合
- **VPN** concepts, tunneling & crypto/auth; **Transport vs Tunnel** modes; **IPsec**  
  **虚拟专网**、隧道与加密/认证；**传输/隧道**两种模式；**IPsec** 框架
- **Proxies**: Forward Proxy purposes (security/caching/auth/filter) & **Reverse Proxy** roles  
  **正向代理**的目的（安全/缓存/认证/过滤）与**反向代理**的作用（隐藏后端/卸载 SSL 等）

---

## ⚪ Lecture Content 

### 1) Hidden Terminal Problem & RTS/CTS 隐藏终端与 RTS/CTS
**Hidden Terminal 概念 | Definition**  

- Because of **obstacles or distance**, station **B** cannot hear station **A**, while the **AP (Access Point)** can hear both A and B. As a result, **B** may transmit without knowing the medium is already busy, causing a **collision**. Such stations that are both reachable by the AP but **not** by each other are called **hidden terminals**. To avoid these collisions, the **RTS/CTS (Request To Send / Clear To Send)** mechanism is introduced.
  
  由于**障碍物或距离**的影响，终端 **B** 听不到终端 **A** 的信号，而 **AP（Access Point，接入点）** 能同时听到 A 与 B 的信号。结果是 **B** 在**不知道信道已被占用**的情况下发起发送，从而引发**碰撞**。这类**对 AP 可达但彼此不可达**的终端称为**隐藏终端**。为避免这类碰撞，标准引入了 **RTS/CTS（Request To Send / Clear To Send，发送请求 / 允许发送）** 机制。

```
1) Station A senses the channel idle for ≥ DIFS, then sends RTS (Request To Send) to the AP. 
2) The AP, after SIFS, sends CTS (Clear To Send) — informing A and neighbors (e.g., B).  
3) Station A waits for SIFS, then transmits the DATA frame.
```
```
1) 终端A监听信道为空闲 ≥ DIFS → 向AP发送 RTS (Request To Send)
2) AP 在 SIFS 后发 CTS (Clear To Send) → 通知 A 与 B
3) 终端A 等待 SIFS → 发送 DATA 帧
```
**RTS/CTS Interaction (Steps 4–5) / RTS/CTS 交互（步骤 4–5）**
```
4) After A finishes sending DATA, the AP waits SIFS and transmits ACK (Acknowledgment) → informing A (success) and neighbors (e.g., B).  
5) Station B cannot hear A, but it can hear the AP’s CTS/ACK → it stays silent during the reserved period, then resumes contention after receiving ACK.
```
```
4) A发完DATA后，AP在 SIFS 后发 ACK → 通知 A 与 B
5) 终端B虽收不到A的信号，但能收到AP的 CTS/ACK → 期间保持静默
   收到 ACK 后解除发送禁止，再参与竞争
```
**Key point:** The **AP** “announces” the reserved timeslot to all stations that can hear it via **CTS/ACK**, so **hidden terminals** avoid transmitting concurrently with **A**.

**要点：** AP 以**CTS/ACK**向所有能听到它的站点“宣告占用时隙”，**隐藏终端**据此避免与 A 同时发送。

---

### 2) Handover & Roaming / 切换与漫游

- **Handover**: While moving across cell or WLAN **AP coverage boundaries**, the device **switches to a new base station/AP** **without dropping the connection**. The **IP address is preserved** (or session continuity is maintained), so ongoing sessions do not break.
 
  **切换（Handover）**：终端在移动穿越蜂窝或 WLAN 的 **AP 覆盖边界** 时，**无缝切换到新的基站/接入点而不断线**；**IP 地址保持/会话不中断**。
  
- **Roaming**: Communication continues **across different operators’ networks** using the **same device and number** (e.g., **international roaming**: your phone attaches to a local operator abroad and keeps working).
    
  **漫游（Roaming）**：在 **不同运营商网络之间** 仍可使用 **同一终端与号码** 继续通信（如 **国际漫游**：在国外接入当地运营商网络继续使用）。

---
### 3) Bluetooth — Basics / 蓝牙基础

**Concept & Uses / 概念与用途** 
- Operates in the **2.4 GHz ISM** band; common for keyboards/mice, headsets, speakers, and in-car navigation. Core elements include **versions (1.1/1.2/2.0/2.1/3.0/4.0/5.0)**, **power classes (Class)**, and **profiles (Profile)**. First connection requires entering **pairing mode** and completing **pairing**. Compared with **Wi-Fi**, Bluetooth is typically **one-to-one** and **lower-power** (significantly reduced since **v4.0** / BLE).  

工作在 **2.4 GHz** 频段；常见于键鼠、耳机、音箱、车载导航等。包含 **版本（1.1/1.2/2.0/2.1/3.0/4.0/5.0）**、**功率等级（Class）**、**配置文件（Profile）** 等要素；首次连接需进入 **配对模式** 并完成 **配对**。与 **Wi-Fi** 相比：蓝牙多为 **一对一** 通信，且 **功耗更低**（自 **4.0** 起明显降低）。

**Bluetooth Version Highlights (per slides) / 版本要点（讲义表）**
- **1.1**: First broadly adopted release. **1.2**: Added interference mitigation with **802.11b/g** (adaptive frequency hopping, etc.).
  
  **1.1**：开始普及；**1.2**：增加与 **802.11b/g** 干扰对策（自适应跳频等）。
- **2.0**: Optional **EDR (Enhanced Data Rate)**; data rate up to **3 Mbps**.
  
  **2.0**：可选 **EDR（增强数据速率）**，速率至 **3 Mbps**。
- **2.1**: Simplified pairing and **NFC** support; added **Sniff Subrating** to extend battery life for low-activity devices.
  
  **2.1**：简化配对，支持 **NFC**；加入 **Sniff Subrating** 以延长低活跃设备电池寿命。
- **3.0**: Optional **HS (High Speed)** mode with throughput up to **~24 Mbps**; strengthened power management for energy savings.
  
  **3.0**：可选 **HS（高速）**，速率至 **约 24 Mbps**，并强化电源管理以省电。
- **4.0**: Added **BLE (Bluetooth Low Energy)** for **significantly lower power**; typical PHY rate around **1 Mbps**.
  
  **4.0**：支持 **BLE（低功耗蓝牙）**，**大幅省电**（速率约 **1 Mbps**）。
- **5.0**: PHY rates **2 / 1 / 0.125 Mbps**; the **125 kbps** mode enables **longer range** (e.g., up to **~400 m** in favorable conditions).
  
  **5.0**：速率 **2 / 1 / 0.125 Mbps**，其中 **125 kbps** 对应更长距离（示例：可达 **~400 m** 级别）。

**Power Classes / 功率等级（覆盖范围）**
- Slides example: **100 mW / 10 mW / 1 mW**; higher transmit power generally means **longer range** but **higher energy use**.
  
  讲义示例：**100 mW / 10 mW / 1 mW**；发射功率越高通常**覆盖更远**但**耗电更大**。
- Typical mapping (for reference): **Class 1 ≈ 100 mW (~100 m)**, **Class 2 ≈ 2.5–10 mW (~10 m)**, **Class 3 ≈ 1 mW (~1 m)**.
  
  常见映射（参考）：**Class 1 ≈ 100 mW（~100 m）**、**Class 2 ≈ 2.5–10 mW（~10 m）**、**Class 3 ≈ 1 mW（~1 m）**。
  
**Pairing Flow / 使用流程提示**
- **First pairing**: put the device into **pairing** mode → discover it from the host (phone/PC) → select and **pair** → (if required) enter PIN/passkey → negotiate the target **Profile** (e.g., hands-free headset **HFP**, stereo audio **A2DP**, keyboard/mouse **HID**) → connected.
  
  **首次配对**：将设备置于**配对模式** → 在主机（手机/电脑）中搜索 → 选择并**配对** →（如需）输入 PIN/配对码 → 协商目标**配置文件 Profile**（如免提 **HFP**、立体声 **A2DP**、键鼠 **HID**）→ 连接完成。
  
- **Reconnect**: after the first pairing, devices usually auto-reconnect when in range and Bluetooth is on.
  
  **重新连接**：首次配对后，设备在进入覆盖范围且蓝牙开启时通常会自动重连。
  
- **Tips**: keep only one device in pairing mode to avoid confusion; if the connection fails, delete old pairing records and retry.
  
  **提示**：一次只让一个设备进入配对模式以免混淆；连接异常可先删除旧的配对记录再重试。

---

### 4) Firewall / IDS / IPS / Antivirus
### 防火墙、入侵检测/防御、杀毒

**Firewall (Perimeter Access Control) / 防火墙（边界访问控制）**
- Separates **external (Internet)** and **internal (intranet)** networks, **blocking disallowed traffic** (especially inbound to internal).
  
 将**外部（互联网侧）** 与**内部（内网侧）** 分隔，**阻断不允许的通信**（尤其从外到内）。
- Typical policies: **default deny**, **allowlist**, stateful packet inspection; placed at the network **edge and in front of the DMZ**.
  
  常见策略：**默认拒绝**、**白名单**、**有状态检测**；部署在**网络边界**与 **DMZ 之前**。
- Can filter by **L3/L4 (IP/port/protocol)** and **L7 (application)**, and log events for auditing.
  
 可按 **L3/L4（IP/端口/协议）** 与 **L7（应用）** 过滤，并记录日志用于审计。

**IDS / IPS**
- **IDS (Intrusion Detection System):** detects and **alerts** after observing suspicious activity; **IPS (Intrusion Prevention System):** can **actively block** suspicious traffic.
  
 **IDS（入侵检测系统）：** 检测后**告警**；**IPS（入侵防御系统）：** 可**主动阻断**可疑流量。
- Detection methods include **signature-based** (known patterns) and **anomaly-based**(behavioral/statistical).
  
  检测方式包括**基于特征**（已知特征库）与**基于异常**（行为/统计）。
  
- Deployment: IDS often on a **SPAN/tap (out-of-band)**; IPS **inline** to drop traffic; tune to reduce **false positives/negatives**.
  
 部署：IDS 常接**镜像/分光口（带外）**；IPS **串联在链路上**以丢弃流量；需要调优以降低**误报/漏报**。

**Antivirus (AV) / 杀毒软件**
- **Server-side** (mail/file servers) and **endpoint** (PCs) editions defend against malware at different points.
  
**服务器版**（邮件/文件服务器）与**客户端版**（PC），分别在服务器与终端侧防御恶意代码。
- Engines combine **signatures** + **heuristics** + **behavior monitoring**; keep **definitions/engines updated** and enable **real-time protection**.
  
 引擎结合**特征库** + **启发式** + **行为监控**；保持**病毒库/引擎更新**并启用**实时防护**。
 
- Pair AV with **email/web gateways** and endpoint EDR for layered defense.
  
  配合**邮件/网页网关**与终端**EDR**实现分层防护。

---

### 5) Firewall & DMZ Architecture
### 5) 防火墙与 DMZ 架构

DMZ (Demilitarized Zone) Design
- Segment the network behind the edge firewall into **DMZ** and **Intranet**; minimize exposed services/ports and disable anything unnecessary.
- Typical DMZ hosts: **Web**, **Mail**, **authoritative DNS**—systems that must be reachable from the Internet and thus sit in a higher-risk zone.
- Segmentation principle: if a DMZ server is compromised, strict L3/L4/L7 isolation keeps blast radius **confined to the DMZ**.
- Traffic baselines (tighten per policy):
  - **Internet → DMZ**: allow only required ports (e.g., 80/443, 25/587, 53/UDP).
  - **DMZ → Internet**: allow only what’s needed (updates, upstream APIs) with logging.
  - **Intranet → DMZ**: allow app access to necessary services (via reverse proxy, DB split), least privilege.
  - **DMZ → Intranet**: **deny by default**; if unavoidable, use one-way proxy/message queue/jump host with fine-grained audit.
- Logging & monitoring: integrate **edge FW, WAF/reverse proxy, IDS/IPS, host EDR**, and centralize logs/alerts.

DMZ（非武装区）设计
- 在边界防火墙内侧将网络分为 **DMZ** 与 **内网（Intranet）**；尽量减少对外暴露的服务/端口，关闭所有非必要组件。
- DMZ 常驻主机：**Web**、**邮件（Mail）**、**权威 DNS** 等必须被互联网访问的系统，属于高风险域。
- 分段原则：即使 DMZ 主机被攻陷，严格的三/四/七层隔离也能将影响范围**限制在 DMZ**。
- 访问基线（按策略进一步收敛）：
  - **Internet → DMZ**：仅放行必要端口（如 80/443、25/587、53/UDP）。
  - **DMZ → Internet**：仅放行确有需要的流量（系统更新、上游 API 等），并记录日志。
  - **内网 → DMZ**：按最小权限开放必要服务（经反向代理/数据库拆分等）。
  - **DMZ → 内网**：**默认拒绝**；确需访问时采用单向代理/消息队列/跳板机并细粒度审计。
- 日志与监控：联动 **边界防火墙、WAF/反向代理、IDS/IPS、主机 EDR**，集中化日志与告警。

Text Topology (three-arm: Internet / DMZ / Intranet)
``` 

                 +-------------------+
                 |      Internet     |
                 +---------+---------+
                           |
                      [ Public Router ]
                           |
                    +------+------+
                    |  Edge FW    |  (ACL / NAT / WAF / IPS / Reverse Proxy)
        +-----------+-------------+-------------+
        |           |                           |
     (WAN)       (DMZ)                        (LAN)
        |           |                           |
        |      +----+------------------+        |
        |      |         DMZ           |        |
        |      |  Web / Mail / DNS     |        |
        |      +----+-----------+------+        |
        |           |           |               |
        |        [WAF]       [IDS/IPS]         |
        |                                       |
        |                        +--------------+------------------+
        |                        |            Intranet             |
        |                        |  Apps / DB / File / Directory   |
        |                        |  Default-deny from DMZ          |
        |                        +---------------------------------+

```
```
                 +-------------------+
                 |       互联网       |
                 +---------+---------+
                           |
                        [ 公网路由 ]
                           |
                    +------+------+
                    |  边界防火墙  |  （ACL / NAT / WAF / IPS / 反向代理）
        +-----------+-------------+-------------+
        |           |                           |
      外联口        DMZ口                        内网口
        |           |                           |
        |      +----+------------------+        |
        |      |         DMZ 区        |        |
        |      |  Web / Mail / DNS     |        |
        |      +----+-----------+------+        |
        |           |           |               |
        |        [WAF]       [IDS/IPS]         |
        |                                       |
        |                        +--------------+------------------+
        |                        |            内网（Intranet）     |
        |                        |  业务/数据库/文件/目录等服务     |
        |                        |  自 DMZ 默认拒绝，仅按需放行     |
        |                        +---------------------------------+

```
Notes
- Edge FW typically has three logical/physical interfaces: **WAN / DMZ / LAN**.
- Prefer additional inner policy enforcement (e.g., internal FW or micro-segmentation) between DMZ and Intranet.
- Publish public services through **WAF/reverse proxy** (TLS termination, L7 policies, auditing).
- Follow **default-deny**, **least privilege**, and **observable/traceable** baselines; changes require change-control & dual review.

备注
- 边界防火墙通常具有三条逻辑/物理接口：**外网 / DMZ / 内网**。
- 建议在 DMZ 与内网之间再加一层策略控制（内向防火墙/微分段）。
- 公网发布优先经 **WAF/反代**（终止 TLS、执行七层策略与审计）。
- 遵循 **默认拒绝**、**最小权限**、**可观测可追溯** 的基线；所有变更需走变更管理与双人复核。

> Operational focus: expose ONLY required ports toward the DMZ/Intranet; drop/deny ALL other traffic by default.
> 实践关注：仅开放必要端口到 DMZ/内网；其余全部默认丢弃/拒绝。

---

### 6) IDS/IPS: Signature vs Anomaly — Two Main Detection/Prevention Methods
### IDS/IPS：特征匹配（Signature-based） vs 异常检测（Anomaly-based）—— 入侵检测/防御两大方法

- **Signature-based:**
  **特征匹配（Signature-based）：**
- Match traffic against known attack **signatures/patterns**; **on match → alert or block**.
  将流量与已知攻击的**特征/模式**进行匹配；**匹配时 → 告警或阻断**。
- **Pros**: High accuracy for known threats.
  **优点**：对已知威胁命中率高。
- **Limits**: Weak against **novel/zero-day** attacks; requires frequent signature updates.
  **限制**：对**新型/零日攻击**识别能力弱；需要频繁更新签名库。
- **Anomaly-based:**
  **异常检测（Anomaly-based）：**
- Build a baseline of normal behavior and flag deviations → alert or block.
  以**正常行为/流量**建立基线并检测偏离 → **告警**或**阻断**。
- **Pros:** Can surface previously **unknown** attacks.
  **优点：** 能够发现先前**未知**的攻击。
- **Limits:** Baseline tuning is hard; mis-tuning leads **to false positives/negatives**.
  **限制：** 基线调优困难；调优不当会**导致误报/漏报**。
- **Combined use:** Deploy both to balance coverage and precision; correlate results for better efficacy.
  **组合使用：** 联合部署两种方法以平衡覆盖面与精度；通过关联分析提升效果。

---
### 7) VPN & IPsec 虚拟专网与安全机制
**Why VPN is Needed / 为何需要 VPN**
- **Traditional leased lines** prevent data leakage but **are expensive**; a **VPN** carries private traffic over the **public Internet** to **reduce cost**, while **confidentiality** and **integrity** are ensured via **tunneling** plus **encryption/authentication**.
  传统专线可防泄漏但成本高 → 通过**互联网**承载的**虚拟私网（VPN）以降低成本**，**同时靠隧道（tunneling）与加密/认证**保证机密性/完整性。
  
**Core Technologies / 核心技术**
- **Tunneling** (encapsulation) + **Encryption/Authentication**.
  **Tunneling**（封装）+ **Encryption/Authentication**（加密/认证）。
- Example framework: **IPsec (Security Architecture for IP)**.
  示例框架：**IPsec（IP 安全体系结构，Security Architecture for IP）**。

**Two IPsec Modes: Transport vs Tunnel**
**两种模式：Transport（传输模式）与 Tunnel（隧道模式）**

- **Transport Mode / Transport（传输模式）**：
  - **Only the L4 header (TCP/UDP) and payload** are protected by ESP; the **original IP header stays in clear** (not encrypted). As a result, you **cannot detect tampering of the outer IP header** with ESP alone. *(AH could add header integrity, but is rarely used due to NAT issues.)*
    **仅传输层头（TCP/UDP）与数据**由 ESP 保护；**原始 IP 头保持明文**（未加密）。因此，仅用 ESP 时**无法检测外层 IP 头是否被篡改**。*（可用 AH 增加 IP 头完整性校验，但因与 NAT 不兼容而较少部署。）*
    
- **Tunnel Mode / Tunnel（隧道模式）**：
  - Encapsulate the **entire inner IP packet** via the **VPN router**; the **IP header is encrypted/protected as well**, therefore **tampering of the IP header can be detected**.
    通过**VPN 路由器**将**内层 IP 包**整体封装；**连同 IP 头也被加密/保护**，因此能**检测 IP 头篡改**。
    
**ASCII Sketch (abstract) / 图示（抽象示意）**
```
Transport Mode

[ IP | TCP/UDP | Data ] → encrypt {TCP/UDP | Data}; IP header remains in clear.
[ IP | TCP/UDP | Data ] → 仅加密 {TCP/UDP | Data}；IP 头保持明文。

Tunnel Mode

Inner: [ IP_in | TCP/UDP | Data ]
Outer: [ IP_out | ESP/AH | (Encrypted Inner Packet) ]
内层： [ IP_in | TCP/UDP | Data ]
外层： [ IP_out | ESP/AH | （加密后的内层数据包）]
```
> Lecture note: In **Tunnel mode**, the **IP header is protected**; in **Transport mode**, the **original IP header is not protected** (left in clear).
> 讲义明确：在**隧道模式**中，**IP 头也能得到保护**；在**传输模式**中，**IP 头本身不被保护**（保持明文）。

---

### 8) Proxy / Reverse Proxy 代理与反向代理

**Forward Proxy（正向代理）**  
- Used by **internal clients** to access the **external Internet** via a proxy; origins on the Internet see the **proxy’s IP**, not the client’s.  
  由**内网客户端**经 **代理服务器** 访问 **外部网站**；外部仅看到**代理的 IP**，看不到内网终端的真实 IP。  
- Purposes: **Security** (hide internal IPs) / **Caching** (reuse fetched content) / **User authentication** (allow only authorized users) / **Filtering** (block sites/categories).  
  目的：“**安全**”（隐藏内部地址）/“**缓存**”（复用已取内容，提速省带宽）/“**用户认证**”（仅允许通过认证的用户上网）/“**过滤**”（按策略限制访问某些站点/类别）。

**Reverse Proxy（反向代理）**  
- External clients connect to the **reverse proxy**, which **handles/forwards** requests to backend web servers; clients **don’t reach** backends directly.  
  由**外部客户端**访问**反向代理**，由其**代替后端 Web 服务器**处理/转发请求；外部**不直接**接触后端。  
- Benefits: **Shield backends** (hide topology) / **SSL termination/offload** / **Unified ingress** (access control, WAF, load balancing).  
  好处：**保护后端**（隐藏具体服务器/结构，降低被直接攻击的机会）/ **SSL 终止/卸载**（反代承担 TLS 握手与加解密）/ **统一接入**（可做访问控制、WAF、负载分担）。
  
**Text topology diagrams / 文字拓扑示意**
```
Forward Proxy:
 Client → Proxy → Internet (Web Servers)

Reverse Proxy:
 Internet (Clients) → Reverse Proxy → Internal Web Servers
```
```
正向代理（Forward Proxy）：
 客户端 → 代理服务器 → 互联网（Web 服务器）

反向代理（Reverse Proxy）：
 互联网（客户端）→ 反向代理 → 内部 Web 服务器

```

---

## Key Points 

- **RTS/CTS** uses **CTS/ACK** “coverage announcements” so **hidden terminals** know the medium is busy and avoid collisions.
  **RTS/CTS** 通过 **CTS/ACK** 的“覆盖宣告”让**隐藏终端**知晓占用，从而回避碰撞。
- **Handover** = seamless **AP/base-station switch** within the same network; **Roaming** = keeping service across **different operators**.
  **Handover**＝同网内**AP/基站切换**不断线；**Roaming**＝跨**运营商网络**延续同一终端/号码通信。
- **Bluetooth**: versions (1.1→5.0), **Class (power/range)**, **Profiles & pairing**; more power-efficient and typically one-to-one vs **Wi-Fi**.
  **Bluetooth**：版本演进（1.1→5.0）、**Class 功率/范围、Profile 与配对**；相较 **Wi-Fi** 更省电，通常为一对一。
- **Firewall / IDS / IPS / Antivirus**: perimeter blocking, detect/prevent intrusions, and malware defense; **DMZ** hosts outward-facing services, isolated from the intranet.
  **Firewall / IDS / IPS / Antivirus**：边界拦截、入侵检测/防御与恶意代码防护；**DMZ** 放置对外服务并与内网隔离。
- **Signature vs Anomaly (IDS/IPS)**: signature excels at **known** threats but needs updates; anomaly detects **unknowns** but needs baselines and handles false positives—**use both**.
  **签名法 vs 异常法（IDS/IPS）**：签名法擅长**已知威胁**但需持续更新；异常法可发现**未知异常**但需基线并权衡误报——**组合更佳**。
- **VPN (IPsec)**: **Transport mode** does **not** protect the IP header; **Tunnel mode** protects **including** the IP header; both rely on **tunneling + encryption/authentication**.
  **VPN（IPsec）**：**传输模式**不保护 IP 头；**隧道模式**连同 IP 头也受保护；二者均依赖**隧道 + 加密/认证**。
- **Proxy / Reverse Proxy**: forward proxy for **egress control, caching, auditing**; reverse proxy for **edge protection, SSL offload, unified entry**.
  **正向代理 / 反向代理**：正向代理侧重**出网控制、缓存、审计**；反向代理侧重**入口防护、SSL 卸载、统一接入**。

---
## ※※ Supplementary Cheat Sheets | 速查单

### WLAN & VPN Quick Reference
- [RTS/CTS Timeline | RTS/CTS 时序速查](./figs/lecture14_rts_cts_timeline.md)  
  *隐藏终端问题与 RTS/CTS 时序解决方案*

- [VPN Modes & IPsec | VPN 模式与 IPsec 速查](./figs/lecture14_vpn_modes_ipsec.md)  
  *传输模式/隧道模式、IPsec 组件与报文结构*

<h2></h2>

[← Previous Lecture / 上一讲](./lecture13.md) · [Next Lecture / 下一讲 →](./lecture15.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

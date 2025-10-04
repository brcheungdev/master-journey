[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 13: TCP Flow & Congestion Control, UDP, Wireless LAN (802.11), CSMA/CA  
# 第13讲：TCP 流量与拥塞控制、UDP、无线局域网（802.11）、CSMA/CA

---

## ⚪ Lecture Overview

- **TCP Flow Control**: Receiver advertises its **Window** (16-bit) — the bytes it can accept; the sender rate-limits accordingly.  
  **TCP 流量控制**：接收端通过 **Window（16 位）** 通告可接收的字节数，发送端据此限速。
- **TCP Header & Flags**: Header fields (ports, **SEQ/ACK**, **Window**, **Checksum**, **Urgent Pointer**, **Options**) and control bits **CWR/ECE/URG/ACK/PSH/RST/SYN/FIN**.  
  **TCP 首部与控制位**：首部字段（端口、**SEQ/ACK**、**Window**、**Checksum**、**Urgent Pointer**、**Options**）与控制位 **CWR/ECE/URG/ACK/PSH/RST/SYN/FIN**。
- **TCP Congestion Control**: **cwnd**, **ssthresh**; **Slow Start**, post-**Timeout** threshold reduction; window adjustment under **Fast Retransmit**; contrast with handling under normal timeout-based retransmission.  
  **TCP 拥塞控制**：**cwnd**、**ssthresh**；**慢启动（Slow Start）**，**超时（Timeout）** 后阈值下降；**快速重传（Fast Retransmit）** 下的窗口调整；与常规超时重传的处理对比。
- **UDP**: Connectionless, no retransmission/congestion control, lightweight header; differences from **TCP** and typical use cases.  
  **UDP**：无连接、无重传/拥塞控制、首部简洁；与 **TCP** 的差异及适用场景。
- **Wireless LAN (802.11)**: Standard evolution (**a/b/g/n/ac/ax** with rates/bands/MIMO), characteristics (pros/cons, interference), and **public Wi-Fi threats & countermeasures** (WPA2/WPA3, refusing unknown APs).  
  **无线局域网（802.11）**：标准演进（**a/b/g/n/ac/ax** 的速率/频段/MIMO），特性（优缺点与干扰），以及 **公共无线网的威胁与对策**（WPA2/WPA3、拒绝连接未知 AP）。
- **WLAN Frame & Modulation**: **PLCP** preamble/header, **PSDU**; EtherType examples **0x0800/0x0806/0x86DD**; modulation schemes **PSK/FSK/CCK/QAM**.  
  **WLAN 帧结构与调制**：**PLCP** 前导码/头、**PSDU**；以太类型 **0x0800/0x0806/0x86DD**；调制方式 **PSK/FSK/CCK/QAM**。
- **Access Modes & Medium Access**: **Infrastructure vs Ad-hoc**; **CSMA/CA** with **DIFS/SIFS/ACK/Backoff** timing.  
  **接入模式与介质访问**：**基础设施模式 vs 自组网（Ad-hoc）**；**CSMA/CA** 机制与 **DIFS/SIFS/ACK/Backoff** 时序。 

---

## ⚪ Lecture Content 

### 1) TCP Flow Control — Receive Window  
### TCP 流量控制：接收端窗口

**Purpose**: Prevent **receiver buffer overflow**. The receiver advertises how many more bytes it can accept in the **ACK’s TCP header Window field (16 bits, measured in bytes)**. The sender limits the total **in-flight, unacknowledged data** to that amount: a larger window ⇒ more segments can be sent back-to-back; a smaller window ⇒ the sender must slow down.

**目的**：防止**接收缓冲溢出**。接收端在 **ACK** 的 **TCP 头 Window 字段（16 bit，以字节为单位）**中通告自己还能接收的字节数，发送端据此限制“飞行中未确认数据”的总量。**窗口变大** → 可连续发送更多段；**窗口变小** → 需收敛发送量。

**Operational notes / 运行要点**
- **Sender limit（发送侧上限）**:  
  In-flight bytes must satisfy `in_flight ≤ min(advertised_window, cwnd)`.  
  在任意时刻需满足 `在途字节数 ≤ min(对端通告窗口, 拥塞窗口cwnd)`。
- **Zero window & probes（零窗口与探测）**:  
  If the receiver advertises **0**, the sender pauses and periodically sends **Zero-Window Probes (ZWP)** to learn when space becomes available.  
  若接收端通告为 **0**，发送端暂停并周期性发送**零窗口探测**以获知何时可恢复发送。
- **Window scaling（窗口扩大选项）**:  
  The 16-bit field caps at **65,535 bytes**; with **Window Scale (RFC 7323)** negotiated at SYN, the effective window can be enlarged for high BDP paths.  
  16 位字段上限 **65,535 字节**；若在握手时协商**窗口扩大（RFC 7323）**，可在大带宽时延路径上放大有效窗口。
- **Avoid tiny updates（避免过小窗口）**:  
  Receivers typically avoid advertising tiny increases to prevent **silly window syndrome**.  
  接收端通常避免通告很小的增量，以防**愚蠢窗口综合征（SWS）**。

```
Receiver: advertises Window in ACK  →  Sender: limit in-flight bytes ≤ min{rcv_wnd, cwnd}
```
> **Note**: This is **end-to-end flow control**, independent of but concurrent with the network-side **congestion control** (discussed later).
> **注**：这是**端到端**的**流量控制**，与网络侧的**拥塞控制**（后述）相互独立但同时生效。


### 2) TCP Header & Control Flags / TCP 首部与控制位

**Fixed header length (minimum)**: **20 bytes (5 × 32-bit words)**  
**固定首部最小长度**：**20 字节（5×32bit 词）**
**Key fields**  
- **Src Port (16b), Dst Port (16b), Sequence Number (32b), Acknowledgment Number (32b), Header Length (Data Offset), Flags (8b), Window (16b), Checksum (16b), Urgent Pointer (16b), Options/Padding**.  
- **源端口（16b）、目的端口（16b）、序号（32b）、确认号（32b）、首部长度（数据偏移）、控制位（8b）、窗口（16b）、校验和（16b）、紧急指针（16b）、选项/填充**。
**Control flags (each 1 bit)**  
- `CWR, ECE, URG, ACK, PSH, RST, SYN, FIN`.  
- `CWR（拥塞窗口已减少）、ECE（显式拥塞回显）、URG（紧急）、ACK（确认）、PSH（推送）、RST（复位）、SYN（同步/建连）、FIN（结束/断连）`。

```
| SrcPort | DstPort |
|               Sequence Number               |
|             Acknowledgment Number           |
| HLen |Res| Flags |        Window Size       |
|        Checksum        |     Urgent Ptr     |
| Options ...            | Padding |   Data   |
```

### 3) TCP Congestion Control — cwnd / ssthresh & State Changes
**Idea:** The network may already be congested. To reduce loss and retransmissions, the sender maintains a **congestion window (`cwnd`)** and enforces **` inflight ≤ min{rcv_wnd, cwnd}`**. A **slow-start threshold (`ssthresh`)** separates **Slow Start** from **Congestion Avoidance**.
### TCP 拥塞控制：拥塞窗口 / 阈值与状态变化
**思想：** 网络可能已处于拥塞状态。为减少丢包与重传，发送端维护**拥塞窗口 `cwnd`**，并以 **`inflight ≤ min{rcv_wnd, cwnd}`** 为约束；同时设置**慢启动阈值 `ssthresh`**，用于划分**慢启动**与**拥塞避免**两个阶段。

**(A) Connection Start: Slow Start（慢启动）**
- Initialize `cwnd = 1 MSS`; on each **ACK**, grow **exponentially** (approximately **doubling per RTT**).
- 初始 `cwnd = 1 MSS`；每收到**一个 ACK**，指数式增长（约每**RTT 翻倍**）。
- Actual sending is limited by `min{rcv_wnd, cwnd}`; **ssthresh** is not explicitly set yet (or is effectively large depending on implementation).
- 实际发送受 `min{rcv_wnd, cwnd}` 限制；此时 **ssthresh** 尚未设定具体值（或视实现为很大）。

**(B) Timeout Occurs（超时发生）**
- Treat as severe congestion: set **ssthresh ← cwnd/2** (half of the current cwnd), set **cwnd ← 1 MSS**, and return to **Slow Start**.
- 认为网络严重拥塞：将 **ssthresh ← cwnd/2**（当时的 cwnd 一半），将 **cwnd ← 1 MSS**，并回到 **慢启动（Slow Start）**。
  
**(C) Fast Retransmit — Post-Recovery Handling (different from Timeout) / 高速再送 — 恢复后的处理（与 Timeout 不同）**
- If only **duplicate ACKs** are observed (ACKs still arrive, so the network isn’t fully partitioned), treat it as **milder congestion**.
- 若仅发生**重复 ACK**（还能收到 ACK，说明网络未完全阻断），按**拥塞较轻**处理。
  - **ssthresh** is set to a prior threshold (slides describe “**ssthresh + 3 segments and then linear increase**”): after **Fast Retransmit** triggers, the sender uses approximately **ssthresh + 3 × MSS** as a temporary window, then grows **linearly by +1 MSS per RTT** (Congestion Avoidance).
  - **ssthresh** 设置为之前的某阈值（讲义表述为“**ssthresh + 3 段发送并线性增大**”）：在触发**快速重传**后，发送端以 **ssthresh + 3 × MSS** 近似作为临时窗口，随后**按每 RTT 线性 +1 MSS** 的方式增长（拥塞避免）。
  - Unlike (B) **Timeout**, do **not** cut **cwnd** back to **1 MSS**; instead keep sending at a reduced rate and **increase linearly** thereafter.
  - 与 (B) **Timeout** 不同：**不把 cwnd 砍回 1 MSS**，而是以较低速率继续发送，并在之后**线性增大**。
  
**(D) Regular Timeout Retransmission (no ACKs reachable) / 常规超时重传（无 ACK 可达）**

- Treat this as **severe congestion**: set **cwnd ← 1 MSS**, enter **exponential Slow Start**, and when `cwnd > ssthresh`, switch to **linear Congestion Avoidance** (+1 MSS per RTT).
- 视为**强拥塞**：将 **cwnd ← 1 MSS**，进入**指数慢启动**；当 `cwnd > ssthresh` 后，转入**线性拥塞避免**（每 RTT **+1 MSS**）。

Summary / 小结
**Fast Retransmit** is the “gentler” path, while **Timeout** is a “reset-and-restart” path. Together with `ssthresh`, they implement **AIMD (Additive Increase, Multiplicative Decrease)** behavior.
**Fast Retransmit** 路径相对“更温和”，**Timeout** 路径则“归零再起”。两者配合 `ssthresh` 形成 **AIMD（加性增大、乘性减小）** 行为。


### 4) UDP — Service & Header vs TCP  
### UDP 与 TCP 的差异与头部
**UDP Features**  
- **Connectionless, no retransmission, no congestion control** → low overhead and latency; suitable for **DNS, SNMP** (small control flows), **voice/video** (latency-sensitive), **intra-LAN** apps, and **multicast/broadcast**.  
- **无连接、无重传、无拥塞控制 → 开销小、时延低；适于 DNS、SNMP** 等小量控制流，以及 **语音/视频** 等对时延敏感业务、**LAN 内部**专用应用、**多播/广播** 等。
**UDP Header (minimal, 4 fields)**  
- `Src Port (16b), Dst Port (16b), Length (16b), Checksum (16b)` — minimal header.  
- `Src Port(16b)、Dst Port(16b)、Length(16b)、Checksum(16b)` —— 头部极简。
**UDP vs TCP (side-by-side)**  
- **Connection setup/teardown** — **UDP: none**; **TCP: 3-way handshake / 4-way close**, inefficient for tiny transfers.  
  **建立/释放连接** —— **UDP 无需**；**TCP 三次握手/四次挥手**，对“小数据”低效。  
- **Ordering & reliability** — **UDP** does **not** guarantee order or delivery; **TCP** provides sequencing, ACK, retransmission, flow & congestion control.  
  **有序与可靠** —— **UDP 不保证顺序与到达**；**TCP 提供顺序/确认/重传/流量与拥塞控制**。  
- **Typical protocols** — TCP: **HTTP/FTP/SMTP/POP/TELNET/SSH**; UDP: **DNS/DHCP**.  
  **典型协议** —— TCP（**HTTP/FTP/SMTP/POP/TELNET/SSH**），UDP（**DNS/DHCP**）。


### 5) Wireless LAN (802.11) — Standards & Features 无线 LAN 标准与特性
**Standards & Peak Rates (Examples) / 标准与峰值速率（示例）:**
- 802.11（2.4 GHz, 2 Mbps, 1997）
- **11a**（5 GHz, **54 Mbps**, 1999）
- **11b**（2.4 GHz, **11 Mbps**, 1999）
- **11g**（2.4 GHz, **54 Mbps**, 2003）
- **11n**（2.4/5 GHz, **600 Mbps**, 2009；**SU-MIMO**）
- **11ac**（5 GHz, **6.9 Gbps**, 2014；**SU-MIMO**）
- **11ax**（2.4/5 GHz, **9.6 Gbps**, 2014；**MU-MIMO**）
**Coverage & Pros/Cons / 覆盖范围与优缺点**

- Typical coverage is **30–100 m**; no cabling needed, mobile and flexible, supports roaming.
  典型覆盖 **30–100 m**；无需布线、移动灵活、可实现漫游。
- Cons: Susceptible to eavesdropping (encryption required); multiple APs with overlapping channels cause **throughput degradation**; the **2.4 GHz** band suffers interference from **microwave ovens** and other devices, leading to instability or disconnections.
  缺点：易被窃听（需加密）；多 AP/信道重叠会导致**吞吐下降**；**2.4 GHz** 频段与**微波炉**等同频干扰，易出现不稳定或断连。
- Mitigation, optional: Prefer WPA2/WPA3, plan channels (1/6/11 in 2.4 GHz), and use 5/6 GHz to reduce interference.
  缓解建议，可选：优先使用 WPA2/WPA3，进行信道规划（2.4 GHz 选 1/6/11），并尽量使用 5/6 GHz 以降低干扰。

### 6) Security in Public WLAN / 公共无线网络的威胁与对策

- Eavesdropping / 通信窃听
  If the wireless link is unencrypted, traffic can be sniffed. 
      Mitigation: Prefer **WPA2-AES / WPA3**; avoid WEP/WPA (weak/obsolete). Use end-to-end encryption (HTTPS/SSH/VPN) even on encrypted Wi-Fi.
  无线段未加密时，通信内容可能被嗅探。
      对策：优先使用 **WPA2-AES / WPA3**；禁用 WEP/WPA（弱/过时）。即使在加密 Wi-Fi 上，也尽量使用端到端加密（HTTPS/SSH/VPN）。
- Unauthorized Access / 不正访问
  Attackers may access the network from a legitimate device to steal data.
      Mitigation: Lock your device when unattended; disable sharing services; use a host firewall; keep OS and patches up-to-date.
  攻击者可能借合法主机入网窃取信息。
      对策：离开时锁定设备；关闭不必要的共享服务；启用主机防火墙；及时更新系统补丁。
- Impersonation (Spoofing) / なりすまし（伪装/冒名）
  Stolen credentials or session cookies allow attackers to impersonate users.
      Mitigation: Use MFA where possible; ensure HTTPS with a correct certificate; avoid captive-portal reuse of passwords; clear cookies on shared PCs.
  被窃取的账号口令或会话 Cookie 可能被用来冒充用户。
      对策：尽量启用多因素认证；确认 HTTPS 证书正确；避免在门户页复用重要密码；公共电脑用后清理 Cookie。
- Evil Twin / Rogue AP / 恶意或伪造 AP
  Attackers set up a fake AP to lure users and steal credentials.
      Mitigation: **Do not connect to unknown APs**; verify SSID and certificate on enterprise Wi-Fi; prefer personal hotspots or trusted networks; use a VPN on public Wi-Fi.
  攻击者搭建假 AP 引诱用户连接并窃取账号口令。
      对策：**不要连接不明 AP**；企业网下核对 SSID 与证书；优先使用个人热点或受信网络；在公共 Wi-Fi 上使用 VPN。


### 7) MIMO — SU vs MU / 多输入多输出：单用户与多用户

- **SU-MIMO (Single-User MIMO)**
  Multiple antennas serve **one** client at a time (more spatial streams to a single STA).
  多根天线在同一时刻仅服务**单个主机**（把多个空间流集中给一台终端）。
- **MU-MIMO (Multi-User MIMO)**
  With beamforming, multiple antennas serve **multiple** clients **simultaneously** (different spatial streams per STA).
  借助波束赋形等技术，使用多根天线**同时**为**多个主机**发送（每台主机分配不同的空间流）。
- **Spatial Streams & Throughput / 空间流与吞吐**
  The AP splits data into several **spatial streams** and transmits them concurrently from multiple antennas; the receiver separates and **reconstructs** mixed signals. **More antennas/streams → higher potential throughput** (channel conditions permitting).
  AP 将数据拆分为多个**空间流**，由多天线**并发发送**；接收端对“混合”信号进行**分离重构**。在信道条件允许下，**天线/空间流越多 → 潜在吞吐越高**。
  
> Note / 备注：MU-MIMO 在 802.11ac 主要用于**下行**，802.11ax 进一步增强（含上行/下行、多用户调度与 OFDMA 协同）。实际增益还受 **SNR、相关性、用户分布、调度算法** 等因素影响。


### 8) 802.11 Frame & EtherType 无线帧结构与类型
- **PLCP Preamble:** At the very beginning of the frame, used for PHY synchronization and channel acquisition. 
  **PLCP 前导码：** 位于帧首，用于物理层同步与信道获取。
  
- **PLCP Header:** Carries PHY parameters such as modulation/coding scheme, data rate, and PSDU length.  
  **PLCP 头：** 携带物理层参数，如调制/编码方式、数据速率与 PSDU 长度。【**含调制方式/速率、数据长**等物理层信息。】

- **PSDU:** The payload delivered to the PHY, consisting of the 802.11 MAC header plus upper-layer data.  
  **PSDU：** 交付给物理层的负载，由 802.11 MAC 头与上层业务数据组成。【由**802.11 MAC 头 + 业务数据**组成（数据链路层附加）。】

- **Type (EtherType):** Identifies the upper-layer protocol carried in the payload. Common values:  
  **Type（以太类型号）：** 指示上层协议：`0x0800 IPv4`, `0x0806 ARP`, `0x86DD IPv6`。  

### 9) Modulation Methods / 调制方式

- **PSK / FSK:** Used in 802.11 as foundational schemes (Phase-Shift Keying / Frequency-Shift Keying).  
  **PSK / FSK：** 用于 802.11 的基础调制（相移键控 / 频移键控）。
- **CCK (Complementary Code Keying):** Employed by 802.11b (and compatible use in 11g for legacy rates) to encode multiple bits per symbol with complementary codes.  
  **CCK（补码键控）：** 被 802.11b 采用（11g 兼容低速率）；利用互补码实现每符号多比特编码。【11b/11g 使用的**补码键控**。】
- **QAM (Quadrature Amplitude Modulation):** Used by 11a/11g/11n/11ac/11ax; higher-order mappings (e.g., 16/64/256-QAM, even 1024-QAM in 11ax) deliver higher throughput at the cost of higher SNR requirements.  
  **QAM（正交振幅调制）：** 由 11a/11g/11n/11ac/11ax 采用；更高阶映射（如 16/64/256-QAM，11ax 甚至 1024-QAM）可提升吞吐，但需要更高的信噪比。【11a/11g/11n/11ac/11ax 使用的**正交振幅调制**（更高阶映射带来更高吞吐）】

### 10) Infrastructure vs Ad-hoc / 基础设施模式 与 自组网模式

- **Infrastructure Mode:** Stations communicate **through an AP (Access Point)**; the AP bridges traffic to the wired LAN, supports association/roaming, and centralizes security (WPA2/WPA3). Best for managed WLANs.  
  **基础设施模式：** 各终端通过**AP（接入点）** 转发通信；AP 可桥接到有线网络，支持关联/漫游，并集中实施安全（WPA2/WPA3）。适合受管的企业/校园 WLAN。
- **Ad-hoc (IBSS):** Stations **talk directly peer-to-peer** without an AP; in some setups a client may **relay** frames for others. Simple and quick to form, but **limited scalability**, weaker coordination/QoS, and security is often looser.  
  **自组网（IBSS）：** 终端之间**直接通信**，无 AP；在部分场景下客户端可**中继**他人流量。组网简便，但**规模与性能受限**、协调/QoS 较弱，安全性通常也更低。


### 11) CSMA/CA — Access Method for WLAN
### 无线局域网的介质访问（CSMA/CA）
**Key idea:** Similar to Ethernet’s **CSMA/CD** but **no collision detection** on radio (can’t transmit and listen reliably at once), so WLAN uses **collision avoidance**.  
**要点：** 与以太网的 **CSMA/CD** 类似，但无线端**无法边发边听进行冲突检测**，因此采用**冲突回避**。
- Before sending, sense the medium; if idle, wait a random backoff, then transmit.  
  发送前先监听信道；若空闲，等待一个随机退避时间后再发送。
- On successful reception, the receiver sends an ACK after a SIFS
  接收端成功收到数据后，在 SIFS 之后发送 ACK 确认。
- The next contender must wait a DIFS and perform backoff before attempting.
  下一位发送者必须等待 DIFS 并执行退避后再竞争发送。
  
**Timing (text sketch) / 时序（文字示意）**  

```
A finishes → (DIFS sensing) → A backoff & send DATA
AP receives → (SIFS) → AP sends ACK
Then B → (DIFS sensing) → B backoff & send DATA → ...
```
- **DIFS**：Distributed Inter-Frame Space（分布式帧间间隔）
- **SIFS**：Short Inter-Frame Space（短帧间间隔）
- **ACK** ：Acknowledgment frame （确认帧）


---
## Key Points

- **TCP Flow Control**
  - The receiver advertises its **Window** (bytes it can accept), and the sender limits in-flight data accordingly.
  - 接收端通过 **Window** 通告可接收字节数，发送端据此限制**在途数据量（in-flight）**。
- **TCP Congestion Control**
  - **Slow Start** grows cwnd exponentially; on **timeout** reset to `cwnd = 1`. After **Fast Retransmit**, grow **linearly**; **ssthresh** separates exponential (slow start) and linear (avoidance) phases.
  - **慢启动**指数增长；**超时**回落到 `cwnd = 1`。**快速重传**后改为**线性增加**；**ssthresh** 将**指数阶段**与**线性阶段**分界。
- **UDP**
  - Lightweight and low latency; good for DNS/multimedia/broadcast/multicast/private LAN uses; no ordering or reliability guarantees.
  - 轻量低时延，适用于 DNS、音视频、多播/广播、专网等；**不保证有序与可靠**。
- **WLAN**
  - Know standards/bands/rates and **(MU-)MIMO**; use strong encryption; beware **rogue APs**; **2.4 GHz interference** can reduce throughput or drop links.
  - 关注标准/频段/速率与 **(MU-)MIMO**；开启强加密；警惕**伪造 AP**；**2.4 GHz 干扰**会降吞吐或断连。
- **CSMA/CA**
  - Avoids collisions using **DIFS/SIFS/ACK/Backoff**; no collision detection like Ethernet.
  - 通过 **DIFS/SIFS/ACK/Backoff** 进行**冲突回避**；不像以太网那样具备**碰撞检测**能力。

---

## ※※Supplementary Cheat Sheets | 速查单

### TCP & CSMA/CA Quick Reference
- [TCP Congestion Control | TCP 拥塞控制速查](./figs/lecture13_tcp_cwnd_ssthresh.md)  
  *TCP 拥塞窗口、慢启动、拥塞避免与快速重传处理*

- [CSMA/CA Timing | CSMA/CA 时序速查](./figs/lecture13_csma_ca_timing.md)  
  *CSMA/CA DIFS/SIFS/ACK/Backoff 时序机制与碰撞回避*


<h2></h2>

[← Previous Lecture / 上一讲](./lecture12.md) · [Next Lecture / 下一讲 →](./lecture14.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

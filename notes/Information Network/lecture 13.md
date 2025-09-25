#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 13: TCP Flow & Congestion Control, UDP, Wireless LAN (802.11), CSMA/CA  
# 情報ネットワーク概論 第13回：TCPのフロー／輻輳制御・UDP・無線LAN・CSMA/CA

---

## ⚪ Lecture Overview 
- **TCP Flow Control（流量控制）**：接收端通过 **Window**（16 bit）通告可接收的字节数，发送端据此限速。  
- **TCP Header & Flags**：首部字段（端口、SEQ/ACK、Window、Checksum、Urgent Pointer、Options）与 **CWR/ECE/URG/ACK/PSH/RST/SYN/FIN** 控制位。  
- **TCP Congestion Control（拥塞控制）**：**cwnd**、**ssthresh**；**Slow Start**、**Timeout** 后降阈；**Fast Retransmit** 下的窗口调整；与**常规超时重传**下的不同处理。  
- **UDP**：无连接、无重传/拥塞控制、头部简洁；与 **TCP** 的差异与适用场景。  
- **Wireless LAN (802.11)**：标准演进（a/b/g/n/ac/ax，速率/频段/MIMO）、特性（优缺点、干扰）、**公共无线网威胁与对策**（WPA2/WPA3、拒绝连接未知 AP）。  
- **WLAN 帧结构与调制**：PLCP 前导码/头、PSDU；Type(EtherType) 0x0800/0x0806/0x86DD；PSK/FSK/CCK/QAM。  
- **接入模式与介质访问**：**Infrastructure vs Ad-hoc**；**CSMA/CA** 机制与 **DIFS/SIFS/ACK/Backoff** 时序。 

---

## ⚪ Lecture Content 

### 1) TCP Flow Control — Receive Window  TCP 流量控制：接收端窗口
**目的**：防止**接收缓冲溢出**。接收端在 **ACK** 的 **TCP 头 Window 字段（16 bit，字节为单位）**中通告自己还能接收的量，发送端据此限制“飞行中未确认数据”的总量。窗口变大 → 可连续发送更多段；变小 → 需收敛发送量。  
```
Receiver: advertises Window in ACK  →  Sender: limit in-flight bytes ≤ min{rcv_wnd, cwnd}
```
注：这是**端到端**的**流量控制**，与网络侧的**拥塞控制**（后述）独立但同时生效。

### 2) TCP Header & Control Flags TCP 首部与控制位
**固定首部长度**：最少 **20 字节（5×32bit）**；<br/>
关键字段：
- **Src/Dst Port（各16b）、Sequence#（32b）、ACK#（32b）、HeaderLen、Flags（8b）、Window（16b）、Checksum（16b）、Urgent Pointer（16b）、Options/Pad**。
**控制位（各1 bit）**：`CWR, ECE, URG, ACK, PSH, RST, SYN, FIN`。
```
| SrcPort | DstPort |
|               Sequence Number               |
|             Acknowledgment Number           |
| HLen |Res| Flags |        Window Size       |
|        Checksum        |     Urgent Ptr     |
| Options ...            | Padding |   Data   |
```

### 3) TCP Congestion Control — cwnd / ssthresh & State Changes
**TCP 拥塞控制：拥塞窗口/阈值与状态变化**
**思想**：网络可能已拥挤，为减少丢包与重传，发送端维护**拥塞窗口**cwnd，以`inflight ≤ min{rcv_wnd, cwnd}`为约束。另有**慢启动阈值 ssthresh**划分慢启动与拥塞避免阶段。

**(A) 连接开始：Slow Start（慢启动）**
- 初始`cwnd = 1 MSS`；每收到**一个 ACK**，指数式增长（约每**RTT 翻倍**）。
- 实际发送受`min{rcv_wnd, cwnd}`限制；此时**ssthresh**尚未设定具体值（或视实现为很大）。
**(B) Timeout（超时）发生**
- 认为网络严重拥塞：将**ssthresh ← cwnd/2**（当时的一半），**cwnd ← 1 MSS**，回到**慢启动**。
**(C) Fast Retransmit / 高速再送后的处理（与 Timeout 不同）**
- 若仅发生**重复 ACK**（能收 ACK，说明网络未完全阻断），按“拥塞较轻”处理：
  - **ssthresh**设置为之前的某阈值（讲义表述为“ssthresh + 3 段发送并线性增大”）：在触发快速重传后，发送端以**ssthresh + 3×MSS**近似作为临时窗口，随后**按每 RTT 线性+1 MSS**方式增长（拥塞避免）。
  - 与 (B) 不同：**不把 cwnd 砍回 1**，而是继续在较低速率下**线性增大**。
**(D) 常规超时重传（无 ACK 可达）**
- 视为强拥塞：**cwnd ← 1 MSS**，**指数慢启动**，当`cwnd > ssthresh`后转入**线性拥塞避免**（+1 MSS/RTT）。

小结：**Fast Retransmit**路径“更温和”，**Timeout**路径“归零再起”。两者配合`ssthresh`形成**AIMD行为**。

### 4) UDP — Service & Header vs TCP UDP 与 TCP 的差异与头部
**UDP 特点：**
- **无连接、无重传、无拥塞控制 → 开销小、时延低；适于 DNS、SNMP**等小量控制流，以及**语音/视频**等对时延敏感业务、**LAN 内部**专用应用、多播/广播等。
**UDP 头部**：`Src Port(16b)、Dst Port(16b)、Length(16b)、Checksum(16b)`，极简。
**UDP vs TCP 对照：**
- **建立/释放连接**：**UDP 无需**；**TCP 三次握手/四次挥手**，对“小数据”低效。
- **有序与可靠**：**UDP 不保证顺序与到达；TCP 有顺序/确认/重传/流量与拥塞控制**。
- **典型协议**：TCP（HTTP/FTP/SMTP/POP/TELNET/SSH）、UDP（DNS/DHCP）。

### 5) Wireless LAN (802.11) — Standards & Features 无线 LAN 标准与特性
**标准与速率（示例）：**
- 802.11（2.4 GHz, 2 Mbps, 1997）
- **11a**（5 GHz, **54 Mbps**, 1999）
- **11b**（2.4 GHz, **11 Mbps**, 1999）
- **11g**（2.4 GHz, **54 Mbps**, 2003）
- **11n**（2.4/5 GHz, **600 Mbps**, 2009；**SU-MIMO**）
- **11ac**（5 GHz, **6.9 Gbps**, 2014；**SU-MIMO**）
- **11ax**（2.4/5 GHz, **9.6 Gbps**, 2014；**MU-MIMO**）
**覆盖范围与优缺点：**
- 典型覆盖**30–100 m**；无需布线、移动灵活、漫游可行。
- **缺点**：易被窃听（需加密）、多 AP/信道重叠致**吞吐下降**；2.4 GHz 与**微波炉**等同频干扰导致不稳定或断连。

### 6) Security in Public WLAN 公共无线网络的威胁与对策
- **通信窃听**：无线段未加密 → 内容可被嗅探。**对策**：优先使用**WPA2-AES / WPA3**（WEP/WPA 弱，禁用）。
- **不正访问**：从合法主机入侵网络窃取信息。**对策**：勿将计算机置于可被他人随意使用状态。
- **なりすまし（伪装/冒名）**：利用窃取信息伪装合法主机滥用服务或攻击。
- **恶意/伪造 AP**：搭建假 AP 引导用户连接盗取账号口令。**对策**：**不要连接不明 AP**。

### 7) MIMO — SU vs MU
- **SU-MIMO**：多根天线服务**单个主机**；

- **MU-MIMO**：通过波束赋形等手段，**同时**用多天线服务**多个主机**；

- AP将数据分成多个**空间流**并从多天线并发发射；接收侧将“混合”信号**分离重构，天线数越多，潜在吞吐越高**。

### 8) 802.11 Frame & EtherType 无线帧结构与类型
- **PLCP Preamble（前导码）**：位于帧首、供物理层同步。

- **PLCP Header**：**含调制方式/速率、数据长**等物理层信息。

- **PSDU**：由**802.11 MAC 头 + 业务数据**组成（数据链路层附加）。

- **Type (EtherType)**指示上层协议：`0x0800 IPv4`, `0x0806 ARP`, `0x86DD IPv6`。

### 9) Modulation Methods 调制方式
- **PSK/FSK**：用于 802.11（基础相位/频移键控）。
- **CCK**：11b/11g 使用的**补码键控**。
- **QAM**：11a/11g/11n/11ac/11ax 使用的**正交振幅调制**（更高阶映射带来更高吞吐）

### 10) Infrastructure vs Ad-hoc 基础设施/自组网模式
- **Infrastructure Mode**：经**AP（无线接入点）**转发；
- **Ad-hoc（独立模式）**：终端之间**直接通信**，必要时由客户端**中继**。

### 11) CSMA/CA — Access Method for WLAN 无线局域网的介质访问
**要点**：与以太网**CSMA/CD**类似但**不具备冲突检测**（无线难以边发边听），因此采用**冲突回避**：
- 发送前**监听信道**，若空闲则**等待随机退避时间（Backoff）**后发送；
- 接收端成功收帧后，**SIFS**后发送**ACK**确认；
- 下一发送者等待**DIFS**并执行退避。
**时序（文字示意）**
```
A finishes → (DIFS sensing) → A backoff & send DATA
AP receives → (SIFS) → AP sends ACK
Then B → (DIFS sensing) → B backoff & send DATA → ...
```
- **DIFS**：Distributed Inter-Frame Space（分布式帧间间隔）
- **SIFS**：Short Inter-Frame Space（短帧间间隔）
- **ACK**：确认帧


---
## Key Points
- **TCP Flow**：接收端用**Window**通知可接收量，发送端限制在 flight 数据量。
- **TCP Congestion**：慢启动指数增、超时回落至`cwnd=1`；快速重传下**线性增加**继续发送；`ssthresh`将指数/线性阶段分界。
- **UDP**：轻量低时延，适用于 DNS/多媒体/广播多播/专网；不保证顺序与可靠。
- **WLAN**：标准/速率/频段与**(MU-)MIMO**；注意**加密与伪 AP**风险；**2.4 GHz 干扰**会降吞吐或断连。
- **CSMA/CA**：通过**DIFS/SIFS/ACK/Backoff**回避冲突，无 CD 能力。


---

## ※※Supplementary Cheat Sheets | 速查单

### TCP & CSMA/CA Quick Reference
- [TCP Congestion Control | TCP 拥塞控制速查](./figs/lecture13_tcp_cwnd_ssthresh.md)  
  *TCP 拥塞窗口、慢启动、拥塞避免与快速重传处理*

- [CSMA/CA Timing | CSMA/CA 时序速查](./figs/lecture13_csma_ca_timing.md)  
  *CSMA/CA DIFS/SIFS/ACK/Backoff 时序机制与碰撞回避*




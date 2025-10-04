[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md) 

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 12: Remote Login (Telnet/SSH), FTP; Email (SMTP/POP3/IMAP & TLS/SSL); TCP (Header/Handshake/Timeout/Sliding Window/Fast Retransmit)
# 信息网络概论 第12讲：远程登录（Telnet/SSH）、FTP；邮件（SMTP/POP3/IMAP 与 TLS/SSL）；TCP（首部/握手/超时/滑动窗口/快速重传）

---

## ⚪ Lecture Overview 讲座概览

- **Remote login**: Telnet vs **SSH** — encryption, security, and recommended usage  
  **远程登录**：Telnet 与 **SSH**——加密方式、安全性与使用建议
- **FTP** basics & **FTPS** (SSL/TLS)  
  **FTP** 基础与 **FTPS**（SSL/TLS）
- **Email path**: SMTP for sending; POP3/IMAP for receiving; **TLS/SSL** protection (POP3S/IMAPS/HTTPS)  
  **邮件链路**：发送用 SMTP；接收用 POP3/IMAP；支持 **TLS/SSL** 保护（POP3S/IMAPS/HTTPS）
- **TCP**: connection-oriented reliability — header & flags; 3-way handshake; 4-way termination; SEQ/ACK; timeout & retransmission; sliding window; fast retransmit; flow & congestion control  
  **TCP**：面向连接的可靠性——首部与标志位；三次握手；四次挥手；SEQ/ACK；超时与重传；滑动窗口；快速重传；流量与拥塞控制


---

## ⚪ Lecture Content 讲座内容

### 1) Remote Login: Telnet vs SSH   远程登录

- **Telnet**: Provides remote login; credentials and session are **plaintext**, easy to be sniffed; **generally disabled** in modern environments.  
  **Telnet**：提供远程登录；**口令与会话明文**，易被窃听；现代环境多**禁用**。
- **SSH**: Provides **encrypted** remote login; credentials are transmitted securely; in practice you **should replace Telnet with SSH**.  
  **SSH**：提供**加密**的远程登录；口令加密传输；实际运维应**以 SSH 取代 Telnet**。


```
Telnet: plaintext → credentials exposed → avoid
SSH   : encrypted → safe remote shell → use this
```

---

### 2) FTP & FTPS 文件传输
- **FTP (File Transfer Protocol)**: Used for **file transfer between hosts**; by default, both the **control** and **data** channels are **plaintext**.  
  **FTP（File Transfer Protocol）**：用于**主机间文件传输**；默认情况下，**控制通道**与**数据通道**均为**明文**。 
- **FTPS**: Adds **SSL/TLS** at the transport layer to **encrypt** the FTP control and/or data channels.  
  **FTPS**：在传输层引入 **SSL/TLS**，对 FTP 的**控制通道**和/或**数据通道**进行**加密**。


---
### 3) Email Sending: SMTP / 邮件发送（SMTP）

- **SMTP (Simple Mail Transfer Protocol)**: The **client (or an MTA)** sends mail **to an SMTP server**, which then uses **DNS lookups** and multi-hop routing to deliver it **to the recipient’s mail server**. The recipient’s end host can be **offline**, so **always-on mail servers** relay and store mail.  
  **SMTP（Simple Mail Transfer Protocol）**：**客户端（或 MTA）→ SMTP 服务器**发送邮件；服务器再经由**DNS 解析**与多跳路由转发到**收件方的邮件服务器**。收件方主机可**离线**，因此由**始终在线**的邮件服务器中转与保存。
- **Sender authentication**: Legacy SMTP has **no built-in sender auth**, making it easy to abuse as a **spam relay**. Best practice is to use the **Submission port + SMTP AUTH**, allowing **only authenticated** users to send mail. **POP before SMTP** existed historically, but **separate SMTP AUTH** is safer and is now preferred.  
  **发件人认证**：传统 SMTP **无内建发件人认证**，容易被滥用为**垃圾邮件踏板**。推荐采用**Submission 端口 + SMTP AUTH**，仅允许**通过认证**的用户外发邮件。**POP before SMTP**曾被用过，但与 POP 分离认证更安全，已逐渐弃用。

```
Client MUA --SMTP--> Outbound SMTP Server --(DNS+routed)--> Recipient’s SMTP Server
```

---

### 4) Email Receiving: POP3 / IMAP  
### 邮件接收：POP3 / IMAP

- **Receive-side flow**  
  **收件侧流程**
  1) Start the mail client and initiate retrieval → authenticate to the server using **POP3** with **username/password**.  
     启动邮件客户端发起接收 → 使用 **POP3** 向服务器提交 **用户名/密码**。  
  2) The server **authenticates** the user (checks against its local account store).  
     服务器进行**认证**（与本地账户数据库比对）。  
  3) The server **delivers the user’s mailbox messages** to the client via POP3.  
     服务器通过 POP3 向客户端**发送该用户邮箱中的邮件**。  
- **POP3**: Downloads mail **to the local machine** and by default **deletes it from the server**; readable **offline**, but **the same messages won’t appear on other devices**. Best when a **single device** manages the mailbox.  
  **POP3**：将邮件**下载到本机**并默认**从服务器删除**；可**离线阅读**，但**其他设备看不到同一份数据**。适合**单机管理**邮箱的场景。  
- **POP3S**: POP3 over **TLS/SSL** to encrypt the session.  
  **POP3S**：基于 **TLS/SSL** 的 POP3，会话内容加密。  
- **IMAP**: Keeps mail **on the server**, so multiple devices (PC/phone) **share the same mailbox view**; when the network is down, mail is **not readable offline** (unless locally cached).  
  **IMAP**：邮件**保存在服务器**，多终端（PC/手机）可**共享同一邮箱视图**；网络中断时**无法离线阅读**（除非有本地缓存）。  
- **IMAPS**: IMAP over **TLS/SSL** to encrypt the session.  
  **IMAPS**：基于 **TLS/SSL** 的 IMAP，会话内容加密。

---

### 5) TLS/SSL Overview (Transport-layer encryption)  
### 5) TLS/SSL 概要（传输层加密）

- **TLS (Transport Layer Security) / SSL** sit **above the transport layer** and provide **encryption** and **integrity** for applications; used by **HTTPS / POP3S / IMAPS**.  
  **TLS（传输层安全）/SSL** 位于**传输层之上**，为应用提供**加密**与**完整性**；被 **HTTPS / POP3S / IMAPS** 等采用。

- They offer **confidentiality**, **message integrity (MAC/AEAD)**, and **server authentication** (optional **client auth**) via **X.509 certificates**.  
  它们通过 **X.509 证书**提供**机密性**、**消息完整性（MAC/AEAD）**以及**服务器认证**（可选**客户端认证**）。

- Typical flow: **TLS handshake** → negotiate version/cipher suite, exchange certificates/keys → **encrypted application data**.  
  典型流程：**TLS 握手** → 协商版本/密码套件、交换证书与密钥 → **加密的应用数据**。

---

### 6) TCP — Service & Reliability / 面向连接与可靠性

- **Connection-oriented:** Establish a **connection before sending data**.  
  **面向连接：** 数据发送前先**建立连接**。
- **Reliable transport mechanisms:** checksum, **Sequence number (SEQ)**, **Acknowledgment (ACK)**, retransmission control, **windowing**, connection management, **flow control / congestion control**, etc.  
  **可靠传输机制：** 校验和、**序号（SEQ）**、**确认（ACK）**、重传控制、**窗口**、连接管理、**流量控制/拥塞控制**等。
- **In-order, loss recovery:** delivers bytes **in order** and **recovers losses** using ACK + retransmission (timeout or fast-retransmit).  
  **有序与丢包恢复：** 通过 **ACK + 重传**（超时或快速重传）实现**按序到达**与**丢包恢复**。
- **Flow vs Congestion:** **Flow control** protects the receiver (advertised window); **congestion control** protects the network (e.g., slow start/AIMD).  
  **流量与拥塞：** **流量控制**保护接收端（通告窗口）；**拥塞控制**保护网络（如慢启动/AIMD）。


---

### 7) TCP Header & Control Flags / 首部与控制位

- **Fixed header = 20 bytes (5 × 32-bit words), options not included. Key fields:**  
  **Src/Dst Port (16b each), Sequence Number (32b), Acknowledgment Number (32b), Data Offset (header length), Control Flags (8b), Window, Checksum, Urgent Pointer, Options/Padding.**  
  **固定首部为 20 字节（5×32 位，不含选项）。关键字段：**  
  **源/目的端口（各 16 位）、序号（32 位）、确认号（32 位）、首部长度（Data Offset）、控制位（8 位）、窗口、校验和、紧急指针、选项/填充。**
- **Control flags (1 bit each): `CWR, ECE, URG, ACK, PSH, RST, SYN, FIN`.**  
  **控制位（各 1 位）：`CWR, ECE, URG, ACK, PSH, RST, SYN, FIN`。**

 **meaning / 提示**
> - **CWR**: Congestion Window Reduced — sender has reacted to ECN.  
>   **CWR**：拥塞窗口已降低（对 ECN 的响应）。  
> - **ECE**: ECN-Echo — signals congestion experienced.  
>   **ECE**：回显拥塞标记（ECN）。  
> - **URG**: Urgent pointer field is valid.  
>   **URG**：紧急指针有效。  
> - **ACK**: Acknowledgment field is valid.  
>   **ACK**：确认号有效。  
> - **PSH**: Push — request the receiver to deliver data to app ASAP.  
>   **PSH**：推送，提示接收端尽快把数据交付应用。  
> - **RST**: Reset connection.  
>   **RST**：复位连接。  
> - **SYN**: Synchronize sequence numbers (handshake).  
>   **SYN**：同步序号（建连握手）。  
> - **FIN**: Sender has finished sending data.  
>   **FIN**：发送方数据发送完毕（断连）。

**Layout / 首部布局（not to scale / 非比例）**

```
| SrcPort | DstPort |
|               Sequence Number               |
|             Acknowledgment Number           |
| Hlen |Res|Flags|         Window Size        |
|        Checksum        |     Urgent Ptr     |
| Options ...            | Padding |   Data   |
```

---

### 8) TCP Connection Establishment / 三次握手

- Connection setup uses the **SYN/ACK** control flags in a **3-way handshake**.  
  使用 **SYN/ACK** 控制位进行 **三次握手（3-way handshake）** 完成连接建立。
  
1) **Client → Server**: send `SYN=1` (connection request).  
   **客户端 → 服务器**：发送 `SYN=1`（连接请求）。

2) **Server → Client**: reply `SYN=1, ACK=1` (synchronize and acknowledge).  
   **服务器 → 客户端**：回复 `SYN=1, ACK=1`（同步并确认）。

3) **Client → Server**: send `ACK=1` (final acknowledgment) → **connection established**.  
   **客户端 → 服务器**：发送 `ACK=1`（最终确认）→ **连接建立**。


```
Client                Server
  SYN  ---------------->
       <----------------  SYN,ACK
  ACK  ---------------->      (connected)

```

---

### 9) TCP Connection Termination / 四次挥手

- TCP uses a **four-way handshake** to reliably close a connection; each direction of data flow is closed independently.  
  TCP 使用**四次挥手**可靠地关闭连接；数据流的两个方向**分别**关闭（半关闭）。

1) **Client → Server**: send `FIN=1, ACK=1` to request closing its send direction.  
   **客户端 → 服务器**：发送 `FIN=1, ACK=1`，请求关闭**发送方向**。

2) **Server → Client**: send `ACK=1` to acknowledge the FIN (server may still have data to send).  
   **服务器 → 客户端**：发送 `ACK=1` 确认对方的 FIN（服务器**仍可继续发送**尚未发完的数据）。

3) **Server → Client**: when ready, send `FIN=1, ACK=1` to close its own send direction.  
   **服务器 → 客户端**：准备就绪后发送 `FIN=1, ACK=1`，关闭**自身发送方向**。

4) **Client → Server**: send `ACK=1` (final acknowledgment) → **connection released**.  
   **客户端 → 服务器**：发送 `ACK=1`（最终确认）→ **连接释放**。
```
Client                                  Server
FIN, ACK  ---------------------------->
             <----------------------------  ACK
             <----------------------------  FIN, ACK
ACK        ---------------------------->
(both directions closed; connection terminated)

```

> **Note:** After step 4, the client typically enters **TIME_WAIT** to ensure late segments are not misinterpreted.  
> **说明：** 第 4 步后，客户端通常进入 **TIME_WAIT** 状态，确保迟到报文不会被误判为新连接的数据。


---

### 10) Data Transfer: SEQ/ACK  
### 数据传输与确认

- **Sequence Number (SEQ)**: A continuous, **byte-based** numbering that marks each byte’s position in the stream.
  **序号（SEQ）**：以**字节**为单位的连续编号，用于标识数据在字节流中的位置。
- **Acknowledgment Number (ACK)**: **The next byte index expected** from the peer (i.e., “I have received up to N−1”).
  **确认号（ACK）**：表示**期望接收的下一个字节序号**（即“我已成功接收到 N−1 为止的字节”）。
- **ACK-based reliability**: The receiver sends ACKs to confirm receipt; the sender **slides its window** forward and **drops acknowledged data** from its retransmission buffer.
  **基于 ACK 的可靠性**：接收方通过 ACK 确认已收数据；发送方据此**滑动窗口**并从重传缓冲中**删除已确认的数据**。

```
Example (segment size = 100 bytes)
Sender: SEQ=1..100 → Receiver ACK=101
Sender: SEQ=101..200 → Receiver ACK=201
...
```
```
（假设 MSS = 100 字节）
发送方 → 接收方：    SEQ = 1..100      ⇒ 接收方回 ACK = 101
发送方 → 接收方：    SEQ = 101..200    ⇒ 接收方回 ACK = 201
...
```

---

### 11) Retransmission & Timeout  
### 重传与超时
- **Round-Trip Time (RTT)**: The elapsed time from sending a segment to receiving its ACK; the sender **continuously measures** it.
  **往返时延（RTT）**：从发送一个报文段到收到其 ACK 的用时；发送端会**持续测量**该指标。
- **Retransmission Timeout (RTO)**: If an **ACK is not received before timeout**, the sender **retransmits**. RTO is **dynamically adapted** based on the measured RTT (kept **slightly larger** than RTT).
  **超时重传（RTO）**：若在**超时时间到达前未收到 ACK**，则触发**重传**。RTO 会依据测得的 RTT **动态调整**（通常**略大于** RTT）。

---

### 12) Sliding Window  
### 滑动窗口

- **Goal**: Improve **throughput** by allowing multiple segments in flight (i.e., **don’t wait** for an ACK after every single segment).
  **目的**：通过允许多个报文段“在途”，**提高吞吐**（即**不必**每发送一段就等待 ACK）。
- **Window (bytes)**: The amount of data the sender may transmit **before receiving ACKs**; as ACKs arrive, the window **slides forward**.
  **窗口（字节）**：在收到 ACK 之前**允许连续发送**的数据量；随着 ACK 抵达，窗口**向前滑动**。
- **Sender buffering**: The sender must **buffer unacknowledged data**; once acknowledged, those bytes are **removed** from the buffer and the window **advances** (right-shifts).
  **发送端缓存**：发送端需**缓存未被确认的数据**；一旦被确认，已确认数据从缓存**删除**，窗口**右移**。
- **MSS (Maximum Segment Size)**: Upper bound on a single TCP segment’s payload; constrained by path MTU and options.
  **MSS（最大报文段）**：单个 TCP 报文段可承载的**最大有效负载**；受路径 MTU 与选项限制。
- **Flow control interaction**: The **receiver-advertised window** (rwnd) limits how much the sender can send; the **effective window** is `min(cwnd, rwnd)`.
  **与流量控制的关系**：接收端通告的**窗口（rwnd）**限制发送速率；**有效窗口**为 `min(cwnd, rwnd)`（拥塞窗口与接收窗口取较小值）。

**Example / 示例**

```
Window size = 3000 bytes, MSS = 1000
Send SEQ 1..1000, 1001..2000, 2001..3000 without waiting
ACK for 1..1000 arrives → slide window right by 1000, send 3001..4000
```
```
窗口大小 = 3000 字节，MSS = 1000  
可连续发送 SEQ 1..1000、1001..2000、2001..3000（无需等待）  
当收到 1..1000 的 ACK 时 → 窗口**右移 1000**，继续发送 3001..4000
```
---

### 13) Fast Retransmit / 高速再送

- **Conventional retransmission** waits for a **timeout** before resending, which adds latency.
  **常规重传**需要等待**超时**才会重发，时延较大。
- **Fast retransmit**: when the receiver detects a gap (a segment lost) it keeps sending **duplicate ACKs** for the last in-order byte. Upon receiving **≥ 3 duplicate ACKs**, the sender **immediately retransmits** the missing segment (no timeout needed).
  **快速重传**：当接收端检测到序号缺口（丢段）时，会对已按序收到的最后一个字节持续返回**重复 ACK**。发送端一旦收到**≥3 个重复 ACK**，**无需等待超时**就**立刻重传**缺失的报文段。
- (lecture phrasing): Receiving **3+ identical ACK numbers** makes the sender assume that segment didn’t arrive and **retransmit that segment (and subsequent ones as needed)** — i.e., **Go-Back-N semantics**.
  （讲义表述）：当收到**3 次以上相同确认号**时，发送端认定该段未达，并对**该序号及其后的分段**执行**重传**（具 **Go-Back-N** 语义）。
**Example / 示例**
```
... receive duplicate ACK x3 for ACK=1001 → fast retransmit the missing segment(s)
```
```
已发送 `SEQ=1..1000`、`1001..2000（丢失）`、`2001..3000`；接收端反复返回 `ACK=1001` → 达到 3 次后，发送端对缺失的 `1001..2000` **快速重传**。
```

---

### 14) Flow & Congestion Control / 流量与拥塞控制

- **Flow Control** — The receiver **advertises a window** (rwnd) to limit the sender’s rate and **prevent receive-buffer overflow**.
  **流量控制（Flow Control）**——接收端通过**窗口通告（rwnd）**限制发送速率，避免**接收缓冲溢出**。
- **Congestion Control** — The sender adjusts its sending rate based on **congestion signals** (e.g., loss, delay/RTT growth), aiming to **avoid network collapse**. *(This lecture: high-level overview.)*
  **拥塞控制（Congestion Control）**——发送端根据**网络拥塞迹象**（如丢包、时延/RTT 增长）**调节发送速率**，以**避免网络崩溃**。（本讲为概述层面）

---
## Key Points 

- **Use SSH instead of Telnet** for remote login; FTP is plaintext and should be protected with **FTPS (TLS/SSL)**.
  **SSH 取代 Telnet**：远程登录应使用加密的 SSH；FTP 为明文，需使用 **FTPS（TLS/SSL）** 保护。
- **Email path** — use **SMTP** (with **Submission + AUTH**) to send; **POP3/IMAP** to receive; secure with **POP3S/IMAPS** (TLS/SSL).
  **邮件链路**：外发用 **SMTP**（配 **Submission + AUTH**）；接收用 **POP3/IMAP**；用 **POP3S/IMAPS（TLS/SSL）** 加密。
- **TCP reliability** — header includes **SEQ/ACK/window/flags**; **3-way handshake** to connect, **4-way FIN** to terminate; **adaptive RTO** and **sliding window** improve throughput; **fast retransmit** on **≥3 duplicate ACKs**; plus **flow** and **congestion control**.
  **TCP 可靠性**：首部含 **SEQ/ACK/窗口/控制位**；**三次握手**建连、**四次挥手**断连；**自适应 RTO** 与 **滑动窗口**提升吞吐；**重复 ACK ≥ 3** 触发**快速重传**；并具备**流量控制**与**拥塞控制**。

---

## ※※Supplementary Cheat Sheets | 速查单

### TCP Quick Reference
- [TCP Header & Flags | TCP 首部与控制位速查](./figs/lecture12_tcp_header_flags.md)  
  *TCP 首部结构、控制位功能与连接管理*

- [TCP Sliding Window & Fast Retransmit | 滑动窗口与快速重传速查](./figs/lecture12_tcp_sliding_window_fast_retx.md)  
  *滑动窗口机制、快速重传与超时重传策略*

<h2></h2>

[← Previous Lecture / 上一讲](./lecture11.md) · [Next Lecture / 下一讲 →](./lecture13.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

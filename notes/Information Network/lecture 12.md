#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 12: Remote Login (Telnet/SSH), FTP; Email (SMTP/POP3/IMAP & TLS/SSL); TCP (Header/Handshake/Timeout/Sliding Window/Fast Retransmit)
# 情報ネットワーク概論 第12回：遠隔ログイン（Telnet/SSH）、FTP；メール（SMTP/POP3/IMAP・TLS/SSL）；TCP（ヘッダ／ハンドシェイク／タイムアウト／スライディングウィンドウ／高速再送）

---

## ⚪ Lecture Overview 讲座概览
- **Remote login**: Telnet vs **SSH**（是否加密、使用建议）  
  **远程登录**：Telnet 与 **SSH** 的差异（是否加密、使用建议）
- **FTP** basics & FTPS（SSL/TLS）  
  **FTP** 基本与基于 SSL/TLS 的 **FTPS** 
- **Email path**: SMTP send, POP3/IMAP receive; **TLS/SSL** 保护（POP3S/IMAPS/HTTPS）  
  **邮件链路**：SMTP 发送、POP3/IMAP 接收；**TLS/SSL**（POP3S/IMAPS/HTTPS） 
- **TCP**: 面向连接与可靠控制；首部与控制位；三次握手/四次挥手；SEQ/ACK；超时与重传；  
  **控制**：滑动窗口、快速重传、流量/拥塞控制。 

---

## ⚪ Lecture Content 讲座内容

### 1) Remote Login: Telnet vs SSH 远程登录
- **Telnet**：提供远程登录；**口令与会话明文**，易被窃听，现代环境多**禁用**。  
  **SSH**：提供**加密**的远程登录；口令加密传输，实际运维中应**以 SSH 取代 Telnet**。 

```
Telnet: plaintext → credentials exposed → avoid
SSH   : encrypted → safe remote shell → use this
```

---

### 2) FTP & FTPS 文件传输
- **FTP**（File Transfer Protocol）：用于**主机间文件传输；控制/数据内容明文**。
**FTPS**：在 FTP 上传输层引入**SSL/TLS**以加密通信内容。

---

### 3) Email Sending: SMTP 邮件发送（SMTP）
- **SMTP**（Simple Mail Transfer Protocol）：**客户端（或 MTA）→ SMTP 服务器**发送邮件；服务器再经由**DNS解析**与多跳路由转发到**收件方的邮件服务器**。收件方主机可**离线**，因此由**始终在线**的邮件服务器中转。
- **Sender auth 问题**：传统SMTP**无发件人认证**，易被滥用为垃圾邮件**踏板**；故推荐**Submission端口 + SMTP AUTH**，只允许**认证通过**的邮件外发。**POP before SMTP**曾被用过，但与 POP 分离认证更安全，已逐渐弃用。

```
Client MUA --SMTP--> Outbound SMTP Server --(DNS+routed)--> Recipient’s SMTP Server
```

---

### 4) Email Receiving: POP3 / IMAP 接收
- 收件侧流程
1. 启动邮件客户端发起接收 → 使用**POP3**向服务器提交**用户名/密码**；
2. 服务器**认证**（与本地账户数据库比对）；
3. 通过 POP3 向客户端**发送该用户邮箱中的邮件**。
- **POP3**：下载到**本机**并默认**从服务器删除**；离线可读，但**其他设备不可见**同一份数据。需要**单机管理**邮件时使用。
**POP3S**：POP3 over **TLS/SSL**，保护会话内容。
- **IMAP**：邮件**保存在服务器**，多终端（PC/手机）**共享同一邮箱视图**；网络中断时**离线不可读**（除非本地缓存）。
**IMAPS**：IMAP over **TLS/SSL**。

---

### 5) TLS/SSL 概要（传输层加密）
- **TLS（传输层安全）/SSL**：位于**传输层**之上为应用提供**加密与完整性**；被**HTTPS/POP3S/IMAPS**等采用。

---

### 6) TCP — Service & Reliability 面向连接与可靠性
- **面向连接（Connection-oriented）**：数据发送前先**建立连接**；
- **可靠传输机制**：校验和、**序号（SEQ）**、**确认（ACK）**、重传控制、**窗口**、连接管理、**流量控制/拥塞控制**等。

---

### 7) TCP Header & Control Flags 首部与控制位
- **固定首部 20 字节**（5×32bit，不含选项）；关键字段：
源/目的端口（各16b）、**序号（32b）**、**确认号（32b）**、首部长度、**控制位（8b）**、窗口、校验和、紧急指针、选项/填充。
- **控制位（各1b）**：`CWR, ECE, URG, ACK, PSH, RST, SYN, FIN`。
```
| SrcPort | DstPort |
|               Sequence Number               |
|             Acknowledgment Number           |
| Hlen |Res|Flags|         Window Size        |
|        Checksum        |     Urgent Ptr     |
| Options ...            | Padding |   Data   |
```

---

### 8) TCP Connection Establishment 三次握手
- 使用**SYN/ACK**控制位的**三次握手（3-way handshake）**：
1. **Client → Server**：`SYN=1` 连接请求；
2. **Server → Client**：`SYN=1`, ACK=1 同步并确认；
3. **Client → Server**：`ACK=1` 最终确认 → 连接建立。
```
Client                Server
  SYN  ---------------->
       <----------------  SYN,ACK
  ACK  ---------------->      (connected)

```

---

### 9) TCP Connection Termination 四次挥手
- 1. **Client → Server**：`FIN=1, ACK=1` 关闭请求；
  2. **Server → Client**：`ACK=1` 确认；
  3. **Server → Client**：`FIN=1**, ACK=1` 反向关闭；
  4. **Client → Server**：`ACK=1` 最终确认 → 连接释放。

---

### 10) Data Transfer: SEQ/ACK 数据传输与确认
- **序号（Sequence Number）**：以**字节**计的连续编号，标识数据在流中的位置；
**确认号（ACK Number）：期望收到的下一个字节序号**。
- **ACK 保障**：接收方用 ACK 告知已收；发送方据此**滑动窗口**、删除已确认分段。
```
Example (segment size = 100 bytes)
Sender: SEQ=1..100 → Receiver ACK=101
Sender: SEQ=101..200 → Receiver ACK=201
...
```

---

### 11) Retransmission & Timeout 重传与超时
- **往返时延（RTT）**：每次发送到收到 ACK 的时间；发送端持续测量。
- **超时重传（RTO）**：若**超时仍未收到 ACK** → 触发**重传**；RTO 会**随 RTT 变化动态调整**（略大于 RTT）。

---

### 12) Sliding Window 滑动窗口
- 目的：**提高吞吐**（不必每段都等待 ACK 才发送下一段）。
- **窗口（Window）**：在未获确认前允许连续发送的数据量（字节）；**窗口随 ACK 前移**。
- **发送端**需将未确认数据**缓存**；收到 ACK 后可从缓冲删除、窗口右移。
- **MSS**（最大报文段）受路径设备约束。
```
Window size = 3000 bytes, MSS = 1000
Send SEQ 1..1000, 1001..2000, 2001..3000 without waiting
ACK for 1..1000 arrives → slide window right by 1000, send 3001..4000
```

---

### 13) Fast Retransmit 高速再送
- **常规重传**：等待**超时**才重传，时延较大。
- **快速重传**：接收端在丢段时会对后续有序段反复回 ACK（**重复 ACK ≥3**）；发送端据此**无需等超时即**判定丢失并立即重传。
讲义描述：当收到**3 次以上相同确认号**时，发送端认定该段未达并对**该序号及其后的分段**执行重传（Go-Back-N 语义）。
```
... receive duplicate ACK x3 for ACK=1001 → fast retransmit the missing segment(s)
```

---

###  14) Flow & Congestion Control 流量与拥塞控制
- **流量控制（Flow Control）**：接收端以**窗口通告**限制发送速率，避免**接收缓冲溢出**。
- **拥塞控制（Congestion Control）**：发送端根据**网络拥塞迹象**（丢包/延迟）调节发送速率，避免网络崩溃。（本讲概述层面）


---
## Key Points
- **SSH 取代 Telnet**：远程登录应使用加密的 SSH；FTP 明文，需**FTPS(TLS/SSL)**保护。
- **邮件链路**：**SMTP** 外发（配**Submission + AUTH**）；**POP3/IMAP**接收；**POP3S/IMAPS**通过 TLS/SSL 加密。
- **TCP 可靠性**：首部含**SEQ/ACK/窗口/控制位**；三次握手建连、四次挥手断连；**RTO 动态、滑动窗口**提速；**重复 ACK≥3**触发**快速重传**；具**流量/拥塞控制**。

---

## ※※Supplementary Cheat Sheets | 速查单

### TCP Quick Reference
- [TCP Header & Flags | TCP 首部与控制位速查](./figs/lecture12_tcp_header_flags.md)  
  *TCP 首部结构、控制位功能与连接管理*

- [TCP Sliding Window & Fast Retransmit | 滑动窗口与快速重传速查](./figs/lecture12_tcp_sliding_window_fast_retx.md)  
  *滑动窗口机制、快速重传与超时重传策略*

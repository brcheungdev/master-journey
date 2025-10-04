[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 15: NAT / NAPT, Their Issues & Workarounds; SSL/TLS, Digital Certificates & HTTPS  
# 第15讲：NAT / NAPT、其问题与应对；SSL/TLS、数字证书与 HTTPS

---

## ⚪ Lecture Overview 

- **NAT**: Maps **private IPs ↔ global IPs** (typically one-to-one). Helps conserve IPv4 space; depending on the mode, multiple internal hosts may **share** a single global address for outbound access.  
  **NAT**：将 **私有 IP ↔ 全球 IP**（通常一对一）进行转换；缓解 IPv4 枯竭；视模式而定，可让多台内网主机在**出网**时**共享**一个全球地址。
- **NAPT**: Extends NAT by **also translating transport ports** (“IP masquerading”). Uses the **5-tuple** to distinguish sessions so **many internal hosts** can talk to the **same external host** concurrently.  
  **NAPT**：在 NAT 基础上**同时转换端口号**（“IP 伪装”）；以 **五元组**区分会话，使**多台内网主机**能够与**同一外部主机**并发通信。
- **NAT/NAPT issues**: External peers **cannot easily initiate** inbound connections to internal hosts; translation/state **adds overhead**; device reboot **breaks existing TCP sessions**.  
  **NAT/NAPT 问题**：外部**难以主动连入**内网主机；转换/维护状态**有开销**；设备重启会**中断现有 TCP 连接**。
- **Workarounds**:  
  1) Migrate to **IPv6** and assign each host a **global address** (no NAT/NAPT needed).  
  2) Under **IPv4**, **design applications with NAT/NAPT in mind** (only mitigates the “inbound reachability” issue).  
  **对策**：  
  1) 迁移至 **IPv6**，为**每台主机**分配**全球地址**（无需 NAT/NAPT）。  
  2) 在 **IPv4** 条件下，按 **NAT/NAPT 前提**设计应用（仅缓解“外部连入”问题）。
- **SSL/TLS basics**: Symmetric vs asymmetric cryptography; **public/private key pairs** and their roles.  
  **SSL/TLS 基础**：对称/非对称加密；**公钥/私钥**成对及其使用场景。
- **Digital certificates & CA hierarchy**: **Server generates a key pair → applies to a CA and obtains a certificate → client validates the CA chain → they establish a session key**.  
  **数字证书与 CA 体系**：**服务器生成密钥对 → 向 CA 申请并获颁证书 → 客户端验证 CA 信任链 → 双方协商建立会话密钥**。
- **HTTPS**: HTTP over **TLS/SSL**. The session uses a **symmetric key**; its secure exchange relies on the server’s **public key** and **CA-validated** trust chain.  
  **HTTPS**：在 HTTP 之上使用 **TLS/SSL** 加密；会话采用**对称密钥**，其安全分发依赖服务器的**公钥**与 **CA 验证**的信任链。

---

## ⚪ Lecture Content 

### 1) NAT — Network Address Translator / 网络地址转换

**Purpose / 目的**  
- Convert **LAN private addresses** to **Internet global addresses** to alleviate IPv4 exhaustion; allow many endpoints to access the Internet using **one (or a few) global IPs**.  
- 将 **LAN 私有地址** 转换为 **Internet 全球地址**，以缓解 IPv4 地址不足；支持以**一个（或少量）全球地址**让多终端访问互联网。
**Characteristics / 基本特性**  
- Maintains an **address translation table** inside the router, **creating and updating entries automatically**.  
- 在路由器内部维护**地址转换表**，并**自动**建立与更新对应关系。  
- Traditional one-to-one **Static NAT** maps only **IP ↔ IP**. Without port translation, **at any given time, only one internal host** can maintain a session with a **specific external host**, which **limits concurrency**. → **NAPT** is needed to enable concurrent sharing of the same external destination.  
- 传统一对一 **Static NAT** 仅做 **IP ↔ IP** 映射，**同一时刻**内网**仅一台**主机能与某一**特定外部主机**保持对应会话（不含端口复用），因此**难以并发共享**同一外部目的主机。→ 需 **NAPT** 解决并发性。

---

### 2) NAPT — Network Address **Ports** Translator / 端口地址转换

**Core Idea / 核心思想**  
- Beyond IP translation, **also translate transport-layer ports**, so sessions are distinguished by a **5-tuple**:  
  `DstIP, SrcIP, DstPort, SrcPort, Protocol` (any difference ⇒ a different session).  
- 在 NAT 的 IP 转换之外，**再转换传输层端口**，以 **“5 元组”** 区分会话：  
  `DstIP, SrcIP, DstPort, SrcPort, Protocol`（任一不同即视为不同会话）。
  
**Effect / 效果**  
- **Multiple internal hosts** can simultaneously talk to the **same external host** by multiplexing one global IP with **different external source ports**.  
- **多台内网主机**可同时与**同一外部主机**通信（通过不同的**外显源端口**复用一个全球 IP）。  
- **Entry lifetime** is typically created on **TCP SYN**, and removed after **FIN/ACK** completes (implementations may also use idle timeouts).  
- **表项生命周期**：典型地在 **TCP SYN** 发出时建立；在 **FIN 的 ACK** 完成后删除（不同实现可能含空闲超时老化）。

**Mapping Sketch / 抽象示意**  

```
10.0.0.11:12345 → 203.0.113.5:40001 → Internet → 93.184.216.34:80
10.0.0.12:54321 → 203.0.113.5:40002 → Internet → 93.184.216.34:80
(The same global IP is accessed concurrently through different exposed source ports to the same external host and port)
(同一全局IP，通过不同外显源端口并发访问同一外部主机与端口)
```

---

### 3) NAT/NAPT Problems & Workarounds
### 3) NAT/NAPT 的问题与对策

**Main Issues**
**主要问题**
- **Outside-to-inside initiation is hard**: external hosts generally **cannot directly initiate** connections to internal hosts (no fixed mapping/hole punching).
- **从外到内直连困难**：外部主机通常**无法直接发起**到内网主机的连接（缺少固定映射/穿透）。
  
- **Overhead**: building/looking up translation entries and rewriting packets introduces **processing cost**.
- **开销**：转换表的创建、查找与报文改写带来**处理开销**。

- **Reliability**: if the NAT/NAPT device **crashes/reboots**, existing **TCP sessions break**.
- **可靠性**：NAT/NAPT 设备在通信中**异常/重启**会导致所有**TCP 会话中断**。

**Remedies**
**解决方向**
- **Path A (Fundamental fix)**: move to **IPv6**, give **each host a global address**, so **no NAT/NAPT** is needed; hosts are **reachable from anywhere**, and **translation overhead disappears**. → Solves **1/2/3** at once.
- **方向 A（根治）**：采用**IPv6**，为每台主机分配**唯一全球地址**，**无需 NAT/NAPT**；主机可从 Internet **任何位置**直达，并**消除转换开销**。→ 同时解决**1/2/3**。

- **Path B (Workaround under IPv4)**: design apps **with NAT/NAPT in mind** (e.g., **port forwarding**, **hole punching**, **reverse connections**). This mainly **mitigates issue 1**; **issues 2/3 remain**.
- **方向 B（权衡）**：在**IPv4**下按**NAT/NAPT 前提**设计应用（如**端口映射/打洞/反向连接**等）。主要**缓解问题 1**；但**问题 2/3 仍存在**。

---

### 4) SSL / TLS — Cryptography Basics
### 4) SSL / TLS — 基础与密钥体系

**Goals**
- Protect data in transit on the Internet via **encryption** and **integrity**, implemented using **cryptographic keys**.
**目标**
- 在互联网中通过**加密**与**完整性保护**来保护传输中的数据，基于**密钥**实现。

**Two Key Types**
**两类密钥**

- **Symmetric (Shared) Key**: The **same key** is used for **encryption and decryption**; it must be **distributed securely**.
- **共通鍵（对称密钥）**：使用**同一把密钥**进行**加密/解密**；必须**安全配送**该密钥。

- **Asymmetric (Public/Private) Keys**: A **public key** can be shared openly; the **private key** is kept secret by the owner. The two are **generated as a pair**. Data encrypted with the public key can be **decrypted only by the matching private key**, and vice versa.
- **公開鍵 / 秘密鍵（非对称）**：**公钥**可公开；**私钥**仅由持有者保管；二者**成对生成**。用公钥加密的数据只能被**对应的私钥**解开，反之亦然。

---

### 5) Digital Signature & Certificate — How It Works
### 5) デジタル署名 & 証明書 — 工作机制

**Server-side Preparation (Steps 1–3)**
**服务器侧准备（1–3）**

```
1) The web server generates a public/private key pair.
2) It sends the public key + application materials to a Certification Authority (CA) to request a certificate.
3) The CA signs the submitted information with the CA’s private key and issues a digital certificate.  
   The server installs this certificate; the certificate and any revocation status (CRL/OCSP) are published in a repository.
```

```
1) Web 服务器生成 公钥/私钥（Key Pair）
2) 将 公钥 + 申请资料 发给 认证局（CA）申请证书
3) CA 用“CA 私钥”对上述信息签名，签发“数字证书”
   服务器安装该证书；证书与 CRL（吊销列表）在 Repository 公布
```
**Key Point**：The **CA’s signature** vouches for the **binding** between “this **public key**” and “this **subject identity**,” making it **trustworthy** to clients.
**要点**：**CA 的签名**保证“**此公钥** ↔ **此主体信息**”的**绑定可信**，从而使客户端能够信任该公钥。

**Client-side Handshake (Steps 4–6)**
**客户端侧握手（4–6）**

```
4) The client initiates a connection to the web server.
5) The server sends its digital certificate to the client.
6) The client verifies the certificate’s signature using the CA’s public key → confirms the certificate’s validity and ownership.  
   Then the client generates a session symmetric key,  
   encrypts it with the server’s public key, and sends it to the server;  
   The server uses its private key to decrypt and obtain the session key.
```
```
4) 客户端发起到 Web 服务器的连接
5) 服务器发送其数字证书给客户端
6) 客户端用“CA 公钥”验证证书签名 → 确认证书有效与归属
   之后 客户端生成“会话共通鍵”（对称密钥）
   用 服务器公钥 加密后发送给服务器
   服务器用 私钥 解密获得该会话密钥
```
Modern browsers **preinstall** root certificates (containing CA public keys) to validate the server’s **certificate chain**.
现代浏览器**预装**主流 CA 的根证书（含 CA 公钥），用于验证服务器的**证书链**。

**CA Hierarchy / PKI Layers**
**CA 体系 / PKI 层级**

- **Root CA**: Top of the hierarchy; self-signed; must pass rigorous audits and publish a **CPS (Certification Practice Statement)**.

  **ルート認証局（Root CA）**：体系最上层；自身无需再被其他实体签名，但须通过**严格审计**并公开**CPS（认证业务运用规程）**。

- **Intermediate CA**: Issued and vouched for by an upper CA; builds the **chain of trust** to end-entity certificates.
  
  **中間認証局（Intermediate CA）**：由上级 CA 签发证书以证明其**正当性**，共同构成**信任链**。

---

### 6) HTTPS — Encrypted & Authenticated **HTTP over TLS/SSL**
### HTTPS — 加密与认证（**HTTP over TLS/SSL**）

**Concept**
**概念**

- **TLS/SSL** is layered on top of **HTTP** to encrypt data between the browser and the web server with a **session symmetric key**.
  
**TLS/SSL** 叠加在 **HTTP** 之上，用 **会话对称密钥** 对浏览器与 Web 服务器之间的数据进行加密。

- This **session key** is generated by the **client** and securely delivered to the **server** by encrypting it with the server’s **public key**.
- 
该 **会话密钥** 由 **客户端** 生成，并使用服务器的 **公钥（public key）** 加密后安全地交付给 **服务器**。

- Certificate validity is ensured by a **Certificate Authority (CA)** and the **chain of trust**.
  
证书的有效性由 **认证机构（CA）** 及其 **信任链（chain of trust）** 来保证。

**Key Points**
**要点**

- **Confidentiality**: eavesdroppers cannot read **plaintext**.
  
**机密性（Confidentiality）**：窃听者无法读取 **明文**。

- **Integrity**: prevents **in-transit tampering**.
  
**完整性（Integrity）**：防止传输过程中的 **篡改**。

- **Authentication**: the peer’s identity is verified via the **certificate chain** (primarily **server-side**; **mutual/client certificates** are also possible).
  
**认证（Authentication）**：通过 **证书链** 验证对端身份（以 **服务器端** 为主；也可进行 **双向/客户端证书** 认证）。

---

## Key Points（EN / 中文）

- **NAT** performs **IP↔IP translation**, while **NAPT** additionally uses **port multiplexing** to allow many internal hosts to make **concurrent outbound connections** behind one public IP. NAPT table entries are typically created on **SYN** and removed after **FIN-ACK**.
  
  **NAT** 做 **IP↔IP 转换**，**NAPT** 进一步用 **端口复用** 实现“**一公网多内主机并发外联**”；NAPT 表项常在 **SYN** 时建立、在 **FIN-ACK** 后删除。
  
- **NAT/NAPT — three major issues**: **hard inbound connections**, **translation overhead**, and **session loss on device reboot**. **IPv6** can **eliminate** these constraints **in one shot**.
  
  **NAT/NAPT 三大问题**：**外到内直连难**、**转换开销**、**设备重启致会话断**；**IPv6** 可 **一次性消除** 这些限制。
  
- **SSL/TLS**: a **symmetric key** encrypts/decrypts **session data**; the **public/private key** pair is used to securely **distribute the session key** and **authenticate identity**.
  
  **SSL/TLS**：用 **对称密钥** 对 **会话数据** 加解密；通过 **公钥/私钥** **安全分发会话密钥** 并 **进行身份校验**。
  
- **Certificates & CAs**: server **generates a key pair** → **applies for and receives a certificate** (signed with the **CA’s private key**) → client **verifies** it with the **CA’s public key** → they **establish a session key**. **Root CAs** and **Intermediate CAs** together form the **chain of trust**.
  
  **证书 & CA**：服务器 **生成密钥对** → **申请/签发证书**（由 **CA 私钥**签名）→ 客户端用 **CA 公钥** **验证** → **建立会话密钥**。**根 CA** 与 **中间 CA** 共同构成 **信任链**。
  
- **HTTPS = HTTP + TLS/SSL**: provides **encryption**, **integrity**, and **authentication**; browsers come with **preinstalled root certificates**.
  
  **HTTPS = HTTP + TLS/SSL**：提供 **加密**、**完整性** 与 **身份认证**；浏览器预装 **根证书**。

---

## ※※Supplementary Cheat Sheets | 速查单

### NAPT & TLS Quick Reference
- [NAPT Translation Table | NAPT 转换表速查](./figs/lecture15_napt_translation_table.md)  
  *NAPT 表项结构、生命周期与多主机并发访问机制*

- [TLS Handshake & Certificate Chain | TLS 握手与证书链速查](./figs/lecture15_tls_handshake_certificate_chain.md)  
  *TLS 握手流程、证书链验证与密钥交换机制*

<h2></h2>

[← Previous Lecture / 上一讲](./lecture14.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

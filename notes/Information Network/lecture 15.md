#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 15: NAT / NAPT, Their Issues & Workarounds; SSL/TLS, Digital Certificates & HTTPS  
# 情報ネットワーク概論 第15回：NAT／NAPT、その課題と対策；SSL/TLS・デジタル証明書・HTTPS

---

## ⚪ Lecture Overview 
- **NAT**：将 **私有IP ↔ 全球IP** 一对一转换；缓解 IPv4 枯竭，可让多台主机**共享**一个全球地址进行外联（取决于方式）。:contentReference[oaicite:1]{index=1}  
- **NAPT**：在 NAT 基础上**同时转换端口号**（“IP 伪装”），用 5 元组区分会话，使**多台内网主机**可与**同一外部主机**并发通信。:contentReference[oaicite:2]{index=2}  
- **NAT/NAPT 问题**：外部**难以主动连入**内网主机；转换/维护**有开销**；设备重启会**中断现有 TCP 连接**。:contentReference[oaicite:3]{index=3}  
- **对策**：  
  1) 迁移 **IPv6**，给**每台主机**分配全球地址（无需 NAT/NAPT）。  
  2) 在 **IPv4** 条件下按 **NAT/NAPT 前提**设计应用（仅缓解“外部连入”问题）。 :contentReference[oaicite:4]{index=4}  
- **SSL/TLS 基础**：对称/非对称密钥，公钥/私钥配对与使用场景。:contentReference[oaicite:5]{index=5}  
- **数字证书与 CA 体系**：**服务器生成密钥对 → 向 CA 申请并颁发证书 → 客户端验证 CA → 建立会话密钥**。:contentReference[oaicite:6]{index=6}  
- **HTTPS**：在 HTTP 之上使用 **TLS/SSL** 加密；会话用**对称密钥**，其分发依靠**服务器公钥**加密与 **CA** 验证信任链。:contentReference[oaicite:7]{index=7}

---

## ⚪ Lecture Content 

### 1) NAT — Network Address Translator  网络地址转换
**目的 / Purpose**  
- 将 **LAN 私有地址** 转换为 **Internet 全球地址**，以缓解 IPv4 地址不足；支持以**一个（或少量）全球地址**让多终端访问互联网。:contentReference[oaicite:8]{index=8}

**基本特性 / Characteristics**  
- 维护**地址转换表**于路由器内部，**自动**建立与更新。  
- 传统一对一 **Static NAT** 仅做 **IP ↔ IP** 映射，**同一时刻**内网**仅一台**主机能与某一**特定外部主机**保持对应会话（不含端口复用），因此**难以并发共享**同一外部目的主机。→ 需 **NAPT** 解决并发性。:contentReference[oaicite:9]{index=9}

---

### 2) NAPT — Network Address **Ports** Translator  端口地址转换
**核心思想 / Idea**  
- 在 NAT 的 IP 转换之外，**再转换传输层端口**，以“**5 元组**”区分会话：  
  `DstIP, SrcIP, DstPort, SrcPort, Protocol`（任一不同即视为不同会话）。:contentReference[oaicite:10]{index=10}

**效果 / Effect**  
- **多台内网主机**可同时与**同一外部主机**通信（通过不同的**外显源端口**复用一个全球 IP）。  
- **表项生命周期**：典型地在 **TCP SYN** 发出时建立；在 **FIN** 的 ACK 完成后删除（不同实现可能含超时老化）。:contentReference[oaicite:11]{index=11}

**抽象示意 / Mapping Sketch**  
```
10.0.0.11:12345 → 203.0.113.5:40001 → Internet → 93.184.216.34:80
10.0.0.12:54321 → 203.0.113.5:40002 → Internet → 93.184.216.34:80
(同一全局IP，通过不同外显源端口并发访问同一外部主机与端口)
```

### 3) NAT/NAPT 的问题与对策 Problems & Workarounds
**主要问题 / Issues**
- **从外到内直连困难**：外部主机**无法直接发起**到内网主机的连接（缺少固定映射/穿透）。
- **开销**：转换表的创建、查找与报文改写带来**处理开销**。
- **可靠性**：NAT/NAPT 设备在通信中**异常/重启**会导致所有**TCP 会话中断**。
**解决方向 / Remedies**
- **方向 A（根治）**：采用**IPv6**，为每台主机分配**唯一全球地址**，**无需 NAT/NAPT**，从 Internet**任何位置**可直达；也**消除转换开销**。→ 同时解决**1/2/3**。
- **方向 B（权衡）**：在**IPv4**下按**NAT/NAPT 前提**设计应用（例如使用**端口映射/打洞/反向连接**等理念），主要**缓解问题 1**；但**2/3 仍存在**。

### 4) SSL / TLS — 基础与密钥体系 Cryptography Basics
**目标 / Goals**
- 在互联网中**加密**与**完整性保护**数据传输；基于**密钥**实现。
**两类密钥 / Keys**
- **共通鍵（对称密钥）**：同一把密钥用于**加密/解密**；需**安全配送**。
- **公開鍵 / 秘密鍵（非对称）**：**公钥**可公开；**私钥**仅由持有者保管；二者**成对生成**。用公钥加密的数据只能被**私钥**解开，反之亦然。

### 5) デジタル署名 & 証明書 — 工作机制 Digital Signature & Certificate
**服务器侧准备（1–3）**
```
1) Web 服务器生成 公钥/私钥（Key Pair）
2) 将 公钥 + 申请资料 发给 认证局（CA）申请证书
3) CA 用“CA 私钥”对上述信息签名，签发“数字证书”
   服务器安装该证书；证书与 CRL（吊销列表）在 Repository 公布
```
要点：**CA 的签名**保证“此公钥 ↔ 此主体信息”的绑定**可信**。
**客户端侧握手（4–6）**
```
4) 客户端发起到 Web 服务器的连接
5) 服务器发送其数字证书给客户端
6) 客户端用“CA 公钥”验证证书签名 → 确认证书有效与归属
   之后 客户端生成“会话共通鍵”（对称密钥）
   用 服务器公钥 加密后发送给服务器
   服务器用 私钥 解密获得该会话密钥
```
浏览器内**预装**主流 CA 的根证书（含 CA 公钥），用于验证服务器证书链。
**CA 体系 / PKI 层级**
- **ルート認証局（Root CA）**：体系最上层；自身无需再被其他实体签名，但须通过**严格审计**并公开**CPS（认证业务运用规程）**。
- **中間認証局（Intermediate CA）**：由上级 CA 签发证书以证明其**正当性**，共同构成**信任链**。

### 6) HTTPS — 加密与认证 HTTP over TLS/SSL
**概念 / Concept**
- 在**HTTP**之上叠加**TLS/SSL**，将浏览器 ↔ **Web 服务器**的数据用**会话对称密钥**加密传输；该会话密钥由**客户端生成**并通过**服务器公钥**加密后安全交付服务器。**证书有效性**由 **CA** 验证与信任链保障。
要点 / Key Points
- **机密性**：窃听者无法读取明文。
- **完整性**：防止中途篡改。
- **认证**：通过**证书链**确认对端身份（服务器端为主，必要时也可做**客户端证书**）。

---
## Key Points
- **NAT**做**IP↔IP**转换，**NAPT**进一步用**端口复用**实现“一公网多内主机并发外联”；NAPT 表项常在**SYN**时建立、在**FIN-ACK**后删除。
- **NAT/NAPT 三大问题**：**外到内直连难、转换开销、设备重启致会话断**；**IPv6**可一次性消除这些限制。
- **SSL/TLS**：对称密钥负责会话数据加解密；**公钥/私钥**用于**安全分发会话密钥**与**身份校验**。
- **证书 & CA**：服务器密钥对 → 申请/签发证书（CA 私钥签名）→ 客户端以**CA 公钥**验真 → 建立会话密钥。**根 CA / 中间 CA**共同形成**信任链**。
- **HTTPS** = HTTP + TLS/SSL：**加密传输 + 完整性 + 身份认证**，浏览器预装**根证书**。

---

## ※※Supplementary Cheat Sheets | 速查单

### NAPT & TLS Quick Reference
- [NAPT Translation Table | NAPT 转换表速查](./figs/lecture15_napt_translation_table.md)  
  *NAPT 表项结构、生命周期与多主机并发访问机制*

- [TLS Handshake & Certificate Chain | TLS 握手与证书链速查](./figs/lecture15_tls_handshake_certificate_chain.md)  
  *TLS 握手流程、证书链验证与密钥交换机制*

[← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)  

# Lecture 03: OSI Reference Model, TCP/IP, PDU, CO/CL, Best-effort
# 信息网络基础 第3讲：OSI 参照模型／TCP/IP／PDU／面向连接与无连接／ Best-effort

---

## ⚪ Lecture Overview 
## 课程概览
- Why standardize: from vendor-specific protocols to **OSI Reference Model**  
  为什么要标准化：从厂商私有协议走向 **OSI 参照模型**  
- **OSI RM** objectives & the **7 layers** with roles and examples  
  **OSI 参照模型**的目标与**七层**功能及示例  
- **Encapsulation/Decapsulation** data flow across layers  
  层间**封装/解封装** 的数据流  
- Pros/cons of layered network architecture  
  分层网络体系结构的优缺点  
- **TCP/IP**: de facto standard, IETF, history, and OSI vs TCP/IP mapping  
  **TCP/IP**：事实标准、IETF、历史与 OSI 对应关系  
- **RFC**: what it is and how proposals evolve  
  **RFC**：定义与提案—评论—修订—被广泛使用的过程  
- **CO vs CL** communications, **PDU** terms, **congestion**, **best-effort**  
  **面向连接 vs 无连接** 通信、**PDU** 名称、**拥塞** 与 **尽力而为** 服务

---

## ⚪ Lecture Content 

### 1) From Vendor Protocols to OSI
### 从厂商协议到 OSI 标准
- **Past**: Protocols were developed **per vendor** → mutual interconnection **hard or impossible**.  
  **过去**：协议按**厂商**各自为政 → 异构互连**困难**或**不可行**。  
  - Examples 例：**SNA (IBM, 1974)**，**DECnet (DEC)**；日本系 **DCNA/DINA/FNA/HNA** 等。  
- **Standardization**: led by **ISO** and **CCITT→ITU-T**; **Hubert Zimmermann (1980)** proposed OSI RM.  
  **标准化**：由 **ISO** 与 **CCITT→ITU-T** 推进；**Hubert Zimmermann (1980)** 提出 OSI 参照模型。  
- **OSI = Open Systems Interconnection**; aim: interoperable open systems.  
  **OSI** 全称 **Open Systems Interconnection**；目标：实现开放系统互连。 

---

### 2) Purposes of OSI RM
### OSI 参照模型的目的
- Establish **basic concepts** for information networking.  
  建立信息网络系统的**基本概念**。  
- Clarify the **scope** OSI should cover; **layer roles** must be explicit.  
  明确 OSI 的**覆盖范围**；并使各层**职责清晰**。  
- Provide a **reference model** to **map** existing architectures (e.g., position **TCP/IP** within OSI).  
  提供可与现有体系结构**对照**的**参考模型**（如将 **TCP/IP** 放入 OSI 框架）。  
- Clarify where **various standards** fit in the OSI layers.  
  明确**各类标准**应归属的 OSI 层级。 
---

### 3) OSI 7 Layers — Roles & Examples
### OSI 七层：功能与示例
**Layer → Function → Examples**  
**层 → 主要功能 → 典型示例**

1. **Physical / 物理层**  
   - Bits on the medium; voltages/optics; connectors & cables; **bit-level transfer**.  
     物理信号与接口、介质差异抽象；**比特级**传输。  
   - Ex: **RS-232C, X.21, V.24, I-series**。  

2. **Data Link / 数据链路层**  
   - Between **directly connected** nodes; **frame** identification & transfer; **error detection/recovery**; **block-level guarantee**.  
     邻接节点间帧传输与差错控制；**按块**可靠传输。  
   - Ex: **HDLC, ISO8802/2 LLC, 8802/3 MAC (Ethernet), 8802/4/5 MAC**。  

3. **Network / 网络层**  
   - Addressing & **routing**; **end-to-end** relaying across one/multiple subnets.  
     **寻址与路由**；跨网段 **端到端** 转发。  
   - Ex: **X.25 PLP, IP, IPX**。  

4. **Transport / 传输层**  
   - Reliable, economical, homogeneous end-to-end data transfer; **setup/teardown**, **error & flow control**, **multiplexing**, **classes 0–4**.  
     端到端的可靠传输；**连接建立/释放**、**差错/流量控制**、**多路复用**、**等级0–4**。  
   - Ex: **TCP, UDP**。  

5. **Session / 会话层**  
   - Manage dialogues: **establish/terminate**, mode (full/half-duplex), sync, **retransmission**.  
     会话管理：建连/断连、对话模式、同步与**重传**。  

6. **Presentation / 表示层**  
   - **Data representation** conversion: host-specific ↔ network common; **code conversion**, **encryption**, **compression**.  
     **数据表示**转换：主机内码↔网络通用；**字符集转换、加密、压缩**。  

7. **Application / 应用层**  
   - Application-specific protocols (e.g., file transfer, e-mail).  
     面向应用的协议（文件传输、邮件等）。  

8. **Application Program / 应用程序**：用户程序与中间件。  
> 讲义中额外标注应用程序实体以区分于第7层“应用层接口”。

---

### 4) Encapsulation & Decapsulation
### 封装与解封装
- **Down the stack**: each layer **adds its header** to the data.  
  **向下传递**：每下一层**附加该层首部**。  
- **Up the stack**: each layer **removes its header** from the data.  
  **向上传递**：每上一层**剥离该层首部**。  
- Applies on **end hosts** and **on-path devices** (e.g., routers handle L3/L2).  
  既适用于**端系统**也适用于**中间设备**（如路由器处理 L3/L2）。
  
---

### 5) Pros & Cons of Layered Architecture
### 分层体系的利与弊
- **Pros 优点**  
  - Clearer **protocol description** & **development process**.  
    **协议描述与开发流程**更清晰。  
  - **Independence** between layers; reason locally at same level.  
    层与层**相互独立**；同层只需考虑对等交互。  
- **Cons 缺点**  
  - **Overhead**: add/remove headers at each layer; extra interfaces & control signals.  
    **开销**：层层加/解首部；需要接口与控制信号。  
  - **Implementation difficulty**: optimizing, changing, compacting can be hard; depends on chosen layering.  
    **实现挑战**：高效化、演进、紧凑化不易；与层次设计相关。 
---

### 6) International Protocols & De Facto Standards
### 国际协议与事实标准
- **OSI protocols** standardized by **ISO**; **not widely deployed** today.  
  **OSI 协议**由 **ISO** 标准化；但**并未广泛普及**。  
- **TCP/IP** is **de facto standard** worldwide (not an ISO standard).  
  **TCP/IP** 虽非 ISO 正式标准，但作为**事实标准**全球通用。  
- Reasons for adoption（讲义原文要点）：  
  - Rapidly **build usable protocols**;  
    快速做出**可用协议**；  
  - Start **interoperability tests early** once specs are roughly set;  
    规范雏形即开展**互通试验**；  
  - **Iteratively fix** programs, protocols, documents “while in use”.  
    **边用边改**程序/协议/文档。
    
---

### 7) TCP/IP: Organization, History, Layering
### TCP-IP：组织、历史与分层
- **IETF** (Internet Engineering Task Force) proposes & standardizes TCP/IP.  
  **IETF** 负责 TCP/IP 的提案与标准化。  
- **History**（讲义要点）：  
  - Developed by **ARPANET research groups** in **early 1970s**；  
    1970 年代前期起源于 **ARPANET** 研究团队；  
  - **~1982**: specifications largely decided；  
    **约 1982 年**：规格基本确定；  
  - **1983**: the **only protocol** used on ARPANET.  
    **1983 年**：成为 ARPANET **唯一** 使用的协议。  
- **Layer mapping / 分层对照**（讲义图示）：  
  - OSI **L5–L7** ≈ TCP/IP **Application**；  
    OSI **5–7 层**≈ TCP/IP **应用层**；  
  - OSI **L4** ↔ TCP/IP **Transport**；  
    OSI **传输层** ↔ TCP/IP **传输层**；  
  - OSI **L3** ↔ TCP/IP **Internet**；  
    OSI **网络层** ↔ TCP/IP **网际层**；  
  - OSI **L1–L2** ≈ TCP/IP **Network Interface** (sometimes bundled).  
    OSI **物理+链路** ≈ TCP/IP **网络接口层**（有时合并表述）。

---

### 8) RFC — Request For Comments / RFC：征求意见稿
- **What**: Public documents that describe **Internet technologies** (protocols, formats, etc.).  
  **定义**：公开发布的**互联网技术文档**（协议、格式等）。  
- **Who**: Issued by **IETF**; **anyone** may submit; publicly accessible.  
  **组织**：由 **IETF** 发布；**开放投稿**，可公开阅览。  
- **Why**: To publish specs and **collect comments** for improvement.  
  **目的**：公开规范并**广泛征求意见**以改进。  
- **Typical flow**（讲义示例）：  
  1) Propose a **new protocol**；提出**新协议**  
  2) Community **comments**；社区**评论**  
  3) Provide **revised** versions；发布**修订**稿  
  4) Becomes **implicitly recognized** and **widely used**（de facto）。  
     **被广泛认可与使用**（事实标准）。

---

### 9) Protocol Families (Examples) / 协议族（示例）
- **OSI**: FTAM, MOT(E)IS, VT, CMIS/CMIP, CLNP, CONP …（讲义列举）  
  **OSI** 协议族：FTAM、MOT(E)IS、VT、CMIS/CMIP、CLNP、CONP 等。  
- **TCP/IP**: IP, IC?P (讲义记法；通常为 **ICMP**), TCP, UDP, HTTP, TELNET, SNMP, SMTP …  
  **TCP/IP** 协议族：IP、IC?P（讲义记法；常见为 **ICMP**）、TCP、UDP、HTTP、TELNET、SNMP、SMTP 等。  
- **IPX/SPX (NetWare)**: IPX, SPX, N?C (讲义记法；常见为 **NCP**) …  
  **IPX/SPX**：IPX、SPX、N?C（讲义记法；常见 **NCP**）等。  
- **AppleTalk**: DDP, RTMP, AEP, ATP, ZIP …；**DECnet**: DRP, NSP, SCP …；**XNS**: IDP, SPP, PEP …  
  **AppleTalk**：DDP、RTMP、AEP、ATP、ZIP…；**DECnet**：DRP、NSP、SCP…；**XNS**：IDP、SPP、PEP…  

---

### 10) Communication Types — CO vs CL
### 通信类型：面向连接 vs 无连接
- **Connection-oriented (CO)**  
  - Establish **connection** before data transfer; notify peer about forthcoming transmission.  
    **先建连接**再传数据；预告即将传输。  
  - **Delivery confirmation**; ensure **in-order** reception; apply **congestion avoidance** & **continuous transmission** strategies.  
    **送达确认**；保证**有序**接收；采用**连续传输/拥塞回避**等策略。  
  - **Reliable** communication (e.g., **TCP**); **segment order** guaranteed at receiver.  
    **可靠**（如 **TCP**）；接收端**保证段顺序**。  
- **Connectionless (CL)**  
  - Each send is an **independent** transmission; **no delivery confirmation**; may skip connection setup.  
    每次发送**相互独立**；**无送达确认**；可不经建联流程。  
  - **Best-effort**; loss & reordering possible; **upper layers** must add reliability if needed (e.g., IP + TCP).  
    **尽力而为**；可能丢包/乱序；需由**上层**补足可靠性（如在 IP 之上用 TCP）。

---

### 11) PDU Terms by Layer
### 各层 PDU 名称
- **Packet**：can be generic; narrowly often **Network (IP) layer** unit.  
  **分组**：广义统称；狭义多指 **L3(IP)** 的单位。  
- **Message**：**Session/Presentation/Application** layer unit.  
  **报文**：**L5/L6/L7** 数据单位。  
- **Segment**：**Transport (TCP)** layer unit.  
  **段**：**L4(TCP)** 单位。  
- **Datagram**：**Network and above** simple unit; **no retransmit/order guarantee** (e.g., **IP/UDP**).  
  **数据报**：**L3 及以上**，不含重传/顺序控制（IP/UDP 等）。  
- **Frame**：**Data Link** layer unit.  
  **帧**：**L2** 单位。 

---

### 12) Congestion / 輻輳
### 拥塞
- When network load exceeds device processing capacity, **routers/switches** cannot process all packets.  
  当网络负载超过设备处理能力时，**路由器/交换机**无法及时处理。  
- **Effects**: packet **drops**, severe **delay**, service quality declines.  
  **结果**：**丢包**、**时延增加**、通信质量下降。  
- **User symptoms**:  
  **用户感知**：  
  - Web pages **slow** to load after clicking links（延迟）；  
    点击链接后网页加载**缓慢**（时延）。  
  - **Audio/video** stutter or stop（数据缺落）。 
    **音视频**卡顿或中断（数据缺落）。
     
---

### 13) Best-effort Service
### 尽力而为服务
- **IP (Network layer)** is **best-effort**: no guarantee of actual delivery, but **tries its best** to forward.  
  **IP（网络层）**提供**尽力而为**传输：不保证必达，但尽最大努力转发。  
- **Reliability** can be provided by **TCP** (transport layer) above IP.  
  **可靠性**由 **TCP（传输层）**在 IP 之上提供。  
- **Access speeds** marketed by ISPs (e.g., “1 Gbps fiber”) are **best-effort**: actual throughput may be far lower depending on congestion (e.g., ~10 Mbps under heavy load).  
  运营商宣称的接入速率（如“1 Gbps 光纤”）也是**尽力而为**：拥塞时实际吞吐可能显著低于标称（如仅 ~10 Mbps）。  

---

## Key Points 
## 关键要点
- **OSI RM** gives a common vocabulary & mapping frame for heterogeneous systems; **7 layers** support **encapsulation/decapsulation**.  
  **OSI 参照模型**提供异构系统的共通框架与映射；**七层**职责明确并支撑**封装/解封装**。  
- **Layering trade-offs**: clarity & modularity vs header overhead & implementation difficulty.  
  **分层取舍**：清晰与模块化 vs 首部开销与实现复杂度。  
- **TCP/IP** became a **de facto** global standard via IETF & iterative practice; maps against OSI layers.  
  **TCP/IP** 由 IETF 迭代实践，成为全球**事实标准**；可与 OSI 分层**对照**。  
- **RFC** promotes evolution via open publication and review: proposal → comments → revision → wide adoption.  
  **RFC** 通过开放流程推动规范成熟：提案 → 评论 → 修订 → 广泛采用。  
- **CO vs CL**: connection setup/ack/order vs independent sends/best-effort, with reliability often added by upper layers.  
  **面向连接 vs 无连接**：建连/确认/有序 与 独立发送/尽力而为；可靠性常由上层补充。  
- **PDU terminology alignment**（Message/Segment/Packet/Datagram/Frame）and understanding **congestion** help analyze behavior & performance.  
  统一 **PDU 名称** 与理解**拥塞机理**有助于分析网络与协议栈性能。

<h2></h2>

[← Previous Lecture / 上一章](./lecture02.md) · [→ Next Lecture / 下一章](./lecture04.md) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

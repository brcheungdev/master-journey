[← Back to Course Directory / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)  

# Lecture 02 — Computer Networks: Concepts & History
# 第2讲 — 计算机网络：概念与发展历史（情報ネットワーク概論 第2回）

---

## ⚪ Lecture Overview
## 课程概览

- What is a computer network: definitions, components, and purposes  
  计算机网络的定义：释义、组成和用途  
- Networking history: from beacons to ARPANET and the Internet  
  网络发展历史：从烽火通信到 ARPANET 与互联网  
- LAN, WAN, MAN: differences, applications, and features  
  局域网、广域网、城域网：区别、应用与特点  
- Hosts, terminals, and early online systems (SAGE, SABRE)  
  主机、终端与早期在线系统（SAGE、SABRE）  
- Packet vs line switching; store-and-forward principles  
  分组交换与线路交换；先存后转的原理  
- Network architecture, protocols, layering, services, interfaces  
  网络体系结构、协议、分层设计、服务与接口  
- Layering principles: standardization, modularity, minimal interfaces  
  分层原则：标准化、模块化、接口最小化  

---

## ⚪ Lecture Content 
## 讲座内容

### 1. What is a Computer Network?
### 什么是计算机网络
- **Definition**: A system connecting multiple computers via communication lines for sharing hardware, software, and data.  
  **定义**：利用通信线路连接多台计算机，进行硬件、软件、数据共享的系统。  
- **Core Components**:  
  **核心组成**：  
  1) Hosts (nodes)  
  1) 主机（节点）  
  2) Communication lines  
  2) 通信线路  
  3) Routers/switches for packet forwarding  
  3) 路由器/交换机用于分组转发  
- **Key Idea**: Data is divided into **packets**; routers forward packets hop-by-hop until reaching destination.  
  **关键概念**：数据被分割成 **分组**，路由器逐跳转发直至到达目的地。

---

### 2. Networking History
### 网络发展历史
1. **Beacon signals**: early optical communication methods.  
   **烽火通信**：早期的光学通信方式。  
2. **Morse code** (Samuel Morse, 1844): first long-distance telegraph message between Washington & Baltimore.  
   **莫尔斯电码**（索缪尔·莫尔斯，1844）：华盛顿至巴尔的摩的首条远程电报。  
3. **Telephone** (Alexander Graham Bell, 1876): converted voice to electrical signals over wires.  
   **电话**（亚历山大·格拉汉姆·贝尔，1876）：将语音转换为电信号通过导线传输。  
4. **Computer networks**: began as local/proprietary; **1969 ARPANET** became the Internet’s foundation.  
   **计算机网络**：起初多为本地/专有网络；**1969 年 ARPANET** 奠定了互联网基础。  

**Early Online Systems**  
**早期在线系统**  
- **SAGE** (US DoD & MIT, 1958): air defense system.  
  **SAGE**（美国国防部与麻省理工，1958）：空防系统。  
- **SABRE** (American Airlines, 1964): airline reservation system.  
  **SABRE**（美国航空，1964）：航空订座系统。  

---

### 3. LAN, WAN, MAN
### 局域网、广域网、城域网
- **LAN (Local Area Network)**: single building/campus; fast, low cost, privately managed.  
  **局域网**：单个建筑/校园内；速度快、成本低、私有管理。  
- **WAN (Wide Area Network)**: connects multiple LANs across large distances; higher cost, lower speed.  
  **广域网**：跨地区连接多个局域网；成本高、速度较低。  
- **MAN (Metropolitan Area Network)**: covers an entire city; intermediate scale.  
  **城域网**：覆盖整个城市；规模介于 LAN 与 WAN 之间。  
- **Comparison Factors**: scope, cost, performance, management, protocols.  
  **比较维度**：范围、成本、性能、管理、协议。  

---

### 4. Hosts, Terminals, and Online Systems
### 主机、终端与在线系统
- **Host (Node)**: network-connected computer for computing/storage.  
  **主机（节点）**：负责计算/存储的联网计算机。  
- **Terminal**: input/output device (keyboard + display).  
  **终端**：输入/输出设备（键盘+显示器）。  
- **Online System Workflow**:  
  **在线系统流程**：  
  1) Input from terminal  
     1) 终端输入  
  2) Data sent to host  
     2) 数据传输至主机  
  3) Host processes  
     3) 主机处理  
  4) Results returned  
     4) 结果返回  
  5) Displayed on terminal  
     5) 终端显示 

---

### 5. ARPANET and the Internet
### ARPANET 与互联网
- **Origin**: US DoD project (1960s) aiming for **fault-tolerant communication** with alternate routes.  
  **起源**：20 世纪 60 年代美国国防部项目，目标是具备**容错能力**的可替代路径通信。  
- **Problem**: centralized networks are vulnerable to single-point failures.  
  **问题**：中心化网络易受单点故障影响。  
- **Solution**: packet switching enables rerouting when links fail.  
  **解决方案**：分组交换可在链路故障时重新选路绕行。  
- **Milestones**:  
  - 1969: 4-node ARPANET started.  
  - 1972: Expanded to 34 nodes; proved packet-switched networking works.  
  - Basis for today’s Internet.   
  **里程碑**：  
  - 1969: 4-node ARPANET started.  
    1969 年：4 个节点的 ARPANET 启动。  
  - 1972: Expanded to 34 nodes; proved packet-switched networking works.  
    1972 年：扩展至 34 个节点，验证了分组交换网络的可行性。  
  - Basis for today’s Internet.  
    成为今日互联网的基础。
    
---

### 6. Packet Switching vs Line Switching / 分组交换与线路交换

- **Line Switching (circuit switching)**  
  **线路交换（电路交换）**  
  - Reserve a dedicated end-to-end circuit before any data is sent; it remains allocated until the session ends (e.g., telephone).  
    传输前需预留一条端到端专用电路；会话结束前始终占用（如传统电话）。  
  - Resources stay occupied even during silence, leading to low utilization.  
    即使静音也占用资源，链路利用率较低。  
  - Suits constant-bit-rate, delay-sensitive voice streams.  
    适合恒定码率、对时延敏感的语音等场景。  

- **Packet Switching**  
  **分组交换**  
  - Split data into packets with headers (source, destination, sequence, etc.).  
    将数据切分为带首部的分组（源、目的、序号等）。  
  - Many flows statistically share the same links; no dedicated circuits required.  
    多路通信以统计复用方式共享链路；无需专用电路。  
  - Intermediate nodes store-and-forward packets; receiver reassembles in order.  
    中间节点采用先存后转；接收端按序重组报文。  
  - Suits bursty, data-centric traffic and scales well.  
    适合突发型、以数据为主的业务，伸缩性更好。  


---

### 7. Store-and-Forward Principle
### 先存后转原理
- **Message Switching**: store entire message at intermediate nodes, then forward.  
  **报文交换**：在中继节点完整存储整个报文后再转发。  
- **Packet Switching**: store only packets; shorter delays, higher efficiency.  
  **分组交换**：只缓存分组；时延更短、效率更高。  

---

### 8. Network Architecture and Protocols
### 网络体系结构与协议
- **Protocols** = rules for **format, addressing, error control, sequencing**.  
  **协议** = 关于**数据格式、寻址、差错控制、顺序控制**的规则。  
- **Protocol Families**:  
  **协议族**： 
  - TCP/IP: IP, ICMP, TCP, UDP, HTTP, SMTP, SNMP …  
  - IPX/SPX (Novell), AppleTalk, OSI stack protocols.  
- **Architecture** organizes protocols into layers  
  **体系结构**将协议按层次组织

  - Each layer provides **services** to the layer above via well-defined **interfaces**.  
    每一层通过清晰定义的**接口**向上一层提供**服务**。

  - Enables **standardization**, **modularity**, and **abstraction**.  
    由此实现**标准化**、**模块化**与**抽象化**。


---

### 9. Protocols, Services, and Interfaces
### 协议、服务、接口
- **Protocol**: peer-to-peer rules at the same layer across different machines.  
  **协议**：不同机器上**同层对等体**之间的通信规则。  
- **Service**: functions provided by a lower layer to the upper layer.  
  **服务**：下层提供给上层的功能。  
- **Interface**: boundary defining how upper layers access lower-layer services.  
  **接口**：定义上层如何访问下层服务的边界与调用约定。  

---

### 10. Layering Principles
### 分层设计原则
1. Separate **concepts (what)** from **functions (how)** in each layer.  
   在每一层中区分**概念（做什么）**与**功能（怎么做）**。  
2. Minimize **information exchange between layers**.  
   尽量**减少层间信息交互**。  
3. Follow **international standards** for compatibility.  
   遵循**国际标准**，以确保兼容性。  
4. Balance **number of layers** vs **system complexity**.  
   在**层数多少**与**系统复杂度**之间保持平衡。  

---

## Key Points
## 关键要点
- A computer network consists of **hosts, communication links, and forwarding devices**, enabling resource sharing.  
  计算机网络由**主机、通信链路与转发设备**构成，实现资源共享。  
- Historical path: **beacon → Morse code → telephone → SAGE/SABRE → ARPANET → Internet**.  
  历史脉络：**烽火通信 → 莫尔斯电码 → 电话 → SAGE/SABRE → ARPANET → 互联网**。  
- **LAN/WAN/MAN** differ significantly in scope, performance, cost, and management.  
  **LAN/WAN/MAN** 在范围、性能、成本与管理方式上差异明显。  
- **Packet switching** is generally more efficient and fault-tolerant than **circuit switching**.  
  **分组交换**相较**电路交换**通常更高效且具备更强容错能力。  
- **Network architecture** layers protocols and clarifies **protocol/service/interface** roles; design follows **standardization, modularity, minimal interfaces**, and **complexity balance**.  
  **网络体系结构**以分层组织协议并澄清**协议/服务/接口**角色；设计遵循**标准化、模块化、接口最小化**与**复杂度平衡**。  

<h2></h2>

[← Previous Lecture / 上一章](./lecture01.md) · [→ Next Lecture / 下一章](./lecture03.md) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md) 

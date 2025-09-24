#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)  

# Lecture 2: Computer Networks — Concepts & History / 情報ネットワーク概論 第2回  

---

## ⚪ Lecture Overview 
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

### 1. What is a Computer Network? / 什么是计算机网络
- **Definition**: A system connecting multiple computers via communication lines for sharing hardware, software, and data.  
  **定义**：利用通信线路连接多台计算机，进行硬件、软件、数据共享的系统。  
- **Core Components**:  
  1) Hosts (nodes) 主机（节点）  
  2) Communication lines 通信线路  
  3) Routers/switches for packet forwarding 路由器/交换机负责分组转发  
- **Key Idea**: Data is divided into **packets**; routers forward packets hop-by-hop until reaching destination.  
  **关键概念**：数据被分割成 **分组**，路由器逐跳转发至目的地。

---

### 2. Networking History / 网络发展历史
1. **Beacon signals (烽火通信)**: early optical communication methods.  
2. **Morse code (莫尔斯电码)**: Samuel Morse, 1844; first long-distance telegraph message between Washington & Baltimore.  
3. **Telephone (电话)**: Alexander Graham Bell, 1876; converted voice to electrical signals over wires.  
4. **Computer networks (计算机网络)**:  
   - Started as local, proprietary networks.  
   - 1969: **ARPANET** → foundation of the Internet.  
- **Early Online Systems**:  
  - **SAGE** (US DoD & MIT, 1958): air defense system.  
  - **SABRE** (American Airlines, 1964): airline reservation system.  

---

### 3. LAN, WAN, MAN / 局域网、广域网、城域网
- **LAN (Local Area Network)**: single building/campus; fast, low cost, privately managed.  
  **局域网**：单个建筑/校园内；速度快、成本低、私有管理。  
- **WAN (Wide Area Network)**: connects multiple LANs across large distances; higher cost, lower speed.  
  **广域网**：跨地区连接多个局域网；成本高、速度较低。  
- **MAN (Metropolitan Area Network)**: covers an entire city; intermediate scale.  
  **城域网**：覆盖整个城市；规模介于 LAN 与 WAN 之间。  
- **Comparison Factors**: scope, cost, performance, management, protocols.  
  **比较维度**：范围、成本、性能、管理、协议。

---

### 4. Hosts, Terminals, and Online Systems / 主机、终端与在线系统
- **Host (Node)**: network-connected computer for computing/storage.  
  **主机（节点）**：负责计算/存储的联网计算机。  
- **Terminal**: input/output device (keyboard + display).  
  **终端**：输入/输出设备（键盘+显示器）。  
- **Online System Workflow**:  
  1) Input from terminal → 2) Data sent to host → 3) Host processes → 4) Results returned → 5) Displayed on terminal  
  **在线系统流程**：终端输入 → 数据传输至主机 → 主机处理 → 结果返回 → 终端显示  

---

### 5. ARPANET and the Internet / ARPANET 与互联网
- **Origin**: US DoD project (1960s) aiming for **fault-tolerant communication** with alternate routes.  
  **起源**：1960年代美国国防部项目，目标是**容错通信**。  
- **Problem**: centralized networks vulnerable to single-point failures.  
  **问题**：中心化网络易受单点故障影响。  
- **Solution**: packet switching enables rerouting when links fail.  
  **解决方案**：分组交换在链路故障时可自动绕行。  
- **Milestones**:  
  - 1969: 4-node ARPANET started.  
  - 1972: Expanded to 34 nodes; proved packet-switched networking works.  
  - Basis for today’s Internet.  

---

### 6. Packet Switching vs Line Switching / 分组交换与线路交换
- **Line Switching (线路交换)**:  
  - Reserve entire circuit before data transfer; connection stays until finished (e.g., telephone).  
  - Requires dedicated resources even during silence.  
  - Example: traditional telephony.  
- **Packet Switching (分组交换)**:  
  - Data split into packets with headers (source, destination, sequence).  
  - Multiple communications share the same line; no need for dedicated circuits.  
  - Receiver reassembles packets using header information.  

---

### 7. Store-and-Forward Principle / 先存后转原理
- **Message Switching**: store entire message at intermediate nodes, then forward.  
  **报文交换**：在中继节点完整存储整个报文，再转发。  
- **Packet Switching**: store only packets; shorter delays, higher efficiency.  
  **分组交换**：只存储分组，延迟低、效率高。  

---

### 8. Network Architecture and Protocols / 网络体系结构与协议
- **Protocols** = rules for **format, addressing, error control, sequencing**.  
  **协议** = 规定**数据格式、寻址、差错控制、顺序控制**的规则。  
- **Protocol Families**:  
  - TCP/IP: IP, ICMP, TCP, UDP, HTTP, SMTP, SNMP …  
  - IPX/SPX (Novell), AppleTalk, OSI stack protocols.  
- **Architecture** organizes protocols into layers:  
  - Each layer provides **services** to the above layer via well-defined **interfaces**.  
  - Enables **standardization, modularity, abstraction**.

---

### 9. Protocols, Services, and Interfaces / 协议、服务、接口
- **Protocol**: peer-to-peer rules at the same layer across different machines.  
  **协议**：不同机器相同层之间通信的规则。  
- **Service**: functions provided by a lower layer to the upper layer.  
  **服务**：下层向上层提供的功能。  
- **Interface**: boundary defining how upper layers access lower-layer services.  
  **接口**：层与层之间交互的边界和调用约定。

---

### 10. Layering Principles / 分层设计原则
1. Separate **concepts (what)** from **functions (how)** in each layer.  
   在每一层中区分**概念（做什么）**与**功能（怎么做）**。  
2. Minimize **information exchange between layers**.  
   层间信息交互应尽量减少。  
3. Follow **international standards** for compatibility.  
   遵循**国际标准**，保证兼容性。  
4. Balance **number of layers** vs **system complexity**.  
   在**层数多少**与**系统复杂度**之间保持平衡。  

---

## Key Points 
- 计算机网络由 **主机、通信链路、路由设备** 构成，实现资源共享。  
- 历史发展：烽火通信 → 莫尔斯电码 → 电话 → SAGE/SABRE → ARPANET → 互联网。  
- **LAN/WAN/MAN** 在范围、性能、成本、管理方式上差异明显。  
- **分组交换** 相比 **线路交换** 更高效、容错性更强。  
- **网络体系结构** 将协议分层，清晰定义 **协议、服务、接口**。  
- 分层设计需遵循 **标准化、模块化、接口最小化** 与 **复杂度平衡** 的原则。  

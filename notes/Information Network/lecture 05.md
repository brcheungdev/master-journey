#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 5: Physical/Wireless Media, Topologies, Ethernet & CSMA/CD, Slot/Backoff, 10BASE5 Length Proof  
# 情報ネットワーク概論 第5回：物理/無線メディア・トポロジ・EthernetとCSMA/CD・スロット/バックオフ・10BASE5長さの理由

---

## ⚪ Lecture Overview 
- Infrared & Radio waves: definitions, wavelength/frequency ranges, properties, use cases  
  红外与电波：定义、波长/频率范围、特性与用途  
- Network topologies: **Bus / Star / Ring(Loop) / Mesh / Tree** — features, pros & cons  
  网络拓扑：总线/星型/环(环路)/网状/树型——特性、优缺点  
- Shared-medium access: **Contention (CSMA/CSMA-CD)** vs **Token passing**  
  共享介质接入：竞争方式（CSMA/CSMA-CD）与令牌传递  
- Ethernet basics & frame format; **MAC address (48-bit)**; `ipconfig/ifconfig`  
  以太网概念与帧格式；MAC 地址（48 位）；Windows/Mac 查询方法  
- Ethernet families & media/distances (10/100/1000/10G/40G…)  
  以太网类型与介质/距离（10/100/1000/10G/40G…）  
- CSMA/CD workflow; **IFG (9.6 μs @10 Mb/s)**; **slot time (51.2 μs)**; binary exponential **backoff**  
  CSMA/CD 工作流程；帧间隔；时隙时间；指数退避  
- **10BASE5 = 500 m** 的物理原因：在最小帧内必须能检测到远端冲突 + 传播/中继器延迟推导  
  10BASE5 取 500 m 的原因：最小帧内冲突可检测 + 传播/中继器延迟推导

---

## ⚪ Lecture Content 

### 1) Infrared (IR) & Radio Waves / 红外与电波
- **Infrared（赤外線）**  
  - **Wavelength**: 0.78–1000 μm（= 0.78 μm–1 mm，处于可见光红端之外）。  
    **波长**：0.78–1000 μm（从可见红光外延至毫米波前）。  
  - **IrDA** window: **0.85–0.90 μm**（近红外）。  
    **IrDA** 工作波段：0.85–0.90 μm。  
  - **Properties**: penetrates air well but **poor wall penetration**; **small diffraction**, unsuitable for **long-distance comms**.  
    **特性**：空气透过性好，但**不易穿墙**、**绕射弱**，不适合**长距通信**。  
  - **Uses**: heaters, remote controls, IR sensors, **thermography**.  
    **用途**：电热器、遥控器、红外传感、热成像等。  

- **Radio（電波）**（按日本电波法）  
  - **Frequency ≤ 3000 GHz (3 THz)** → **wavelength ≥ 0.1 mm**。  
    **频率 ≤ 3 THz** → **波长 ≥ 0.1 mm**。  
  - **Good diffraction** → usable **through walls** (e.g., Wi-Fi).  
    **绕射性强** → **可穿墙**（如 Wi-Fi）。  
  - **Uses**: TV/radio, mobile, Wi-Fi, microwave ovens, radar.  
    **用途**：电视/广播、移动通信、无线局域网、微波炉、雷达等。  

---

### 2) Network Topologies / 网络拓扑
- **Bus（バス型）** — e.g., 10BASE2/10BASE5  
  - **Pros**: economical; simple cabling.  
    **优点**：布线简单、成本低。  
  - **Cons**: adding/removing nodes or **link faults** require **network downtime**; **weak under congestion**; only for **very small** nets.  
    **缺点**：增删节点或链路故障需**停网**；**拥塞抗性差**；仅适合**极小规模**。

- **Star（スター型）** — e.g., 10BASE-T/100BASE-TX/1000BASE-T  
  - **Pros**: adding/removing nodes & link faults **do not impact whole net**; economical; good for **small** nets.  
    **优点**：增删/故障**不影响全网**；经济；适合**小规模**。  
  - **Con**: central **switch failure** stops the **entire** network.  
    **缺点**：中心交换设备故障会**全网停摆**。

- **Ring / Loop（リング/ループ型）** — e.g., Token Ring  
  - **Pros**: relatively economical; **high transfer efficiency**。  
    **优点**：较经济；**传输效率高**。  
  - **Cons**: node add/remove or link fault **requires stop**; fit **small high-speed** nets.  
    **缺点**：增删/故障需**停网**；适合**小规模高速**。

- **Mesh（メッシュ型）**  
  - **Pros**: **alternate routes** on failure; **very high reliability**。  
    **优点**：故障时可切换路由；**可靠性极高**。  
  - **Cons**: many links → **high cost**; used for **backbones**。  
    **缺点**：链路多、**成本高**；用于**骨干**。

- **Tree（ツリー型）**  
  - **Pros**: relatively economical; fit **large-scale** nets。  
    **优点**：较经济；适合**大规模**。  
  - **Cons**: prone to **congestion** near roots; add/remove/fault can stop **partial** areas.  
    **缺点**：根部易**拥塞**；增删/故障需**局部停网**。

---

### 3) Shared-Medium Access / 共享介质接入
- **Contention（コンテンション）**  
  - Nodes **compete** for transmit right; used by **10BASE2/10BASE5**; includes **CSMA / CSMA-CD**。  
    节点**争用**信道；用于 10BASE2/5；包含 CSMA / CSMA-CD。  
  - **Performance drops sharply** under heavy traffic.  
    负载高时性能**急剧下降**。

- **Token Passing（トークンパッシング）** — Token Bus / Token Ring  
  - Only the node **holding the token** may transmit; variants: **early token release**, **abend token**。  
    持有令牌者方可发送；有早期释放、异常令牌等机制。  
  - **Stable throughput** even when busy (no sharp collapse).  
    繁忙时吞吐**不骤降**，更稳定。

---

### 4) Ethernet & Frames / 以太网与帧
- **Ethernet**: most used **wired LAN**; defined at **OSI L1+L2**。  
  **以太网**：最常用的有线局域网；定义在 **物理层 + 数据链路层**。  
- **Frame (L2 PDU)** layout（bytes）：  
  - **Preamble (8)** — start marker；帧开始标识。  
  - **Dest MAC (6)** — 目的 MAC。  
  - **Src MAC (6)** — 源 MAC。  
  - **Type (2)** — upper-protocol ID：e.g., **0x0800 IPv4**, **0x0806 ARP**, **0x8035 RARP**。  
  - **Data (46–1500)** — 负载区（不足 46B 需填充）。  
  - **FCS (4)** — **Frame Check Sequence**；帧校验序列（多项式取余）。  
- **Octet = 8 bits**；历史上也曾使用 **7-bit**“byte”的系统。  
  **八位字节 = 8 位**；历史上亦有 7 位“字节”的机型。

---

### 5) MAC Address / MAC 地址
- **48-bit** address used at **L2** to identify interfaces: **NIC on PCs/servers**, **virtual NICs**（VMware 等）、**router interfaces**。  
  **48 位**链路层地址，用于识别接口：PC/服务器物理 **NIC**、虚拟 **vNIC**、路由器端口等。  
- Structure: **OUI (24b)** + **Vendor-assigned (24b)**；stored in **NIC ROM**；usually **not rewritable**。  
  结构：**厂商标识 24 位** + **厂商分配 24 位**；写入 **网卡 ROM**；通常**不可改**。  
- Check on OS:  
  - **Windows**: `ipconfig /all` → “**Physical Address**”；可用 `| more` 分屏。  
  - **macOS**: `ifconfig -a`。  

---

### 6) Ethernet Families & Media / 以太网家族与介质
- **Copper/Coax/Twisted Pair/Optics** with typical **max segment lengths**：  
  - **10BASE2** — **185 m**, **coax**（细同轴）。  
  - **10BASE5** — **500 m**, **coax**（粗同轴）。  
  - **10BASE-T** — **100 m**, **UTP Cat3–5**。  
  - **10BASE-F** — **1000 m**, **MMF**。  
  - **100BASE-TX** — **100 m**, **UTP Cat5 / STP**。  
  - **100BASE-FX** — **412 m**, **MMF**。  
  - **100BASE-T4** — **100 m**, **UTP Cat3–5**。  
  - **1000BASE-CX** — **25 m**, **shielded copper**。  
  - **1000BASE-SX** — **550 m**, **MMF**。  
  - **1000BASE-LX** — **550 m (MMF) / 5000 m (SMF)**。  
  - **1000BASE-T** — **100 m**, **UTP Cat5/5e**。  
  - **10GBASE-SR** — **300 m**, **MMF**。  
  - **10GBASE-LR** — **10 km**, **SMF**。  
  - **10GBASE-ER** — **40 km**, **SMF**。  
  - **10GBASE-LX4** — **10 km**, **SMF**。  
  - **10G/40GBASE-T** — **100 m / 30 m**, **Cat6a / Cat7 (UTP/FTP)**。  

---

### 7) CSMA vs CSMA/CD / 竞争接入与冲突检测
- **CSMA**（Carrier Sense Multiple Access）  
  - When a node wants to send, it **sends immediately** if it senses the medium idle (“fastest wins”).  
    节点欲发送时检测空闲即发，“先到先发”。  
  - If multiple nodes send simultaneously → **collision** → data **corrupted**。  
    并发发送会**碰撞**而**破坏**帧。  

- **CSMA/CD**（… with **Collision Detection**）  
  - Improvement over CSMA: **detect collisions early**, **abort quickly** to **free the medium**, then **backoff** and retry.  
    改进型：**早探测**、**快放弃**、**退避后重试**，提高信道利用。  

---

### 8) CSMA/CD: Operating Steps / 工作步骤
1. **Carrier Sense**（搬送波检测）  
   - Before sending, listen for other signals on the medium; proceed only if idle.  
     发送前检测信道是否空闲；空闲才发送。  
2. **IFG wait**（Interframe Gap；帧间隔）  
   - If idle, wait **IFG** then transmit; **keep monitoring** for collisions during transmission。  
     空闲则等待 IFG 后发送；发送中持续监测碰撞。  
3. **Collision detected** → **abort** sending  
   - Send a **jam** signal to notify others, then **backoff**。  
     检测到碰撞立即中止发送，发 **jam**（干扰）告知他人，随后**退避**。  
4. **Backoff time**  
   - Wait a random backoff interval; then **go back to step 1**。  
     按随机退避时间等待后，**返回步骤 1** 重试。  

- **10 Mb/s example**: **IFG = 9.6 μs**（相当于 **96 bit** 的发送时长）。  
  10Mb/s 下 IFG 为 9.6 微秒（96 位发送时间）。  

---

### 9) IFG, Slot Time & Backoff / 帧间隔、时隙与退避
- **IFG (Interframe Gap)**  
  - @ **10 Mb/s**: 9.6 μs = time to send **96 bits**；@**10BASE5** 记法同。  
    10Mb/s 时为 9.6 μs，即 96 位的发送时间。  

- **Slot time（スロット時間）**  
  - Defined as time to send the **minimum frame (64 B = 512 bits, excl. preamble)**。  
    定义为发送**最小帧（64B=512bit，不含前导）**所需时间。  
  - @ **10 Mb/s**: **512 / (10×10⁶)** ≈ **51.2 μs**。  
    10Mb/s 时约 **51.2 μs**。  

- **Binary Exponential Backoff（二进制指数退避）**  
  - Let **n** be the number of collisions for this frame.  
    设 **n** 为该帧已发生的碰撞次数。  
  - If **n ≤ 15**: choose random integer **t ∈ [0, 2ᵏ−1]**, where **k = n** if **n ≤ 10**, else **k=10**。  
    当 **n ≤ 15**：在 **[0,2ᵏ−1]** 随机取 **t**，其中 **k=n(n≤10)**，**n≥11** 时 **k=10**。  
  - **Backoff time = t × slot_time**。  
    退避时间 = **t × 时隙时间**。  
  - If **n = 16**: **give up** sending this frame → report **error** to upper layer。  
    当 **n=16**：放弃该帧，向上层上报**发送错误**。  

---

### 10) 10BASE5 & 10BASE2: Distances & Repeaters / 距离与中继
- **10BASE5**（粗同轴）  
  - **Max segment length 500 m**；可放置 **≤2** 个 **repeaters**（物理层放大/整形）→ **max span 1.5 km**。  
    段长 500 m；≤2 个中继器；最大跨越约 1.5 km。  
- **10BASE2**（细同轴）  
  - **Max segment length 185 m**（细缆**衰减大**）；可放置 **≤4** 个 **repeaters** → **max span 925 m**。  
    段长 185 m；≤4 个中继；最大跨越 925 m。  
- **Max hosts per segment**: **100**。  
  每段主机数上限约 **100**。  

---

### 11) Why is 10BASE5 limited to 500 m? / 10BASE5 为何限制在 500 m
**Goal**（物理层保障冲突检测）  
- A sender must be able to **detect a far-end collision** **before finishing** sending the **minimum frame**; otherwise it would **assume success** incorrectly.  
  在发送**最小帧**结束前，必须能**检测到远端冲突**；否则会**误判成功**。  

**Worst-case setup（最差场景假设）**  
- Topology: Host A —— Repeater —— Repeater —— Host B，三段同轴各长 **L**（**3L** 总缆长），两端各一台主机；两个中继器的延迟均为 **tᵣ**。  
  拓扑：A—中继—中继—B，三段同轴各长 **L**（总长 **3L**），两端主机，两个中继器延迟均 **tᵣ**。  
- Parameters: **tᵣ = 9 μs**；propagation speed **v_g = 0.77 c**, where **c = 3×10⁸ m/s**。  
  设定：中继延迟 **9 μs**；传播速度 **v_g = 0.77c**。  
- Sender A transmits the **minimum frame**（64B=512b），其发送持续时间 **T_min = 51.2 μs**（10 Mb/s）。  
  A 发送最小帧，持续 **51.2 μs**。  

**Timing to detect a collision / 检测冲突的时间链路**  
- Consider collision **near B**; B **immediately aborts** and **sends jam** back.  
  最坏冲突发生在 B 近端；B 立刻**中止并回送 jam**。  
- **I.** Head of A’s frame reaches near B: **t₁ = (3L / v_g) + 2 tᵣ**。  
  A 的帧头到达 B 近端时间：**t₁ = (3L/v_g) + 2tᵣ**。  
- **II.** Jam from B reaches A: **t₂ = (3L / v_g) + 2 tᵣ**。  
  B 的 jam 到达 A 的时间：**t₂ = (3L/v_g) + 2tᵣ**。  
- Total time for A to detect the collision: **t₁ + t₂ = 2 × (3L / v_g + 2 tᵣ)**。  
  A 检测到冲突的总时延：**t₁ + t₂ = 2 × (3L/v_g + 2tᵣ)**。  

**Constraint / 约束条件**  
- Must satisfy **t₁ + t₂ ≤ T_min**。  
  需要满足 **t₁ + t₂ ≤ 最小帧发送时长**。  

**Solve for L / 求解 L**  
\[
2\left(\frac{3L}{v_g} + 2t_r\right) \le 51.2\,\mu s
\Rightarrow
\frac{6L}{v_g} + 4t_r \le 51.2\,\mu s
\]
取 **v_g = 0.77×3×10⁸ m/s**，**t_r = 9 μs**，解得：
\[
L \le 585.2\,m
\]
- Considering **signal attenuation**, the **standard chooses 500 m** for 10BASE5 segments（保守余量）。  
  考虑**衰减与余量**，标准将 **10BASE5 段长** 定为 **500 m**。  

---

## Key Points 
- **红外**：0.78–1000 μm；不易穿墙、绕射弱；IrDA 0.85–0.90 μm。**电波**：≤3 THz；可穿墙、应用广。  
- **拓扑优缺点**：总线/环需停网变更，星型中心故障全停，网状可靠但成本高，树型适合大规模但易在汇聚处拥塞。  
- **接入机制**：竞争（CSMA/CSMA-CD）在高负载下性能骤降；令牌传递忙时也能稳定。  
- **以太网帧**：Preamble(8) / Dest(6) / Src(6) / Type(2) / Data(46–1500) / FCS(4)；八位字节=8 bit。  
- **MAC 48 位**：OUI(24)+设备(24)，写入 NIC ROM；Windows `ipconfig /all`，macOS `ifconfig -a` 可查。  
- **家族与介质**：10/100/1000/10G/40G 及其 UTP/同轴/光纤的典型最大距离列表。  
- **CSMA/CD 实务**：IFG=9.6 μs（10 Mb/s），slot=51.2 μs；二进制指数退避（n≤10→k=n，n≥11→k=10；n=16 放弃）。  
- **10BASE5 500 m**：基于“最小帧内必须能探测远端冲突”的物理约束 + 传播/中继延迟推导并留出衰减余量。  


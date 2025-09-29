[← Back to Course README / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 5: Physical/Wireless Media, Topologies, Ethernet & CSMA/CD, Slot/Backoff, 10BASE5 Length Proof  
# 第5回：物理/无线介质、网络拓扑、以太网与 CSMA/CD、时隙/退避、10BASE5 段长推导

---

## ⚪ Lecture Overview 
- Infrared & Radio waves: definitions, wavelength/frequency ranges, properties, use cases  
  红外与电波：定义、波长/频率范围、特性与应用场景  
- Network topologies: **Bus / Star / Ring(Loop) / Mesh / Tree** — features, pros & cons  
  网络拓扑：总线 / 星型 / 环（环路）/ 网状 / 树型——特性、优缺点  
- Shared-medium access: **Contention (CSMA/CSMA-CD)** vs **Token passing**  
  共享介质接入：竞争方式（CSMA/CSMA-CD）与令牌传递  
- Ethernet basics & frame format; **MAC address (48-bit)**; `ipconfig/ifconfig`  
  以太网基础与帧格式；**48 位 MAC 地址**；`ipconfig/ifconfig` 查询  
- Ethernet families & media/distances (10/100/1000/10G/40G…)  
  以太网家族与介质/距离（10/100/1000/10G/40G…）  
- CSMA/CD workflow; **IFG (9.6 μs @10 Mb/s)**; **slot time (51.2 μs)**; binary exponential **backoff**  
  CSMA/CD 工作流程；**帧间隔**；**时隙时间**；二进制指数**退避**  
- **10BASE5 = 500 m** physical rationale: detect far-end collision within **minimum frame**, incl. propagation/repeater delays  
  **10BASE5 = 500 m** 的物理依据：在**最小帧**内必须能探测到远端冲突（含传播/中继延迟）

---

### 1) Infrared (IR) & Radio Waves / 红外与电波
- **Infrared (IR)**  
  - **Wavelength**: 0.78–1000 μm (0.78 μm–1 mm), beyond the red end of visible light.  
    **波长**：0.78–1000 μm（0.78 微米至 1 毫米），位于可见红光之外。  
  - **IrDA window**: **0.85–0.90 μm** (near-IR).  
    **IrDA** 工作波段：**0.85–0.90 μm**（近红外）。  
  - **Properties**: good in air; **poor wall penetration**, **weak diffraction** → not for long range.  
    **特性**：空气中传播良好；**不易穿墙**、**绕射弱**，不适合长距离通信。  
  - **Uses**: heaters, remotes, IR sensors, **thermography**.  
    **应用**：电暖、遥控器、红外传感、热成像。  

- **Radio waves**  （按日本电波法） 
  - **Frequency ≤ 3 THz** → **wavelength ≥ 0.1 mm**.  
    **频率 ≤ 3 THz** → **波长 ≥ 0.1 mm**。  
  - **Good diffraction** → can **penetrate walls** (e.g., Wi-Fi).  
    **绕射强** → **可穿墙**（如 Wi-Fi）。  
  - **Uses**: broadcasting, cellular, Wi-Fi, microwave ovens, radar.  
    **应用**：广播电视、蜂窝通信、无线局域网、微波炉、雷达。

---

### 2) Network Topologies / 网络拓扑
- **Bus** — e.g., 10BASE2/10BASE5  
  - **Pros**: simple cabling; low cost.  
    **优点**：布线简单，成本低。  
  - **Cons**: add/remove nodes or **link faults** require **downtime**; weak under congestion; for **very small** nets.  
    **缺点**：增删节点或链路故障须**停网**；拥塞适应性差；仅适用于**极小网络**。  

- **Star** — e.g., 10BASE-T/100BASE-TX/1000BASE-T  
  - **Pros**: add/remove/faults don’t affect whole net; economical for **small** nets.  
    **优点**：增删/故障不致全网受影响；对**小规模**经济。  
  - **Con**: central **switch** failure stops the **entire** net.  
    **缺点**：中心交换设备故障会**全网停摆**。  

- **Ring / Loop** — e.g., Token Ring  
  - **Pros**: economical; **high transfer efficiency**.  
    **优点**：较经济；**传输效率高**。  
  - **Cons**: add/remove/fault require **stop**; suited to **small high-speed** nets.  
    **缺点**：增删/故障需**停网**；适合**小规模高速**网络。  

- **Mesh**  
  - **Pros**: **alternate routes** on failures; **very reliable**.  
    **优点**：可走**备份路径**；**可靠性高**。  
  - **Cons**: many links → **high cost**; used for **backbones**.  
    **缺点**：链路多、**成本高**；多用于**骨干网**。  

- **Tree**  
  - **Pros**: relatively economical; fits **large-scale** nets.  
    **优点**：较经济；适合**大规模**网络。  
  - **Cons**: **congestion** near roots; changes/faults may stop **partial** areas.  
    **缺点**：根部易**拥塞**；增删/故障可能导致**局部停网**。

---

### 3) Shared-Medium Access / 共享介质接入
- **Contention（コンテンション）**  
  - Nodes **compete** for transmit right; used by **10BASE2/10BASE5**; includes **CSMA / CSMA-CD**。  
    节点**争用**信道；10BASE2/10BASE5 采用；包含 CSMA / CSMA-CD。  
  - **Performance drops sharply** under heavy traffic.  
    高负载下吞吐**急剧下降**。  

- **Token Passing (Token Bus / Token Ring)**   
  - Only the node **holding the token** may transmit; variants: **early token release**, **abend token**。  
    仅**持有令牌**的节点可以发送；有早期释放、异常令牌等机制。  
  - **Stable throughput** even when busy (no sharp collapse).  
    即使繁忙也能保持**稳定吞吐**，更稳定。

---

### 4) Ethernet & Frames / 以太网与帧
- **Ethernet**: dominant **wired LAN**, defined at **OSI L1+L2**.  
  **以太网**：主流**有线局域网**，定义在 **物理层 + 数据链路层**。 
- **Frame (L2 PDU)** layout (bytes):  
  - **Preamble (8)** — start marker. / 帧开始标识  
  - **Dest MAC (6)** — destination. / 目的 MAC  
  - **Src MAC (6)** — source. / 源 MAC  
  - **Type (2)** — upper protocol (e.g., **0x0800 IPv4**, **0x0806 ARP**, **0x8035 RARP**).  
    上层协议类型（示例如上）  
  - **Data (46–1500)** — payload (pad to 46 B if short).  
    负载区（不足 46B 需填充）  
  - **FCS (4)** — Frame Check Sequence.  
    帧校验序列（CRC）   
- **Octet = 8 bits** (historically some systems used 7-bit “byte”).  
  **八位字节 = 8 位**（历史上也有 7 位“字节”的系统）。

---

### 5) MAC Address / MAC 地址
- **48-bit** L2 address identifying interfaces (**NIC**, **vNIC**, router ports).  
  **48 位**链路层地址，用于标识接口（物理/虚拟网卡、路由端口）。  
- Structure: **OUI (24b)** + **Vendor (24b)**; stored in **NIC ROM**; usually **not rewritable**.  
  结构：**OUI 24 位** + **厂商分配 24 位**；写入 **网卡 ROM**；通常**不可改写**。  
- Check on OS: **Windows** `ipconfig /all` (“Physical Address”); **macOS** `ifconfig -a`.  
  系统查看：**Windows** 用 `ipconfig /all`（Physical Address），**macOS** 用 `ifconfig -a`。  

---

### 6) Ethernet Families & Media / 以太网家族与介质
- **Copper/Coax/Twisted Pair/Optics** with typical **max segment lengths**:  
  **铜缆/同轴/双绞线/光纤**及常见**最大段长**：  
  - **10BASE2** — **185 m**, **coax**. / 细同轴  
  - **10BASE5** — **500 m**, **coax**. / 粗同轴  
  - **10BASE-T** — **100 m**, **UTP Cat3–5**.  
  - **10BASE-F** — **1000 m**, **MMF**.  
  - **100BASE-TX** — **100 m**, **UTP Cat5 / STP**.  
  - **100BASE-FX** — **412 m**, **MMF**.  
  - **100BASE-T4** — **100 m**, **UTP Cat3–5**.  
  - **1000BASE-CX** — **25 m**, **shielded copper**.  
  - **1000BASE-SX** — **550 m**, **MMF**.  
  - **1000BASE-LX** — **550 m (MMF) / 5000 m (SMF)**.  
  - **1000BASE-T** — **100 m**, **UTP Cat5/5e**.  
  - **10GBASE-SR** — **300 m**, **MMF**.  
  - **10GBASE-LR** — **10 km**, **SMF**.  
  - **10GBASE-ER** — **40 km**, **SMF**.  
  - **10G/40GBASE-T** — **100 m / 30 m**, **Cat6a / Cat7(UTP/FTP)**。 

---

### 7) CSMA vs CSMA/CD / 竞争接入与冲突检测
- **CSMA** (Carrier Sense Multiple Access)  
  - If the medium is idle, **transmit immediately** (“fastest wins”).  
    检测空闲即**立刻发送**（“先到先发”）。  
  - Simultaneous sends → **collision** → data **corrupted**.  
    并发发送会**碰撞**，数据**损坏**。  

- **CSMA/CD** (… with **Collision Detection**)  
  - Detect collisions **early**, **abort quickly**, then **backoff** and retry.  
    **尽早检测**并**立刻放弃**，随后**退避**重试，提高信道利用率。  

---
### 8) CSMA/CD: Operating Steps / 工作步骤
1. **Carrier Sense** — listen first; send only if idle.  
   **载波侦听**：先听后发，空闲才发送。  
2. **IFG wait** — wait **IFG**, transmit, and keep monitoring for collisions.  
   **等待帧间隔**： 空闲则等待 **IFG** 后发送，发送中持续监听碰撞。  
3. **If collision** — **abort** and send **jam**, then backoff.  
   **若检测到碰撞**：**立即中止**并发送 **jam（干扰）** 告知他人，随后退避。  
4. **Backoff** — wait a random time, then retry from step 1.  
   **退避**：按随机退避时间等待后，**返回步骤 1** 重试。 

- **10 Mb/s example**: **IFG = 9.6 μs** (time to send **96 bits**).  
  **10 Mb/s**：**IFG = 9.6 μs**（相当于发送 **96 bit** 的时长）。
  
---

### 9) IFG, Slot Time & Backoff / 帧间隔、时隙与退避

- **IFG (Interframe Gap)**  
  - @ **10 Mb/s**: 9.6 μs = time to send **96 bits**.  
    **10 Mb/s** 下 **9.6 μs** 等于发送 **96 位** 所需的时间。

- **Slot time（スロット時間）**  
  - Defined as the time to send the **minimum frame (64 B = 512 bits, excl. preamble)**.  
    定义为发送**最小帧（64 B = 512 bit，不含前导）**所需的时间。  
  - @ **10 Mb/s**: **512 / (10×10⁶)** ≈ **51.2 μs**.  
    **10 Mb/s** 时约为 **51.2 μs**。

- **Binary Exponential Backoff（二进制指数退避）**  
  - Let **n** be the number of collisions for this frame.  
    设 **n** 为该帧已发生的碰撞次数。  
  - If **n ≤ 15**: choose a random integer **t ∈ [0, 2ᵏ−1]**, where **k = n** if **n ≤ 10**, else **k = 10**.  
    当 **n ≤ 15**：在 **[0, 2ᵏ−1]** 随机取 **t**，其中 **n ≤ 10** 时 **k = n**，**n ≥ 11** 时 **k = 10**。  
  - **Backoff time = t × slot_time**.  
    **退避时间 = t × 时隙时间**。  
  - If **n = 16**: **give up** sending this frame → report **error** to the upper layer.  
    当 **n = 16**：放弃发送该帧，并向上层上报**发送错误**。


---

### 10) 10BASE5 & 10BASE2: Distances & Repeaters / 距离与中继

- **10BASE5** (thick coax)  
  - **Max segment length 500 m**; up to **≤2** **repeaters** (physical-layer amplification/reshaping) → **max span ~1.5 km**.  
    **最大段长 500 m**；可放置 **≤2 个**物理层中继器（放大/整形）→ **最大覆盖约 1.5 km**。

- **10BASE2** (thin coax)  
  - **Max segment length 185 m** (higher cable **attenuation**); up to **≤4** **repeaters** → **max span ~925 m**.  
    **最大段长 185 m**（细缆**衰减更大**）；可放置 **≤4 个**中继器 → **最大覆盖约 925 m**。

- **Max hosts per segment**: **100**.  
  **每段主机上限**：约 **100 台**。


---

### 11) Why is 10BASE5 limited to 500 m? / 10BASE5 为何限制在 500 m
**Goal**（ensure collision detection at the physical layer/物理层保障冲突检测）  
- A sender must be able to **detect a far-end collision** **before finishing** sending the **minimum frame**; otherwise it would **assume success** incorrectly.  
  在发送**最小帧**结束之前，发送端必须能够**检测到最远端发生的碰撞**；否则会**误以为发送成功**。  

**Worst-case setup (assumptions)**  
最差场景假设（前提）

- **Topology**: Host A —— Repeater —— Repeater —— Host B; three coax segments each length **L** (**total 3L**). One host at each end; both repeaters have a delay **tᵣ**.  
  **拓扑**：A —— 中继 —— 中继 —— B；三段同轴电缆各长 **L**（**总缆长 3L**）。两端各一台主机；两个中继器的单向处理延迟均为 **tᵣ**。

- **Parameters**: **tᵣ = 9 μs**; propagation speed **v_g = 0.77·c**, where **c = 3×10⁸ m/s**.  
  **参数**：**tᵣ（中继延迟） = 9 μs**；传播速度 **v_g = 0.77·c**，其中 **c = 3×10⁸ m/s**。

- **Minimum frame at 10 Mb/s**: Sender A transmits **64 B = 512 bits**, so **T_min = 51.2 μs**.  
  **10 Mb/s 下的最小帧**：发送端 A 发送 **64 B = 512 bit**，因此 **T_min = 51.2 μs**。【 A 发送最小帧，持续 **51.2 μs**。】

### Timing to detect a collision / 检测冲突的时间链路

- Consider a collision **near B**; B **immediately aborts** and **sends a jam** back.  
  最坏冲突发生在 **B 近端**；B 立刻**中止发送**并**回送 jam**。  
- **I.** Head of A’s frame reaches near B: **t₁ = (3L / v_g) + 2 tᵣ**.  
  **I.** A 的帧头到达 B 近端的时间：**t₁ = (3L / v_g) + 2 tᵣ**。  
- **II.** Jam from B reaches A: **t₂ = (3L / v_g) + 2 tᵣ**.  
  **II.** B 发出的 jam 抵达 A 的时间：**t₂ = (3L / v_g) + 2 tᵣ**。  
- Total time for A to detect the collision: **t₁ + t₂ = 2 × (3L / v_g + 2 tᵣ)**.  
  A 检测到冲突的总时延：**t₁ + t₂ = 2 × (3L / v_g + 2 tᵣ)**。
  

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

- **Infrared**: 0.78–1000 μm; poor wall penetration, weak diffraction; IrDA 0.85–0.90 μm. **Radio**: ≤3 THz; penetrates walls; broad applications.  
  **红外**：0.78–1000 μm；不易穿墙、绕射弱；IrDA 0.85–0.90 μm。**电波**：≤3 THz；可穿墙、应用广。  

- **Topology pros/cons**: Bus/Ring require downtime for changes; Star fails if the center fails; Mesh is reliable but costly; Tree suits large scale but congests near aggregation.  
  **拓扑优缺点**：总线/环需停网变更，星型中心故障全停，网状可靠但成本高，树型适合大规模但易在汇聚处拥塞。  

- **Access methods**: Contention (CSMA/CSMA-CD) collapses under heavy load; Token passing remains stable when busy.  
  **接入机制**：竞争（CSMA/CSMA-CD）在高负载下性能骤降；令牌传递忙时也能稳定。  

- **Ethernet frame**: Preamble(8) / Dest(6) / Src(6) / Type(2) / Data(46–1500) / FCS(4); octet = 8 bits.  
  **以太网帧**：Preamble(8) / Dest(6) / Src(6) / Type(2) / Data(46–1500) / FCS(4)；八位字节 = 8 bit。  

- **48-bit MAC**: OUI(24) + Device(24), stored in NIC ROM; check via Windows `ipconfig /all`, macOS `ifconfig -a`.  
  **MAC 48 位**：OUI(24)+设备(24)，写入 NIC ROM；Windows `ipconfig /all`，macOS `ifconfig -a` 可查。  

- **Families & media**: Typical max distances for 10/100/1000/10G/40G over UTP/coax/fiber.  
  **家族与介质**：10/100/1000/10G/40G 及其 UTP/同轴/光纤的典型最大距离列表。  

- **CSMA/CD practice**: IFG = 9.6 μs (10 Mb/s), slot = 51.2 μs; binary exponential backoff (n≤10→k=n, n≥11→k=10; n=16 give up).  
  **CSMA/CD 实务**：IFG = 9.6 μs（10 Mb/s），slot = 51.2 μs；二进制指数退避（n≤10→k=n，n≥11→k=10；n=16 放弃）。  

- **10BASE5 500 m**: Ensured by “must detect far-end collision within the minimum frame” plus propagation/repeater delays and safety margin.  
  **10BASE5 500 m**：基于“最小帧内必须能探测远端冲突”的物理约束 + 传播/中继延迟推导并留出衰减余量。  
 

---

## ※※ Supplementary Notes (Lecture 5)  
- [Collision Timing & 10BASE5 Length Derivation](./figs/lecture05_collision_timing.md)
  *10BASE5 段长推导与最小帧内碰撞检测原理*
- [CSMA/CD Operation Flow & Timing](./figs/lecture05_csma_cd_flow.md)
  *CSMA/CD 工作流程、退避算法与时序图解*

---

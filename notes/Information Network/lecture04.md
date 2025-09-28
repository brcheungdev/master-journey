[← Back to Course README / 返回课程目录](./README.md#toc)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)  

# Lecture 4: LAN & TCP/IP History, Physical Media, Ethernet Naming, Encoding, Fiber Optics  
# 第4讲：局域网与 TCP/IP 历史、传输介质、以太网命名、编码、光纤

---

## ⚪ Lecture Overview 
- LAN & TCP/IP history: **ALOHA(1968) → ARPANET(1969) → Ethernet(1973)**, **TCP prototype(1975)**, **UNIX/BSD & TCP/IP(1981)**, **IEEE 802 (1980)**, **TCP/IP unification(1983)**, **ARPANET end/NSFNET(1990)**, **AUP commercialization(1991)**, **Japan commercial ISPs(1993)**, **vBNS/Internet2(1995–)**  
  局域网与 TCP/IP 的历史关键节点：从 ALOHA 到 ARPANET、以太网、TCP 原型、BSD 集成、IEEE 标准化、TCP/IP 成为事实标准、NSFNET 接力与互联网商用化。  
- Japan academic backbones: **SINET1→6** (speed from **100 Mbps → 400 Gbps**; **100 Gbps** international lines; **5G** cooperation)  
  日本学术主干网 SINET 的演进：带宽从 **100 Mbps** 提升到 **400 Gbps**，并引入 **100 Gbps** 国际线路与 **5G** 协同。  
- TCP/IP **4-layer** vs OSI **7-layer** mapping; **Network Interface / Physical** defines media  
  TCP/IP 四层与 OSI 七层的映射；**网络接口/物理层** 定义传输介质。  
- Physical media: **metal cables (coax / twisted pair)**, **fiber optics**, **electromagnetic waves** (wireless/infrared)  
  传输介质：金属线缆、光纤与电磁波（无线/红外）。  
- Ethernet naming: **aBASEb** (rate/baseband/media or distance) and **baseband vs broadband**  
  以太网命名规则 **aBASEb** 与 **基带/宽带** 的区别。  
- Twisted-pair categories & wiring: **Cat3…Cat8**, **UTP/STP**, **straight vs cross** (MDI/MDI-X)  
  双绞线类别与布线：**Cat3…Cat8**、**UTP/STP**、**直通/交叉**（MDI/MDI-X）。  
- Line coding on Ethernet PHY: **NRZ / NRZI / Manchester / MLT-3** and standards  
  以太网物理层符号编码：**NRZ/NRZI/曼彻斯特/MLT‑3** 与各标准的对应。  
- Optics fundamentals: **EM spectrum**, **reflection/refraction (Snell)**, **total internal reflection**, **single vs multi‑mode**  
  光学基础：**电磁谱**、**反射/折射（斯涅尔）**、**全反射**、**单模 vs 多模**。  

---

## ⚪ Lecture Content 

### 1) LAN & TCP/IP: A Historical Thread / 历史脉络（LAN 与 TCP/IP）
- **1968 – ALOHA system** (University of Hawaii)  
  无线分组通信（岛际无线包传输）；以太网后来将 **介质从无线改为同轴**，提升**速率与可靠性**。  
- **1969 – ARPANET** launched  
  开始进行**分组交换**通信实验；**1972 年**已扩展到 **34** 个节点。  
- **1973 – Ethernet** (Xerox) on **coaxial cable**; drew ideas from ALOHA  
  以同轴电缆实现的局域网；理念承袭自 ALOHA（ALOHA 用无线）。  
- **1975 – TCP prototype**; **UNIX** adoption grows  
  **1975 年**完成 TCP 原型；同时期 **UNIX** 普及。  
- **1976 – Xerox PARC** Ethernet paper published  
  以太网论文发表（成熟化里程碑）。  
- **1981 – 4.1BSD** integrates **TCP/IP**  
  **4.1BSD** 集成 **TCP/IP**。  
- **1980 – IEEE 802 standardization**: **802.3 Ethernet (CSMA/CD)**, **802.4 Token Bus**, **802.5 Token Ring**  
  **IEEE 802** 标准化：**802.3 以太网**、**802.4 令牌总线**、**802.5 令牌环**。  
  > TokenBus/TokenRing 的**有效吞吐**可达标称的 **≈95%**，而冲突条件下 CSMA/CD 以太网**有效吞吐**常仅 **≈50%**。  
- **1983 – TCP/IP** becomes standard on ARPANET  
  **1983 年** TCP/IP 成为 ARPANET 的标准协议。  
- **1988 – ARPANET** reaches **20,000** nodes  
  **1988 年** ARPANET 节点数达 **20,000**。  
- **1990s**: **ARPANET retired → NSFNET**; **AUP (1991)** opens commercialization; **10BASE‑T** popularizes LANs; **Japan commercial ISPs (1993)**  
  1990 年代：**ARPANET 退役 → NSFNET**；**AUP(1991)** 开放商用；**10BASE‑T** 简化布线、普及 LAN；**日本 1993 年**设立商用 ISP。  
- **1995–2000 – US backbones**: **vBNS (1995)** with NAP interconnects, connects supercomputing centers & universities; **Internet2 (1996)** research backbone; **vBNS+ (2000)** privatized  
  **1995–2000**：**vBNS** 上线、**Internet2** 启动、**vBNS+** 完全私营化。  

---

### 2) Japan Academic Backbones — SINET / 日本学术网 SINET
- Lead org: **NII (National Institute of Informatics)**  
  主导单位：**国立情報学研究所**。  
- **SINET1 (1992–)**: mainframe terminal protocols (**non‑TCP/IP**), **100 Mbps**; inherited **NACSIS**  
  **SINET1（1992–）**：大型机终端协议（**不使用 TCP/IP**），**100 Mbps**；承接 **NACSIS**。  
- **SINET2 (2002–, SuperSINET)**: **TCP/IP**, up to **10 Gbps**  
  **SINET2（2002–）**：采用 **TCP/IP**，速率 **至 10 Gbps**。  
- **SINET3 (2007–)**: up to **40 Gbps**  
  **SINET3（2007–）**：**至 40 Gbps**。  
- **SINET4 (2011–)**: up to **40 Gbps**, higher reliability  
  **SINET4（2011–）**：**至 40 Gbps**，强调高可靠。  
- **SINET5 (2016–)**: up to **400 Gbps**; **100 Gbps** international lines  
  **SINET5（2016–）**：**至 400 Gbps**；**100 Gbps** 国际回线。  
- **SINET6 (2022–)**: **400 Gbps optical**; collaboration with **5G**  
  **SINET6（2022–）**：**400 Gbps 光传输**；与 **5G** 协同。  

---

### 3) TCP/IP 4-Layer vs OSI 7-Layer / TCP-IP 四层与 OSI 七层
- OSI: **Physical / Data Link / Network / Transport / Session / Presentation / Application**  
  OSI：**物理 / 数据链路 / 网络 / 传输 / 会话 / 表示 / 应用**。  
- TCP/IP: **Network Interface / Internet / Transport / Application**  
  TCP/IP：**网络接口 / 网际 / 传输 / 应用**。  
- Mapping idea: OSI **L1–L2 ≈ TCP/IP NI**; OSI **L3 ↔ TCP/IP Internet**; OSI **L4 ↔ TCP/IP Transport**; OSI **L5–L7 ≈ TCP/IP Application**  
  映射：OSI **L1–L2 ≈ 网络接口**；OSI **L3 ↔ 网际层**；OSI **L4 ↔ 传输层**；OSI **L5–L7 ≈ 应用层**。  
- Media defined at **OSI Physical** / **TCP/IP Network Interface**  
  传输介质由 **OSI 物理层** 或 **TCP/IP 网络接口层** 定义。 

---

### 4) Transmission Media — Types & Placement / 传输介质：类型与分层位置
- **Wired**  
  有线  
  1) **Metal cables**: **Coax**, **Twisted Pair**  
     **金属线缆**：**同轴**、**双绞线**。  
     - Coax up to **~1 Gbps**, **~3,600 m** (lecture example)  
       同轴可达 **~1 Gbps**、**~3,600 m**（讲义示例）。  
     - Twisted pair up to **10 Gbps**, within **100 m**  
       双绞线 **至 10 Gbps**、**100 m** 内。  
  2) **Fiber optics**: **Single‑mode** (to **~10 Gbps**, **~40 km**), **Multi‑mode** (to **~100 Gbps**, **~2 km**)  
     **光纤**：**单模**（至 **~10 Gbps**、**~40 km**），**多模**（至 **~100 Gbps**、**~2 km**）。  
- **Wireless**  
  无线  
  - **Infrared (IrDA)** up to **~16 Mbps**, **~1 m**  
    **红外 (IrDA)** **~16 Mbps**、**~1 m**。  
  - **2.4/5 GHz Wi‑Fi** up to **~9.6 Gbps** (distance per standard)  
    **2.4/5 GHz Wi‑Fi** **~9.6 Gbps**（距离视标准而定）。 

---

### 5) Metal Cables — Coax & Twisted Pair / 金属线缆：同轴与双绞线
- **Twisted Pair**: two copper wires twisted (pitch) to suppress noise; **untwisting degrades immunity**  
  **双绞线**：两根铜线按节距绞合抑制噪声；**解绞会降低抗干扰**。  
- **Coax**: more reliable than UTP but **higher cost**  
  **同轴**：相较 UTP 更可靠，但**成本更高**。  
- **Bit transfer**: map **High/Low** voltages to **1/0**  
  **比特传输**：**高/低电平** 对应 **1/0**。  
---

### 6) Coax-based Ethernets / 同轴以太网（10BASE2/5）
- **10BASE2 (Thinnet)** / **10BASE5 (Thicknet)**; **10 Mbps** (CSMA/CD)  
  **10BASE2（细以太）** / **10BASE5（粗以太）**；标称 **10 Mbps**（CSMA/CD）。  
- **Bus topology**; **half‑duplex** on the same cable  
  **总线拓扑**；同一根线上**半双工**收发。  
- **Max segment length**: e.g., 10BASE5 **500 m**  
  **最大段长**：如 10BASE5 **500 m**。  
- **Expansion**: 10BASE2 uses **T‑connector**; 10BASE5 uses **transceiver**; **adding hosts requires downtime**  
  **扩容**：10BASE2 用 **T 形接头**，10BASE5 用 **收发器**；**两者增设主机需停网**。 

---

### 7) Star Ethernets on Twisted Pair / 双绞线星型以太网
- **10BASE‑T / 100BASE‑TX / 1000BASE‑T** on twisted pair  
  **10BASE‑T / 100BASE‑TX / 1000BASE‑T** 采用双绞线。  
- **Star topology** to **Switching Hub/Router**; **no downtime** for adding hosts  
  **星型**连接到**交换机/路由器**；**增设主机无需停网**。  
- **Hub→Host up to 100 m**; **full‑duplex** (separate pairs)  
  **交换机→主机最长 100 m**；**全双工**（收发分线）。  
- **UTP/STP**: STP offers **better noise immunity**  
  **UTP/STP**：STP 比 UTP **抗干扰更强**。   

---

### 8) “aBASEb” Naming / 以太网命名法
- **a**: data rate (**10/100/1000/10G/100G**; **1 M = 1000, 1 G = 1000 M = 1,000,000**)  
  **a**：速率（**10/100/1000/10G/100G**；**1M=1000，1G=1000M=1,000,000**）。  
- **BASE**: **Baseband** (vs **BROAD** = Broadband)  
  **BASE**：**基带**（对应 **BROAD**=宽带）。  
- **b**: medium/distance code — **digits** (e.g., **5 → 500 m**, **2 → 185 m** for coax) or **letters** (**T**=Twisted Pair, **F**=Fiber; **S/L/E**=**850/1300/1550 nm**)  
  **b**：介质/距离代号——**数字**（如 **5→500 m**、**2→185 m**）或**字母**（**T**=双绞线，**F**=光纤；**S/L/E**=**850/1300/1550 nm**）。  
- Example: **1000BASE‑T** → **1000 Mbps / baseband / twisted pair**  
  例：**1000BASE‑T** → **1000 Mbps / 基带 / 双绞线**。  
---

### 9) Baseband vs Broadband / 基带与宽带传输
- **Baseband**: transmit **digital** directly on the medium (no modulation); common for wired Ethernet  
  **基带**：**数字信号直接**上线传输（不经调制）；以太网有线常用。  
  - Typical line codes: **NRZ, bipolar, Manchester**, etc.  
    典型码型：**NRZ、双极性、曼彻斯特** 等。  
- **Broadband**: **modulate** digital into analog; receiver **demodulates** (e.g., modems)  
  **宽带**：将数字**调制为模拟**发送，接收端**解调**复原（如 **Modem**）。  
  - Typical modulation: **AM/FM/PM/QAM**  
    典型调制：**AM/FM/PM/QAM**。
    
---

### 10) Twisted Pair Categories / 双绞线类别（Cat）
- Category & twist **pitch** determine **rate/bandwidth** and number of **used pairs**  
  类别与绞合**节距**决定可支持的**速率/带宽**与**使用的线对数**。  
- **Cat3**: 10BASE‑T (**2 pairs**)  
  **Cat3**：10BASE‑T（**2 对**）  
- **Cat4**: Token Ring (**2 pairs**)  
  **Cat4**：令牌环（**2 对**）  
- **Cat5**: 100BASE‑TX (**2 pairs**)  
  **Cat5**：100BASE‑TX（**2 对**）  
- **Cat5e**: 1000BASE‑T (**4 pairs**)  
  **Cat5e**：1000BASE‑T（**4 对**）  
- **Cat6/6A**: Gigabit/10G (**4 pairs**)  
  **Cat6/6A**：千兆/10G（**4 对**）  
- **Cat7**: 10GBASE‑T (**4 pairs**)  
  **Cat7**：10GBASE‑T（**4 对**）  
- **Cat8**: 40GBASE‑T (**4 pairs**)  
  **Cat8**：40GBASE‑T（**4 对**）  
- **Straight vs Cross**: PC↔Switch uses **straight**; **Switch↔Switch** or **PC↔PC** uses **cross**; **Auto‑MDI/MDI‑X** usually removes the need (except old PC↔PC)  
  **直通 vs 交叉**：PC↔交换机用**直通**（常用）；**交换机↔交换机**或**PC↔PC**用**交叉**；现代 **Auto‑MDI/MDI‑X** 多可自动适配（老旧 **PC↔PC** 例外;外通常无需关心交叉。）。  

---

### 11) Line Coding on Ethernet PHY / 以太网物理层符号编码
- **NRZ**: 1→High, 0→Low; used by **1000BASE‑X (fiber)**  
  **NRZ**：1→高、0→低；用于 **1000BASE‑X（光）**。  
- **NRZI**: toggle on “1”; used by **100BASE‑FX (fiber)**  
  **NRZI**：遇“1”翻转；用于 **100BASE‑FX（光）**。  
- **Manchester**: mid‑bit transition; used by **10BASE‑5/2/T (copper)**  
  **曼彻斯特**：位中翻转；用于 **10BASE‑5/2/T（铜）**。  
- **MLT‑3**: cycle **0 → +E → 0 → −E → 0** on “1”; used by **100BASE‑TX (copper)**  
  **MLT‑3**：在“1”时按 **0 → +E → 0 → −E → 0** 循环；用于 **100BASE‑TX（铜）**。  

---

### 12) Fiber Optic Cabling / 光纤布线基础
- Standards: **1000BASE‑LX/SX**, **100BASE‑FX**, etc.  
  标准：**1000BASE‑LX/SX**、**100BASE‑FX** 等。  
- Fiber bundles can reach **~100 cores** with steel armor; **one core up / one core down** → two‑core **full‑duplex**  
  **光纤束**可至 **~100 芯**并外覆钢丝；**上下行各 1 芯** → 两芯构成**全双工**。  
- **Light ON/OFF** encodes bits  
  **发光/不发光 (ON/OFF)** 对应表示比特信息。  
- **Single‑mode (SMF)**: **1300/1550 nm**; **long distance / low dispersion**; higher material purity → **higher cost**  
  **单模 (SMF)**：**1300/1550 nm**；**远距离/低色散**；材料纯度高 → **成本高**。  
- **Multi‑mode (MMF)**: **850/1300 nm**; **many modes**; **short‑reach high bandwidth**; plastics possible → **lower cost**  
  **多模 (MMF)**：**850/1300 nm**；**多模并行**；**短距高带宽**；材料可用塑料 → **成本低**。  

---

### 13) Electromagnetic Waves & Optics / 电磁波与光学要点
- **EM waves**: light is both **wave** and **photon**; wavelength **λ** inversely proportional to frequency **f**; energy increases as **λ** decreases  
  **电磁波**：光既是**波**也是**光子**；**波长 λ** 与 **频率 f** 成反比；**能量 E** 随 **λ 变短而增大**;**波长越短能量越高（短波更具破坏性）**。  
- **Spectrum**: γ‑ray / X‑ray / UV / **visible** / IR / **radio**  
  **光谱**：γ 射线 / X 射线 / 紫外 / **可见光** / 红外 / **电波**（从短到长）。  
- **Vector relation**: **E** and **H** fields are orthogonal to each other and to the propagation direction  
  **矢量关系**：电场与磁场**互相垂直**，且都与传播方向**垂直**。  

---

### 14) Reflection & Refraction (Snell) / 反射与折射（斯涅尔定律）
- **Law of reflection**: **θ₁ = θ₂** (independent of medium)  
  **反射定律**：**入射角 = 反射角**（与媒质无关）。  
- **Snell’s law**: **sinθ₁ / sinθ₃ = n₂ / n₁** when entering a different medium  
  **折射定律**：入射到不同介质时方向改变，满足 **sinθ₁ / sinθ₃ = n₂ / n₁**。  
- Lenses **focus** light by refraction  
  光学元件（如**透镜**）通过折射**汇聚光线**。   

---

### 15) Total Internal Reflection & Fiber / 全反射与光纤导光
- From **higher‑n** to **lower‑n** medium, beyond a critical angle, **total internal reflection** occurs (no transmission)  
  从**高折射率介质**入射到**低折射率介质**时，超过临界角会出现**全反射**（不进入第二介质）。  
- Fiber structure: **core (higher‑n)** and **cladding (lower‑n)** → light is trapped by TIR within the **core**  
  光纤结构：**核（高折射率）**与**包层（低折射率）** → 光在**核**内由**全反射**传输而不泄露。   
- 讲义步骤图：  
  - (A) 普通折射；(B) 入射角更小 → 边界沿向；(C) 再小 → **全反射**（不入射）。  

---

### 16) Single vs Multi‑Mode / 单模与多模
- **Single‑mode (SMF)**: one mode → **low dispersion**, **long‑reach**; high‑purity quartz → **higher cost**; best for **long‑haul backbone**  
  **单模 (SMF)**：仅 1 模态 传播， **色散小/距离长**；常用高纯石英 ， **成本高**；**长距干线**优选。  
- **Multi‑mode (MMF)**: many modes → **modal dispersion**, **shorter reach**; **high capacity** at **short distances**; plastics → **lower cost**  
  **多模 (MMF)**：多模并行 → **模式色散大**、**距离较短长距困难**；**短距**下可支持**高带宽**；材料可选塑料 → **成本低**。  

---

## Key Points 
- Historical line (**ALOHA → ARPANET → Ethernet → TCP/IP → NSFNET → vBNS/Internet2**) and Japan **SINET1–6 (100 Mbps→400 Gbps)** milestones and bandwidth growth.  
  历史纵线（**ALOHA → ARPANET → Ethernet → TCP/IP → NSFNET → vBNS/Internet2**）与日本 **SINET1–6（100 Mbps→400 Gbps）** 的里程碑与带宽提升。  
- IEEE **802.3/4/5** positioning and **TokenBus/TokenRing** effective throughput advantage vs **CSMA/CD** (lecture figures: **≈95% vs ≈50%**).  
  IEEE **802.3/4/5** 的定位，以及 **TokenBus/TokenRing** 在**有效吞吐**上的优势对比 **CSMA/CD**（讲义数值：**≈95% vs ≈50%**）。  
- **TCP/IP 4 layers ↔ OSI 7 layers** mapping; **Physical/Network Interface** define transmission media.  
  **TCP/IP 四层 ↔ OSI 七层** 的对应；**物理/网络接口层** 定义传输介质。  
- Media parameters: **coax/twisted pair/fiber/IR/Wi‑Fi** typical **rate–distance** ranges; **star vs bus**, **half/full‑duplex** differences.  
  介质参数：**同轴/双绞/光纤/红外/无线** 的典型**速率–距离**范围；**星型 vs 总线**、**半/全双工** 差异。  
- **aBASEb** naming, **Baseband vs Broadband**, **Cat3–Cat8 / UTP–STP / Straight–Cross / Auto‑MDI‑X** usage.  
  **aBASEb** 命名、**基带 vs 宽带**、**Cat3–Cat8 / UTP–STP / 直通–交叉 / Auto‑MDI‑X** 的使用场景。  
- PHY coding: **NRZ/NRZI/Manchester/MLT‑3** vs **1000BASE‑X / 100BASE‑FX / 10BASE‑5/2/T / 100BASE‑TX**.  
  物理层编码：**NRZ/NRZI/曼彻斯特/MLT‑3** 对应 **1000BASE‑X / 100BASE‑FX / 10BASE‑5/2/T / 100BASE‑TX**。  
- Optics: **EM spectrum, reflection/refraction, total internal reflection**, and **SMF vs MMF** trade‑offs (distance/bandwidth/cost).  
  光学：**电磁谱、反射/折射、全反射**，以及 **SMF vs MMF** 的距离/带宽/成本取舍。  

---

<h2></h2>

[← Previous / 上一章](./lecture03.md) · [Next / 下一章 →](./lecture05.md) · [Back to Course README / 返回课程目录](./README.md#toc) · [Notes Home / 笔记首页](../) · [Repository Home / 仓库首页](../../README.md)

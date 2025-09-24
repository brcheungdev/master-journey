#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)  

# Lecture 4: LAN & TCP/IP History, Physical Media, Ethernet Naming, Encoding, Fiber Optics  
# 情報ネットワーク概論 第4回：LAN/TCP-IPの歴史・伝送媒体・Ethernet命名・符号化・光ファイバ

---

## ⚪ Lecture Overview 
- LAN & TCP/IP history: **ALOHA(1968) → ARPANET(1969) → Ethernet(1973)**，**TCP prototype(1975)**，**UNIX/BSD & TCP/IP(1981)**，**IEEE 802 标准(1980)**，**TCP/IP 统一(1983)**，**ARPANET 结束/NSFNET(1990)**，**AUP 商用化(1991)**，**日本商用ISP(1993)**，**vBNS/Internet2(1995–)**  
  局域网与 TCP/IP 的历史关键节点：从 ALOHA 到 ARPANET、以太网、TCP 原型、BSD 集成、IEEE 标准化、TCP/IP 成为事实标准、NSFNET 接力与互联网商用化  
- Japan academic backbones: **SINET1→6**（速度从 **100 Mbps → 400 Gbps**，并引入 **100 Gbps** 国际线路与 **5G** 协同）  
  日本学术主干网 SINET 演进：带宽提升与新一代光传输/5G  
- TCP/IP **4-layer** vs OSI **7-layer** 对照；**Network Interface 层/物理层** 定义传输介质  
  TCP/IP 四层模型与 OSI 七层模型的映射与分工  
- Physical media: **metal cables (coax / twisted pair)**、**fiber optics**、**electromagnetic waves**（无线/红外）  
  传输介质：金属线缆、光纤、电磁波  
- Ethernet naming: **aBASEb**（速率/基带/介质或距离）与 **baseband vs broadband** 的区别  
  以太网命名法与基带/宽带传输差异  
- Twisted-pair categories & wiring: **Cat3…Cat8**, **UTP/STP**, **straight vs cross**（MDI/MDI-X）  
  双绞线类别与布线类型  
- Line coding on Ethernet PHY: **NRZ / NRZI / Manchester / MLT-3** 与标准对应  
  物理层符号编码及其在不同以太网标准中的使用  
- Optics fundamentals: **EM spectrum**, **reflection/refraction (Snell)**, **total internal reflection**, **single vs multi mode**  
  光与电磁波基础、反射/折射/全反射、单模与多模光纤

---

## ⚪ Lecture Content 

### 1) LAN & TCP/IP: A Historical Thread / 历史脉络（LAN 与 TCP/IP）
- **1968 – ALOHA system**（University of Hawaii）  
  无线分组通信（岛际无线包传输）；以太网后来将 **介质从无线改为同轴**，提升**速率与可靠性**。  
- **1969 – ARPANET** 建成  
  **分组交换** 通信实验开展；**1972 年**已扩展到 **34** 个节点。  
- **1973 – Ethernet**（Xerox）  
  在**同轴电缆**上实现的局域网；理念承袭自 ALOHA（ALOHA 用无线）。  
- **1975 – TCP prototype** 完成；同一时期 **UNIX** 开始普及。  
- **1976 – Xerox PARC** 发表以太网论文（Ethernet 成熟化的里程碑）。  
- **1981 – UNIX (4.1BSD)** 集成 **TCP/IP**（Berkeley Software Distribution）。  
- **1980 – IEEE 802 标准化**  
  - **802.3**：CSMA/CD 与以太网（Ethernet）  
  - **802.4**：**Token Bus**（工厂 LAN；后衰退）  
  - **802.5**：**Token Ring**（IBM，4/16 Mbps；日本未普及）  
  - 讲义指出：**TokenBus/TokenRing** 的**有效转发效率**高（实速可达标称 **≈95%**），而 **CSMA/CD 以太网** 在冲突条件下的**有效吞吐**常仅 **≈50%**。  
- **1983 – TCP/IP** 成为 **ARPANET 等网络的标准协议**。  
- **1988 – ARPANET** 节点数达 **20 000**。  
- **1990 – 之后**  
  - 启动 **TCP/IP 的 ANSI 标准化**；**ARPANET 退役**，研究网移交 **NSFNET(1985-)**。  
  - **1991 – AUP**（可接受使用政策）**开放商用**目的，加速普及。  
  - **IETF** 引入开放的标准化流程（**个人可参与**）；**RFC** 作为公开征求意见/版本演进的载体。  
  - **10BASE-T（UTP）** 标准化使布线简化，LAN **全面普及**。  
  - **1993 – 日本**设立**商用 ISP**。  
- **1995–2000 – 美国骨干**  
  - **1995**：**NSFNET 停运**；**vBNS** 上线（接入 **NAP**，承载多骨干互联）。连接 **5** 个超算中心与企业骨干，使 **100** 所大学可接入。  
  - **1996**：**Internet2** 项目启动（研究教育社区高带宽需求；**100 Gbps** 级骨干；>210 高校、>70 企业、>45 非营利/政府接入；以 **vBNS** 为骨干）。  
  - **2000**：**vBNS+** 完全民营化。  :contentReference[oaicite:1]{index=1}

---

### 2) Japan Academic Backbones — SINET / 日本学术网 SINET
- 主导单位：**NII（国立情報学研究所）**  
- **SINET1（1992–）**：大型机终端协议（**不使用 TCP/IP**），**100 Mbps**；承接 **NACSIS** 网络。  
- **SINET2（2002–，SuperSINET）**：采用 **TCP/IP**，速率 **至多 10 Gbps**。  
- **SINET3（2007–）**：**至多 40 Gbps**。  
- **SINET4（2011–）**：**至多 40 Gbps**，强调 **高可靠化**。  
- **SINET5（2016–）**：**至多 400 Gbps**；**国际回线 100 Gbps**。  
- **SINET6（2022–）**：**400 Gbps 光传输**；与 **5G 无线**协同。  :contentReference[oaicite:2]{index=2}

---

### 3) TCP/IP 4-Layer vs OSI 7-Layer / TCP-IP 四层与 OSI 七层
- OSI：**物理 / 数据链路 / 网络 / 传输 / 会话 / 表示 / 应用**。  
- TCP/IP：**网络接口 / 网际(Internet) / 传输 / 应用**。  
- **映射**（讲义图示思想）：**OSI L1–L2**≈**TCP/IP 网络接口**；**OSI L3**↔**TCP/IP Internet**；**OSI L4**↔**TCP/IP Transport**；**OSI L5–L7**≈**TCP/IP Application**。  
- **传输介质** 由 **OSI 物理层** 或 **TCP/IP 网络接口层** 定义。  :contentReference[oaicite:3]{index=3}

---

### 4) Transmission Media — Types & Placement / 传输介质：类型与分层位置
- **Wired 有线**  
  1) **Metal cables 金属线缆**：  
     - **Coax 同轴**（讲义举例：可至 **1 Gbps**，距离 **≈3 600 m** 量级）；  
     - **Twisted Pair 双绞线**（**至 10 Gbps**，**100 m** 以内）。  
  2) **Fiber optics 光纤**：  
     - **Single-mode**（**至 10 Gbps**，**≈40 km**）；  
     - **Multi-mode**（**至 100 Gbps**，**≈2 km**）。  
- **Wireless 无线**  
  - **Infrared (IrDA)**（**至 16 Mbps**，**≈1 m**）；  
  - **Radio 2.4/5 GHz（Wi-Fi）**（**至 9.6 Gbps**，距离视标准而定）。  :contentReference[oaicite:4]{index=4}

---

### 5) Metal Cables — Coax & Twisted Pair / 金属线缆：同轴与双绞线
- **Twisted Pair（双绞线）**：两根铜线按一定 **pitch** 绞合成对并成束；**绞合抑制噪声**，**解绞会恶化抗干扰**。  
- **Coax（同轴）**：相较 UTP（非屏蔽双绞线）**更可靠**，但**成本更高**。  
- **比特传输**：利用**电压高/低**对应 **1/0**。  :contentReference[oaicite:5]{index=5}

---

### 6) Coax-based Ethernets / 同轴以太网（10BASE2/5）
- **10BASE2（Thinnet）** / **10BASE5（Thicknet）**；标称 **10 Mbps**（CSMA/CD）。  
- **总线型拓扑**；**半双工**（同一根线上收/发）。  
- **最大段长**：如 10BASE5 **500 m**。  
- **扩容方式**：10BASE2 用 **T 形接头**，10BASE5 用 **transceiver**；两者**增设主机需停网**处理。  :contentReference[oaicite:6]{index=6}

---

### 7) Star Ethernets on Twisted Pair / 双绞线星型以太网
- **10BASE-T / 100BASE-TX / 1000BASE-T** 使用 **双绞线**。  
- **星型**连接到 **Switching Hub** / Router；**增设主机无需停网**。  
- **Hub→Host 最长 100 m**；**全双工**（收发分线）。  
- **UTP / STP**：STP 比 UTP **更抗干扰**。  :contentReference[oaicite:7]{index=7}

---

### 8) “aBASEb” Naming / 以太网命名法
- **a**：速率（**10/100/1000/10G/100G**；**1 M = 1000，1 G = 1000 M = 1 000 000**）。  
- **BASE**：**Baseband（基带）**（另有 **BROAD**：Broadband 宽带）。  
- **b**：  
  - **数字**：如 **5 → 500 m**，**2 → 185 m**（传统同轴段长代号）；  
  - **字母**（介质/波长）：**T**=Twisted Pair，**F**=Fiber；S/L/E = **850/1300/1550 nm** 波段。  
- 例：**1000BASE-T** → **1000 Mbps/基带/双绞线**。  :contentReference[oaicite:8]{index=8}

---

### 9) Baseband vs Broadband / 基带与宽带传输
- **Baseband 基带**：**数字信号直接**上线传输（不经调制）；以太网有线常用。  
  - 典型码型：**NRZ、（单/复流）NRZ/NZ**、**Bipolar**、**Manchester** 等。  
- **Broadband 宽带**：将数字**调制为模拟**发送，接收端**解调**复原；**Modem** 常用；  
  - 典型调制：**AM/FM/PM/QAM**（振幅/频率/相位/幅相）。  :contentReference[oaicite:9]{index=9}

---

### 10) Twisted Pair Categories / 双绞线类别（Cat）
- 类别与绞合 **pitch** 相关，决定可支持的 **速率/频宽**（以及使用的**对数**）：  
  - **Cat3**：10BASE-T（**2 对**）  
  - **Cat4**：Token Ring（**2 对**）  
  - **Cat5**：100BASE-TX（**2 对**）  
  - **Cat5e**：1000BASE-T（**4 对**）  
  - **Cat6/6A**：千兆/10G（讲义示例为“1000BASE-T/-TX”，**4 对**）  
  - **Cat7**：10GBASE-T（**4 对**）  
  - **Cat8**：40GBASE-T（**4 对**）  
- **Straight vs Cross**：  
  - **Straight**：PC ↔ 交换机（常用）；  
  - **Cross**：**交换机↔交换机** 或 **PC↔PC**；  
  - 现代交换机多具 **Auto-MDI/MDI-X**，除 **PC↔PC** 外通常无需关心交叉。  :contentReference[oaicite:10]{index=10}

---

### 11) Line Coding on Ethernet PHY / 以太网物理层符号编码
- **NRZ**：1→High，0→Low；用于 **1000BASE-X（光）**。  
- **NRZI**：遇到“1”时电平翻转；用于 **100BASE-FX（光）**。  
- **Manchester**：周期中点翻转；用于 **10BASE-5/2/T（铜）**。  
- **MLT-3**：在 1 时在 **0 → +E → 0 → −E → 0** 循环；用于 **100BASE-TX（铜）**。  :contentReference[oaicite:11]{index=11}

---

### 12) Fiber Optic Cabling / 光纤布线基础
- 标准：**1000BASE-LX/SX、100BASE-FX** 等。  
- **光纤束**可至 **100 芯**并外覆钢丝；**上下行各 1 芯** → 两芯构成**全双工**。  
- **发光/不发光（ON/OFF）** 对应比特信息。  
- **单模（SMF）**：波长 **1300/1550 nm**；**远距离/低色散**；材料纯度高、**成本高**。  
- **多模（MMF）**：波长 **850/1300 nm**；**多模并行**，**短距离高带宽**，材料可为塑料，**成本低**。  :contentReference[oaicite:12]{index=12}

---

### 13) Electromagnetic Waves & Optics / 电磁波与光学要点
- **电磁波**：光既是**波**也是**光子**；**波长 λ** 与 **频率 f** 反比；**能量 E** 随 **λ 变短而增大**（短波更具破坏性）。  
- **光谱**：γ 射线 / X 射线 / 紫外 / **可见光** / 红外 / **电波**（从短到长）。  
- **矢量关系**：电场与磁场 **彼此垂直** 且 **均与传播方向垂直**。  :contentReference[oaicite:13]{index=13}

---

### 14) Reflection & Refraction（Snell）/ 反射与折射（斯涅尔定律）
- **反射定律**：**入射角 = 反射角（θ₁ = θ₂）**（与媒质无关）。  
- **折射定律**：入射到不同介质时方向改变，满足 **sinθ₁/sinθ₃ = n₂/n₁**。  
- 光学元件（如**透镜**）通过折射**汇聚光线**。  :contentReference[oaicite:14]{index=14}

---

### 15) Total Internal Reflection & Fiber / 全反射与光纤导光
- 从**高折射率介质**入射到**低折射率介质**时，入射角减小到某临界值以下会出现**全反射**（光**无法进入**第二介质）。  
- 光纤结构：**Core（核）**折射率**高**，**Cladding（包层）**折射率**低** → 光在 **Core** 内**全反射**传输**不泄露**。  
- 讲义步骤图：  
  - (A) 普通折射；(B) 入射角更小 → 边界沿向；(C) 再小 → **全反射**（不入射）。  :contentReference[oaicite:15]{index=15}

---

### 16) Single vs Multi-Mode / 单模与多模
- **Single-mode（SMF）**：  
  - **仅 1 模态** 传播，**色散/波形劣化小**，**可长距**；  
  - 常用**高纯度石英**，**成本高**；**大容量长距**干线优选。  
- **Multi-mode（MMF）**：  
  - **多模共存**，**模式色散大**、**长距困难**；  
  - 支持**大容量**但以**短距**为宜；常见**塑料**材质，**成本低**。  :contentReference[oaicite:16]{index=16}

---

## Key Points 
- 历史纵线（**ALOHA → ARPANET → Ethernet → TCP/IP → NSFNET → vBNS/Internet2**）与日本 **SINET1–6（100 Mbps→400 Gbps）** 的节点年份、里程碑与带宽提升。  
- IEEE **802.3/4/5** 的定位与 **TokenBus/TokenRing** 在**有效吞吐**上的优势对比 **CSMA/CD**（讲义数值：**≈95% vs ≈50%**）。  
- **TCP/IP 四层 ↔ OSI 七层** 的对应；**物理/网络接口层** 定义传输介质。  
- 介质参数：**同轴/双绞/光纤/红外/无线** 的**速率—距离**范围（按讲义所列），以及**星型 vs 总线型**、**半/全双工** 的差异。  
- **aBASEb** 命名与 **Baseband/Broadband** 概念；**Cat3–Cat8、UTP/STP、Straight/Cross** 的应用与 **MDI-X** 自适应。  
- 物理层**符号编码**：**NRZ/NRZI/Manchester/MLT-3** 对应 **1000BASE-X / 100BASE-FX / 10BASE-5/2/T / 100BASE-TX**。  
- 光学基础：**EM 光谱、反射/折射/斯涅尔、全反射**；光纤结构与 **SMF/MMF** 的**距离/带宽/成本**取舍。  :contentReference[oaicite:17]{index=17}

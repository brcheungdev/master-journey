[← Back to Course README / 返回课程目录](./README.md#toc)

#  My notes
- This folder contains my notes, thoughts, and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor: Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 8: Beyond Ethernet/Wi-Fi — L2/L3 Devices, VLAN & 802.1Q, IPv6 Basics, Global IP Assignment  
# 超越以太网/无线局域网：L2/L3 设备、VLAN 与 802.1Q、IPv6 基础与公网 IP 分配

---

## ⚪ Lecture Overview 
- Limits of **shared-medium Ethernet (CSMA/CD)**: collisions & efficiency (~50%) vs **token** systems (~95%).  
  共享介质以太网（CSMA/CD）的局限：碰撞多、吞吐最高约 50%，对比令牌网可达约 95%。 
- Non-Ethernet/Wi-Fi data links: **ATM, FDDI, Fibre Channel, IEEE1394, USB, HDMI, iSCSI, InfiniBand** — roles, speeds, media.  
  以太/无线之外的数据链路：各自用途、速率与介质。 
- **Global IP** assignment: **ICANN → JPNIC → ISP → user**；**Dynamic vs Static** globals & **DDNS** for servers.  
  全球 IP 分配链；动态/固定公网 IP 及 DDNS 场景。
- **IPv6** addressing & header fields; notation & abbreviation.  
  IPv6 地址与首部，表示与省略规则。
- L2/L3 devices: **Repeater, Bridge, Switching Hub (L2), Router, L3 Switch**；**learning & forwarding**；**flow control (PAUSE)**。  
  二层/三层设备与学习转发、拥塞控制（暂停帧）。 
- **VLAN** basics, **Trunk** & **802.1Q tag** (TPID/PCP/CFI/VID)，跨交换机的多 VLAN 传输。  
  VLAN 与干道、标签字段与跨设备传递。

---

## ⚪ Lecture Content 

### 1) Issues with Shared-medium Ethernet / 共享介质以太网的问题

- As Ethernet became widespread, a single shared segment could have **≈100 hosts**, causing **frequent collisions**; under heavy load, everybody is “always sending,” so **efficiency tops out around ~50%**.  
  以太网普及后，单条共享链路上的主机数量可达 **≈100 台**，**冲突**频发；高负载时各节点“总在发送”，**效率最多约 ~50%**。  

- **Token Bus/Token Ring** can reach **≈95% efficiency** under saturation.  
  **Token Bus/Token Ring** 在饱和状态下**效率可达 ≈95%**。  

- *High-level:* more hosts → more collisions; contention collapses throughput vs token passing.  
  *要点：* 主机越多 → 冲突越多；竞争接入在高负载下吞吐崩塌，而令牌传递保持高效率。  

<details>
<summary><strong>Notes / 补充说明（点击展开）</strong></summary>

- In **CSMA/CD** shared media, a **single collision domain** means any two simultaneous transmissions collide; as load increases, the probability of collision rises **non-linearly**, forcing repeated **backoff** and retransmissions.  
  在 **CSMA/CD** 共享介质中，一个**单一冲突域**使任意两台同时发送都会冲突；负载升高时冲突概率**非线性上升**，导致频繁**退避**与重传。  

- Token systems **serialize** access via a circulating **token**: only the holder may transmit, so utilization remains high even when busy (no collision cost).  
  令牌网络通过在节点间循环的**令牌**来**串行化**发送权：只有持有令牌者可发送，因此即使繁忙也能保持高利用（无冲突代价）。  

- Modern switched, **full-duplex** Ethernet breaks the shared medium into **per-link** segments, eliminating collisions altogether (topic continued in later sections).  
  现代交换式、**全双工**以太网把共享介质拆成**逐链路**的点到点段，**消除了冲突**（后续章节继续展开）。

</details>


---

### 2) Data Links beyond Ethernet/Wi-Fi / 以太与无线之外的链路

- **ATM (Asynchronous Transfer Mode)**  
  Fixed-length **53-byte cells = 5B header + 48B payload**; **no built-in congestion control** (handled by higher layers/network).  
  固定长度 **53 字节单元 = 5B 头 + 48B 载荷**；**无内建拥塞控制**（由上层/网络侧配合）。  
  *Fixed-size cells simplify hardware switching; AAL adapts voice/data.*  
  *固定长度便于硬件交换；AAL 适配语音/数据业务。*

- **FDDI (Fiber Distributed Data Interface)**  
  Token-ring over fiber; **100 Mbps**; **dual counter-rotating rings** for resilience; up to **≤500 stations**, **~100 km** total (MMF point-to-point **≤2 km**).  
  基于光纤的令牌环；**100 Mbps**；**双反向环**容错；**≤500 站**、全网**~100 km**（多模点到点 **≤2 km**）。  
  *Common as enterprise/campus backbones in the 90s.*  
  *90 年代企业/园区主干常见。*

- **Fibre Channel (SAN)**  
  Storage-area networking; speeds up to **128 Gbps**; **low latency/high reliability**; topologies: point-to-point, arbitrated loop, switched.  
  面向存储区域网；速率至 **128 Gbps**；**低时延/高可靠**；支持点到点、仲裁环、交换等拓扑。  
  *Often connects RAID/tape libraries and datacenter storage.*  
  *常用于连接 RAID/磁带库与数据中心存储。*

- **IEEE 1394 (FireWire/i.LINK)**  
  Up to **3.2 Gbps**; supports **isochronous + asynchronous** transfers; popular for AV/pro video.  
  最高 **3.2 Gbps**；支持**等时/异步**传输；家用/专业 **AV** 互联常见。  
  *Isochronous channels guarantee media bandwidth/timing.*  
  *等时信道保障媒体带宽与时序。*

- **USB**  
  Up to **40 Gbps (USB4)**; data + power; widely used from peripherals to docks/displays.  
  最高 **40 Gbps（USB4）**；数据+供电；从外设到坞站/显示广泛应用。  
  *Can tunnel PCIe/DisplayPort; Type-C is ubiquitous.*  
  *可隧道承载 PCIe/DP；Type-C 已普及。*

- **HDMI**  
  Single-cable audio/video with HDCP; since **1.4** can **carry TCP/IP** in certain ecosystems (Ethernet over HDMI) with CEC control.  
  单线音视频并支持 HDCP；自 **1.4** 起在部分生态中可**承载 TCP/IP**（以太 over HDMI），并有 CEC 控制。  
  *Mainstream interface for TVs/monitors/home theater.*  
  *电视/显示器/家庭影院主流接口。*

- **iSCSI**  
  **SCSI over TCP/IP**; up to **40 Gbps** (per underlying Ethernet); FC-like semantics with **lower cost** and simpler deployment.  
  **SCSI over TCP/IP**；取决以太层可达 **40 Gbps**；语义类似 FC，但**成本更低**、部署更简。  
  *Leverages existing IP/Ethernet networks for storage.*  
  *复用现有 IP/以太网络承载存储流量。*

- **InfiniBand**  
  Up to **~600 Gbps** (HDR/NDR/…); **ultra-low latency**, **RDMA**; dominant in HPC/AI clusters.  
  最高 **~600 Gbps**（HDR/NDR/…）；**极低时延**、支持 **RDMA**；HPC/AI 集群主流互连。  
  *Lossless fabric with queue-pair verbs over a switched topology.*  
  *基于交换结构的无损网络，提供队列对列（QP）动词接口。*

<details>
<summary><strong>Notes / 补充说明（点击展开）</strong></summary>

- **When to use what / 如何选型**  
  - **ATM**: historically for QoS backbones/access; mostly legacy now.  
    **ATM**：历史上用于带 QoS 的骨干/接入；如今多为遗留。  
  - **FDDI**: former campus fiber backbone; replaced by GigE/10G/40G.  
    **FDDI**：曾为园区主干；已被千兆/万兆以太替代。  
  - **Fibre Channel vs iSCSI**: FC excels in perf/reliability on dedicated fabrics; iSCSI wins on cost/ease over IP networks.  
    **FC vs iSCSI**：FC 在专网中性能/可靠性更强；iSCSI 基于 IP 网，**性价比/易用性**更优。  
  - **InfiniBand**: choose for HPC/AI when bandwidth×latency efficiency and RDMA matter most.  
    **InfiniBand**：HPC/AI 优选，强调带宽×时延效率与 RDMA。  
  - **USB/HDMI/1394**: endpoint/AV-centric rather than general L2 segments.  
    **USB/HDMI/1394**：偏终端与音视频互联，非通用二层网段。

- **Interop tips / 互操作提示**  
  - Gateways/bridges can translate between **FC↔Ethernet** (FCoE/iSCSI) or **IB↔Ethernet**.  
    可通过网关在 **FC↔以太（FCoE/iSCSI）** 或 **IB↔以太** 间转换。  
  - Evaluate **bandwidth, latency, jitter, distance, cost, ecosystem** jointly.  
    选型需综合 **带宽/时延/抖动/距离/成本/生态**。

</details>


---

### 3) Global IP Address Assignment / 全球 IP 地址分配

- **ICANN** manages global Internet number resources; **JPNIC** allocates within Japan (the sole authorized body).  
  **ICANN** 负责全球互联网编号资源；**JPNIC** 负责日本境内的分配（唯一合法机构）。  
  End users do **not** apply to JPNIC directly; an **ISP** applies on behalf of users and assigns addresses.  
  最终用户**不直接**向 JPNIC 申请；由 **ISP（运营商）** 代为申请并下发地址。  

- To access the public Internet, you need a **globally unique** **Global IP**. **Private IPs** must go through **NAT** on the edge router to be used on the Internet:  
  上公网需要**全球唯一**的 **公网 IP（Global IP）**。**私有 IP** 必须在边界路由器上通过 **NAT** 转换后才能被公网使用：  

  ```
  Private LAN  --(NAT on Router)-->  Global Internet
  ```
**Implication:** NAT maps **many private (internal) addresses** to **a small pool of public addresses**, masking the internal topology.

**含义：**NAT 会把**多个内网（私有）地址**映射到**少量公网地址**，从而**隐藏内部拓扑**。
  

**Dynamic vs Static Global IP / 动态与固定公网 IP**

- **Dynamic / 动态**  
Common for home/consumer access; your IP **changes** periodically or after router reboot.  
家庭/普通接入常见；公网 IP 会**定期变化**或重启路由器后变化。  

- **Static / 固定**  
Hosting public-facing services (Web/Mail, etc.) typically **requires a static IP**; if you only have a dynamic IP, use **DDNS** to keep your domain pointing to the current address.  
对外发布 Web/邮件等服务通常**需要固定公网 IP**；若只有动态 IP，可用 **DDNS** 动态更新域名解析到当前地址。  

- **Example / 示例**  
Access by IP directly is possible (e.g., `https://153.127.246.22`) when DNS is unavailable.  
在 DNS 不可用时，可直接用 IP 访问（如 `https://153.127.246.22`）。  

<details>
<summary><strong>Notes / 补充说明（点击展开）</strong></summary>

- **Allocation chain / 分配链路**：IANA/ICANN → RIR（如 APNIC/ARIN/RIPE…）→ NIR（日本为 JPNIC）→ ISP/企业 → 终端用户。  
- **NAT variants / NAT 形态**：SNAT/DNAT、NAPT（端口复用）、CGNAT（运营商级 NAT）。  
- **Static IP tips / 固定 IP 实务**：建议搭配**反向解析（PTR）**与**合规的 rDNS**，邮件服务器尤其重要。  
- **DDNS usage / DDNS 使用**：路由器或客户端守护进程定期将当前公网 IP 更新到 DNS 供应商。  
- **Security / 安全提示**：公网暴露服务需配合**防火墙、ACL、端口限速**与**证书/密钥管理**。  

</details>

   
--- 
### 4) IPv6 Addressing & Header / IPv6 地址与首部
- **Background:** The **global IPv4 address pool was exhausted in 2011/02**, which accelerated the push toward **IPv6**; however, because IPv4 can still be used (via NAT, reclaiming, etc.), the migration has been relatively slow.  
  **背景：****IPv4 全球地址在 2011/02 枯竭** → 推动 **IPv6** 部署；但由于 IPv4 仍可继续使用（如 NAT、回收再分配等），迁移进展**相对缓慢**。

- **128-bit unsigned integer:** An IPv6 address is **128 bits**, written as **8 groups of 16 bits** each, represented in **hexadecimal** and separated by **colons**.  
  **128 位无符号整数：**IPv6 地址为 **128 位**，书写为 **8 组 16 位**，每组用 **十六进制**表示并以**冒号**分隔。

```
FEDC:BA98:7654:3210:FEDC:BA98:7654:3210
```
- **Zero compression allowed:** One **contiguous run** of 16-bit zero groups may be replaced by `::`, and this may be used **at most once per address** (e.g., `1080::8:800:200C:417A`).  
  **允许 0 压缩：**一段**连续的 16 位全 0 组**可用 `::` **压缩且每个地址最多一次**（如 `1080::8:800:200C:417A`）。

> Tip / 提示：You may also **omit leading zeros** within each 16-bit group  
> 还可**省略每组前导零**，例如  
> `2001:0db8:0000:0000:0000:ff00:0042:8329` → `2001:db8::ff00:42:8329`

**IPv6 Header / IPv6 首部字段**
```
|Version|Traffic Class|Flow Label|Payload Length|Next Header|Hop Limit|
|                  Source Address (128 bits)                 |
|               Destination Address (128 bits)               |
|        (Extension Headers ... as indicated)                |
|                       Upper-layer Data                     |

```
- **Version = 6**; **Traffic Class** ≈ IPv4 **TOS**; **Flow Label** is intended for QoS and is rarely used today.  
  **版本 = 6**；**Traffic Class** 近似 IPv4 的 **TOS**；**Flow Label** 预期用于 QoS，当前较少使用。  
- **Payload Length**: length of the payload **excluding** the IPv6 header; **Next Header** is analogous to IPv4 **Protocol**; **Hop Limit** is analogous to IPv4 **TTL**.  
  **Payload Length（有效载荷长度）**：**不包含** IPv6 头部本身；**Next Header** 类似于 IPv4 的 **Protocol**；**Hop Limit** 类似于 IPv4 的 **TTL**。  
- **Source / Destination Address**: **128 bits each**; may be followed by multiple **Extension Headers** chained via **Next Header**.  
  **源/目的地址**：**各 128 位**；之后可通过 **Next Header** 串联多个**扩展头（Extension Headers）**。

   
--- 
### 5) Network Devices & Layers / 网络设备与分层

- **Repeater (L1) — regeneration (amplify/reshape); does not check FCS, so errored bits are repeated.**  
  **中继器（L1）— 物理层再生（放大/整形）；不检查 FCS，因此出错比特也会被转发。**
- **Bridge (L2) — forwards only frames with valid FCS; does not interconnect different L3 IP subnets.**  
  **网桥（L2）— 仅转发 FCS 校验正确的帧；不负责不同三层（L3）网段的互通。**
- **Switching Hub / L2 Switch — each port acts like a bridge; builds a MAC address table and forwards only to the destination port.**  
  **交换式集线器 / 二层交换机 — 各端口等同于网桥；学习并维护 MAC 地址表，只定向转发到目的端口。**
- **Router (L3) — connects different IP networks; forwards IP packets by routing; can interconnect heterogeneous L2 (e.g., Ethernet ↔ FDDI).**  
  **路由器（L3）— 连接不同 IP 网络；按路由转发 IP 包；可在异构二层之间互联（如 Ethernet ↔ FDDI）。**
- **L3 Switch — a switch with hardware L3 forwarding (routing) for high throughput.**  
  **三层交换机 — 集成硬件三层转发（路由）的交换机，用于高吞吐。**

#### MAC Learning & Forwarding / 学习与转发
- **On startup, the switch’s MAC table is empty.**  
  **交换机启动时 MAC 表为空。**
- **Upon receiving a frame, learn “Source MAC → ingress port”.**  
  **收到帧后学习“源 MAC → 入端口”的映射。**
- **If Destination MAC is known, forward only to that port; otherwise, flood within the broadcast domain (unknown unicast).**  
  **命中目的 MAC 则仅转发到对应端口；未命中则在广播域内泛洪（未知单播）。**
- **Age out stale entries so the table adapts to topology changes.**  
  **老化过期表项，以适应拓扑变化。**

```
(1) Initial: MAC table is empty.  
    初始：MAC 表为空。
(2) Upon receiving a frame: record **Source MAC → inbound port**.  
    收到帧：记录 **源 MAC → 入端口**。
(3) On subsequent communication: if **Destination MAC** is learned, forward **only to the mapped port** (otherwise flood).  
    再次通信：若已学习到**目的 MAC**，则**仅转发到对应端口**（否则进行泛洪）。
```
- **Auto-negotiation**: automatically selects **speed (10M / 100M / 1G / 10G)**, **duplex (half/full)**, and **pairing (Auto-MDI/MDI-X)** for straight/crossover compatibility.  
  **自协商（auto-negotiation）**：自动协商 **速率（10M / 100M / 1G / 10G）**、**双工（半/全双工）** 与 **线序（Auto-MDI/MDI-X）**，从而兼容直通/交叉网线。
 
---

### 6) From Collisions to Full-Duplex / 从碰撞到全双工

- **Repeater Hub (shared bus)**: all ports broadcast on the same medium and most links are **half-duplex → collisions occur**.  
  **Repeater Hub（共享总线）**：所有端口在同一介质上广播，且多为**半双工 → 产生碰撞**。
- **Switch + Twisted Pair**: separate transmit/receive pairs enable **full-duplex**; the switch **forwards only to the destination port → no collisions**, improving efficiency.  
  **Switch + 双绞线**：收发对线分离，实现**全双工**；交换机**仅转发到目的端口 → 无碰撞**，效率提升。
- **High efficiency can still trigger congestion**: when switch buffers overflow, the device sends **PAUSE (IEEE 802.3x)** to ask the sender to temporarily throttle.  
  **效率高也可能诱发拥塞**：交换机缓冲溢出时，会发送 **PAUSE（IEEE 802.3x）** 帧请求对端暂缓发送。
  
<details>
<summary><strong>Supplement / 补充</strong></summary>

- **Collision domain vs. broadcast domain**: a switch removes **collision domains** per port but the **broadcast domain** remains within a VLAN.  
  **碰撞域 vs 广播域**：交换机将**碰撞域**隔离到每个端口，但 **VLAN 内的广播域**依旧存在。  
- **PAUSE scope**: 802.3x PAUSE applies **per link** and may cause head-of-line blocking; modern networks often use **priority flow control (PFC)** within Data Center Bridging.  
  **PAUSE 作用域**：802.3x 为**链路级**暂停，可能引发队首阻塞；数据中心常用 **PFC**（优先级流控）细粒度限流。  
- **Duplex mismatch**: ensure both ends negotiate **full-duplex** (or both fixed) to avoid late collisions and severe throughput drops.  
  **双工不匹配**：需保证两端一致为**全双工**（或同时固定），避免晚碰撞与吞吐骤降。  

</details>

   
---

### 7) VLAN & L3 Switch / 虚拟局域网与三层交换

- **VLAN (Virtual LAN)**: at **L2**, a single physical switched network is **logically split** into multiple **broadcast domains**.  
  **VLAN（虚拟局域网）**：在 **二层**将一套物理交换网络**逻辑分割**为多个**广播域**。  
- **Port-based VLAN** (common): assign ports to VLANs; **inter-VLAN communication** requires a **Router** or an **L3 Switch**.  
  **端口型 VLAN**（常见）：按端口划分 VLAN；**VLAN 间通信**需要 **路由器** 或 **三层交换机**。  
- **Multi-switch / multi-floor VLANs**: use **Trunk Ports (Trunk Links)** between switches to carry **multiple VLANs**.  
  **跨交换机/跨楼层 VLAN**：交换机之间使用 **Trunk 端口（干道链路）** 承载**多 VLAN** 流量。  
- VLAN identification across trunks uses the **802.1Q Tag**; when forwarding to an access host port, the switch **strips the tag**.  
  干道上通过 **802.1Q 标签**标识 VLAN；转发至接入端口（主机口）时交换机会**剥离标签**。  

**802.1Q VLAN Tag** *(inserted between SrcMAC and Type)* / **802.1Q VLAN 标签**（插入在 源MAC 与 Type 之间）
- **TPID (16b)**: fixed **0x8100**, marks an 802.1Q-tagged frame.  
  **TPID（16 位）**：固定 **0x8100**，标识 802.1Q 帧。  
- **PCP (3b)**: **priority** (8 levels, 0–7).  
  **PCP（3 位）**：**优先级**（8 级，0–7）。  
- **DEI/CFI (1b)**: drop eligibility / canonical format indicator (**0** in Ethernet).  
  **DEI/CFI（1 位）**：可丢弃/规范格式指示（以太网中通常为 **0**）。  
- **VID (12b)**: **VLAN ID** (valid range **1–4094**; 0 and 4095 reserved).  
  **VID（12 位）**：**VLAN 标识**（有效范围 **1–4094**；0 与 4095 保留）。  

**802.1Q frame layout / 802.1Q 帧结构**

```
| DestMAC | SrcMAC | 0x8100 | PCP |CFI|   VID   |  Type  | Payload ... | FCS |
```


<details>
<summary><strong>Supplement / 补充</strong></summary>

- **Access vs Trunk ports**: Access carries **one** VLAN and sends **untagged** frames to hosts; Trunk carries **multiple** VLANs with **802.1Q tags**.  
  **接入口 vs 干道口**：接入口承载**单一** VLAN，向主机发送**无标签**帧；干道口承载**多个** VLAN，使用 **802.1Q** 标签。
- **Native VLAN**: on some vendors, the **native VLAN** on a trunk is sent **untagged**; ensure trunks on both ends agree to avoid VLAN leaks.  
  **本征 VLAN**：部分设备上干道的**本征 VLAN**帧为**无标签**；需两端一致以防 VLAN“泄露”。
- **Inter-VLAN routing**: L3 switch provides **SVIs (Switch Virtual Interfaces)**—one IP per VLAN—to route between VLANs at line rate.  
  **VLAN 间路由**：三层交换通过 **SVI（虚接口）**为每个 VLAN 提供一个三层网关，实现线速路由。
- **QoS with PCP**: higher **PCP** can prioritize traffic (e.g., voice) across trunks; mapping to queue/DSCP is platform-specific.  
  **PCP 与 QoS**：较高 **PCP** 可在干道上优先传送（如语音）；与队列/DSCP 的映射依设备实现。
</details>

**Note / 说明**：Between switches, **Trunk** links carry **tagged** frames (802.1Q); **Access** ports deliver **untagged** frames to end hosts.  
**注**：交换机之间的 **Trunk** 链路传输**带标签**的 802.1Q 帧；**接入端口（Access）** 向主机送达的帧通常**不带标签**。
 
---

## Key Points / 关键要点

- **Shared-medium Ethernet efficiency** is low under heavy load (≈50%); **token networks** can reach ≈95%.  
  **以太网共享介质**在高负载下效率低（≈50%）；**令牌网**可达 ≈95%。
- Know the major **non-Ethernet/Wi-Fi links**: **ATM (53-byte cells) / FDDI (100 Mbps dual ring) / Fibre Channel (to 128G) / IEEE 1394 (3.2G) / USB (40G) / HDMI (IP over HDMI from 1.4) / iSCSI (to 40G) / InfiniBand (to 600G)**.  
  认识多种**非以太/无线链路**：**ATM（53B 单元）/ FDDI（100 Mbps 双环）/ FC（至 128G）/ 1394（3.2G）/ USB（40G）/ HDMI（1.4 起可承载 IP）/ iSCSI（至 40G）/ InfiniBand（至 600G）**。
- **Global IP assignment chain**: ICANN → JPNIC → ISP → end user. **Dynamic** addresses change; **servers** typically need a **static IP** or **DDNS**.  
  **全球 IP 分配链**：ICANN → JPNIC → ISP → 用户。**动态**地址会变化；**服务器**通常需要**固定 IP**或**DDNS**。
- **IPv6**: 128-bit, colon-hex notation with `::` zero compression; header includes **Version / TrafficClass / FlowLabel / PayloadLength / NextHeader / HopLimit / Addresses**.  
  **IPv6**：128 位，冒号十六进制，支持 `::` 零压缩；首部含 **Version / TrafficClass / FlowLabel / PayloadLength / NextHeader / HopLimit / Addr**。
- **L2/L3 devices**: Repeater (L1 regeneration), Bridge (L2 filtering), Switch (MAC learning & forwarding), Router (L3 forwarding), L3 Switch (routing inside a switch).  
  **二层/三层设备**：中继器（L1 放大/整形）、网桥（L2 过滤）、交换机（学习转发）、路由器（L3 转发）、三层交换机（交换机内置路由）。
- **Collision-free Ethernet**: switch + twisted pair for **full-duplex**; when congested, devices may send **PAUSE (802.3x)**.  
  **无碰撞以太**：交换机 + 双绞线实现**全双工**；拥塞时可发送 **PAUSE（802.3x）**。
- **VLANs**: L2 logical segmentation; **Trunks** carry multiple VLANs using **802.1Q (TPID=0x8100, PCP, CFI, VID)** across switches.  
  **VLAN**：L2 逻辑分段；**Trunk** 通过 **802.1Q（TPID=0x8100，PCP，CFI，VID）** 在交换机之间承载多 VLAN。

---

## ※※ Supplementary Cheat Sheets | 速查单

### IPv6 & VLAN Quick Reference
- [IPv6 Header Fields | IPv6 首部字段速查表](./figs/lecture08_ipv6_header_fields.md)  
  *IPv6 首部结构、字段含义与地址表示规则*

- [IEEE 802.1Q VLAN Tag | VLAN 标签与端口模式](./figs/lecture08_vlan_8021q_tag.md)  
  *802.1Q 标签字段、Trunk/Access 概念与帧结构示意*

<h2></h2>

[← Previous Lecture / 上一章](./lecture07.md) · [Next Lecture / 下一章](./lecture09.md) · [Back to Course Directory / 返回课程目录](./README.md#toc)

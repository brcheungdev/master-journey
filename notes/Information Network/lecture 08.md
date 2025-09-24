#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 8: Beyond Ethernet/Wi-Fi — L2/L3 Devices, VLAN & 802.1Q, IPv6 Basics, Global IP Assignment  
# 情報ネットワーク概論 第8回：イーサネット/無線LAN以外のL2技術・L2/L3機器・VLAN/802.1Q・IPv6基礎・グローバルIP割り当て

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
- 普及导致单段主机多（可至 **≈100** 台），**冲突**频发；高负载时“总在发送”，**效率最多约 50%**。  
  Token Bus/Token Ring 在饱和下效率可达 **≈95%**。  
  *High-level:* more hosts → more collisions; contention collapses throughput vs token passing. 

---

### 2) Data Links beyond Ethernet/Wi-Fi / 以太与无线之外的链路
- **ATM**（Asynchronous Transfer Mode）  
  固定长 **53-byte cell = 5B header + 48B payload**；无内建拥塞控制功能。
- **FDDI**（Fiber Distributed Data Interface）  
  光纤令牌环；**100 Mbps**；**双环**具备故障备援；**≤500** 站、**最远 100 km**（MMF 点到点 **≤2 km**）。 
- **Fibre Channel**（SAN）  
  面向存储区域网；速率至 **128 Gbps**；高可靠。
- **IEEE1394（FireWire/i.Link）**  
  最高 **3.2 Gbps**；家用 AV 互联。
- **USB**  
  最高 **40 Gbps（USB4）**。
- **HDMI**  
  一线传输音视频；具版权保护；**1.4 起可承载 TCP/IP**（以太 over HDMI 生态）。
- **iSCSI**  
  将 **SCSI** 命令封装在 **TCP/IP**；最高 **40 Gbps**；与 FC 类似但更低成本。
- **InfiniBand**  
  最高 **600 Gbps**；面向服务器/集群，**高带宽、低时延**。

---

### 3) Global IP Address Assignment / 全球 IP 地址分配
- **ICANN** 负责全球资源；**JPNIC** 负责日本的分配事项（唯一合法机构）。  
  用户并不直接向 JPNIC 申请；由 **ISP** 代表用户向 JPNIC 申请并分配。 
- 出网需使用**全球唯一**的 **Global IP**；**私有 IP** 需经 **NAT** 转换后上网：  
  ```
  Private LAN  --(NAT on Router)-->  Global Internet
  ```
  Implication: NAT 将内网多地址映射到公网地址上

Dynamic vs Static Global IP / 动态与固定公网 IP
- **动态**：家庭/普通接入常用；定时或重启路由器后 **IP 变化**。
- **固定**：对外发布 Web/邮件 等服务器需固定地址；若为动态，则需要 **DDNS** 动态变更域名解析。
- **示例**：通过 https://153.127.246.22
 亦可直达站点
   
--- 
### 4) IPv6 Addressing & Header / IPv6 地址与首部
- 背景：**IPv4 全球地址 2011/02 枯竭** → 推进 **IPv6**；但因 IPv4 可继续用，迁移较缓。
- **128-bit** 无符号整数：写作 **8 组 16bit**，每组以 **16 进制** 表示并以 **冒号**分隔：
```
FEDC:BA98:7654:3210:FEDC:BA98:7654:3210
```
允许 0 压缩：连续`0:` 可在仅一处记作`::`（如 `1080::8:800:200C:417A`）。

IPv6 Header / IPv6 首部字段
```
|Version|Traffic Class|Flow Label|Payload Length|Next Header|Hop Limit|
|                  Source Address (128 bits)                 |
|               Destination Address (128 bits)               |
|        (Extension Headers ... as indicated)                |
|                       Upper-layer Data                     |

```
- Version=6；Traffic Class≈ IPv4 TOS；Flow Label 预期用于 QoS（当前鲜用）。
- Payload Length：不含 IPv6 头的长度；Next Header 类似 IPv4 Protocol；Hop Limit 类似 IPv4 TTL。
- Src/Dst：各 128 bit；可跟多个 扩展头（Next Header 链表）。
   
--- 
### 5) Network Devices & Layers / 网络设备与分层
- **Repeater（中继器）**：L1 物理层再生（放大/整形）；**不检查 FCS**，错误比特亦转发。
- **Bridge（网桥）**：L2 依据帧 **FCS** 仅转发“未损坏帧”；不负责不同三层网段互通。
- **Switching Hub（交换式集线器 / L2 Switch）**：各端口具桥功能，形成 **MAC 地址表**，只转发到目的端口。
- **Router（路由器）**：L3 连接不同网段；依据路由选择 **转发 IP 包**；可连接不同的二层技术（如 Ethernet ↔ FDDI）。
- **L3 Switch**：在交换设备中集成 **路由功能**。

MAC Learning & Forwarding / 学习与转发
- 交换机启动时** MAC 表为空**；每次收到帧，从** 源 MAC** 学习“MAC ↔ 端口”映射，逐步完善表项；
查到**目的 MAC**即定向转发，未命中则泛洪。
```
(1) 初始：MAC 表为空
(2) 收到帧：记录 源MAC→入端口
(3) 再通信：目的MAC已学到 → 仅转发到对应端口
```
- 自协商（auto-negotiation）：速率**10M/100M/1G/10G、半/全双工**、直通/交叉**（Auto-MDI/MDI-X）**。
  
---
### 6) From Collisions to Full-Duplex / 从碰撞到全双工
- **Repeater Hub（共享总线）**：所有端口广播，且多为**半双工 → 产生碰撞**。
- **Switch + Twisted Pair**：收发对线分离，**全双工**；交换机**仅转发给目的端口 → 无碰撞**，提升效率。
- **效率高也可能诱发拥塞**：交换机缓冲溢出时发送** PAUSE（802.3x）** 要求主机暂缓发送。
   
---
### 7) VLAN & L3 Switch / 虚拟局域网与三层交换
- **VLAN（Virtual LAN）**：在 L2 把一个物理交换网络**逻辑分割**成多个广播域。
常见**Port-based VLAN**：按端口划分；**VLAN 间通信**需**Router 或 L3 Switch**。
- 多交换机跨楼层/跨机柜的 VLAN：交换机之间用**Trunk Port（Trunk Link）**承载**多 VLAN 流量**，
通过**802.1Q Tag **标识 VLAN；对接收端主机转发时**剥离标签**。

802.1Q VLAN Tag（插入在 SrcMAC 与 Type 间）
- **TPID（16b）**：固定**0x8100**，标识 802.1Q 帧。
- **PCP（3b）**：优先级（8 级）。
- **CFI（1b）**：成帧指示（以太中为**0**）。
- **VID（12b）**：VLAN ID（不同 VLAN 取不同值）。
```
| DestMAC | SrcMAC | 0x8100 | PCP |CFI|   VID   |  Type  | Payload ... | FCS |
```
Note: Trunk 间传输带标签；接入端口（Access）向主机送达的帧通常**不带标签**。

  
---
## Key Points
- **以太网共享介质**在高负载下效率低（≈50%）；令牌网可达 ≈95%。
- 认识多种**非以太/无线链路**：**ATM（53B 单元）/FDDI（100 Mbps 双环）/FC（至128G）/1394（3.2G）/USB（40G）/HDMI（1.4起可承载IP）/iSCSI（至40G）/InfiniBand（至600G）**。
- **Global IP**：ICANN → JPNIC → ISP → 用户；**动态**地址会变化，**服务器**需**固定 IP**或**DDNS**。
- **IPv6**：128 位，冒号 16 进制，支持`::`0 压缩；首部含**Version/TrafficClass/FlowLabel/PayloadLen/NextHeader/HopLimit/Addr**。
- **L2/L3 设备**：Repeater（L1 放大）/Bridge（L2 过滤）/Switch（学习转发）/Router（L3 转发）/L3 Switch（内置路由）。
- 无碰撞以太：交换机 + 双绞线 全双工；拥塞时可 PAUSE；
- **VLAN**：L2 逻辑分段；Trunk 用**802.1Q（TPID=0x8100, PCP, CFI, VID）**跨交换机承载多 VLAN。
---

## ※※ Supplementary Cheat Sheets | 速查单

### IPv6 & VLAN Quick Reference
- [IPv6 Header Fields | IPv6 首部字段速查表](./figs/lecture08_ipv6_header_fields.md)  
  *IPv6 首部结构、字段含义与地址表示规则*

- [IEEE 802.1Q VLAN Tag | VLAN 标签与端口模式](./figs/lecture08_vlan_8021q_tag.md)  
  *802.1Q 标签字段、Trunk/Access 概念与帧结构示意*


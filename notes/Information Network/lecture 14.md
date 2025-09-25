#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Fundamentals of Information Network(情報ネットワーク概論)**.
- Instructor:Prof. Seiichiro Aoki (青木 成一郎)

# Lecture 14: Hidden Terminal & RTS/CTS, Handover/Roaming, Bluetooth, Firewall/IDS/IPS/AV, DMZ, IDS/IPS Methods, VPN & IPsec, Proxies (Forward/Reverse)
# 情報ネットワーク概論 第14回：隠れ端末とRTS/CTS，ハンドオーバ／ローミング，Bluetooth，ファイアウォール／IDS・IPS／アンチウイルス，DMZ，シグニチャ型とアノマリ型，VPN・IPsec，プロキシ／リバースプロキシ

---

## ⚪ Lecture Overview 
- **Hidden Terminal** in WLAN & **RTS/CTS** handshake for collision avoidance  
  无线局域网**隐藏终端**问题与 **RTS/CTS** 碰撞回避流程 
- **Handover (handoff)** & **Roaming** differences and continuity  
  **切换**与**漫游**的区别与连续通信 
- **Bluetooth** basics: versions, classes, profiles, pairing, vs Wi-Fi  
  **蓝牙**基础：版本/功率等级/配置文件/配对，与 Wi-Fi 的对比
- **Security middleboxes**: Firewall, **IDS/IPS**, **Antivirus**; **DMZ** design  
  安全中间件：防火墙、**入侵检测/防御**、**杀毒**；**隔离区 DMZ** 设计 
- **IDS/IPS methods**: Signature-based vs Anomaly-based  
  **签名法**与**异常检测法**的对比与组合
- **VPN** concepts, tunneling & crypto/auth; **Transport vs Tunnel** modes; **IPsec**  
  **虚拟专网**、隧道与加密/认证；**传输/隧道**两种模式；**IPsec** 框架
- **Proxies**: Forward Proxy purposes (security/caching/auth/filter) & **Reverse Proxy** roles  
  **正向代理**的目的（安全/缓存/认证/过滤）与**反向代理**的作用（隐藏后端/卸载 SSL 等）

---

## ⚪ Lecture Content 

### 1) Hidden Terminal Problem & RTS/CTS 隐藏终端与 RTS/CTS
**Hidden Terminal 概念 | Definition**  
- 由于**障碍物/距离**，某终端 **B** 收不到 **A** 的信号，但 **AP** 可以同时收到 A/B 的信号 → **B** 不知信道被占用而发送，造成**碰撞**。这类对 AP 可达、互相不可达的终端称为 **隐藏终端**。为避免该类冲突，引入 **RTS/CTS** 机制。
```
1) 终端A监听信道为空闲 ≥ DIFS → 向AP发送 RTS (Request To Send)
2) AP 在 SIFS 后发 CTS (Clear To Send) → 通知 A 与 B
3) 终端A 等待 SIFS → 发送 DATA 帧
```
**RTS/CTS 交互（步骤 4–5）**
```
4) A发完DATA后，AP在 SIFS 后发 ACK → 通知 A 与 B
5) 终端B虽收不到A的信号，但能收到AP的 CTS/ACK → 期间保持静默
   收到 ACK 后解除发送禁止，再参与竞争

```
要点：AP 以**CTS/ACK**向所有能听到它的站点“宣告占用时隙”，**隐藏终端**据此避免与 A 同时发送。


---
### 2) Handover & Roaming 切换与漫游
- **Handover（ハンドオーバ）**：移动穿越蜂窝或 WLAN **AP 覆盖边界**时，**切换接入点/基站**而**不断线**；IP 地址维持/会话不中断。
- **Roaming（ローミング）**：跨越**不同运营商网络**仍可使用**同一终端与号码**进行通信（如**国际漫游**，在国外接入当地运营商网络继续通信）。

---
### 3) Bluetooth 基础
**概念与用途**
- 工作在**2.4 GHz**；常见于键鼠、耳机、音箱、车载导航等。包含**版本（1.1/1.2/2.0/2.1/3.0/4.0/5.0）**、**功率等级（Class）**、**配置文件（Profile）**等要素；首次连接需进入**配对模式**并完成**配对**。与**Wi-Fi**相比：蓝牙多为**一对一**通信、**功耗更低**（ver.4 起明显降低）。
**版本要点（讲义表）**
- 1.1：开始普及；**1.2**：增加与**802.11b/g**干扰对策。
- 2.0：可选**EDR**，速率至**3 Mbps**。
- 2.1：简化配对，支持**NFC**；加入**Sniff Subrating**以延长低活跃设备电池寿命。
- 3.0：可选**HS**，速率至**约 24 Mbps**，并强化电源管理以省电。
- 4.0：支持**BLE**（低功耗蓝牙），**大幅省电**（速率约**1 Mbps**）。
- 5.0：速率**2/1/0.125 Mbps**，其中**125 kbps**对应更长距离（示例：可达**~400 m**级别）。
**Class（功率/范围）**
- 讲义示例：**100 mW / 10 mW / 1 mW**（功率等级影响覆盖距离与功耗）。
**使用流程提示 **
- **首次配对**：设备置于**pairing**模式 → 搜索 → 配对。常见 Profile：耳机免提（hands-free）、耳机等。

---
### 4) Firewall / IDS / IPS / Antivirus 防火墙、入侵检测/防御、杀毒
**Firewall（边界访问控制）**
- 将**外部（互联网侧）与内部（内网侧）**分隔，**阻断不允许的通信**（尤其从外到内）。
**IDS / IPS**
- **IDS（入侵检测系统）**：检测后**告警**；**IPS（入侵防御系统）**：可**主动阻断**可疑流量。
**Antivirus**
- **服务器版**（邮件/文件服务器）与**客户端版**（PC），分别在服务器与终端侧防御恶意代码。

---
### 5) Firewall & DMZ 架构
**DMZ（非武装区）设计**
- 在防火墙内侧划分**DMZ**与**内网（Intranet）**；尽量**减少对外开放端口**、关闭不必要端口。
- **DMZ 部署**：通常放置**Web / Mail / 外部向 DNS**等必须被外部访问的服务器，难免暴露在攻击面上。
- 若**DMZ 服务器**受攻陷，**与内网隔离**可把损害**限制在 DMZ**范围内。

**文字拓扑示意**
 ``` 
Internet ──[ Firewall ]── DMZ: (Web / Mail / DNS)
                   │
                   └── Intranet (Internal Systems)
 ```
实践关注：仅开放必要端口到 DMZ/内网，其他一律丢弃/拒绝。

---
### 6) IDS/IPS：Signature vs Anomaly 入侵检测/防御两大方法
- **Signature-based（シグニチャ型）**
  - 将已知攻击的**特征/模式**（签名）与流量匹配；**匹配 → 告警/阻断**。
  - **优点**：对**已知威胁**命中准。**限制**：对未知手法难以识别，需**持续更新签名库**。
- **Anomaly-based（アノマリ型）**
  - 以**正常数据/行为模式**为基线，检测**偏离**基线的流量并**告警/阻断**。
  - **优点**：可发现**未知**异常；**限制**：基线设定与**误报**需权衡。
- **组合使用**：两者各有长短，一般**联合部署**以覆盖面与准确性。

---
### 7) VPN & IPsec 虚拟专网与安全机制
**为何需要 VPN**
- 传统专线可防泄漏但成本高 → 通过**互联网**承载的**虚拟私网（VPN）以降低成本**，**同时靠隧道（tunneling）与加密/认证**保证机密性/完整性。
**核心技术**
-**Tunneling**（封装）+ **Encryption/Authentication**（加密/认证）。
- 示例框架：**IPsec（Security Architecture for IP）**。
**两种模式：Transport vs Tunnel**
- **Transport（传输模式）**：
  - **仅 TCP/UDP 头与数据**被加密；**IP 头不加密**，因此**无法判断 IP 头是否被篡改**。
- **Tunnel（隧道模式）**：
  - 通过**VPN 路由器**将**内层 IP 包**整体封装；**连同 IP 头也被加密/保护**，因此能**检测 IP 头篡改**。
- 图示（抽象）：
```
Transport: [ IP | TCP/UDP | Data ]  → encrypt {TCP/UDP|Data}, IP header in clear

Tunnel   : [ IP_in | TCP/UDP | Data ] as inner payload
           Outer: [ IP_out | ESP/AH | (Encrypted Inner Packet) ]
```
讲义明确：**隧道模式**对 IP 头也能进行保护；**传输模式**不保护 IP 头本身。

---
### 8) Proxy / Reverse Proxy 代理与反向代理
**正向代理（Forward Proxy）**
- 由**内网客户端**经 **Proxy Server **访问**外部网站**；外部仅见到代理地址，看不到内网终端的真实 IP。
- **目的**：
1. **安全**（隐藏内部地址）
2. **缓存**（曾访问内容由代理复用 → 提速/省外链）
3. **用户认证**（仅允许通过认证的用户上网）
4. **过滤**（按策略限制访问某些站点/类别）
**反向代理（Reverse Proxy）**
- 由**外部客户端**访问**反向代理**，由其**代替后端 Web 服务器**处理/转发请求；外部**不直接**接触后端。
- **好处**：
1. **保护后端**（隐藏具体服务器/结构，降低被直接攻击的机会）
2. **SSL 终止/卸载**（反代承担 TLS 握手与加解密）
3. **统一接入**（可做访问控制、WAF、负载分担等）。
**文字拓扑示意**
```
Forward Proxy:
 Client → Proxy → Internet (Web Servers)

Reverse Proxy:
 Internet (Clients) → Reverse Proxy → Internal Web Servers
```

---
## Key Points
- **RTS/CTS** 通过 **CTS/ACK** 的“覆盖宣告”让**隐藏终端**知晓占用，从而回避碰撞。
- **Handover**=同网内**AP/基站切换**不断线；**Roaming**=跨**运营商网络**延续同一终端/号码通信。
- **Bluetooth**：版本演进（1.1→5.0）、**Class 功率/范围、Profile & 配对**；与**Wi-Fi**相比更节能、常为一对一。
- **Firewall/IDS/IPS/AV**：边界拦截、检测/防御、病毒查杀协同；**DMZ**放置对外服务并与内网隔离。
- **Signature vs Anomaly**：签名法擅长**已知**、需更新；异常法可发现**未知**、需基线与误报权衡；**组合更佳**。
- **VPN（IPsec）**：**传输模式**不保护 IP 头；**隧道模式**连同 IP 头也受保护；均依赖**隧道+加密/认证**。
- **Proxy/Reverse Proxy**：正向代理偏**出网控制/缓存/审计**；反向代理偏**入口防护/SSL卸载/统一接入**。


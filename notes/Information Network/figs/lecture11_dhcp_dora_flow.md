# DHCP DORA Flow Quick Reference  
# DHCP DORA 流程速查表

---

## ⚪ DHCP Overview | DHCP 概览
- **Purpose**: 自动分配 IPv4 地址、子网掩码、默认网关、DNS  
- **Mode**: Client–Server 模式，基于 **UDP 67/68 端口**  
- **Lease**: 地址有租约时间，可续租或释放  

---

## ⚪ DORA Flow | DORA 四步流程
```
D  Discover: Client → Broadcast → "Any DHCP server here?"
O  Offer   : Server → Broadcast → "I can offer IP X with lease time Y"
R  Request : Client → Broadcast → "I request IP X from server"
A  ACK     : Server → Broadcast → "IP X assigned, lease confirmed"
```

---

## ⚪ DHCP Message Fields | DHCP 报文字段
| Field   | Meaning (English)                 | 含义（中文）         |
| ------- | --------------------------------- | -------------- |
| op      | Message Type (1=Request, 2=Reply) | 报文类型           |
| yiaddr  | Your IP Address (offered)         | 客户端被分配的 IP 地址  |
| siaddr  | Server IP Address                 | DHCP 服务器 IP 地址 |
| chaddr  | Client Hardware Address (MAC)     | 客户端硬件地址 (MAC)  |
| options | Parameters like DNS, lease        | 选项：DNS、租约等     |

---

## ⚪ DHCP Lease Lifecycle | 租约生命周期
- **T1**: Lease Renewal (50%)
- **T2**: Rebinding (87.5%)
- **Expiry**: 地址过期需重新申请
 
---

## Key Points
- DORA: Discover → Offer → Request → ACK
- 广播用于发现与多服务器场景
- 租约可续租或释放，避免地址浪费
- DHCP 提供 DNS、网关等参数

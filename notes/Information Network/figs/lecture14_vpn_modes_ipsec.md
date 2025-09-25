# VPN Modes & IPsec Quick Reference  
# VPN 模式与 IPsec 速查表

---

## ⚪ Why VPN | 为什么需要 VPN
- 公网上建立**虚拟专用通道**  
- 通过**隧道 + 加密 + 认证**保障机密性、完整性、防篡改  

---

## ⚪ Two Modes | 两种模式
| Mode        | Encrypted Parts           | IP Header Protection | Typical Usage             |
|-------------|---------------------------|----------------------|----------------------------|
| Transport    | TCP/UDP Header + Payload  | ❌ No                 | Host-to-Host               |
| Tunnel       | Entire Inner IP Packet    | ✅ Yes                | Gateway-to-Gateway / Remote |

---

## ⚪ Packet Format | 报文结构
```
Transport: [IP | TCP/UDP | Data] → {TCP/UDP|Data} Encrypted
Tunnel   : [IP_out | ESP | {IP_in | TCP/UDP | Data} Encrypted]
```

---

## ⚪ IPsec Components | IPsec 组成
- **AH** (Authentication Header): 完整性 + 认证
- **ESP** (Encapsulating Security Payload): 机密性 + 完整性 + 认证

---

## Key Points
- Transport 模式只保护传输层数据
- Tunnel 模式保护整个内层 IP 包 (含 IP 头)
- IPsec = AH + ESP + IKE (密钥交换)

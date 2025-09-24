子网掩码按位与计算步骤

# IPv4 Subnet Calculation Steps  
# IPv4 子网掩码按位与计算步骤

---

## ⚪ Objective 目标
快速判断：
1) **Network Address** 网络地址  
2) **Broadcast Address** 广播地址  
3) **Usable Host Range** 可用主机范围  
4) **Host Count** 主机数量  

---

## ⚪ Steps 步骤

```
1) Write IP & subnet mask in both decimal & binary
   同时写出 IP 和掩码的十进制 & 二进制形式

2) Compute Network Address:
   Network = IP AND Mask
   网络地址 = IP 按位与 掩码

3) Compute Broadcast Address:
   Broadcast = Network + (Host bits all 1)
   广播地址 = 网络地址 + 主机位全 1

4) Usable Host Range:
   Hosts = Broadcast − Network − 2
   可用范围 = (网络地址+1) 到 (广播地址−1)

5) Host Count:
   Count = 2^(Host bits) − 2
   主机数 = 2^(主机位数) − 2
```

---
## ⚪ Example 示例
Given: IP = 172.20.100.52, Mask = 255.255.254.0 (/23)
```
IP (bin):    10101100.00010100.01100100.00110100
Mask (bin):  11111111.11111111.11111110.00000000
------------------------------------------------
Network:     10101100.00010100.01100100.00000000 → 172.20.100.0
Broadcast:   10101100.00010100.01100101.11111111 → 172.20.101.255
Range:       172.20.100.1 ... 172.20.101.254
Host Count:  2^9 − 2 = 510
```

---
## Key Points
- 网络地址: 主机位全 0
- 广播地址: 主机位全 1
- 主机数: 2^(主机位数) − 2
- 掩码长 = 网络位数 = /prefix

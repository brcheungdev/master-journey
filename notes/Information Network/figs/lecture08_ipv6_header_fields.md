# IPv6 Header Fields Quick Reference  
# IPv6 首部字段速查表

---

## ⚪ IPv6 Header Structure | IPv6 首部结构
```
| Version | Traffic Class | Flow Label | Payload Length | Next Header | Hop Limit |
|                       Source Address (128 bits)                      |
|                    Destination Address (128 bits)                    |
|                Extension Headers (if any) + Upper-layer Data          |
```

---
## ⚪ Field Meanings | 字段含义

| Field            | Bits | Meaning (English)                         | 含义（中文）                |
| ---------------- | ---- | ----------------------------------------- | --------------------- |
| Version          | 4    | Always **6** for IPv6                     | IPv6 固定值 6            |
| Traffic Class    | 8    | QoS / priority info (like IPv4 TOS)       | 服务质量/优先级（类似 IPv4 TOS） |
| Flow Label       | 20   | Identify packets of the same flow         | 标识同一流量的分组             |
| Payload Length   | 16   | Length of data after the header (bytes)   | 首部后数据的长度（字节数）         |
| Next Header      | 8    | Upper-layer protocol / next extension hdr | 下层协议或扩展头类型            |
| Hop Limit        | 8    | Decrement per hop; 0 → discard            | 每跳减 1；0 丢弃            |
| Source Address   | 128  | IPv6 source address                       | 源 IPv6 地址             |
| Destination Addr | 128  | IPv6 destination address                  | 目的 IPv6 地址            |

---
## ⚪ Address Notation | IPv6 地址表示
- **Full**:`FEDC:BA98:7654:3210:FEDC:BA98:7654:3210`
- **Zero Compression**:`::`可压缩连续 0（只能出现一次）
- **Leading Zero Omission**: 每组前导 0 可省略
```
1080:0:0:0:8:800:200C:417A   →  1080::8:800:200C:417A
```

---
## Key Points
- IPv6 固定首部长度 40 字节（无选项时）
-  Hop Limit 取代 IPv4 TTL
-  Next Header 链接后续扩展头或 TCP/UDP/ICMPv6
-  流量标签与流优先级为未来 QoS 设计

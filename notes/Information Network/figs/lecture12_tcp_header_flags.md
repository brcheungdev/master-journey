# TCP Header & Flags Quick Reference  
# TCP 首部与控制位速查表

---

## ⚪ TCP Header Fields | TCP 首部字段
| Field                  | Length      | Meaning (English)           | 含义（中文）                   |
|------------------------|-------------|-----------------------------|-------------------------------|
| Source Port            | 16 bits      | Sender port                 | 源端口                        |
| Destination Port       | 16 bits      | Receiver port               | 目的端口                       |
| Sequence Number        | 32 bits      | First byte in this segment   | 本段第一个字节序号              |
| Acknowledgment Number   | 32 bits      | Next expected byte number    | 期望收到的下一个字节序号        |
| Data Offset (Header Len)| 4 bits       | Header length                | 首部长度（32bit字为单位）        |
| Reserved               | 3 bits       | Must be zero                 | 保留位，置零                   |
| Flags                  | 9 bits       | Control bits (see below)     | 控制位                         |
| Window Size            | 16 bits      | Flow control window size     | 接收窗口大小                   |
| Checksum               | 16 bits      | Error detection              | 校验和                         |
| Urgent Pointer         | 16 bits      | Urgent data position         | 紧急数据指针                   |
| Options + Padding       | Variable     | Optional parameters          | 可选参数及填充                 |

---

## ⚪ TCP Control Flags | TCP 控制位

| Flag | Name (English)         | 名称（中文）   | Function (English)                  | 功能（中文）               |
|------|------------------------|---------------|-------------------------------------|----------------------------|
| URG  | Urgent Pointer valid    | 紧急           | Urgent pointer field significant     | 紧急指针有效                |
| ACK  | Acknowledgment valid    | 确认           | Acknowledgment field significant     | 确认号有效                  |
| PSH  | Push Function           | 推送           | Request push to receiving application| 请求推送至应用层            |
| RST  | Reset Connection        | 复位           | Abort connection immediately         | 立即复位连接                |
| SYN  | Synchronize Sequence    | 同步           | Synchronize sequence numbers          | 同步序号，建立连接           |
| FIN  | Finish                  | 结束           | Gracefully close connection           | 结束连接                     |
| CWR  | Congestion Window Reduced| 拥塞窗口减少   | ECN Congestion signal                 | 拥塞控制相关                 |
| ECE  | ECN Echo                | ECN 回显       | Explicit Congestion Notification Echo | 拥塞控制相关                 |

---

## Key Points

- 三次握手：SYN → SYN+ACK → ACK
- 四次挥手：FIN → ACK → FIN → ACK
- TCP 首部最少 20 字节，可带选项
- 控制位可组合使用，如 SYN+ACK

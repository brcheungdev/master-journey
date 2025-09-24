# IEEE 802.1Q VLAN Tag Quick Reference  
# IEEE 802.1Q VLAN 标签速查表

---

## ⚪ Frame with 802.1Q Tag | 802.1Q 帧结构
```
| Dest MAC | Src MAC | TPID=0x8100 | PCP | CFI |   VID   |  Type  | Payload ... |  FCS  |
           |<------ 802.1Q VLAN Tag (4 bytes) ------>|
```
- 插入位置：源 MAC 与以太类型字段之间
- Trunk 口之间传 VLAN 流量时保留此标签；Access 口送主机时去掉标签

---
## ⚪ Tag Fields | 标签字段含义

| Field | Bits | Meaning (English)                          | 含义（中文）            |
| ----- | ---- | ------------------------------------------ | ----------------- |
| TPID  | 16   | Tag Protocol Identifier, always **0x8100** | 协议标识符，固定值 0x8100  |
| PCP   | 3    | Priority Code Point (QoS, 0–7)             | 优先级，8 级           |
| CFI   | 1    | Canonical Format Indicator (Ethernet=0)    | 成帧指示，以太网取 0       |
| VID   | 12   | VLAN Identifier (1–4094 usable)            | VLAN ID，1–4094 可用 |

---
## ⚪ VLAN Concepts | VLAN 相关概念
- Access Port: 属于单一 VLAN，向终端主机转发时剥离 802.1Q 标签
- Trunk Port: 在交换机之间传多 VLAN，保留 802.1Q 标签识别 VLAN
```
Switch1 (VLAN10,20)
  | Trunk (Tagged) |
Switch2 (VLAN10,20)
  | Access Port    |
 Host (Untagged)
```

---
## Key Points
- VID 取值 1–4094（0 & 4095 保留）
- Trunk 保留 802.1Q 标签，Access 去标签
- PCP 支持 QoS 优先级；CFI 基本总为 0

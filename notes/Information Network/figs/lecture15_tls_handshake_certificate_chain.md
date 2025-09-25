# TLS Handshake & Certificate Chain Quick Reference  
# TLS 握手与证书链速查表

---

## ⚪ TLS Handshake Steps | TLS 握手步骤
1. ClientHello: 客户端发起，支持的 TLS 版本/密码套件  
2. ServerHello: 服务器选择版本/套件，发送证书  
3. 证书验证: 客户端用 CA 公钥验证服务器证书链  
4. ClientKeyExchange: 客户端生成会话密钥，用服务器公钥加密发送  
5. ChangeCipherSpec + Finished: 双方切换到加密通信  

---

## ⚪ Certificate Chain | 证书链
```
Root CA Certificate
   ↓
Intermediate CA Certificate(s)
   ↓
Server Certificate (网站证书)
```
-  客户端预装**Root CA 公钥**
-  验证服务器证书签名链直到 Root CA
  
---

## ⚪ Encryption Usage | 加密使用
- **非对称加密**：只用于会话密钥交换 + 身份验证
- **对称加密**：用于后续数据加解密（高效）

  
---
## ⚪ Key Points
- Root CA 可信任 → 中间 CA → 服务器证书
- 公钥加密仅用于密钥分发，数据传输用对称密钥
- 浏览器内置根证书，验证链顶端 CA

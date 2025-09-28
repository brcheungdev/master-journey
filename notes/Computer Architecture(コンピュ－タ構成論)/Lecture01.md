#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
## Lecture 1
- Understanding the **Hierarchy of Computer Systems** <br/>
理解计算机系统的层级结构
- C++
- Development Environment: **Visual Studio Community 2022** 开发环境
 
---
## ⚪ Lecture Content 
### 1. Computer System Hierarchy  
**计算机系统层次结构**

1. Application Level  
   应用层  
2. High-level Language Level  
   高级语言层  
3. Machine Instruction Level (with OS)  
   机器指令层（含操作系统）  
4. Register Transfer Level  
   寄存器传输层  
5. Gate Level (Logic Design)  
   门级（逻辑设计）  
6. Device Level (MOS Device Design)  
   器件层（MOS 器件设计） 

- **Software Layers**: Application, High-level Language, OS, Machine Instructions  
  软件层：应用、高级语言、操作系统、机器指令  
- **Hardware Layers**: Register Transfer, Gate, Device Levels  
  硬件层：寄存器传输、门级、器件层  
- OS acts as a bridge between software and hardware  
  操作系统在软硬件之间起桥梁作用  

### 2. Applications of Computers  
**计算机的应用**

- **Numerical Simulation**: Structural mechanics, fluid dynamics, electromagnetics  
  数值仿真：结构力学、流体力学、电磁学  
- **Big Data**: Data mining, neural networks, forecasting  
  大数据：数据挖掘、神经网络、预测分析  
- **Business Systems**: ERP, banking, reservations  
  商业系统：ERP、银行业务、预订系统  
- **Multimedia**: Games, VR, visualization  
  多媒体：游戏、虚拟现实、可视化  
- **AI & Robotics**: Image/speech understanding, industrial & medical robots  
  人工智能与机器人：图像/语音识别、工业与医疗机器人  
- **Internet & IoT**: Online services, smart cities  
  互联网与物联网：在线服务、智慧城市  

### 3. Programming Languages  
**程序设计语言**

- **Procedural Languages**: C, C++, Java, Python, Fortran, COBOL  
  过程式语言：C、C++、Java、Python、Fortran、COBOL  
- **Declarative Languages**: SQL, Haskell, Prolog  
  声明式语言：SQL、Haskell、Prolog  
- **General-purpose vs Domain-specific** languages  
  通用语言 vs 领域专用语言  
- **Compiled vs Interpreted** approaches  
  编译型 vs 解释型  
  - *Compiler*: Analyze entire source → generate machine code → execute  
    编译器：分析整个源码 → 生成机器码 → 执行  
  - *Interpreter*: Execute line by line → easier debugging but slower  
    解释器：逐行执行 → 调试方便但速度较慢  

### 4. C Programming Basics  
**C 语言基础**

Why learn C:  
为什么要学习 C：  
- Close to hardware  
  贴近硬件层次  
- OS and device-level programming  
  适合操作系统与设备级编程  
- Good for understanding system internals  
  有助于理解系统内部原理
  
Example: **Hello World!** Program  
示例：Hello World! 程序  
```c
  #include <stdio.h>
  int main(void) {
      printf("Hello World!\n");
      return 0;
  }
```
---
### Key Points 
- Understand software/hardware layering  
  理解软硬件分层结构  
- Learn C as a bridge between high-level programming and system architecture  
  学习 C 语言作为高级编程与系统体系结构之间的桥梁  
- Practice with Visual Studio environment  
  在 Visual Studio 环境中进行实践


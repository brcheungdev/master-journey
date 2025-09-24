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
### 1. Computer System Hierarchy  计算机系统层次结构
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

 - **Software Layers**: Application, High-level Language, OS, Machine Instructions  软件层
 - **Hardware Layers**: Register Transfer, Gate, Device Levels                      硬件层
 - OS acts as a bridge between software and hardware

### 2. Applications of Computers  计算机的应用
- **Numerical Simulation**: Structural mechanics, fluid dynamics, electromagnetics  
- **Big Data**: Data mining, neural networks, forecasting  
- **Business Systems**: ERP, banking, reservations  
- **Multimedia**: Games, VR, visualization  
- **AI & Robotics**: Image/speech understanding, industrial & medical robots  
- **Internet & IoT**: Online services, smart cities

### 3. Programming Languages
- **Procedural Languages**: C, C++, Java, Python, Fortran, COBOL  
- **Declarative Languages**: SQL, Haskell, Prolog  
- **General-purpose vs Domain-specific** languages  
- **Compiled vs Interpreted** approaches  
  - *Compiler*: Analyze entire source → generate machine code → execute  
  - *Interpreter*: Execute line by line → easier debugging but slower

 ### 4. C Programming Basics
- Why learn C:
  - Close to hardware  
  - OS and device-level programming  
  - Good for understanding system internals  
- Example: **Hello World!** Program
  ```c
  #include <stdio.h>
  int main(void) {
      printf("Hello World!\n");
      return 0;
  }
  
---
### Key Points 
- Understand software/hardware layering  
  理解软硬件分层结构  
- Learn C as a bridge between high-level programming and system architecture  
  学习 C 语言作为高级编程与系统体系结构之间的桥梁  
- Practice with Visual Studio environment  
  在 Visual Studio 环境中进行实践


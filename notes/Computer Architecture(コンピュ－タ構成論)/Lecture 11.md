#  My notes
- This folder contains my notes, thoughts and learning summaries during my master's degree study.
- The main topics include: **Computer Architecture(コンピュ-タ構成論)**.
- Instructor:Prof. Shinji Tomita (富田眞治)  

---
# Lecture 11: Memory Systems — Hierarchy, Virtual Memory & Caches
Memory hierarchy, locality, virtual memory (paging/segmentation, TLB), page replacement, cache mapping & write policies, multi-level caches, VA→TLB→Cache pipeline, storage devices, Fugaku overview<br/>
内存层次结构、局部性、虚拟内存（分页/分段、TLB）、页面替换、缓存映射与写入策略、多级缓存、VA→TLB→缓存流水线、存储设备、富流概述

---

## ⚪ Lecture Overview
- Memory performance metrics: **access time / cycle time / latency / bandwidth**
- Why **memory hierarchy** works: **temporal & spatial locality**, system integration
- **Virtual memory**: paging & segmentation; **page table / TLB**; page faults
- **Replacement policies**: FIFO anomaly, **LRU**, Working Set
- **Caches**: block/line, set-associative, directory & data array, write-through vs write-back
- **Multi-level caches** and effective access-time formulas; **split I$ / D$ (Harvard)**
- **VA → TLB → Cache → Memory** access pipeline
- Storage landscape: **DRAM / SSD / HDD / RAID / Tape / DVD / BD / USB / Optane**
- **Address space evolution** (IBM/Intel) & **Fugaku** supercomputer notes
- 记忆性能指标：访问时间/周期时间/延迟/带宽
- 记忆层次结构为何有效：时间与空间局部性、系统集成
- 虚拟内存：分页与分段；页表/高速缓存缓存列表；页面错误
- 替换策略：先进先出异常、LRU（最近最少使用）算法、工作集
- 缓存：块/行、组关联式、目录与数据数组、写通过与写回
- 多级缓存及有效访问时间公式；分段 I$ / D$（哈弗模式）
- VA → TLB → 缓存 → 记忆的访问流水线
- 存储格局：DRAM / SSD / HDD / RAID / 磁带 / DVD / BD / USB / 奥泰纳
- 地址空间演变（IBM/英特尔）及“富谷”超级计算机说明
---

## ⚪ Lecture Content 讲座内容

### 1) Memory Requirements & Performance Metrics    内存需求与性能指标
- **Access time**: time until data becomes available  
- **Cycle time**: time until next R/W is possible (≥ access time)  
- **Latency**: delay until first data in a burst  
- **Bandwidth (throughput)**: bytes or transfers per second (max BW excludes latency)
- **访问时间**：数据可获取所需的时间
- **循环时间**：下次读写操作可行所需的时间（≥ 访问时间）
- **延迟**：数据在一次传输中首次出现所需的时间
- **带宽（吞吐量）**：每秒的字节数或传输量（最大带宽不包括延迟）
---

### 2) Memory Hierarchy (Registers → Caches → DRAM → SSD/HDD → Archive)    存储层次结构（寄存器 → 缓存 → DRAM → SSD/HDD → 存档）
- **Registers**: O(100 ps), a few dozen entries  
- **L1/L2/L3 Caches**: O(100 ps–ns), MB-scale  
- **Main Memory (DRAM)**  
- **Secondary / Mass Storage**: **SSD/HDD**, Data Warehouse/Archive  
- **Portable storage**: **USB**, **DVD/BD**, **Magnetic Tape** (e.g., ~45 TB, ~1 GB/s)  
- **Goal**: hide main memory **latency** and **capacity** limits by leveraging hierarchy.
- **寄存器**：O(100 皮秒)，几十个条目
- **一级/二级/三级缓存**：O(100 皮秒至纳秒)，兆字节级
- **主存储器（DRAM）**
- **次级/大规模存储**：**SSD/HDD**，数据仓库/存档
- **便携式存储**：**USB**，**DVD/BD**，**磁带**（例如，约 45TB，约 1GB/秒）
- **目标**：通过利用这种层次结构来隐藏主存储器的**延迟**和**容量**限制。

**Why effective?**  **为何有效？**
1) **Locality of reference**  
   - **Temporal**: recently used will be used again  
   - **Spatial**: nearby addresses likely accessed soon  
2) **System integration**: combine diverse technologies to approximate the “ideal” memory. 
1）**参考的局限性**
- **时间方面**：近期使用的内容日后仍有可能再次使用
- **空间方面**：附近的地址很可能很快就会被访问到
2）**系统整合**：将多种技术相结合，以接近“理想”的存储方式。

---

### 3) Virtual Memory — Address Spaces & Methods    虚拟内存——地址空间与方法
Assume (for illustration): **VA=4 GB**, **PA=4 MB**; real systems often VA=2⁶⁴B, PA=GBs. 

**Methods**   **方法**
- **Paging**: split VA into fixed-size pages (e.g., **4 KB**), PA into frames; map at run time  
- **Segmentation**: variable-length program/data segments mapped to contiguous PA; per-segment protection; fragmentation/compaction overhead; often **combined** with paging (e.g., Intel) 
- **分页**：将虚拟地址空间分割成固定大小的页面（例如，**4KB**），将物理地址分割成帧；在运行时进行映射
- **分段**：将可变长度的程序/数据段映射到连续的物理地址；每个段都有保护机制；存在碎片化/压缩开销；通常与分页相结合（例如，英特尔）

**Fragmentation**   **碎片化**
- Segmentation may cause **external fragmentation**; compaction can “pack” segments. Paging provides fixed units but still needs frame management. 
- 分区可能会导致**外部碎片**；压缩可以“压缩”分区。分页提供了固定的单元，但仍需要帧管理。

---

### 4) VA→PA Translation — Page Table & TLB       VA→PA 转换 — 页表与 TLB
**Direct mapping with page table**                **采用页表的直接映射**
1) Look up **page table** by **VPN**             
2) If **V=1**: get **PFN**, form **PA**           
3) If **V=0**: **page fault** → OS loads page from disk to a free frame, updates table  
1) 通过虚拟页号（VPN）查找页表
2) 如果 **V=1** ：获取页框号（PFN），形成物理地址（PA）
3) 如果 **V=0** ：发生页错误 → 操作系统从磁盘加载页面到一个空闲帧中，并更新表

**Associative mapping with TLB**            **带有 TLB 的关联映射**
- **TLB (Translation Lookaside Buffer)** caches popular (VPN→PFN) pairs; on TLB hit, skip page table lookup; on miss, consult page table (HW or SW handler). 
**Events**
- **TLB hit** → continue  
- **TLB miss** → probe page table; if present, refill TLB  
- **Page fault** → not in memory; OS fetches from disk, possibly evicting a frame; process may be **switched out** during I/O. 
**Page replacement** (when no free frames)
- **FIFO** (can show **Belady’s anomaly**)  
- **LRU** (Least Recently Used) — widely used  
- **Working Set** — keep pages referenced in last **T** time window. 

---

### 5) Caches — Principles & Organization
**Principle**: exploit locality; map memory **blocks (lines, e.g., 32–64 B)** into cache sets.
**Directory + Data Array**
- Address splits into **[Tag | Set | Offset]**; directory (by set) holds tags & status; data array stores blocks.  
- **Mapping**  
  - **Direct-mapped** (rows=1)  
  - **Fully associative** (sets=1)  
  - **Set-associative** (general case; multiple “ways” per set)  
- **Capacity**: `Cache Size = BlockSize × #Sets × #Ways`

**Replacement (per-set)**: typically **LRU**.  
**Writes**: **write-through (store-through)** vs **write-back (store-in)**. 

**Effective Access Time (1/2/3-level)**
```c
Single-level: T_C = T_H + β · T_L1
Two-level: T_C = T_H + β · T_L1 + βγ · T_L2
(β: L1 miss rate; γ: L2 local miss rate)
```
- Example ratios (from slides): `T_L1/T_H≈5`, `T_L2/T_H≈50`, `β≈0.02`, `γ≈0.2` ⇒ `T_C≈1.3·T_H`  
- Modern CPUs often use **3-level caches** (e.g., **L1 64 KB**, **L2 256 KB**, **L3 8 MB** in Intel i7-6700 example). 

**Split vs Unified**
- **Split (Harvard)**: separate **I-cache** and **D-cache**; avoids I/D conflicts, writes don’t hit I$  
- **Unified**: one cache for both; may have I/D contention; common as L2/L3. 

---

### 6) From VA Generation to Cache Access — End-to-End Path
1) Instruction (e.g., `LOAD R0, Rb, Rx, D`) generates **VA = Rb + Rx + D**  
2) **TLB** lookup by **VPN**; on hit, get **PFN**  
3) **Cache directory** lookup by **set** (from PFN+offset bits)  
4) On **cache hit**, read from data array; on **miss**, fetch block from memory and install (evict per **LRU** if needed)  
5) **Write-through**: update memory immediately; **Write-back**: defer until eviction  
6) On **TLB miss**, consult **page table**; if present, refill TLB; if absent, **page fault** → OS brings page from disk; may **context-switch** the process  
7) Replacement in TLB/Cache uses **LRU** or variants
---

### 7) Storage Devices & Throughputs (Snapshot)
- **SSD / HDD**; **Disk cache**; **RAID**  
- **Optane** (e.g., 16–32 GB class, ~10 µs) as fast storage tier  
- **Tape / DVD / BD / USB** (examples: Tape ~45 TB, ~1 GB/s; DVD/BD capacities & typical transfer rates)
---

### 8) Address Space Evolution (IBM / Intel)    地址空间演进（IBM/英特尔）
- **IBM**: S/360 (24-bit) → S/370 (24-bit + VM) → S370-XA (31-bit) → ESA/390 → z/Arch (64-bit)  
- **Intel**: 8086 (1 MB, 16-bit seg) → 286 (16 MB) → 386 (**4 GB**, IA-32) → … → x86-64 (**Intel 64**, 64-bit VA/seg)

---

### 9) Fugaku Supercomputer — Memory & Vector Notes    “Fugaku”超级计算机——内存与向量运算说明
- **Peak ~414 PFLOPS** (2.7 TF/node × 153,600 nodes), **power 30–40 MW**  
- **SVE** vector extension (masking, gather/scatter), **HBM** high-BW memory  
- Node: shared memory; inter-node: **Tofu** 6-D torus; aggregate mem BW ~**1 TB/s** (illustrative in slides)  
- Benchmarks: **TOP500**, **HPCG**, **HPL-AI**, **Graph500** 
- **峰值性能约 414 PFLOPS**（2.7 TF/node × 153,600 个节点），**能耗 30 - 40 兆瓦**
- **SVE**向量扩展（掩码、收集/散列），**HBM**高带宽内存
- 节点：共享内存；节点间：**Tofu** 6 维环形结构；总内存带宽约**1TB/s**（幻灯片中有示例说明）
- 基准测试：**TOP500**、**HPCG**、**HPL-AI**、**Graph500**
- 
---

### Key Points
- **Locality + hierarchy** hides latency/capacity limits; caches convert random main-memory access into fast hits  
- **Virtual memory** gives each process a large, contiguous VA; **TLB** is critical to avoid page-table overhead  
- **Page replacement** impacts performance dramatically: beware **FIFO anomaly**; **LRU/Working-Set** commonly used  
- **Cache design**: mapping (set-assoc), block size (~32–64 B), write policy, multi-level stacking决定实际性能  
- **Pipeline** from **VA→TLB→Cache→Memory** explains where **misses** originate and how OS/HW cooperate
- **区域 + 层次结构** 可消除延迟/容量限制；缓存将随机的主存访问转换为快速命中
- **虚拟内存** 为每个进程提供一个大且连续的虚拟地址空间；**高速缓存列表** 对避免页表开销至关重要
- **页面替换** 对性能有显著影响：注意 **先进先出异常**；**最近最少使用/工作集** 常被使用
- **缓存设计**：映射（组关联）、块大小（约 32 - 64 字节）、写策略、多级堆叠 决定了实际性能
- **流水线** 从 **虚拟地址→高速缓存列表→缓存→内存** 解释了 **未命中** 的来源以及操作系统/硬件如何协作

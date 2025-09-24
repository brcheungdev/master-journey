*Prepared as note for Lecture 5.*

# Collision Timing & 10BASE5 Segment Length Derivation  
# 冲突时序与 10BASE5 段长推导

---

## ⚪ Objective 目标
- 解释 **为什么 10BASE5 标准限制单段长度为 500 m**。  
- 基于 **CSMA/CD** 机制，推导**最小帧发送时间内必须能探测到远端冲突**的物理约束。  

---

## ⚪ Physical Constraints 物理约束
- **Collision detection**:  
  A sender **must detect** a collision **before** finishing sending the **minimum frame (64B)**.  
  若在最小帧发送完前未检测到冲突，发送端会**误以为传输成功**。  

- **Worst-case**:  
  - Collision occurs **at the farthest end** of the cable after frame head arrives.  
  - Jam signal returns after collision; must reach sender **before frame end**.  
  最坏场景：帧头到达远端后立即碰撞，Jam 信号返回必须在帧结束前到达发送端。  

---

## ⚪ Parameters 设定
| Symbol       | Meaning / 含义                   | Value / 数值                         |
|--------------|----------------------------------|--------------------------------------|
| \( v_g \)    | Propagation speed 传播速度       | \( 0.77c = 2.31×10^8\,m/s \)         |
| \( t_r \)    | Repeater delay 中继器延迟        | \( 9\,μs \) per repeater             |
| \( L \)      | Length per segment 每段长度      | 求解目标                             |
| \( T_{min}\) | Min frame tx time 最小帧发送时间 | \( 64B = 512b \)，@10 Mb/s → 51.2 μs |

Topology (worst case):  
```
Host A —— Repeater —— Repeater —— Host B
  |<-- L -->|<--- L --->|<--- L --->|
```
Total cable length = **3L**; two repeaters, each delay \(t_r\)。  

---

## ⚪ Timing Equations 时间方程
(1) A → B-near (frame head travel):
    t1 = (3L / vg) + 2 * tr

(2) B → A (jam return):
    t2 = (3L / vg) + 2 * tr

(3) Total time to detect collision:
    t_total = t1 + t2
            = 2 * (3L / vg + 2 * tr)

Constraint (must detect before min frame ends):
    t_total ≤ T_min

---

## ⚪ ASCII Timing Diagram 时间线示意
```
A: |---- Send Frame ----->|         (collision)          |
                          v                             |
B:                         X <- Detect Collision -> Jam -|
                          |                             |
A: <----------------------|--------- Jam ---------------|
          t1                        t2
Total = t1 + t2  ≤  T_min (64B sending time)
```


---

## ⚪ Solve for \( L \) 推导 L
Given:
  vg = 0.77 * c = 2.31e8 m/s
  tr = 9 μs
  T_min = 51.2 μs

Constraint:
  t_total = 2 * (3L / vg + 2 * tr) ≤ 51.2 μs

Expand:
  (6L / vg) + 4 * tr ≤ 51.2 μs

Plug numbers:
  (6L / 2.31e8) + 4 * 9 ≤ 51.2
  (6L / 2.31e8) + 36 ≤ 51.2
  (6L / 2.31e8) ≤ 15.2

Solve L:
  L ≤ (15.2e-6 s * 2.31e8 m/s) / 6
    = (3511.2) / 6
    = 585.2 m  (theoretical upper bound per segment)

Engineering margin:
  Considering attenuation, tolerances, etc.
  → Standard chooses 500 m (10BASE5 max segment length).


---

## ⚪ Standard Choice 标准取值
- Theoretical upper bound ≈ **585 m**.  
- Considering **signal attenuation** & **safety margins**,  
  IEEE chose **500 m** as the **max segment length** for 10BASE5.  

---

## ⚪ Key Points 
- **Collision detectability**: 必须在最小帧内检测到碰撞。  
- **Longer cables** → collision returns **too late** → sender misjudges success。  
- **500 m limit** = physical delay + repeater latency + safety margin。  

---


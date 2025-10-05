[Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

## My notes
- This file contains my notes, thoughts, and learning summaries during my master's degree study.

# Computer Programming (Python) — Lecture 08 Notes 
# 计算机编程（Python）——第 08 讲笔记

---

# Table of Contents / 目录

- [Today’s Agenda / 今日教学安排](#todays-agenda--今日教学安排)
- [Learning Objectives / 学习目标](#learning-objectives--学习目标)
- [File I/O Basics / 文件 I/O 基础](#file-io-basics--文件-io-基础)
- [Write Text: `print()` vs `write()` / 文本写入：`print()` 与 `write()`](#write-text-print-vs-write--文本写入print-与-write)
- [Create vs Append vs Exclusive / 新建、追加与独占写入](#create-vs-append-vs-exclusive--新建追加与独占写入)
- [Read Text: `read`/`readline`/Iteration/`readlines` / 文本读取：`read`、`readline`、迭代、`readlines`](#read-text-readreadlineiterationreadlines--文本读取readreadline迭代readlines)
- [Binary I/O & In‑Memory Streams / 二进制 I/O 与内存流](#binary-io--inmemory-streams--二进制-io-与内存流)
- [OS File Ops / 文件操作（复制/移动/改名/权限/删除）](#os-file-ops--文件操作复制移动改名权限删除)
- [Directories & Globbing / 目录与通配匹配](#directories--globbing--目录与通配匹配)
- [Paths: `os.path` & `pathlib` / 路径：`os.path` 与 `pathlib`](#paths-ospath--pathlib--路径ospath-与-pathlib)
- [Exercises — Primes (1) & (2) / 演习——素数（1）与（2）](#exercises--primes-1--2--演习——素数1与2)
- [Timing with `%timeit` / 用 `%timeit` 测速](#timing-with-timeit--用-timeit-测速)
- [Plotting time curves / 绘制时间曲线](#plotting-time-curves--绘制时间曲线)
- [Implementation Notes & Minimal Tests / 实现思路与最小对拍](#implementation-notes--minimal-tests--实现思路与最小对拍)

---

## Today’s Agenda / 今日教学安排

- File I/O (open/modes/with), file/dir ops, path handling, `BytesIO`/`StringIO`.  
文件 I/O（打开/模式/`with`）、文件/目录操作、路径处理、`BytesIO`/`StringIO`。

- **Exercises:** **Prime(1)** `is_prime`/`prime_list_1`; **Prime(2)** `prime_list_2` + speedup + plot.  
**演习：****素数（1）**`is_prime`/`prime_list_1`；**素数（2）**`prime_list_2` + 加速 + 绘图。

---

## Learning Objectives / 学习目标

- Open, read, write, and close text/binary files safely; understand mode flags.  
**掌握**文本/二进制文件的打开、读写与安全关闭；理解模式标志。

- Use `with` for automatic closing; choose `print()` vs `write()` appropriately.  
**会用**`with`**自动关闭**；合理选择 `print()` 与 `write()`。

- Perform common **OS file/dir ops** and handle **paths** with `os.path`/`pathlib`.  
**完成**常见**文件/目录**操作并用 `os.path`/`pathlib` 处理**路径**。

- Implement and benchmark prime generators; visualize timings with Matplotlib.  
**实现**素数生成并**基准测试**；用 Matplotlib **可视化**耗时。

---

## File I/O Basics / 文件 I/O 基础

- **Open/Close:** `f = open(filename, mode)`; `f.close()`.  
**打开/关闭：**`f = open(filename, mode)`；`f.close()`。

- **Text vs Binary:** mode second char `t` (default) or `b`.  
**文本 vs 二进制：**模式第二字符 `t`（默认）或 `b`。

- **Use `with`:** `with open(path,"w",encoding="utf-8") as f: ...` auto‑closes on block exit.  
**使用 `with`：**`with open(path,"w",encoding="utf-8") as f: ...` 在退出代码块时**自动关闭**。

> 以上要点来自讲义对 open/close 与 with 的分解。  
> 引自讲义关于 **open/close** 与 **with** 的说明。 

---

## Write Text: `print()` vs `write()` / 文本写入：`print()` 与 `write()`

- **`write()`** returns **bytes count** and **adds no spaces/newlines**.  
**`write()`** 返回**写入字节数**，**不自动添加**空格/换行。

- **`print()`** by default adds **spaces between args** and a **trailing newline**; tweak via `sep=''`, `end=''`.  
**`print()`** 默认在参数间加**空格**、末尾加**换行**；可通过 `sep=''`、`end=''` 调整。

- For long texts, write in **chunks**.  
**长文本**建议**分块**写入。

> 以上来自讲义“write()/print() 写入差异与分块写入”的示例页。  
> 引自讲义对 **write/print 差异**、**分块写入** 的阐述。

---

## Create vs Append vs Exclusive / 新建、追加与独占写入

- **`"w"`** write (truncate or create), **`"a"`** append, **`"x"`** **exclusive create** (error if exists).  
**`"w"`** 写入（截断或新建）、**`"a"`** 追加、**`"x"`** **独占新建**（存在则报错）。

- Combine with **`b`** for binary: e.g., `"wb"`.  
可与 **`b`** 组合用于二进制，如 `"wb"`。

- `"x"` mode integrates well with **exceptions** for safe create‑once patterns.  
`"x"` 与**异常处理**配合构建**一次性创建**的安全模式。

> 以上要点来自讲义关于 `"x"` 模式与异常示例。  
> 引自 `"x"` 模式与异常处理 的讲义页。

---

## Read Text: `read`/`readline`/Iteration/`readlines` / 文本读取：`read`、`readline`、迭代、`readlines`

- **`read()`** load whole file or given **max size**; can **chunk**.  
**`read()`** 读取**全文件**或**限定长度**；支持**分块**。

- **`readline()`** reads **one line** at a time.  
**`readline()`** 每次读取**一行**。

- **Iteration**: `for line in f:` memory‑friendly.  
**迭代读取：**`for line in f:` 更省内存。

- **`readlines()`** returns **list of lines**.  
**`readlines()`** 返回**行列表**。

> 以上来自讲义对应页（read/迭代/readlines）。  
> 引自讲义 **read/迭代/readlines** 章节。

---

## Binary I/O & In‑Memory Streams / 二进制 I/O 与内存流

- Use `"rb"`/`"wb"` and **`bytes`** objects; large files via chunked read/write.  
**使用**`"rb"`/`"wb"` 与 **`bytes`**；大文件**分块**读写。

- **`tell()`** returns current **byte offset**; **`seek(offset, origin)`** repositions (origins **0/1/2**).  
**`tell()`** 返回**字节偏移**；**`seek(offset, origin)`** 重定位（起点 **0/1/2**）。

- In‑memory streams: **`io.BytesIO`** / **`io.StringIO`**.  
**内存流：**`io.BytesIO`/`io.StringIO`。

> 以上来自讲义“二进制 I/O、seek/tell 与 BytesIO/StringIO”部分。  
> 引自讲义 **二进制 I/O/seek/tell/BytesIO/StringIO**。 

---

## OS File Ops / 文件操作（复制/移动/改名/权限/删除）

- **Copy/Move:** `shutil.copy()` / `shutil.move()`.  
**复制/移动：**`shutil.copy()` / `shutil.move()`。

- **Rename:** `os.rename()`; **links:** `os.link()` hardlink, `os.symlink()` symlink.  
**改名：**`os.rename()`；**链接：**`os.link()` 硬链接，`os.symlink()` 软链接。

- **Permissions/Owner:** `os.chmod()` / `os.chown()`; **remove:** `os.remove()`.  
**权限/所有者：**`os.chmod()` / `os.chown()`；**删除：**`os.remove()`。

- Some operations need **elevated privileges** (e.g., symlink on Windows).  
部分操作在 **Windows** 等平台可能需要**开发者模式/管理员**权限。

> 以上要点来自讲义对应页（含 WinError 1314 提示）。  
> 引自讲义（含 **WinError 1314** 的提示页）。

---

## Directories & Globbing / 目录与通配匹配

- **Get/Change/Make/Remove:** `os.getcwd()`, `os.chdir()`, `os.mkdir()`, `os.rmdir()`.  
**获取/切换/创建/删除目录：**`os.getcwd()`、`os.chdir()`、`os.mkdir()`、`os.rmdir()`。

- **Glob patterns:** `*`, `?`, `[abc]`, `[a-z]`, `[0-9]`, `[!abc]`.  
**通配规则：**`*`、`?`、`[abc]`、`[a-z]`、`[0-9]`、`[!abc]`。

> 以上对应讲义 glob 章节中的示例与规则表。  
> 引自讲义 **glob() 模式匹配** 部分。

---

## Paths: `os.path` & `pathlib` / 路径：`os.path` 与 `pathlib`

- **Checks:** `exists()`, `isfile()`, `isdir()`, `isabs()`.  
**路径检查：**`exists()`、`isfile()`、`isdir()`、`isabs()`。

- **Abs/Real:** `abspath()`, `realpath()`; **Join:** `os.path.join()`.  
**绝对/真实路径：**`abspath()`、`realpath()`；**拼接：**`os.path.join()`。

- **`pathlib`** (Py3.4+): `Path()` objects; build with `/` operator, rich methods.  
**`pathlib`**（Py3.4+）：`Path()` 对象；用 `/` 运算拼接，方法丰富。

> 以上要点来自讲义“pathlib 使用例”。  
> 引自讲义 **pathlib** 示例页。 

---

## Exercises — Primes (1) & (2) / 演习——素数（1）与（2）

**Prime (1)**  
- Write `is_prime(n)` and **`prime_list_1(n)`** (return all primes ≤ n).  
**编写**`is_prime(n)`**与**`prime_list_1(n)`（返回 ≤ n 的所有素数）。

- Provided testbench validates against primes ≤ 50.  
**提供的测试脚本**会比对 **≤50 的素数**。 

**Prime (2)**  
- Optimize as **`prime_list_2(n)`**; measure 1k..10k in steps of 1k with `%timeit`.  
**实现更快的**`prime_list_2(n)`；用 `%timeit` 在 **1k..10k**（步长 **1k**）测时。 

- Then plot **prime_list_1 vs prime_list_2** timings with the sample **Matplotlib** script.  
随后用提供的 **Matplotlib** 示例脚本绘制两者耗时对比。 

---

## Timing with `%timeit` / 用 `%timeit` 测速

- In Jupyter, prefix with `%timeit` to benchmark a single statement; loop over n.  
在 Jupyter 中用 `%timeit` 基准单条语句；在循环中遍历 `n`。

- Two helper scripts iterate 1000..10000 and print timings.  
两段辅助脚本遍历 **1000..10000** 并打印耗时。 

---

## Plotting time curves / 绘制时间曲线

- Use the given template: set `x`, `y_1` (ms for list_1), `y_2` (ms for list_2), then `ax.plot`.  
使用给定模板：设置 `x`、`y_1`（list_1 毫秒）、`y_2`（list_2 毫秒），然后 `ax.plot`。

- Label axes, enable grid, `plt.savefig(...)` then `plt.show()`.  
标注坐标轴、启用网格、`plt.savefig(...)` 后 `plt.show()`。 

---

## Implementation Notes & Minimal Tests / 实现思路与最小对拍

**`is_prime(n)`**  
- Return `False` for `n < 2`. Check divisibility by **2** then test **odd divisors up to `sqrt(n)`**.  
**`n < 2` 返回 `False`**；先判 2，再测试**奇数因子 ≤ `sqrt(n)`**。

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```

**`prime_list_1(n)` — baseline**  
- Call `is_prime(k)` for each `k` from **2..n**; simple but slower.  
**遍历 2..n 调 `is_prime(k)`；简单但偏慢。**

```python
def prime_list_1(n: int):
    return [k for k in range(2, n+1) if is_prime(k)]
```

**`prime_list_2(n)` — faster**  
- Either **skip evens + stop at sqrt**, or implement a **sieve (Eratosthenes)**.  
**要么跳过偶数并止于 sqrt**，**要么写埃氏筛**。

```python
def prime_list_2(n: int):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            sieve[p*p : n+1 : step] = b"\x00" * ((n - p*p)//step + 1)
        p += 1
    return [i for i in range(2, n+1) if sieve[i]]
```

**Minimal tests / 最小对拍**  
- Use provided benches `prime_list_1.py` and `prime_list_2.py`.  
**用提供的测试脚本**进行对拍。 

**I/O demo with `poem.txt`**  
- Example file content is defined as a Python triple‑quoted string; you can write/read it to test.  
**示例 `poem.txt` 定义为三引号字符串；可写入/读取用于测试。** 

```python
from pathlib import Path

poem = '''There was a young lady named Bright,
whose speed was far faster than light:
She started one day
In a relative way,
And returned on the previous night.'''

# write
Path("poem.txt").write_text(poem, encoding="utf-8")

# read
print(Path("poem.txt").read_text(encoding="utf-8").splitlines()[0])
```

---

## Complexity Analysis / 复杂度分析

**`prime_list_1(n)` (trial division) / 试除法基线**  
- Each `k` in `[2..n]` tests up to `sqrt(k)` divisors → **~ O(n · √n)** time, **O(1)** extra space.  
**对区间 `[2..n]` 的每个 `k` 最多试到 `√k` 个因子 → 时间 **约 O(n · √n)**，额外空间 **O(1)**。

**`prime_list_2(n)` (Eratosthenes) / 埃氏筛**  
- Marks each composite by its smallest prime factor; total work is **~ O(n log log n)** with **O(n)** space.  
**通过最小质因子标记合数；总体工作量 **约 O(n log log n)**，空间 **O(n)**。

**`is_prime(n)` / 单点判定**  
- Checks odd divisors up to `sqrt(n)` → **O(√n)** time, **O(1)** space.  
**仅检查奇数因子至 `√n` → 时间 **O(√n)**，空间 **O(1)**。

> tips / 建议：当需要“全部 ≤ n 的素数”时优先 **埃氏筛**；当只偶尔判定单个整数的素性时使用 **is_prime** 更直接。

---

## Source Files / 源码文件

- [`Python/src/is_prime.py`](./Python/src/is_prime.py)  —  [Download / 下载](sandbox:/mnt/data/Python/src/is_prime.py)  
**说明：**单点素数判定。

- [`Python/src/prime_list_1.py`](./Python/src/prime_list_1.py)  —  [Download / 下载](sandbox:/mnt/data/Python/src/prime_list_1.py)  
**说明：**基线生成器（试除法）。

- [`Python/src/prime_list_2.py`](./Python/src/prime_list_2.py)  —  [Download / 下载](sandbox:/mnt/data/Python/src/prime_list_2.py)  
**说明：**埃氏筛，更快。

- [`Python/src/Timeit-1.py`](./Python/src/Timeit-1.py)  —  [Download / 下载](sandbox:/mnt/data/Python/src/Timeit-1.py)  
**说明：**对 `prime_list_1` 在 n=1000..10000 的 `%timeit` 基准脚本。

- [`Python/src/Timeit-2.py`](./Python/src/Timeit-2.py)  —  [Download / 下载](sandbox:/mnt/data/Python/src/Timeit-2.py)  
**说明：**对 `prime_list_2` 在 n=1000..10000 的 `%timeit` 基准脚本。

---

## Plot Script / 绘图脚本

- [`Python/src/plot_graph_1-2.py`](./Python/src/plot_graph_1-2.py) — [Download / 下载](sandbox:/mnt/data/Python/src/plot_graph_1-2.py)  
**说明：**直接导入 `prime_list_1/2`，在 `n = 1000..10000` 基准测试后生成：
  - `outputs/plots/prime_timeit.csv`（CSV 数据）  
  - `outputs/plots/prime_timeit.json`（JSON 数据）  
  - `outputs/plots/prime_timeit.png`（曲线图）

> 用法：在项目根目录执行：  
> `python Python/src/plot_graph_1-2.py`

<h2></h2>

[← Previous Lecture / 上一讲](./lecture07.md) · [Next Lecture / 下一讲 →](./lecture09.md) · [Course Directory / 课程目录](./README.md#toc) · [Notes Home / 笔记首页](./README.md)

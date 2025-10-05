# plot_graph_1-2.py
from __future__ import annotations

import json
import math
import time
from pathlib import Path
from typing import Iterable, List, Tuple, Optional

import matplotlib.pyplot as plt

# ---------- Config / 配置 ----------
RANGE_START = 1000   # inclusive / 起始（含）
RANGE_STOP  = 10000  # inclusive / 结束（含）
RANGE_STEP  = 1000   # step / 步长
REPEAT      = 5      # repeats per n / 每个 n 重复次数
NUMBER      = 1      # loops per repeat / 每次重复调用次数

# Output locations / 输出位置
OUT_DIR = Path(__file__).resolve().parents[2] / "outputs" / "plots"
OUT_DIR.mkdir(parents=True, exist_ok=True)
CSV_PATH = OUT_DIR / "prime_timeit.csv"
JSON_PATH = OUT_DIR / "prime_timeit.json"
PNG_PATH = OUT_DIR / "prime_timeit.png"


def _bench(func, n: int) -> float:
    """Measure wall-clock seconds for a single run of func(n).
    用壁钟时间测一次 func(n) 的耗时（秒）。
    """
    t0 = time.perf_counter()
    func(n)
    t1 = time.perf_counter()
    return t1 - t0


def _stat(samples: List[float]) -> Tuple[float, float]:
    """Return mean and stdev of a list of samples (seconds).
    返回样本的均值与标准差（秒）。
    """
    if not samples:
        return 0.0, 0.0
    m = sum(samples) / len(samples)
    v = sum((x - m) ** 2 for x in samples) / max(1, (len(samples) - 1))
    return m, math.sqrt(v)


def time_series(list_fn, ns: Iterable[int]) -> List[Tuple[int, float, float]]:
    """Return [(n, mean_ms, stdev_ms), ...] for the given prime list function.
    对给定素数生成函数返回 [(n, 平均毫秒, 标准差毫秒), ...]。
    """
    out = []
    for n in ns:
        samples = []
        for _ in range(REPEAT):
            t = 0.0
            for _ in range(NUMBER):
                t += _bench(list_fn, n)
            samples.append(t / NUMBER)
        mean_s, std_s = _stat(samples)
        out.append((n, mean_s * 1000.0, std_s * 1000.0))
        print(f"n={n:5d}  mean={mean_s*1000:8.3f} ms  std={std_s*1000:7.3f} ms")
    return out


def save_csv_json(series1, series2, label1="prime_list_1", label2="prime_list_2"):
    """Save timing data to CSV and JSON files.
    将时序数据保存为 CSV 与 JSON 文件。
    """
    # CSV
    with CSV_PATH.open("w", encoding="utf-8") as f:
        f.write("n,%s(ms),%s_sd(ms),%s(ms),%s_sd(ms)\n" % (label1, label1, label2, label2))
        for (n1, m1, s1), (n2, m2, s2) in zip(series1, series2):
            assert n1 == n2
            f.write(f"{n1},{m1:.6f},{s1:.6f},{m2:.6f},{s2:.6f}\n")
    # JSON
    data = {
        "label1": label1,
        "label2": label2,
        "series1": series1,
        "series2": series2,
    }
    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved CSV -> {CSV_PATH}")
    print(f"Saved JSON -> {JSON_PATH}")


def plot(series1, series2, label1="prime_list_1", label2="prime_list_2", title="Prime list timing"):
    """Plot time curves and save PNG.
    绘制时间曲线并保存 PNG。
    """
    xs  = [n for n, _, _ in series1]
    y1  = [m for _, m, _ in series1]
    y2  = [m for _, m, _ in series2]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(xs, y1, marker="o", label=label1)
    ax.plot(xs, y2, marker="o", label=label2)
    ax.set_xlabel("n (upper bound)")
    ax.set_ylabel("time (ms)")
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150)
    print(f"Saved plot -> {PNG_PATH}")


def main():
    # Lazy import local implementations / 延迟导入本地实现
    from prime_list_1 import prime_list_1
    from prime_list_2 import prime_list_2

    ns = list(range(RANGE_START, RANGE_STOP + 1, RANGE_STEP))
    print("Benchmarking prime_list_1 ...")
    s1 = time_series(prime_list_1, ns)
    print("\nBenchmarking prime_list_2 ...")
    s2 = time_series(prime_list_2, ns)

    save_csv_json(s1, s2, "prime_list_1", "prime_list_2")
    plot(s1, s2, "prime_list_1", "prime_list_2", "Prime list timing (lower is better)")


if __name__ == "__main__":
    main()

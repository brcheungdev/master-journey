# prime_list_1.py

from __future__ import annotations
from typing import List
from is_prime import is_prime

def prime_list_1(n: int) -> List[int]:
    """
    Baseline prime generator: test each k in [2..n] with is_prime(k).
    朴素版素数生成器：遍历区间 [2..n]，逐个调用 is_prime(k)。

    Time complexity / 时间复杂度：约 O(n * sqrt(n)).
    """
    if n < 2:
        return []
    return [k for k in range(2, n + 1) if is_prime(k)]


if __name__ == "__main__":
    # Minimal smoke test / 最小化自测
    print(prime_list_1(30))  # -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

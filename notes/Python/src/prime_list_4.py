# prime_list_4.py
from __future__ import annotations
from typing import List

def prime_list_4(n: int) -> List[int]:
    """
    Faster sieve using an odd-only array:
      index i represents number (2*i + 3)  ->  3,5,7,...
    仅奇数的埃氏筛：索引 i 对应奇数 (2*i+3)，即 3,5,7,...
    """
    if n < 2:
        return []
    # '2' is the only even prime / 2 是唯一偶素数
    primes = [2] if n >= 2 else []

    # Count of odd numbers from 3..n (inclusive) / 区间 3..n 的奇数个数
    m = (n - 1) // 2
    if m <= 0:
        return primes

    # Bytearray as boolean flags for odds / 奇数位的布尔标记
    sieve = bytearray(b"\x01") * m  # True-like
    # For each odd prime p, start crossing off from p*p
    # 对每个奇素数 p，从 p*p 开始划去其倍数
    # Mapping: odd number -> index:  i = (p - 3)//2
    # p upper bound: p*p <= n  ->  p <= sqrt(n)
    import math
    limit = int(math.isqrt(n))
    # Iterate only over candidate odd p / 仅遍历奇数候选 p
    p = 3
    while p <= limit:
        i = (p - 3)//2
        if sieve[i]:
            # start index for p*p
            start_num = p * p
            # convert start_num to index in odd-array
            start_idx = (start_num - 3)//2
            step = p  # step in terms of numbers, maps to index stride p
            sieve[start_idx : m : step] = b"\x00" * ((m - start_idx - 1)//step + 1)
        p += 2

    # Collect odds that remain True / 收集仍为 True 的奇数位
    primes.extend(2*i + 3 for i in range(m) if sieve[i] and (2*i + 3) <= n)
    return primes


if __name__ == "__main__":
    print(prime_list_4(50))

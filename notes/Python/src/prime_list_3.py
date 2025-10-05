# prime_list_3.py
from __future__ import annotations
from typing import List

def prime_list_3(n: int) -> List[int]:
    """
    Sieve of Eratosthenes (standard form) to list primes <= n.
    标准埃氏筛：返回所有 <= n 的素数。
    """
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)  # True-like bytes / 以字节模拟布尔
    sieve[0:2] = b"\x00\x00"             # 0,1 非素数

    p = 2
    # Mark multiples from p*p (safe start) / 从 p*p 开始标记倍数
    while p * p <= n:
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : n + 1 : step] = b"\x00" * ((n - start)//step + 1)
        p += 1

    return [i for i in range(2, n + 1) if sieve[i]]


if __name__ == "__main__":
    print(prime_list_3(50))

# prime_list_2.py
from __future__ import annotations
from typing import List

def prime_list_2(n: int) -> List[int]:
    """
    Faster prime generator using the Sieve of Eratosthenes.
    采用埃氏筛的更快素数生成器。

    Algorithm / 算法：
      - Allocate a boolean sieve of size n+1, mark 0/1 as non-prime.
        分配大小为 n+1 的布尔筛，标记 0/1 为非素数。
      - For p from 2 to floor(sqrt(n)):
        对 p=2..sqrt(n) 迭代：
          If sieve[p] is True, mark multiples p*p, p*(p+1), ... as False.
          若 sieve[p] 为真，则从 p*p 开始标记其倍数为 False。
      - Collect indices still True as primes.
        将仍为 True 的下标收集为素数表。
    Complexity / 复杂度：约 O(n log log n) 时间，O(n) 空间。
    """
    if n < 2:
        return []
    sieve = bytearray(b"") * (n + 1)
    sieve[0:2] = b"

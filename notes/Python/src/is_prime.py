# is_prime.py
from __future__ import annotations

def is_prime(n: int) -> bool:
    """
    Return True if n is a prime, else False.
    素数判定：若 n 为素数返回 True，否则返回 False。

    Rules / 规则：
      - n < 2 -> False
        n < 2 时不是素数。
      - Even numbers other than 2 are not prime.
        除 2 外的所有偶数都不是素数。
      - Test only odd divisors up to sqrt(n).
        仅测试不超过 sqrt(n) 的奇数因子。
    """
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


if __name__ == "__main__":
    # Minimal smoke test / 最小化自测
    tests = {0: False, 1: False, 2: True, 3: True, 4: False, 29: True, 49: False}
    for k, exp in tests.items():
        got = is_prime(k)
        print(f"is_prime({k}) = {got} : {got == exp}")

# P3.py
from __future__ import annotations

def P3(n: int) -> int:
    """
    Triangular number by recursion:
      P3(0) = 0
      P3(n) = P3(n-1) + n  (n >= 1)
    递归求三角数：P3(0)=0；P3(n)=P3(n-1)+n（n>=1）。
    """
    if n < 0:
        raise ValueError("n must be non-negative / n 必须为非负")
    if n == 0:
        return 0
    return P3(n - 1) + n


if __name__ == "__main__":
    # Minimal self-test mirroring the provided testbench
    exp = (0, 1, 3, 6, 10, 15, 21, 28, 36, 45)
    ok = True
    for i, want in enumerate(exp):
        got = P3(i)
        ok &= (got == want)
        print(f"P3({i}) = {got:3} : {got == want}")
    print("\nCongratulations!" if ok else "\nTry again!")

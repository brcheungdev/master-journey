# P5.py
from __future__ import annotations

def P5(n: int) -> int:
    """
    Pentagonal number by recursion:
      P5(0) = 0
      P5(n) = P5(n-1) + (3*n - 2)  (n >= 1)
    递归求五角数：P5(0)=0；P5(n)=P5(n-1)+(3*n-2)（n>=1）。
    """
    if n < 0:
        raise ValueError("n must be non-negative / n 必须为非负")
    if n == 0:
        return 0
    return P5(n - 1) + 3 * n - 2


if __name__ == "__main__":
    exp = (0, 1, 5, 12, 22, 35, 51, 70, 92, 117)
    ok = True
    for i, want in enumerate(exp):
        got = P5(i)
        ok &= (got == want)
        print(f"P5({i}) = {got:3} : {got == want}")
    print("\nCongratulations!" if ok else "\nTry again!")

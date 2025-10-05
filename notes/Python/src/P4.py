# P4.py
from __future__ import annotations

def P4(n: int) -> int:
    """
    Square number by recursion:
      P4(0) = 0
      P4(n) = P4(n-1) + (2*n - 1)  (n >= 1)
    递归求四角数：P4(0)=0；P4(n)=P4(n-1)+(2*n-1)（n>=1）。
    """
    if n < 0:
        raise ValueError("n must be non-negative / n 必须为非负")
    if n == 0:
        return 0
    return P4(n - 1) + 2 * n - 1


if __name__ == "__main__":
    exp = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
    ok = True
    for i, want in enumerate(exp):
        got = P4(i)
        ok &= (got == want)
        print(f"P4({i}) = {got:3} : {got == want}")
    print("\nCongratulations!" if ok else "\nTry again!")

# PP.py
from __future__ import annotations

def P(p: int, n: int) -> int:
    """
    General polygonal numbers by recursion:
      Closed form:   P(p, n) = ((p-2)*n^2 - (p-4)*n) / 2
      Recurrence:    P(p, 0) = 0
                     P(p, n) = P(p, n-1) + (p-2)*n - (p-3)  (n >= 1)
    一般多角数的递归：闭式 P(p,n)=((p-2)*n^2-(p-4)*n)/2；
    递推：P(p,0)=0；P(p,n)=P(p,n-1)+(p-2)*n-(p-3)（n>=1）。
    """
    if n < 0:
        raise ValueError("n must be non-negative / n 必须为非负")
    if p < 2:
        raise ValueError("p must be >= 2 / p 必须 >= 2")
    if n == 0:
        return 0
    return P(p, n - 1) + (p - 2) * n - (p - 3)


if __name__ == "__main__":
    exp = {
        2: (0, 1,  2,  3,  4,  5,   6,   7,   8,   9),
        3: (0, 1,  3,  6, 10, 15,  21,  28,  36,  45),
        4: (0, 1,  4,  9, 16, 25,  36,  49,  64,  81),
        5: (0, 1,  5, 12, 22, 35,  51,  70,  92, 117),
        6: (0, 1,  6, 15, 28, 45,  66,  91, 120, 153),
        7: (0, 1,  7, 18, 34, 55,  81, 112, 148, 189),
        8: (0, 1,  8, 21, 40, 65,  96, 133, 176, 225),
        9: (0, 1,  9, 24, 46, 75, 111, 154, 204, 261),
       10: (0, 1, 10, 27, 52, 85, 126, 175, 232, 297),
    }
    ok = True
    for p in range(2, 11):
        for i, want in enumerate(exp[p]):
            got = P(p, i)
            ok &= (got == want)
            print(f"P({p},{i}) = {got:3} : {got == want}")
        print()
    print("Congratulations!" if ok else "Try again!")

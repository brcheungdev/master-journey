# FizzBuzz.py
from __future__ import annotations

def fizz_buzz(n: int):
    """
    Classic FizzBuzz:
      - If n is divisible by 15 -> "FizzBuzz"
      - Else if divisible by 3  -> "Fizz"
      - Else if divisible by 5  -> "Buzz"
      - Else return the original number n

    经典 FizzBuzz 规则：
      - 若 n 能被 15 整除 -> 返回 "FizzBuzz"
      - 否则若能被 3 整除 -> 返回 "Fizz"
      - 否则若能被 5 整除 -> 返回 "Buzz"
      - 否则返回 n 本身
    """
    # 先判断 15，避免 3 和 5 的条件提前命中 / Check 15 first to avoid early match by 3 or 5.
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Optional self-test matching your provided testbench
    # 与题目给出的测试向量一致的自测（可选）
    # ------------------------------------------------------------
    exp = (
        1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
        'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17,
        'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
        26, 'Fizz', 28, 29, 'FizzBuzz'
    )

    success = True
    for i in range(30):
        n = i + 1
        result = fizz_buzz(n)
        passed = (result == exp[i])
        success = success and passed
        print(f"fizz_buzz({n}) = {result} : {passed}")

    print("\nCongratulations!" if success else "\nTry again!")

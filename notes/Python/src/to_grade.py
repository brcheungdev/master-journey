# to_grade.py

from __future__ import annotations

def to_grade(score: int) -> str:
    """
    Map a numeric score to a letter grade.
    将分数映射到等级。

    Rules / 规则：
      - score > 100  -> "H"   # higher than range / 高于上限
      - 80..100      -> "A"
      - 70..79       -> "B"
      - 60..69       -> "C"
      - 0..59        -> "F"
      - score < 0    -> "L"   # lower than range / 低于下限

    Notes / 说明：
      - Boundaries are inclusive on the left as shown, e.g. 80 -> "A", 60 -> "C".
        边界按上表处理，例如 80 → "A"，60 → "C"。
      - Input is assumed to be an integer; if floats are possible, consider int(score).
        假定输入为整数；若可能为浮点，可按需先 int(score)。
    """
    if score > 100:
        return "H"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 0:
        return "F"
    return "L"


if __name__ == "__main__":
    # ---------------------------------------------------------
    # Optional self-test (mirrors your provided testbench)
    # 可选自测：与题目给出的测试向量一致
    # ---------------------------------------------------------
    test_vec = (
        (-10, "L"), ( 0, "F"),  (10, "F"),  (30, "F"),
        (50, "F"),  (59, "F"),  (60, "C"),  (69, "C"),
        (70, "B"),  (79, "B"),  (80, "A"),  (89, "A"),
        (90, "A"),  (95, "A"),  (100, "A"), (110, "H"),
    )

    success = True
    for score, exp in test_vec:
        grade  = to_grade(score)
        passed = (grade == exp)
        success = success and passed
        print(f"to_grade({score}) = {grade} : {passed}")

    print("\nCongratulations!" if success else "\nTry again")

# bmi.py
from __future__ import annotations

def bmi(weight: float, height: float) -> int:
    """Compute BMI = weight / (height**2) and truncate to int.
    计算 BMI = 体重 / (身高**2)，并截断为整数（向零取整）。

    Args:
        weight (float): kilograms
        height (float): meters
    Returns:
        int: truncated BMI
    Raises:
        ValueError: if weight <= 0 or height <= 0
    """
    if weight <= 0 or height <= 0:
        raise ValueError("weight and height must be positive / 体重与身高必须为正数")
    # Truncate the fractional part as required by the spec / 按规范截断小数部分
    return int(weight / (height * height))


if __name__ == "__main__":
    # ---------------------------------------------------------------
    # Optional quick self-test mirroring the provided testbench
    # 可选自测：与给定测试向量一致
    # ---------------------------------------------------------------
    test_vecs = (  # ((weight, height), expected_int_bmi)
        ((50, 1.5), 22), ((50, 1.6), 19),
        ((50, 1.7), 17), ((50, 1.8), 15),
        ((55, 1.5), 24), ((55, 1.6), 21),
        ((55, 1.7), 19), ((55, 1.8), 16),
        ((60, 1.5), 26), ((60, 1.6), 23),
        ((60, 1.7), 20), ((60, 1.8), 18),
        ((65, 1.5), 28), ((65, 1.6), 25),
        ((65, 1.7), 22), ((65, 1.8), 20),
    )

    success = True
    for (w_h, exp) in test_vecs:
        w, h = w_h
        val = bmi(w, h)
        ok = (val == exp)
        success &= ok
        print(f"bmi({w}, {h}) = {val} : {ok}")

    print("\nCongratulations!" if success else "\nTry again!")

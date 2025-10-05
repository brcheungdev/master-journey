# heron.py
import math

def heron(a: float, b: float, c: float) -> float:
    """Compute triangle area by Heron's formula.
    使用海伦公式计算三角形面积。

    Steps:
      1) Validate sides are positive and satisfy triangle inequality.
      2) s = (a + b + c) / 2
      3) area = sqrt(s * (s - a) * (s - b) * (s - c))
      4) Return a float (rounded to 10 decimals to avoid tiny FP noise).

    参数:
      a, b, c: 三边长度（float）

    返回:
      float: 三角形面积
    """
    # 1) 基本校验：正数与三角不等式
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive / 边长必须为正数")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle sides / 不满足三角不等式")

    # 2) 半周长 s
    s = (a + b + c) / 2.0

    # 3) 公式内被开方部分（为便于阅读拆成变量）
    # radicand = s * (s - a) * (s - b) * (s - c)
    sa = s - a
    sb = s - b
    sc = s - c
    radicand = s * sa * sb * sc

    # 数值健壮性：理论上 radicand >= 0；若出现极微小负数（浮点误差），夹紧为 0
    if radicand < 0 and abs(radicand) < 1e-12:
        radicand = 0.0
    if radicand < 0:
        # 对于有效输入一般不会发生；若发生说明入参存在问题
        raise ValueError("Negative radicand; check inputs / 被开方数为负，请检查入参")

    area = math.sqrt(radicand)

    # 4) 为通过严格相等测试，适度四舍五入成“干净”的十进制数（如 6.0、13.5、24.0）
    return round(area, 10)


if __name__ == "__main__":
    # 与给定测试向量一致的自测（可选）
    test_vecs = (  # ((a, b, c), exp)
        ((3, 4, 5), 6.0), ((3, 5, 4), 6.0),
        ((4, 3, 5), 6.0), ((4, 5, 3), 6.0),
        ((5, 3, 4), 6.0), ((5, 4, 3), 6.0),
        ((4.5, 6, 7.5), 13.5), ((4.5, 7.5, 6), 13.5),
        ((6, 4.5, 7.5), 13.5), ((6, 7.5, 4.5), 13.5),
        ((7.5, 4.5, 6), 13.5), ((7.5, 6, 4.5), 13.5),
        ((6, 8, 10), 24.0), ((6, 10, 8), 24.0),
        ((8, 6, 10), 24.0), ((8, 10, 6), 24.0),
        ((10, 6, 8), 24.0), ((10, 8, 6), 24.0),
    )

    success = True
    for ((a, b, c), exp) in test_vecs:
        area = heron(a, b, c)
        ok = (area == exp)
        success &= ok
        print(f"heron({a}, {b}, {c}) = {area} : {ok}")

    print("\nCongratulations!" if success else "\nTry again!")

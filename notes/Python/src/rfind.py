# rfind.py
def rfind(string: str, word: str) -> int:
    """
    Return the highest (rightmost) index where substring `word` is found in `string`,
    or -1 if `word` does not occur.
    返回子串 `word` 在 `string` 中最右（最大）起始下标；未找到则返回 -1。

    Notes / 说明：
      - We do NOT call the built-in str.rfind(); this is a manual implementation.
        不调用内置 str.rfind()，手工实现。
      - Empty substring behavior matches Python: rfind("", s) == len(s).
        空子串行为与 Python 一致：rfind("", s) == len(s)。
    """
    n = len(string)
    m = len(word)

    # 空子串：约定返回 len(string)
    if m == 0:
        return n

    # 从最后一个可能的起点 (n - m) 向左扫描到 0
    # Scan candidate starts from right to left
    for i in range(n - m, -1, -1):
        if string[i:i + m] == word:
            return i
    return -1


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Optional self-test (mirrors your provided testbench)
    # 自测：与题目给出的测试向量一致
    # ------------------------------------------------------------
    string = "It rains cats and dogs."
    test_vecs = (
        ("I", 0),  ("a", 14), ("b", -1), ("c", 9),
        ("d", 18), ("e", -1), ("f", -1), ("g", 20),
        ("h", -1), (".", 22),
    )

    print(f"{string = }")
    print()

    success = True
    for (word, exp) in test_vecs:
        offset = rfind(string, word)
        passed = (offset == exp)
        success &= passed
        print(f"find(string, {word}) = {offset} : \t{passed}")

    print("\nCongratulations!" if success else "\nTry again!")

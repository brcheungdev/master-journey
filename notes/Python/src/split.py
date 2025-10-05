# split.py
from typing import List

def split(string: str, sep: str) -> List[str]:
    """
    Split `string` by exact separator `sep` (must be non-empty).
    按精确分隔符 `sep` 拆分字符串（`sep` 不能为空）。

    Behavior (matches Python with explicit sep) / 行为（与 Python 显式 sep 一致）：
      - Preserves empty fields for consecutive/edge separators:
        e.g. split("a,,b,", ",") -> ["a", "", "b", ""]
        对连续/边界分隔符保留空字段。
      - If `sep` not found, returns [string].
        若未找到分隔符，返回 [string]。
      - If `sep == ""`, raise ValueError("empty separator").
        若 `sep == ""`，抛出 ValueError("empty separator")。
    """
    if sep == "":
        raise ValueError("empty separator")

    parts: List[str] = []
    start = 0
    seplen = len(sep)

    while True:
        idx = string.find(sep, start)  # 允许使用 .find()，不使用 .split()
        if idx == -1:
            # no more separator; append the tail / 没有更多分隔符；追加尾部
            parts.append(string[start:])
            break
        # substring before this sep / 当前分隔符之前的子串
        parts.append(string[start:idx])
        # move start past the separator / 将起点移到分隔符之后
        start = idx + seplen

    return parts


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Optional self-test (mirrors your provided testbench)
    # 自测：与题目给出的测试脚本一致
    # ------------------------------------------------------------
    word_list = ['It', 'rains', 'cats', 'and', 'dogs.']
    seps = (" ", "/", "_")

    success = True
    for sep in seps:
        print()
        print(f"{sep = }")
        string = sep.join(word_list)
        print(f"{string = }")
        result = split(string, sep)
        truth = (result == word_list)
        print(f"{result = } : {truth}")
        success &= truth

    print("\nCongratulations!" if success else "\nTry again!")

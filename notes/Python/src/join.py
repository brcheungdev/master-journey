# join.py
from typing import Iterable, Any

def join(iterable: Iterable[Any], sep: str) -> str:
    """
    Concatenate items in `iterable` with separator `sep`, without using str.join().
    用分隔符 `sep` 连接 `iterable` 中的各项，**不使用内置的 str.join()**。

    Behavior (matches Python) / 行为（与 Python 一致）：
      - Empty iterable -> ""          空序列返回空字符串
      - Single item    -> str(item)   单一元素不加分隔符
      - Each element is converted to str() before concatenation
        连接前对每个元素执行 str() 转换

    Examples / 示例:
      join([], " ")                         -> ""
      join(["cats"], " ")                   -> "cats"
      join(["It","rains","cats"], " ")      -> "It rains cats"
      join([1, 2, 3], "-")                  -> "1-2-3"
    """
    out = ""
    first = True
    for item in iterable:
        if not first:
            out += sep        # 追加分隔符 / append separator between items
        out += str(item)      # 统一转为字符串 / stringify each item
        first = False
    return out


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Optional self-test (mirrors the provided testbench)
    # 自测：与题目给出的测试脚本一致
    # ------------------------------------------------------------
    iterables = (
        [],
        ["cats"],
        ['It', 'rains', 'cats', 'and', 'dogs.'],
    )
    seps = [" ", "/", "--"]

    success = True
    for iterable in iterables:
        print()
        print(f"{iterable = }")
        for sep in seps:
            string = join(iterable, sep)
            truth = (string == sep.join(iterable)) 
            print(f'sep    = "{sep}"')
            print(f'string = "{string}" : {truth}')
            success &= truth

    print("\nCongratulations!" if success else "\nTry again!")

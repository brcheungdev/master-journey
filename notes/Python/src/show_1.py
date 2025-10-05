# show_1.py
from typing import List, Any

def show_1(a: List[List[Any]]) -> None:
    """Print a 2‑D list without a frame; items separated by a single space.
    打印二维列表（不带外框）；同一行元素以单个空格分隔。
    """
    # Handle empty input / 处理空输入
    if not a:
        print("")  # print a blank line to indicate "nothing"
        return

    for row in a:
        # Convert every cell to string / 将每个单元格转为字符串
        cells = [str(x) for x in row]
        # Join by a single space / 用单个空格连接
        line = " ".join(cells)
        print(line)


if __name__ == "__main__":
    # Minimal sanity tests / 最小自测
    show_1([[0,1,2]])
    print("---")
    show_1([[0,1,2],[2,0,1],[1,2,0]])

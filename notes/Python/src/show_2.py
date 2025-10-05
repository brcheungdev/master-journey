# show_2.py
from typing import List, Any

def _col_widths(a: List[List[Any]]) -> List[int]:
    """Compute max display width for each column (string length).
    计算每列的最大显示宽度（按字符串长度）。
    """
    if not a:
        return []
    cols = max((len(row) for row in a), default=0)
    widths = [0] * cols
    for row in a:
        for j in range(cols):
            val = "" if j >= len(row) else str(row[j])
            widths[j] = max(widths[j], len(val))
    return widths

def show_2(a: List[List[Any]]) -> None:
    """Print a 2‑D list with an outer frame.
    使用外框打印二维列表。
    """
    widths = _col_widths(a)
    # Build border like +-----+---+ ... / 构建边框
    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+" if widths else "+ +"

    print(border)
    for row in a:
        cells = []
        for j, w in enumerate(widths):
            s = "" if j >= len(row) else str(row[j])
            # Pad with one space on both sides; left align within width
            # 两侧各留一空格；列宽内左对齐
            cells.append(" " + s.ljust(w) + " ")
        print("|" + "|".join(cells) + "|")
        print(border)
    if not a:
        # Empty matrix: just show an empty frame / 空矩阵：打印空框
        pass


if __name__ == "__main__":
    # Minimal sanity tests / 最小自测
    show_2([[0,1,2]])
    show_2([[0,1,2],[2,0,1],[1,2,0]])

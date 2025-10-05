# show_3.py
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

def show_3(a: List[List[Any]]) -> None:
    """Print inner grid only (no outer frame): cells separated by ' | ', row
    separators printed between rows only.
    仅打印内部网格（无外框）：同一行用 ' | ' 分隔，不同行之间打印分隔线。
    """
    widths = _col_widths(a)
    if not widths:
        print("")
        return

    # Row separator (between data rows) / 行间分隔线
    sep = "+".join("-" * (w + 2) for w in widths)

    for i, row in enumerate(a):
        cells = []
        for j, w in enumerate(widths):
            s = "" if j >= len(row) else str(row[j])
            cells.append(" " + s.center(w) + " ")
        print(" | ".join(cells))
        if i < len(a) - 1:
            print(sep)


if __name__ == "__main__":
    # Minimal sanity tests / 最小自测
    show_3([[0,1,2]])
    print()
    show_3([[0,1,2],[2,0,1]])
    print()
    show_3([[0,1,2],[2,0,1],[1,2,0]])

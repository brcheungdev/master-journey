# show_board.py
from __future__ import annotations
from typing import List

MARKS = ("-", "O", "X")  # 0 -> "-", 1 -> "O", 2 -> "X"
# 符号映射：0 -> "-", 1 -> "O", 2 -> "X"

def show_board(board: List[int]) -> None:
    """
    Print a 3x3 Tic-Tac-Toe board from a flat list of 9 ints (0/1/2).
    从长度为 9 的一维整数列表（取值 0/1/2）打印 3x3 井字棋盘。
    """
    if board is None or len(board) != 9:
        raise ValueError("board must be a list of length 9 / board 必须是长度为 9 的列表")
    for r in range(3):
        # Row r uses indices r*3 .. r*3+2 / 第 r 行使用下标 r*3..r*3+2
        row = [MARKS[board[r*3 + c]] for c in range(3)]
        print(" ".join(row))


if __name__ == "__main__":
    # Minimal smoke test / 最小化自测
    boards = [
        [0,1,2, 1,2,0, 2,0,1],
        [1,2,1, 2,0,2, 0,1,0],
    ]
    for b in boards:
        show_board(b)
        print("---")

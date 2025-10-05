# is_win.py
from __future__ import annotations
from typing import List, Tuple

# Winning line indices (rows, cols, diagonals)
# 获胜连线（行、列、对角线）
WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows / 行
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols / 列
    (0, 4, 8), (2, 4, 6),             # diagonals / 对角线
)

def is_win(board: List[int], player: int) -> bool:
    """
    Return True if 'player' (1 or 2) has a winning line on the board.
    若 'player'（1 或 2）在棋盘上成线则返回 True。
    """
    if board is None or len(board) != 9:
        raise ValueError("board must be a list of length 9 / board 必须是长度为 9 的列表")
    if player not in (1, 2):
        raise ValueError("player must be 1 or 2 / player 必须为 1 或 2")

    # Check any winning triple equals 'player' / 检查任一三连是否全等于 player
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


if __name__ == "__main__":
    # Minimal smoke tests / 最小自测
    print(is_win([1,1,1, 0,2,2, 2,0,1], 1))  # True: top row
    print(is_win([1,2,0, 1,2,0, 1,0,2], 1))  # True: left col
    print(is_win([2,1,0, 0,2,0, 0,1,2], 2))  # True: main diagonal

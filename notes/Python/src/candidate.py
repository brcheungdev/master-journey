# candidate.py
from __future__ import annotations
from typing import List

def candidate(board: List[int]) -> List[int]:
    """
    Return the list of empty indices (value==0) for the next move.
    返回所有可落子（值为 0）的索引列表。
    """
    if board is None or len(board) != 9:
        raise ValueError("board must be a list of length 9 / board 必须是长度为 9 的列表")
    # Validate values are only 0/1/2 / 校验只包含 0/1/2
    for v in board:
        if v not in (0, 1, 2):
            raise ValueError("board values must be 0/1/2 only / 棋盘值只能是 0/1/2")
    # 1
    return [i for i, v in enumerate(board) if v == 0]


if __name__ == "__main__":
    print(candidate([0,1,0, 2,1,2, 0,2,1]))  # -> [0,2,6]

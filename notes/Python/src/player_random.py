# player_random.py
from __future__ import annotations
from typing import List
import random

from candidate import candidate

def player_Random(board: List[int], player: int) -> int:
    """
    Select a random index from currently available positions; ignore 'player' for choice.
    从当前可落子位置中随机选择一个索引；对选择过程不使用 player 值。
    """
    cand = candidate(board)
    if not cand:
        raise ValueError("no legal moves / 无可落子位置")
    return random.choice(cand)


if __name__ == "__main__":
    random.seed(1234)
    print(player_Random([0,1,0, 2,1,2, 0,2,1], 1))  # deterministic under fixed seed

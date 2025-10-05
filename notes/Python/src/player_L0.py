# player_L0.py
from __future__ import annotations
import random
from typing import List

from candidate import candidate

# Priority groups inferred from Lecture 11 experiment:
# center(4) > corners(0,2,6,8) > edges(1,3,5,7)
# 来自第 11 讲实验的优先级：中 > 角 > 边（如需，可在笔记中用你的实测结果替换此顺序）。
CENTER = {4}
CORNERS = {0, 2, 6, 8}
EDGES = {1, 3, 5, 7}

def player_L0(board: List[int], player: int) -> int:
    """
    Choose a move from the best available group among candidates:
      1) center if free, else
      2) any corner, else
      3) any edge.
    从候选中按“中>角>边”的优先级选择：先中心，其次任意角，再次任意边。
    """
    cand = set(candidate(board))
    for group in (CENTER, CORNERS, EDGES):
        opts = list(cand & group)
        if opts:
            return random.choice(opts)
    # Fallback shouldn't happen if candidate() non-empty, but keep safe:
    return random.choice(list(cand))

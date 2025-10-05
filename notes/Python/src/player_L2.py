# player_L2.py
from __future__ import annotations
from typing import List
import random

from candidate import candidate
from is_win import is_win
from player_L0 import player_L0
from player_L1 import player_L1  # reuse logic for immediate win

def player_L2(board: List[int], player: int) -> int:
    """
    Priority:
      1) winning move for 'player';
      2) if none, block opponent's immediate win;
      3) else fall back to player_L0.
    优先级：先自己取胜；否则堵对手“一步取胜”；否则退回 L0。
    """
    # 1) Take winning move
    for pos in candidate(board):
        tmp = list(board)
        tmp[pos] = player
        if is_win(tmp, player):
            return pos

    # 2) Block opponent
    opp = 2 if player == 1 else 1
    for pos in candidate(board):
        tmp = list(board)
        tmp[pos] = opp
        if is_win(tmp, opp):
            return pos

    # 3) Fallback
    return player_L0(board, player)

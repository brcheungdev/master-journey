# player_L1.py
from __future__ import annotations
from typing import List
import random

from candidate import candidate
from is_win import is_win
from player_L0 import player_L0

def player_L1(board: List[int], player: int) -> int:
    """
    If there exists a move that gives an immediate win, take it;
    otherwise fall back to player_L0 (center>corner>edge).
    若存在“一步取胜”之处则立即取胜；否则退回 L0（中>角>边）。
    """
    for pos in candidate(board):
        tmp = list(board)
        tmp[pos] = player
        if is_win(tmp, player):
            return pos
    return player_L0(board, player)

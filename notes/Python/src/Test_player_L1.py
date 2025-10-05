# Test_player_L1.py
from __future__ import annotations
import random
from tictac_toe import game_control
from player_L0 import player_L0
from player_L1 import player_L1

if __name__ == "__main__":
    random.seed(20251212)
    w1, w2, d = game_control(count=5000, player_1=player_L1, player_2=player_L0)
    total = w1 + w2 + d
    print(f"L1 (P1) vs L0 (P2): w1={w1} w2={w2} d={d}  win-rate={w1/total:.3%}")

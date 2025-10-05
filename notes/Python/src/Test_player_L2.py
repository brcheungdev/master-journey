# Test_player_L2.py
from __future__ import annotations
import random
from tictac_toe import game_control
from player_L0 import player_L0
from player_L1 import player_L1
from player_L2 import player_L2

def run(pair, count=5000):
    random.seed(20251212)
    w1, w2, d = game_control(count=count, player_1=pair[0], player_2=pair[1])
    total = w1 + w2 + d
    return w1, w2, d, w1/total

if __name__ == "__main__":
    for title, pair in [
        ("L2 vs L1", (player_L2, player_L1)),
        ("L2 vs L0", (player_L2, player_L0)),
        ("L1 vs L0", (player_L1, player_L0)),
    ]:
        w1, w2, d, rate = run(pair, 5000)
        print(f"{title}: w1={w1} w2={w2} d={d}  win-rate={rate:.3%}")

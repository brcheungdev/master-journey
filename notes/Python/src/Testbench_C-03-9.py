# Testbench_C-03-9.py
from __future__ import annotations
import random
from tictac_toe import game_control
from player_random import player_Random
from player_L0 import player_L0
from template_next_move import M22W0000

def as_policy(func):
    # Wrap a "next move" function (board, player)->pos into a Policy(board,player)->pos
    def policy(board, player):
        return func(list(board), player)
    return policy

if __name__ == "__main__":
    random.seed(20251313)
    me = as_policy(M22W0000)

    for title, opp in [
        ("M22W0000 vs Random", player_Random),
        ("M22W0000 vs L0", player_L0),
    ]:
        w1, w2, d = game_control(count=5000, player_1=me, player_2=opp, Debug=0)
        total = w1 + w2 + d
        print(f"{title}: P1 win-rate={w1/total:.3%}  (w1={w1}, w2={w2}, d={d})")

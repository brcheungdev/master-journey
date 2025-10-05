# tictac_toe.py
from __future__ import annotations

import random
from typing import Callable, List, Tuple, Optional

from show_board import show_board
from is_win import is_win
from candidate import candidate
from player_random import player_Random as player_L0  # Level 0 bot

Board = List[int]
Player = int
Policy = Callable[[Board, Player], int]

def init_board() -> Board:
    """Return a fresh empty board (all zeros).
    返回一个新的空棋盘（全 0）。
    """
    return [0] * 9

def place(board: Board, pos: int, player: Player) -> None:
    """Place player's mark at pos if empty, else raise.
    若位置空则在 pos 落下 player 的子，否则抛错。
    """
    if not (0 <= pos < 9):
        raise ValueError("pos out of range 0..8 / 位置必须在 0..8")
    if board[pos] != 0:
        raise ValueError("cell occupied / 该位置已被占用")
    if player not in (1, 2):
        raise ValueError("player must be 1 or 2 / 玩家必须为 1 或 2")
    board[pos] = player

def play_game(board: Optional[Board] = None,
              player_1: Policy = player_L0,
              player_2: Policy = player_L0,
              Debug: int = 0) -> Tuple[int, Board, int]:
    """Play a game from the given board with two policies; return (winner, final_board, moves).
    用两种策略从给定棋面开始对局；返回 (胜者, 终局棋盘, 步数)。胜者：1/2/0(平局)。
    """
    if board is None:
        board = init_board()
    board = list(board)  # shallow copy / 浅拷贝，避免修改外部
    cur = 1  # player 1 starts / 先手为 1
    moves = 0

    while True:
        if is_win(board, 1):
            return 1, board, moves
        if is_win(board, 2):
            return 2, board, moves
        cand = candidate(board)
        if not cand:  # draw
            return 0, board, moves

        # Choose action
        pos = player_1(board, 1) if cur == 1 else player_2(board, 2)
        place(board, pos, cur)
        moves += 1
        if Debug >= 2:
            print(f"Move {moves}: P{cur} -> {pos}")
            if Debug >= 3:
                show_board(board)

        # Check win after move
        if is_win(board, cur):
            return cur, board, moves
        # Swap player
        cur = 2 if cur == 1 else 1

def game_control(count: int = 1000,
                 player_1: Policy = player_L0,
                 player_2: Policy = player_L0,
                 Debug: int = 0,
                 init_pos: Optional[int] = None) -> Tuple[int, int, int]:
    """Run multiple games, optionally forcing the first move at init_pos by player 1.
    执行多局对战；可选：强制先手的第一步下在 init_pos。返回 (wins_1, wins_2, draws)。
    """
    wins_1 = wins_2 = draws = 0
    for _ in range(count):
        board = init_board()
        if init_pos is not None:
            place(board, init_pos, 1)
        winner, _, _ = play_game(board, player_1, player_2, Debug)
        if winner == 1:
            wins_1 += 1
        elif winner == 2:
            wins_2 += 1
        else:
            draws += 1
    return wins_1, wins_2, draws

def document_it(func):
    """Simple debug decorator to print entering/exiting info when Debug >= 1.
    简单调试装饰器：当 Debug>=1 时打印进入/退出信息。
    """
    def wrapper(*args, **kwargs):
        print(f"[doc] enter {func.__name__}")
        out = func(*args, **kwargs)
        print(f"[doc] exit  {func.__name__} -> {out!r}")
        return out
    return wrapper

# Alias consistent with slides / 与讲义一致的别名导出
__all__ = [
    "init_board", "place", "show_board", "is_win",
    "player_L0", "play_game", "game_control", "document_it"
]

if __name__ == "__main__":
    # Quick demo: win-rate for first move at 0,1,4 (small sample)
    import random
    random.seed(0)
    for pos in (0, 1, 4):
        w1, w2, d = game_control(count=2000, init_pos=pos)  # smaller than 10000 for speed
        rate = w1 / (w1 + w2 + d)
        print(f"init_pos={pos}: P1 win-rate = {rate:.3f}  (w1={w1}, w2={w2}, d={d})")

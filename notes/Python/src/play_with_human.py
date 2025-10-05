# play_with_human.py
from __future__ import annotations

from typing import List, Optional

from tictac_toe import init_board, show_board, is_win, place, player_L0

def ask_move(board: List[int], player: int) -> int:
    """Ask human for a legal move (0..8)."""
    while True:
        try:
            pos = int(input(f"Your move (0..8) for player {player}: "))
            if not (0 <= pos < 9):
                print("Out of range.")
                continue
            if board[pos] != 0:
                print("Cell occupied.")
                continue
            return pos
        except Exception:
            print("Invalid input, try again.")

def play_with_human(human_is: int = 1, debug: int = 1) -> int:
    """Play a human vs baseline bot (player_L0). Return winner (1/2/0)."""
    board = init_board()
    cur = 1
    show_board(board)
    while True:
        if cur == human_is:
            pos = ask_move(board, cur)
        else:
            pos = player_L0(board, cur)
            if debug:
                print(f"Bot plays {pos}")
        place(board, pos, cur)
        show_board(board)
        if is_win(board, cur):
            print(f"Player {cur} wins!")
            return cur
        if 0 not in board:
            print("Draw.")
            return 0
        cur = 2 if cur == 1 else 1

if __name__ == "__main__":
    play_with_human(1)

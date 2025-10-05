# ttt_cli.py
from __future__ import annotations

import sys
from typing import List

from show_board import show_board
from is_win import is_win

HELP = """\
Usage:
  python -m Python.src.ttt_cli "<board9>" <player>
  or
  python Python/src/ttt_cli.py "<board9>" <player>

Examples:
  python Python/src/ttt_cli.py "[1,1,1,0,2,2,2,0,1]" 1
  python Python/src/ttt_cli.py "[0,1,2,1,2,0,2,0,1]" 2

board9 is a Python literal list of 9 ints in {0,1,2};
player is 1 (O) or 2 (X).
------------------------------------------------------
用法同上；board9 是长度为 9 的 0/1/2 列表字面量，player 为 1 或 2。
"""

def main(argv: List[str]) -> int:
    if len(argv) != 3:
        print(HELP)
        return 2
    try:
        board = eval(argv[1], {"__builtins__": {}})  
    except Exception:
        print("Invalid board literal. / 无法解析的棋盘字面量。")
        return 2
    try:
        player = int(argv[2])
    except Exception:
        print("Invalid player. Use 1 or 2. / 无效玩家编号，请用 1 或 2。")
        return 2

    # Show board / 打印棋盘
    show_board(board)
    print("---")

    if is_win(board, player):
        print(f"Player {player} wins. / 玩家 {player} 获胜。")
    else:
        print(f"No win for player {player}. / 玩家 {player} 未三连。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

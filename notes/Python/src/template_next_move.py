# template_next_move.py

from __future__ import annotations
from typing import List

def M22W0000(board: List[int], player: int) -> int:
    """
    Return the next move index (0..8) for Tic-Tac-Toe using Negamax with alpha-beta pruning.
    使用带 alpha-beta 剪枝的 Negamax 搜索返回下一步（0..8）。
    All helpers are defined locally inside this function per the slide requirement.
    按讲义要求，所有辅助对象（函数/数据）均定义在本函数内部。

    Board encoding / 棋盘编码：长度 9 列表，值域 {0:'-', 1:'O', 2:'X'}；player ∈ {1,2}
    """
    # ---- Local helpers / 本地辅助 ----
    WIN_LINES = (
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6),
    )

    def is_win(b, p):
        # Check any winning triple equals p / 任一三连等于 p
        for a,b_,c in WIN_LINES:
            if b[a] == b[b_] == b[c] == p:
                return True
        return False

    def legal_moves(b):
        # Empty cells / 空位索引
        return [i for i,v in enumerate(b) if v == 0]

    def full(b):
        return 0 not in b

    def evaluate_terminal(b, me, depth):
        # +10 for my win, -10 for my loss, 0 draw; depth tie-break (sooner win is better)
        # 自胜 +10，己负 -10，平局 0；加入深度微调（越早胜分数越大）
        opp = 2 if me == 1 else 1
        if is_win(b, me):
            return 10 - depth
        if is_win(b, opp):
            return depth - 10
        return 0

    # Move ordering heuristic / 着法排序启发（中>角>边）
    ORDER = [4,0,2,6,8,1,3,5,7]

    # ---- Negamax with alpha-beta / Negamax + αβ 剪枝 ----
    def negamax(b, me, turn, alpha, beta, depth):
        # Terminal tests / 终局检测
        score = evaluate_terminal(b, me, depth)
        if score != 0 or full(b):
            return score, -1

        best_score = -10**9
        best_move = -1
        # Order moves / 按启发顺序遍历走法
        for m in [m for m in ORDER if b[m] == 0]:
            b[m] = turn
            # Switch perspective: score for 'me' equals negative of opponent's score
            # 视角切换：我方评分 = 对手评分的相反数
            opp = 2 if turn == 1 else 1
            val, _ = negamax(b, me, opp, -beta, -alpha, depth+1)
            val = -val
            b[m] = 0

            if val > best_score:
                best_score, best_move = val, m
            if best_score > alpha:
                alpha = best_score
            if alpha >= beta:
                break  # alpha-beta prune / αβ 剪枝
        return best_score, best_move

    # ---- Entry ----
    # Basic validation / 基本校验
    if board is None or len(board) != 9:
        raise ValueError("board must be a list of length 9")
    if player not in (1,2):
        raise ValueError("player must be 1 or 2")
    if not legal_moves(board):
        raise ValueError("no legal moves")

    # Decide next move / 计算下一手
    score, move = negamax(board[:], player, player, -10**9, 10**9, 0)
    return move


if __name__ == "__main__":
    # Minimal smoke tests / 最小对拍
    # Immediate win
    b = [1,1,0, 2,2,0, 0,0,0]
    print("move:", M22W0000(b, 1))  # expect 2 to win
    # Block opponent
    b = [2,2,0, 1,0,0, 0,0,0]
    print("move:", M22W0000(b, 1))  # expect 2 to block at 2

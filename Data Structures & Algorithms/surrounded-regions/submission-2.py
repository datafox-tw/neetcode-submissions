from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        q = deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1) 把所有「邊界上的 O」丟進 queue，並標成安全(例如用 '#')
        def add_if_O(r, c):
            if board[r][c] == "O":
                board[r][c] = "#"
                q.append((r, c))

        for c in range(C):
            add_if_O(0, c)
            add_if_O(R - 1, c)
        for r in range(R):
            add_if_O(r, 0)
            add_if_O(r, C - 1)

        # 2) 從邊界 O 擴散：所有連到邊界的 O 都標成 '#'
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))

        # 3) 收尾：沒被標到的 O 是被包圍的，翻成 X；'#' 改回 O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

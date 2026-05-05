class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        if len(word) > R * C:
            return False

        used = [[False]*C for _ in range(R)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r: int, c: int, pos: int) -> bool:
            # 已經把 word[0..pos-1] 都匹配完了，接下來要匹配 word[pos]
            if pos == len(word):
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not used[nr][nc] and board[nr][nc] == word[pos]:
                    used[nr][nc] = True
                    if dfs(nr, nc, pos + 1):
                        return True
                    used[nr][nc] = False
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    used[i][j] = False

        return False

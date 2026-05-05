from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # 1) 把所有寶藏(0)當作 BFS 起點
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) 多源 BFS：從所有 0 同時往外擴
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 只能走到 land(INF)；水(-1)不走；已經是0或已填距離也不走
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        #這題用directions感覺比較順
        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            #q:參觀每個可能點，每次都是從自己出發向外擴散直到遇到第一個0
            q = deque([(r, c)])
            #已經走過的map，雖然有inorder版本但還是這版比較適合我
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in dirc:
                        nr, nc = row + dr, col + dc
                        #如果這個點不是0而且沒有撞牆和撞海，那就有繼續往下走的潛力
                        # 1. value正確不會到grid外面
                        # 2. 這個點不是海也不是寶藏
                        # 3. 還沒造訪過
                        if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and
                            not visited[nr][nc]  
                        ):
                            visited[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return steps

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
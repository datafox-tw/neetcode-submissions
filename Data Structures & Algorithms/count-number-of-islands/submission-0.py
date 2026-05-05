class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r: int, c: int) -> bool:
            # 清掉我遇到的那個1的所有鄰居（組成島的一部分）
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr, nc)
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    ans += 1
                    dfs(i, j)

        return ans

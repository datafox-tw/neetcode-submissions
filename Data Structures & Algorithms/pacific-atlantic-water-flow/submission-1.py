from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(starts):
            q = deque(starts)
            seen = set(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen:
                        # 倒著走：只能走到更高或同高
                        if heights[nr][nc] >= heights[r][c]:
                            seen.add((nr, nc))
                            q.append((nr, nc))
            return seen

        pacific_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic_starts = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

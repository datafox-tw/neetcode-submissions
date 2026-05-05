class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # 1) 把所有爛水果(2)當作 BFS 起點
        # 1.1) 如果完全沒有水果是return 0
        zero_count = 0
        one_count = 0
        two_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    two_count += 1
                elif grid[r][c] == 1:
                    one_count += 1
                else:
                    zero_count += 1
        if one_count>0 and two_count ==0:
            return -1
        if zero_count>0 and one_count == 0:
            return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) 多源 BFS：從所有 2 同時往外擴，把1變成2，然後刪除舊的2其實就是deque那一套
        step = -1
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 只能走到 land(INF)；水(-1)不走；已經是0或已填距離也不走
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        one_count -= 1
                        q.append((nr, nc))
            step+=1
            print(step)
        # 最後掃描：如果擴散完還有剩下的新鮮水果就return -1
        if one_count >0:
            return -1
        return step
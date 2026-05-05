class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        is_touch_edge = []
        for i in range(R):
            is_touch_edge.append([False]*C)
        def dfs(r: int, c: int) -> bool:
            # 清掉我遇到的那個1的所有鄰居（組成島的一部分）
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # 之後在這個dfs新增的circles都是不能被異動的但還是要跑完偵測流程
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "O":
                    if (nr==0 or nr==R-1 or nc==0 or nc==C-1):
                        self.flag = True
                    self.circles.append((nr,nc))
                    board[nr][nc] = "#"
                    dfs(nr, nc)
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    self.flag = False
                    self.circles = [(i,j)]
                    if (i==0 or i==R-1 or j==0 or j==C-1):
                        self.flag = True
                    board[i][j] = "#"
                    dfs(i, j)
                    if self.flag:
                        for r,c in self.circles:
                            is_touch_edge[r][c] = True
                    #如果被檢測出連到邊界，這坨O不僅不用改成X也不用再次被審判
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == "#":
                    if is_touch_edge[i][j]:
                        board[i][j] = "O"
                    else:
                        board[i][j] = "X"
        print(board)

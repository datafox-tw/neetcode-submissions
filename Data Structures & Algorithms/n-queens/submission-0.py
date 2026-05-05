class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #核心：如何標記被佔領的區域？不是直接塗成黑色，而是用不同方式說明影響力，這樣比較好回撤
        cols = set()
        diag1 = set()
        diag2 = set()
        result = []
        board = [["."] * n for i in range(n)]
        cnt = 0
        def backtrack(row): # row代表的是現在是第幾層
            if row == n: # iterate到最下層
                ans = []
                for item in board:
                    ans.append("".join(item))
                result.append(ans)
                return
            #剩下就是檢查這層哪些合法，然後丟進去backtrack裡面
            for col in range(n):
                if col not in cols and row-col not in diag1 and row+col not in diag2:
                    cols.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)
                    board[row][col] = "Q"
                    backtrack(row + 1) #從第0層到第七層

                    #做對稱的事情
                    cols.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)
                    board[row][col] = "."
        backtrack(0)
        return result




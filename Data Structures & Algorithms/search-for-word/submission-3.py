class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        self.ans = False
        num_row = len(board)
        num_column = len(board[0])
        def backtrack(row,column,pos):
            print(path)
            if self.ans:
                return
            if pos == len(word):
                self.ans = True
                return
            if column>0 and board[row][column-1]==word[pos] and not used[row][column-1]: # if left exist
                path.append(board[row][column-1])
                used[row][column-1] = True
                backtrack(row,column-1,pos+1)
                path.pop()
                used[row][column-1] = False
            if column<len(board[0])-1 and board[row][column+1]==word[pos] and not used[row][column+1]: # if right exist
                used[row][column+1] = True
                path.append(board[row][column+1])
                backtrack(row,column+1,pos+1)
                path.pop()
                used[row][column+1] = False
            if row>0 and board[row-1][column]==word[pos]and not used[row-1][column]: # if above exist
                used[row-1][column] = True
                path.append(board[row-1][column])
                backtrack(row-1,column,pos+1)
                path.pop()
                used[row-1][column] = False
            if row<len(board)-1 and board[row+1][column]==word[pos] and not used[row+1][column]: # if below exist
                used[row+1][column] = True
                path.append(board[row+1][column])
                backtrack(row+1,column,pos+1)
                path.pop()
                used[row+1][column] = False
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(num_row):
            for j in range(num_column):
                if board[i][j]==word[0]:
                    used[i][j] = True
                    path.append(board[i][j])
                    backtrack(i,j,1)
                    path.pop()
                    used[i][j] = False
        return self.ans
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        from collections import Counter
        for row in board:
            cnt = Counter(row)
            for i in cnt:
                if cnt[i] > 1 and i != ".":
                    return False
        # check vertical
        for i in range(0,9):
            column = [sublist[i] for sublist in board]
            cnt = Counter(column)
            for i in cnt:
                if cnt[i] > 1 and i != ".":
                    return False
        # check 3*3
        for i in [0,3,6]:
            for j in [0,3,6]:
                items = []
                items.append(board[i][j])
                items.append(board[i][j+1])
                items.append(board[i][j+2])
                items.append(board[i+1][j])
                items.append(board[i+1][j+1])
                items.append(board[i+1][j+2])
                items.append(board[i+2][j])
                items.append(board[i+2][j+1])
                items.append(board[i+2][j+2])
                cnt = Counter(items)
                for k in cnt:
                    if cnt[k] > 1 and k != ".":
                        return False
        return True

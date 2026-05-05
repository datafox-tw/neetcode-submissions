class Solution:
    def isValidSudoku(self, board):
        # 檢查一組 9 格是否有重複（忽略 '.')
        def valid_unit(unit):
            seen = set()
            for x in unit:
                if x == '.':
                    continue
                if x in seen:
                    return False
                seen.add(x)
            return True

        # rows
        for r in range(9):
            if not valid_unit(board[r]):
                return False

        # cols
        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not valid_unit(col):
                return False

        # 3x3 boxes
        for br in (0, 3, 6):
            for bc in (0, 3, 6):
                box = [board[r][c] for r in range(br, br + 3)
                                  for c in range(bc, bc + 3)]
                if not valid_unit(box):
                    return False

        return True

class Solution:
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        
        # 只要邊界沒有交錯，就繼續繞圈
        while top <= bottom and left <= right:
            
            # 1. 向右走 
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 
            
            # 2. 向下走
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            # --- 注意：因為 top 或 right 剛更新過，需要檢查是否還有剩餘行列 ---
            if not (top <= bottom and left <= right):
                break
                
            # 3. 向左走
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1 
            
            # 4. 向上走
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 
            
        return res
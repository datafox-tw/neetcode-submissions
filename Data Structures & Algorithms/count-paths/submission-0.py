class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy as np
        matrix = np.ones((m, n))
        print(matrix)
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return int(matrix[-1][-1])

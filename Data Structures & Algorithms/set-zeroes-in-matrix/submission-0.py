class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zero_point = []
        for row in range(n):
            for column in range(m):
                if matrix[row][column] == 0:
                    zero_point.append((row,column))
        for i,j in zero_point:
            for row in range(n):
                matrix[row][j] = 0
            for column in range(m):
                matrix[i][column] = 0
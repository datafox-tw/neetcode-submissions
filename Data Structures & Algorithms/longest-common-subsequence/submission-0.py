class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import numpy as np
        dp = np.zeros((len(text1)+1, len(text2)+1))

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return int(dp[0][0])
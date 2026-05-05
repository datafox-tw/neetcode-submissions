class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci
        # if n <= 2:
        #     return n
        # bottom up：從基礎做起
        # dp = [1,2]
        # for i in range(2, n):
        #     dp.append(dp[i-1]+dp[i-2])
        # return dp[-1]
        
        # top down:
        # cache 或者是memo就是放需要的東西
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)